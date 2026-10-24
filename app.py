"""
Aethera Systems Core — Master Repository & Live Application Hub (MasterRep)
Authenticated gateway listing all Aethera Systems Core GitHub repositories,
brief explanations, live Streamlit Cloud deployments, and external Cron scheduler links.
"""

import datetime
import hmac
import urllib.request
import urllib.error
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

# =====================================================================
# PAGE CONFIGURATION
# =====================================================================
st.set_page_config(
    page_title="Aethera Systems Core • Master Repository & App Hub",
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
        "title": "Stock, ETF, REIT & InvIT Quantitative Screener",
        "icon": "🎯",
        "category": "Multi-Asset Tactical Allocator & Paper Trader",
        "accent": "#38bdf8",
        "git_url": "https://github.com/aetherasystemscore/stock-etf-reit-invit-screener",
        "streamlit_url": "https://stock-etf-reit-invit-screener-djbh7czff5apmlkv27srrp.streamlit.app/",
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
        "title": "SmartStock Radar (v5.0 Catalyst & Bear-Market Terminal)",
        "icon": "📡",
        "category": "Event Catalyst NLP & Deep-Value Equity Intelligence",
        "accent": "#ec4899",
        "git_url": "https://github.com/aetherasystemscore/SmartStock-Radar",
        "streamlit_url": "https://smartstock-radar.streamlit.app/",
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
        "title": "HNI & Institutional Investor Trend Radar",
        "icon": "🏛️",
        "category": "Superstar Filings, 15Y Index S/R & Sectoral ETFs",
        "accent": "#f59e0b",
        "git_url": "https://github.com/aetherasystemscore/HNI-Institutional-Investor-Trend",
        "streamlit_url": "https://hni-institutional-investor-trend-uyvhb3nw3abdvqjrfmedf6.streamlit.app/",
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
        "title": "AI Data Center & Power Infrastructure Growth Theme (AI3)",
        "icon": "🖥️",
        "category": "Thematic Value-Chain Research, IPO Tracker & Optimiser",
        "accent": "#10b981",
        "git_url": "https://github.com/aetherasystemscore/AI-Data-Center-Growth-Theme",
        "streamlit_url": "https://ai-data-center-growth-theme-hg4oggdawtcqefqn48n5gm.streamlit.app/",
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
        "title": "Indian Listed NCD, G-Sec & Corporate Bond Screener",
        "icon": "📜",
        "category": "Fixed Income, Sovereign G-Secs & Tax-Free PSU Debt",
        "accent": "#a855f7",
        "git_url": "https://github.com/aetherasystemscore/NCD-Bond_Screener",
        "streamlit_url": "https://ncd-bondscreener-bgftfvgej8y5bsng8id54t.streamlit.app/",
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
            padding-top: 1.4rem;
            padding-bottom: 2.5rem;
            max-width: 1400px;
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
            padding: 1.35rem 1.5rem;
            margin-bottom: 1.1rem;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }
        .cron-card {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.14) 0%, rgba(15, 23, 42, 0.95) 100%);
            border: 1px solid rgba(16, 185, 129, 0.45);
            border-radius: 14px;
            padding: 1.2rem 1.5rem;
            margin-bottom: 1.4rem;
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
            margin-bottom: 0.45rem;
        }
        .url-box {
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 8px;
            padding: 0.45rem 0.75rem;
            font-family: monospace;
            font-size: 0.82rem;
            color: #e2e8f0;
            word-break: break-all;
            margin-top: 0.25rem;
            margin-bottom: 0.55rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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
                        Master Repository &amp; Live Streamlit Application Portal
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
            "brief architectural explanations, live Streamlit apps, and external Cron scheduler links."
        )


