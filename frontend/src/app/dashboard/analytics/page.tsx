"use client";

import { motion } from "framer-motion";

export default function AnalyticsDashboard() {
  return (
    <div className="w-full h-full pb-8 flex flex-col space-y-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-outfit font-bold tracking-tight text-white mb-2">Deep Data Matrix</h1>
          <p className="text-sm text-slate-400">Streamlit Engine directly injected via Port 8501</p>
        </div>
        <div className="flex items-center space-x-2">
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
          <span className="text-sm font-medium text-emerald-400">Plotly Data Active</span>
        </div>
      </div>

      <motion.div 
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6 }}
        className="w-full h-full min-h-[85vh] glass-card overflow-hidden border border-slate-700/50 shadow-2xl relative"
      >
        <iframe
          src="http://localhost:8501/?embedded=true"
          title="SUGAM Streamlit Analytics"
          className="w-full h-full border-0 absolute inset-0"
          style={{ height: "100%", minHeight: "85vh", border: "none" }}
          sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
        />
      </motion.div>
    </div>
  );
}
