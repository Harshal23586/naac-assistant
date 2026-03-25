"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Activity, ShieldCheck, Microscope, AlertTriangle } from "lucide-react";
import Link from "next/link";

export default function PredictorPage() {
  const [formData, setFormData] = useState({
    student_faculty_ratio: 15.0,
    phd_faculty_ratio: 0.5,
    research_publications: 20,
    research_grants_amount: 1000000.0,
    industry_collaborations: 5,
    placement_rate: 75.0,
    compliance_score: 7.0,
    performance_score: 6.5,
    patents_filed: 2,
    digital_infrastructure_score: 6.0,
    library_volumes: 15000,
    laboratory_equipment_score: 7.0,
    financial_stability_score: 7.0,
    administrative_efficiency: 6.5,
    higher_education_rate: 20.0,
    entrepreneurship_cell_score: 6.0,
    community_projects: 5,
    rural_outreach_score: 6.0,
    inclusive_education_index: 6.5
  });

  const [loading, setLoading] = useState(false);
  const [mlResult, setMlResult] = useState<any>(null);
  const [policyResult, setPolicyResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handlePredict = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setMlResult(null);
    setPolicyResult(null);

    // Call backend API (Utilizing relative path mapped by the NGINX API Gateway natively on Port 80)
    const API_URL = "/api/v1";

    try {
      // 1. Fetch ML Prediction
      const mlResponse = await fetch(`${API_URL}/predict/risk`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (!mlResponse.ok) throw new Error("ML Engine returned an error. Ensure model is trained.");
      const mlData = await mlResponse.json();
      setMlResult(mlData.data);

      // 2. Fetch Policy Engine
      const policyResponse = await fetch(`${API_URL}/policy/evaluate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (!policyResponse.ok) throw new Error("Policy Engine returned an error.");
      const policyData = await policyResponse.json();
      setPolicyResult(policyData.data);

    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: parseFloat(e.target.value) || 0
    });
  };

  return (
    <div className="min-h-[85vh] py-8 text-slate-50">
      <Link href="/" className="text-blue-400 hover:text-blue-300 font-medium mb-8 inline-block">
        &larr; Back to Hub
      </Link>
      
      <div className="flex flex-col md:flex-row gap-8">
        {/* Left Side Form */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          className="w-full md:w-1/2 space-y-6"
        >
          <div className="glass-card p-6 sm:p-8">
            <h2 className="text-2xl font-outfit font-bold mb-2 flex items-center">
              <Microscope className="mr-2 text-blue-400" />
              Application Metrics
            </h2>
            <p className="text-slate-400 mb-6 text-sm">Adjust parameters to simulate live ML predictions.</p>
            
            <form onSubmit={handlePredict} className="space-y-4">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Student-Faculty Ratio</label>
                  <input type="number" step="0.1" name="student_faculty_ratio" value={formData.student_faculty_ratio} onChange={handleInputChange} className="w-full bg-slate-800/50 border border-slate-700 rounded-lg p-2.5 text-sm text-white focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Performance Score (0-10)</label>
                  <input type="number" step="0.1" name="performance_score" value={formData.performance_score} onChange={handleInputChange} className="w-full bg-slate-800/50 border border-slate-700 rounded-lg p-2.5 text-sm text-white focus:ring-2 focus:ring-blue-500 outline-none transition" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">Financial Stability (0-10)</label>
                  <input type="number" step="0.1" name="financial_stability_score" value={formData.financial_stability_score} onChange={handleInputChange} className="w-full bg-slate-800/50 border border-slate-700 rounded-lg p-2.5 text-sm text-white focus:ring-2 focus:ring-blue-500 outline-none transition" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-slate-300 mb-1">PhD Faculty Ratio (0.0 - 1.0)</label>
                  <input type="number" step="0.05" name="phd_faculty_ratio" value={formData.phd_faculty_ratio} onChange={handleInputChange} className="w-full bg-slate-800/50 border border-slate-700 rounded-lg p-2.5 text-sm text-white focus:ring-2 focus:ring-blue-500 outline-none transition" />
                </div>
              </div>

              <div className="pt-4">
                <button 
                  type="submit" 
                  disabled={loading}
                  className="w-full bg-blue-500 hover:bg-blue-400 text-slate-950 font-bold py-3 px-4 rounded-xl transition duration-300 shadow-[0_0_20px_rgba(59,130,246,0.5)] disabled:opacity-50 flex items-center justify-center"
                >
                  {loading ? "Analyzing Models..." : "Run AI Prediction Engine"}
                </button>
              </div>
            </form>
          </div>
        </motion.div>

        {/* Right Side Results */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          className="w-full md:w-1/2 space-y-6"
        >
          {error && (
            <div className="glass-card p-6 border-red-500/50 bg-red-950/20">
              <h3 className="text-red-400 font-bold flex items-center mb-2"><AlertTriangle className="mr-2 h-5 w-5"/> System Error</h3>
              <p className="text-sm text-slate-300">{error}</p>
            </div>
          )}

          {!mlResult && !error && !loading && (
            <div className="glass-card p-8 flex flex-col items-center justify-center text-center border-dashed h-full min-h-[300px] border-slate-700">
              <Activity className="h-10 w-10 text-slate-600 mb-4" />
              <h3 className="text-slate-400 font-medium">Awaiting Inference Data</h3>
              <p className="text-xs text-slate-500 mt-2 max-w-xs">Modify metrics and click predict to stream real-time insights from the FastAPI microservice.</p>
            </div>
          )}

          {mlResult && (
            <div className="glass-card p-6 border-blue-500/30 shadow-[0_0_30px_-5px_rgba(59,130,246,0.15)] relative overflow-hidden">
               {mlResult.predicted_risk.includes('Critical') && <div className="absolute top-0 left-0 w-1 h-full bg-red-500"></div>}
               {!mlResult.predicted_risk.includes('Critical') && <div className="absolute top-0 left-0 w-1 h-full bg-blue-500"></div>}
               
              <h3 className="text-sm uppercase tracking-wider text-slate-400 font-semibold mb-1">Decision Tree Inference</h3>
              <div className="flex items-end justify-between mb-6">
                <div>
                  <h2 className={`text-4xl font-black font-outfit mt-1 ${mlResult.predicted_risk.includes('Critical') ? 'text-red-400' : 'text-blue-400'}`}>
                    {mlResult.predicted_risk}
                  </h2>
                </div>
                <div className="text-right">
                  <p className="text-xs text-slate-400">Confidence</p>
                  <p className="text-xl font-bold text-white">{(mlResult.confidence * 100).toFixed(1)}%</p>
                </div>
              </div>
            </div>
          )}

          {policyResult && (
            <div className="glass-card p-6">
               <h3 className="text-sm uppercase tracking-wider text-slate-400 font-semibold mb-4 flex items-center">
                 <ShieldCheck className="mr-2 h-4 w-4" /> Statutory Policy Check (UGC/AICTE)
               </h3>
               
               <div className="space-y-3">
                 {policyResult.evaluations.map((rule: any, i: number) => (
                   <div key={i} className={`p-3 rounded-lg border ${rule.status === 'COMPLIANT' ? 'border-emerald-500/30 bg-emerald-500/5' : rule.status === 'WARNING' ? 'border-yellow-500/30 bg-yellow-500/5' : 'border-red-500/30 bg-red-500/5'}`}>
                     <div className="flex justify-between items-center mb-1">
                       <span className="font-bold text-sm text-slate-200">{rule.policy}</span>
                       <span className={`text-xs font-bold px-2 py-0.5 rounded ${rule.status === 'COMPLIANT' ? 'bg-emerald-500/20 text-emerald-300' : rule.status === 'WARNING' ? 'bg-yellow-500/20 text-yellow-300' : 'bg-red-500/20 text-red-300'}`}>{rule.status}</span>
                     </div>
                     <p className="text-xs text-slate-400">{rule.domain}: {rule.actual}</p>
                     {rule.status !== 'COMPLIANT' && <p className="text-xs text-red-400 mt-1">{rule.requirement}</p>}
                   </div>
                 ))}
               </div>

               {policyResult.is_approval_blocked_by_statute && (
                 <div className="mt-4 p-3 rounded-lg bg-red-950/40 border border-red-500/50 flex items-start">
                   <AlertTriangle className="h-5 w-5 text-red-400 mr-3 flex-shrink-0 mt-0.5" />
                   <div>
                     <p className="text-sm font-bold text-red-400">Statutory Rejection Override Applied</p>
                     <p className="text-xs text-red-200/70 mt-1">Regardless of ML Risk parameters, this institution physically breaches Indian Law requirements and must be flagged.</p>
                   </div>
                 </div>
               )}
            </div>
          )}

        </motion.div>
      </div>
    </div>
  );
}
