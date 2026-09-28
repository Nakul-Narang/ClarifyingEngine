import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

from app.config import settings

connection_pool = None


def init_db_pool():
  global connection_pool
  if connection_pool is None:
    if not settings.DATABASE_URL:
      raise ValueError("Database URL is not set")
    connection_pool = pool.ThreadedConnectionPool(
      minconn=1,
      maxconn=10,
      dsn=settings.DATABASE_URL,
    )


def get_db_connection():
  if connection_pool is None:
    init_db_pool()
  return connection_pool.getconn()


def get_connection():
  return get_db_connection()


def release_db_connection(conn):
  if connection_pool is not None and conn is not None:
    connection_pool.putconn(conn)


def execute_read_query(sql_query: str) -> list[dict]:
  conn = get_db_connection()
  try:
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(sql_query)
      return [dict(row) for row in cursor.fetchall()]
  finally:
    release_db_connection(conn)


def extract_database_schema() -> dict[str, list[str]]:
  schema_query = """
    SELECT table_name, column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
    ORDER BY table_name, ordinal_position
  """
  conn = get_db_connection()
  tables = {}
  try:
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
      cursor.execute(schema_query)
      for row in cursor.fetchall():
        table_name = row["table_name"]
        tables.setdefault(table_name, []).append(
          f"{row['column_name']}({row['data_type']})"
        )
  finally:
    release_db_connection(conn)
  return tables
