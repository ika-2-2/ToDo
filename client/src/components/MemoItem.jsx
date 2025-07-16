import { useState } from "react";

const MemoItem = ({ id, text, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(text);

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

  return (
    <li className="memo-list-item">
      {isEditing ? (
        <>
          <input
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
          />
          <button
            onClick={() => {
              handleEdit(id, editText);
              setIsEditing(false);
            }}
          >
            保存
          </button>
          <button onClick={() => setIsEditing(false)}>キャンセル</button>
        </>
      ) : (
        <>
          <span className="memo-text">{text}</span>
          <div className="memo-buttons">
            <button className="edit-btn" onClick={() => setIsEditing(true)}>
              編集
            </button>
            <button className="delete-btn" onClick={onDelete}>
              削除
            </button>
          </div>
        </>
      )}
    </li>
  );
};

export default MemoItem;
