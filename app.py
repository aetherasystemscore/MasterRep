"""
Aethera Systems Core — Master Repository, Live App Health, Resource Telemetry & Commit Blocker Hub (MasterRep)
Authenticated gateway (Admin / Aether@) listing all Aethera Systems Core GitHub repositories,
brief explanations, live Streamlit Cloud deployments, external Cron scheduler links,
real-time Liveness Probes (/_stcore/health), CPU/RAM container telemetry, and Commit/Blocker forensics.
"""

import base64
import ctypes
import datetime
import gc
import hmac
import json
import os
import shutil
import socket
import subprocess
import sys
import threading
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from zoneinfo import ZoneInfo

import pandas as pd
import requests
import streamlit as st

try:
    import psutil
except ImportError:
    psutil = None

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Aethera Systems Core • Master Repository & Health Hub",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

IST = ZoneInfo("Asia/Kolkata")

# =====================================================================
# AUTHENTICATION CREDENTIALS
# =====================================================================
MASTER_USERNAME = "Admin"
MASTER_PASSWORD = "Aether@"

# =====================================================================
# EXTERNAL CRON & MASTER REPOSITORY LINKS
# =====================================================================
EXTERNAL_CRON_URL = "https://cron-job.org/en/"
MASTER_GITHUB_REPO_MASTERREP = "https://github.com/aetherasystemscore/MasterRep"

