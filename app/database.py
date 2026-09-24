
import psycopg2
from psycopg2,extras import RealDictCursor
from app.config import settings 
def get_connection():
  """Estabilish connection"""
  if not settings.DATABASE_URL:
    raise ValueError("Datsbase Url is not set as environment variables")
  return psycopg2.connect(settings.DATABASE_URL)
def execute_read_query(sql_query:str):
  """Execute the query"""
  conn=get_connection()
  try:
    with conn.cursor(cursor_factory=RealDictCursor)as cursor:
      cursor.execute(sql_query)
      results=cursor.fetchall()
      return [dict(row) for row in results ]
  finally:
    conn.close()
def extract_database_schema()->dict:
  """Extract table ,data"""
  schema_query="""
  SELECT 
      table_name,
      column_name,
      data_type
  FROM information_schema.columns
  WHERE table_schema='public'
  ORDER BY table_name,ordinal_position"""
  conn=get_connection()
  tables={}
  try: 
    with conn.cursor(cursor_factory=RealDictCursor)as Cursor:
      cursor.execute(schema_query)
      for row in cursor.fetchall():
        t_name=row["table_name"]
        if t_name not in tables:
          tables[t_name]=[]
        tables[t_name].append(f"{row['column_name']}({row['data_type']})")
        
          
          
        
  finally:
    conn.close()
  return tables

      
  
  
  
    
