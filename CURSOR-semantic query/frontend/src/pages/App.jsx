import { useEffect, useState } from "react";
import AuthPanel from "../components/AuthPanel";
import Layout from "../components/Layout";
import { setAuthToken } from "../services/api";

export default function App() {
  const [authed, setAuthed] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setAuthToken(token);
      setAuthed(true);
    }
  }, []);

  return authed ? <Layout /> : <AuthPanel onAuthed={() => setAuthed(true)} />;
}
