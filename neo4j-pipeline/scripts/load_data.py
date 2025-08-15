from neo4j import GraphDatabase

# Replace with your password
URI = "bolt://neo4j:7687"
AUTH = ("neo4j", "inglourious_basterds")

driver = GraphDatabase.driver(URI, auth=AUTH)

def add_sample_data(tx):
    tx.run("""
        CREATE (aniket:Person {name: 'Aniket', age: 30})
        CREATE (shankar:Person {name: 'Shankar', age: 25})
        CREATE (nitin:Person {name: 'Nitin', age: 27})
        CREATE (aniket)-[:KNOWS]->(shankar)
        CREATE (shankar)-[:KNOWS]->(nitin)
        CREATE (nitin)-[:KNOWS]->(aniket)
    """)

with driver.session() as session:
    session.execute_write(add_sample_data)

print("✅ Sample data inserted successfully.")

driver.close()
