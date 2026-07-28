import {
  ArrowRight,
  Eye,
  EyeOff,
  Lock,
  User,
} from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function RoleLogin() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (
    e: React.FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    setError("");

    if (!username.trim() || !password.trim()) {
      setError("Please enter both username and password.");
      return;
    }

    try {
      setLoading(true);

      const response = await axios.post(
        "http://localhost:8000/api/v1/login",
        {
          username,
          password,
        }
      );

      console.log("Login Success:", response.data);

      localStorage.setItem(
        "access_token",
        response.data.access_token
      );

      if (response.data.role) {
        localStorage.setItem("role", response.data.role);
      }

      if (response.data.username) {
        localStorage.setItem(
          "username",
          response.data.username
        );
      }

      alert("Login Successful!");

      // Change this if you have a dashboard route
      // navigate("/dashboard");

    } catch (err: any) {
      console.error(err);

      setError(
        err.response?.data?.detail ??
          "Invalid username or password."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-green-50 to-green-100 flex items-center justify-center px-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden">

          {/* Header */}

          <div className="bg-green-800 text-white p-10 text-center">
            <div className="w-20 h-20 rounded-full bg-white/10 border border-white/20 flex items-center justify-center mx-auto mb-5">
              <Lock size={36} />
            </div>

            <h1 className="text-3xl font-bold">
              Welcome Back
            </h1>

            <p className="text-green-100 mt-2">
              Sign in to continue
            </p>
          </div>

          {/* Form */}

          <div className="p-8">

            <form
              onSubmit={handleLogin}
              className="space-y-6"
            >

              {/* Username */}

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Username
                </label>

                <div className="relative">
                  <User
                    size={20}
                    className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"
                  />

                  <input
                    type="text"
                    value={username}
                    onChange={(e) =>
                      setUsername(e.target.value)
                    }
                    placeholder="Enter username"
                    className="w-full pl-12 pr-4 py-3 rounded-xl border border-gray-300 focus:border-green-700 focus:ring-2 focus:ring-green-200 outline-none"
                  />
                </div>
              </div>

              {/* Password */}

              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  Password
                </label>

                <div className="relative">

                  <Lock
                    size={20}
                    className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"
                  />

                  <input
                    type={
                      showPassword
                        ? "text"
                        : "password"
                    }
                    value={password}
                    onChange={(e) =>
                      setPassword(e.target.value)
                    }
                    placeholder="Enter password"
                    className="w-full pl-12 pr-12 py-3 rounded-xl border border-gray-300 focus:border-green-700 focus:ring-2 focus:ring-green-200 outline-none"
                  />

                  <button
                    type="button"
                    onClick={() =>
                      setShowPassword(!showPassword)
                    }
                    className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-500 hover:text-green-700"
                  >
                    {showPassword ? (
                      <EyeOff size={20} />
                    ) : (
                      <Eye size={20} />
                    )}
                  </button>

                </div>
              </div>

              {/* Error */}

              {error && (
                <div className="bg-red-50 border border-red-200 rounded-xl p-3 text-red-600 text-sm">
                  {error}
                </div>
              )}

              {/* Forgot Password */}

              <div className="flex justify-end">
                <button
                  type="button"
                  onClick={() =>
                    navigate("/forgot-password")
                  }
                  className="text-sm font-medium text-green-700 hover:text-green-800 transition"
                >
                  Forgot Password?
                </button>
              </div>

              {/* Login Button */}

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-green-800 hover:bg-green-700 text-white py-3 rounded-xl font-semibold flex justify-center items-center gap-2 transition"
              >
                {loading ? (
                  "Signing In..."
                ) : (
                  <>
                    Sign In
                    <ArrowRight size={18} />
                  </>
                )}
              </button>

            </form>

          </div>

        </div>
      </div>
    </div>
  );
}