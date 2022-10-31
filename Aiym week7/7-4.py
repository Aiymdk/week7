import fastapi
from fastapi.responses import FileResponse

app = fastapi()

@app.get("/")
def root():
    return FileResponse ("index.html")
