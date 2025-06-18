from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API de monitoreo eléctrico"}

@app.post("/sensor-data")
async def receive_data(data: dict):
    print(f"Datos recibidos: {data}")
    return {"status": "success"}
