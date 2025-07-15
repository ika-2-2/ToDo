import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import MemoItem from "./components/MemoItem";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="sitaji">
        <h1 className="headline">ToDoアプリ</h1>
        <section className="memo-list">
          メモ一覧
          <ul className="memo-list-content">
            <MemoItem text="メモ1" onEdit={() => {}} onDelete={() => {}} />
            <MemoItem text="メモ2" onEdit={() => {}} onDelete={() => {}} />
            <MemoItem text="メモ3" onEdit={() => {}} onDelete={() => {}} />
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
