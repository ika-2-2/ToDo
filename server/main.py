from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Generator
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware
from contextlib import contextmanager


#データベース設定
DB_url = "sqlite:///./todos.db"
engine = create_engine(DB_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#データベースモデル
class TodoDB(Base):
    __tablename__="todos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    is_done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

#Pydanticモデル
class Todo(BaseModel):
    id: int
    title: str
    is_done: bool = False

    class Config:
        orm_mode = True

class Create_Todo(BaseModel):
    title: str

class Update_Todo(BaseModel):
    title: Optional[str] = None
    is_done: Optional[bool] = None

@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#データベース操作をカプセル化
class TodoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[TodoDB]:
        return self.db.query(TodoDB).all()

    def get_by_id(self, todo_id: int) -> Optional[TodoDB]:
        return self.db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    def create(self, todo: Create_Todo) -> TodoDB:
        db_todo = TodoDB(title=todo.title, is_done=False)
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def delete(self, todo: TodoDB) -> TodoDB:
        self.db.delete(todo)
        self.db.commit()
        return todo

    def update(self, todo: TodoDB, todo_update: Update_Todo) ->TodoDB:

        if todo_update.title != None:
            todo.title = todo_update.title
        if todo_update.is_done != None:
            todo.is_done = todo_update.is_done
        self.db.commit()
        self.db.refresh(todo)
        return todo

#fastAPIインスタンス化
app = FastAPI()

#CORSの許可
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
    with get_db() as db:
        repo = TodoRepository(db)
        return repo.get_all()

#データの追加
@app.post("/todos", response_model=Todo)
def create_todo(todo: Create_Todo):
    with get_db() as db:
        repo = TodoRepository(db)
        return repo.create(todo)

#データの削除
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    with get_db() as db:
        repo = TodoRepository(db)
        todo = repo.get_by_id(todo_id)
        if todo == None:
            raise HTTPException(status_code=404, detail="sono id ha naiyo")
        return repo.delete(todo)

#データの編集
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: Update_Todo):
    #リクエストと同じIDを探して、Update_Todoが空でなければ編集する
    with get_db() as db:
        repo = TodoRepository(db)
        todo = repo.get_by_id(todo_id)
        if todo == None:
            raise HTTPException(status_code=404, detail="sono id ha naiyo")
        return repo.update(todo, todo_update)