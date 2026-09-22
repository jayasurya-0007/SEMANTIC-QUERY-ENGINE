import { useEffect, useMemo, useState } from "react";
import { askQuery, getSources, tts, uploadFile, uploadText, uploadUrl } from "../services/api";

export default function Layout() {
  const [sources, setSources] = useState([]);
  const [chat, setChat] = useState([]);
  const [question, setQuestion] = useState("");
  const [textInput, setTextInput] = useState("");
  const [urlInput, setUrlInput] = useState("");
  const [typing, setTyping] = useState(false);
  const [status, setStatus] = useState("");

  const refreshSources = async () => {
    const response = await getSources();
    setSources(response.data);
  };

  useEffect(() => {
    refreshSources().catch(() => setStatus("Failed to load sources"));
  }, []);

  const submitQuestion = async () => {
    if (!question.trim()) return;
    const q = question.trim();
    setQuestion("");
    setChat((prev) => [...prev, { role: "user", content: q }]);
    setTyping(true);
    try {
      const response = await askQuery({ question: q, top_k: 4 });
      setChat((prev) => [...prev, { role: "assistant", content: response.data.answer, sources: response.data.sources }]);
    } catch (err) {
      setChat((prev) => [...prev, { role: "assistant", content: err?.response?.data?.detail || "Query failed" }]);
    } finally {
      setTyping(false);
    }
  };

  const onUploadText = async () => {
    await uploadText(textInput);
    setTextInput("");
    await refreshSources();
  };

  const onUploadUrl = async () => {
    await uploadUrl(urlInput);
    setUrlInput("");
    await refreshSources();
  };

  const onUploadFile = async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    await uploadFile(file);
    await refreshSources();
  };

  const playAudio = async (text) => {
    const response = await tts(text);
    const url = URL.createObjectURL(response.data);
    const audio = new Audio(url);
    audio.play();
  };

  const sourceCountLabel = useMemo(() => `${sources.length} source(s)`, [sources.length]);

  return (
    <div className="app-grid">
      <aside className="panel left">
        <h3>Sources</h3>
        <p className="muted">{sourceCountLabel}</p>
        <textarea placeholder="Paste text..." value={textInput} onChange={(e) => setTextInput(e.target.value)} />
        <button onClick={onUploadText}>Add Text</button>
        <input placeholder="https://example.com/article" value={urlInput} onChange={(e) => setUrlInput(e.target.value)} />
        <button onClick={onUploadUrl}>Add URL</button>
        <input type="file" accept=".pdf,.docx,.txt" onChange={onUploadFile} />
        <ul className="source-list">
          {sources.map((item) => (
            <li key={item.id}>
              <strong>{item.name}</strong>
              <span>{item.source_type}</span>
            </li>
          ))}
        </ul>
      </aside>

      <main className="panel center">
        <h3>Chat</h3>
        <div className="chat-box">
          {chat.map((msg, index) => (
            <div key={index} className={`bubble ${msg.role}`}>
              <p>{msg.content}</p>
              {msg.sources?.length > 0 && (
                <small>
                  Sources:{" "}
                  {msg.sources.map((s, i) => (
                    <span key={i}>[{s.meta?.source_id}] </span>
                  ))}
                </small>
              )}
            </div>
          ))}
          {typing && <div className="bubble assistant typing">Assistant is thinking...</div>}
        </div>
        <div className="chat-input">
          <input value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask based on your sources..." />
          <button onClick={submitQuestion}>Send</button>
        </div>
      </main>

      <aside className="panel right">
        <h3>Tools</h3>
        <p className="muted">Text to Speech</p>
        <button
          onClick={() => {
            const last = [...chat].reverse().find((c) => c.role === "assistant");
            if (last) playAudio(last.content);
          }}
        >
          Play Audio
        </button>
        {status && <p className="error">{status}</p>}
      </aside>
    </div>
  );
}
