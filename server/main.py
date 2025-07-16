from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware



DB_url = "sqlite:///./todos.db"

engine = create_engine(DB_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class TodoDB(Base):
    __tablename__="todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    is_done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

class Todo(BaseModel):
    id: int
    title: str
    is_done: bool = False

    class Config:
        orm_mode = True

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    is_done: bool = None



app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#データの受け取り
@app.get("/todos", response_model=List[Todo])
def get_todos():
    db = SessionLocal()
    todos = db.query(TodoDB).all()
    db.close()
    return todos


#データの追加
@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    db = SessionLocal()
    #同じIDがあったら追加できないように確認
    existing_todo = db.query(TodoDB).filter(TodoDB.id == todo.id).first()
    if existing_todo != None:
        db.close()
        raise HTTPException(status_code=400, detail="sono id sudeni aru!")

    db_todo = TodoDB(id=todo.id, title=todo.title, is_done=todo.is_done)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo


#データの削除
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    #今あるToDoリストに削除したいIDと同じIDがあれば削除
    todo = db.query(TodoDB).filter(TodoDB.id == todo.id).first()
    if todo == None:
        db.close()
        raise HTTPException(status_code=404, detail="sono id ha naiyo!")

    db.delete(todo)
    db.commit()
    db.close()
    return todo


#データの編集
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoUpdate):
    #リクエストと同じIDを探して、todoupdateが空でなければ編集する
    db = SessionLocal()
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()
    if todo == None:
        db.close()
        raise HTTPException(status_code=404, detail="sono id ha naiyo!")

    if todo_update.title != None:
        todo.title = todo_update.title
    if todo_update.is_done != None:
        todo.is_done = todo_update.is_done

    db.commit()
    db.refresh()
    db.close()
    return todo