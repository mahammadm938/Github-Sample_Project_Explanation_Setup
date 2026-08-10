print("Hello world")

import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

database = client.get_database_client("PracticeDB")
container = database.get_container_client("Users")


name = input("Enter your name: ")

item = {
    "id": name,
    "name": name
}

container.upsert_item(item)

print(f"Hello {name}!")
print("Welcome to Python World")
print("Data saved to Cosmos DB!")
import asyncio

async def hello_world():
    print("Hello, World!")

    await asyncio.sleep(1)

    print("Welcome to Python World")


asyncio.run(hello_world())
