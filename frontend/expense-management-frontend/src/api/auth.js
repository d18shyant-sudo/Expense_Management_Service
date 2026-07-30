import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8000/api/v1/login",
  headers: {
    "Content-Type": "application/json",
  },
});