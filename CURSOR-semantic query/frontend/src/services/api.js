import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE,
});

export function setAuthToken(token) {
  if (token) {
    api.defaults.headers.common.Authorization = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common.Authorization;
  }
}

export const signup = (payload) => api.post("/signup", payload);
export const login = (payload) => api.post("/login", payload);
export const getSources = () => api.get("/sources");
export const askQuery = (payload) => api.post("/query", payload);

export const uploadText = (text) => {
  const form = new FormData();
  form.append("source_type", "text");
  form.append("text", text);
  return api.post("/upload", form);
};

export const uploadUrl = (url) => {
  const form = new FormData();
  form.append("source_type", "url");
  form.append("url", url);
  return api.post("/upload", form);
};

export const uploadFile = (file) => {
  const form = new FormData();
  form.append("source_type", "file");
  form.append("file", file);
  return api.post("/upload", form);
};

export const tts = (text) =>
  api.post(
    "/tts",
    { text },
    {
      responseType: "blob",
    }
  );
