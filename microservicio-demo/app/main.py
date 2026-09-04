from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Microservicio activo y funcionando correctamente", "status": "OK"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}!"}

@app.get("/suma/{a}/{b}")
def sumar (a: int, b: int):
    return {"resultado": a + b}