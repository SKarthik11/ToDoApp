from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return "GDSC VIT"

Todos = {
    1:{
        "title" : "Finish DA",
        "completed" : False,
    },
    2:{
        "title" : "Study for CAT",
        "completed" : False,
    },
}

#Request Body Schema
class TodoItem(BaseModel):
    title:str
    completed:bool

#View all Todo Items
@app.get("/todos", status_code=status.HTTP_200_OK)
def get_all_todo_items(title:str=""):
    results = {}
    if title!="" or title !=None:
        for id in Todos:
            if title in Todos[id]["title"]:
                results[id] = Todos[id]
            else:
                results = Todos
    return Todos

#View Single Todo Item
@app.get("/todos/{id}", status_code=status.HTTP_200_OK)
def get_todo_items(id : int):
    if id in Todos:
        return Todos[id]
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item not found")


#Create new items
@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo_items(todo_item:TodoItem):
    id = max(Todos)+1
    Todos[id] = todo_item.dict()
    return Todos[id]

#Update Todo Items
@app.put("/todos/{id}", status_code=status.HTTP_200_OK)
def update_todo_item(id : int, todo_item : TodoItem):
    if id in Todos:
        Todos[id] = todo_item.dict()
        return Todos[id]
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item not found") 

#Delete Todos Items
@app.delete("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_items(id: int):
    if id in Todos:
        Todos.pop(id)
        return
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Item not found") 