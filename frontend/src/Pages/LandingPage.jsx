import { useState } from 'react'



export default function LandingPage({ onStart }) {
  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">
      {/* BACKGROUND */}
      <div className="fixed inset-0 bg-[radial-gradient(circle_at_top_right,rgba(139,92,246,0.18),transparent_25%),radial-gradient(circle_at_bottom_left,rgba(236,72,153,0.14),transparent_30%)] pointer-events-none" />

      {/* NAVBAR */}
      <header className="sticky top-0 z-50 border-b border-white/10 backdrop-blur-xl bg-black/60">
        <div className="max-w-7xl mx-auto px-6 py-5 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 rounded-2xl bg-gradient-to-br from-violet-500 to-pink-500 flex items-center justify-center text-xl font-bold shadow-2xl">
              S
            </div>

            <div>
              <h1 className="text-2xl font-bold tracking-tight">
                StudioAI
              </h1>
              <p className="text-xs text-zinc-500">
                Autonomous Multimodal Content Platform
              </p>
            </div>
          </div>

          <nav className="hidden lg:flex items-center gap-10 text-sm text-zinc-400">
            <a href="#features" className="hover:text-white transition">
              Features
            </a>
            <a href="#workflow" className="hover:text-white transition">
              Workflow
            </a>
            <a href="#demo" className="hover:text-white transition">
              Demo
            </a>
            <a href="#pricing" className="hover:text-white transition">
              Pricing
            </a>
          </nav>

          <div className="flex items-center gap-4">
            {/* <button className="hidden md:block px-5 py-2 rounded-xl border border-white/10 hover:bg-white/5 transition">
              Login
            </button> */}

            <button
              onClick={onStart}
              className="px-6 py-3 rounded-2xl bg-white text-black font-semibold shadow-2xl hover:scale-[1.02] transition"
            >
              Start Creating
            </button>
          </div>
        </div>
      </header>

      {/* HERO */}
      <section className="relative">
        <div className="max-w-7xl mx-auto px-6 pt-24 pb-28 grid lg:grid-cols-2 gap-20 items-center">
          {/* LEFT */}
          <div>
            <div className="inline-flex items-center gap-2 rounded-full border border-violet-500/20 bg-violet-500/10 px-5 py-2 text-sm text-violet-300 mb-8">
              ✨ AI Agents + Research + SEO + Image Generation
            </div>

            <h1 className="text-6xl md:text-7xl font-black tracking-tight leading-[1.02]">
              The Future of
              <span className="block bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent">
                AI Content Creation
              </span>
            </h1>

            <p className="mt-8 text-zinc-400 text-xl leading-relaxed max-w-2xl">
              StudioAI is an autonomous AI content operating system that
              researches, writes, optimizes SEO, generates visuals,
              and exports complete multimodal content experiences.
            </p>

            {/* BUTTONS */}
            <div className="mt-12 flex flex-wrap gap-5">
              <button
                onClick={onStart}
                className="px-8 py-5 rounded-2xl bg-white text-black font-semibold text-lg shadow-2xl hover:scale-[1.02] transition"
              >
                Start Now
              </button>

              <button className="px-8 py-5 rounded-2xl border border-white/10 bg-white/5 hover:bg-white/10 transition text-lg">
                Watch Demo
              </button>
            </div>

            {/* STATS */}
            <div className="mt-16 grid grid-cols-3 gap-10">
              <div>
                <div className="text-4xl font-black">10x</div>
                <p className="mt-2 text-zinc-500 text-sm">
                  Faster Content Production
                </p>
              </div>

              <div>
                <div className="text-4xl font-black">AI</div>
                <p className="mt-2 text-zinc-500 text-sm">
                  Autonomous Agent Workflow
                </p>
              </div>

              <div>
                <div className="text-4xl font-black">SEO</div>
                <p className="mt-2 text-zinc-500 text-sm">
                  Optimized Enterprise Content
                </p>
              </div>
            </div>
          </div>

          {/* RIGHT */}
          <div className="relative">
            <div className="rounded-[36px] border border-white/10 bg-white/[0.04] backdrop-blur-2xl overflow-hidden shadow-[0_0_100px_rgba(139,92,246,0.15)]">
              {/* TOP BAR */}
              <div className="flex items-center justify-between px-6 py-5 border-b border-white/10 bg-black/40">
                <div>
                  <h3 className="font-semibold text-lg">
                    StudioAI Dashboard
                  </h3>
                  <p className="text-sm text-zinc-500">
                    Autonomous Content Pipeline
                  </p>
                </div>

                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 rounded-full bg-red-500"></div>
                  <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                  <div className="w-3 h-3 rounded-full bg-green-500"></div>
                </div>
              </div>

              {/* CONTENT */}
              <div className="p-6 space-y-6">
                {/* INPUT */}
                <div className="rounded-3xl border border-white/10 bg-black/40 p-5">
                  <div className="text-sm text-zinc-500 mb-3">
                    Content Topic
                  </div>

                  <div className="text-lg font-medium">
                    AI Agents Transforming Enterprise Marketing Workflows
                  </div>
                </div>

                {/* AGENTS */}
                <div className="space-y-4">
                  {[
                    'Query Generator Agent',
                    'Research Agent',
                    'SEO Optimization Agent',
                    'Image Planning Agent',
                    'Multimodal Composer',
                  ].map((item, idx) => (
                    <div
                      key={idx}
                      className="rounded-2xl border border-white/10 bg-black/30 p-5 flex items-center justify-between"
                    >
                      <div>
                        <h4 className="font-semibold">{item}</h4>
                        <p className="text-sm text-zinc-500 mt-1">
                          Running autonomous workflow...
                        </p>
                      </div>

                      <div className="flex items-center gap-2 text-emerald-400 text-sm">
                        <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
                        Active
                      </div>
                    </div>
                  ))}
                </div>

                {/* RESULT */}
                <div className="rounded-3xl bg-gradient-to-r from-violet-500/10 to-pink-500/10 border border-violet-500/20 p-6">
                  <div className="flex items-center justify-between">
                    <div>
                      <h4 className="font-semibold text-lg">
                        Content Generated
                      </h4>

                      <p className="text-zinc-400 mt-2">
                        Blog + SEO + AI Visuals + PDF Export
                      </p>
                    </div>

                    <button className="px-5 py-3 rounded-2xl bg-white text-black font-medium shadow-xl">
                      Download PDF
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* GLOW */}
            <div className="absolute -top-10 -right-10 w-52 h-52 rounded-full bg-violet-500/20 blur-3xl"></div>
            <div className="absolute -bottom-10 -left-10 w-52 h-52 rounded-full bg-pink-500/20 blur-3xl"></div>
          </div>
        </div>
      </section>

      {/* VIDEO SECTION */}
      <section id="demo" className="max-w-7xl mx-auto px-6 py-28">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-black tracking-tight">
            See StudioAI in Action
          </h2>

          <p className="mt-6 text-zinc-500 text-lg max-w-2xl mx-auto">
            Watch autonomous AI agents research, generate, optimize,
            and compose multimodal content experiences.
          </p>
        </div>

        <div className="rounded-[40px] overflow-hidden border border-white/10 bg-white/[0.04] backdrop-blur-2xl shadow-2xl">
          <div className="aspect-video flex items-center justify-center bg-gradient-to-br from-zinc-950 to-zinc-900">
            <div className="text-center">
              <div className="w-28 h-28 rounded-full bg-white text-black flex items-center justify-center text-4xl mx-auto shadow-2xl">
                ▶
              </div>

              <h3 className="mt-8 text-3xl font-bold">
                Product Demo Video
              </h3>

              <p className="mt-3 text-zinc-500">
                Showcase your AI agent workflow here
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section id="features" className="max-w-7xl mx-auto px-6 py-28">
        <div className="text-center mb-20">
          <h2 className="text-5xl font-black tracking-tight">
            Built Like a Modern AI Operating System
          </h2>

          <p className="mt-6 text-zinc-500 text-lg max-w-3xl mx-auto">
            StudioAI combines autonomous agent orchestration,
            multimodal generation, SEO optimization, and enterprise
            publishing workflows into one unified platform.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {[
            {
              title: 'Autonomous Research',
              desc: 'AI agents intelligently research trends, technologies, and latest industry insights using optimized search planning.',
            },
            {
              title: 'SEO Optimization',
              desc: 'Automatically improve readability, structure, search intent, and ranking potential.',
            },
            {
              title: 'AI Image Generation',
              desc: 'Generate multimodal diagrams, visuals, illustrations, and enterprise-ready graphics.',
            },
            {
              title: 'Multimodal Composition',
              desc: 'Automatically compose images and content into professional long-form articles.',
            },
            {
              title: 'Enterprise Workflow',
              desc: 'Multi-agent architecture designed for scalable autonomous publishing workflows.',
            },
            {
              title: 'PDF Export System',
              desc: 'Export complete polished reports, blogs, newsletters, and presentations instantly.',
            },
          ].map((feature, idx) => (
            <div
              key={idx}
              className="rounded-[32px] border border-white/10 bg-white/[0.03] backdrop-blur-xl p-8 hover:border-violet-500/30 transition-all duration-300 hover:-translate-y-1"
            >
              <div className="w-16 h-16 rounded-3xl bg-gradient-to-br from-violet-500 to-pink-500 mb-7 shadow-xl"></div>

              <h3 className="text-2xl font-bold">
                {feature.title}
              </h3>

              <p className="mt-5 text-zinc-500 leading-relaxed text-lg">
                {feature.desc}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* WORKFLOW */}
      <section id="workflow" className="max-w-7xl mx-auto px-6 py-28">
        <div className="rounded-[40px] border border-white/10 bg-gradient-to-br from-white/[0.04] to-white/[0.02] backdrop-blur-2xl p-12 md:p-20 overflow-hidden relative">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(139,92,246,0.14),transparent_30%)]" />

          <div className="relative z-10">
            <div className="text-center mb-20">
              <h2 className="text-5xl font-black tracking-tight">
                Autonomous Agent Workflow
              </h2>

              <p className="mt-6 text-zinc-500 text-lg max-w-3xl mx-auto">
                Every piece of content is generated through intelligent,
                coordinated AI agents.
              </p>
            </div>

            <div className="grid md:grid-cols-5 gap-6">
              {[
                'Query Planning',
                'Web Research',
                'Content Writing',
                'Image Generation',
                'Multimodal Export',
              ].map((step, idx) => (
                <div
                  key={idx}
                  className="rounded-3xl border border-white/10 bg-black/30 p-6 text-center"
                >
                  <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-pink-500 flex items-center justify-center text-xl font-bold mx-auto mb-5">
                    {idx + 1}
                  </div>

                  <h3 className="font-bold text-lg">
                    {step}
                  </h3>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* PRICING */}
      <section id="pricing" className="max-w-7xl mx-auto px-6 py-28">
        <div className="text-center mb-20">
          <h2 className="text-5xl font-black tracking-tight">
            Simple Pricing
          </h2>

          <p className="mt-6 text-zinc-500 text-lg">
            Built for creators, startups, and AI-first teams.
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {[
            {
              name: 'Starter',
              price: '$0',
              desc: 'Perfect for creators exploring AI workflows.',
            },
            {
              name: 'Pro',
              price: '$29',
              desc: 'Advanced autonomous content generation.',
            },
            {
              name: 'Enterprise',
              price: 'Custom',
              desc: 'Scalable enterprise publishing systems.',
            },
          ].map((plan, idx) => (
            <div
              key={idx}
              className="rounded-[36px] border border-white/10 bg-white/[0.03] p-10 backdrop-blur-xl"
            >
              <h3 className="text-3xl font-black">
                {plan.name}
              </h3>

              <div className="mt-6 text-5xl font-black">
                {plan.price}
              </div>

              <p className="mt-5 text-zinc-500 text-lg leading-relaxed">
                {plan.desc}
              </p>

              <button className="w-full mt-10 px-6 py-4 rounded-2xl bg-white text-black font-semibold hover:scale-[1.01] transition">
                Get Started
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* FINAL CTA */}
      <section className="max-w-7xl mx-auto px-6 pb-28">
        <div className="rounded-[48px] border border-white/10 bg-gradient-to-r from-violet-500/10 to-pink-500/10 p-16 md:p-24 text-center relative overflow-hidden">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(139,92,246,0.18),transparent_30%)]" />

          <div className="relative z-10">
            <h2 className="text-5xl md:text-7xl font-black leading-tight tracking-tight">
              Create the Future of
              <span className="block bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">
                AI Content Production
              </span>
            </h2>

            <p className="mt-8 text-zinc-400 text-xl max-w-3xl mx-auto leading-relaxed">
              Transform ideas into fully researched, SEO-optimized,
              multimodal content experiences powered by autonomous AI agents.
            </p>

            <button
              onClick={onStart}
              className="mt-12 px-10 py-5 rounded-2xl bg-white text-black font-bold text-lg shadow-2xl hover:scale-[1.02] transition"
            >
              Launch StudioAI
            </button>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="border-t border-white/10">
        <div className="max-w-7xl mx-auto px-6 py-12 flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 className="text-2xl font-black">
              StudioAI
            </h3>

            <p className="mt-2 text-zinc-500">
              Autonomous Multimodal AI Content Platform
            </p>
          </div>

          <div className="flex items-center gap-8 text-zinc-500">
            <a href="#" className="hover:text-white transition">
              Privacy
            </a>
            <a href="#" className="hover:text-white transition">
              Terms
            </a>
            <a href="#" className="hover:text-white transition">
              GitHub
            </a>
            <a href="#" className="hover:text-white transition">
              Contact
            </a>
          </div>
        </div>
      </footer>
    </div>
  )
}