# =====================================================================
# MASTER CATALOG OF ALL AETHERA SYSTEMS CORE REPOSITORIES & APPS
# =====================================================================
REPOSITORIES = [
    {
        "id": 1,
        "slug": "stock-etf-reit-invit-screener",
        "full_repo": "aetherasystemscore/stock-etf-reit-invit-screener",
        "title": "Stock, ETF, REIT & InvIT Quantitative Screener",
        "icon": "🎯",
        "category": "Multi-Asset Tactical Allocator & Paper Trader",
        "accent": "#38bdf8",
        "git_url": "https://github.com/aetherasystemscore/stock-etf-reit-invit-screener",
        "streamlit_url": "https://stock-etf-reit-invit-screener-djbh7czff5apmlkv27srrp.streamlit.app/",
        "visibility": "Private",
        "repo_size_kb": 2368,
        "est_ram_mb": "310 – 480 MB",
        "est_cpu_profile": "Moderate (yfinance + Google Sheets Sync)",
        "workflow_file": "paper_trader_345pm.yml",
        "key_dependencies": [
            "streamlit>=1.35.0",
            "pandas>=2.0.0",
            "yfinance>=0.2.38",
            "st-gsheets-connection>=0.1.0",
            "gspread>=5.10.0",
            "scipy>=1.11.0",
            "psutil>=5.9.0",
        ],
        "fallback_commit": {
            "sha": "df7a184",
            "author": "Prakash",
            "date_ist": "24-Oct-2026 17:47 IST",
            "message": "Sync NCD-Bond Screener repo slug (aetherasystemscore/NCD-Bond_Screener) and 58 verified real NSE/BSE debt securities with live NSE overlay",
            "url": "https://github.com/aetherasystemscore/stock-etf-reit-invit-screener/commit/df7a184",
        },
        "blocker_diagnostics": [
            {
                "severity": "MEDIUM",
                "type": "Repository Visibility & Cloud Auth Gate",
                "detail": "Repo is Private on GitHub. Streamlit Community Cloud permits only 1 private app per free account and requires valid Google Sheets service-account secrets in st.secrets.",
            },
            {
                "severity": "RESOLVED",
                "type": "Git CSV Commit Reboot Loop Mitigated (Commit e3710ec)",
                "detail": "Switched Paper_Trades & Execution_Audit_Log to Google-Sheets-Only storage, preventing intraday git commits from triggering continuous Streamlit file-watcher restarts.",
            },
        ],
        "brief_explanation": (
            "Primary 6-pillar institutional tactical allocator covering Broad & Smart Beta ETFs, "
            "NIFTY LargeMidcap 250 Quality Equities, Support/Resistance (S/R) Mean Reversion, "
            "Listed REITs & InvITs, Precious Metals (Gold & Silver ETFs), and the Apex Multi-Factor "
            "Deduplicated Allocator. Combines DMA pullbacks, 14-day RSI exhaustion, an 8-stage dip-averaging "
            "pyramid, ₹50,000 monthly capital protection guardrails, autonomous weekday paper trading "
            "(9:25 AM scan, 3:00 PM entry, 3:10 PM square-off) backed by Google Sheets, and an AI/ML & RAG "
            "strategy forensics engine."
        ),
        "highlights": [
            "6-Pillar Multi-Asset Allocator (Broad ETFs, Nifty 250 Equities, S/R Engine, REITs/InvITs, Precious Metals, Apex)",
            "8-Stage Fall Pyramid (-2.5% to -25%) & ₹50,000 Monthly Per-Ticker Capital Protection",
            "Autonomous Weekday Paper Trader (9:25 AM Scan, 3:00 PM Entry, 3:10 PM Intraday Square-Off) with Google Sheets Sync",
            "Hybrid BM25 + TF-IDF SVD AI/RAG Strategy Forensics & Counterfactual Regime Backtester",
        ],
    },
    {
        "id": 2,
        "slug": "SmartStock-Radar",
        "full_repo": "aetherasystemscore/SmartStock-Radar",
        "title": "SmartStock Radar (v5.0 Catalyst & Bear-Market Terminal)",
        "icon": "📡",
        "category": "Event Catalyst NLP & Deep-Value Equity Intelligence",
        "accent": "#ec4899",
        "git_url": "https://github.com/aetherasystemscore/SmartStock-Radar",
        "streamlit_url": "https://smartstock-radar.streamlit.app/",
        "visibility": "Public",
        "repo_size_kb": 9511,
        "est_ram_mb": "460 – 690 MB",
        "est_cpu_profile": "High (20Y OHLCV Matrix + XGBoost/LightGBM/Optuna)",
        "workflow_file": "daily_audit_daemon.yml",
        "key_dependencies": [
            "streamlit>=1.38.0",
            "pandas>=2.2.0",
            "yfinance>=0.2.40",
            "scikit-learn>=1.3.0",
            "xgboost>=2.0.0",
            "lightgbm>=4.0.0",
            "optuna>=3.5.0",
            "pyarrow>=14.0.0",
        ],
        "fallback_commit": {
            "sha": "92ca49c",
            "author": "Prakash",
            "date_ist": "24-Oct-2026 14:16 IST",
            "message": "chore(ui): rename Streamlit app title and headers to smartstock-radar",
            "url": "https://github.com/aetherasystemscore/SmartStock-Radar/commit/92ca49c",
        },
        "blocker_diagnostics": [
            {
                "severity": "HIGH",
                "type": "Heavy ML Stack & 9.5 MB Repo Memory Pressure",
                "detail": "Loads xgboost, lightgbm, optuna, scikit-learn, scipy, and 20-year historical data (~9.5 MB repo). Can approach Streamlit Cloud's 1 GB RAM cgroup limit if multi-regime backtests run concurrently without cache pruning.",
            },
            {
                "severity": "RESOLVED",
                "type": "Missing Export Blocker Fixed (Commit 0a03036)",
                "detail": "Exported HISTORICAL_REGIMES in data_pipeline_20y.py to prevent ImportError / AttributeError on Tab 4 20Y Horizon Matrix.",
            },
        ],
        "brief_explanation": (
            "Quantitative equity & ETF intelligence terminal for NSE NIFTY 100, Midcap 100, and "
            "Sovereign/Sectoral ETFs driven by live corporate disclosures and 20-year historical trends. "
            "Combines real-time RSS regulatory disclosure NLP, TF-IDF RAG filing retrieval, short-horizon "
            "1–2 week Catalyst Drift screening with Platt-calibrated empirical probabilities, automated "
            "Demerger/Merger swap parity math, path-dependent paper trade auditing, and the Dual-Logic v5.0 "
            "Bear-Market & Physical Moat Engine validated across 20 years of NSE daily bars (2006–present)."
        ),
        "highlights": [
            "1–2 Week Catalyst Drift Screener with Real-Time Exchange Disclosure NLP & Platt-Calibrated Probabilities",
            "Single-Stock Deep Dive with TF-IDF RAG Filing Retrieval & Automated Merger/Demerger Swap Parity",
            "Path-Dependent Paper Prediction Audit Ledger with Mathematical Expectancy, Sharpe/Sortino & ₹50K XIRR Tracker",
            "Dual-Logic v5.0 Bear-Market Engine (Merton Distance-to-Default, Altman Z'', Purged Walk-Forward CV)",
        ],
    },
    {
        "id": 3,
        "slug": "HNI-Institutional-Investor-Trend",
        "full_repo": "aetherasystemscore/HNI-Institutional-Investor-Trend",
        "title": "HNI & Institutional Investor Trend Radar",
        "icon": "🏛️",
        "category": "Superstar Filings, 15Y Index S/R & Sectoral ETFs",
        "accent": "#f59e0b",
        "git_url": "https://github.com/aetherasystemscore/HNI-Institutional-Investor-Trend",
        "streamlit_url": "https://hni-institutional-investor-trend-uyvhb3nw3abdvqjrfmedf6.streamlit.app/",
        "visibility": "Public",
        "repo_size_kb": 4078,
        "est_ram_mb": "290 – 440 MB",
        "est_cpu_profile": "Moderate-High (Background 45s Daemon + Startup Catch-Up)",
        "workflow_file": "",
        "key_dependencies": [
            "streamlit>=1.38.0",
            "pandas>=2.2.0",
            "yfinance>=0.2.40",
            "beautifulsoup4>=4.12.0",
            "lxml>=5.2.0",
            "plotly>=5.22.0",
            "scipy>=1.13.0",
            "scikit-learn>=1.5.0",
        ],
        "fallback_commit": {
            "sha": "05ba3c7",
            "author": "Prakash",
            "date_ist": "24-Oct-2026 16:37 IST",
            "message": "Initial commit: Live HNI & Institutional Investor Trend, 15Y Indices S/R, Sectoral ETF & 3 PM IST Paper Trade Intelligence",
            "url": "https://github.com/aetherasystemscore/HNI-Institutional-Investor-Trend/commit/05ba3c7",
        },
        "blocker_diagnostics": [
            {
                "severity": "MEDIUM",
                "type": "Cold-Boot Offline Catch-Up Latency",
                "detail": "On container startup after multi-day hibernation, sync_daily_live_candidates_and_tables backfills missed weekday 3:00 PM IST slots using live OHLCV bars, which can add 8–15s to initial cold-start render.",
            },
            {
                "severity": "LOW",
                "type": "Background Thread Multiplication Guard",
                "detail": "Uses ensure_3pm_ist_background_scheduler daemon thread; guarded by singleton check so user reruns do not spawn duplicate threads.",
            },
        ],
        "brief_explanation": (
            "Institutional & Superstar investor intelligence platform tracking live NSE/BSE Bulk & Block Deals, "
            "SAST/Insider disclosures, and Trendlyne Superstar Portfolios with empirical T+1 Open and T0 Close "
            "win probabilities under a strict <50% Ignore rule. Integrates a 15-year daily OHLCV Support/Resistance "
            "(S1–S3, R1–R3) & state-conditioned directional probability engine across 25 Indian Indices, "
            "a 42-ETF Sectoral & Future Macro Theme advisor, Superstar follower leaderboards, and a scheduled "
            "3:00 PM IST weekday paper trading engine."
        ),
        "highlights": [
            "Live NSE/BSE Bulk, Block, SAST & Trendlyne Superstar Disclosures with Strict <50% Probability Ignore Rule",
            "25 Indian Indices — 15-Year Daily OHLCV Support/Resistance (S1–S3, R1–R3) & Conditional Upward Probabilities",
            "42 NSE Sectoral & Thematic ETFs Screened Across 35+ Technical/Valuation Metrics & 10 Future Macro Themes",
            "Automated Weekday 3:00 PM IST Top-3 BUY / Top-3 SELL Paper Trading Engine (1W to 10Y Rolling Horizons)",
        ],
    },
    {
        "id": 4,
        "slug": "AI-Data-Center-Growth-Theme",
        "full_repo": "aetherasystemscore/AI-Data-Center-Growth-Theme",
        "title": "AI Data Center & Power Infrastructure Growth Theme (AI3)",
        "icon": "🖥️",
        "category": "Thematic Value-Chain Research, IPO Tracker & Optimiser",
        "accent": "#10b981",
        "git_url": "https://github.com/aetherasystemscore/AI-Data-Center-Growth-Theme",
        "streamlit_url": "https://ai-data-center-growth-theme-hg4oggdawtcqefqn48n5gm.streamlit.app/",
        "visibility": "Public",
        "repo_size_kb": 255,
        "est_ram_mb": "180 – 280 MB",
        "est_cpu_profile": "Low-Moderate (SQLite + 74-Ticker Batch Cache)",
        "workflow_file": "paper_trader_3pm.yml",
        "key_dependencies": [
            "streamlit>=1.38.0",
            "pandas>=2.2.0",
            "plotly>=5.22.0",
            "SQLAlchemy>=2.0.30",
            "pydantic>=2.7.0",
            "yfinance>=0.2.40",
            "psutil>=5.9.0",
        ],
        "fallback_commit": {
            "sha": "9e5a504",
            "author": "github-actions[bot]",
            "date_ist": "24-Oct-2026 15:05 IST",
            "message": "chore(paper-trader): automated 3:00 PM IST live MTM & paper trade sync",
            "url": "https://github.com/aetherasystemscore/AI-Data-Center-Growth-Theme/commit/9e5a504",
        },
        "blocker_diagnostics": [
            {
                "severity": "MEDIUM",
                "type": "Automated GitHub Actions Bot Commit Reloads (Commit 9e5a504)",
                "detail": "github-actions[bot] commits updated paper_trading_ledger.json to main at 3:00 PM IST on weekdays. When pushed, Streamlit Cloud detects the git change and hot-reloads active user sessions.",
            },
            {
                "severity": "LOW",
                "type": "Ephemeral SQLite Write Concurrency",
                "detail": "Uses local embedded SQLite (ai3_research.db) inside container SSD; read-heavy caching prevents SQLite lock contention.",
            },
        ],
        "brief_explanation": (
            "Production quantitative research and portfolio-analysis platform covering the complete 8-segment "
            "AI infrastructure value chain (Compute Hardware, Electronic Components, Data-Centre Infra, "
            "Power & Grid, Cooling/Thermal, Optical Fibre Connectivity, Enterprise AI IT, and Circular "
            "Electronics/E-Waste). Features a 100-point AI Exposure Scoring Engine across 74+ verified Indian "
            "and global supply-chain equities, Value Alternative Finder, ETF & Smallcase look-through overlap "
            "module, DRHP/RHP/IPO tracker, 8-method Portfolio Optimiser, and point-in-time backtesting."
        ),
        "highlights": [
            "8-Segment AI Infrastructure Value-Chain Taxonomy Across 74+ Indian & Global Supply-Chain Benchmark Equities",
            "100-Point AI Exposure Scoring Engine with Fact-vs-Narrative Caps & High-Risk Governance Gatekeeper",
            "Value Alternative Finder, 10-ETF & Smallcase Look-Through Overlap Module, and DRHP/RHP/IPO Tracker",
            "8-Method Portfolio Optimiser (HRP, Black-Litterman, Max Sharpe, Min Variance) & Point-in-Time Backtester",
        ],
    },
    {
        "id": 5,
        "slug": "NCD-Bond_Screener",
        "full_repo": "aetherasystemscore/NCD-Bond_Screener",
        "title": "Indian Listed NCD, G-Sec & Corporate Bond Screener",
        "icon": "📜",
        "category": "Fixed Income, Sovereign G-Secs & Tax-Free PSU Debt",
        "accent": "#a855f7",
        "git_url": "https://github.com/aetherasystemscore/NCD-Bond_Screener",
        "streamlit_url": "https://ncd-bondscreener-bgftfvgej8y5bsng8id54t.streamlit.app/",
        "visibility": "Public",
        "repo_size_kb": 121,
        "est_ram_mb": "120 – 190 MB",
        "est_cpu_profile": "Low (Pure-Python YTM Solver + Cached NSE Debt Feed)",
        "workflow_file": "",
        "key_dependencies": [
            "streamlit>=1.35.0",
            "pandas>=2.0.0",
            "numpy>=1.24.0",
            "plotly>=5.18.0",
            "requests>=2.28.0",
        ],
        "fallback_commit": {
            "sha": "979305b",
            "author": "Prakash",
            "date_ist": "24-Oct-2026 17:47 IST",
            "message": "Upgrade to 100% live real NSE debt market data & 58 exchange-verified ISINs (zero synthetic rows)",
            "url": "https://github.com/aetherasystemscore/NCD-Bond_Screener/commit/979305b",
        },
        "blocker_diagnostics": [
            {
                "severity": "MEDIUM",
                "type": "NSE India Akamai / Bot-Protection HTTP 403 Risk",
                "detail": "Queries live NSE Capital Market Debt API (nseindia.com/api/liveBonds-traded-on-cm) from cloud datacenter IPs. Automatically falls back to the 58 verified NSE/BSE securities dataset (bonds_data.csv) if NSE blocks cloud IPs.",
            },
            {
                "severity": "RESOLVED",
                "type": "SciPy Build Blocker Eliminated (Commit 04190f2)",
                "detail": "Replaced heavy scipy dependency with a pure-Python Newton-Raphson/bisection fractional-period YTM solver to prevent Streamlit Cloud wheel compilation failures.",
            },
        ],
        "brief_explanation": (
            "High-performance secondary-market fixed-income analytics screener connected directly to live NSE "
            "Capital Market Debt & G-Sec APIs (58 verified liquid NSE/BSE securities + 300+ active traded debt "
            "universe). Computes Actual/Actual accrued interest, Dirty Price, fractional-period Yield to Maturity "
            "(YTM), Macaulay Duration, Modified Duration, and Convexity across AAA/AA+ Corporate NCDs, Section "
            "10(15)(iv)(h) Tax-Free PSU Bonds (with Pre-Tax Equivalent Yield), InvIT Bonds, and Sovereign "
            "G-Secs/SDLs, complete with an RBI Policy Rate Shock Simulator and Zerodha Kite holdings sync."
        ),
        "highlights": [
            "100% Live NSE Capital Market Debt & G-Sec Order-Book API Integration + Live 10Y Sovereign Benchmark Yield",
            "Actual/Actual Accrued Interest, Dirty Price, Fractional-Period YTM, Macaulay/Modified Duration & Convexity",
            "Section 10(15)(iv)(h) Tax-Free PSU Bond Pre-Tax Equivalent Yield (PTEY) vs Taxable Bonds & Bank FDs",
            "RBI Monetary Policy Rate Shock Simulator (±200 bps Taylor Convexity) & Zerodha Kite Holdings Sync",
        ],
    },
]