# =====================================================================
# OPTIONAL LIVE PING UTILITY
# =====================================================================
@st.cache_data(ttl=180, show_spinner=False)
def check_url_reachability(url: str) -> str:
    """Checks if a URL responds with HTTP 200/302/303."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Aethera-MasterHub-HealthCheck/1.0"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            code = getattr(resp, "status", 200)
            if 200 <= code < 400:
                return f"🟢 Online (HTTP {code})"
            return f"🟡 HTTP {code}"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 404):
            # Private GitHub repos return 404 without token when probed anonymously
            return f"🔒 Protected / Auth (HTTP {e.code})"
        return f"🟡 HTTP {e.code}"
    except Exception:
        return "⚪ Unverified"


# =====================================================================
# MAIN PORTAL DASHBOARD (POST-LOGIN)
# =====================================================================
def render_master_dashboard() -> None:
    """Renders the authenticated Master Repository & Streamlit App directory."""
    now_ist = datetime.datetime.now(IST).strftime("%d %b %Y • %H:%M:%S IST")

    # Top Auspicious Banner
    st.markdown(
        '<div class="mantra-banner">'
        "✨ ॐ श्रीं महालक्ष्म्यै नमः • ॐ शुभ लाभाय नमः • Empowering Disciplined Quantitative Wealth Creation ✨"
        "</div>",
        unsafe_allow_html=True,
    )

    # Sidebar Controls & Session Info
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
        st.markdown("### 🧭 Quick Navigation")
        view_mode = st.radio(
            "Display Layout",
            options=[
                "📇 Detailed Cards + Summary Table",
                "📇 Detailed Cards Only",
                "📊 Summary Table Only",
            ],
            index=0,
        )
        search_query = st.text_input(
            "🔍 Filter Repositories",
            placeholder="Search by name, keyword, ETF, bond, AI...",
        ).strip()

        st.divider()
        st.markdown("### ⏰ External Cron Scheduler")
        st.link_button(
            "⏰ Open cron-job.org Scheduler",
            EXTERNAL_CRON_URL,
            use_container_width=True,
        )
        st.caption(f"Direct Link: [{EXTERNAL_CRON_URL}]({EXTERNAL_CRON_URL})")

        st.divider()
        st.markdown("### 🗂️ Master Repository Link")
        st.link_button(
            "🐙 GitHub: MasterRep",
            MASTER_GITHUB_REPO_MASTERREP,
            use_container_width=True,
        )

    # Top Title & Header Metrics
    head_left, head_right = st.columns([3.4, 1.2])
    with head_left:
        st.title("🏛️ Aethera Systems Core — Master Repository & Live App Hub")
        st.markdown(
            "Centralized authenticated directory of all **Aethera Systems Core** quantitative repositories, "
            "complete with brief architectural explanations, **GitHub Repository links**, **Live Streamlit App links**, "
            "and **External Cron Automation (`cron-job.org`)**."
        )
    with head_right:
        st.write("")
        st.link_button(
            "⏰ Launch External Cron (cron-job.org)",
            EXTERNAL_CRON_URL,
            use_container_width=True,
            type="primary",
        )
        if st.button("🔒 Sign Out (Admin)", use_container_width=True):
            st.session_state["authenticated"] = False
            st.rerun()

    # KPI Metric Strip
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Production Repositories", f"{len(REPOSITORIES)} Core Apps", "GitHub + Streamlit")
    k2.metric("Master Gateway Repo", "MasterRep", "Authenticated Hub")
    k3.metric("External Cron Engine", "cron-job.org", "24x7 Scheduled Wake & Sync")
    k4.metric("Session Status", "Admin Verified", now_ist.split("•")[-1].strip())

    st.divider()

    # =================================================================
    # SECTION 1: EXTERNAL CRON SCHEDULER & MASTER REPOSITORY BANNER
    # =================================================================
    st.markdown(
        f"""
        <div class="cron-card">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.8rem;">
                <div>
                    <span class="category-pill" style="background:rgba(16,185,129,0.2); color:#6ee7b7; border-color:rgba(16,185,129,0.45);">
                        ⏰ EXTERNAL CRON AUTOMATION &amp; KEEP-ALIVE SCHEDULER
                    </span>
                    <h3 style="margin:0.2rem 0 0.35rem 0; color:#f8fafc;">
                        External Cron Job Management — <a href="{EXTERNAL_CRON_URL}" target="_blank" style="color:#34d399; text-decoration:underline;">{EXTERNAL_CRON_URL}</a>
                    </h3>
                    <p style="margin:0; color:#cbd5e1; font-size:0.94rem;">
                        Used to schedule automated HTTP wake-up pings, container health checks, and market-hour execution triggers across all 5 Streamlit Cloud deployments.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        st.link_button(
            "⏰ Open External Cron (https://cron-job.org/en/)",
            EXTERNAL_CRON_URL,
            use_container_width=True,
            type="primary",
        )
    with c_btn2:
        st.link_button(
            "🐙 Open Master Git Repo (https://github.com/aetherasystemscore/MasterRep)",
            MASTER_GITHUB_REPO_MASTERREP,
            use_container_width=True,
        )

    st.write("")

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
        ]

    # =================================================================
    # SECTION 2: DETAILED REPOSITORY CARDS (GIT REPO + STREAMLIT APP)
    # =================================================================
    if view_mode in ("📇 Detailed Cards + Summary Table", "📇 Detailed Cards Only"):
        st.subheader(f"🚀 All Aethera Systems Core Repositories & Live Streamlit Apps ({len(filtered_repos)})")

        for repo in filtered_repos:
            st.markdown(
                f"""
                <div class="repo-card" style="border-left: 5px solid {repo['accent']};">
                    <div class="category-pill">{repo['icon']} App #{repo['id']} • {repo['category']}</div>
                    <h3 style="margin: 0.15rem 0 0.45rem 0; color: #f8fafc;">
                        {repo['icon']} {repo['title']} <span style="color:#94a3b8; font-size:0.95rem; font-weight:400;">({repo['slug']})</span>
                    </h3>
                    <p style="color: #e2e8f0; font-size: 0.96rem; line-height: 1.55; margin-bottom: 0.75rem;">
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
                        <strong>Git Repository:</strong> <a href="{repo['git_url']}" target="_blank" style="color:#a7f3d0;">{repo['git_url']}</a>
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
    # SECTION 3: UNIFIED MASTER DIRECTORY TABLE (ALL REPOS + CRON)
    # =================================================================
    if view_mode in ("📇 Detailed Cards + Summary Table", "📊 Summary Table Only"):
        st.divider()
        st.subheader("📊 Master Directory Table — All Repositories, Explanations & Links")

        table_rows = []
        for r in filtered_repos:
            table_rows.append(
                {
                    "#": r["id"],
                    "Repository Name": f"{r['icon']} {r['title']} ({r['slug']})",
                    "Category": r["category"],
                    "Brief Explanation": r["brief_explanation"],
                    "Git Repository Link": r["git_url"],
                    "Streamlit App Link": r["streamlit_url"],
                }
            )

        # Append Master Repository & External Cron rows for completeness
        table_rows.append(
            {
                "#": 6,
                "Repository Name": "🏛️ Master Repository Hub (MasterRep)",
                "Category": "Master Gateway & Authentication Hub",
                "Brief Explanation": (
                    "Central authenticated gateway (Admin / Aether@) listing all Aethera Systems Core "
                    "GitHub repositories, brief explanations, live Streamlit app deployments, and external cron automation."
                ),
                "Git Repository Link": MASTER_GITHUB_REPO_MASTERREP,
                "Streamlit App Link": MASTER_GITHUB_REPO_MASTERREP,
            }
        )
        table_rows.append(
            {
                "#": 7,
                "Repository Name": "⏰ External Cron Scheduler (cron-job.org)",
                "Category": "External Cron & Keep-Alive Automation",
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
                "Category": st.column_config.TextColumn("Category", width="medium"),
                "Brief Explanation": st.column_config.TextColumn("Brief Explanation", width="large"),
                "Git Repository Link": st.column_config.LinkColumn(
                    "Git Repository Link",
                    help="Click to open the GitHub Repository",
                    width="medium",
                ),
                "Streamlit App Link": st.column_config.LinkColumn(
                    "Streamlit App / Target Link",
                    help="Click to open the Live Streamlit Application",
                    width="medium",
                ),
            },
        )

        # Quick Copy & Export Expander
        with st.expander("📋 Copyable Markdown / CSV Reference & Cron Target URLs", expanded=False):
            st.markdown("#### 🔗 All 5 Live Streamlit App URLs (for `cron-job.org` or Bookmarks)")
            cron_urls_text = "\n".join([r["streamlit_url"] for r in REPOSITORIES])
            st.code(cron_urls_text, language="text")

            st.markdown("#### 🐙 All GitHub Repository URLs")
            git_urls_text = "\n".join(
                [r["git_url"] for r in REPOSITORIES]
                + [MASTER_GITHUB_REPO_MASTERREP]
            )
            st.code(git_urls_text, language="text")

            st.markdown("#### ⏰ External Cron URL")
            st.code(EXTERNAL_CRON_URL, language="text")

            csv_bytes = df_master.to_csv(index=False).encode("utf-8")
            st.download_button(
                "📥 Download Master Repository Directory (CSV)",
                data=csv_bytes,
                file_name="aethera_master_repositories.csv",
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
