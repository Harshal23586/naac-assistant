"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { Lock, User, ArrowRight, ShieldAlert, Sparkles } from "lucide-react";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    // Simulating secure authentication delay natively elegantly
    setTimeout(() => {
      if (username === "admin" && password === "admin123") {
        router.push("/dashboard");
      } else {
        setError("Invalid credentials. Hint: use admin / admin123");
        setIsLoading(false);
      }
    }, 1200);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] w-full px-4 relative overflow-hidden">
      
      {/* Decorative ambient beams beautifully naturally */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-[100px] -z-10" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] -z-10" />

      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="glass-card w-full max-w-md p-8 sm:p-10 relative overflow-hidden"
      >
        <div className="absolute top-0 right-0 p-4 opacity-10">
          <ShieldAlert className="w-48 h-48 -mr-16 -mt-16 text-blue-500" />
        </div>

        <div className="relative z-10 text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-slate-800/80 border border-slate-700 shadow-xl mb-6">
            <Lock className="w-8 h-8 text-blue-400" />
          </div>
          <h2 className="text-3xl font-outfit font-bold text-white tracking-tight">Access Portal</h2>
          <p className="text-slate-400 mt-2 text-sm">Secure Authentication Matrix</p>
        </div>

        <form onSubmit={handleLogin} className="relative z-10 space-y-6">
          <div className="space-y-4">
            <div className="relative group">
              <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <User className="h-5 w-5 text-slate-500 group-focus-within:text-blue-400 transition-colors" />
              </div>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="block w-full rounded-xl border border-slate-700 bg-slate-900/50 pl-11 px-4 py-3.5 text-slate-200 placeholder-slate-500 shadow-sm outline-none transition-all focus:border-blue-500 focus:ring-1 focus:ring-blue-500/50 focus:bg-slate-800/80"
                placeholder="Institutional ID"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            
            <div className="relative group">
              <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <Lock className="h-5 w-5 text-slate-500 group-focus-within:text-blue-400 transition-colors" />
              </div>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="block w-full rounded-xl border border-slate-700 bg-slate-900/50 pl-11 px-4 py-3.5 text-slate-200 placeholder-slate-500 shadow-sm outline-none transition-all focus:border-blue-500 focus:ring-1 focus:ring-blue-500/50 focus:bg-slate-800/80"
                placeholder="Master Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          {error && (
            <motion.div 
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              className="rounded-lg bg-red-500/10 border border-red-500/20 p-3 flex items-center text-sm text-red-400"
            >
              <ShieldAlert className="h-4 w-4 mr-2 flex-shrink-0" />
              {error}
            </motion.div>
          )}

          <div className="pt-2">
            <button
              type="submit"
              disabled={isLoading}
              className="group relative flex w-full justify-center items-center overflow-hidden rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 px-4 py-3.5 text-sm font-semibold text-white transition-all hover:from-blue-500 hover:to-indigo-500 disabled:opacity-70 shadow-[0_0_30px_-5px_rgba(79,70,229,0.5)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
            >
              <span className="absolute right-0 -mt-12 h-32 w-8 translate-x-12 rotate-12 bg-white opacity-10 transition-all duration-1000 ease-out group-hover:-translate-x-96"></span>
              {isLoading ? (
                <div className="h-5 w-5 animate-spin rounded-full border-2 border-white border-t-transparent" />
              ) : (
                <span className="flex items-center text-base tracking-wide">
                  Authenticate Access <ArrowRight className="ml-2 h-5 w-5" />
                </span>
              )}
            </button>
          </div>
        </form>
        
        <div className="mt-8 text-center border-t border-slate-800/80 pt-6">
           <p className="text-xs text-slate-500 flex items-center justify-center">
             <Sparkles className="h-3 w-3 mr-1 text-slate-400"/> AES-256 Government Grade Encryption Active
           </p>
        </div>
      </motion.div>
    </div>
  );
}
