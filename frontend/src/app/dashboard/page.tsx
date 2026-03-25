"use client";

import { motion } from "framer-motion";
import { Activity, ShieldCheck, AlertTriangle, Users } from "lucide-react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  AreaChart,
  Area,
  BarChart,
  Bar
} from "recharts";

const complianceData = [
  { month: "Jan", score: 65 },
  { month: "Feb", score: 68 },
  { month: "Mar", score: 75 },
  { month: "Apr", score: 82 },
  { month: "May", score: 88 },
  { month: "Jun", score: 94 },
];

const submissionsData = [
  { name: "Colleges", value: 400 },
  { name: "Universities", value: 300 },
  { name: "Gov Bodies", value: 150 },
  { name: "Institutes", value: 200 },
];

export default function DashboardHome() {
  return (
    <div className="space-y-8 pb-8">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-outfit font-bold tracking-tight text-white">Global Analytics</h1>
        <div className="flex items-center space-x-2">
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
          <span className="text-sm font-medium text-emerald-400">Live Backend Stream</span>
        </div>
      </div>

      <motion.div 
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="glass-card p-5 border-l-4 border-l-blue-500">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-sm font-medium text-slate-400">Active Institutions</p>
              <h2 className="text-3xl font-bold text-white mt-1">1,204</h2>
            </div>
            <div className="p-2 bg-blue-500/20 rounded-lg"><Users className="h-5 w-5 text-blue-400" /></div>
          </div>
          <div className="mt-4 flex items-center text-xs text-blue-400"><Activity className="h-3 w-3 mr-1"/> +12% from last month</div>
        </div>

        <div className="glass-card p-5 border-l-4 border-l-emerald-500">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-sm font-medium text-slate-400">Approved Compliances</p>
              <h2 className="text-3xl font-bold text-white mt-1">89.2%</h2>
            </div>
            <div className="p-2 bg-emerald-500/20 rounded-lg"><ShieldCheck className="h-5 w-5 text-emerald-400" /></div>
          </div>
          <div className="mt-4 flex items-center text-xs text-emerald-400"><Activity className="h-3 w-3 mr-1"/> AI Verification Stable</div>
        </div>

        <div className="glass-card p-5 border-l-4 border-l-orange-500">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-sm font-medium text-slate-400">Pending Review</p>
              <h2 className="text-3xl font-bold text-white mt-1">342</h2>
            </div>
            <div className="p-2 bg-orange-500/20 rounded-lg"><Activity className="h-5 w-5 text-orange-400" /></div>
          </div>
          <div className="mt-4 flex items-center text-xs text-slate-400">Workflow Engine Processing</div>
        </div>

        <div className="glass-card p-5 border-l-4 border-l-red-500">
          <div className="flex justify-between items-start">
            <div>
              <p className="text-sm font-medium text-slate-400">Fraud Flags Identified</p>
              <h2 className="text-3xl font-bold text-white mt-1">18</h2>
            </div>
            <div className="p-2 bg-red-500/20 rounded-lg"><AlertTriangle className="h-5 w-5 text-red-500" /></div>
          </div>
          <div className="mt-4 flex items-center text-xs text-red-400">IsolationForest Anomalies Found</div>
        </div>
      </motion.div>

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="glass-card p-6 min-h-[400px]"
        >
          <div className="mb-6">
            <h3 className="text-xl font-bold font-outfit text-white">Composite Compliance Trajectory</h3>
            <p className="text-sm text-slate-400">Average RAG AI Score Evaluation Trends</p>
          </div>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={complianceData}>
                <defs>
                  <linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="month" stroke="#64748b" tick={{fill: '#64748b'}} axisLine={false} tickLine={false} />
                <YAxis stroke="#64748b" tick={{fill: '#64748b'}} axisLine={false} tickLine={false} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#1e293b', borderRadius: '8px', color: '#f8fafc' }}
                  itemStyle={{ color: '#60a5fa' }}
                />
                <Area type="monotone" dataKey="score" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorScore)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="glass-card p-6 min-h-[400px]"
        >
          <div className="mb-6">
            <h3 className="text-xl font-bold font-outfit text-white">Application Volume by Tier</h3>
            <p className="text-sm text-slate-400">Submission bandwidth tracked via SaaS Analytics</p>
          </div>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={submissionsData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="name" stroke="#64748b" tick={{fill: '#64748b'}} axisLine={false} tickLine={false} />
                <YAxis stroke="#64748b" tick={{fill: '#64748b'}} axisLine={false} tickLine={false} />
                <Tooltip 
                  cursor={{fill: '#1e293b'}}
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#1e293b', borderRadius: '8px', color: '#f8fafc' }}
                  itemStyle={{ color: '#818cf8' }}
                />
                <Bar dataKey="value" fill="#818cf8" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
