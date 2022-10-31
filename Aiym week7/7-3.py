from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 

app = FastAPI()

@app.get("/")
def root():
    data = "<h2> Hello World!</h2>"
    return HTMLResponse (content=data)
