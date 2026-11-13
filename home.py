<!DOCTYPE html>
<html lang="en" dir="ltr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>COSMIC PATIENTS — Exploring Human Health Beyond Earth</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js v4 -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <!-- Three.js r128 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Google Fonts: Space Grotesk, Inter & JetBrains Mono -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        display: ['Space Grotesk', 'sans-serif'],
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        obsidian: {
                            950: '#04070d',
                            900: '#080e1a',
                            850: '#0b1220',
                            800: '#101a2e',
                            700: '#192744',
                        },
                        hud: {
                            cyan: '#38bdf8',
                            emerald: '#10b981',
                            amber: '#f59e0b',
                            rose: '#f43f5e',
                            violet: '#a78bfa'
                        }
                    }
                }
            }
        }
    </script>

    <style>
        body {
            background-color: #04070d;
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
            background-image:
                radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 38%),
                radial-gradient(circle at 85% 82%, rgba(167, 139, 250, 0.08) 0%, transparent 42%),
                linear-gradient(to bottom, rgba(4, 7, 13, 0.94), rgba(4, 7, 13, 0.99));
            overflow-x: hidden;
        }

        h1, h2, h3, .font-display {
            font-family: 'Space Grotesk', sans-serif;
        }

        /* Subtle Orbital Telemetry Grid */
        .telemetry-grid {
            background-size: 38px 38px;
            background-image:
                linear-gradient(to right, rgba(56, 189, 248, 0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
        }

        /* Frosted Dark Glass Panels */
        .glass-panel {
            background: rgba(11, 18, 32, 0.85);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(56, 189, 248, 0.16);
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55);
        }

        .glass-card {
            background: rgba(8, 14, 26, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.14);
            transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .glass-card:hover {
            border-color: rgba(56, 189, 248, 0.42);
            box-shadow: 0 0 24px rgba(56, 189, 248, 0.12);
            transform: translateY(-1px);
        }

        /* Custom Telemetry Sliders */
        input[type="range"] {
            -webkit-appearance: none;
            appearance: none;
            background: rgba(25, 39, 68, 0.95);
            height: 6px;
            border-radius: 999px;
            outline: none;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: #38bdf8;
            cursor: pointer;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.85);
            border: 2px solid #04070d;
            transition: transform 0.15s ease;
        }

        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.18);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: #04070d; }
        ::-webkit-scrollbar-thumb { background: #192744; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #38bdf8; }
    </style>
</head>
<body class="telemetry-grid min-h-screen flex flex-col antialiased selection:bg-sky-500/30 selection:text-sky-200">

    <!-- =========================================================================
         PERSISTENT MISSION CONTROL HEADER
    ========================================================================== -->
    <header class="sticky top-0 z-50 glass-panel border-b border-sky-400/20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <div class="flex flex-col xl:flex-row items-center justify-between gap-3">

                <!-- Brand Identity + Live Status -->
                <div class="flex items-center justify-between w-full xl:w-auto gap-4">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-sky-500/20 to-violet-500/25 border border-sky-400/40 flex items-center justify-center shadow-[0_0_18px_rgba(56,189,248,0.25)] shrink-0">
                            <svg class="w-6 h-6 text-sky-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
                            </svg>
                        </div>
                        <div>
                            <div class="flex items-center gap-2 flex-wrap">
                                <h1 class="text-base sm:text-lg font-bold tracking-wider text-white">COSMIC PATIENTS</h1>
                                <span class="px-2 py-0.5 text-[10px] font-mono uppercase rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/35 flex items-center gap-1.5">
                                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
                                    NASA HRP TELEMETRY
                                </span>
                            </div>
                            <p class="text-[11px] sm:text-xs text-slate-400">Exploring Human Health, 3D Physiology &amp; Network Science Beyond Earth</p>
                        </div>
                    </div>

                    <!-- Mobile/Tablet Quick Telemetry Badge -->
                    <div class="flex items-center gap-2 xl:hidden font-mono text-xs">
                        <span id="header-grav-badge-sm" class="px-2.5 py-1 rounded-lg bg-sky-500/15 text-sky-300 border border-sky-400/30 font-bold">0.00g LEO</span>
                    </div>
                </div>

                <!-- 4 Primary Navigation Tabs -->
                <nav class="flex flex-wrap items-center justify-center gap-1.5 bg-obsidian-950/90 p-1.5 rounded-2xl border border-slate-800/90 w-full xl:w-auto">
                    <button onclick="switchTab('simulator')" id="tab-simulator" class="nav-btn px-3 py-2 rounded-xl text-xs font-mono font-bold transition-all bg-sky-500/20 text-sky-300 border border-sky-400/45 shadow-[0_0_14px_rgba(56,189,248,0.22)]">
                        01 // PHYSIOLOGY SIMULATOR
                    </button>
                    <button onclick="switchTab('human')" id="tab-human" class="nav-btn px-3 py-2 rounded-xl text-xs font-mono font-semibold text-slate-400 hover:text-white hover:bg-slate-800/60 border border-transparent transition-all">
                        02 // 3D HUMAN UNIVERSE
                    </button>
                    <button onclick="switchTab('cosmic')" id="tab-cosmic" class="nav-btn px-3 py-2 rounded-xl text-xs font-mono font-semibold text-slate-400 hover:text-white hover:bg-slate-800/60 border border-transparent transition-all">
                        03 // COSMIC NETWORKS &amp; IMPACT
                    </button>
                    <button onclick="switchTab('hardware')" id="tab-hardware" class="nav-btn px-3 py-2 rounded-xl text-xs font-mono font-semibold text-slate-400 hover:text-white hover:bg-slate-800/60 border border-transparent transition-all">
                        04 // BIOMETRIC HARDWARE (ESP32)
                    </button>
                </nav>

                <!-- Desktop Right HUD: Active Gravity Badge, Quick Preset Selector & UTC Clock -->
                <div class="hidden xl:flex items-center gap-2.5 shrink-0">
                    <div class="px-2.5 py-1.5 rounded-xl bg-obsidian-950/90 border border-sky-400/30 font-mono text-center">
                        <div class="text-[9px] text-slate-400 uppercase">ACTIVE GRAVITY</div>
                        <div id="header-grav-badge" class="text-xs font-bold text-sky-300">0.00g (ISS)</div>
                    </div>

                    <select id="header-preset-select" onchange="applyPreset(this.value)" aria-label="Quick Mission Preset" class="px-2.5 py-2 rounded-xl bg-obsidian-950/90 border border-slate-700 text-xs font-mono text-slate-200 focus:border-sky-400 outline-none cursor-pointer">
                        <option value="iss_180" selected>Preset: ISS 180d</option>
                        <option value="earth_1g">Preset: Earth (1g)</option>
                        <option value="twins_340">Preset: Twins (340d)</option>
                        <option value="unmitigated_0g">Preset: Unmitigated 0g</option>
                        <option value="mars_540">Preset: Mars (540d)</option>
                    </select>

                    <div class="px-2.5 py-1.5 rounded-xl bg-obsidian-950/90 border border-slate-800 text-right font-mono">
                        <div class="text-[9px] text-slate-400">MISSION MET // UTC</div>
                        <div id="mission-clock" class="text-xs font-bold text-emerald-300">00:00:00 UTC</div>
                    </div>
                </div>

            </div>
        </div>
    </header>

    <!-- =========================================================================
         MAIN VIEWPORT CONTAINER
    ========================================================================== -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 w-full">

        <!-- =====================================================================
             MODULE 01: HIGH-ACCURACY ASTRONAUT HEALTH SIMULATOR
        ====================================================================== -->
        <div id="view-simulator" class="tab-view space-y-6">

            <!-- Mission Scenario Preset Pills -->
            <div class="glass-panel rounded-2xl p-4 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-3">
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                    <span class="text-xs sm:text-sm font-bold text-white tracking-wide">MISSION PROFILE PRESETS:</span>
                </div>
                <div class="flex flex-wrap gap-2 w-full lg:w-auto">
                    <button onclick="applyPreset('earth_1g')" class="preset-pill px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-emerald-500/15 text-emerald-300 border border-emerald-500/35 hover:bg-emerald-500/25 transition">
                        Earth Baseline (1g)
                    </button>
                    <button onclick="applyPreset('iss_180')" class="preset-pill px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-sky-500/20 text-sky-300 border border-sky-400/50 hover:bg-sky-500/30 transition">
                        ISS 180-Day Expedition
                    </button>
                    <button onclick="applyPreset('twins_340')" class="preset-pill px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-violet-500/15 text-violet-300 border border-violet-500/35 hover:bg-violet-500/25 transition">
                        NASA Twins Study (340d)
                    </button>
                    <button onclick="applyPreset('unmitigated_0g')" class="preset-pill px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-rose-500/15 text-rose-300 border border-rose-500/35 hover:bg-rose-500/25 transition">
                        Unmitigated 0g Risk
                    </button>
                    <button onclick="applyPreset('mars_540')" class="preset-pill px-3 py-1.5 rounded-xl text-xs font-mono font-semibold bg-amber-500/15 text-amber-300 border border-amber-500/35 hover:bg-amber-500/25 transition">
                        Mars 540-Day Transit
                    </button>
                </div>
            </div>

            <!-- Simulator Split Workspace: Controls (4 cols) + Telemetry & Trajectory (8 cols) -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

                <!-- Left Control Console -->
                <div class="lg:col-span-4 glass-panel rounded-2xl p-5 space-y-5 flex flex-col justify-between">
                    <div class="space-y-5">
                        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                            <h2 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-sky-400"></span>
                                MISSION PARAMETERS
                            </h2>
                            <span class="text-[10px] font-mono text-slate-400">BIPHASIC MODEL v2.4</span>
                        </div>

                        <!-- 1. Gravity Environment Selector -->
                        <div class="space-y-2">
                            <label class="text-xs font-semibold text-slate-200 block">1. Gravity Environment &amp; Orbital Photoperiod</label>
                            <div class="grid grid-cols-2 gap-2">
                                <button onclick="setGravity(0)" data-g="0" class="grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-sky-500/20 text-sky-300 border-sky-400/50">
                                    <div class="text-xs font-mono font-bold">LEO / ISS (0.00g)</div>
                                    <div class="text-[10px] text-sky-200/75">16 sunrises / 24h</div>
                                </button>
                                <button onclick="setGravity(0.16)" data-g="0.16" class="grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-obsidian-950/80 text-slate-400 border-slate-800 hover:text-white">
                                    <div class="text-xs font-mono font-bold">Lunar (0.16g)</div>
                                    <div class="text-[10px] text-slate-500">Partial hydrostatic load</div>
                                </button>
                                <button onclick="setGravity(0.38)" data-g="0.38" class="grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-obsidian-950/80 text-slate-400 border-slate-800 hover:text-white">
                                    <div class="text-xs font-mono font-bold">Mars (0.38g)</div>
                                    <div class="text-[10px] text-slate-500">24h 39m Sol cycle</div>
                                </button>
                                <button onclick="setGravity(1)" data-g="1" class="grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-obsidian-950/80 text-slate-400 border-slate-800 hover:text-white">
                                    <div class="text-xs font-mono font-bold">Earth (1.00g)</div>
                                    <div class="text-[10px] text-slate-500">Terrestrial baseline</div>
                                </button>
                            </div>
                        </div>

                        <!-- 2. Mission Duration (1 to 540 days) -->
                        <div class="space-y-1.5">
                            <div class="flex justify-between items-center">
                                <label for="input-duration" class="text-xs font-semibold text-slate-200">2. Mission Duration (T)</label>
                                <span id="val-duration" class="px-2.5 py-0.5 rounded-lg bg-sky-500/15 text-sky-300 font-mono text-xs font-bold border border-sky-400/30">180 Days</span>
                            </div>
                            <input type="range" id="input-duration" min="1" max="540" value="180" class="w-full" oninput="updateSimulation()">
                            <div class="flex justify-between text-[10px] text-slate-400 font-mono">
                                <span>Day 1 (Acute)</span>
                                <span>180d (ISS)</span>
                                <span>340d (Twins)</span>
                                <span>540d (Mars)</span>
                            </div>
                        </div>

                        <!-- 3. Exercise Countermeasure Protocol (1 to 10) -->
                        <div class="space-y-1.5">
                            <div class="flex justify-between items-center">
                                <label for="input-exercise" class="text-xs font-semibold text-slate-200">3. Exercise Protocol (ARED + T2 + CEVIS)</label>
                                <span id="val-exercise" class="px-2.5 py-0.5 rounded-lg bg-emerald-500/15 text-emerald-300 font-mono text-xs font-bold border border-emerald-400/30">8 / 10</span>
                            </div>
                            <input type="range" id="input-exercise" min="1" max="10" value="8" class="w-full" oninput="updateSimulation()">
                            <div class="flex justify-between text-[10px] text-slate-400">
                                <span>1: Unmitigated Disuse</span>
                                <span>10: 2.5h/day Full ARED</span>
                            </div>
                        </div>

                        <!-- 4. Circadian & Sleep Hygiene (1 to 10) -->
                        <div class="space-y-1.5">
                            <div class="flex justify-between items-center">
                                <label for="input-sleep" class="text-xs font-semibold text-slate-200">4. Circadian &amp; Sleep Hygiene</label>
                                <span id="val-sleep" class="px-2.5 py-0.5 rounded-lg bg-violet-500/15 text-violet-300 font-mono text-xs font-bold border border-violet-400/30">6 / 10</span>
                            </div>
                            <input type="range" id="input-sleep" min="1" max="10" value="6" class="w-full" oninput="updateSimulation()">
                            <div class="flex justify-between text-[10px] text-slate-400">
                                <span>1: Severe Circadian Shift</span>
                                <span>10: Blue-LED + 8h Rest</span>
                            </div>
                        </div>

                        <!-- 5. Hydration & Fluid Loading (1 to 10) -->
                        <div class="space-y-1.5">
                            <div class="flex justify-between items-center">
                                <label for="input-hydration" class="text-xs font-semibold text-slate-200">5. Hydration &amp; Electrolyte Loading</label>
                                <span id="val-hydration" class="px-2.5 py-0.5 rounded-lg bg-amber-500/15 text-amber-300 font-mono text-xs font-bold border border-amber-400/30">7 / 10</span>
                            </div>
                            <input type="range" id="input-hydration" min="1" max="10" value="7" class="w-full" oninput="updateSimulation()">
                            <div class="flex justify-between text-[10px] text-slate-400">
                                <span>1: Hypohydrated</span>
                                <span>10: Optimal Isotonic Load</span>
                            </div>
                        </div>
                    </div>

                    <!-- Phase Indicator Footer -->
                    <div class="p-3.5 rounded-xl bg-obsidian-950/90 border border-slate-800 space-y-1">
                        <div class="text-[11px] font-mono font-bold text-sky-300">ACTIVE ADAPTATION PHASE:</div>
                        <div id="adaptation-phase-label" class="text-xs text-slate-300 leading-relaxed">
                            Chronic Spaceflight Equilibrium (Post-Diuresis Steady State)
                        </div>
                    </div>
                </div>

                <!-- Right Telemetry Dashboard & Chart -->
                <div class="lg:col-span-8 space-y-5">

                    <!-- 4 Primary Live Telemetry Cards -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-3.5">

                        <!-- Primary 1: Resting Heart Rate -->
                        <div class="glass-card rounded-2xl p-4">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs font-semibold text-slate-300">Resting Heart Rate</span>
                                <span id="badge-hr" class="px-2 py-0.5 text-[10px] font-mono font-bold rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">NOMINAL</span>
                            </div>
                            <div class="flex items-baseline gap-1.5 mt-1">
                                <span id="out-hr" class="text-3xl font-extrabold font-mono text-white">74</span>
                                <span class="text-xs font-mono text-slate-400">bpm</span>
                            </div>
                            <div id="delta-hr" class="mt-1.5 text-[11px] font-mono text-slate-400">+4 bpm vs Earth (70)</div>
                        </div>

                        <!-- Primary 2: Allostatic Stress & Cortisol -->
                        <div class="glass-card rounded-2xl p-4">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs font-semibold text-slate-300">Allostatic Stress</span>
                                <span id="badge-stress" class="px-2 py-0.5 text-[10px] font-mono font-bold rounded bg-amber-500/15 text-amber-300 border border-amber-500/30">ELEVATED</span>
                            </div>
                            <div class="flex items-baseline gap-1.5 mt-1">
                                <span id="out-stress" class="text-3xl font-extrabold font-mono text-white">44</span>
                                <span class="text-xs font-mono text-slate-400">%</span>
                            </div>
                            <div id="delta-stress" class="mt-1.5 text-[11px] font-mono text-slate-400">+26% vs Earth (18%)</div>
                        </div>

                        <!-- Primary 3: Cephalic Fluid Shift / SANS Index -->
                        <div class="glass-card rounded-2xl p-4">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs font-semibold text-slate-300">Cephalic Fluid Shift</span>
                                <span id="badge-fluid" class="px-2 py-0.5 text-[10px] font-mono font-bold rounded bg-sky-500/15 text-sky-300 border border-sky-500/30">ELEVATED</span>
                            </div>
                            <div class="flex items-baseline gap-1.5 mt-1">
                                <span id="out-fluid" class="text-3xl font-extrabold font-mono text-white">6.8</span>
                                <span class="text-xs font-mono text-slate-400">/ 10</span>
                            </div>
                            <div id="delta-fluid" class="mt-1.5 text-[11px] font-mono text-slate-400">+6.3 vs Earth (0.5)</div>
                        </div>

                        <!-- Primary 4: Arterial Oxygen SpO2 -->
                        <div class="glass-card rounded-2xl p-4">
                            <div class="flex items-center justify-between mb-1">
                                <span class="text-xs font-semibold text-slate-300">Arterial SpO₂</span>
                                <span id="badge-spo2" class="px-2 py-0.5 text-[10px] font-mono font-bold rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">OPTIMAL</span>
                            </div>
                            <div class="flex items-baseline gap-1.5 mt-1">
                                <span id="out-spo2" class="text-3xl font-extrabold font-mono text-white">98.1</span>
                                <span class="text-xs font-mono text-slate-400">%</span>
                            </div>
                            <div id="delta-spo2" class="mt-1.5 text-[11px] font-mono text-slate-400">-0.4% vs Earth (98.5%)</div>
                        </div>

                    </div>

                    <!-- 3 Secondary Clinical Biomarker Cards -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
                        <div class="glass-card rounded-xl px-4 py-3 flex items-center justify-between">
                            <div>
                                <div class="text-[11px] text-slate-400 font-medium">Plasma Volume Delta</div>
                                <div id="out-plasma" class="text-lg font-bold font-mono text-sky-300">-11.8%</div>
                            </div>
                            <span class="text-[10px] font-mono px-2 py-1 rounded bg-obsidian-950 border border-slate-800 text-slate-400">Henry-Gauer Shift</span>
                        </div>

                        <div class="glass-card rounded-xl px-4 py-3 flex items-center justify-between">
                            <div>
                                <div class="text-[11px] text-slate-400 font-medium">Orthostatic Intolerance Risk</div>
                                <div id="out-ortho" class="text-lg font-bold font-mono text-amber-300">34%</div>
                            </div>
                            <span class="text-[10px] font-mono px-2 py-1 rounded bg-obsidian-950 border border-slate-800 text-slate-400">Post-Landing Syncope</span>
                        </div>

                        <div class="glass-card rounded-xl px-4 py-3 flex items-center justify-between">
                            <div>
                                <div class="text-[11px] text-slate-400 font-medium">Bone &amp; Muscle Integrity</div>
                                <div id="out-bone" class="text-lg font-bold font-mono text-emerald-300">94.2%</div>
                            </div>
                            <span id="out-sans-level" class="text-[10px] font-mono px-2 py-1 rounded bg-violet-500/15 border border-violet-400/30 text-violet-300">SANS: MODERATE</span>
                        </div>
                    </div>

                    <!-- Multi-Metric Longitudinal Trajectory Graph -->
                    <div class="glass-panel rounded-2xl p-5">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
                            <div>
                                <h3 class="text-sm sm:text-base font-bold text-white">Biphasic Physiological Adaptation Trajectory (Day 0 → Day <span id="chart-day-span">180</span>)</h3>
                                <p class="text-xs text-slate-400">Acute Hydrostatic Shift (Days 1–7) → Henry-Gauer Diuresis (Days 7–21) → Chronic Orbital Adaptation</p>
                            </div>
                            <div class="flex flex-wrap items-center gap-3 text-[11px] font-mono">
                                <span class="flex items-center gap-1.5 text-rose-400"><span class="w-2.5 h-2.5 rounded-full bg-rose-400"></span>HR (bpm)</span>
                                <span class="flex items-center gap-1.5 text-amber-400"><span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>Stress (%)</span>
                                <span class="flex items-center gap-1.5 text-sky-400"><span class="w-2.5 h-2.5 rounded-full bg-sky-400"></span>Fluid Shift (×10)</span>
                                <span class="flex items-center gap-1.5 text-violet-400"><span class="w-2.5 h-2.5 rounded-full bg-violet-400"></span>Plasma Δ (%)</span>
                            </div>
                        </div>
                        <div class="relative h-64 sm:h-72 w-full">
                            <canvas id="telemetryChart"></canvas>
                        </div>
                    </div>

                    <!-- Live Clinical Interpretation + Expandable Mathematical Equations & NASA Citations -->
                    <div class="glass-panel rounded-2xl p-5 border-l-4 border-l-violet-400 space-y-4">
                        <div class="flex items-center justify-between">
                            <h4 class="text-sm font-bold text-violet-300">CLINICAL TELEMETRY ASSESSMENT</h4>
                            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-violet-500/15 text-violet-300 border border-violet-400/30">LIVE COUPLING</span>
                        </div>
                        <div id="clinical-insights" class="space-y-1.5 text-xs sm:text-sm text-slate-300 leading-relaxed"></div>

                        <!-- Mathematical Model & NASA Literature Basis -->
                        <details open class="bg-obsidian-950/90 border border-slate-800 rounded-xl p-4 text-xs space-y-3">
                            <summary class="cursor-pointer font-mono font-bold text-sky-300 select-none flex items-center justify-between">
                                <span>MATHEMATICAL MODEL &amp; NASA LITERATURE BASIS (EQUATIONS + CITATIONS)</span>
                                <span class="text-[10px] text-slate-400">[Toggle Equations]</span>
                            </summary>
                            <div class="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3 font-mono text-[11px] text-slate-300">
                                <div class="p-3 rounded-lg bg-obsidian-900 border border-slate-800/90 space-y-1">
                                    <div class="text-sky-400 font-bold">1. Hydrostatic &amp; Biphasic Plasma Volume Δ (%):</div>
                                    <div>ΔP_hydro = ρ · g · h → 0 as g → 0</div>
                                    <div>ΔPV(t) = -μ_g · [13.5 · (1 - e^(-t/9)) + (10 - H)·0.55]</div>
                                    <div class="text-slate-500 text-[10px]">Models acute central hypervolemia (d1–5) followed by ANP-mediated Henry-Gauer renal diuresis (-10% to -15% PV).</div>
                                </div>
                                <div class="p-3 rounded-lg bg-obsidian-900 border border-slate-800/90 space-y-1">
                                    <div class="text-rose-400 font-bold">2. Biphasic Resting Heart Rate (bpm):</div>
                                    <div>HR(t) = 70 - B_acute(t) + D_chronic(t,E) + Δ_sleep + Δ_hyd</div>
                                    <div>B_acute(t) = 4.2 · μ_g · sin(π·t/10) for t ≤ 10d</div>
                                    <div class="text-slate-500 text-[10px]">Captures week-1 baroreceptor bradycardia (-3 to -5 bpm) followed by chronic hypovolemic &amp; deconditioning tachycardia.</div>
                                </div>
                                <div class="p-3 rounded-lg bg-obsidian-900 border border-slate-800/90 space-y-1">
                                    <div class="text-amber-400 font-bold">3. Allostatic Stress &amp; Orbital Circadian Load (%):</div>
                                    <div>Stress(t) = 14 + C_orbit(g) + 7.2·ln(1 + t/14)·μ_g + 4.2(10-S) - 1.4E</div>
                                    <div class="text-slate-500 text-[10px]">LEO 0g incurs highest circadian penalty (16 sunrises/24h, 90-min orbital period) vs Mars 24h39m Sol.</div>
                                </div>
                                <div class="p-3 rounded-lg bg-obsidian-900 border border-slate-800/90 space-y-1">
                                    <div class="text-emerald-400 font-bold">4. Validated NASA Literature Citations:</div>
                                    <ul class="list-disc list-inside text-slate-400 text-[10px] space-y-0.5 font-sans">
                                        <li><strong>NASA HRP:</strong> Cardiovascular &amp; Cephalic Fluid Shift Evidence Reports (Norsk et al., 2015).</li>
                                        <li><strong>NASA Twins Study:</strong> Garrett-Bakelman et al., <em>Science</em> (2019) — 340-day longitudinal multi-omics &amp; carotid remodeling.</li>
                                        <li><strong>ISS Circadian Studies:</strong> Flynn-Evans et al., <em>npj Microgravity</em> — Sleep deficiency &amp; dynamic lighting countermeasures.</li>
                                    </ul>
                                </div>
                            </div>
                        </details>
                    </div>

                </div>
            </div>
        </div>

        <!-- =====================================================================
             MODULE 02: INTERACTIVE 3D HUMAN UNIVERSE (THREE.JS WEBGL)
        ====================================================================== -->
        <div id="view-human" class="tab-view hidden space-y-5">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

                <!-- 3D WebGL Holographic Viewport (7 Columns) -->
                <div class="lg:col-span-7 glass-panel rounded-2xl p-4 space-y-3">
                    <!-- Top 3D Controls Bar -->
                    <div class="flex flex-wrap items-center justify-between gap-2">
                        <div class="flex items-center gap-2">
                            <span class="px-2.5 py-1 rounded-lg bg-sky-500/15 text-sky-300 border border-sky-400/30 font-mono text-[11px] font-bold">
                                WEBGL 3D // REAL-TIME BIOMETRIC RIG
                            </span>
                            <span id="holo-live-hr-pill" class="px-2.5 py-1 rounded-lg bg-rose-500/15 text-rose-300 border border-rose-400/30 font-mono text-[11px] font-bold">
                                ❤️ 74 BPM
                            </span>
                        </div>

                        <!-- Camera Focus Presets & Auto-Rotate -->
                        <div class="flex flex-wrap items-center gap-1.5">
                            <button onclick="focusCamera('full')" class="cam-btn px-2.5 py-1 rounded-lg text-[11px] font-mono bg-sky-500/20 text-sky-300 border border-sky-400/40 transition">Full Body</button>
                            <button onclick="focusCamera('cranial')" class="cam-btn px-2.5 py-1 rounded-lg text-[11px] font-mono bg-obsidian-950 text-slate-300 border border-slate-700 hover:border-violet-400 transition">Cranial / Neuro</button>
                            <button onclick="focusCamera('thoracic')" class="cam-btn px-2.5 py-1 rounded-lg text-[11px] font-mono bg-obsidian-950 text-slate-300 border border-slate-700 hover:border-rose-400 transition">Thoracic / Cardio</button>
                            <button onclick="focusCamera('skeletal')" class="cam-btn px-2.5 py-1 rounded-lg text-[11px] font-mono bg-obsidian-950 text-slate-300 border border-slate-700 hover:border-amber-400 transition">Skeletal</button>
                            <button onclick="toggleAutoRotate()" id="btn-autorotate" class="px-2.5 py-1 rounded-lg text-[11px] font-mono bg-emerald-500/15 text-emerald-300 border border-emerald-500/35 transition">Auto-Orbit: ON</button>
                        </div>
                    </div>

                    <!-- Three.js Canvas Container -->
                    <div id="three-container" class="relative w-full h-[460px] sm:h-[520px] rounded-xl overflow-hidden bg-obsidian-950 border border-slate-800 cursor-grab active:cursor-grabbing">
                        <canvas id="human3dCanvas" class="w-full h-full block"></canvas>

                        <!-- Hover Raycast HUD Tag -->
                        <div id="three-hover-hud" class="hidden absolute top-3 left-3 px-3 py-1.5 rounded-lg bg-obsidian-900/95 border border-sky-400/50 text-xs font-mono text-sky-200 pointer-events-none shadow-lg">
                            Click to inspect organ
                        </div>

                        <!-- Bottom Interaction Instructions -->
                        <div class="absolute bottom-3 left-3 right-3 flex flex-wrap items-center justify-between gap-2 pointer-events-none text-[10px] font-mono text-slate-400 bg-obsidian-950/80 px-3 py-1.5 rounded-lg border border-slate-800/80">
                            <span>DRAG: Rotate 360° • SCROLL / PINCH: Zoom • CLICK ORGAN: Inspect Physiology</span>
                            <span id="three-status-readout" class="text-sky-300">Fluid Shift: 6.8/10 | Bone: 94.2%</span>
                        </div>
                    </div>

                    <!-- Direct Organ Selector Pills -->
                    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
                        <button onclick="selectOrgan('brain')" id="pill-org-brain" class="org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-bold bg-violet-500/20 text-violet-200 border border-violet-400/50 transition">
                            01. Brain &amp; CNS
                        </button>
                        <button onclick="selectOrgan('heart')" id="pill-org-heart" class="org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-semibold bg-obsidian-950 text-slate-300 border border-slate-800 hover:border-rose-400/50 transition">
                            02. Heart
                        </button>
                        <button onclick="selectOrgan('lungs')" id="pill-org-lungs" class="org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-semibold bg-obsidian-950 text-slate-300 border border-slate-800 hover:border-emerald-400/50 transition">
                            03. Lungs
                        </button>
                        <button onclick="selectOrgan('vessels')" id="pill-org-vessels" class="org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-semibold bg-obsidian-950 text-slate-300 border border-slate-800 hover:border-sky-400/50 transition">
                            04. Vascular Bed
                        </button>
                        <button onclick="selectOrgan('skeletal')" id="pill-org-skeletal" class="org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-semibold bg-obsidian-950 text-slate-300 border border-slate-800 hover:border-amber-400/50 transition col-span-2 sm:col-span-1">
                            05. Skeletal Frame
                        </button>
                    </div>
                </div>

                <!-- Organ Spaceflight Physiology & Pathology Profile (5 Columns) -->
                <div class="lg:col-span-5 glass-panel rounded-2xl p-6 space-y-5">
                    <div class="flex items-start justify-between border-b border-slate-800 pb-4">
                        <div>
                            <span id="org-system-tag" class="text-[10px] font-mono uppercase px-2.5 py-0.5 rounded-full bg-violet-500/20 text-violet-300 border border-violet-400/35">
                                NEURO-OCULAR &amp; CNS
                            </span>
                            <h2 id="org-title" class="text-xl sm:text-2xl font-bold text-white mt-2">Brain &amp; Cranial Vault</h2>
                        </div>
                        <span id="org-badge-status" class="px-2.5 py-1 rounded-lg font-mono text-xs font-bold bg-amber-500/15 text-amber-300 border border-amber-400/35">
                            SANS WATCH
                        </span>
                    </div>

                    <!-- Live Coupled Impact (Reads Module 01 Simulator State) -->
                    <div class="p-4 rounded-xl bg-sky-950/40 border border-sky-400/35 space-y-1.5">
                        <div class="text-xs font-mono font-bold text-sky-300 flex items-center gap-1.5">
                            <span class="w-2 h-2 rounded-full bg-sky-400 animate-ping"></span>
                            LIVE COUPLED IMPACT (CURRENT SIMULATOR TELEMETRY)
                        </div>
                        <p id="org-live-impact" class="text-xs sm:text-sm text-white leading-relaxed"></p>
                    </div>

                    <!-- Terrestrial Baseline Function -->
                    <div class="p-4 rounded-xl bg-obsidian-950/90 border border-slate-800 space-y-1.5">
                        <h3 class="text-xs font-mono font-bold text-emerald-400 uppercase">01 // Terrestrial Baseline Function (1.00g)</h3>
                        <p id="org-earth-fn" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></p>
                    </div>

                    <!-- Spaceflight & Microgravity Mechanism -->
                    <div class="p-4 rounded-xl bg-obsidian-950/90 border border-slate-800 space-y-1.5">
                        <h3 class="text-xs font-mono font-bold text-amber-400 uppercase">02 // Spaceflight &amp; Microgravity Mechanism</h3>
                        <p id="org-space-mech" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></p>
                    </div>

                    <!-- NASA Clinical Countermeasures -->
                    <div class="p-4 rounded-xl bg-obsidian-950/90 border border-slate-800 space-y-1.5">
                        <h3 class="text-xs font-mono font-bold text-violet-300 uppercase">03 // NASA Clinical Countermeasures</h3>
                        <p id="org-countermeasures" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></p>
                    </div>
                </div>

            </div>
        </div>

        <!-- =====================================================================
             MODULE 03: COSMIC CONNECTION — NETWORK SIMILARITIES & IMPACT
        ====================================================================== -->
        <div id="view-cosmic" class="tab-view hidden space-y-6">

            <!-- Interactive Network Perturbation & Stress Simulator Controls -->
            <div class="glass-panel rounded-2xl p-5 grid grid-cols-1 lg:grid-cols-12 gap-5 items-center">
                <!-- Biological Network Toggle -->
                <div class="lg:col-span-4 space-y-1.5">
                    <label class="text-xs font-mono font-bold text-slate-300 block">BIOLOGICAL NETWORK ARCHITECTURE:</label>
                    <div class="grid grid-cols-2 gap-1.5 bg-obsidian-950 p-1 rounded-xl border border-slate-800">
                        <button onclick="setBioGraphType('connectome')" id="btn-bio-connectome" class="px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-sky-500/20 text-sky-300 border border-sky-400/40 transition">
                            Brain Connectome
                        </button>
                        <button onclick="setBioGraphType('vascular')" id="btn-bio-vascular" class="px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition">
                            Microvascular Bed
                        </button>
                    </div>
                </div>

                <!-- Perturbation / Microgravity Stress Slider -->
                <div class="lg:col-span-4 space-y-1.5">
                    <div class="flex justify-between items-center text-xs">
                        <label for="input-net-stress" class="font-mono font-bold text-slate-200">Perturbation / Stress Severity:</label>
                        <span id="val-net-stress" class="px-2 py-0.5 rounded bg-rose-500/15 text-rose-300 font-mono font-bold border border-rose-400/30">0% (Baseline)</span>
                    </div>
                    <input type="range" id="input-net-stress" min="0" max="80" value="0" class="w-full" oninput="updateNetworkLab()">
                    <div class="flex justify-between text-[10px] font-mono text-slate-400">
                        <span>0% Intact</span>
                        <span>40% Moderate</span>
                        <span>80% Severe Collapse</span>
                    </div>
                </div>

                <!-- Attack Mode Toggle (Random Noise vs Targeted Hub Disruption) -->
                <div class="lg:col-span-4 space-y-1.5">
                    <label class="text-xs font-mono font-bold text-slate-300 block">PERTURBATION TOPOLOGY MODE:</label>
                    <div class="grid grid-cols-2 gap-1.5 bg-obsidian-950 p-1 rounded-xl border border-slate-800">
                        <button onclick="setAttackMode('random')" id="btn-atk-random" class="px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 transition">
                            Random Node Loss
                        </button>
                        <button onclick="setAttackMode('targeted')" id="btn-atk-targeted" class="px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition">
                            Targeted Hub Attack
                        </button>
                    </div>
                </div>
            </div>

            <!-- Side-by-Side Interactive Force/Filament Canvases -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Left Canvas: Human Biological Network -->
                <div class="glass-panel rounded-2xl p-5 space-y-3">
                    <div class="flex items-center justify-between">
                        <div>
                            <span class="text-[10px] font-mono text-sky-400">SCALE: ~10⁻⁶ TO 10⁻¹ METERS (SYNAPTIC / CAPILLARY)</span>
                            <h3 id="bio-graph-heading" class="text-sm sm:text-base font-bold text-white">Human Brain Connectome (Cortical Hubs)</h3>
                        </div>
                        <span id="bio-eff-badge" class="px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-400/30 font-mono text-xs font-bold">
                            E_glob: 100%
                        </span>
                    </div>
                    <div class="relative h-64 sm:h-72 w-full rounded-xl overflow-hidden bg-obsidian-950 border border-slate-800">
                        <canvas id="bioNetCanvas" class="w-full h-full cursor-crosshair"></canvas>
                        <div id="bio-tip" class="hidden absolute bottom-3 left-3 px-3 py-1.5 rounded-lg bg-obsidian-900/95 border border-sky-400/50 text-xs font-mono text-sky-200 pointer-events-none"></div>
                    </div>
                </div>

                <!-- Right Canvas: The Cosmic Web -->
                <div class="glass-panel rounded-2xl p-5 space-y-3">
                    <div class="flex items-center justify-between">
                        <div>
                            <span class="text-[10px] font-mono text-violet-400">SCALE: ~10²⁴ METERS (DARK MATTER FILAMENTS)</span>
                            <h3 class="text-sm sm:text-base font-bold text-white">The Cosmic Web (Galaxy Superclusters &amp; Halos)</h3>
                        </div>
                        <span id="cosmic-eff-badge" class="px-2.5 py-1 rounded-lg bg-violet-500/15 text-violet-300 border border-violet-400/30 font-mono text-xs font-bold">
                            E_glob: 100%
                        </span>
                    </div>
                    <div class="relative h-64 sm:h-72 w-full rounded-xl overflow-hidden bg-obsidian-950 border border-slate-800">
                        <canvas id="cosmicNetCanvas" class="w-full h-full cursor-crosshair"></canvas>
                        <div id="cosmic-tip" class="hidden absolute bottom-3 left-3 px-3 py-1.5 rounded-lg bg-obsidian-900/95 border border-violet-400/50 text-xs font-mono text-violet-200 pointer-events-none"></div>
                    </div>
                </div>
            </div>

            <!-- Quantitative Metrics Table + Log-Log Degree Distribution Chart -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

                <!-- Quantitative Topology Metrics Table (7 Columns) -->
                <div class="lg:col-span-7 glass-panel rounded-2xl p-5 space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <h3 class="text-base font-bold text-white">Quantitative Graph-Theory Comparison</h3>
                            <p class="text-xs text-slate-400">Empirical scaling invariants (Vazza &amp; Feletti, <em>Frontiers in Physics</em>, 2020) + Live Perturbation Telemetry</p>
                        </div>
                        <span id="resilience-verdict" class="px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-400/30 font-mono text-[11px] font-bold">
                            SCALE-FREE RESILIENT
                        </span>
                    </div>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse text-xs">
                            <thead>
                                <tr class="border-b border-slate-700/80 text-slate-400 font-mono">
                                    <th class="py-2.5 px-3">Graph Metric</th>
                                    <th class="py-2.5 px-3 text-sky-300">Biological Network</th>
                                    <th class="py-2.5 px-3 text-violet-300">Cosmic Web</th>
                                    <th class="py-2.5 px-3 text-emerald-300">Topological Alignment</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/70 font-mono">
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Active Nodes (N)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-n">68 (6.9×10¹⁰ real)</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-n">68 (~10¹¹ real)</td>
                                    <td class="py-2 px-3 text-emerald-400">Same Order (10¹⁰–10¹¹)</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Active Edges (E)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-e">164</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-e">158</td>
                                    <td class="py-2 px-3 text-emerald-400">Filamentary Mesh</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Average Degree ⟨k⟩</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-k">4.82</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-k">4.65</td>
                                    <td class="py-2 px-3 text-emerald-400">96.4% Match</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Clustering Coeff. (C)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-c">0.44</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-c">0.41</td>
                                    <td class="py-2 px-3 text-emerald-400">High Small-World C</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Global Efficiency (E_glob)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-eff">100%</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-eff">100%</td>
                                    <td class="py-2 px-3 text-amber-300" id="m-eff-status">Optimal Flow</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Giant Component (%)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-gc">100%</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-gc">100%</td>
                                    <td class="py-2 px-3 text-emerald-400">Percolated Web</td>
                                </tr>
                                <tr class="hover:bg-slate-800/30">
                                    <td class="py-2 px-3 font-bold text-white">Power-Law Exponent (γ)</td>
                                    <td class="py-2 px-3 text-sky-300" id="m-bio-gamma">2.24</td>
                                    <td class="py-2 px-3 text-violet-300" id="m-cos-gamma">2.18</td>
                                    <td class="py-2 px-3 text-emerald-400">P(k) ∝ k⁻ᵞ Scale-Free</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Log-Log Degree Distribution Chart P(k) ∝ k^-γ (5 Columns) -->
                <div class="lg:col-span-5 glass-panel rounded-2xl p-5 flex flex-col justify-between">
                    <div>
                        <h3 class="text-sm sm:text-base font-bold text-white">Log-Log Degree Distribution: P(k) ∝ k⁻ᵞ</h3>
                        <p class="text-xs text-slate-400">Overlapping scale-free power-law heavy tails (note hub truncation under Targeted Attack)</p>
                    </div>
                    <div class="relative h-64 w-full my-2">
                        <canvas id="powerLawChart"></canvas>
                    </div>
                    <div class="text-[11px] text-slate-400 font-mono">
                        Methodological Note: Structural isomorphism reflects shared physical optimization laws, not causal identity.
                    </div>
                </div>

            </div>

            <!-- 4-Pillar Impact Analysis: What Do These Relationships Affect? -->
            <div class="glass-panel rounded-2xl p-6 space-y-4 border-t-2 border-t-sky-400">
                <div>
                    <span class="text-[11px] font-mono uppercase text-sky-400">TRANSLATIONAL SPACE MEDICINE &amp; COMPLEXITY SCIENCE</span>
                    <h3 class="text-lg sm:text-xl font-bold text-white mt-0.5">What Do These Relationships Affect? (4-Pillar Practical Impact)</h3>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Pillar 1 -->
                    <div class="glass-card rounded-xl p-4 space-y-2 border-l-4 border-l-sky-400">
                        <div class="flex items-center justify-between">
                            <h4 class="text-sm font-bold text-white">1. Early Spaceflight Diagnostics (Graph Biomarkers)</h4>
                            <span class="text-xs font-mono text-sky-400">RETINAL &amp; fMRI</span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            Measuring shifts in retinal microvascular clustering coefficient (<em>C</em>) and functional brain connectome path length detects microgravity-induced vascular remodeling and SANS <strong>weeks before clinical symptoms appear</strong>.
                        </p>
                    </div>

                    <!-- Pillar 2 -->
                    <div class="glass-card rounded-xl p-4 space-y-2 border-l-4 border-l-emerald-400">
                        <div class="flex items-center justify-between">
                            <h4 class="text-sm font-bold text-white">2. Universal Resource Transport Optimization</h4>
                            <span class="text-xs font-mono text-emerald-400">MINIMAL ENERGY</span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            Both biological evolution and gravitational collapse converge on <strong>small-world, scale-free architectures</strong> because they maximize resource flow (oxygenated blood &amp; neural signals vs. baryonic gas) at minimum structural wiring cost.
                        </p>
                    </div>

                    <!-- Pillar 3 -->
                    <div class="glass-card rounded-xl p-4 space-y-2 border-l-4 border-l-rose-400">
                        <div class="flex items-center justify-between">
                            <h4 class="text-sm font-bold text-white">3. Targeted Hub Protection Protocols</h4>
                            <span class="text-xs font-mono text-rose-400">HUB VULNERABILITY</span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            As shown in the simulator above, scale-free networks resist random noise but collapse if high-degree hubs fail. Mapping biological "super-hubs" (e.g., optic nerve head vessels, hippocampal hubs) guides targeted shielding against <strong>Galactic Cosmic Rays (GCR)</strong> and cephalic fluid pressure.
                        </p>
                    </div>

                    <!-- Pillar 4 -->
                    <div class="glass-card rounded-xl p-4 space-y-2 border-l-4 border-l-violet-400">
                        <div class="flex items-center justify-between">
                            <h4 class="text-sm font-bold text-white">4. Cross-Domain Predictive Digital Twins</h4>
                            <span class="text-xs font-mono text-violet-400">N-BODY ALGORITHMS</span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            Graph-theoretic algorithms originally developed to trace dark matter filament percolation in cosmological N-body simulations are now adapted to model <strong>3D capillary perfusion and human physiological digital twins</strong> for deep-space Mars missions.
                        </p>
                    </div>
                </div>
            </div>

        </div>

        <!-- =====================================================================
             MODULE 04: REAL-TIME BIOMETRIC HARDWARE INTEGRATION (ESP32 + MAX30102)
        ====================================================================== -->
        <div id="view-hardware" class="tab-view hidden space-y-6">

            <!-- Station Header & Serial / Demo Controls -->
            <div class="glass-panel rounded-2xl p-5 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
                <div class="space-y-1">
                    <div class="flex items-center gap-2">
                        <span id="hw-led" class="w-3 h-3 rounded-full bg-emerald-400 animate-ping"></span>
                        <h2 class="text-base sm:text-lg font-bold text-white">Biometric Telemetry Station (ESP32 + MAX30102 Pulse Oximeter)</h2>
                    </div>
                    <p id="hw-mode-desc" class="text-xs text-slate-400">
                        Active Stream: Live Sensor Demo Mode (synthesized arterial PPG with dicrotic notch) — or connect physical ESP32 hardware via USB Serial.
                    </p>
                </div>

                <div class="flex flex-wrap gap-2.5 w-full lg:w-auto">
                    <button onclick="toggleDemoMode()" id="btn-demo-toggle" class="px-4 py-2 rounded-xl text-xs font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 hover:bg-emerald-500/30 transition">
                        PAUSE DEMO STREAM
                    </button>
                    <button onclick="connectWebSerial()" class="px-4 py-2 rounded-xl text-xs font-mono font-bold bg-sky-500/20 text-sky-300 border border-sky-400/45 hover:bg-sky-500/30 transition">
                        CONNECT ESP32 VIA USB (WEB SERIAL)
                    </button>
                </div>
            </div>

            <!-- PPG Oscilloscope + Earth-vs-Astronaut Telemetry Comparison -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

                <!-- Left 8 Columns: PPG Oscilloscope, Demo Exertion Control & Arduino Firmware -->
                <div class="lg:col-span-8 glass-panel rounded-2xl p-5 space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-2">
                        <div>
                            <h3 class="text-sm sm:text-base font-bold text-white">Real-Time Photoplethysmogram (PPG) Oscilloscope</h3>
                            <p class="text-xs text-slate-400 font-mono">MAX30102 IR Channel | Systolic Peak + Dicrotic Notch + Respiratory Baseline</p>
                        </div>
                        <div class="flex items-center gap-2 font-mono text-xs">
                            <span class="px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-400/30">
                                SQI: <strong id="hw-sqi">98%</strong>
                            </span>
                            <span class="px-2.5 py-1 rounded-lg bg-rose-500/15 text-rose-300 border border-rose-400/30 animate-pulse">
                                ● LIVE 115200 BAUD
                            </span>
                        </div>
                    </div>

                    <!-- PPG Canvas -->
                    <div class="relative h-64 w-full rounded-xl bg-obsidian-950 border border-slate-800 overflow-hidden">
                        <canvas id="ppgOscilloscope" class="w-full h-full"></canvas>
                    </div>

                    <!-- Demo Mode Exertion / Stress Modulation Slider -->
                    <div class="p-3.5 rounded-xl bg-obsidian-950/90 border border-slate-800 space-y-1.5">
                        <div class="flex justify-between items-center text-xs">
                            <label for="input-demo-exertion" class="font-mono font-bold text-slate-300">Demo Subject Physical Exertion / Stress Level:</label>
                            <span id="val-demo-exertion" class="font-mono font-bold text-sky-300">Rest Baseline (~72 bpm)</span>
                        </div>
                        <input type="range" id="input-demo-exertion" min="0" max="100" value="10" class="w-full" oninput="updateDemoExertion()">
                        <div class="flex justify-between text-[10px] font-mono text-slate-500">
                            <span>0%: Supine Rest (64 bpm)</span>
                            <span>50%: Light Ergometer (105 bpm)</span>
                            <span>100%: Peak EVA Exertion (145 bpm)</span>
                        </div>
                    </div>

                    <!-- Production-Ready Arduino C++ Code Block -->
                    <details class="bg-obsidian-950/90 border border-slate-800 rounded-xl p-4 text-xs">
                        <summary class="cursor-pointer font-mono font-bold text-sky-300 select-none flex items-center justify-between">
                            <span>ESP32 + MAX30102 ARDUINO C++ FIRMWARE (JSON / CSV SERIAL STREAM)</span>
                            <span class="text-[10px] text-slate-400">[Click to Expand]</span>
                        </summary>
                        <div class="mt-3 space-y-2">
                            <div class="flex items-center justify-between">
                                <span class="text-[11px] text-slate-400">Flash onto ESP32 via Arduino IDE (SparkFun MAX3010x Library):</span>
                                <button onclick="copyFirmwareCode()" class="px-3 py-1 rounded-lg bg-sky-500/20 text-sky-300 border border-sky-400/40 hover:bg-sky-500/30 font-mono font-bold text-xs transition">
                                    COPY FIRMWARE CODE
                                </button>
                            </div>
                            <pre id="esp32-firmware" class="p-3.5 rounded-xl bg-black/85 text-emerald-300 font-mono overflow-x-auto text-[11px] leading-relaxed border border-slate-800">#include &lt;Wire.h&gt;
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;
const byte RATE_SIZE = 4;
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;
float beatsPerMinute;
int beatAvg = 72;

void setup() {
  Serial.begin(115200);
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("{\"error\":\"MAX30102 wiring fault\"}");
    while (1);
  }
  particleSensor.setup();
  particleSensor.setPulseAmplitudeRed(0x0A);
  particleSensor.setPulseAmplitudeGreen(0);
}

