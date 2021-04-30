from fastapi import FastAPI

app = FastAPI()

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}

@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}
    

