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
