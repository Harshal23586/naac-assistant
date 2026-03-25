import type { Metadata } from "next";
import { Inter, Outfit } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });
const outfit = Outfit({ subsets: ["latin"], variable: "--font-outfit" });

export const metadata: Metadata = {
  title: "SUGAM Intelligence",
  description: "AI-Powered National Education Policy 2020 Compliance Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark scroll-smooth">
      <body
        className={`${inter.variable} ${outfit.variable} font-sans bg-slate-950 text-slate-50 antialiased min-h-screen flex flex-col`}
      >
        {/* Abstract background gradient effect */}
        <div className="fixed inset-0 -z-10 h-full w-full bg-slate-950">
          <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.3),rgba(255,255,255,0))]"></div>
        </div>

        <header className="sticky top-0 z-50 w-full border-b border-slate-800 bg-slate-950/80 backdrop-blur-md">
          <div className="flex h-16 items-center px-4 sm:px-8 max-w-7xl mx-auto text-blue-400 font-outfit font-bold text-xl tracking-tight">
            <span className="text-white mr-2">🏛️ SUGAM</span> Intelligence
          </div>
        </header>

        <main className="flex-1 w-full max-w-7xl mx-auto p-4 sm:p-6 lg:p-8 mt-4">
          {children}
        </main>
      </body>
    </html>
  );
}
