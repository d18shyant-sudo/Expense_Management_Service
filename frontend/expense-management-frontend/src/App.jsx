import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import RoleLogin from "./pages/RoleLogin";
import ForgotPassword from "./pages/forgot_Password";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<RoleLogin />} />
      <Route path="/forgot-password" element={<ForgotPassword />} />
    </Routes>
  );
}