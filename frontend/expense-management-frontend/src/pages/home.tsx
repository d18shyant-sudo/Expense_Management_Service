import { ArrowRight } from "lucide-react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-green-50 to-green-100 flex items-center justify-center px-6">

      <div className="max-w-5xl w-full">

        <div className="bg-white rounded-3xl shadow-2xl overflow-hidden grid md:grid-cols-2">

          {/* Left Section */}
          <div className="bg-green-800 text-white p-10 flex flex-col justify-center">

            <span className="inline-block bg-green-700 px-4 py-2 rounded-full text-sm font-semibold mb-6 w-fit">
              Expense Management System
            </span>

            <h1 className="text-5xl font-bold leading-tight">
              Where Every Expense
              <br />
              Finds Its Approval.
            </h1>

            <p className="mt-6 text-green-100 leading-7">
              Simplify expense submission, approvals and reimbursements
              through one secure and efficient platform.
            </p>

          </div>

          {/* Right Section */}
          <div className="p-10 flex flex-col justify-center items-center text-center">

            <h2 className="text-3xl font-bold text-gray-800">
              Welcome
            </h2>

            <p className="text-gray-500 mt-3 mb-10">
              Securely access your Expense Management account.
            </p>

            <button
              onClick={() => navigate("/login")}
              className="bg-green-800 hover:bg-green-700 text-white px-8 py-4 rounded-xl font-semibold flex items-center gap-3 transition-all hover:scale-105 shadow-lg"
            >
              Get Started
              <ArrowRight size={20} />
            </button>

          </div>

        </div>

        <p className="text-center mt-8 text-gray-500">
          © 2026 Expense Management System
        </p>

      </div>

    </div>
  );
}