# =====================================================================
# CUSTOM STYLING
# =====================================================================
def inject_custom_css() -> None:
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1.3rem;
            padding-bottom: 2.5rem;
            max-width: 1440px;
        }
        .mantra-banner {
            background: linear-gradient(90deg, rgba(30,58,138,0.45) 0%, rgba(15,23,42,0.85) 50%, rgba(30,58,138,0.45) 100%);
            border: 1px solid rgba(251, 191, 36, 0.35);
            border-radius: 10px;
            padding: 0.45rem 1rem;
            text-align: center;
            color: #fde68a;
            font-size: 0.92rem;
            font-weight: 600;
            letter-spacing: 0.3px;
            margin-bottom: 1rem;
        }
        .login-card {
            background: linear-gradient(145deg, #111827 0%, #0f172a 100%);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 16px;
            padding: 2rem 2.2rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.55);
            margin-top: 1.5rem;
        }
        .repo-card {
            background: linear-gradient(145deg, #111827 0%, #0f172a 100%);
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-radius: 14px;
            padding: 1.25rem 1.45rem;
            margin-bottom: 0.9rem;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }
        .telemetry-card {
            background: linear-gradient(145deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.75) 100%);
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }
        .cron-card {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.14) 0%, rgba(15, 23, 42, 0.95) 100%);
            border: 1px solid rgba(16, 185, 129, 0.45);
            border-radius: 14px;
            padding: 1.15rem 1.45rem;
            margin-bottom: 1.2rem;
        }
        .category-pill {
            display: inline-block;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
            font-size: 0.76rem;
            font-weight: 600;
            background: rgba(56, 189, 248, 0.14);
            color: #7dd3fc;
            border: 1px solid rgba(56, 189, 248, 0.3);
            margin-bottom: 0.4rem;
        }
        .badge-ok {
            display: inline-block;
            padding: 0.18rem 0.6rem;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 600;
            background: rgba(16, 185, 129, 0.18);
            color: #6ee7b7;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }
        .badge-warn {
            display: inline-block;
            padding: 0.18rem 0.6rem;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 600;
            background: rgba(245, 158, 11, 0.18);
            color: #fcd34d;
            border: 1px solid rgba(245, 158, 11, 0.4);
        }
        .badge-err {
            display: inline-block;
            padding: 0.18rem 0.6rem;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 600;
            background: rgba(239, 68, 68, 0.18);
            color: #fca5a5;
            border: 1px solid rgba(239, 68, 68, 0.4);
        }
        .url-box {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            padding: 0.45rem 0.75rem;
            font-family: monospace;
            font-size: 0.81rem;
            color: #e2e8f0;
            word-break: break-all;
            margin-top: 0.25rem;
            margin-bottom: 0.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =====================================================================
# HOST & CONTAINER CPU / RAM / DISK TELEMETRY ENGINE
# =====================================================================
def release_container_memory() -> None:
    """Forces Python garbage collection and invokes glibc malloc_trim(0) on Linux containers."""
    try:
        gc.collect()
        if sys.platform.startswith("linux"):
            libc = ctypes.CDLL("libc.so.6")
            libc.malloc_trim(0)
    except Exception:
        pass


def get_host_resource_telemetry() -> dict:
    """
    Collects real-time CPU, App Process RAM (VmRSS), Container Cgroup Memory Quota,
    OS Load Average, Active Threads, and Ephemeral Disk telemetry.
    """
    telemetry = {
        "app_ram_mb": 0.0,
        "cgroup_limit_mb": 1024.0,
        "system_total_ram_mb": 1024.0,
        "system_used_ram_mb": 0.0,
        "system_ram_pct": 0.0,
        "cpu_pct": 0.0,
        "cpu_count": os.cpu_count() or 1,
        "load_avg_str": "N/A",
        "active_threads": threading.active_count(),
        "disk_free_gb": 0.0,
        "disk_total_gb": 0.0,
        "disk_pct": 0.0,
        "platform": "Linux (Streamlit Cloud Pod)" if sys.platform.startswith("linux") else f"{sys.platform} (Local Host)",
        "status": "🟢 Optimal (Safe from OOM / Throttling)",
        "status_color": "#10b981",
        "timestamp": datetime.datetime.now(IST).strftime("%H:%M:%S IST"),
    }

    # 1. Read Cgroup Memory Limit on Linux containers if present
    for cg_path in ("/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"):
        if os.path.exists(cg_path):
            try:
                with open(cg_path, "r") as f:
                    raw = f.read().strip()
                    if raw.isdigit():
                        val_mb = float(raw) / (1024 * 1024)
                        if 128.0 <= val_mb <= 65536.0:
                            telemetry["cgroup_limit_mb"] = round(val_mb, 1)
                            break
            except Exception:
                pass

    # 2. Read Process RSS (VmRSS)
    def _read_rss() -> float:
        if psutil is not None:
            try:
                return round(psutil.Process().memory_info().rss / (1024 * 1024), 1)
            except Exception:
                pass
        if os.path.exists("/proc/self/status"):
            try:
                with open("/proc/self/status", "r") as f:
                    for line in f:
                        if line.startswith("VmRSS:"):
                            return round(float(line.split()[1]) / 1024.0, 1)
            except Exception:
                pass
        return 0.0

    rss_mb = _read_rss()
    if rss_mb > 550.0:
        release_container_memory()
        rss_mb = _read_rss()
    telemetry["app_ram_mb"] = rss_mb

    # 3. Read System / Virtual Memory & CPU Load
    if psutil is not None:
        try:
            proc = psutil.Process()
            vm = psutil.virtual_memory()
            telemetry["system_total_ram_mb"] = round(vm.total / (1024 * 1024), 1)
            telemetry["system_used_ram_mb"] = round(vm.used / (1024 * 1024), 1)
            telemetry["system_ram_pct"] = round(vm.percent, 1)
            try:
                proc_cpu = proc.cpu_percent(interval=0.05) / max(1, telemetry["cpu_count"])
                sys_cpu = psutil.cpu_percent(interval=None)
                telemetry["cpu_pct"] = round(max(proc_cpu, sys_cpu), 1)
            except Exception:
                telemetry["cpu_pct"] = round(psutil.cpu_percent(interval=None), 1)
        except Exception:
            pass
    elif os.path.exists("/proc/meminfo"):
        try:
            total_kb, avail_kb = 0.0, 0.0
            with open("/proc/meminfo", "r") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        total_kb = float(line.split()[1])
                    elif line.startswith("MemAvailable:"):
                        avail_kb = float(line.split()[1])
            if total_kb > 0:
                telemetry["system_total_ram_mb"] = round(total_kb / 1024.0, 1)
                used_kb = total_kb - avail_kb
                telemetry["system_used_ram_mb"] = round(used_kb / 1024.0, 1)
                telemetry["system_ram_pct"] = round((used_kb / total_kb) * 100.0, 1)
        except Exception:
            pass

    # 4. OS Load Average
    if hasattr(os, "getloadavg"):
        try:
            l1, l5, l15 = os.getloadavg()
            telemetry["load_avg_str"] = f"{l1:.2f} / {l5:.2f} / {l15:.2f}"
        except Exception:
            pass
    elif os.path.exists("/proc/loadavg"):
        try:
            with open("/proc/loadavg", "r") as f:
                parts = f.read().split()
                telemetry["load_avg_str"] = f"{parts[0]} / {parts[1]} / {parts[2]}"
        except Exception:
            pass

    # 5. Ephemeral SSD Disk Usage
    try:
        du = shutil.disk_usage(os.getcwd())
        telemetry["disk_total_gb"] = round(du.total / (1024**3), 1)
        telemetry["disk_free_gb"] = round(du.free / (1024**3), 1)
        telemetry["disk_pct"] = round(((du.total - du.free) / du.total) * 100.0, 1) if du.total > 0 else 0.0
    except Exception:
        pass

    # 6. Health Classification
    quota_pct = (telemetry["app_ram_mb"] / max(1.0, telemetry["cgroup_limit_mb"])) * 100.0
    telemetry["quota_pct"] = round(min(100.0, quota_pct), 1)

    if telemetry["app_ram_mb"] > 800 or telemetry["cpu_pct"] > 85:
        telemetry["status"] = "🔴 High Usage (OOM / Throttling Risk)"
        telemetry["status_color"] = "#ef4444"
    elif telemetry["app_ram_mb"] > 500 or telemetry["cpu_pct"] > 60:
        telemetry["status"] = "🟡 Moderate Resource Load"
        telemetry["status_color"] = "#f59e0b"
    else:
        telemetry["status"] = "🟢 Optimal (Safe from OOM / Throttling)"
        telemetry["status_color"] = "#10b981"

    return telemetry


# =====================================================================
# LIVENESS PROBE & APP HEALTH CHECKER (/_stcore/health + INGRESS + TCP)
# =====================================================================
def _probe_single_app(repo: dict) -> dict:
    """
    Runs a fast 3-layer probe on a Streamlit Cloud app:
    1) TCP Port 443 Socket Handshake RTT (ms)
    2) HTTPS Ingress Root Probe (GET / without redirect loop)
    3) Streamlit Internal Liveness Probe (GET /_stcore/health)
    """
    app_url = repo["streamlit_url"]
    parsed = urllib.parse.urlparse(app_url)
    host = parsed.hostname or ""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; AetheraMasterHub-LivenessProbe/2.0)",
        "Accept": "text/html,application/json,*/*;q=0.8",
        "Cache-Control": "no-cache",
    }

    # Layer 1: TCP Socket Handshake RTT
    tcp_ms = None
    tcp_ok = False
    if host:
        t_tcp = time.time()
        try:
            with socket.create_connection((host, 443), timeout=3.0):
                tcp_ms = int((time.time() - t_tcp) * 1000)
                tcp_ok = True
        except Exception:
            tcp_ms = None

    # Layer 2: HTTPS Root Ingress Check (allow_redirects=False avoids Streamlit Cloud 303 auth loop)
    t_ing = time.time()
    ingress_code = 0
    ingress_ms = 0
    edge_server = "Unknown"
    ingress_state = "🔴 Unreachable"
    try:
        r_root = requests.get(app_url, headers=headers, allow_redirects=False, timeout=4.5)
        ingress_code = r_root.status_code
        ingress_ms = int((time.time() - t_ing) * 1000)
        edge_server = r_root.headers.get("Server", r_root.headers.get("Via", "Cloud Ingress"))
        if ingress_code == 200:
            body_low = (r_root.text or "")[:2000].lower()
            if "gone to sleep" in body_low or "zzz" in body_low:
                ingress_state = "🟡 Hibernating (Sleep Mode)"
            else:
                ingress_state = "🟢 Awake & Serving (HTTP 200)"
        elif ingress_code in (301, 302, 303, 307, 308):
            loc = r_root.headers.get("Location", "")
            if "share.streamlit.io/-/auth/app" in loc:
                ingress_state = "🟢 Online (Cloud Ingress Active • HTTP 303)"
            else:
                ingress_state = f"🟢 Redirect Active (HTTP {ingress_code})"
        elif ingress_code >= 500:
            ingress_state = f"🔴 Container Error (HTTP {ingress_code})"
        else:
            ingress_state = f"🟡 HTTP {ingress_code}"
    except Exception as e:
        ingress_ms = int((time.time() - t_ing) * 1000)
        ingress_state = f"🔴 Error ({str(e)[:28]})"

    # Layer 3: Streamlit /_stcore/health Liveness Endpoint
    health_url = app_url.rstrip("/") + "/_stcore/health"
    t_hlth = time.time()
    liveness_status = "⚪ Unknown"
    liveness_ms = 0
    try:
        r_hlth = requests.get(health_url, headers=headers, allow_redirects=False, timeout=4.0)
        liveness_ms = int((time.time() - t_hlth) * 1000)
        h_code = r_hlth.status_code
        h_body = (r_hlth.text or "").strip().lower()
        if h_code == 200 and "ok" in h_body:
            liveness_status = f"🟢 HEALTHY (/_stcore/health = ok • {liveness_ms}ms)"
        elif h_code in (302, 303):
            liveness_status = f"🟢 REACHABLE (Ingress Gate 303 • {liveness_ms}ms)"
        elif h_code >= 500:
            liveness_status = f"🔴 UNHEALTHY (HTTP {h_code} • {liveness_ms}ms)"
        else:
            liveness_status = f"🟡 HTTP {h_code} ({liveness_ms}ms)"
    except Exception as e:
        liveness_ms = int((time.time() - t_hlth) * 1000)
        liveness_status = f"🔴 Probe Timeout ({liveness_ms}ms)"

    healthy = tcp_ok and (200 <= ingress_code < 400)
    return {
        "slug": repo["slug"],
        "healthy": healthy,
        "tcp_ok": tcp_ok,
        "tcp_ms": tcp_ms if tcp_ms is not None else -1,
        "ingress_code": ingress_code,
        "ingress_ms": ingress_ms,
        "ingress_state": ingress_state,
        "liveness_status": liveness_status,
        "liveness_ms": liveness_ms,
        "edge_server": edge_server,
        "probed_at": datetime.datetime.now(IST).strftime("%H:%M:%S IST"),
    }


