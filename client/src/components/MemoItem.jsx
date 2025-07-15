const MemoItem = ({ text, onEdit, onDelete }) => (
  <li className="memo-list-item">
    <span className="memo-text">{text}</span>
    <div className="memo-buttons">
      <button className="edit-btn" onClick={onEdit}>
        編集
      </button>
      <button className="delete-btn" onClick={onDelete}>
        削除
      </button>
    </div>
  </li>
);

export default MemoItem;
