import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import RoleLogin from "./pages/RoleLogin";
import ForgotPassword from "./pages/forgot_Password";
import Register from "./pages/Register";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<RoleLogin />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  
  );
}