# 🛡️ Aethera Systems Core — Master Operations & SRE Command Portal

Authenticated **Master Portal & SRE Command Center** for all **Aethera Systems Core** quantitative financial research repositories, live Streamlit Cloud applications, real-time liveness probes, container CPU/RAM telemetry, and commit/CI blocker forensics.

- **Master GitHub Repository:** [https://github.com/aetherasystemscore/MasterRep](https://github.com/aetherasystemscore/MasterRep)
- **External Cron Scheduler:** [https://cron-job.org/en/](https://cron-job.org/en/)

---

## 🔐 Login Credentials

Access to the Master Portal is protected by an authentication gate:

| Field | Value |
| :--- | :--- |
| **User Name** | `Admin` |
| **Password** | `Aether@` |

---

## 🩺 Key SRE & Operations Features

### 1. Real-Time App Health & 3-Layer Liveness Probes
Concurrently probes all 5 deployed Streamlit Cloud applications across three network layers:
1. **TCP Socket Handshake (`:443`)** — Measures raw network round-trip latency (ms) and TLS reachability.
2. **HTTPS Root Ingress (`GET /`)** — Inspects Streamlit Cloud edge routing (`HTTP 200 OK` vs `HTTP 303 Auth Cookie Redirect` vs `502/503 Booting`).
3. **Streamlit Internal Liveness Probe (`GET /_stcore/health`)** — Queries the internal Tornado health endpoint (`ok` payload check) to detect asleep containers (`Zzz`), frozen event loops, or OOM-crashed workers.
- **1-Click Wake-Up Ping** per app or across all 5 apps simultaneously.

### 2. Host Container CPU / RAM / Disk / Thread Telemetry & Per-App Resource Matrix
- **Live Container Telemetry (`psutil` + Linux `/proc/self/status` + cgroup v1/v2):**
  - Tracks **Process Resident Memory (`VmRSS`)** against the **1,024 MB Streamlit Community Cloud hard limit**, with automatic warning (`>75%`) and critical OOM (`>88%`) thresholds.
  - Displays **CPU Utilization (%)**, **1m / 5m / 15m OS Load Averages**, **Active Python Threads**, **Open File Descriptors**, and **Container Ephemeral Disk Usage**.
  - Includes a **🧹 Force GC + `malloc_trim(0)`** button to immediately reclaim unreferenced Python objects and return free heap pages to the Linux kernel.
- **Per-App Resource Footprint Matrix:**
  - Profiles estimated steady-state and peak RAM (MB), CPU load profile, cold-start time, and heavy dependency stacks (`xgboost`, `lightgbm`, `optuna`, `scikit-learn`, `yfinance`, etc.) for all 5 Aethera apps.

### 3. Commit History, CI/CD Workflow Status & App Blocker Forensics
- **Live GitHub REST API Polling (`commits` + `actions/runs`)** with pre-verified fallback metadata (including support for private repositories via optional `GITHUB_TOKEN`).
- **Automated Blocker Heuristics & Root-Cause Diagnostics** for common Streamlit Cloud failure modes:
  - **Bot Auto-Commit File-Watcher Reload Loops:** Detects `github-actions[bot]` commits to `main` that trigger mid-session Streamlit script reruns.
  - **1 GB RAM OOM Risk (`SIGKILL` / Exit Code 137):** Flags heavy ML dependency footprints (`SmartStock-Radar`) and unbounded dataframe caches.
  - **Cold-Start / Main-Thread Backfill Stalls:** Identifies synchronous startup catch-up jobs (`HNI-Institutional-Investor-Trend`) that can delay `/_stcore/health` readiness.
  - **Upstream Cloud IP Rate-Limiting (`HTTP 403` / Timeout):** Tracks NSE India API cloud IP blocks (`NCD-Bond_Screener`) and Yahoo Finance burst throttling.
  - **Dependency Build Blockers:** Documents native wheel compilation fixes (e.g., removing `scipy` in `NCD-Bond_Screener`).
- **🔄 1-Click Remote Container Reboot Trigger:** Can commit a timestamp to `.streamlit_reboot` via the GitHub Contents API (when `GITHUB_TOKEN` is provided) to force a clean container restart on any app.

---

## 📦 Registered Repositories & Live Streamlit Apps

| # | Application Name | Category | GitHub Repository | Live Streamlit App |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Stock, ETF, REIT & InvIT Screener** | Equities, ETFs, REITs & InvITs | [aetherasystemscore/stock-etf-reit-invit-screener](https://github.com/aetherasystemscore/stock-etf-reit-invit-screener) | [Launch Streamlit App](https://stock-etf-reit-invit-screener-djbh7czff5apmlkv27srrp.streamlit.app/) |
| **2** | **SmartStock Radar** | Quantitative Stock Discovery | [aetherasystemscore/SmartStock-Radar](https://github.com/aetherasystemscore/SmartStock-Radar) | [Launch Streamlit App](https://smartstock-radar.streamlit.app/) |
| **3** | **HNI & Institutional Investor Trend Tracker** | Institutional & Smart-Money Flows | [aetherasystemscore/HNI-Institutional-Investor-Trend](https://github.com/aetherasystemscore/HNI-Institutional-Investor-Trend) | [Launch Streamlit App](https://hni-institutional-investor-trend-uyvhb3nw3abdvqjrfmedf6.streamlit.app/) |
| **4** | **AI & Data Center Growth Theme Tracker** | Thematic Equity Research | [aetherasystemscore/AI-Data-Center-Growth-Theme](https://github.com/aetherasystemscore/AI-Data-Center-Growth-Theme) | [Launch Streamlit App](https://ai-data-center-growth-theme-hg4oggdawtcqefqn48n5gm.streamlit.app/) |
| **5** | **NCD & Bond Screener** | Fixed Income & Debt Markets | [aetherasystemscore/NCD-Bond_Screener](https://github.com/aetherasystemscore/NCD-Bond_Screener) | [Launch Streamlit App](https://ncd-bondscreener-bgftfvgej8y5bsng8id54t.streamlit.app/) |

---

## ⏰ External Cron Automation

- **Cron-Job.org Console:** [https://cron-job.org/en/](https://cron-job.org/en/)
  - Used to schedule periodic HTTP `GET` keep-alive pings (`?ping=true` and `/_stcore/health`) so Streamlit Community Cloud containers do not enter hibernation (`Zzz`).

---

## 🚀 Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
