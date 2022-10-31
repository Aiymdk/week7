import uid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        self.id = str(uuid.uuid4())
        
people = [Person("Aru",19), Person("Tomi",18), Person("Asel",15)]

def find_person(id):
    for person in people:
        if person.id == id:
            return person
        return None
    
app= FastAPI()

@app.get("/")
async def main():
    return FileResponse("public/index.html")

@app.get("/api/users")
def get_people():
    return people

@app.get("/api/users/{id}")
def get_person(id):

    person = find_person(id)
    print(person)
    if person==None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    return person

@app.post("/api/users")
def create_person(data = body()):
    person = Person(data["name"], data["age"])
    people.append(person)
    return person

@app.put("/api/users")
def edit_person(data = body()):
    person = find_person(data["id"])
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    person.age = data["age"]
    person.name = data["name"]
    return person

@app.delete("/api/users/{id}")
def delete_person(id):
    person = find_person(id)
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    people.remove(person)
    return 
