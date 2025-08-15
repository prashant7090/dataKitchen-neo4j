# 🧪 DataKitchen + Neo4j + Python DataOps Pipeline

This project demonstrates a local DataOps pipeline integrating:
- Python scripts
- Neo4j graph database
- DataKitchen TestGen

Everything runs in Docker for easy local development and testing.

---

## 🧰 Tech Stack

- Docker + Docker Compose
- Neo4j (v5.20)
- Python (v3.10)
- DataKitchen TestGen
- Data mounted via volumes for live development

---

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:prashant7090/dataKitchen-neo4j.git
cd dataKitchen-neo4j/neo4j-pipeline

2. Start Docker Containers

docker-compose up -d

3. Install Python Dependencies

docker exec -it python-scripts bash
pip install -r dependency.txt

4. Setup DataKitchen  - Outisde of container.

git clone https://github.com/DataKitchen/dataops-testgen.git .dk
cd .dk
docker network create datakitchen-network || true
docker-compose up -d


