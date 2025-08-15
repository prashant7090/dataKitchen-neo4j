from neo4j import GraphDatabase

# Use Docker service name for Neo4j host
uri = "bolt://neo4j:7687"
auth = ("neo4j", "inglourious_basterds")

driver = GraphDatabase.driver(uri, auth=auth)

def check_neo4j_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Neo4j is connected!' AS message")
        print(result.single()["message"])

check_neo4j_connection()
