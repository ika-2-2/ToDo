from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    is_done: bool

todos: List[Todo] = []

#データの受け取り
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

#データの追加
@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    #同じIDがあったら追加できないように確認
    for i in todos:
        if i.id == todo.id:
            raise HTTPException(status_code=400, detail="baka mou id aru")
    todos.append(todo)
    return todo

#データの削除
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    #今あるToDoリストに削除したいIDと同じIDがあれば削除
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            return todos.pop(i)
    raise HTTPException(status_code=404, detail="sono id ha naiyo!")

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    is_done: bool = None

#データの編集
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    #リクエストと同じIDを探して、todoupdateが空で無ければ編集する
    for todo in todos:
        if todo.id == todo_id:
            if todo_update.title is not None:
                todo.title = todo_update.title
            if todo_update.is_done is not None:
                todo.is_done = todo_update.is_done
            return todo
    raise HTTPException(status_code=404, detail="sono id ha naiyo!")