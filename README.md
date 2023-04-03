# fastapi-AMS

## Prequisites
    [ ] Ubuntu 
    [ ] Python 3.9
    [ ] PostgreSQL

## How to start

1. Install Dependencies:
```python
pip install -r requirements
```

2. Add a `.env` file as shown in `.env.example`

3. Create postgres user or use existing by editing `.env`
```bash
sudo -u postgres psql
ALTER USER postgres PASSWORD 'abcd';
```
4. Run the server with univorn
```bash
uvicorn app:app --port 8000 --reload
```
4. Run the server with docker
```bash
docker compose up
```
5. For Swagger UI, with the given link add "/docs", i.e., http://localhost:8010/docs  
Here you can test the api endpoints.




