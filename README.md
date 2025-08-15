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
mkdir testgen-setup
cd neo4j-pipeline/testgen-setup
curl -O https://raw.githubusercontent.com/DataKitchen/data-observability-installer/main/dk-installer.py
python3 dk-installer.py tg install
neo4j-pipeline/testgen-setup/dk-tg-credentials.txt

# If TestGen is not already running (after reboot or stopping containers)
cd neo4j-pipeline/testgen-setup
python3 dk-installer.py tg start




