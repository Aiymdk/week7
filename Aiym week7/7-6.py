from fastapi import FastAPI
app = FastAPI()

@app.get("/users")

def get_model(name, age):
    return {"user_name": name, "user_age": age}
