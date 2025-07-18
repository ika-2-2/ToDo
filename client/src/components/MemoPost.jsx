import { createContext, useContext, useState } from "react";

const MemoContext = createContext();

export const useMemos = () => useContext(MemoContext);

export const MemoProvider = ({ children }) => {
  const [memos, setMemos] = useState([]);
  return (
    <MemoContext.Provider value={{ memos, setMemos }}>
      {children}
    </MemoContext.Provider>
  );
};

const MemoPost = ({ onAdd }) => {
  const [text, setText] = useState("");

  const handleAdd = () => {
    if (!text.trim()) return;
    fetch("http://localhost:8000/todos", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({ title: text }),
    })
      .then((res) => res.json())
      .then(() => {
        setText("");
        if (onAdd) onAdd();
      });
  };

  return (
    <section className="memo-input">
      メモの追加
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="メモを入力してください"
      ></textarea>
      <button onClick={handleAdd}>追加</button>
    </section>
  );
};

export default MemoPost;
