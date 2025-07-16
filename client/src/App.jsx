import React, { memo, useEffect, useState } from "react";
import "./App.css";
import MemoItem from "./components/MemoItem";

function App() {
  const [memos, setMemos] = useState([]);

  function handleEdit(id, newTitle) {
    fetch(`http://localhost:8000/todos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title: newTitle }),
    })
      .then((res) => res.json())
      .then((updatedMemo) => {
        setMemos((prevMemos) =>
          prevMemos.map((memo) =>
            memo.id === updatedMemo.id ? updatedMemo : memo
          )
        );
      });
  }

  useEffect(() => {
    fetch("http://localhost:8000/todos")
      .then((res) => res.json())
      .then((data) => setMemos(data))
      .catch((err) => {
        console.error("メモとってこれなかった", err);
      });
  }, []);

  return (
    <>
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
                onEdit={handleEdit}
                onDelete={() => {}}
              />
            ))}
          </ul>
        </section>
        <section className="memo-input">
          メモの追加
          <textarea
            name="textarea"
            id="textarea"
            placeholder="メモを入力してください"
          ></textarea>
          <button>追加</button>
        </section>
      </div>
    </>
  );
}

export default App;
