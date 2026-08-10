print("Hello world")

# Create Cosmos DB client
cosmos_client = CosmosClient(
    COSMOS_ENDPOINT,
    COSMOS_KEY
)

# Get database
database = cosmos_client.get_database_client(
    COSMOS_DATABASE
)

# Get container
container = database.get_container_client(
    COSMOS_CONTAINER
)

