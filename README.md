# Installation
## Local
Create `.env` file
```bash
vim .env
```

Make sure you have added the following env variables (necessary to connect to the database)
1. `DB_NAME`
2. `DB_USER`
3. `DB_PASS`
4. `DB_HOST`
5. `DB_POST`

Create virtual environment in the project root directory
```bash
python3 -m venv .
```

Activate the virtual env
```bash
source ./bin/activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run the `dev` server locally
```bash
fastapi dev app/main.py
```

## Production
Create docker image (make sure you have docker and the docker process/daemon is runnning)
```
docker build -t kaaj-fastapi .
```

Run the server using docker
```
docker run -p 80:80 kaaj-fastapi
```
