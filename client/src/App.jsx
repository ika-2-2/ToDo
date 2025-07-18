import React, { useEffect } from "react";
import "./App.css";
import MemoItem from "./components/MemoItem";
import MemoPost from "./components/MemoPost";
import { MemoProvider, useMemos } from "./components/MemoContext";

function MainContent() {
  const { memos, setMemos } = useMemos();

  // メモ一覧取得
  useEffect(() => {
    fetch("http://localhost:8000/todos")
      .then((res) => res.json())
      .then((data) => setMemos(data))
      .catch((err) => {
        console.error("メモとってこれなかった", err);
      });
  }, [setMemos]);

  // メモ追加後に一覧を再取得
  const handleAddMemo = () => {
    fetch("http://localhost:8000/todos")
      .then((res) => res.json())
      .then((data) => setMemos(data));
  };

  return (
    <div className="sitaji">
      <h1 className="headline">ToDoアプリ</h1>
      <section className="memo-list">
        メモ一覧
        <ul className="memo-list-content">
          {memos.map((memo) => (
            <MemoItem
              key={memo.id}
              id={memo.id}
              text={memo.title}
              onDelete={handleAddMemo}
              onEdit={handleAddMemo}
            />
          ))}
        </ul>
      </section>
      <MemoPost onAdd={handleAddMemo} />
    </div>
  );
}

function App() {
  return (
    <MemoProvider>
      <MainContent />
    </MemoProvider>
  );
}

export default App;
