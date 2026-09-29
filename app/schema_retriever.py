from qdrant_client import QdrantClient
from qdrant_client.models import Distance,VectoParams,PointStruct
from litellm import embedding
from app.config import settings
from app.database import extract_database_schema
COLLECTION_NAME="schema_vectors"
def get_qdrant_client() -> QdrantClient:
   if settings.QDRANT_URL :
      return QdrantClient(url=settings.QDRANT_URL,api_key=settings.QDRANT_API_KEY)
   return QdrantClient(":memory:")
def get_text_embedding(text:str)->list[float]:
   response=embedding(model="text-embedding-3-small",input=[text])
   return response.data[0].["embedding"]
def index_database_schema():
   client =get_qdrant_client()
   schemas=extract_database_schema()
   if not schemas:
      print("[Warning]No tables found in database to index")
      return
   vector_size=1536
   client.recreate_collection(
      collection_name=COLLECTION_NAME
      vectors_config=VectorParams(size=vector_size,distance=Distance.COSINE)

   )
   points=[]
   for item in schemas:
      tale_name=item["table_name"]
      raw_schema=item["raw_schema"]
      

