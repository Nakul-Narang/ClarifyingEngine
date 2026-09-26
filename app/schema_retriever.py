from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectoParams,PointStruct
from litellm import embedding
from app.config import settings
from app.database import extract_database_schema
COLLECTION_NAME="schema_tables"