@st.cache_data(ttl=120, show_spinner=False)
def probe_all_apps_health() -> dict:
    """Probes all 5 Streamlit Cloud deployments in parallel using ThreadPoolExecutor."""
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        for res in executor.map(_probe_single_app, REPOSITORIES):
            results[res["slug"]] = res
    return results


# =====================================================================
# GITHUB COMMIT TELEMETRY, WORKFLOW RUNS & BLOCKER FORENSICS ENGINE
# =====================================================================
def resolve_github_pat() -> str:
    """Resolves GitHub PAT from session state, Streamlit secrets, environment, or local git credential manager."""
    try:
        if st.session_state.get("master_github_pat"):
            return st.session_state["master_github_pat"].strip()
    except Exception:
        pass
    try:
        for k in ("GITHUB_PAT", "GH_PAT", "GITHUB_TOKEN"):
            val = st.secrets.get(k, "")
            if val:
                return str(val).strip()
    except Exception:
        pass
    for k in ("GITHUB_PAT", "GH_PAT", "GITHUB_TOKEN"):
        val = os.environ.get(k, "")
        if val:
            return val.strip()
    try:
        p = subprocess.Popen(
            ["git", "credential", "fill"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out, _ = p.communicate(input="protocol=https\nhost=github.com\n\n", timeout=2)
        for line in out.splitlines():
            if line.startswith("password="):
                token = line.split("=", 1)[1].strip()
                if token:
                    return token
    except Exception:
        pass
    return ""


def _fetch_single_repo_git_forensics(repo: dict, pat: str) -> dict:
    """
    Fetches live commit history, repository metadata, and recent GitHub Actions runs
    for a repository, and analyzes commits for potential app blockers.
    Falls back gracefully to verified baseline metadata if rate-limited or private without PAT.
    """
    full_repo = repo["full_repo"]
    headers = {
        "User-Agent": "Aethera-MasterHub-Forensics/2.0",
        "Accept": "application/vnd.github.v3+json",
    }
    if pat:
        headers["Authorization"] = f"token {pat}"

    fb = repo["fallback_commit"]
    result = {
        "slug": repo["slug"],
        "full_repo": full_repo,
        "live_api": False,
        "visibility": repo["visibility"],
        "size_kb": repo["repo_size_kb"],
        "latest_sha": fb["sha"],
        "latest_author": fb["author"],
        "latest_date_ist": fb["date_ist"],
        "latest_message": fb["message"],
        "latest_url": fb["url"],
        "recent_commits": [fb],
        "workflow_status": "⚪ No Scheduled Workflow" if not repo.get("workflow_file") else "🟢 Configured",
        "workflow_conclusion": "N/A",
        "workflow_last_run": "-",
        "detected_commit_risks": [],
    }

    try:
        # 1. Fetch commits (last 5)
        r_com = requests.get(
            f"https://api.github.com/repos/{full_repo}/commits?per_page=5",
            headers=headers,
            timeout=4.5,
        )
        if r_com.status_code == 200:
            commits_data = r_com.json()
            if isinstance(commits_data, list) and commits_data:
                result["live_api"] = True
                parsed_commits = []
                bot_commit_count = 0
                for c in commits_data:
                    sha = (c.get("sha") or "")[:7]
                    c_info = c.get("commit") or {}
                    author_info = c_info.get("author") or {}
                    author_name = author_info.get("name") or "Unknown"
                    raw_date = author_info.get("date") or ""
                    try:
                        dt = datetime.datetime.fromisoformat(raw_date.replace("Z", "+00:00")).astimezone(IST)
                        date_str = dt.strftime("%d-%b-%Y %H:%M IST")
                    except Exception:
                        date_str = raw_date
                    msg = (c_info.get("message") or "").splitlines()[0]
                    c_url = c.get("html_url") or f"https://github.com/{full_repo}/commit/{sha}"
                    parsed_commits.append(
                        {
                            "sha": sha,
                            "author": author_name,
                            "date_ist": date_str,
                            "message": msg,
                            "url": c_url,
                        }
                    )
                    if "bot" in author_name.lower() or "automated" in msg.lower():
                        bot_commit_count += 1
                    # Scan commit message for conflict/error/blocker indicators
                    msg_low = msg.lower()
                    if any(k in msg_low for k in ("conflict", "revert", "broken", "hotfix", "oom", "crash")):
                        result["detected_commit_risks"].append(
                            f"Commit `{sha}` flagged keyword (`{msg[:65]}`)"
                        )

                result["recent_commits"] = parsed_commits
                top = parsed_commits[0]
                result["latest_sha"] = top["sha"]
                result["latest_author"] = top["author"]
                result["latest_date_ist"] = top["date_ist"]
                result["latest_message"] = top["message"]
                result["latest_url"] = top["url"]

                if bot_commit_count >= 2:
                    result["detected_commit_risks"].append(
                        f"Frequent automated bot commits ({bot_commit_count}/5 recent commits) — causes Streamlit Cloud file-watcher reruns."
                    )

        # 2. Fetch latest GitHub Actions workflow run if applicable
        if repo.get("workflow_file"):
            r_wf = requests.get(
                f"https://api.github.com/repos/{full_repo}/actions/runs?per_page=3",
                headers=headers,
                timeout=4.0,
            )
            if r_wf.status_code == 200:
                runs = (r_wf.json() or {}).get("workflow_runs") or []
                if runs:
                    latest_run = runs[0]
                    st_val = latest_run.get("status", "unknown")
                    conc_val = latest_run.get("conclusion") or st_val
                    raw_w_date = latest_run.get("created_at") or ""
                    try:
                        w_dt = datetime.datetime.fromisoformat(raw_w_date.replace("Z", "+00:00")).astimezone(IST)
                        w_date_str = w_dt.strftime("%d-%b-%Y %H:%M IST")
                    except Exception:
                        w_date_str = raw_w_date
                    result["workflow_last_run"] = w_date_str
                    result["workflow_conclusion"] = conc_val
                    if conc_val == "success":
                        result["workflow_status"] = f"🟢 Passing ({w_date_str})"
                    elif conc_val in ("failure", "cancelled", "timed_out"):
                        result["workflow_status"] = f"🔴 Failed ({conc_val} • {w_date_str})"
                        result["detected_commit_risks"].append(
                            f"GitHub Actions workflow `{latest_run.get('name')}` ended with `{conc_val}` at {w_date_str}."
                        )
                    else:
                        result["workflow_status"] = f"🟡 {st_val} ({w_date_str})"
    except Exception:
        pass

    return result


@st.cache_data(ttl=180, show_spinner=False)
def fetch_all_repos_git_forensics(pat: str = "") -> dict:
    """Fetches Git commit & workflow forensics across all 5 repositories concurrently."""
    results = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(_fetch_single_repo_git_forensics, r, pat) for r in REPOSITORIES]
        for fut in futures:
            res = fut.result()
            results[res["slug"]] = res
    return results


def trigger_remote_container_reboot(full_repo: str, pat: str) -> tuple[bool, str]:
    """Triggers a Streamlit Cloud container reboot by committing a timestamp to .streamlit_reboot."""
    if not pat:
        return False, "Enter a GitHub PAT in the sidebar to push a .streamlit_reboot trigger commit."
    url = f"https://api.github.com/repos/{full_repo}/contents/.streamlit_reboot"
    headers = {
        "Authorization": f"token {pat.strip()}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Aethera-MasterHub-RebootTrigger",
    }
    sha = None
    try:
        r_get = requests.get(url, headers=headers, timeout=5)
        if r_get.status_code == 200:
            sha = r_get.json().get("sha")
    except Exception:
        pass

    now_ist = datetime.datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")
    content_b64 = base64.b64encode(
        f"Container reboot triggered via Aethera MasterRep at {now_ist}\n".encode("utf-8")
    ).decode("utf-8")
    payload = {
        "message": f"chore(reboot): trigger Streamlit container restart [{now_ist}]",
        "content": content_b64,
        "branch": "main",
    }
    if sha:
        payload["sha"] = sha

    try:
        r_put = requests.put(url, headers=headers, data=json.dumps(payload), timeout=7)
        if r_put.status_code in (200, 201):
            new_sha = (r_put.json().get("commit") or {}).get("sha", "")[:7]
            return True, f"✅ Pushed reboot commit `{new_sha}` to `{full_repo}`! Streamlit Cloud is restarting the app."
        return False, f"❌ GitHub API returned HTTP {r_put.status_code}: {r_put.text[:120]}"
    except Exception as e:
        return False, f"❌ Reboot request failed: {str(e)}"


# =====================================================================
# AUTHENTICATION LOGIC
# =====================================================================
def verify_credentials(username: str, password: str) -> bool:
    """Validates username (Admin) and password (Aether@) using constant-time comparison."""
    clean_user = (username or "").strip()
    clean_pass = (password or "").strip()
    user_ok = hmac.compare_digest(clean_user, MASTER_USERNAME) or hmac.compare_digest(
        clean_user.lower(), MASTER_USERNAME.lower()
    )
    pass_ok = hmac.compare_digest(clean_pass, MASTER_PASSWORD)
    return bool(user_ok and pass_ok)


def render_login_page() -> None:
    """Renders the centered login screen asking for Username (Admin) and Password (Aether@)."""
    st.markdown(
        '<div class="mantra-banner">'
        "✨ ॐ श्रीं महालक्ष्म्यै नमः • ॐ शुभ लाभाय नमः • Aethera Systems Core Quantitative Ecosystem ✨"
        "</div>",
        unsafe_allow_html=True,
    )

    _, center_col, _ = st.columns([1.1, 1.6, 1.1])
    with center_col:
        st.markdown(
            """
            <div class="login-card">
                <div style="text-align:center; margin-bottom: 1rem;">
                    <span style="font-size: 2.8rem;">🏛️</span>
                    <h2 style="margin: 0.3rem 0 0.2rem 0; color: #f8fafc;">Aethera Systems Core</h2>
                    <p style="margin: 0; color: #94a3b8; font-size: 0.95rem;">
                        Master Repository, Live App Liveness, CPU/RAM Telemetry &amp; Commit Blocker Portal
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("aethera_master_login_form", clear_on_submit=False):
            st.markdown("#### 🔐 Administrator Authentication")
            username_input = st.text_input(
                "User Name",
                placeholder="Enter User Name (Admin)",
                help="Enter the administrator username.",
            )
            password_input = st.text_input(
                "Password",
                type="password",
                placeholder="Enter Password",
                help="Enter the administrator password.",
            )
            submit_btn = st.form_submit_button(
                "🚀 Login to Master Repository Hub",
                use_container_width=True,
                type="primary",
            )

            if submit_btn:
                if verify_credentials(username_input, password_input):
                    st.session_state["authenticated"] = True
                    st.session_state["auth_user"] = MASTER_USERNAME
                    st.session_state["login_time_ist"] = datetime.datetime.now(IST).strftime(
                        "%Y-%m-%d %H:%M:%S IST"
                    )
                    st.rerun()
                else:
                    st.error("❌ Invalid User Name or Password. Please enter valid Admin credentials.")

        st.caption(
            "Protected Master Gateway • Authenticate to view all GitHub repositories, "
            "live liveness probes, CPU/RAM usage, commit blocker forensics, and external Cron scheduler links."
        )


# =====================================================================
# MAIN PORTAL DASHBOARD (POST-LOGIN)
# =====================================================================
def render_master_dashboard() -> None:
    """Renders the authenticated Master Repository, Health Probe, CPU/RAM & Commit Forensics Hub."""
    now_ist = datetime.datetime.now(IST).strftime("%d %b %Y • %H:%M:%S IST")
    host_tel = get_host_resource_telemetry()
    pat = resolve_github_pat()
    health_map = probe_all_apps_health()
    git_map = fetch_all_repos_git_forensics(pat)

    # Top Auspicious Banner
    st.markdown(
        '<div class="mantra-banner">'
        "✨ ॐ श्रीं महालक्ष्म्यै नमः • ॐ शुभ लाभाय नमः • Empowering Disciplined Quantitative Wealth Creation ✨"
        "</div>",
        unsafe_allow_html=True,
    )

    # Sidebar Controls, Live CPU/RAM Telemetry & Session Info
    with st.sidebar:
        st.markdown("### 🏛️ Master Command Hub")
        st.success(f"👤 **User:** `{st.session_state.get('auth_user', MASTER_USERNAME)}` (Verified)")
        st.caption(f"🕒 **Login Time:** {st.session_state.get('login_time_ist', now_ist)}")
        st.caption(f"🌐 **Current Time:** {now_ist}")

        if st.button("🔒 Logout", use_container_width=True, type="secondary"):
            st.session_state["authenticated"] = False
            st.session_state.pop("auth_user", None)
            st.rerun()

        st.divider()
        st.markdown("### 💻 Host CPU / RAM Telemetry")
        sc1, sc2 = st.columns(2)
        sc1.metric("App RAM (RSS)", f"{host_tel['app_ram_mb']:.1f} MB")
        sc2.metric("CPU Load", f"{host_tel['cpu_pct']:.1f}%")
        st.progress(
            min(100, int(host_tel["quota_pct"])),
            text=f"Cloud Quota: {host_tel['app_ram_mb']:.0f} / {host_tel['cgroup_limit_mb']:.0f} MB ({host_tel['quota_pct']:.1f}%)",
        )
        st.caption(
            f"**Status:** {host_tel['status']}  \n"
            f"**Cores:** {host_tel['cpu_count']} vCPU • **Threads:** {host_tel['active_threads']}  \n"
            f"**Disk Free:** {host_tel['disk_free_gb']} GB / {host_tel['disk_total_gb']} GB"
        )
        sb1, sb2 = st.columns(2)
        if sb1.button("🩺 Re-Probe All", use_container_width=True, help="Re-run live HTTP & GitHub probes"):
            probe_all_apps_health.clear()
            fetch_all_repos_git_forensics.clear()
            st.rerun()
        if sb2.button("🧹 Flush RAM", use_container_width=True, help="Run GC & Linux heap trim"):
            release_container_memory()
            st.toast("🧹 Memory flushed via Python GC & malloc_trim(0).")
            st.rerun()

        st.divider()
        st.markdown("### 🔍 Filter Repositories")
        search_query = st.text_input(
            "Search Keyword",
            placeholder="Search by name, commit, ETF, bond, AI...",
        ).strip()

        st.divider()
        st.markdown("### 🔑 GitHub PAT (Optional)")
        pat_input = st.text_input(
            "Personal Access Token",
            value=st.session_state.get("master_github_pat", ""),
            type="password",
            placeholder="ghp_... (for private repo & reboot)",
            help="Optional token to query private repo commits live and trigger 1-click .streamlit_reboot restarts.",
        )
        if pat_input != st.session_state.get("master_github_pat", ""):
            st.session_state["master_github_pat"] = pat_input.strip()
            fetch_all_repos_git_forensics.clear()
            st.rerun()

        st.divider()
        st.markdown("### ⏰ External Cron & Master Repo")
        st.link_button(
            "⏰ Open cron-job.org Scheduler",
            EXTERNAL_CRON_URL,
            use_container_width=True,
        )
        st.link_button(
            "🐙 GitHub: MasterRep",
            MASTER_GITHUB_REPO_MASTERREP,
            use_container_width=True,
        )

    # Top Title & Quick Actions
    head_left, head_right = st.columns([3.3, 1.3])
    with head_left:
        st.title("🏛️ Aethera Systems Core — Master Repository & Health Hub")
        st.markdown(
            "Authenticated command center for all **Aethera Systems Core** repositories: "
            "**GitHub & Streamlit App links**, **Live Liveness Probes (`/_stcore/health`)**, "
            "**CPU / RAM Resource Telemetry**, **Commit & App Blocker Forensics**, and **External Cron (`cron-job.org`)**."
        )
    with head_right:
        st.write("")
        st.link_button(
            "⏰ Launch External Cron (cron-job.org)",
            EXTERNAL_CRON_URL,
            use_container_width=True,
            type="primary",
        )
        if st.button("🩺 Run Live Health & Commit Probe Now", use_container_width=True):
            probe_all_apps_health.clear()
            fetch_all_repos_git_forensics.clear()
            st.rerun()

    # Summary KPI Strip
    online_count = sum(1 for r in REPOSITORIES if health_map.get(r["slug"], {}).get("healthy", False))
    avg_latency = int(
        sum(max(0, health_map.get(r["slug"], {}).get("ingress_ms", 0)) for r in REPOSITORIES)
        / max(1, len(REPOSITORIES))
    )
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Production Apps Online", f"{online_count} / {len(REPOSITORIES)} Reachable", f"Avg Ingress {avg_latency} ms")
    k2.metric("Host App Process RAM", f"{host_tel['app_ram_mb']:.1f} MB", f"{host_tel['quota_pct']:.1f}% of {host_tel['cgroup_limit_mb']:.0f} MB Quota")
    k3.metric("Host CPU & Threads", f"{host_tel['cpu_pct']:.1f}% CPU", f"{host_tel['cpu_count']} vCPU • {host_tel['active_threads']} Threads")
    k4.metric("Container Disk Free", f"{host_tel['disk_free_gb']} GB Free", f"{host_tel['disk_pct']}% Used of {host_tel['disk_total_gb']} GB")
    k5.metric("External Cron Engine", "cron-job.org", "Keep-Alive & Scheduled Sync")

    st.divider()

    # =================================================================
    # NAVIGATION TABS
    # =================================================================
    tab_repos, tab_health, tab_commits, tab_table = st.tabs(
        [
            "🚀 1. Repositories & Live Streamlit Apps (Cards)",
            "🩺 2. App Health, Liveness Probes & CPU/RAM Usage",
            "🔍 3. Commits, CI Workflows & App Blocker Forensics",
            "📊 4. Unified Master Directory Table & Cron URLs",
        ]
    )

    # Filter repositories by search query
    filtered_repos = REPOSITORIES
    if search_query:
        q = search_query.lower()
        filtered_repos = [
            r
            for r in REPOSITORIES
            if q in r["title"].lower()
            or q in r["slug"].lower()
            or q in r["category"].lower()
            or q in r["brief_explanation"].lower()
            or any(q in h.lower() for h in r["highlights"])
            or q in git_map.get(r["slug"], {}).get("latest_message", "").lower()
        ]

    # =================================================================
    # TAB 1: REPOSITORY CARDS (BRIEF EXPLANATION + GIT + STREAMLIT + LIVE STATUS)
    # =================================================================
    with tab_repos:
        # External Cron Banner
        st.markdown(
            f"""
            <div class="cron-card">
                <span class="category-pill" style="background:rgba(16,185,129,0.2); color:#6ee7b7; border-color:rgba(16,185,129,0.45);">
                    ⏰ EXTERNAL CRON AUTOMATION &amp; KEEP-ALIVE SCHEDULER
                </span>
                <h4 style="margin:0.2rem 0 0.3rem 0; color:#f8fafc;">
                    External Cron Scheduler — <a href="{EXTERNAL_CRON_URL}" target="_blank" style="color:#34d399; text-decoration:underline;">{EXTERNAL_CRON_URL}</a>
                </h4>
                <p style="margin:0; color:#cbd5e1; font-size:0.92rem;">
                    Prevents Streamlit Cloud container hibernation ("Zzz" sleep state) and triggers scheduled market-hour wake-ups across all 5 apps.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        c_b1, c_b2 = st.columns(2)
        with c_b1:
            st.link_button(
                "⏰ Open External Cron (https://cron-job.org/en/)",
                EXTERNAL_CRON_URL,
                use_container_width=True,
                type="primary",
            )
        with c_b2:
            st.link_button(
                "🐙 Open Master Git Repo (https://github.com/aetherasystemscore/MasterRep)",
                MASTER_GITHUB_REPO_MASTERREP,
                use_container_width=True,
            )

        st.subheader(f"🚀 All Aethera Systems Core Repositories ({len(filtered_repos)})")

        for repo in filtered_repos:
            slug = repo["slug"]
            hlth = health_map.get(slug, {})
            git_info = git_map.get(slug, {})
            badge_class = "badge-ok" if hlth.get("healthy") else "badge-warn"

            st.markdown(
                f"""
                <div class="repo-card" style="border-left: 5px solid {repo['accent']};">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
                        <span class="category-pill">{repo['icon']} App #{repo['id']} • {repo['category']}</span>
                        <div>
                            <span class="{badge_class}">{hlth.get('ingress_state', '🟢 Online')} • {hlth.get('ingress_ms', 0)} ms</span>
                            <span class="category-pill" style="margin-left:6px;">💾 Est. RAM: {repo['est_ram_mb']}</span>
                            <span class="category-pill" style="margin-left:6px;">🔨 Latest Commit: {git_info.get('latest_sha', '-')} ({git_info.get('latest_date_ist', '-')})</span>
                        </div>
                    </div>
                    <h3 style="margin: 0.2rem 0 0.45rem 0; color: #f8fafc;">
                        {repo['icon']} {repo['title']} <span style="color:#94a3b8; font-size:0.95rem; font-weight:400;">({repo['slug']})</span>
                    </h3>
                    <p style="color: #e2e8f0; font-size: 0.95rem; line-height: 1.55; margin-bottom: 0.6rem;">
                        <strong>Brief Explanation:</strong> {repo['brief_explanation']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col_links, col_highlights = st.columns([1.35, 1.65])
            with col_links:
                st.markdown("**🔗 Direct Repository & Live App Links:**")
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    st.link_button(
                        "🚀 Open Streamlit App",
                        repo["streamlit_url"],
                        use_container_width=True,
                        type="primary",
                    )
                with btn_col2:
                    st.link_button(
                        "🐙 Open Git Repository",
                        repo["git_url"],
                        use_container_width=True,
                    )

                st.markdown(
                    f"""
                    <div class="url-box">
                        <strong>Streamlit App:</strong> <a href="{repo['streamlit_url']}" target="_blank" style="color:#38bdf8;">{repo['streamlit_url']}</a><br/>
                        <strong>Git Repository:</strong> <a href="{repo['git_url']}" target="_blank" style="color:#a7f3d0;">{repo['git_url']}</a><br/>
                        <strong>Latest Commit:</strong> <a href="{git_info.get('latest_url', repo['git_url'])}" target="_blank" style="color:#fde68a;">{git_info.get('latest_sha', '')}</a> — {git_info.get('latest_message', '')[:85]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col_highlights:
                st.markdown("**⚡ Key Quantitative Capabilities:**")
                for bullet in repo["highlights"]:
                    st.markdown(f"- {bullet}")

            st.write("")

    # =================================================================
    # TAB 2: APP HEALTH, LIVENESS PROBES (/_stcore/health) & CPU/RAM USAGE
    # =================================================================
    with tab_health:
        st.subheader("💻 Real-Time Container & Host Resource Telemetry (CPU / RAM / Disk / Threads)")
        st.markdown(
            f"""
            <div class="telemetry-card">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                    <div>
                        <h4 style="margin:0 0 0.25rem 0; color:#f8fafc;">Runtime Environment: <code>{host_tel['platform']}</code></h4>
                        <p style="margin:0; color:#94a3b8; font-size:0.9rem;">
                            Last Polled: <strong>{host_tel['timestamp']}</strong> • OS Load Avg (1m/5m/15m): <code>{host_tel['load_avg_str']}</code> •
                            System RAM Used: <code>{host_tel['system_used_ram_mb']} MB / {host_tel['system_total_ram_mb']} MB ({host_tel['system_ram_pct']}%)</code>
                        </p>
                    </div>
                    <div>
                        <span class="badge-ok" style="color:{host_tel['status_color']}; border-color:{host_tel['status_color']};">
                            {host_tel['status']}
                        </span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        m1, m2, m3, m4 = st.columns(4)
        m1.metric(
            "App Process Memory (VmRSS)",
            f"{host_tel['app_ram_mb']:.1f} MB",
            f"Limit: {host_tel['cgroup_limit_mb']:.0f} MB ({host_tel['quota_pct']:.1f}%)",
        )
        m2.metric(
            "CPU Utilization",
            f"{host_tel['cpu_pct']:.1f}%",
            f"{host_tel['cpu_count']} Logical vCPUs",
        )
        m3.metric(
            "Active Python Threads",
            f"{host_tel['active_threads']} Threads",
            f"Load Avg: {host_tel['load_avg_str']}",
        )
        m4.metric(
            "Ephemeral Container SSD",
            f"{host_tel['disk_free_gb']} GB Free",
            f"{host_tel['disk_pct']}% Used of {host_tel['disk_total_gb']} GB",
        )

        st.progress(
            min(100, int(host_tel["quota_pct"])),
            text=f"Streamlit Cloud Container Memory Headroom: {host_tel['app_ram_mb']:.1f} MB used of {host_tel['cgroup_limit_mb']:.0f} MB cgroup ceiling ({100.0 - host_tel['quota_pct']:.1f}% free)",
        )

        st.divider()
        st.subheader("🩺 Live Application Health & Liveness Probe Matrix (`/_stcore/health` & TCP/HTTPS)")
        st.caption(
            "Concurrently probes TCP Port 443 socket RTT, HTTPS Root Ingress (`GET /`), and Streamlit's internal "
            "Tornado liveness endpoint (`GET /_stcore/health`) across all 5 deployed apps."
        )

        liveness_rows = []
        for repo in REPOSITORIES:
            slug = repo["slug"]
            h = health_map.get(slug, {})
            liveness_rows.append(
                {
                    "#": repo["id"],
                    "Application": f"{repo['icon']} {repo['title']}",
                    "Ingress Health": h.get("ingress_state", "⚪ Unknown"),
                    "Liveness Probe (/_stcore/health)": h.get("liveness_status", "⚪ Unknown"),
                    "TCP 443 RTT (ms)": h.get("tcp_ms", -1),
                    "HTTPS Latency (ms)": h.get("ingress_ms", -1),
                    "Est. Container RAM": repo["est_ram_mb"],
                    "CPU / Workload Profile": repo["est_cpu_profile"],
                    "Live App URL": repo["streamlit_url"],
                    "Health Endpoint": repo["streamlit_url"].rstrip("/") + "/_stcore/health",
                }
            )

        df_health = pd.DataFrame(liveness_rows)
        st.dataframe(
            df_health,
            use_container_width=True,
            hide_index=True,
            column_config={
                "#": st.column_config.NumberColumn("#", width="small"),
                "Live App URL": st.column_config.LinkColumn("Live App URL", width="medium"),
                "Health Endpoint": st.column_config.LinkColumn("/_stcore/health URL", width="medium"),
            },
        )

    # =================================================================
    # TAB 3: COMMITS, CI WORKFLOWS & APP BLOCKER FORENSICS
    # =================================================================
    with tab_commits:
        st.subheader("🔍 Git Commit History, CI/CD Workflows & App Blocker Forensics")
        st.markdown(
            "Analyzes the latest commits, dependency manifests (`requirements.txt`), repository sizes, visibility rules, "
            "and automated GitHub Actions workflows across all repositories to identify **what can block, stall, or restart** "
            "a Streamlit Cloud deployment."
        )

        # Summary Table of Latest Commits & Workflow Status
        commit_summary_rows = []
        for repo in REPOSITORIES:
            slug = repo["slug"]
            g = git_map.get(slug, {})
            high_blockers = [b for b in repo["blocker_diagnostics"] if b["severity"] in ("HIGH", "MEDIUM")]
            blocker_badge = (
                f"⚠️ {len(high_blockers)} Active Watch Item(s)"
                if high_blockers
                else "🟢 Clear"
            )
            commit_summary_rows.append(
                {
                    "#": repo["id"],
                    "Repository": f"{repo['icon']} {repo['slug']}",
                    "Visibility": g.get("visibility", repo["visibility"]),
                    "Repo Size": f"{g.get('size_kb', repo['repo_size_kb'])} KB",
                    "Latest SHA": g.get("latest_sha", "-"),
                    "Commit Date (IST)": g.get("latest_date_ist", "-"),
                    "Author": g.get("latest_author", "-"),
                    "Latest Commit Message": g.get("latest_message", "-"),
                    "GitHub Actions Status": g.get("workflow_status", "-"),
                    "Blocker Risk Summary": blocker_badge,
                    "Commit Diff Link": g.get("latest_url", repo["git_url"]),
                }
            )

        st.dataframe(
            pd.DataFrame(commit_summary_rows),
            use_container_width=True,
            hide_index=True,
            column_config={
                "#": st.column_config.NumberColumn("#", width="small"),
                "Commit Diff Link": st.column_config.LinkColumn("Commit Diff Link", width="small"),
            },
        )

        st.divider()
        st.subheader("🛠️ Per-Repository Commit History & App Blocker Breakdown")

        for repo in filtered_repos:
            slug = repo["slug"]
            g = git_map.get(slug, {})
            with st.expander(
                f"{repo['icon']} {repo['title']} ({repo['full_repo']}) — Latest Commit `{g.get('latest_sha')}` • {g.get('latest_date_ist')}",
                expanded=True,
            ):
                c_left, c_right = st.columns([1.45, 1.55])
                with c_left:
                    st.markdown("##### 📜 Recent Commits (`main` branch)")
                    for c_item in g.get("recent_commits", []):
                        st.markdown(
                            f"- [`{c_item['sha']}`]({c_item['url']}) **{c_item['date_ist']}** (*{c_item['author']}*): {c_item['message']}"
                        )

                    st.markdown("##### 📦 Key Dependencies (`requirements.txt`)")
                    st.code(", ".join(repo["key_dependencies"]), language="text")

                    if st.button(
                        f"🔄 Trigger Container Reboot (.streamlit_reboot) on {slug}",
                        key=f"reboot_{slug}",
                        use_container_width=True,
                    ):
                        ok, msg = trigger_remote_container_reboot(repo["full_repo"], pat)
                        if ok:
                            st.success(msg)
                        else:
                            st.warning(msg)

                with c_right:
                    st.markdown("##### 🚨 Potential App Blockers & Commit Forensics")
                    for diag in repo["blocker_diagnostics"]:
                        sev = diag["severity"]
                        if sev == "HIGH":
                            st.error(f"**[HIGH RISK — {diag['type']}]** {diag['detail']}")
                        elif sev == "MEDIUM":
                            st.warning(f"**[WATCH — {diag['type']}]** {diag['detail']}")
                        elif sev == "RESOLVED":
                            st.success(f"**[RESOLVED — {diag['type']}]** {diag['detail']}")
                        else:
                            st.info(f"**[INFO — {diag['type']}]** {diag['detail']}")

                    for dyn_risk in g.get("detected_commit_risks", []):
                        st.warning(f"**[LIVE COMMIT SCAN]** {dyn_risk}")

    # =================================================================
    # TAB 4: UNIFIED MASTER DIRECTORY TABLE & CRON TARGETS
    # =================================================================
    with tab_table:
        st.subheader("📊 Unified Master Directory Table — All Repositories, Health, Commits & Links")

        table_rows = []
        for r in filtered_repos:
            slug = r["slug"]
            h = health_map.get(slug, {})
            g = git_map.get(slug, {})
            table_rows.append(
                {
                    "#": r["id"],
                    "Repository Name": f"{r['icon']} {r['title']} ({r['slug']})",
                    "App Health": h.get("ingress_state", "🟢 Online"),
                    "Est. RAM": r["est_ram_mb"],
                    "Latest Commit": f"{g.get('latest_sha', '-')} ({g.get('latest_date_ist', '-')})",
                    "Brief Explanation": r["brief_explanation"],
                    "Git Repository Link": r["git_url"],
                    "Streamlit App Link": r["streamlit_url"],
                }
            )

        table_rows.append(
            {
                "#": 6,
                "Repository Name": "🏛️ Master Repository Hub (MasterRep)",
                "App Health": "🟢 Active (Current Portal)",
                "Est. RAM": f"{host_tel['app_ram_mb']:.1f} MB (Live)",
                "Latest Commit": "main (Active)",
                "Brief Explanation": (
                    "Central authenticated gateway (Admin / Aether@) listing all Aethera Systems Core "
                    "GitHub repositories, brief explanations, liveness probes, CPU/RAM usage, commit blocker forensics, and external cron automation."
                ),
                "Git Repository Link": MASTER_GITHUB_REPO_MASTERREP,
                "Streamlit App Link": MASTER_GITHUB_REPO_MASTERREP,
            }
        )
        table_rows.append(
            {
                "#": 7,
                "Repository Name": "⏰ External Cron Scheduler (cron-job.org)",
                "App Health": "🟢 External Scheduler",
                "Est. RAM": "Cloud SaaS",
                "Latest Commit": "24x7 Active",
                "Brief Explanation": (
                    "External scheduled cron job platform used to trigger automated HTTP wake-up pings and "
                    "scheduled background tasks across the deployed Streamlit applications."
                ),
                "Git Repository Link": EXTERNAL_CRON_URL,
                "Streamlit App Link": EXTERNAL_CRON_URL,
            }
        )

        df_master = pd.DataFrame(table_rows)
        st.dataframe(
            df_master,
            use_container_width=True,
            hide_index=True,
            column_config={
                "#": st.column_config.NumberColumn("#", width="small"),
                "Repository Name": st.column_config.TextColumn("Repository / System", width="medium"),
                "Brief Explanation": st.column_config.TextColumn("Brief Explanation", width="large"),
                "Git Repository Link": st.column_config.LinkColumn("Git Repository Link", width="medium"),
                "Streamlit App Link": st.column_config.LinkColumn("Streamlit App / Target Link", width="medium"),
            },
        )

        st.markdown("#### ⏰ Copyable Streamlit App & `/_stcore/health` URLs for `cron-job.org` Keep-Alive Jobs")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.caption("**Primary Streamlit App URLs:**")
            st.code("\n".join([r["streamlit_url"] for r in REPOSITORIES]), language="text")
        with col_c2:
            st.caption("**Internal Liveness Probe (`/_stcore/health`) URLs:**")
            st.code(
                "\n".join([r["streamlit_url"].rstrip("/") + "/_stcore/health" for r in REPOSITORIES]),
                language="text",
            )

        csv_bytes = df_master.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download Master Repository & Health Directory (CSV)",
            data=csv_bytes,
            file_name="aethera_master_repositories_health.csv",
            mime="text/csv",
        )


# =====================================================================
# ENTRYPOINT
# =====================================================================
def main() -> None:
    inject_custom_css()
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        render_login_page()
    else:
        render_master_dashboard()


if __name__ == "__main__":
    main()
