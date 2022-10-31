from fastapi import FastAPI, form
from fastapi.responses import FileResponse

app= FastAPI()

@app.get("/")
def root():
    return FileResponse("public/index4.html")

@app.post("/postdata")
def postdata(username:str = form(),
languages:list =form()):
    return {"name": username, "languages": languages}
