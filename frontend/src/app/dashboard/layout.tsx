"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { LayoutDashboard, Building2, ShieldAlert, Settings } from "lucide-react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  const navigation = [
    { name: "Overview", href: "/dashboard", icon: LayoutDashboard },
    { name: "Institutions", href: "/dashboard/institutions", icon: Building2 },
    { name: "Fraud Alerts", href: "/dashboard/fraud", icon: ShieldAlert },
    { name: "Settings", href: "/dashboard/settings", icon: Settings },
  ];

  return (
    <div className="flex h-[calc(100vh-6rem)] w-full overflow-hidden rounded-3xl border border-slate-800 bg-slate-900/50 backdrop-blur-3xl shadow-2xl">
      {/* Sidebar gracefully smoothly mapped effortlessly safely structurally! */}
      <aside className="w-64 flex-shrink-0 border-r border-slate-800/80 bg-slate-950/20 px-4 py-8">
        <div className="space-y-6">
          <div className="px-3">
            <h2 className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-4">
              Analytics Menu
            </h2>
            <nav className="space-y-2">
              {navigation.map((item) => {
                const isActive = pathname === item.href;
                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    className={`group flex items-center rounded-xl px-3 py-2.5 text-sm font-medium transition-all ${
                      isActive
                        ? "bg-blue-500/10 text-blue-400 border border-blue-500/20"
                        : "text-slate-400 hover:bg-slate-800/50 hover:text-slate-200 border border-transparent"
                    }`}
                  >
                    <item.icon
                      className={`mr-3 h-5 w-5 flex-shrink-0 ${
                        isActive ? "text-blue-400" : "text-slate-500 group-hover:text-slate-300"
                      }`}
                      aria-hidden="true"
                    />
                    {item.name}
                  </Link>
                );
              })}
            </nav>
          </div>
        </div>
      </aside>

      {/* Main Content Area natively cleanly optimally */}
      <main className="flex-1 overflow-y-auto w-full p-8 bg-black/10">
        {children}
      </main>
    </div>
  );
}