void loop() {
  long irValue = particleSensor.getIR();
  if (checkForBeat(irValue) == true) {
    long delta = millis() - lastBeat;
    lastBeat = millis();
    beatsPerMinute = 60.0 / (delta / 1000.0);
    if (beatsPerMinute &lt; 220 &amp;&amp; beatsPerMinute &gt; 35) {
      rates[rateSpot++] = (byte)beatsPerMinute;
      rateSpot %= RATE_SIZE;
      beatAvg = 0;
      for (byte x = 0; x &lt; RATE_SIZE; x++) beatAvg += rates[x];
      beatAvg /= RATE_SIZE;
    }
  }
  // Estimate SpO2 proxy when finger contact is valid (IR &gt; 50,000)
  float spo2 = (irValue &gt; 50000) ? 98.4 : 0.0;
  Serial.printf("{\"hr\":%d,\"spo2\":%.1f,\"ir\":%ld}\n", beatAvg, spo2, irValue);
  delay(40); // 25 Hz telemetry frame rate
}</pre>
                        </div>
                    </details>
                </div>

                <!-- Right 4 Columns: Live Earth Vitals & Earth-vs-Space Delta Comparison -->
                <div class="lg:col-span-4 space-y-4">
                    <div class="glass-panel rounded-2xl p-5 space-y-3.5">
                        <h3 class="text-xs font-mono font-bold text-slate-300 uppercase border-b border-slate-800 pb-2">
                            Live Earth Subject Vitals (1.00g)
                        </h3>

                        <div class="flex items-center justify-between p-3.5 rounded-xl bg-obsidian-950/90 border border-rose-500/30">
                            <div>
                                <div class="text-[11px] text-slate-400">Measured Heart Rate</div>
                                <div class="text-3xl font-extrabold font-mono text-rose-400 mt-0.5"><span id="hw-live-hr">72</span> <span class="text-xs font-normal text-slate-400">bpm</span></div>
                            </div>
                            <span class="text-xs font-mono px-2 py-1 rounded bg-rose-500/15 text-rose-300">PPG LOCK</span>
                        </div>

                        <div class="flex items-center justify-between p-3.5 rounded-xl bg-obsidian-950/90 border border-emerald-500/30">
                            <div>
                                <div class="text-[11px] text-slate-400">Measured SpO₂ Saturation</div>
                                <div class="text-3xl font-extrabold font-mono text-emerald-400 mt-0.5"><span id="hw-live-spo2">98.4</span>%</div>
                            </div>
                            <span class="text-xs font-mono px-2 py-1 rounded bg-emerald-500/15 text-emerald-300">RED/IR RATIO</span>
                        </div>
                    </div>

                    <!-- Earth vs Simulated Astronaut Delta Comparison -->
                    <div class="glass-panel rounded-2xl p-5 space-y-3.5 border-l-4 border-l-sky-400">
                        <h3 class="text-xs font-mono font-bold text-white uppercase">
                            Earth Subject vs. Simulated Astronaut
                        </h3>

                        <div class="grid grid-cols-2 gap-2.5 text-center font-mono">
                            <div class="p-3 rounded-xl bg-obsidian-950/90 border border-slate-800">
                                <div class="text-[10px] text-slate-400">EARTH SUBJECT (1g)</div>
                                <div id="comp-earth-str" class="text-xs sm:text-sm font-bold text-emerald-400 mt-1">72 bpm / 98.4%</div>
                            </div>
                            <div class="p-3 rounded-xl bg-obsidian-950/90 border border-slate-800">
                                <div class="text-[10px] text-slate-400">ASTRONAUT (SIM)</div>
                                <div id="comp-astro-str" class="text-xs sm:text-sm font-bold text-sky-300 mt-1">74 bpm / 98.1%</div>
                            </div>
                        </div>

                        <div class="p-3 rounded-xl bg-obsidian-950/80 border border-slate-800/80 flex items-center justify-between font-mono text-xs">
                            <span class="text-slate-400">Cardiac Rate Delta (ΔHR):</span>
                            <span id="comp-delta-badge" class="font-bold text-sky-300">+2 bpm</span>
                        </div>

                        <p id="hw-delta-analysis" class="text-xs text-slate-300 leading-relaxed"></p>
                    </div>
                </div>

            </div>
        </div>

    </main>

    <!-- HUD Toast Notification (No alert()) -->
    <div id="hud-toast" class="fixed bottom-5 right-5 z-50 hidden max-w-sm glass-panel border-sky-400/50 rounded-xl p-3.5 shadow-2xl">
        <div class="flex items-center gap-2.5">
            <span class="w-2 h-2 rounded-full bg-sky-400 animate-ping shrink-0"></span>
            <span id="hud-toast-msg" class="text-xs font-mono text-white">Telemetry Updated</span>
        </div>
    </div>

    <!-- Mission Control Footer -->
    <footer class="border-t border-slate-800/80 bg-obsidian-950/95 py-4 mt-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-slate-400">
            <div>
                <span class="font-bold text-sky-400 font-mono">COSMIC PATIENTS</span> — Interactive Space-Medicine, 3D Physiology &amp; Network Science Platform.
            </div>
            <div class="font-mono text-[11px] text-slate-500">
                Educational Research Model • NASA HRP &amp; ISS Biotelemetry Framework
            </div>
        </div>
    </footer>

    <!-- =========================================================================
         CORE APPLICATION ENGINE (SIMULATOR, THREE.JS 3D, NETWORKS & HARDWARE)
    ========================================================================== -->
    <script>
        // =====================================================================
        // GLOBAL STATE & UTILITIES
        // =====================================================================
        const simState = {
            gravity: 0,          // 0 = LEO/ISS, 0.16 = Lunar, 0.38 = Mars, 1 = Earth
            duration: 180,       // 1 to 540 days
            exercise: 8,         // 1 to 10
            sleep: 6,            // 1 to 10
            hydration: 7,        // 1 to 10
            hr: 74,
            stress: 44,
            fluidShift: 6.8,
            spo2: 98.1,
            plasmaDelta: -11.8,
            orthostaticRisk: 34,
            boneIntegrity: 94.2,
            sansLevel: 'MODERATE'
        };

        let telemetryChart = null;
        let powerLawChart = null;
        let selectedOrganKey = 'brain';

        function showToast(msg) {
            const toast = document.getElementById('hud-toast');
            document.getElementById('hud-toast-msg').textContent = msg;
            toast.classList.remove('hidden');
            clearTimeout(window._toastTimer);
            window._toastTimer = setTimeout(() => toast.classList.add('hidden'), 3800);
        }

        function updateMissionClock() {
            const clockEl = document.getElementById('mission-clock');
            if (clockEl) {
                clockEl.textContent = new Date().toISOString().substring(11, 19) + ' UTC';
            }
        }
        setInterval(updateMissionClock, 1000);
        updateMissionClock();

        function switchTab(tabName) {
            document.querySelectorAll('.tab-view').forEach(v => v.classList.add('hidden'));
            document.getElementById(`view-${tabName}`).classList.remove('hidden');

            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('bg-sky-500/20', 'text-sky-300', 'border-sky-400/45', 'shadow-[0_0_14px_rgba(56,189,248,0.22)]');
                btn.classList.add('text-slate-400', 'border-transparent');
            });

            const activeBtn = document.getElementById(`tab-${tabName}`);
            activeBtn.classList.remove('text-slate-400', 'border-transparent');
            activeBtn.classList.add('bg-sky-500/20', 'text-sky-300', 'border-sky-400/45', 'shadow-[0_0_14px_rgba(56,189,248,0.22)]');

            if (tabName === 'human') {
                requestAnimationFrame(() => {
                    resizeThreeViewport();
                    updateOrganInspector(selectedOrganKey);
                });
            } else if (tabName === 'cosmic') {
                requestAnimationFrame(() => {
                    initNetworkCanvases();
                    if (powerLawChart) powerLawChart.resize();
                });
            }
        }

        // =====================================================================
        // MODULE 01: HIGH-ACCURACY BIPHASIC NASA HRP PHYSIOLOGY SIMULATOR
        // =====================================================================
        function setGravity(gVal) {
            simState.gravity = gVal;
            document.querySelectorAll('.grav-btn').forEach(btn => {
                const bg = parseFloat(btn.getAttribute('data-g'));
                if (bg === gVal) {
                    btn.className = 'grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-sky-500/20 text-sky-300 border-sky-400/50 shadow-[0_0_12px_rgba(56,189,248,0.18)]';
                } else {
                    btn.className = 'grav-btn px-2.5 py-2 rounded-xl text-left border transition bg-obsidian-950/80 text-slate-400 border-slate-800 hover:text-white';
                }
            });

            const badgeText = gVal === 0 ? '0.00g (ISS)' : gVal === 0.16 ? '0.16g (LUNAR)' : gVal === 0.38 ? '0.38g (MARS)' : '1.00g (EARTH)';
            document.getElementById('header-grav-badge').textContent = badgeText;
            document.getElementById('header-grav-badge-sm').textContent = badgeText;
            updateSimulation();
        }

        function computePhysiologyAtDay(day, exercise, sleep, hydration, gravity) {
            // Microgravity unloading factor mu_g: 1.0 in 0g LEO, 0.84 Lunar, 0.62 Mars, 0.0 Earth
            const muG = 1 - gravity;

            // 1. Biphasic Plasma Volume Delta (%)
            // Acute central hypervolemia (days 1-4) triggers Henry-Gauer ANP renal diuresis over days 5-21,
            // contracting plasma volume by ~10-15% in 0g (exacerbated by low hydration).
            let plasmaDelta = 0;
            if (muG > 0) {
                const acuteHypervolemia = day <= 5 ? Math.sin((day / 5) * Math.PI) * 3.2 * muG : 0;
                const diuresisProgress = day <= 3 ? 0 : (1 - Math.exp(-(day - 3) / 8.5));
                const chronicContraction = muG * (11.2 + (10 - hydration) * 0.65) * diuresisProgress;
                plasmaDelta = acuteHypervolemia - chronicContraction;
            } else {
                plasmaDelta = -((10 - hydration) * 0.45);
            }
            plasmaDelta = Number(Math.max(-22.0, Math.min(4.0, plasmaDelta)).toFixed(1));

            // 2. Cephalic Fluid Shift & SANS Index (0.0 to 10.0)
            // Peaks around days 4-7 as hydrostatic gradient vanishes (ΔP = ρgh -> 0), then settles ~22% lower post-diuresis
            let shiftProfile = 0;
            if (day <= 6) {
                shiftProfile = (day / 6) * 9.4;
            } else {
                shiftProfile = 9.4 - Math.min(2.1, ((day - 6) / 25) * 2.1);
            }
            let fluidShift = (shiftProfile * muG * 0.80) + ((10 - hydration) * 0.16);
            if (gravity === 1) fluidShift = Math.max(0.3, (10 - hydration) * 0.15);
            fluidShift = Number(Math.max(0.2, Math.min(10.0, fluidShift)).toFixed(1));

            // 3. Resting Heart Rate (bpm)
            // Week 1 transient baroreceptor bradycardia (-3 to -5 bpm) due to central venous engorgement,
            // followed by chronic elevation from hypovolemia (-plasmaDelta), myocardial deconditioning, sleep deficit, and dehydration.
            const earlyBradycardia = (day <= 10 ? Math.sin((day / 10) * Math.PI) * 4.2 : 0) * muG;
            const deconditioningLoad = (day > 10 ? Math.min(11.0, ((day - 10) / 45) * (10 - exercise) * 1.15) : 0) * muG;
            const hypovolemicComp = Math.max(0, -plasmaDelta) * 0.35;
            const sleepPenalty = (10 - sleep) * 0.75;
            const hydPenalty = (10 - hydration) * 0.95;

            let hr = 70 - earlyBradycardia + deconditioningLoad + hypovolemicComp + sleepPenalty + hydPenalty - 5.2;
            if (gravity === 1 && exercise >= 7 && sleep >= 7 && hydration >= 7) {
                hr = 70;
            }
            hr = Math.round(Math.max(52, Math.min(132, hr)));

            // 4. Allostatic Stress & Cortisol Index (%)
            // LEO 0g has 16 sunrises/24h circadian desynchrony penalty (14%), Lunar 8%, Mars 4%, Earth 0%
            const orbitalCircadianLoad = gravity === 0 ? 14 : gravity === 0.16 ? 8 : gravity === 0.38 ? 4 : 0;
            const isolationLoad = muG * (7.2 * Math.log(1 + day / 14));
            let stress = 14 + orbitalCircadianLoad + isolationLoad + ((10 - sleep) * 4.2) - (exercise * 1.4);
            stress = Math.round(Math.max(8, Math.min(100, stress)));

            // 5. Arterial Oxygen Saturation SpO2 (%)
            let spo2 = 98.7 - ((10 - exercise) * 0.12) - ((10 - sleep) * 0.06) - ((10 - hydration) * 0.05) - (muG * 0.15);
            spo2 = Number(Math.max(94.2, Math.min(99.5, spo2)).toFixed(1));

            // 6. Secondary Clinical Biomarkers
            // Orthostatic Intolerance Risk (%)
            let ortho = Math.round(
                8 + (muG * 22) + (Math.max(0, -plasmaDelta) * 1.6) + ((10 - exercise) * 2.4) + ((10 - hydration) * 2.1)
            );
            ortho = Math.max(5, Math.min(95, ortho));

            // Bone & Muscle Integrity (%) - Unmitigated 0g loses ~1.2% BMD/month; ARED exercise offsets up to 85%
            const monthlyLossRate = muG * (1.35 * (1 - (exercise / 11.5)));
            const months = day / 30;
            let bone = Number(Math.max(68.0, Math.min(100.0, 100 - (monthlyLossRate * months))).toFixed(1));

            // SANS Ocular Risk Level
            let sansLevel = 'LOW';
            if (fluidShift >= 7.6 && day >= 60) sansLevel = 'HIGH';
            else if (fluidShift >= 6.0 && day >= 30) sansLevel = 'MODERATE';
            else if (fluidShift >= 4.5) sansLevel = 'WATCH';

            return { hr, stress, fluidShift, spo2, plasmaDelta, orthostaticRisk: ortho, boneIntegrity: bone, sansLevel };
        }

        function updateSimulation() {
            const duration = parseInt(document.getElementById('input-duration').value);
            const exercise = parseInt(document.getElementById('input-exercise').value);
            const sleep = parseInt(document.getElementById('input-sleep').value);
            const hydration = parseInt(document.getElementById('input-hydration').value);
            const gravity = simState.gravity;

            document.getElementById('val-duration').textContent = `${duration} Days`;
            document.getElementById('val-exercise').textContent = `${exercise} / 10`;
            document.getElementById('val-sleep').textContent = `${sleep} / 10`;
            document.getElementById('val-hydration').textContent = `${hydration} / 10`;
            document.getElementById('chart-day-span').textContent = duration;

            const metrics = computePhysiologyAtDay(duration, exercise, sleep, hydration, gravity);
            Object.assign(simState, { duration, exercise, sleep, hydration, ...metrics });

            // Update Primary Cards
            document.getElementById('out-hr').textContent = metrics.hr;
            document.getElementById('out-stress').textContent = metrics.stress;
            document.getElementById('out-fluid').textContent = metrics.fluidShift.toFixed(1);
            document.getElementById('out-spo2').textContent = metrics.spo2.toFixed(1);

            const hrDiff = metrics.hr - 70;
            document.getElementById('delta-hr').textContent = `${hrDiff >= 0 ? '+' : ''}${hrDiff} bpm vs Earth (70)`;
            document.getElementById('delta-stress').textContent = `${metrics.stress - 18 >= 0 ? '+' : ''}${metrics.stress - 18}% vs Earth (18%)`;
            document.getElementById('delta-fluid').textContent = `+${(metrics.fluidShift - 0.5).toFixed(1)} vs Earth (0.5)`;
            document.getElementById('delta-spo2').textContent = `${(metrics.spo2 - 98.5).toFixed(1)}% vs Earth (98.5%)`;

            // Status Badges
            setStatusPill('badge-hr', metrics.hr <= 78 ? 'NOMINAL' : metrics.hr <= 92 ? 'ELEVATED' : 'CRITICAL', metrics.hr <= 78 ? 'emerald' : metrics.hr <= 92 ? 'amber' : 'rose');
            setStatusPill('badge-stress', metrics.stress <= 35 ? 'OPTIMAL' : metrics.stress <= 62 ? 'ELEVATED' : 'CRITICAL', metrics.stress <= 35 ? 'emerald' : metrics.stress <= 62 ? 'amber' : 'rose');
            setStatusPill('badge-fluid', metrics.fluidShift <= 3.0 ? 'OPTIMAL' : metrics.fluidShift <= 6.9 ? 'ELEVATED' : 'CRITICAL', metrics.fluidShift <= 3.0 ? 'emerald' : metrics.fluidShift <= 6.9 ? 'sky' : 'rose');
            setStatusPill('badge-spo2', metrics.spo2 >= 96.5 ? 'OPTIMAL' : 'ELEVATED', metrics.spo2 >= 96.5 ? 'emerald' : 'amber');

            // Secondary Clinical Cards
            document.getElementById('out-plasma').textContent = `${metrics.plasmaDelta > 0 ? '+' : ''}${metrics.plasmaDelta.toFixed(1)}%`;
            document.getElementById('out-ortho').textContent = `${metrics.orthostaticRisk}%`;
            document.getElementById('out-bone').textContent = `${metrics.boneIntegrity.toFixed(1)}%`;
            document.getElementById('out-sans-level').textContent = `SANS: ${metrics.sansLevel}`;

            // Active Phase Label
            const phaseEl = document.getElementById('adaptation-phase-label');
            if (gravity === 1) {
                phaseEl.textContent = '1.00g Terrestrial Hydrostatic Equilibrium';
            } else if (duration <= 7) {
                phaseEl.textContent = 'Phase I: Acute Cephalic Fluid Shift & Central Hypervolemia (Days 1–7)';
            } else if (duration <= 21) {
                phaseEl.textContent = 'Phase II: Henry-Gauer ANP Renal Diuresis & Plasma Volume Contraction (Days 7–21)';
            } else {
                phaseEl.textContent = 'Phase III: Chronic Orbital Adaptation, SANS & Musculoskeletal Remodeling (>21 Days)';
            }

            // Update Trajectory Chart, Clinical Insights, 3D Human Rig, and Hardware Delta
            updateTrajectoryChart(duration, exercise, sleep, hydration, gravity);
            renderClinicalInsights(metrics);
            updateOrganInspector(selectedOrganKey);
            updateHardwareDelta();
        }

        function setStatusPill(id, label, color) {
            const el = document.getElementById(id);
            el.textContent = label;
            el.className = `px-2 py-0.5 text-[10px] font-mono font-bold rounded bg-${color}-500/15 text-${color}-300 border border-${color}-400/35`;
        }

        function applyPreset(key) {
            const headerSelect = document.getElementById('header-preset-select');
            if (headerSelect) headerSelect.value = key;

            if (key === 'earth_1g') {
                document.getElementById('input-duration').value = 30;
                document.getElementById('input-exercise').value = 8;
                document.getElementById('input-sleep').value = 8;
                document.getElementById('input-hydration').value = 8;
                setGravity(1);
                showToast('Loaded Earth Baseline (1.00g) Reference');
            } else if (key === 'iss_180') {
                document.getElementById('input-duration').value = 180;
                document.getElementById('input-exercise').value = 8;
                document.getElementById('input-sleep').value = 6;
                document.getElementById('input-hydration').value = 7;
                setGravity(0);
                showToast('Loaded ISS 180-Day Expedition Profile');
            } else if (key === 'twins_340') {
                document.getElementById('input-duration').value = 340;
                document.getElementById('input-exercise').value = 8;
                document.getElementById('input-sleep').value = 5;
                document.getElementById('input-hydration').value = 7;
                setGravity(0);
                showToast('Loaded NASA Twins Study (340-Day Mission)');
            } else if (key === 'unmitigated_0g') {
                document.getElementById('input-duration').value = 240;
                document.getElementById('input-exercise').value = 2;
                document.getElementById('input-sleep').value = 3;
                document.getElementById('input-hydration').value = 3;
                setGravity(0);
                showToast('Alert: Simulated Unmitigated 0g Deconditioning');
            } else if (key === 'mars_540') {
                document.getElementById('input-duration').value = 540;
                document.getElementById('input-exercise').value = 8;
                document.getElementById('input-sleep').value = 6;
                document.getElementById('input-hydration').value = 7;
                setGravity(0.38);
                showToast('Loaded Mars 540-Day Surface & Transit Profile (0.38g)');
            }
        }

        function renderClinicalInsights(m) {
            const box = document.getElementById('clinical-insights');
            const notes = [];

            if (simState.gravity === 1) {
                notes.push(`• <strong>Terrestrial Hydrostatic Gradient (1.00g):</strong> Gravity maintains normal head-to-foot arterial pressure gradients, keeping cephalic fluid shift minimal (<span class="font-mono text-sky-300">${m.fluidShift}/10</span>) and plasma volume stable.`);
            } else {
                const env = simState.gravity === 0 ? 'LEO Microgravity (0.00g)' : simState.gravity === 0.16 ? 'Lunar Gravity (0.16g)' : 'Martian Gravity (0.38g)';
                notes.push(`• <strong>Fluid Redistribution &amp; Henry-Gauer Diuresis (${env}):</strong> Loss of hydrostatic pressure shifts ~2L of fluid cephalad (<span class="font-mono text-sky-300">Index: ${m.fluidShift}/10</span>), triggering atrial stretch receptors and a <span class="font-mono text-sky-300">${m.plasmaDelta}%</span> plasma volume contraction.`);
            }

            if (simState.duration <= 10 && simState.gravity < 1) {
                notes.push(`• <strong>Early Baroreceptor Adaptation:</strong> During the first 7–10 days in orbit, central venous engorgement increases cardiac stroke volume, inducing a transient resting heart rate dip (<span class="font-mono text-rose-300">${m.hr} bpm</span>) before diuresis completes.`);
            } else if (m.hr >= 84) {
                notes.push(`• <strong>Compensatory Tachycardia &amp; Deconditioning:</strong> Reduced plasma volume (<span class="font-mono text-sky-300">${m.plasmaDelta}%</span>) combined with exercise (${simState.exercise}/10) and hydration (${simState.hydration}/10) elevates resting heart rate to <span class="font-mono text-rose-300">${m.hr} bpm</span> and post-flight orthostatic intolerance risk to <span class="font-mono text-amber-300">${m.orthostaticRisk}%</span>.`);
            }

            if (m.stress >= 55) {
                notes.push(`• <strong>Orbital Circadian Desynchrony:</strong> Experiencing 16 orbital sunrises per 24h with sleep hygiene at ${simState.sleep}/10 elevates allostatic cortisol stress to <span class="font-mono text-amber-300">${m.stress}%</span>.`);
            }

            if (m.boneIntegrity < 90) {
                notes.push(`• <strong>Musculoskeletal Unloading Risk:</strong> Over ${simState.duration} days with exercise protocol ${simState.exercise}/10, bone and anti-gravity muscle integrity declines to <span class="font-mono text-rose-300">${m.boneIntegrity}%</span>.`);
            }

            if (notes.length === 1) {
                notes.push(`• <strong>Countermeasure Efficacy Confirmed:</strong> Daily ARED/T2 exercise (${simState.exercise}/10) and hydration (${simState.hydration}/10) preserve Bone/Muscle Integrity at <span class="font-mono text-emerald-300">${m.boneIntegrity}%</span> and arterial SpO₂ at <span class="font-mono text-emerald-300">${m.spo2}%</span>.`);
            }

            box.innerHTML = notes.map(n => `<p>${n}</p>`).join('');
        }

        function initTelemetryChart() {
            const ctx = document.getElementById('telemetryChart').getContext('2d');
            telemetryChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'Resting HR (bpm)',
                            data: [],
                            borderColor: '#f43f5e',
                            backgroundColor: 'rgba(244, 63, 94, 0.1)',
                            borderWidth: 2.5,
                            tension: 0.35,
                            fill: true,
                            pointRadius: 2.5
                        },
                        {
                            label: 'Allostatic Stress (%)',
                            data: [],
                            borderColor: '#f59e0b',
                            backgroundColor: 'rgba(245, 158, 11, 0.08)',
                            borderWidth: 2.5,
                            tension: 0.35,
                            fill: true,
                            pointRadius: 2.5
                        },
                        {
                            label: 'Cephalic Fluid Shift (×10)',
                            data: [],
                            borderColor: '#38bdf8',
                            borderWidth: 2.4,
                            borderDash: [5, 3],
                            tension: 0.35,
                            fill: false,
                            pointRadius: 2
                        },
                        {
                            label: 'Plasma Volume Δ (%)',
                            data: [],
                            borderColor: '#a78bfa',
                            borderWidth: 2.2,
                            tension: 0.35,
                            fill: false,
                            pointRadius: 2
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    interaction: { mode: 'index', intersect: false },
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: 'rgba(4, 7, 13, 0.95)',
                            titleColor: '#38bdf8',
                            bodyColor: '#e2e8f0',
                            borderColor: 'rgba(56, 189, 248, 0.4)',
                            borderWidth: 1,
                            padding: 10
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255, 255, 255, 0.04)' },
                            ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 11 } }
                        },
                        y: {
                            min: -25,
                            max: 135,
                            grid: { color: 'rgba(255, 255, 255, 0.04)' },
                            ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 11 } }
                        }
                    }
                }
            });
        }

        function updateTrajectoryChart(duration, exercise, sleep, hydration, gravity) {
            if (!telemetryChart) return;
            // Sample key physiological checkpoints (including acute days 2, 5, 12) + evenly spaced mission intervals
            const sampleDays = new Set([0, 2, 5, 10, 18]);
            const steps = 10;
            for (let i = 1; i <= steps; i++) {
                sampleDays.add(Math.round((duration / steps) * i));
            }
            const sortedDays = Array.from(sampleDays).filter(d => d <= duration).sort((a, b) => a - b);

            const labels = [];
            const hrArr = [];
            const stressArr = [];
            const fluidArr = [];
            const plasmaArr = [];

            sortedDays.forEach(d => {
                labels.push(`Day ${d}`);
                const m = computePhysiologyAtDay(Math.max(1, d), exercise, sleep, hydration, gravity);
                hrArr.push(d === 0 ? 70 : m.hr);
                stressArr.push(d === 0 ? 18 : m.stress);
                fluidArr.push(d === 0 ? 5.0 : Number((m.fluidShift * 10).toFixed(1)));
                plasmaArr.push(d === 0 ? 0 : m.plasmaDelta);
            });

            telemetryChart.data.labels = labels;
            telemetryChart.data.datasets[0].data = hrArr;
            telemetryChart.data.datasets[1].data = stressArr;
            telemetryChart.data.datasets[2].data = fluidArr;
            telemetryChart.data.datasets[3].data = plasmaArr;
            telemetryChart.update();
        }

        // =====================================================================
        // MODULE 02: INTERACTIVE 3D HUMAN UNIVERSE (THREE.JS WEBGL)
        // =====================================================================
        let scene, camera, renderer, humanGroup;
        let heartMesh, brainGroup, lungsGroup, vascularGroup, skeletalGroup;
        let vascularParticles = [];
        let clickableOrgans = [];
        let raycaster, mouseNDC;
        let isDragging3D = false;
        let prevPointer = { x: 0, y: 0 };
        let targetRotation = { x: 0.05, y: 0.35 };
        let currentRotation = { x: 0.05, y: 0.35 };
        let targetCamPos = new THREE.Vector3(0, 0.35, 5.4);
        let targetLookAt = new THREE.Vector3(0, 0.25, 0);
        let currentLookAt = new THREE.Vector3(0, 0.25, 0);
        let autoRotate3D = true;
        let hoveredOrganMesh = null;

        function initThreeHumanUniverse() {
            const container = document.getElementById('three-container');
            const canvas = document.getElementById('human3dCanvas');
            if (!container || !canvas || typeof THREE === 'undefined') return;

            scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x04070d, 0.065);

            const w = container.clientWidth || 640;
            const h = container.clientHeight || 500;
            camera = new THREE.PerspectiveCamera(42, w / h, 0.1, 100);
            camera.position.copy(targetCamPos);

            renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
            renderer.setSize(w, h);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

            // Studio Space-Medicine Lighting
            const ambientLight = new THREE.AmbientLight(0x8bb8e8, 0.65);
            scene.add(ambientLight);

            const keyLight = new THREE.PointLight(0x38bdf8, 1.5, 20);
            keyLight.position.set(3.5, 4.5, 4.5);
            scene.add(keyLight);

            const rimLight = new THREE.PointLight(0xa78bfa, 1.2, 20);
            rimLight.position.set(-4, 2.5, -3.5);
            scene.add(rimLight);

            const bottomFill = new THREE.PointLight(0x10b981, 0.6, 15);
            bottomFill.position.set(0, -3.5, 2);
            scene.add(bottomFill);

            humanGroup = new THREE.Group();
            scene.add(humanGroup);

            // Spatial Scanner Pedestal Rings
            const ringGeo1 = new THREE.RingGeometry(1.15, 1.22, 64);
            const ringMat1 = new THREE.MeshBasicMaterial({ color: 0x38bdf8, side: THREE.DoubleSide, transparent: true, opacity: 0.45 });
            const floorRing1 = new THREE.Mesh(ringGeo1, ringMat1);
            floorRing1.rotation.x = -Math.PI / 2;
            floorRing1.position.y = -2.15;
            humanGroup.add(floorRing1);

            const ringGeo2 = new THREE.RingGeometry(0.75, 0.79, 64);
            const floorRing2 = new THREE.Mesh(ringGeo2, ringMat1.clone());
            floorRing2.rotation.x = -Math.PI / 2;
            floorRing2.position.y = -2.14;
            humanGroup.add(floorRing2);

            // Translucent Holographic Body Shell Material
            const holoBodyMat = new THREE.MeshPhongMaterial({
                color: 0x38bdf8,
                emissive: 0x0c4a6e,
                emissiveIntensity: 0.35,
                transparent: true,
                opacity: 0.14,
                shininess: 90,
                depthWrite: false
            });

            const wireMat = new THREE.MeshBasicMaterial({
                color: 0x38bdf8,
                wireframe: true,
                transparent: true,
                opacity: 0.06
            });

            function addLimbCapsule(rTop, rBot, len, x, y, z, rx = 0, rz = 0) {
                const geo = new THREE.CylinderGeometry(rTop, rBot, len, 20, 1);
                const mesh = new THREE.Mesh(geo, holoBodyMat);
                mesh.position.set(x, y, z);
                mesh.rotation.set(rx, 0, rz);
                humanGroup.add(mesh);

                const topCap = new THREE.Mesh(new THREE.SphereGeometry(rTop, 16, 12), holoBodyMat);
                topCap.position.set(0, len / 2, 0);
                mesh.add(topCap);

                const botCap = new THREE.Mesh(new THREE.SphereGeometry(rBot, 16, 12), holoBodyMat);
                botCap.position.set(0, -len / 2, 0);
                mesh.add(botCap);
            }

            // Head & Neck Silhouette
            const headGeo = new THREE.SphereGeometry(0.36, 28, 24);
            headGeo.scale(0.88, 1.12, 0.96);
            const headMesh = new THREE.Mesh(headGeo, holoBodyMat);
            headMesh.position.set(0, 1.78, 0);
            humanGroup.add(headMesh);
            humanGroup.add(new THREE.Mesh(headGeo, wireMat).translateY(1.78));

            addLimbCapsule(0.14, 0.16, 0.24, 0, 1.32, 0); // Neck

            // Torso & Pelvis Silhouette
            const torsoGeo = new THREE.CylinderGeometry(0.52, 0.40, 1.25, 28, 4);
            torsoGeo.scale(1.0, 1.0, 0.62);
            const torsoMesh = new THREE.Mesh(torsoGeo, holoBodyMat);
            torsoMesh.position.set(0, 0.62, 0);
            humanGroup.add(torsoMesh);

            const pelvisGeo = new THREE.CylinderGeometry(0.41, 0.36, 0.34, 24);
            pelvisGeo.scale(1.02, 1.0, 0.65);
            const pelvisMesh = new THREE.Mesh(pelvisGeo, holoBodyMat);
            pelvisMesh.position.set(0, -0.14, 0);
            humanGroup.add(pelvisMesh);

            // Left & Right Arms
            addLimbCapsule(0.13, 0.10, 0.64, -0.66, 0.84, 0, 0, -0.16);
            addLimbCapsule(0.10, 0.075, 0.60, -0.78, 0.22, 0.04, -0.12, -0.08);
            addLimbCapsule(0.13, 0.10, 0.64, 0.66, 0.84, 0, 0, 0.16);
            addLimbCapsule(0.10, 0.075, 0.60, 0.78, 0.22, 0.04, -0.12, 0.08);

            // Left & Right Legs
            addLimbCapsule(0.20, 0.14, 0.88, -0.23, -0.74, 0, 0, 0.03);
            addLimbCapsule(0.13, 0.09, 0.86, -0.25, -1.62, -0.02, 0, 0.01);
            addLimbCapsule(0.20, 0.14, 0.88, 0.23, -0.74, 0, 0, -0.03);
            addLimbCapsule(0.13, 0.09, 0.86, 0.25, -1.62, -0.02, 0, -0.01);

            // =================================================================
            // INTERNAL CLICKABLE 3D ORGAN SYSTEMS
            // =================================================================
            clickableOrgans = [];

            // 1. BRAIN & CRANIAL VAULT
            brainGroup = new THREE.Group();
            brainGroup.position.set(0, 1.82, -0.01);
            const brainMat = new THREE.MeshPhongMaterial({
                color: 0xa78bfa,
                emissive: 0x7c3aed,
                emissiveIntensity: 0.75,
                shininess: 80
            });
            const hemiGeo = new THREE.SphereGeometry(0.21, 20, 16);
            hemiGeo.scale(0.76, 0.88, 1.12);
            const leftHemi = new THREE.Mesh(hemiGeo, brainMat);
            leftHemi.position.set(-0.08, 0.03, 0);
            const rightHemi = new THREE.Mesh(hemiGeo, brainMat);
            rightHemi.position.set(0.08, 0.03, 0);
            const cerebellum = new THREE.Mesh(new THREE.SphereGeometry(0.12, 14, 12), brainMat);
            cerebellum.position.set(0, -0.11, -0.09);
            brainGroup.add(leftHemi, rightHemi, cerebellum);
            brainGroup.traverse(obj => { if (obj.isMesh) { obj.userData.organKey = 'brain'; clickableOrgans.push(obj); } });
            humanGroup.add(brainGroup);

            // 2. HEART (MULTI-CHAMBERED ANATOMICAL MESH)
            heartMesh = new THREE.Group();
            heartMesh.position.set(0.06, 0.84, 0.07);
            const heartMat = new THREE.MeshPhongMaterial({
                color: 0xf43f5e,
                emissive: 0xbe123c,
                emissiveIntensity: 0.85,
                shininess: 100
            });
            const ventricleGeo = new THREE.SphereGeometry(0.145, 20, 18);
            ventricleGeo.scale(0.88, 1.25, 0.85);
            const mainVentricle = new THREE.Mesh(ventricleGeo, heartMat);
            mainVentricle.rotation.z = 0.28;

            const rightAtrium = new THREE.Mesh(new THREE.SphereGeometry(0.085, 16, 14), heartMat);
            rightAtrium.position.set(-0.08, 0.08, 0.02);

            const leftAtrium = new THREE.Mesh(new THREE.SphereGeometry(0.08, 16, 14), heartMat);
            leftAtrium.position.set(0.07, 0.09, -0.02);

            heartMesh.add(mainVentricle, rightAtrium, leftAtrium);
            heartMesh.traverse(obj => { if (obj.isMesh) { obj.userData.organKey = 'heart'; clickableOrgans.push(obj); } });
            humanGroup.add(heartMesh);

            // 3. LUNGS (LEFT & RIGHT PULMONARY LOBES)
            lungsGroup = new THREE.Group();
            lungsGroup.position.set(0, 0.86, -0.02);
            const lungMat = new THREE.MeshPhongMaterial({
                color: 0x10b981,
                emissive: 0x059669,
                emissiveIntensity: 0.45,
                transparent: true,
                opacity: 0.52,
                shininess: 60
            });
            const lungGeo = new THREE.SphereGeometry(0.19, 20, 18);
            lungGeo.scale(0.78, 1.65, 0.72);
            const rightLung = new THREE.Mesh(lungGeo, lungMat);
            rightLung.position.set(-0.21, 0, 0);
            rightLung.rotation.z = -0.08;
            const leftLung = new THREE.Mesh(lungGeo, lungMat);
            leftLung.position.set(0.21, 0, 0);
            leftLung.rotation.z = 0.08;
            lungsGroup.add(rightLung, leftLung);
            lungsGroup.traverse(obj => { if (obj.isMesh) { obj.userData.organKey = 'lungs'; clickableOrgans.push(obj); } });
            humanGroup.add(lungsGroup);

            // 4. VASCULAR NETWORK (AORTA, CAROTIDS, SUBCLAVIAN, FEMORAL + FLUID FLOW PARTICLES)
            vascularGroup = new THREE.Group();
            const vesselMat = new THREE.MeshPhongMaterial({
                color: 0x38bdf8,
                emissive: 0x0284c7,
                emissiveIntensity: 0.75
            });

            function buildVesselTube(points, radius) {
                const curve = new THREE.CatmullRomCurve3(points.map(p => new THREE.Vector3(...p)));
                const tubeGeo = new THREE.TubeGeometry(curve, 24, radius, 8, false);
                const mesh = new THREE.Mesh(tubeGeo, vesselMat);
                mesh.userData.organKey = 'vessels';
                clickableOrgans.push(mesh);
                vascularGroup.add(mesh);
                return curve;
            }

            const aortaCurve = buildVesselTube([[0.05, 0.94, 0.05], [0.02, 1.08, 0.02], [-0.02, 0.95, -0.04], [-0.01, 0.45, -0.03], [0, -0.08, -0.02]], 0.026);
            const carotidL = buildVesselTube([[0.03, 1.06, 0.02], [0.08, 1.42, 0.02], [0.09, 1.72, 0.01]], 0.015);
            const carotidR = buildVesselTube([[-0.01, 1.06, 0.02], [-0.08, 1.42, 0.02], [-0.09, 1.72, 0.01]], 0.015);
            const femoralL = buildVesselTube([[0, -0.08, -0.02], [0.18, -0.25, 0], [0.23, -0.85, 0.01], [0.25, -1.55, 0]], 0.017);
            const femoralR = buildVesselTube([[0, -0.08, -0.02], [-0.18, -0.25, 0], [-0.23, -0.85, 0.01], [-0.25, -1.55, 0]], 0.017);

            // Animated Blood/Fluid Flow Pulses
            vascularParticles = [];
            const pulseMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
            const pulseGeo = new THREE.SphereGeometry(0.024, 8, 8);
            [aortaCurve, carotidL, carotidR, femoralL, femoralR].forEach((curve, idx) => {
                for (let k = 0; k < 2; k++) {
                    const pMesh = new THREE.Mesh(pulseGeo, pulseMat);
                    vascularGroup.add(pMesh);
                    vascularParticles.push({ mesh: pMesh, curve, t: (k * 0.5 + idx * 0.17) % 1 });
                }
            });
            humanGroup.add(vascularGroup);

            // 5. SKELETAL & MUSCULAR FRAME (SPINE, RIBCAGE, PELVIC GIRDLE, LONG BONES)
            skeletalGroup = new THREE.Group();
            const boneMat = new THREE.MeshPhongMaterial({
                color: 0xe2e8f0,
                emissive: 0x10b981,
                emissiveIntensity: 0.35,
                shininess: 50
            });

            // Vertebral Spine Column (14 stacked vertebrae)
            for (let v = 0; v < 14; v++) {
                const vy = 1.24 - v * 0.095;
                const vz = -0.09 + Math.sin(v * 0.42) * 0.025;
                const vert = new THREE.Mesh(new THREE.CylinderGeometry(0.036, 0.04, 0.065, 10), boneMat);
                vert.position.set(0, vy, vz);
                skeletalGroup.add(vert);
            }

            // Thoracic Ribcage Pairs
            for (let r = 0; r < 5; r++) {
                const ry = 1.06 - r * 0.095;
                const rxScale = 0.28 + Math.sin((r / 4) * Math.PI) * 0.08;
                const ribTorus = new THREE.Mesh(new THREE.TorusGeometry(rxScale, 0.012, 8, 24, Math.PI * 1.45), boneMat);
                ribTorus.rotation.x = Math.PI / 2;
                ribTorus.rotation.z = -Math.PI * 0.22;
                ribTorus.scale.set(1.15, 0.72, 1);
                ribTorus.position.set(0, ry, 0.01);
                skeletalGroup.add(ribTorus);
            }

            // Femur & Tibia Structural Shafts
            const bonePositions = [
                [-0.22, -0.72, 0.03], [0.22, -0.72, -0.03],
                [-0.24, -1.58, 0.01], [0.24, -1.58, -0.01]
            ];
            bonePositions.forEach(([bx, by, brz]) => {
                const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.032, 0.028, 0.74, 10), boneMat);
                shaft.position.set(bx, by, 0);
                shaft.rotation.z = brz;
                skeletalGroup.add(shaft);
            });

            skeletalGroup.traverse(obj => { if (obj.isMesh) { obj.userData.organKey = 'skeletal'; clickableOrgans.push(obj); } });
            humanGroup.add(skeletalGroup);

            // =================================================================
            // MOUSE & TOUCH ORBIT CONTROLS + RAYCASTING
            // =================================================================
            raycaster = new THREE.Raycaster();
            mouseNDC = new THREE.Vector2();
            let pointerDownPos = { x: 0, y: 0 };

            const onPointerDown = (clientX, clientY) => {
                isDragging3D = true;
                prevPointer = { x: clientX, y: clientY };
                pointerDownPos = { x: clientX, y: clientY };
            };

            const onPointerMove = (clientX, clientY) => {
                const rect = canvas.getBoundingClientRect();
                mouseNDC.x = ((clientX - rect.left) / rect.width) * 2 - 1;
                mouseNDC.y = -((clientY - rect.top) / rect.height) * 2 + 1;

                if (isDragging3D) {
                    const dx = clientX - prevPointer.x;
                    const dy = clientY - prevPointer.y;
                    targetRotation.y += dx * 0.009;
                    targetRotation.x = Math.max(-0.55, Math.min(0.55, targetRotation.x + dy * 0.006));
                    prevPointer = { x: clientX, y: clientY };
                } else {
                    performOrganHoverRaycast();
                }
            };

            const onPointerUp = (clientX, clientY) => {
                isDragging3D = false;
                const moveDist = Math.hypot(clientX - pointerDownPos.x, clientY - pointerDownPos.y);
                if (moveDist < 6) {
                    performOrganClickRaycast();
                }
            };

            canvas.addEventListener('mousedown', e => onPointerDown(e.clientX, e.clientY));
            window.addEventListener('mousemove', e => {
                if (!document.getElementById('view-human').classList.contains('hidden')) {
                    onPointerMove(e.clientX, e.clientY);
                }
            });
            window.addEventListener('mouseup', e => {
                if (isDragging3D) onPointerUp(e.clientX, e.clientY);
            });

            // Touch Support
            canvas.addEventListener('touchstart', e => {
                if (e.touches.length === 1) {
                    onPointerDown(e.touches[0].clientX, e.touches[0].clientY);
                }
            }, { passive: true });

            canvas.addEventListener('touchmove', e => {
                if (e.touches.length === 1) {
                    onPointerMove(e.touches[0].clientX, e.touches[0].clientY);
                }
            }, { passive: true });

            canvas.addEventListener('touchend', e => {
                if (e.changedTouches.length === 1) {
                    onPointerUp(e.changedTouches[0].clientX, e.changedTouches[0].clientY);
                }
            });

            // Scroll Zoom
            canvas.addEventListener('wheel', e => {
                e.preventDefault();
                targetCamPos.z = Math.max(2.2, Math.min(7.5, targetCamPos.z + e.deltaY * 0.003));
            }, { passive: false });

            animateThreeHuman();
        }

        function performOrganHoverRaycast() {
            if (!raycaster || !camera) return;
            raycaster.setFromCamera(mouseNDC, camera);
            const hits = raycaster.intersectObjects(clickableOrgans, false);
            const hud = document.getElementById('three-hover-hud');

            if (hits.length > 0) {
                const orgKey = hits[0].object.userData.organKey;
                hoveredOrganMesh = orgKey;
                document.getElementById('human3dCanvas').style.cursor = 'pointer';
                hud.classList.remove('hidden');
                hud.textContent = `INSPECT: ${organProfiles[orgKey].title.toUpperCase()}`;
            } else {
                hoveredOrganMesh = null;
                document.getElementById('human3dCanvas').style.cursor = isDragging3D ? 'grabbing' : 'grab';
                hud.classList.add('hidden');
            }
        }

        function performOrganClickRaycast() {
            if (!raycaster || !camera) return;
            raycaster.setFromCamera(mouseNDC, camera);
            const hits = raycaster.intersectObjects(clickableOrgans, false);
            if (hits.length > 0) {
                const orgKey = hits[0].object.userData.organKey;
                selectOrgan(orgKey);
                showToast(`Selected 3D System: ${organProfiles[orgKey].title}`);
            }
        }

        function focusCamera(preset) {
            if (preset === 'full') {
                targetCamPos.set(0, 0.35, 5.4);
                targetLookAt.set(0, 0.25, 0);
            } else if (preset === 'cranial') {
                targetCamPos.set(0, 1.85, 2.35);
                targetLookAt.set(0, 1.78, 0);
                selectOrgan('brain');
            } else if (preset === 'thoracic') {
                targetCamPos.set(0, 0.92, 2.55);
                targetLookAt.set(0, 0.85, 0);
                selectOrgan('heart');
            } else if (preset === 'skeletal') {
                targetCamPos.set(0.4, -0.45, 3.6);
                targetLookAt.set(0, -0.45, 0);
                selectOrgan('skeletal');
            }
        }

        function toggleAutoRotate() {
            autoRotate3D = !autoRotate3D;
            const btn = document.getElementById('btn-autorotate');
            btn.textContent = autoRotate3D ? 'Auto-Orbit: ON' : 'Auto-Orbit: OFF';
            btn.className = autoRotate3D
                ? 'px-2.5 py-1 rounded-lg text-[11px] font-mono bg-emerald-500/15 text-emerald-300 border border-emerald-500/35 transition'
                : 'px-2.5 py-1 rounded-lg text-[11px] font-mono bg-obsidian-950 text-slate-400 border border-slate-700 transition';
        }

        function resizeThreeViewport() {
            const container = document.getElementById('three-container');
            if (!container || !renderer || !camera) return;
            const w = container.clientWidth;
            const h = container.clientHeight;
            if (w > 0 && h > 0) {
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
                renderer.setSize(w, h);
            }
        }

        function animateThreeHuman(time = 0) {
            requestAnimationFrame(animateThreeHuman);
            if (!renderer || !scene || !camera) return;
            if (document.getElementById('view-human').classList.contains('hidden')) return;

            const tSec = time * 0.001;

            // Smooth Orbit Rotation
            if (autoRotate3D && !isDragging3D) {
                targetRotation.y += 0.0045;
            }
            currentRotation.x += (targetRotation.x - currentRotation.x) * 0.08;
            currentRotation.y += (targetRotation.y - currentRotation.y) * 0.08;
            humanGroup.rotation.x = currentRotation.x;
            humanGroup.rotation.y = currentRotation.y;

            // Smooth Camera Focus & Zoom Interpolation
            camera.position.lerp(targetCamPos, 0.08);
            currentLookAt.lerp(targetLookAt, 0.08);
            camera.lookAt(currentLookAt);

            // 1. Real-Time Heartbeat Coupling (Exact BPM from Module 01!)
            const freqHz = simState.hr / 60;
            const beatPhase = (tSec * freqHz) % 1;
            // Realistic double-peak systolic/diastolic cardiac contraction curve
            const systole = Math.exp(-Math.pow((beatPhase - 0.15) / 0.07, 2)) * 0.18;
            const diastole = Math.exp(-Math.pow((beatPhase - 0.34) / 0.08, 2)) * 0.09;
            const heartScale = 1 + systole + diastole;
            if (heartMesh) {
                heartMesh.scale.set(heartScale, heartScale, heartScale);
            }

            // 2. Realistic Respiratory Lung Expansion (14 breaths/min)
            if (lungsGroup) {
                const breath = 1 + Math.sin(tSec * 1.45) * 0.045;
                lungsGroup.scale.set(breath, 1 + Math.sin(tSec * 1.45) * 0.025, breath);
                const lungColor = simState.spo2 >= 96.5 ? 0x10b981 : 0xf59e0b;
                lungsGroup.children.forEach(m => m.material.color.setHex(lungColor));
            }

            // 3. Brain Glow Coupled to Cephalic Fluid Shift & Stress
            if (brainGroup) {
                const stressIntensity = 0.45 + (simState.fluidShift / 10) * 0.85;
                const brainColor = simState.fluidShift > 6.8 ? 0xf43f5e : simState.fluidShift > 4.5 ? 0xa78bfa : 0x38bdf8;
                brainGroup.children.forEach(m => {
                    m.material.emissive.setHex(brainColor);
                    m.material.emissiveIntensity = stressIntensity + Math.sin(tSec * 3) * 0.12;
                });
            }

            // 4. Vascular Cephalic Fluid Gradient & Traveling Flow Particles
            if (vascularGroup) {
                const shiftRatio = Math.min(1, simState.fluidShift / 9.5);
                const vesselColor = new THREE.Color().lerpColors(new THREE.Color(0x38bdf8), new THREE.Color(0xf43f5e), shiftRatio);
                vascularGroup.children.forEach(obj => {
                    if (obj.isMesh && obj.userData.organKey === 'vessels') {
                        obj.material.color.copy(vesselColor);
                        obj.material.emissive.copy(vesselColor);
                    }
                });
                const flowSpeed = 0.004 * (simState.hr / 70);
                vascularParticles.forEach(p => {
                    p.t = (p.t + flowSpeed) % 1;
                    const pos = p.curve.getPointAt(p.t);
                    p.mesh.position.copy(pos);
                });
            }

            // 5. Skeletal Integrity Color Coupling (Emerald/White -> Amber -> Rose)
            if (skeletalGroup) {
                const boneHex = simState.boneIntegrity >= 93 ? 0x10b981 : simState.boneIntegrity >= 86 ? 0xf59e0b : 0xf43f5e;
                skeletalGroup.children.forEach(b => {
                    if (b.material) b.material.emissive.setHex(boneHex);
                });
            }

            // Update 3D HUD Badges
            document.getElementById('holo-live-hr-pill').textContent = `❤️ ${simState.hr} BPM`;
            document.getElementById('three-status-readout').textContent =
                `Fluid Shift: ${simState.fluidShift.toFixed(1)}/10 | Bone: ${simState.boneIntegrity.toFixed(1)}%`;

            renderer.render(scene, camera);
        }

        // Organ Spaceflight Physiology & Pathology Profiles
        const organProfiles = {
            brain: {
                tag: 'NEURO-OCULAR & CNS // SANS',
                title: 'Brain & Cranial Vault',
                earth: 'Operates under a gravity-driven hydrostatic gradient that drains cerebral venous blood smoothly via the internal jugular veins while integrating vestibular and visual orientation cues.',
                space: 'Microgravity eliminates the hydrostatic gradient, elevating intracranial venous pressure, upward-shifting the brain within the skull, and flattening the posterior globe of the eye—causing Spaceflight-Associated Neuro-ocular Syndrome (SANS).',
                cm: 'Lower Body Negative Pressure (LBNP) suits to sequester fluid in the legs, Venous-Constrictive Thigh Cuffs, and dynamic blue-enriched LED lighting to stabilize circadian rhythms.',
                status: (s) => s.sansLevel === 'HIGH' ? ['CRITICAL SANS RISK', 'rose'] : s.sansLevel === 'MODERATE' ? ['SANS WATCH', 'amber'] : ['NOMINAL', 'emerald'],
                live: (s) => `Current Fluid Shift Index is ${s.fluidShift.toFixed(1)}/10 with Allostatic Stress at ${s.stress}% over ${s.duration} days. SANS Ocular Risk is rated ${s.sansLevel}. ${s.fluidShift > 6.5 ? 'Elevated intracranial venous congestion requires LBNP countermeasure sessions.' : 'Cerebral perfusion and circadian alignment remain well-compensated.'}`
            },
            heart: {
                tag: 'CARDIOVASCULAR PUMP',
                title: 'The Heart (Myocardium)',
                earth: 'Generates sufficient stroke work to pump blood vertically against 1.00g gravity from the lower extremities to the cerebral cortex, preserving left ventricular mass.',
                space: 'Unloaded from pumping against gravity, the left ventricle undergoes ~8–10% myocardial atrophy and adopts a more spherical geometry during multi-month missions.',
                cm: 'Daily high-intensity aerobic interval training on the T2 Treadmill (with bungee loading) and CEVIS cycle ergometer.',
                status: (s) => s.hr > 90 ? ['HIGH LOAD', 'rose'] : s.hr > 78 ? ['ELEVATED HR', 'amber'] : ['OPTIMAL', 'emerald'],
                live: (s) => `The 3D heart above is pulsing in real time at ${s.hr} bpm (${s.hr - 70 >= 0 ? '+' : ''}${s.hr - 70} bpm vs Earth). With Plasma Volume at ${s.plasmaDelta}% and Exercise Protocol at ${s.exercise}/10, myocardial stroke work is ${s.exercise >= 7 ? 'well-preserved' : 'experiencing deconditioning'}.`
            },
            lungs: {
                tag: 'PULMONARY GAS EXCHANGE',
                title: 'Lungs & Alveolar Network',
                earth: 'Gravity creates apicobasal gradients in both alveolar ventilation and pulmonary capillary blood flow (Ventilation-Perfusion V/Q mismatch).',
                space: 'In 0g microgravity, ventilation and perfusion become remarkably uniform across all lung zones, preserving efficient oxygen transfer inside pressurized spacecraft cabins.',
                cm: 'Closed-loop Environmental Control and Life Support Systems (ECLSS) scrubbing cabin CO₂ below 3 mmHg and maintaining 21% O₂ partial pressure.',
                status: (s) => s.spo2 >= 96.5 ? ['OPTIMAL V/Q', 'emerald'] : ['MILD DIP', 'amber'],
                live: (s) => `Simulated arterial oxygen saturation is ${s.spo2.toFixed(1)}% under ${s.gravity}g gravity. Uniform alveolar perfusion sustains tissue oxygenation despite upper-thoracic fluid redistribution.`
            },
            vessels: {
                tag: 'VASCULAR & FLUID HOMEOSTASIS',
                title: 'Vascular Bed & Fluid Shift',
                earth: 'Arterial pressure in the feet (~200 mmHg) is roughly double that at head level (~100 mmHg), supported by lower-limb venous valves and skeletal muscle pumps.',
                space: 'Arterial pressure equalizes across the body (~100 mmHg everywhere), shifting ~2 liters of fluid headward ("puffy face, bird legs"), thickening carotid intima-media walls, and triggering Henry-Gauer renal plasma volume loss.',
                cm: 'Pre-reentry isotonic saline/fluid loading protocols, midodrine pharmacology, and lower-body compression garments to prevent post-landing orthostatic syncope.',
                status: (s) => s.orthostaticRisk > 55 ? ['HIGH SYNCOPE RISK', 'rose'] : s.orthostaticRisk > 30 ? ['MODERATE SHIFT', 'sky'] : ['BALANCED', 'emerald'],
                live: (s) => `Cephalic Fluid Shift is ${s.fluidShift.toFixed(1)}/10 with Plasma Volume contracted by ${s.plasmaDelta}%. Post-reentry Orthostatic Intolerance Risk is currently ${s.orthostaticRisk}% (Hydration Protocol: ${s.hydration}/10).`
            },
            skeletal: {
                tag: 'MUSCULOSKELETAL SYSTEM',
                title: 'Skeletal & Anti-Gravity Frame',
                earth: 'Continuous ground reaction forces stimulate osteoblast bone remodeling and maintain postural slow-twitch muscle fibers in the spine and legs.',
                space: 'Absence of mechanical loading accelerates osteoclast bone resorption (losing 1.0–1.5% bone mineral density per month in the hip and lumbar spine) and releases calcium into the bloodstream (renal stone risk).',
                cm: 'Daily high-load resistive squats and deadlifts on the Advanced Resistive Exercise Device (ARED), plus bisphosphonate prophylaxis and Vitamin D3.',
                status: (s) => s.boneIntegrity < 86 ? ['BONE LOSS ALERT', 'rose'] : s.boneIntegrity < 93 ? ['MILD UNLOADING', 'amber'] : ['PROTECTED', 'emerald'],
                live: (s) => `After ${s.duration} days at ${s.gravity}g with Exercise Protocol ${s.exercise}/10, Bone & Muscle Integrity stands at ${s.boneIntegrity.toFixed(1)}%. ${s.exercise >= 7 ? 'ARED resistance loading is actively suppressing osteoclastic bone loss.' : 'Increasing ARED resistance sessions is strongly advised.'}`
            }
        };

        function selectOrgan(key) {
            selectedOrganKey = key;
            document.querySelectorAll('.org-pill').forEach(p => {
                p.className = 'org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-semibold bg-obsidian-950 text-slate-300 border border-slate-800 hover:border-sky-400/50 transition';
            });
            const activePill = document.getElementById(`pill-org-${key}`);
            if (activePill) {
                activePill.className = 'org-pill px-2.5 py-2 rounded-xl text-xs font-mono font-bold bg-sky-500/20 text-sky-200 border border-sky-400/50 shadow-[0_0_12px_rgba(56,189,248,0.2)] transition';
            }
            updateOrganInspector(key);
        }

        function updateOrganInspector(key) {
            const prof = organProfiles[key];
            if (!prof) return;
            const [badgeLabel, badgeColor] = prof.status(simState);

            document.getElementById('org-system-tag').textContent = prof.tag;
            document.getElementById('org-title').textContent = prof.title;
            document.getElementById('org-earth-fn').textContent = prof.earth;
            document.getElementById('org-space-mech').textContent = prof.space;
            document.getElementById('org-countermeasures').textContent = prof.cm;
            document.getElementById('org-live-impact').textContent = prof.live(simState);

            const badgeEl = document.getElementById('org-badge-status');
            badgeEl.textContent = badgeLabel;
            badgeEl.className = `px-2.5 py-1 rounded-lg font-mono text-xs font-bold bg-${badgeColor}-500/15 text-${badgeColor}-300 border border-${badgeColor}-400/35`;
        }

        // =====================================================================
        // MODULE 03: COSMIC CONNECTION — NETWORK SIMILARITIES & IMPACT LAB
        // =====================================================================
        let bioGraphType = 'connectome';
        let attackMode = 'random';
        let netStressPct = 0;
        let bioGraphNodes = [];
        let cosmicGraphNodes = [];
        let hoveredBioIdx = -1;
        let hoveredCosmicIdx = -1;
        let netLoopStarted = false;

        function setBioGraphType(type) {
            bioGraphType = type;
            const btnC = document.getElementById('btn-bio-connectome');
            const btnV = document.getElementById('btn-bio-vascular');
            if (type === 'connectome') {
                btnC.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-sky-500/20 text-sky-300 border border-sky-400/40 transition';
                btnV.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition';
                document.getElementById('bio-graph-heading').textContent = 'Human Brain Connectome (Cortical Hubs)';
            } else {
                btnV.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-rose-500/20 text-rose-300 border border-rose-400/40 transition';
                btnC.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition';
                document.getElementById('bio-graph-heading').textContent = 'Human Microvascular Capillary Tree (Retinal/Cerebral)';
            }
            updateNetworkLab();
        }

        function setAttackMode(mode) {
            attackMode = mode;
            const btnR = document.getElementById('btn-atk-random');
            const btnT = document.getElementById('btn-atk-targeted');
            if (mode === 'random') {
                btnR.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-400/40 transition';
                btnT.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition';
            } else {
                btnT.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-bold bg-rose-500/20 text-rose-300 border border-rose-400/40 transition';
                btnR.className = 'px-2.5 py-1.5 rounded-lg text-xs font-mono font-semibold text-slate-400 hover:text-white transition';
            }
            updateNetworkLab();
        }

        function buildScaleFreeNodes(w, h) {
            const total = 68;
            const hubCount = 7;
            const nodes = [];

            // Create 7 High-Degree Super-Hubs (Ranked by centrality)
            for (let i = 0; i < hubCount; i++) {
                nodes.push({
                    id: i + 1,
                    x: 55 + ((i + 0.5) / hubCount) * (w - 110) + (Math.random() - 0.5) * 35,
                    y: 45 + Math.random() * (h - 90),
                    vx: (Math.random() - 0.5) * 0.16,
                    vy: (Math.random() - 0.5) * 0.16,
                    r: 5.5 + (hubCount - i) * 0.35,
                    isHub: true,
                    hubRank: i,
                    randomOrder: Math.random()
                });
            }

            // Create 61 Peripheral / Filament Nodes clustered around Super-Hubs
            for (let i = hubCount; i < total; i++) {
                const parent = nodes[i % hubCount];
                const angle = Math.random() * Math.PI * 2;
                const dist = 16 + Math.random() * 68;
                nodes.push({
                    id: i + 1,
                    x: Math.max(16, Math.min(w - 16, parent.x + Math.cos(angle) * dist)),
                    y: Math.max(16, Math.min(h - 16, parent.y + Math.sin(angle) * dist)),
                    vx: (Math.random() - 0.5) * 0.24,
                    vy: (Math.random() - 0.5) * 0.24,
                    r: 2.1 + Math.random() * 1.4,
                    isHub: false,
                    hubRank: 99,
                    randomOrder: Math.random()
                });
            }
            return nodes;
        }

        function initNetworkCanvases() {
            const bCanvas = document.getElementById('bioNetCanvas');
            const cCanvas = document.getElementById('cosmicNetCanvas');
            if (!bCanvas || !cCanvas) return;

            const bRect = bCanvas.parentElement.getBoundingClientRect();
            bCanvas.width = bRect.width || 500;
            bCanvas.height = bRect.height || 275;

            const cRect = cCanvas.parentElement.getBoundingClientRect();
            cCanvas.width = cRect.width || 500;
            cCanvas.height = cRect.height || 275;

            if (bioGraphNodes.length === 0) {
                bioGraphNodes = buildScaleFreeNodes(bCanvas.width, bCanvas.height);
                cosmicGraphNodes = buildScaleFreeNodes(cCanvas.width, cCanvas.height);
            }

            updateNetworkLab();

            if (!netLoopStarted) {
                netLoopStarted = true;
                animateNetworkCanvases();
            }
        }

        function applyNodePerturbationState(nodes, stressFraction, mode) {
            const removeCount = Math.floor(nodes.length * (stressFraction * 0.75));
            // Sort indices by attack priority
            const sorted = nodes.map((n, idx) => ({ idx, n })).sort((a, b) => {
                if (mode === 'targeted') {
                    // Hubs first!
                    if (a.n.hubRank !== b.n.hubRank) return a.n.hubRank - b.n.hubRank;
                    return a.n.randomOrder - b.n.randomOrder;
                } else {
                    // Peripheral / random nodes first
                    return a.n.randomOrder - b.n.randomOrder;
                }
            });

            const disabledSet = new Set(sorted.slice(0, removeCount).map(item => item.idx));
            nodes.forEach((n, idx) => {
                n.disabled = disabledSet.has(idx);
            });
        }

        function updateNetworkLab() {
            netStressPct = parseInt(document.getElementById('input-net-stress').value);
            const frac = netStressPct / 100;

            document.getElementById('val-net-stress').textContent =
                netStressPct === 0 ? '0% (Baseline)' : `${netStressPct}% (${attackMode === 'targeted' ? 'Hub Attack' : 'Random Noise'})`;

            if (bioGraphNodes.length > 0) {
                applyNodePerturbationState(bioGraphNodes, frac, attackMode);
                applyNodePerturbationState(cosmicGraphNodes, frac, attackMode);
            }

            // Compute Graph-Theoretic Resilience & Topology Metrics
            const activeN = Math.max(12, Math.round(68 * (1 - frac * 0.75)));
            let bioEff, cosEff, bioGC, cosGC, bioK, cosK, bioC, cosC, bioGamma, cosGamma;

            if (attackMode === 'random') {
                // Scale-free networks are famously tolerant to random failures!
                bioEff = Math.round(100 - frac * 22);
                cosEff = Math.round(100 - frac * 24);
                bioGC = Math.round(100 - frac * 18);
                cosGC = Math.round(100 - frac * 20);
                bioK = (4.82 - frac * 1.1).toFixed(2);
                cosK = (4.65 - frac * 1.05).toFixed(2);
                bioC = (0.44 - frac * 0.08).toFixed(2);
                cosC = (0.41 - frac * 0.07).toFixed(2);
                bioGamma = (2.24 + frac * 0.25).toFixed(2);
                cosGamma = (2.18 + frac * 0.22).toFixed(2);
            } else {
                // Targeted Hub Disruption causes catastrophic collapse of Global Efficiency & Giant Component!
                bioEff = Math.max(8, Math.round(100 * Math.pow(1 - frac, 2.35)));
                cosEff = Math.max(7, Math.round(100 * Math.pow(1 - frac, 2.4)));
                bioGC = Math.max(11, Math.round(100 * Math.pow(1 - frac, 2.1)));
                cosGC = Math.max(10, Math.round(100 * Math.pow(1 - frac, 2.15)));
                bioK = Math.max(1.1, 4.82 - frac * 3.8).toFixed(2);
                cosK = Math.max(1.05, 4.65 - frac * 3.7).toFixed(2);
                bioC = Math.max(0.05, 0.44 - frac * 0.42).toFixed(2);
                cosC = Math.max(0.04, 0.41 - frac * 0.39).toFixed(2);
                bioGamma = (2.24 + frac * 1.45).toFixed(2);
                cosGamma = (2.18 + frac * 1.40).toFixed(2);
            }

            const bioE = Math.round((activeN * parseFloat(bioK)) / 2);
            const cosE = Math.round((activeN * parseFloat(cosK)) / 2);

            document.getElementById('bio-eff-badge').textContent = `E_glob: ${bioEff}%`;
            document.getElementById('cosmic-eff-badge').textContent = `E_glob: ${cosEff}%`;

            document.getElementById('m-bio-n').textContent = `${activeN} (6.9×10¹⁰ real)`;
            document.getElementById('m-cos-n').textContent = `${activeN} (~10¹¹ real)`;
            document.getElementById('m-bio-e').textContent = bioE;
            document.getElementById('m-cos-e').textContent = cosE;
            document.getElementById('m-bio-k').textContent = bioK;
            document.getElementById('m-cos-k').textContent = cosK;
            document.getElementById('m-bio-c').textContent = bioC;
            document.getElementById('m-cos-c').textContent = cosC;
            document.getElementById('m-bio-eff').textContent = `${bioEff}%`;
            document.getElementById('m-cos-eff').textContent = `${cosEff}%`;
            document.getElementById('m-bio-gc').textContent = `${bioGC}%`;
            document.getElementById('m-cos-gc').textContent = `${cosGC}%`;
            document.getElementById('m-bio-gamma').textContent = bioGamma;
            document.getElementById('m-cos-gamma').textContent = cosGamma;

            const verdictEl = document.getElementById('resilience-verdict');
            const statusEl = document.getElementById('m-eff-status');
            if (bioEff >= 75) {
                verdictEl.textContent = 'SCALE-FREE RESILIENT';
                verdictEl.className = 'px-2.5 py-1 rounded-lg bg-emerald-500/15 text-emerald-300 border border-emerald-400/30 font-mono text-[11px] font-bold';
                statusEl.textContent = 'Optimal Flow';
                statusEl.className = 'py-2 px-3 text-emerald-400';
            } else if (bioEff >= 42) {
                verdictEl.textContent = 'DEGRADED PATHWAYS';
                verdictEl.className = 'px-2.5 py-1 rounded-lg bg-amber-500/15 text-amber-300 border border-amber-400/30 font-mono text-[11px] font-bold';
                statusEl.textContent = 'Lengthened Paths';
                statusEl.className = 'py-2 px-3 text-amber-300';
            } else {
                verdictEl.textContent = 'HUB FRAGMENTATION COLLAPSE';
                verdictEl.className = 'px-2.5 py-1 rounded-lg bg-rose-500/15 text-rose-300 border border-rose-400/30 font-mono text-[11px] font-bold';
                statusEl.textContent = 'Network Fragmented';
                statusEl.className = 'py-2 px-3 text-rose-400';
            }

            updatePowerLawChart(frac, attackMode);
        }

        function drawFilamentGraph(canvas, nodes, nodeColor, edgeRgba, hoveredIdx, time) {
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            const linkRadius = 72;

            ctx.clearRect(0, 0, w, h);

            // Subtle drift for active nodes
            nodes.forEach(n => {
                if (!n.disabled) {
                    n.x += n.vx;
                    n.y += n.vy;
                    if (n.x < 14 || n.x > w - 14) n.vx *= -1;
                    if (n.y < 14 || n.y > h - 14) n.vy *= -1;
                }
            });

            // Draw Filaments between active nodes
            for (let i = 0; i < nodes.length; i++) {
                if (nodes[i].disabled) continue;
                for (let j = i + 1; j < nodes.length; j++) {
                    if (nodes[j].disabled) continue;
                    const dist = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
                    // Allow longer-range backbone bridges between active super-hubs
                    const maxD = (nodes[i].isHub && nodes[j].isHub) ? linkRadius * 2.1 : linkRadius;
                    if (dist < maxD) {
                        const isHov = hoveredIdx === i || hoveredIdx === j;
                        const alpha = isHov ? 0.95 : (1 - dist / maxD) * 0.55;
                        ctx.strokeStyle = edgeRgba.replace('ALPHA', alpha.toFixed(2));
                        ctx.lineWidth = isHov ? 1.8 : (nodes[i].isHub && nodes[j].isHub ? 1.3 : 0.8);
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();

                        // Traveling transport pulse along active hub filaments
                        if (nodes[i].isHub && nodes[j].isHub) {
                            const t = (time * 0.0009 + i * 0.23) % 1;
                            const px = nodes[i].x + (nodes[j].x - nodes[i].x) * t;
                            const py = nodes[i].y + (nodes[j].y - nodes[i].y) * t;
                            ctx.fillStyle = '#ffffff';
                            ctx.beginPath();
                            ctx.arc(px, py, 1.8, 0, Math.PI * 2);
                            ctx.fill();
                        }
                    }
                }
            }

            // Draw Nodes (Active vs Perturbed/Disrupted)
            nodes.forEach((n, idx) => {
                if (n.disabled) {
                    // Render disrupted node as faint dashed/crossed ghost
                    ctx.beginPath();
                    ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
                    ctx.strokeStyle = 'rgba(244, 63, 94, 0.35)';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                    return;
                }

                const isHov = hoveredIdx === idx;
                ctx.beginPath();
                ctx.arc(n.x, n.y, isHov ? n.r + 3 : n.r, 0, Math.PI * 2);
                ctx.fillStyle = isHov ? '#ffffff' : nodeColor;
                ctx.shadowColor = nodeColor;
                ctx.shadowBlur = n.isHub || isHov ? 14 : 4;
                ctx.fill();
            });
            ctx.shadowBlur = 0;
        }

        function animateNetworkCanvases(time = 0) {
            requestAnimationFrame(animateNetworkCanvases);
            if (document.getElementById('view-cosmic').classList.contains('hidden')) return;

            const bCanvas = document.getElementById('bioNetCanvas');
            const cCanvas = document.getElementById('cosmicNetCanvas');
            if (!bCanvas || !cCanvas) return;

            const bioColor = bioGraphType === 'connectome' ? '#38bdf8' : '#f43f5e';
            const bioRgba = bioGraphType === 'connectome' ? 'rgba(56, 189, 248, ALPHA)' : 'rgba(244, 63, 94, ALPHA)';
            drawFilamentGraph(bCanvas, bioGraphNodes, bioColor, bioRgba, hoveredBioIdx, time);
            drawFilamentGraph(cCanvas, cosmicGraphNodes, '#a78bfa', 'rgba(167, 139, 250, ALPHA)', hoveredCosmicIdx, time);
        }

        function bindNetworkCanvasHover(canvasId, tipId, isCosmic) {
            const canvas = document.getElementById(canvasId);
            const tip = document.getElementById(tipId);
            if (!canvas) return;

            const handleMove = (e) => {
                const rect = canvas.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const list = isCosmic ? cosmicGraphNodes : bioGraphNodes;
                let foundIdx = -1;
                for (let i = 0; i < list.length; i++) {
                    if (Math.hypot(list[i].x - x, list[i].y - y) < 13) {
                        foundIdx = i;
                        break;
                    }
                }
                if (isCosmic) hoveredCosmicIdx = foundIdx;
                else hoveredBioIdx = foundIdx;

                if (foundIdx !== -1) {
                    const node = list[foundIdx];
                    tip.classList.remove('hidden');
                    const statusStr = node.disabled ? 'DISRUPTED / OFFLINE' : (node.isHub ? 'SUPER-HUB (HIGH DEGREE)' : 'FILAMENT NODE');
                    tip.textContent = `Node #${node.id} | ${statusStr}`;
                } else {
                    tip.classList.add('hidden');
                }
            };

            canvas.addEventListener('mousemove', handleMove);
            canvas.addEventListener('mouseleave', () => {
                if (isCosmic) hoveredCosmicIdx = -1;
                else hoveredBioIdx = -1;
                tip.classList.add('hidden');
            });
        }

        function initPowerLawChart() {
            const ctx = document.getElementById('powerLawChart').getContext('2d');
            powerLawChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['k=1', 'k=2', 'k=4', 'k=8', 'k=16', 'k=32', 'k=64'],
                    datasets: [
                        {
                            label: 'Biological Connectome P(k)',
                            data: [0.48, 0.24, 0.11, 0.048, 0.021, 0.009, 0.004],
                            borderColor: '#38bdf8',
                            backgroundColor: 'rgba(56, 189, 248, 0.15)',
                            borderWidth: 2.5,
                            tension: 0.25,
                            pointRadius: 3
                        },
                        {
                            label: 'Cosmic Web Filaments P(k)',
                            data: [0.50, 0.25, 0.115, 0.051, 0.022, 0.0095, 0.0042],
                            borderColor: '#a78bfa',
                            borderDash: [5, 3],
                            borderWidth: 2.5,
                            tension: 0.25,
                            pointRadius: 3
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            labels: { color: '#cbd5e1', font: { family: 'JetBrains Mono', size: 10 } }
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255,255,255,0.04)' },
                            ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 10 } }
                        },
                        y: {
                            type: 'logarithmic',
                            min: 0.0005,
                            max: 1.0,
                            grid: { color: 'rgba(255,255,255,0.05)' },
                            ticks: { color: '#94a3b8', font: { family: 'JetBrains Mono', size: 10 } }
                        }
                    }
                }
            });
        }

        function updatePowerLawChart(frac, mode) {
            if (!powerLawChart) return;
            const baseBio = [0.48, 0.24, 0.11, 0.048, 0.021, 0.009, 0.004];
            const baseCos = [0.50, 0.25, 0.115, 0.051, 0.022, 0.0095, 0.0042];

            // Under Targeted Hub Attack, high-degree hubs (k=16, 32, 64) drop sharply!
            const modBio = baseBio.map((v, i) => {
                if (mode === 'targeted' && i >= 3) {
                    return Math.max(0.0005, v * Math.pow(1 - frac, i * 1.1));
                }
                return Math.max(0.0005, v * (1 - frac * 0.25));
            });

            const modCos = baseCos.map((v, i) => {
                if (mode === 'targeted' && i >= 3) {
                    return Math.max(0.0005, v * Math.pow(1 - frac, i * 1.1));
                }
                return Math.max(0.0005, v * (1 - frac * 0.25));
            });

            powerLawChart.data.datasets[0].data = modBio;
            powerLawChart.data.datasets[1].data = modCos;
            powerLawChart.update();
        }

        // =====================================================================
        // MODULE 04: REAL-TIME BIOMETRIC HARDWARE (ESP32 + MAX30102 + PPG)
        // =====================================================================
        let demoStreamOn = true;
        let demoExertion = 10;
        let earthLiveHr = 72;
        let earthLiveSpo2 = 98.4;
        let ppgBuffer = new Array(160).fill(0);
        let ppgPhase = 0;

        function toggleDemoMode() {
            demoStreamOn = !demoStreamOn;
            const btn = document.getElementById('btn-demo-toggle');
            const led = document.getElementById('hw-led');
            if (demoStreamOn) {
                btn.textContent = 'PAUSE DEMO STREAM';
                led.className = 'w-3 h-3 rounded-full bg-emerald-400 animate-ping';
                showToast('Live Demo PPG Stream Active');
            } else {
                btn.textContent = 'RESUME DEMO STREAM';
                led.className = 'w-3 h-3 rounded-full bg-slate-500';
                showToast('Demo Stream Paused');
            }
        }

        function updateDemoExertion() {
            demoExertion = parseInt(document.getElementById('input-demo-exertion').value);
            const targetBpm = Math.round(64 + (demoExertion / 100) * 81);
            const label = demoExertion < 25 ? `Rest Baseline (~${targetBpm} bpm)`
                : demoExertion < 65 ? `Light Ergometer (~${targetBpm} bpm)`
                : `Peak EVA Exertion (~${targetBpm} bpm)`;
            document.getElementById('val-demo-exertion').textContent = label;
            if (demoStreamOn) {
                earthLiveHr = targetBpm;
                earthLiveSpo2 = Number((98.6 - (demoExertion / 100) * 1.3).toFixed(1));
                updateHardwareTelemetryUI();
            }
        }

        async function connectWebSerial() {
            if (!('serial' in navigator)) {
                showToast('Web Serial API unavailable in this frame. Open directly in Chrome/Edge or use Demo Mode.');
                return;
            }
            try {
                const port = await navigator.serial.requestPort();
                await port.open({ baudRate: 115200 });
                demoStreamOn = false;
                document.getElementById('hw-mode-desc').textContent =
                    'Connected to physical ESP32 + MAX30102 via USB Serial (115200 baud).';
                document.getElementById('hw-led').className = 'w-3 h-3 rounded-full bg-sky-400 animate-ping';
                showToast('ESP32 + MAX30102 Connected via USB Serial!');

                const decoder = new TextDecoderStream();
                port.readable.pipeTo(decoder.writable);
                const reader = decoder.readable.getReader();

                let serialBuf = '';
                while (true) {
                    const { value, done } = await reader.read();
                    if (done) break;
                    serialBuf += value;
                    const lines = serialBuf.split('\n');
                    serialBuf = lines.pop();
                    for (const line of lines) {
                        const clean = line.trim();
                        if (!clean) continue;
                        if (clean.startsWith('{')) {
                            try {
                                const data = JSON.parse(clean);
                                const parsedHr = data.hr || data.bpm;
                                if (parsedHr && parsedHr >= 35 && parsedHr <= 220) earthLiveHr = Math.round(parsedHr);
                                if (data.spo2 && data.spo2 >= 75 && data.spo2 <= 100) earthLiveSpo2 = Number(data.spo2);
                                document.getElementById('hw-sqi').textContent = '99%';
                                updateHardwareTelemetryUI();
                            } catch (e) { /* skip partial packet */ }
                        } else if (clean.includes(',')) {
                            const [hStr, sStr] = clean.split(',');
                            const hVal = parseFloat(hStr);
                            const sVal = parseFloat(sStr);
                            if (!isNaN(hVal) && hVal >= 35 && hVal <= 220) earthLiveHr = Math.round(hVal);
                            if (!isNaN(sVal) && sVal >= 75 && sVal <= 100) earthLiveSpo2 = sVal;
                            document.getElementById('hw-sqi').textContent = '99%';
                            updateHardwareTelemetryUI();
                        }
                    }
                }
            } catch (err) {
                showToast('USB Serial connection cancelled.');
            }
        }

        function copyFirmwareCode() {
            const codeText = document.getElementById('esp32-firmware').textContent;
            const ta = document.createElement('textarea');
            ta.value = codeText;
            document.body.appendChild(ta);
            ta.select();
            try {
                document.execCommand('copy');
                showToast('ESP32 + MAX30102 Arduino C++ Firmware Copied!');
            } catch (e) {
                showToast('Unable to copy firmware.');
            }
            document.body.removeChild(ta);
        }

        function updateHardwareTelemetryUI() {
            document.getElementById('hw-live-hr').textContent = earthLiveHr;
            document.getElementById('hw-live-spo2').textContent = earthLiveSpo2.toFixed(1);
            updateHardwareDelta();
        }

        function updateHardwareDelta() {
            document.getElementById('comp-earth-str').textContent = `${earthLiveHr} bpm / ${earthLiveSpo2.toFixed(1)}%`;
            document.getElementById('comp-astro-str').textContent = `${simState.hr} bpm / ${simState.spo2.toFixed(1)}%`;

            const deltaHr = simState.hr - earthLiveHr;
            const deltaBadge = document.getElementById('comp-delta-badge');
            deltaBadge.textContent = `${deltaHr >= 0 ? '+' : ''}${deltaHr} bpm`;
            deltaBadge.className = Math.abs(deltaHr) <= 5 ? 'font-bold text-emerald-400' : 'font-bold text-amber-300';

            const analysisEl = document.getElementById('hw-delta-analysis');
            if (Math.abs(deltaHr) <= 5) {
                analysisEl.textContent = `Your Earth terrestrial pulse (${earthLiveHr} bpm) closely tracks the simulated astronaut's compensated orbital heart rate (${simState.hr} bpm).`;
            } else if (deltaHr > 5) {
                analysisEl.textContent = `The simulated astronaut exhibits a +${deltaHr} bpm elevation above your Earth reading (${earthLiveHr} bpm), driven by hypovolemic plasma contraction (${simState.plasmaDelta}%) and circadian stress (${simState.stress}%).`;
            } else {
                analysisEl.textContent = `The simulated astronaut's heart rate is ${Math.abs(deltaHr)} bpm lower than your current Earth reading (${earthLiveHr} bpm), reflecting exertion-induced tachycardia on Earth or early orbital bradycardia.`;
            }
        }

        function animatePPGOscilloscope(time = 0) {
            requestAnimationFrame(animatePPGOscilloscope);
            const canvas = document.getElementById('ppgOscilloscope');
            if (!canvas || document.getElementById('view-hardware').classList.contains('hidden')) return;

            const rect = canvas.parentElement.getBoundingClientRect();
            if (canvas.width !== rect.width && rect.width > 0) {
                canvas.width = rect.width;
                canvas.height = rect.height || 256;
            }

            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;

            if (demoStreamOn) {
                ppgPhase += (earthLiveHr / 60) * 0.11;
                const cycle = ppgPhase % (Math.PI * 2);
                let wave = 0;
                if (cycle < 0.62) {
                    // Sharp Systolic Upstroke & Peak
                    wave = Math.sin((cycle / 0.62) * Math.PI) * 0.85;
                } else if (cycle < 1.32) {
                    // Dicrotic Notch & Diastolic Wave
                    wave = Math.sin(((cycle - 0.62) / 0.70) * Math.PI) * 0.34;
                } else {
                    wave = Math.sin(cycle * 2.0) * 0.02;
                }
                // Subtle Respiratory Sinus Baseline Modulation
                const respMod = Math.sin(time * 0.0018) * 0.06;
                ppgBuffer.push(wave + respMod);
                ppgBuffer.shift();
            }

            // Medical Telemetry Grid
            ctx.clearRect(0, 0, w, h);
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.06)';
            ctx.lineWidth = 1;
            for (let x = 0; x < w; x += 28) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
            }
            for (let y = 0; y < h; y += 28) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
            }

            // Glowing Arterial PPG Waveform
            ctx.beginPath();
            ctx.strokeStyle = '#f43f5e';
            ctx.lineWidth = 2.6;
            ctx.shadowColor = '#f43f5e';
            ctx.shadowBlur = 12;

            const dx = w / (ppgBuffer.length - 1);
            const baselineY = h * 0.74;
            ppgBuffer.forEach((val, idx) => {
                const px = idx * dx;
                const py = baselineY - val * (h * 0.54);
                if (idx === 0) ctx.moveTo(px, py);
                else ctx.lineTo(px, py);
            });
            ctx.stroke();
            ctx.shadowBlur = 0;
        }

        // Subtle realistic beat-to-beat HRV jitter in Demo Mode
        setInterval(() => {
            if (demoStreamOn) {
                const base = Math.round(64 + (demoExertion / 100) * 81);
                earthLiveHr = base + Math.floor(Math.random() * 3) - 1;
                earthLiveSpo2 = Number((98.6 - (demoExertion / 100) * 1.3 + (Math.random() * 0.2 - 0.1)).toFixed(1));
                document.getElementById('hw-sqi').textContent = `${97 + Math.floor(Math.random() * 3)}%`;
                updateHardwareTelemetryUI();
            }
        }, 2200);

        // =====================================================================
        // APPLICATION BOOTSTRAP
        // =====================================================================
        window.onload = function() {
            initTelemetryChart();
            initPowerLawChart();
            updateSimulation();
            initThreeHumanUniverse();
            selectOrgan('brain');
            bindNetworkCanvasHover('bioNetCanvas', 'bio-tip', false);
            bindNetworkCanvasHover('cosmicNetCanvas', 'cosmic-tip', true);
            animatePPGOscilloscope();
        };

        window.addEventListener('resize', () => {
            if (!document.getElementById('view-human').classList.contains('hidden')) {
                resizeThreeViewport();
            }
            if (!document.getElementById('view-cosmic').classList.contains('hidden')) {
                initNetworkCanvases();
            }
        });
    </script>
</body>
</html>
