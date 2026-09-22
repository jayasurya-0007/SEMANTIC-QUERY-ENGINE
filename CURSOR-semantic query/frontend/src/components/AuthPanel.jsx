import { useState } from "react";
import { login, setAuthToken, signup } from "../services/api";

export default function AuthPanel({ onAuthed }) {
  const [isSignup, setIsSignup] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const submit = async (event) => {
    event.preventDefault();
    setError("");
    try {
      if (isSignup) {
        await signup({ email, password });
      }
      const response = await login({ email, password });
      const token = response.data.access_token;
      localStorage.setItem("token", token);
      setAuthToken(token);
      onAuthed();
    } catch (err) {
      setError(err?.response?.data?.detail || "Authentication failed");
    }
  };

  return (
    <div className="auth-wrap">
      <h1>Semantic Query Engine</h1>
      <form onSubmit={submit} className="auth-card">
        <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="Email" required />
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Password"
          minLength={8}
          required
        />
        <button type="submit">{isSignup ? "Sign up + Login" : "Login"}</button>
        {error && <p className="error">{error}</p>}
        <p className="toggle" onClick={() => setIsSignup((v) => !v)}>
          {isSignup ? "Already have an account? Login" : "Need an account? Sign up"}
        </p>
      </form>
    </div>
  );
}
