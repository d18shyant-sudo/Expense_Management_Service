import { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import toast from "react-hot-toast";

import {
  Mail,
  Lock,
  Eye,
  EyeOff,
  ShieldCheck,
  ArrowLeft,
} from "lucide-react";


export default function ForgotPassword() {

  const navigate = useNavigate();

  const API = "http://localhost:8000/api/v1";

  const [step, setStep] = useState(1);

  const [email, setEmail] = useState("");

  const [otp, setOtp] = useState([
    "",
    "",
    "",
    "",
    "",
    "",
  ]);

  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [showPassword, setShowPassword] =
    useState(false);

  const [showConfirmPassword, setShowConfirmPassword] =
    useState(false);

  const [loading, setLoading] =
    useState(false);


  const otpRefs = useRef<(HTMLInputElement | null)[]>([]);



  const sendOtp = async () => {

    if (!email) {
      toast.error("Please enter your email");
      return;
    }

    try {

      setLoading(true);

      const response = await axios.post(
        `${API}/forgot-password`,
        {
          email,
        }
      );

      toast.success(
        response.data.message ||
        "OTP sent successfully!"
      );

      setStep(2);

    } catch (error: any) {

      toast.error(
        error.response?.data?.detail ||
        "Failed to send OTP"
      );

    } finally {

      setLoading(false);

    }
  };



  const handleOtpChange = (
    value: string,
    index: number
  ) => {

    if (!/^[0-9]?$/.test(value)) {
      return;
    }


    const updatedOtp = [...otp];

    updatedOtp[index] = value;

    setOtp(updatedOtp);



    if (
      value &&
      index < 5
    ) {

      otpRefs.current[index + 1]?.focus();

    }

  };



  const handleOtpKeyDown = (
    e: React.KeyboardEvent<HTMLInputElement>,
    index: number
  ) => {

    if (
      e.key === "Backspace" &&
      !otp[index] &&
      index > 0
    ) {

      otpRefs.current[index - 1]?.focus();

    }

  };




const verifyOtp = async () => {

  const enteredOtp = otp.join("");

  if (enteredOtp.length !== 6) {
    toast.error("Please enter 6 digit OTP");
    return;
  }

  try {
    setLoading(true);

    const response = await axios.post(`${API}/verify-otp`, {
      email,
      otp: enteredOtp,
    });

    toast.success(response.data.message || "OTP verified successfully!");
    setStep(3);

  } catch (error: any) {
    toast.error(error.response?.data?.detail || "Invalid OTP");
  } finally {
    setLoading(false);
  }
};

const resetPassword = async () => {

  if (!newPassword || !confirmPassword) {
    toast.error("Please enter both password fields");
    return;
  }

  if (newPassword !== confirmPassword) {
    toast.error("Passwords do not match");
    return;
  }

  try {
    setLoading(true);

    const response = await axios.post(`${API}/reset-password`, {
      email,
      otp: otp.join(""),
      new_password: newPassword,
    });

    toast.success(response.data.message || "Password reset successfully");
    navigate("/login");

  } catch (error: any) {
    toast.error(error.response?.data?.detail || error.response?.data?.message || "Failed to reset password");
  } finally {
    setLoading(false);
  }
};


return (
    <div className="min-h-screen bg-gradient-to-br from-white via-green-50 to-green-100 flex items-center justify-center px-4">

      <div className="bg-white rounded-3xl shadow-xl w-full max-w-md p-8">


        <button
          onClick={() => navigate("/login")}
          className="flex items-center text-green-700 hover:text-green-800 transition mb-6"
        >

          <ArrowLeft
            className="w-5 h-5 mr-2"
          />

          Back to Login

        </button>



        <h1 className="text-3xl font-bold text-center text-green-800">

          Forgot Password

        </h1>



        <p className="text-center text-gray-500 mt-2 mb-8">

          {step === 1 &&
            "Enter your registered email address"}

          {step === 2 &&
            "Enter the OTP sent to your email"}

          {step === 3 &&
            "Create your new password"}

        </p>



        {step === 1 && (

          <>

            <div className="relative mb-6">

              <Mail
                className="absolute left-4 top-3 text-gray-400"
              />


              <input
                type="email"
                placeholder="Email Address"
                value={email}
                onChange={(e)=>
                  setEmail(e.target.value)
                }
                className="w-full pl-12 pr-4 py-3 border rounded-xl focus:outline-none focus:border-green-700 focus:ring-2 focus:ring-green-200"
              />

            </div>



            <button
              onClick={sendOtp}
              disabled={loading}
              className="w-full bg-green-800 hover:bg-green-700 text-white py-3 rounded-xl font-semibold transition"
            >

              {loading
                ? "Sending OTP..."
                : "Send OTP"}

            </button>


          </>

        )}



        {step === 2 && (

          <>

            <div className="flex justify-center gap-3 mb-6">

              {otp.map((digit,index)=>(

                <input
                  key={index}
                  ref={(el)=>
                    {
                      otpRefs.current[index]=el
                    }
                  }
                  value={digit}
                  maxLength={1}
                  onChange={(e)=>
                    handleOtpChange(
                      e.target.value,
                      index
                    )
                  }
                  onKeyDown={(e)=>
                    handleOtpKeyDown(
                      e,
                      index
                    )
                  }
                  className="w-12 h-12 text-center text-xl font-bold border rounded-xl focus:outline-none focus:border-green-700 focus:ring-2 focus:ring-green-200"
                />

              ))}

            </div>



            <button
              onClick={verifyOtp}
              disabled={loading}
              className="w-full bg-green-800 hover:bg-green-700 text-white py-3 rounded-xl font-semibold transition"
            >

              {loading
                ? "Verifying..."
                : "Verify OTP"}

            </button>


          </>

        )}
                {step === 3 && (

          <>

            <div className="relative mb-5">

              <Lock
                className="absolute left-4 top-3 text-gray-400"
              />

              <input
                type={
                  showPassword
                    ? "text"
                    : "password"
                }
                placeholder="New Password"
                value={newPassword}
                onChange={(e)=>
                  setNewPassword(e.target.value)
                }
                className="w-full pl-12 pr-12 py-3 border rounded-xl focus:outline-none focus:border-green-700 focus:ring-2 focus:ring-green-200"
              />


              <button
                type="button"
                onClick={() =>
                  setShowPassword(!showPassword)
                }
                className="absolute right-4 top-3 text-gray-500 hover:text-green-700"
              >

                {showPassword ? (
                  <EyeOff size={20}/>
                ) : (
                  <Eye size={20}/>
                )}

              </button>

            </div>



            <div className="relative mb-6">

              <Lock
                className="absolute left-4 top-3 text-gray-400"
              />


              <input
                type={
                  showConfirmPassword
                    ? "text"
                    : "password"
                }
                placeholder="Confirm Password"
                value={confirmPassword}
                onChange={(e)=>
                  setConfirmPassword(e.target.value)
                }
                className="w-full pl-12 pr-12 py-3 border rounded-xl focus:outline-none focus:border-green-700 focus:ring-2 focus:ring-green-200"
              />


              <button
                type="button"
                onClick={() =>
                  setShowConfirmPassword(
                    !showConfirmPassword
                  )
                }
                className="absolute right-4 top-3 text-gray-500 hover:text-green-700"
              >

                {showConfirmPassword ? (
                  <EyeOff size={20}/>
                ) : (
                  <Eye size={20}/>
                )}

              </button>

            </div>



            <button
              onClick={resetPassword}
              disabled={loading}
              className="w-full bg-green-800 hover:bg-green-700 text-white py-3 rounded-xl font-semibold transition"
            >

              {loading
                ? "Resetting Password..."
                : "Reset Password"}

            </button>


          </>

        )}

      </div>

    </div>
  );
}