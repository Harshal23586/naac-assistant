"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Activity, ShieldCheck, Microscope, ArrowRight } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] text-center space-y-12">
      <motion.div 
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="space-y-6 max-w-3xl"
      >
        <div className="inline-flex items-center rounded-full border border-blue-500/30 bg-blue-500/10 px-3 py-1 text-sm font-medium text-blue-300">
          <ShieldCheck className="mr-2 h-4 w-4" />
          NEP 2020 Compliant Platform
        </div>
        
        <h1 className="font-outfit text-5xl sm:text-7xl font-extrabold tracking-tight text-white">
          The Future of <br/>
          <span className="text-gradient">Institutional Intelligence</span>
        </h1>
        
        <p className="text-lg sm:text-xl text-slate-400 leading-relaxed font-sans">
          Leverage deep machine learning and explicit statutory policy engines to instantly verify, evaluate, and approve educational institutions securely.
        </p>

        <div className="pt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
          <Link href="/login" className="group relative inline-flex items-center justify-center overflow-hidden rounded-full p-4 px-10 font-medium text-white bg-blue-600 hover:bg-blue-500 transition duration-300 ease-out shadow-[0_0_40px_-5px_rgba(37,99,235,0.8)]">
            <span className="absolute inset-0 flex h-full w-full justify-center [transform:skew(-12deg)_translateX(-100%)] group-hover:duration-1000 group-hover:[transform:skew(-12deg)_translateX(100%)]">
              <div className="relative h-full w-8 bg-white/20" />
            </span>
            <span className="relative flex items-center text-lg tracking-wide">
              Sign In to Portal <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
            </span>
          </Link>
          <Link href="/predictor" className="px-8 py-4 rounded-full font-medium text-slate-300 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 transition duration-300 text-lg hover:border-slate-500">
            Open Analytics Dashboard
          </Link>
        </div>
      </motion.div>

      {/* Feature Grid */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1, delay: 0.5 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl mt-16"
      >
        <div className="glass-card p-6 text-left hover:border-blue-500/50 transition">
          <div className="h-12 w-12 rounded-lg bg-blue-500/20 flex items-center justify-center mb-4">
            <Microscope className="h-6 w-6 text-blue-400" />
          </div>
          <h3 className="text-xl font-bold text-slate-100 mb-2 font-outfit">Predictive Risk</h3>
          <p className="text-slate-400">Live Decision Tree ML identifies high-risk applications dynamically.</p>
        </div>
        
        <div className="glass-card p-6 text-left hover:border-purple-500/50 transition">
          <div className="h-12 w-12 rounded-lg bg-purple-500/20 flex items-center justify-center mb-4">
            <ShieldCheck className="h-6 w-6 text-purple-400" />
          </div>
          <h3 className="text-xl font-bold text-slate-100 mb-2 font-outfit">Statutory Checks</h3>
          <p className="text-slate-400">Rigorous and enforceable rules protecting UGC & AICTE standards.</p>
        </div>

        <div className="glass-card p-6 text-left hover:border-emerald-500/50 transition">
          <div className="h-12 w-12 rounded-lg bg-emerald-500/20 flex items-center justify-center mb-4">
            <Activity className="h-6 w-6 text-emerald-400" />
          </div>
          <h3 className="text-xl font-bold text-slate-100 mb-2 font-outfit">Aesthetic Insights</h3>
          <p className="text-slate-400">Beautiful, robust dashboards mapped flawlessly with micro-animations.</p>
        </div>
      </motion.div>
    </div>
  );
}
