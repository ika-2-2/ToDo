import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="sitaji">
        <h1 className="headline">ToDoアプリ</h1>
        <section className="memo-list">
          メモ一覧
          <ul className="memo-list-content">
            <li className="memo-list-item">メモ1</li>
            <li className="memo-list-item">メモ2</li>
            <li className="memo-list-item">メモ3</li>
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
