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
      text_to_embed=f"Table name:{tale_name}\nSchema:\n{raw_schema}"
      vector =get_text_embedding(text_to_embed)
      point_id=str(uuid.uuid5(uid.NAMESPACE_DNS,tale_name))
      points.append(PointStruct(id=point_id, vector=vector,payload ={"table_name":tale_name,"raw_schema":raw_schema}
))
client.upsert(collection_name=COLLECTION_NAME,points=points)
print(f"[Success] Indexed{len(points)} database table schemas into Qdrant collection '{COLLECTION_NAME}'.")
def retrieve_relevant_tables(user_query:str,top_k:int=3)->list[dict]:
 client=get_qdrant_client()
 query_vector=get_text_embedding(user_query)
 search_results=client.search(
   collection_name=COLLECTION_NAME,
   query_vector=query_vector,
   limit=top_k)
 return[{"table_name":hit.payload["tale_name"],
       "raw_schema":hit.payload["raw_schema"],
"score":hit.score}
for hit in search_results]



      
      
