from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
from ai71 import AI71 

""" CONNECT MONGODB SETUP """
# SERVER PUBLIC MONGO DB
uri = "mongodb+srv://falcon-hack:launchai-2024@cluster0.rymcrpi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client_db = MongoClient(uri)
dbName = "Cluster0"
collection = client_db[dbName]["trial"]
# Send a ping to confirm a successful connection
try:
    client_db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

""" CONNECT AI71 SETUP """
#AI71_API_KEY = "api71-api-a4e21705-d85c-47d8-8c9f-bbf7403654cf"
AI71_API_KEY = "api71-api-2a34d04e-d6cc-456a-aab6-ed890c8fe41c"
def generate_completion(system_prompt, user_prompt):
    output = ""
    for chunk in AI71(AI71_API_KEY).chat.completions.create(
        model="tiiuae/falcon-180b-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": user_prompt},
        ],
        stream=True,
    ):
        if chunk.choices[0].delta.content:
            output += (chunk.choices[0].delta.content)
    return output.rstrip().lstrip()