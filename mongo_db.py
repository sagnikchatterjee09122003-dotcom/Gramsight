
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

password = ""
safe_password = urllib.parse.quote_plus(password)
uri = f"mongodb+srv://Sagnik:{safe_password}@cluster0.5xbih08.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))

def connect(clent):
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


db = client['voting_system']
voters_collection = db['voters']

# --- DATA STRUCTURE (Your "Schema") ---
def add_voter(voter_id, name, has_voted=False):
    voter_data = {
        "voter_id": voter_id,
        "name": name,
        "has_voted": has_voted,
        "registration_date": "2026-04-30"
    }
    
    try:
        result = voters_collection.insert_one(voter_data)
        print(f"✅ Data added! Inserted ID: {result.inserted_id}")
    except Exception as e:
        print(f"❌ Failed to add data: {e}")

# Try adding a record
connect(client)
add_voter("V101", "Sagnik")