import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="VAST × NVIDIA · AI Data Factory for Cloud",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Password Gate ──────────────────────────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("""
    <style>
    .auth-container {
        max-width: 420px; margin: 15vh auto; padding: 48px;
        background: #0a0e1f; border: 1px solid #1a2540;
        border-radius: 20px; text-align: center;
    }
    .auth-title { font-size: 28px; font-weight: 900; color: #e8e8f0; margin-bottom: 8px; }
    .auth-sub { font-size: 15px; color: #5878a8; margin-bottom: 32px; }
    </style>
    <div class="auth-container">
      <div style="font-size:36px;margin-bottom:16px;">⚡</div>
      <div class="auth-title">VAST AI Factory</div>
      <div class="auth-sub">Enter your access code to continue</div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        pwd = st.text_input("", placeholder="Access code", type="password", label_visibility="collapsed")
        if st.button("Enter →", use_container_width=True, type="primary"):
            if pwd == "vastaios":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect access code.")
    st.stop()

# ── Page state ────────────────────────────────────────────────────────────────
if "show_ncp" not in st.session_state:
    st.session_state.show_ncp = False




# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #05080f;
    color: #e8e8f0;
}
.main { background-color: #05080f; }
.block-container { padding: 2rem 3rem 2rem 3rem !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
header { display: none !important; }
footer { display: none !important; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #05080f; }
::-webkit-scrollbar-thumb { background: #1a3060; border-radius: 3px; }

.nav-bar {
    position: sticky; top: 0; z-index: 999;
    background: rgba(10,10,15,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid #1e1e2e;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 48px; height: 64px;
}
.nav-logos { display: flex; align-items: center; gap: 12px; }
.nav-brand {
    font-size: 18px; font-weight: 800; letter-spacing: -0.5px;
    background: linear-gradient(90deg, #ffffff, #00c2e0);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.nav-divider { color: #3a3a5a; font-size: 20px; }
.nav-partner { font-size: 15px; font-weight: 600; color: #f97316; }
.nav-links { display: flex; gap: 32px; }
.nav-links a {
    color: #8098b8; text-decoration: none; font-size: 13px;
    font-weight: 500; letter-spacing: 0.3px; transition: color 0.2s;
}
.nav-links a:hover { color: #e8e8f0; }
.nav-cta {
    background: linear-gradient(135deg, #0078ff, #00c2e0);
    color: white !important; border: none; padding: 9px 20px;
    border-radius: 6px; font-size: 13px; font-weight: 600;
    cursor: pointer; text-decoration: none !important;
    transition: opacity 0.2s; display: inline-block;
}
.nav-cta:hover { opacity: 0.85; }

.hero {
    min-height: 90vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center;
    padding: 80px 48px 60px;
    position: relative; overflow: hidden;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,120,255,0.18) 0%, transparent 70%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(249,115,22,0.08) 0%, transparent 60%),
                #0a0a0f;
}
.hero-mesh {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(rgba(0,120,255,0.12) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black, transparent);
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,120,255,0.12); border: 1px solid rgba(0,194,224,0.4);
    border-radius: 100px; padding: 6px 16px; margin-bottom: 32px;
    font-size: 12px; font-weight: 600; letter-spacing: 1px;
    color: #00c2e0; text-transform: uppercase;
}
.hero-badge-dot {
    width: 6px; height: 6px; border-radius: 50%; background: #a78bfa;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.4); }
}
.hero h1 {
    font-size: clamp(40px, 6vw, 76px);
    font-weight: 900; line-height: 1.05;
    letter-spacing: -2px; margin: 0 0 24px;
    background: linear-gradient(135deg, #ffffff 40%, #7ee8f8 75%, #00c2e0 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    max-width: 900px;
}
.hero-sub {
    font-size: clamp(16px, 2vw, 20px);
    color: #6080b0; max-width: 640px;
    line-height: 1.7; margin: 0 0 48px; font-weight: 400;
}
.hero-ctas { display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
.btn-primary {
    background: linear-gradient(135deg, #0078ff, #00c2e0);
    color: white !important; padding: 14px 32px; border-radius: 8px;
    font-size: 15px; font-weight: 700; text-decoration: none !important;
    display: inline-block; transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 24px rgba(0,120,255,0.4);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,120,255,0.5); }
.btn-secondary {
    background: transparent; color: #e8e8f0 !important;
    padding: 14px 32px; border-radius: 8px;
    border: 1px solid #1e3060; font-size: 15px; font-weight: 600;
    text-decoration: none !important; display: inline-block;
    transition: border-color 0.2s, background 0.2s;
}
.btn-secondary:hover { border-color: #00c2e0; background: rgba(0,120,255,0.08); }

.section { padding: 96px 48px; }
.section-alt { background: #080c18; }
.section-label {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    color: #00c2e0; text-transform: uppercase; margin-bottom: 12px;
}
.section-title {
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 800; letter-spacing: -1.5px; line-height: 1.1;
    margin: 0 0 16px;
}
.section-sub {
    font-size: 17px; color: #5878a8; max-width: 560px;
    line-height: 1.7; margin: 0 0 56px;
}

.stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 2px; background: #1a1a2e; border-radius: 16px;
    overflow: hidden; border: 1px solid #1a2540;
}
.stat-cell {
    background: #080c18; padding: 40px 32px; text-align: center;
}
.stat-number {
    font-size: clamp(36px, 4vw, 56px);
    font-weight: 900; letter-spacing: -2px; line-height: 1;
    background: linear-gradient(135deg, #ffffff, #00c2e0);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}
.stat-label { font-size: 13px; color: #3a5080; font-weight: 500; line-height: 1.5; }

.ba-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 16px; }
.ba-card { border-radius: 16px; padding: 32px; }
.ba-before { background: #080c14; border: 1px solid #1a2030; }
.ba-after  { background: #080c14; border: 1px solid #1a2a40; }
.ba-header {
    font-size: 15px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 24px;
}
.ba-before .ba-header { color: #ef4444; }
.ba-after  .ba-header { color: #10b981; }
.ba-row {
    display: flex; justify-content: space-between; align-items: flex-start;
    padding: 14px 0; border-bottom: 1px solid #1e1e2e;
}
.ba-row:last-child { border-bottom: none; }
.ba-row-label { font-size: 17px; color: #5878a8; flex: 1; }
.ba-row-val { font-size: 17px; font-weight: 700; text-align: right; max-width: 55%; }
.ba-before .ba-row-val { color: #ef4444; }
.ba-after  .ba-row-val { color: #10b981; }

.zigzag-item {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 64px; align-items: center;
    padding: 64px 0; border-bottom: 1px solid #1a1a2e;
}
.zigzag-item:last-child { border-bottom: none; }
.zigzag-item.reverse { direction: rtl; }
.zigzag-item.reverse > * { direction: ltr; }
.zigzag-text h3 {
    font-size: clamp(22px, 3vw, 32px); font-weight: 800;
    letter-spacing: -1px; margin: 0 0 16px; line-height: 1.2;
}
.zigzag-text p { font-size: 15px; color: #5878a8; line-height: 1.8; margin: 0; }
.zigzag-visual {
    background: #0a0e1f; border: 1px solid #1a2540;
    border-radius: 16px; padding: 32px;
    display: flex; flex-direction: column; gap: 12px;
}
.pill {
    background: #0d0d1e; border: 1px solid #1e3060;
    border-radius: 8px; padding: 12px 16px;
    font-size: 13px; color: #7090c0;
    display: flex; align-items: center; gap: 10px;
}
.pill-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.pill-purple .pill-dot { background: #0078ff; }
.pill-orange .pill-dot { background: #f97316; }
.pill-green  .pill-dot  { background: #10b981; }
.pill-blue   .pill-dot  { background: #3b82f6; }

.entry-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 24px; margin-top: 16px;
}
.entry-card {
    background: #0a0e1f; border: 1px solid #1a2540;
    border-radius: 16px; padding: 32px;
    display: flex; flex-direction: column;
    transition: border-color 0.3s, transform 0.3s;
}
.entry-card:hover { border-color: #00c2e0; transform: translateY(-4px); }
.entry-card.featured {
    border-color: #00c2e0;
    background: linear-gradient(160deg, #0c1030, #0a0e1f);
    box-shadow: 0 0 40px rgba(0,120,255,0.15);
}
.entry-phase {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: #00c2e0; margin-bottom: 12px;
}
.entry-card h3 { font-size: 20px; font-weight: 800; letter-spacing: -0.5px; margin: 0 0 12px; }
.entry-card p { font-size: 14px; color: #5878a8; line-height: 1.65; margin: 0 0 24px; flex: 1; }
.entry-features { list-style: none; padding: 0; margin: 0 0 28px; }
.entry-features li {
    font-size: 13px; color: #7090c0; padding: 6px 0;
    display: flex; align-items: center; gap: 8px;
}
.entry-features li::before { content: '✓'; color: #00c2e0; font-weight: 700; flex-shrink: 0; }
.entry-btn {
    display: block; text-align: center; padding: 12px;
    border-radius: 8px; font-size: 14px; font-weight: 700;
    text-decoration: none !important; transition: all 0.2s; margin-top: auto;
}
.entry-btn-primary {
    background: linear-gradient(135deg, #0078ff, #00c2e0);
    color: white !important; box-shadow: 0 4px 16px rgba(0,120,255,0.35);
}
.entry-btn-secondary {
    background: transparent; color: #e8e8f0 !important;
    border: 1px solid #1e3060;
}
.entry-btn:hover { opacity: 0.85; transform: translateY(-1px); }

.uc-tag {
    display: inline-block; font-size: 14px; font-weight: 600;
    letter-spacing: 0.5px; padding: 3px 10px; border-radius: 100px;
    margin-bottom: 8px; margin-right: 6px;
}
.tag-mistral { background: rgba(249,115,22,0.12); color: #f97316; }
.tag-vast    { background: rgba(0,120,255,0.10); color: #00c2e0; }

.footer {
    border-top: 1px solid #1a1a2e; padding: 40px 48px;
    display: flex; align-items: center; justify-content: space-between;
}
.footer-brand {
    font-size: 15px; font-weight: 800;
    background: linear-gradient(90deg, #ffffff, #00c2e0);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

div[data-testid="stTabs"] button { color: #5878a8 !important; font-size: 15px !important; font-weight: 500 !important; padding: 10px 18px !important; }
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #00c2e0 !important; border-bottom-color: #00c2e0 !important; font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

# ── NAV ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
  <div class="nav-logos">
    <span class="nav-brand">VAST AIOS</span>
  </div>
  <div class="nav-links">
    <a href="#solutions">Solutions</a>
    <a href="#results">Results</a>
    <a href="#savings">Cost &amp; Time</a>
    <a href="#why">Why Now</a>
    <a href="#entry">Get Started</a>
  </div>
  <a href="#entry" class="nav-cta">Choose Your Entry Point →</a>
</div>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-mesh"></div>
  <div class="hero-badge">
    <span class="hero-badge-dot"></span>
    VAST AI Factory · Public &amp; Private Cloud
  </div>
  <h1>VAST AI Factory for<br>Hybrid Cloud</h1>
  <p class="hero-sub">
    As VAST consolidates AI demand across enterprise tenants, VAST provides
    the foundational Operating System for AI — scaling from 25,000 cameras today
    to 500,000+ camera deployments, with real-time agentic intelligence at every layer.
  </p>
  <div class="hero-ctas">
    <a href="#solutions" class="btn-primary">Explore Solutions</a>
    <a href="?ncp=1" class="btn-secondary" target="_self">Why NCPs Choose VAST →</a>
    <a href="#entry" class="btn-secondary">Choose Your Entry Point</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1: SOLUTIONS ──────────────────────────────────────────────────────
st.markdown('<div id="solutions"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Solutions &amp; Use Cases</div>
  <div class="section-title">VAST Foundation Stack<br>for NVIDIA Blueprints.</div>
  <div class="section-sub">
    Production-ready, open-source E2E pipelines that demonstrate the full power of VAST AI OS —
    from video intelligence to genomics to enterprise RAG and fraud detection.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="font-size:14px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;padding:0 0 8px 0;">
  VAST Foundation Stack for NVIDIA Blueprints
</div>
""", unsafe_allow_html=True)
tab1, tab2, tab_genomics, tab_fraud = st.tabs([
    "🎥  Video Search & Summarization",
    "📄  Research Assistant",
    "🧬  Genomic RAG Engine",
    "🛡️  Transaction Fraud Detection",
])

st.markdown("""
<div style="padding:8px 0 0 0;">
  <div style="font-size:16px;font-weight:800;color:#e8e8f0;margin-bottom:4px;">Other AI Pipelines</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:#00b4d8;text-transform:uppercase;padding:16px 0 6px 0;">
  🏙️ Smart Cities & Public Safety
</div>
""", unsafe_allow_html=True)
tab3, tab4 = st.tabs([
    "🏙️  Smart City & Public Safety",
    "🚦  Intelligent Mobility",
])

st.markdown("""
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:#00b4d8;text-transform:uppercase;padding:16px 0 6px 0;">
  🧬 Life Sciences & Healthcare
</div>
""", unsafe_allow_html=True)
tab5, tab6, tab7 = st.tabs([
    "🧬  CAR-T Intelligence",
    "🩻  Imaging Intelligence",
    "🔬  Biomedical RAG",
])

st.markdown("""
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:#00b4d8;text-transform:uppercase;padding:16px 0 6px 0;">
  🏦 Financial Services
</div>
""", unsafe_allow_html=True)
tab8, tab9, tab10, tab11 = st.tabs([
    "📄  Document RAG",
    "🏦  Fraud Detection",
    "🔐  Data Classification",
    "📊  Observability",
])

st.markdown("""
<div style="font-size:12px;font-weight:700;letter-spacing:2px;color:#00b4d8;text-transform:uppercase;padding:16px 0 6px 0;">
  ⚙️ Industrial & Defense
</div>
""", unsafe_allow_html=True)
tab12, tab13, tab14, tab15, tab16 = st.tabs([
    "📺  Broadcast & Media",
    "🤖  Physical AI & Robotics",
    "🛡️  Defense & ISR",
    "⚡  Energy & Seismic",
    "🌐  Network Telemetry",
])

with tab1:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST AIOS</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA Cosmos Reason 2</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 4px;color:#e8e8f0;">Public Safety &amp; Video Search Summarization</h3>
      <p style="font-size:17px;color:#5878a8;line-height:1.7;margin:0 0 8px;max-width:800px;">The only platform capable of ingesting 500,000 simultaneous camera streams, reasoning over trillions of video vectors in real-time, and autonomously dispatching first responders — all without a single external database or message broker.</p>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST Wins — 5 Unmatched USPs</div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🏗️ DASE: The Only Architecture That Doesn't Break at Scale</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Legacy systems hit critical bottlenecks at 20,000–30,000 cameras because centralized metadata servers become hotspots. VAST's Disaggregated Shared-Everything (DASE) architecture separates compute logic from storage media over an NVMe fabric — every node accesses a global, lockless metadata pool. Result: linear scaling to 500K cameras with <strong style="color:#e8e8f0;">zero degradation</strong>.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🧬 Trillions of Vectors, One Namespace, Zero Fragmentation</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">500K cameras × 10s chunks × 30 days = <strong style="color:#e8e8f0;">259 billion vectors minimum</strong>. Competing vector DBs crash at this scale. VAST VectorDB is engineered for stability at exabyte scale — vectors stored as a column alongside timestamps, GPS, camera IDs, and ACLs in one unified table. Hybrid semantic + metadata search in a single query.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🤖 Cosmos Reason 2: From Detection to Deliberate Reasoning</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Traditional VMS vendors do object detection — they can count cars, not reason about them. NVIDIA Cosmos Reason 2 uses Chain-of-Thought inference to answer <em style="color:#00c2e0;">why</em> something is happening: distinguishing a stalled vehicle from a stopped one, differentiating normal crowd behaviour from a public safety emergency, adapting to scenarios never explicitly programmed.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔁 Re-Process Any Historical Video Instantly</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">New person of interest? New investigation angle? Legacy archives require slow cold-storage rehydration — hours or days of delay. VAST's all-flash platform means new AI agents re-scan petabytes of historical footage at NVMe speeds instantly. The integrated VastDB lets you query enriched metadata to pinpoint only the relevant clips before re-processing.</div>
          </div>

          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🛡️ Non-Disruptive AI-ification of Existing Infrastructure</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST's clients have existing CCTV command centers worth <strong style="color:#e8e8f0;">hundreds of millions of dollars</strong>. VAST doesn't require ripping them out. Clients simply write output data to the VAST object store — landing data on VAST seamlessly adds AI capabilities to legacy workflows without disrupting current operations.</div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1e3060;border-radius:10px;padding:18px 20px;">
          <div style="font-size:14px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:14px;">Agentic Capabilities</div>
          <div style="font-size:15px;color:#6080b0;line-height:2.3;">
            ✓ &nbsp;Real-time situational awareness — 500K+ feeds simultaneously<br>
            ✓ &nbsp;NL video search: <em>"Crowd density anomaly near Masjid al-Haram"</em><br>
            ✓ &nbsp;Automatic License Plate Recognition (ALPR) at city scale<br>
            ✓ &nbsp;Crowd &amp; behavioural analysis — large-scale, stadiums, transit hubs<br>
            ✓ &nbsp;Digital forensics: faces, plates, objects across disparate networks<br>
            ✓ &nbsp;SAR drone &amp; aerial footage ingestion and analysis<br>
            ✓ &nbsp;GSM signal + geospatial telemetry vector fusion<br>
            ✓ &nbsp;Deepfake &amp; fraud detection via VAST PolicyEngine
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">VSS Pipeline — Smart Cities Blueprint</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Stage 1 · Ingest</strong><br><span style="font-size:14px;color:#7090c0;">H.264 / 4K CCTV streams from VMS land in VAST S3 DataStore. 500K concurrent feeds, zero metadata hotspots via DASE architecture.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 2 · Intelligent Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Built-in Kafka-compatible event broker fires at 1.4M events/sec per node. Object &amp; motion detection initiates VLM — GPU only processes high-priority frames, low-value data filtered out.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 3 · Chunk &amp; Infer</strong><br><span style="font-size:14px;color:#7090c0;">NVIDIA microservices extract 10-second clips, downsample, and pass to Cosmos Reason 2 VLM with dynamically customized prompts (surveillance, safety, traffic). CoT reasoning generates rich scene descriptions.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 4 · Unified Store</strong><br><span style="font-size:14px;color:#7090c0;">Scene embeddings stored as a column in VastDB alongside GPS coordinates, timestamps, camera ID, ACLs, and sensor readings. No separate vector DB. Hybrid semantic + metadata search in one query.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Stage 5 · NL Search &amp; Vector Fusion</strong><br><span style="font-size:14px;color:#7090c0;">Operators search trillions of vectors in natural language. Multi-modal fusion: video vectors + GSM signals + geospatial telemetry = comprehensive real-time situational awareness dashboard.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 6 · Agentic Action</strong><br><span style="font-size:14px;color:#7090c0;">Incident detected → Accident Agent or Violence Agent fires → ServiceNow log + incident report + CAD dispatch with GPS coordinates. All autonomous, sub-second.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 7 · Re-process &amp; Investigate</strong><br><span style="font-size:14px;color:#7090c0;">New investigation? New AI agent re-scans historical video archive at NVMe speeds. VastDB metadata query pinpoints relevant clips — no cold storage rehydration, no delays.</span></div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1a2a1a;border-radius:10px;padding:16px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1px;color:#3a5080;text-transform:uppercase;margin-bottom:10px;">Open Source Blueprint</div>
          <div style="font-size:14px;color:#5878a8;line-height:1.6;">Full VSS ingest pipeline + secure retrieval frontend hosted on <a href="https://github.com/vast-data/cosmos-labs" target="_blank" style="color:#00c2e0;">Cosmos Labs GitHub</a>. Fork it, modify the business logic, swap models — deploy in under one working day.</div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST AIOS</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA DASE</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 4px;color:#e8e8f0;">Intelligent Mobility &amp; Traffic Flow</h3>
      <p style="font-size:17px;color:#5878a8;line-height:1.7;margin:0 0 8px;max-width:800px;">VAST serves as the high-performance neural center for AI Cloud smart cities — moving from fixed-timer traffic lights and retrospective monitoring to proactive, real-time orchestration across every intersection, highway, and transit corridor in the cloud.</p>
    </div>
    """, unsafe_allow_html=True)

    col_c, col_d = st.columns(2, gap="large")

    with col_c:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST Wins — 5 Unmatched USPs</div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚡ Sub-Millisecond Signal Control Across an Entire City Grid</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Traditional traffic systems use fixed timers. VAST's DASE architecture provides the sub-millisecond latency required to process live intersection video, compute optimal signal timing, and push updates across an entire city grid <strong style="color:#e8e8f0;">simultaneously</strong> — eliminating ghost traffic jams caused by stale signal data.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🚌 True Multi-Modal Reasoning, Not Just Object Detection</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Most traffic AI classifies vehicles by type. VAST + Cosmos Reason 2 understands <em style="color:#00c2e0;">intent and context</em> — distinguishing a delivery truck making a legal stop from one blocking a lane, or a cyclist moving safely vs. one in danger. This contextual understanding enables automated speed limit changes, lane priority shifts, and emergency routing that legacy systems cannot perform.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🏙️ Digital Twins Fed by a Global Namespace</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">City planners need to simulate bridge closures, large-scale crowd flows, and major events before they happen. VAST's Global Namespace means petabytes of historical traffic telemetry from thousands of edge sensors appear as a single local drive — feeding AI simulation factories with the data density required for high-fidelity digital twins.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🚑 Automatic Green Waves with Cross-Department Data Sharing</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">When an incident is detected, VAST DataSpace makes the data instantly available to Traffic, Fire, and Police simultaneously — without copying or moving it. Green Wave sequences are cleared for emergency vehicles in real-time. No inter-departmental API calls, no delays, no data silos between agencies.</div>
          </div>

          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">📸 Nationwide Speed Fine Detection at Zero Marginal Cost</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">High-resolution traffic cameras record directly to VAST DataStore. Localized Inference Agents process frames for speed anomalies and log events into VastDB. Action Agents automatically issue citations via integrated APIs — all without a human in the loop. Scales from one city to the entire cloud with no additional infrastructure.</div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1e3060;border-radius:10px;padding:18px 20px;">
          <div style="font-size:14px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:14px;">Mobility Use Cases</div>
          <div style="font-size:15px;color:#6080b0;line-height:2.3;">
            ✓ &nbsp;AI-driven adaptive signal control — sub-millisecond updates<br>
            ✓ &nbsp;Multi-modal object classification at intersection level<br>
            ✓ &nbsp;Digital twin simulation on petabytes of traffic telemetry<br>
            ✓ &nbsp;Instant cross-department data sharing — Traffic, Fire, Police<br>
            ✓ &nbsp;Emergency Green Wave — automatic corridor clearance<br>
            ✓ &nbsp;Nationwide automated speed fine detection<br>
            ✓ &nbsp;Predictive congestion modelling via historical similarity search
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_d:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Intelligent Mobility Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Stage 1 · Multi-Modal Ingest</strong><br><span style="font-size:14px;color:#7090c0;">4K video + LiDAR + IoT sensor streams land directly in VAST DataStore. NFS/S3/NVMe simultaneously — no preprocessing bottlenecks, no gateway overhead.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 2 · Edge Filtering</strong><br><span style="font-size:14px;color:#7090c0;">Lightweight object &amp; motion detection at the edge filters low-value frames. Only high-priority data — accidents, anomalies, violations — forwarded to GPU inference clusters.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 3 · Contextual Reasoning</strong><br><span style="font-size:14px;color:#7090c0;">Cosmos Reason 2 classifies vehicle types, detects anomalies, understands intent. Generates structured scene context: vehicle count, density, incident type, severity score.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 4 · VastDB Unified Store</strong><br><span style="font-size:14px;color:#7090c0;">Vectors + GPS + timestamps + weather + vehicle types stored as columns in VastDB. Similarity search: "find all intersections with cyclist incidents in rain, 2022–2024."</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Stage 5 · Real-Time Orchestration</strong><br><span style="font-size:14px;color:#7090c0;">Signal timing updated city-wide in sub-milliseconds. Green Wave cleared for emergency vehicles. Digital signage updated for speed limits and lane changes. All simultaneous.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 6 · Agentic Citation &amp; Dispatch</strong><br><span style="font-size:14px;color:#7090c0;">Speed violations → Action Agent issues citation via API. Accidents → first responder CAD dispatch with GPS. Cross-department DataSpace shares incident data to Traffic, Fire, Police instantly.</span></div>
          </div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div style="margin:24px 0 8px;">
      <div style="font-size:13px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">🎬 VSS Live Demo</div>
      <div style="background:#0a0e1f;border:2px dashed #2a2a4a;border-radius:12px;padding:40px;text-align:center;">
        <div style="font-size:32px;margin-bottom:12px;">▶</div>
        <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:8px;">Video Search Summarization Demo</div>
        <div style="font-size:14px;color:#3a5080;">Vimeo embed coming soon — paste your Vimeo video URL here</div>
        <div style="margin-top:16px;font-size:12px;color:#3a3a5a;font-family:monospace;">st.video("https://vimeo.com/YOUR_VIDEO_ID")</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


with tab2:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST Sync Engine</span>
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-vast">VAST AgentEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 4px;color:#e8e8f0;">Document RAG</h3>
      <p style="font-size:17px;color:#5878a8;line-height:1.7;margin:0 0 8px;max-width:800px;">Deploy secure, enterprise-grade AI assistants across all enterprise tenants — each strictly isolated, each respecting its own access control policies — without a single separate vector database, ETL pipeline, or Kafka cluster.</p>
    </div>
    """, unsafe_allow_html=True)

    col_e, col_f = st.columns(2, gap="large")

    with col_e:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST Wins — 5 Unmatched USPs</div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔒 Hard Ministry Isolation, Not Soft Permissions</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Most RAG platforms enforce document-level permissions in software — a misconfiguration leaks classified data between tenants. VAST enforces isolation at the <strong style="color:#e8e8f0;">storage fabric level</strong>: tenant-specific VIP pools, VLANs, and encryption keys mean Ministry of Finance data is physically air-gapped from Ministry of Health data on the same hardware.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">⚡ Zero-ETL: From SharePoint to Searchable in Minutes</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Traditional RAG stacks require Airflow pipelines, S3 connectors, and batch jobs to move documents from Confluence, SharePoint, or Google Drive. VAST's native Sync Engine eliminates all of this — documents are pulled automatically, ACLs fetched concurrently, and the moment data lands it triggers the embedding pipeline. <strong style="color:#e8e8f0;">Zero manual orchestration.</strong></div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🧬 Vectors + Metadata in One Table, One Query</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">AWS RAG stacks require stitching together RDS for metadata and a separate vector DB (Milvus, Pinecone) for semantic search — two round trips per query, two systems to maintain, two failure points. VAST stores vectors as a column in VastDB alongside ACLs and metadata. A single hybrid query returns semantically relevant, permission-filtered results.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">📦 Serverless Scale-to-Zero, No EKS Management</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Managing EKS node groups to process document queues is expensive and complex. VAST DataEngine runs containerized embedding functions natively on the storage cluster. Document backlog? Auto-scales up. Idle? Scales to <strong style="color:#e8e8f0;">2GB RAM and 2 cores</strong>. VAST pays only for what runs — no over-provisioned compute sitting idle.</div>
          </div>

          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🤖 Agent-as-a-Service via AgentEngine</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST hosts conversational RAG agents directly on the platform via AgentEngine — managing session context natively in VastDB. VAST can offer autonomous AI copilots, document summarizers, and compliance agents to tenant customers as a managed service. No external LLM orchestration frameworks required.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_f:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Document RAG Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Stage 1 · Sync Engine Ingestion</strong><br><span style="font-size:14px;color:#7090c0;">VAST Sync Engine automatically pulls documents from Confluence, Google Drive, SharePoint into VAST S3. Concurrent ACL fetch — permissions stored alongside data at ingest time.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 2 · Event Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Document landing in S3 bucket immediately triggers built-in Kafka-compatible event broker. No external Kafka cluster required — eliminates dedicated broker infrastructure entirely.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 3 · DataEngine Processing</strong><br><span style="font-size:14px;color:#7090c0;">Serverless lambda-like functions on the DataEngine chunk the document and prepare text. Auto-scales with backlog; idles at 2GB RAM when no documents to process.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 4 · NVIDIA Embedding</strong><br><span style="font-size:14px;color:#7090c0;">NVIDIA NIM embedding model generates vector representations. Model endpoint swappable without redesign — upgrade to latest NVIDIA or custom model by redirecting endpoint.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 5 · VastDB Unified Store</strong><br><span style="font-size:14px;color:#7090c0;">Vectors + ACLs + metadata written as columns in VastDB. Single table, single query engine. No RDS + Milvus stitching. Hard tenant isolation enforced at storage fabric level.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Stage 6 · AgentEngine RAG</strong><br><span style="font-size:14px;color:#7090c0;">Conversational agent queries by user identity — hybrid semantic + ACL-filtered search in one native query. Session context managed in VastDB. Users only see what they're authorized to view.</span></div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1e3060;border-radius:10px;padding:18px 20px;">
          <div style="font-size:14px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:14px;">Key Capabilities</div>
          <div style="font-size:15px;color:#6080b0;line-height:2.3;">
            ✓ &nbsp;Hard isolation between enterprise tenants<br>
            ✓ &nbsp;Zero-ETL sync from enterprise content sources<br>
            ✓ &nbsp;Scale-to-zero serverless compute — 2GB RAM idle<br>
            ✓ &nbsp;Unified vector + metadata in a single VastDB query<br>
            ✓ &nbsp;AgentEngine — Agent-as-a-Service for tenant customers<br>
            ✓ &nbsp;Open-source blueprint on <a href="https://github.com/vast-data/cosmos-labs" target="_blank" style="color:#00c2e0;">Cosmos Labs GitHub</a>
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab11:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST Event Broker</span>
      <span class="uc-tag tag-vast">VAST InsightEngine</span>
      <span class="uc-tag tag-vast">VAST AgentEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 4px;color:#e8e8f0;">Observability at cloud Scale</h3>
      <p style="font-size:17px;color:#5878a8;line-height:1.7;margin:0 0 8px;max-width:800px;">Traditional observability platforms like Splunk and Datadog charge $1–$4/GB ingestion — economically untenable at 500K camera scale. VAST runs the entire observability pipeline on-platform at flat storage economics, with AI-native diagnostics and closed-loop automated remediation.</p>
    </div>
    """, unsafe_allow_html=True)

    col_g, col_h = st.columns(2, gap="large")

    with col_g:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST Wins — 5 Unmatched USPs</div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">💰 Flat Economics: Cents/GB vs. $1–$4/GB</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">At VAST's scale — 500K cameras, 26 tenants, thousands of edge nodes — Splunk/Datadog per-GB pricing becomes <strong style="color:#e8e8f0;">tens of millions of dollars annually</strong>. VAST runs the observability pipeline directly on-platform. No per-GB ingestion fees. No hot/warm/cold tiering. No retention cliffs. Full resolution data retained for months to years.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🤖 AI-First Diagnostics: Natural Language, Not Dashboards</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Engineers describe symptoms in natural language — "latency spikes on Camera Zone 7 after 11pm" — and the AI autonomously investigates: querying error rates, following distributed traces, checking infrastructure health, cross-referencing operational runbooks. Mean time to diagnosis drops from <strong style="color:#e8e8f0;">hours to minutes</strong>. Senior SRE expertise democratized to every engineer.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔗 Unified Signal Correlation in One SQL Query</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Traditional tools require manual pivoting between Splunk (logs), Datadog (metrics), and Jaeger (traces) — three separate systems, three interfaces, three data silos. VAST stores all three signals in one VastDB table, queryable via a single Trino SQL engine. An AI agent joins a latency spike in traces with a CPU anomaly in metrics and an error in logs <strong style="color:#e8e8f0;">in one query</strong>.</div>
          </div>

          <div style="margin-bottom:20px;padding-bottom:20px;border-bottom:1px solid #1a1a2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">🔄 Closed-Loop: Detect, Diagnose, and Remediate Automatically</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Statistical anomaly detection learns per-service baselines and fires alerts on deviations — not static thresholds that generate false alarms. Each anomaly automatically triggers an AI investigation. Engineers arrive at the alert with the root cause already identified. <strong style="color:#e8e8f0;">Low-risk actions auto-execute</strong>; medium-risk require one-click approval; high-risk create tickets with full diagnostic context.</div>
          </div>

          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">♾️ Infinite Retention: Last Year's Data at Today's Latency</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST's disaggregated architecture separates compute from storage — last year's telemetry is queryable with the same sub-second latency as today's data. Historical baselines enable trend analysis, regression investigation, and compliance auditing across the entire cloud's infrastructure without rehydration delays or additional cost.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_h:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Observability Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 1 · Collection</strong><br><span style="font-size:14px;color:#7090c0;">OpenTelemetry collectors gather traces, metrics, and logs from 500K cameras, edge nodes, AI pipelines, and tenant services. Open standard — no proprietary agents.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 2 · Event Broker Streaming</strong><br><span style="font-size:14px;color:#7090c0;">Built-in Kafka-compatible broker streams telemetry at high throughput from hundreds of thousands of sources simultaneously — no dedicated Kafka cluster required.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 3 · VastDB Storage</strong><br><span style="font-size:14px;color:#7090c0;">Petabytes of full-resolution telemetry stored with transactional integrity + trillion-scale vector indexing. All three signals (traces, metrics, logs) in one table. Flat economics — no tiering.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Stage 4 · Anomaly Detection</strong><br><span style="font-size:14px;color:#7090c0;">Statistical models learn per-service baselines. Deviations fire alerts — not static thresholds. Each alert automatically triggers an AI investigation via InsightEngine.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;margin-bottom:6px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Stage 5 · AI Root Cause Analysis</strong><br><span style="font-size:14px;color:#7090c0;">LLM queries raw telemetry via SQL — joins latency spike in traces + CPU anomaly in metrics + error in logs in one query. Cites relevant runbooks. Root cause identified before engineer opens the alert.</span></div>
          </div>
          <div style="padding-left:16px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:6px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Stage 6 · Closed-Loop Remediation</strong><br><span style="font-size:14px;color:#7090c0;">Low-risk: auto-execute (restart pod, clear cache). Medium-risk: one-click approval. High-risk: ticket with full context. Full audit trail logged for cloud-wide compliance reporting.</span></div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1a2a1a;border-radius:10px;padding:16px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1px;color:#3a5080;text-transform:uppercase;margin-bottom:12px;">Cost Comparison</div>
          <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:6px;font-size:13px;">
            <div style="color:#5878a8;font-weight:700;padding:6px 0;border-bottom:1px solid #1e1e2e;"></div>
            <div style="color:#ef4444;font-weight:700;padding:6px 4px;border-bottom:1px solid #1e1e2e;">Splunk/Datadog</div>
            <div style="color:#10b981;font-weight:700;padding:6px 4px;border-bottom:1px solid #1e1e2e;">VAST</div>
            <div style="color:#5878a8;padding:5px 0;font-size:12px;">Pricing</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">$1–4/GB ingestion</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">Cents/GB flat</div>
            <div style="color:#5878a8;padding:5px 0;font-size:12px;">Retention</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">15–30 days max</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">Years, full res</div>
            <div style="color:#5878a8;padding:5px 0;font-size:12px;">AI</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">Proprietary, limited</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">LLMs via SQL</div>
            <div style="color:#5878a8;padding:5px 0;font-size:12px;">Signals</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">3 separate tools</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">1 SQL engine</div>
            <div style="color:#5878a8;padding:5px 0;font-size:12px;">Lock-in</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">Proprietary agents</div><div style="color:#7090c0;padding:5px 4px;font-size:12px;">OpenTelemetry</div>
          </div>
        </div>
        """, unsafe_allow_html=True)


with tab5:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA NIM</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">CAR-T Intelligence Agent</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:800px;margin:0 0 16px;">
        Deploy a fully agentic CAR-T cell therapy pipeline on VAST — from raw clinical trial ingestion to real-time treatment outcome reasoning. 
        No proprietary black boxes. Open-source, swap any LLM, runs natively on VAST DataEngine.
        <a href="https://hcls-ai-factory.org/cart-intelligence-agent/" target="_blank" style="color:#00c2e0;margin-left:8px;">→ Live Blueprint</a>
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_c1, col_c2 = st.columns(2, gap="large")
    with col_c1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">USPs — Why VAST for CAR-T</div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Unified Genomic + Clinical Data Lake</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Raw genome files, patient records, and clinical trial PDFs unified in VastDB — no separate S3 + Aurora + Milvus stack. Hybrid similarity + metadata search across patient cohorts in a single query.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. PHI Auto-Masking on Write</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine serverless functions mask Patient Health Information the moment data enters the platform — before any model sees it. HIPAA compliance without multi-step ETL pipelines.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Swap Endpoints — No Bedrock Lock-in</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">The CAR-T blueprint is fully open-source. Replace any default NVIDIA model with your own fine-tuned LLM endpoint — drop in the latest biomedical model without redesigning infrastructure.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Scale-to-Zero Serverless Compute</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine auto-scales processing functions linearly when trial data backlogs build up — scales to zero when idle. No EKS node groups to manage.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Outcome Reasoning at Petabyte Scale</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Agent reasons across patient genomes, treatment protocols, and adverse event records simultaneously — enabling automated drug discovery and treatment pathway optimization across entire patient populations.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">CAR-T Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">Genome sequences, EHRs, clinical trial PDFs → VAST S3 via Sync Engine</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">PHI Masking</strong><br><span style="font-size:14px;color:#7090c0;">DataEngine triggers instantly — PHI stripped before any model access</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Chunk + Embed</strong><br><span style="font-size:14px;color:#7090c0;">Biomedical texts chunked → embedding model generates vectors stored in VastDB alongside patient metadata</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Hybrid Search</strong><br><span style="font-size:14px;color:#7090c0;">Single VastDB query: genome vectors + demographics + regulatory flags + treatment history</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">CAR-T Agent Action</strong><br><span style="font-size:14px;color:#7090c0;">Agent surfaces treatment pathway recommendations, adverse event alerts, trial eligibility scoring</span></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab6:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA VLMs</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Imaging Intelligence Agent</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:800px;margin:0 0 16px;">
        Petabyte-scale medical imaging analysis with real-time clinical decision support. Deploy Vision-Language Models locally at hospital edge nodes — sub-30ms latency, no round-trip to the cloud.
        <a href="https://hcls-ai-factory.org/imaging-intelligence-agent/" target="_blank" style="color:#00c2e0;margin-left:8px;">→ Live Blueprint</a>
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_i1, col_i2 = st.columns(2, gap="large")
    with col_i1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">USPs — Why VAST for Medical Imaging</div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Edge-to-Core — Sub-30ms at Hospital Level</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">4K surgical imaging and live patient monitoring cannot tolerate latency back to a central cloud region. VAST DataSpace bridges hospital edge nodes with the core via a Global Namespace — VLMs run locally for real-time clinical decision support.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Massive Bandwidth for Multi-Modal Imaging</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Legacy storage maxes out at one or two 4K feeds. VAST provides the immense bus capacity to run multiple simultaneous 4K and 8K imaging streams — critical for operating theatres, radiology departments, and multi-site hospital networks.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. DICOM + Vector Hybrid Search</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">DICOM metadata, imaging vectors, and patient records stored as columns in VastDB. Radiologists search across petabytes of historical scans using natural language — "show all chest CTs with nodules larger than 8mm in patients over 60."</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Real-Time Clinical Decision Support</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VLM analyzes live surgical video and imaging streams — detecting anomalies, flagging critical findings, and surfacing relevant historical cases in real time alongside the procedure.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Open-Source — Swap Any VLM Endpoint</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">The imaging blueprint is fully open-source. Replace the default NVIDIA VLM with any fine-tuned medical imaging model — deploy Pixtral, BioViL, or your own endpoint without infrastructure changes.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_i2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Imaging Intelligence Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">DICOM scans, surgical video, MRI/CT feeds → VAST DataStore at edge hospital node</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Edge VLM Inference</strong><br><span style="font-size:14px;color:#7090c0;">Vision-Language Model analyzes imaging locally — sub-30ms, no cloud round-trip</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Store + Index</strong><br><span style="font-size:14px;color:#7090c0;">Scene embeddings + DICOM metadata + ACLs written as VastDB columns — instantly searchable</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">NL Search</strong><br><span style="font-size:14px;color:#7090c0;">Radiologist queries in plain language across petabytes of historical scans in seconds</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Clinical Alert</strong><br><span style="font-size:14px;color:#7090c0;">Agent flags critical findings, surfaces relevant historical cases, triggers clinical workflow</span></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab7:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST Sync Engine</span>
      <span class="uc-tag tag-vast">VAST AgentEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Biomedical Knowledge & Evidence Intelligence</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:800px;margin:0 0 16px;">
        Live RAG over petabytes of oncology documents, clinical guidelines, research literature, and patient records — with strict ACL enforcement and open-source model flexibility.
        <a href="https://hcls-ai-factory.org/" target="_blank" style="color:#00c2e0;margin-left:8px;">→ HCLS AI Factory</a>
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_b1, col_b2 = st.columns(2, gap="large")
    with col_b1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">USPs — Biomedical RAG on VAST</div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">6. Live RAG on Scientific Literature + EHRs</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Ingest PubMed, clinical guidelines, oncology trial data, and patient EHRs into one unified VastDB. Clinicians and researchers query across all sources simultaneously — automated drug discovery, disease diagnosis from patient genomes, evidence synthesis.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">7. ACL-Enforced — Clinician-Level Access Control</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">ACLs from hospital systems fetched at ingest and stored natively in VastDB. When a doctor queries the agent, it only surfaces records they are explicitly authorized to view — zero additional IAM engineering.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">8. Genome + Clinical Hybrid Search</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Patient genome embeddings, demographic metadata, and regulatory flags stored as columns in one VastDB table. Hybrid queries join genomic similarity search with structured patient filters — enabling population-scale disease diagnosis.</div>
          </div>
          <div style="margin-bottom:18px;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">9. Event-Driven — New Literature Auto-Ingested</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Sync Engine continuously pulls new publications from configured sources. The moment a paper lands in S3, DataEngine triggers chunking and embedding automatically — the knowledge base stays current without manual intervention.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">10. Hosted Agents — No External Orchestration</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">RAG agents hosted directly on VAST AgentEngine, managing conversation sessions and context natively in VastDB. Deploy a Biomedical Evidence agent, a Drug Discovery agent, or a Clinical Trial Matching agent — all on the same platform.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_b2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Biomedical RAG Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Sync</strong><br><span style="font-size:14px;color:#7090c0;">PubMed, clinical guidelines, EHRs, trial data → VAST S3 via Sync Engine (continuous)</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">PHI Mask + ACL Fetch</strong><br><span style="font-size:14px;color:#7090c0;">Patient data masked on write — ACLs stored alongside records in VastDB</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Chunk + Embed</strong><br><span style="font-size:14px;color:#7090c0;">Biomedical text → embedding model → vectors stored as VastDB columns alongside genome metadata</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Hybrid Search</strong><br><span style="font-size:14px;color:#7090c0;">Clinician query → semantic + metadata filter in one VastDB query → ACL-enforced results</span></div>
          </div>
          <div style="padding-left:14px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:12px;align-items:flex-start;">
            <div style="width:8px;height:8px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Agent Response</strong><br><span style="font-size:14px;color:#7090c0;">RAG agent answers with cited evidence — drug discovery insights, trial eligibility, diagnosis support</span></div>
          </div>
        </div>
        """, unsafe_allow_html=True)




    st.markdown("""
    <div style="margin:24px 0 8px;">
      <div style="font-size:13px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">🎬 Document RAG Live Demo</div>
      <div style="background:#0a0e1f;border:2px dashed #2a2a4a;border-radius:12px;padding:40px;text-align:center;">
        <div style="font-size:32px;margin-bottom:12px;">▶</div>
        <div style="font-size:18px;font-weight:700;color:#e8e8f0;margin-bottom:8px;">Document RAG / Research Assistant Demo</div>
        <div style="font-size:14px;color:#3a5080;">Vimeo embed coming soon — paste your Vimeo video URL here</div>
        <div style="margin-top:16px;font-size:12px;color:#3a3a5a;font-family:monospace;">st.video("https://vimeo.com/YOUR_VIDEO_ID")</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


with tab_genomics:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,194,224,0.12);color:#00c2e0;">NVIDIA NIM</span>
      <span class="uc-tag tag-vast">VAST VectorDB</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Genomic RAG Engine</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">
        DNA Sequencing to Clinical Insights. Transform raw FASTQ files into searchable clinical knowledge — 
        variant calling, ClinVar enrichment, AI explanations, and semantic search, all automated on VAST AI OS.
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_g1, col_g2 = st.columns(2, gap="large")
    with col_g1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #1a2a50;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Genomics</div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Petabyte-Scale Genomic Data Lake</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Raw FASTQ files, BAM/VCF outputs, and ClinVar annotations unified in one VAST namespace. No separate object store, no data movement between preprocessing and analysis stages.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Event-Driven Variant Calling Pipeline</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">FASTQ file lands in S3 → DataEngine triggers variant calling pipeline automatically → ClinVar enrichment → LLM explanation generated. Zero manual orchestration, no Airflow pipelines.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Vector Columns for Semantic Clinical Search</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Genomic embeddings stored as columns alongside patient metadata and ACLs in VastDB. Hybrid queries combine variant similarity search with structured filters — enabling population-scale disease diagnosis.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. LLM Memoization — No Repeated Inference</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST stores LLM-generated explanations natively in VastDB. Identical variants reuse cached explanations — dramatically reducing GPU inference costs at population scale.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. HIPAA-Ready — PHI Masked on Write</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine serverless functions strip PHI the moment data enters the platform. ACLs from hospital systems stored natively alongside records — clinicians only see data they are authorized to view.</div>
          </div>
        </div>
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;margin-top:14px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:12px;">Industries</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">Healthcare</span>
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">Life Sciences</span>
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">Pharma</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_g2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Genomic RAG Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">FASTQ Upload</strong><br><span style="font-size:14px;color:#7090c0;">Raw DNA sequence files land in VAST S3 via S3 Event Triggers</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Variant Calling</strong><br><span style="font-size:14px;color:#7090c0;">DataEngine pipeline runs GATK/DeepVariant → ClinVar enrichment automated</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Embeddings</strong><br><span style="font-size:14px;color:#7090c0;">NVIDIA NIM generates genomic embeddings → stored as Vector Columns in VastDB alongside metadata</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">LLM Memoization</strong><br><span style="font-size:14px;color:#7090c0;">LLM generates clinical explanations — cached in VastDB, reused for identical variants</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Semantic Search</strong><br><span style="font-size:14px;color:#7090c0;">Clinicians query in natural language — hybrid vector + metadata search, ACL-enforced, drug discovery enabled</span></div>
          </div>
        </div>
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:12px;">Key Capabilities</div>
          <div style="font-size:14px;color:#6080b0;line-height:2.2;">
            ✓ &nbsp;FASTQ → clinical insight, fully automated<br>
            ✓ &nbsp;Variant calling + ClinVar enrichment on ingest<br>
            ✓ &nbsp;LLM memoization — reuse cached explanations<br>
            ✓ &nbsp;Vector columns native in VastDB<br>
            ✓ &nbsp;PHI masked on write — HIPAA ready
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab_fraud:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST Event Broker</span>
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-vast">VAST VectorDB</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Transaction Fraud Detection</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">
        Real-Time Anomaly Scoring. Millisecond fraud detection with built-in PII masking — 
        combines rule-based scoring with ML vector similarity to catch fraud patterns in real-time 
        across financial services, insurance, and e-commerce.
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_f1, col_f2 = st.columns(2, gap="large")
    with col_f1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #1a2a50;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Fraud Detection</div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Millisecond Event Streaming — No External Kafka</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST's built-in Kafka-compatible Event Broker ingests transaction streams at 1.4M events/sec per node. No external message broker to manage — the streaming layer is native to the storage platform.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. PII Masking Built Into the Pipeline</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine serverless functions strip and mask PII the moment transactions arrive — before any model sees the data. PCI-DSS compliant by design, not by bolt-on.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. 7-Factor Scoring + ML Vector Similarity</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Rule-based 7-factor scoring combined with ML vector similarity search in a single VastDB query — catching both known patterns and novel fraud that rules alone miss.</div>
          </div>
          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1a2540;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Unified Transaction + Vector Store</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Transaction records, fraud embeddings, and account metadata stored as columns in one VastDB table. No stitching together separate stream processors, vector DBs, and relational databases.</div>
          </div>
          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Real-Time Dashboard + Agentic Actions</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Detected fraud triggers instant downstream actions — account freeze, compliance alert, case creation — all orchestrated via DataEngine without external workflow tools.</div>
          </div>
        </div>
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;margin-top:14px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:12px;">Industries</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">Financial Services</span>
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">Insurance</span>
            <span style="background:#0c1030;border:1px solid #1e3060;border-radius:100px;padding:4px 14px;font-size:13px;color:#7090c0;">E-Commerce</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_f2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Fraud Detection Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Event Broker</strong><br><span style="font-size:14px;color:#7090c0;">Transaction stream ingested at 1.4M events/sec — no external Kafka needed</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">PII Mask</strong><br><span style="font-size:14px;color:#7090c0;">DataEngine strips PII instantly on arrival — PCI-DSS compliant before any model access</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Embed</strong><br><span style="font-size:14px;color:#7090c0;">Transaction embedding generated → stored as Vector Column in VastDB alongside account metadata</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">7-Factor Score</strong><br><span style="font-size:14px;color:#7090c0;">Rule-based scoring + ML vector similarity in single VastDB query — known + novel fraud caught</span></div>
          </div>
          <div style="padding-left:12px;color:#1a2540;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Dashboard + Action</strong><br><span style="font-size:14px;color:#7090c0;">Real-time fraud dashboard + agentic actions: account freeze, compliance alert, case creation</span></div>
          </div>
        </div>
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:12px;">Key Capabilities</div>
          <div style="font-size:14px;color:#6080b0;line-height:2.2;">
            ✓ &nbsp;1.4M events/sec native — no external Kafka<br>
            ✓ &nbsp;PII masking built into ingest pipeline<br>
            ✓ &nbsp;7-factor scoring + ML vector similarity<br>
            ✓ &nbsp;PCI-DSS compliant by architecture<br>
            ✓ &nbsp;Real-time streaming + agentic response
          </div>
        </div>
        """, unsafe_allow_html=True)



with tab3:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST VSS</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA Cosmos Reason 2</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Smart City & Public Safety</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">A major government agency scaling from 50,000 to 200,000 cameras. Replaced 58 separate Milvus vector databases with one unified VAST platform. Zero rip-and-replace of existing $100M CCTV infrastructure.</p>
    </div>
    """, unsafe_allow_html=True)
    col_s1, col_s2 = st.columns(2, gap="large")
    with col_s1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Smart City</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Eliminate 58 Milvus Databases</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Scaling semantic search previously required 58 separate Milvus vector databases — 6–8 FTEs just for patching. VAST replaces all of them with one native vector store built into the platform.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Zero Rip-and-Replace</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">The agency kept their $100M CCTV command center intact. Existing VMS systems write camera footage directly to VAST S3 — AI capabilities added on top without disrupting operations.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Serverless Pipelines on Ingest</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">The moment a video chunk lands, the native event broker triggers NVIDIA microservices — VLM inference for scene descriptions, fall detection, accident ID, and violence detection in real time.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Unified Hybrid Search</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">VastDB treats vector embeddings as a column alongside metadata — investigators query complex scenarios across 200K cameras without disjointed databases. Sub-second across the entire network.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. 600 H200 + 1,500 GB300 GPUs</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">The agency feeds massive GPU clusters for inference and embodied AI/robotics from VAST — scaling to exabyte levels. Full end-to-end pipeline deploys in under one working day.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_s2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Smart City VSS Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">CCTV/VMS footage writes to VAST S3 — no pipeline rewrite, existing systems intact</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Event Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Built-in Kafka broker fires at 1.4M events/sec per node</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">VLM Inference</strong><br><span style="font-size:14px;color:#7090c0;">NVIDIA microservices chunk video → Cosmos Reason 2 generates scene descriptions</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Store + Index</strong><br><span style="font-size:14px;color:#7090c0;">Vectors + GPS + timestamps stored as VastDB columns — hybrid NL search across 200K cameras</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Agentic Action</strong><br><span style="font-size:14px;color:#7090c0;">Fall/violence detection → ServiceNow log → first responder CAD dispatch with GPS</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab12:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST VSS</span>
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Broadcast & Media VSS</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Leading sports & media organizations. Real-time video ingestion, automated clipping, metadata enrichment, and AI-powered deep search across massive media archives.</p>
    </div>
    """, unsafe_allow_html=True)
    col_m1, col_m2 = st.columns(2, gap="large")
    with col_m1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Broadcast & Media</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Multi-4K/8K Stream Bandwidth</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Legacy storage maxes at 1–2 4K feeds. VAST provides the bus capacity to run multiple simultaneous 4K and 8K streams — meeting Netflix and Prime Video delivery specs mandated by major platforms.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Command-F for Video Archives</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Search directly within video content — find specific plays, player actions, or the brand of shoes an athlete is wearing across 20 years of footage. Enables coach film review, investigative journalism, and sponsor monetization at scale.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Own Your Stats — No Rights Fees</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Run open-source AI models locally on VAST — generate your own stats and highlights without paying third-party data provider rights fees or per-query cloud usage fees. Leading sports organizations have saved $1M–$3.5M TCO over 10 years vs. legacy storage vendors.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Automated Clip + Highlight Pipelines</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine triggers automated workflows: ingest → scene detection → clip generation → metadata tagging → publishing — hyper-specific highlight reels generated without manual intervention. Enables new monetization streams from existing archive content.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. MovieLabs 2030 Ready</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST pairs advanced infrastructure with cybersecurity and data protection — future-proofing broadcasters for evolving industry standards, rights renewals, and rigorous delivery specifications.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_m2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Broadcast VSS Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">Live broadcast feeds + archived media → VAST DataStore (multi-4K/8K simultaneous)</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Event Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Event broker fires on new content — triggers scene analysis pipeline</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">VLM Scene Analysis</strong><br><span style="font-size:14px;color:#7090c0;">VLM generates semantic descriptions + sport-specific metadata (player IDs, actions, brands)</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Vector Index</strong><br><span style="font-size:14px;color:#7090c0;">Embeddings + player IDs + timestamps stored in VastDB — search across 20 years of archive</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Monetization Action</strong><br><span style="font-size:14px;color:#7090c0;">Auto-generate highlight reel + hyper-targeted ad placement + sponsor clip packaging</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab9:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST VSS</span>
      <span class="uc-tag tag-vast">VAST Event Broker</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Bank Branch Monitoring & Fraud Detection</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Real-time cross-branch criminal detection — correlate video, transactions, and audio across hundreds of bank branches simultaneously to identify structuring fraud and serial offenders.</p>
    </div>
    """, unsafe_allow_html=True)
    col_f1, col_f2 = st.columns(2, gap="large")
    with col_f1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Fraud Detection</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Real-Time Transaction Streaming</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">High-volume transaction streams ingested via VAST's built-in Kafka-compatible Event Broker — 1.4M events/sec per node. No external Kafka cluster to manage or maintain.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Multi-Branch Criminal Search</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Search across hundreds of bank branches simultaneously — identify criminals using multiple debit cards to withdraw under the $10K reporting limit, moving between locations rapidly. Correlate video, transactions, and audio in one VastDB query.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Multimodal Fraud Detection</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Facial recognition vectors, transaction metadata, and audio analysis unified in VastDB — no stitching together separate video analytics, transaction DB, and voice tools. One hybrid query across all modalities.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Agentic Risk Workflows</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">When a fraud pattern is detected, an Action Agent automatically freezes the account, logs the incident, alerts compliance, and flags the physical branch — all without human intervention.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Hard Multi-Tenant Isolation</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Each bank's data strictly isolated at storage fabric level — FIPS 140-3 encryption, hard tenancy, and full audit trails for regulatory compliance across all jurisdictions.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_f2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Fraud Detection Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">Branch camera feeds + transaction streams + audio → VAST S3 + Event Broker</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Real-Time Correlation</strong><br><span style="font-size:14px;color:#7090c0;">Transaction event fires instantly — correlated with video feed from the same branch</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Multimodal Analysis</strong><br><span style="font-size:14px;color:#7090c0;">Face recognition + transaction pattern + audio analyzed in unified VastDB pipeline</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Cross-Branch Query</strong><br><span style="font-size:14px;color:#7090c0;">Same face + sub-$10K transactions + multiple locations — identified across all branches in seconds</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Fraud Agent Action</strong><br><span style="font-size:14px;color:#7090c0;">Account freeze + compliance alert + branch notification — fully autonomous</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab13:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA Cosmos</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Physical AI & Robotics</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Multimodal sensor and vision data for real-time agentic inference. High-speed ingestion for AI training loops. Powers humanoids, autonomous drones, and embodied AI at the scale of 1,500 GB300 GPUs.</p>
    </div>
    """, unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2, gap="large")
    with col_r1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Physical AI & Robotics</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Massive Multi-Modal Sensor Ingest</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Simultaneous ingestion of LiDAR, camera, IMU, and thermal sensor streams at extreme bandwidth — VAST's DASE architecture eliminates the I/O bottlenecks that cripple legacy storage during high-frequency sensor fusion.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Sub-Millisecond Agentic Decision Loops</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">DataEngine triggers inference the moment sensor data lands — enabling real-time decision loops required for autonomous robotics, drone navigation, and humanoid control systems.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Continuous Learning from Operations</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Every inference result is written back to VastDB alongside ground truth labels — enabling continuous model improvement without separate training pipelines or data copies.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Cross-Modal Reasoning in One Query</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">VastDB unifies video vectors, LiDAR point clouds, and telemetry metadata in one store — agents reason across modalities simultaneously for complex scene understanding.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. 1,500 GB300 GPU Proven Scale</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Proven at scale — VAST feeds massive GPU clusters for embodied AI training and inference, scaling to exabyte levels without crashing or performance degradation.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_r2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Physical AI Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Sensor Ingest</strong><br><span style="font-size:14px;color:#7090c0;">LiDAR + camera + IMU + thermal → VAST DataStore at edge node</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Event Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Native event broker fires on sensor data arrival — 1.4M events/sec</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Multi-Modal Fusion</strong><br><span style="font-size:14px;color:#7090c0;">NVIDIA microservices fuse sensor streams → VLM generates unified scene understanding</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Store + Learn</strong><br><span style="font-size:14px;color:#7090c0;">Inference results + ground truth → VastDB — continuous training loop, no data copies</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Agentic Action</strong><br><span style="font-size:14px;color:#7090c0;">Robot executes decision — navigation, manipulation, alert, or escalation</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab8:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST AgentEngine</span>
      <span class="uc-tag tag-vast">VAST Sync Engine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Document RAG</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Live RAG on unstructured and structured enterprise data. Automated market intelligence synthesis, scientific literature inference, and competitive intelligence monitoring — powered by open-source agents on VAST.</p>
    </div>
    """, unsafe_allow_html=True)
    col_ra1, col_ra2 = st.columns(2, gap="large")
    with col_ra1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Research Assistant</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Live RAG on Scientific Literature</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Sync Engine continuously ingests PubMed, arXiv, internal research databases, and competitive intelligence sources — knowledge base stays current without manual curation or nightly batch jobs.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Automated Market Intelligence</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Agents continuously monitor and synthesize competitive intelligence — surfacing insights from unstructured documents, earnings calls, and regulatory filings in real time without analyst intervention.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Structured + Unstructured in One Query</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">VastDB unifies structured data (databases, spreadsheets) and unstructured data (PDFs, emails, presentations) — agents run hybrid queries across both in one operation, no ETL between systems.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Event-Driven Knowledge Updates</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">New document lands in S3 → DataEngine triggers chunking and embedding automatically → knowledge base updated within seconds. No nightly batch jobs, no manual curation.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Multi-Agent Orchestration via MCP</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">AgentEngine coordinates specialized agents — Literature Agent, Competitive Intelligence Agent, and Synthesis Agent — passing context via Model Context Protocols without external orchestration tools.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_ra2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Research Assistant Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Sync</strong><br><span style="font-size:14px;color:#7090c0;">PubMed / arXiv / SharePoint / competitive feeds → VAST S3 continuously via Sync Engine</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Trigger + Embed</strong><br><span style="font-size:14px;color:#7090c0;">New doc triggers DataEngine → chunked and embedded automatically within seconds</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Store</strong><br><span style="font-size:14px;color:#7090c0;">Vectors + source metadata + ACLs stored as VastDB columns — instantly searchable</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Research Query</strong><br><span style="font-size:14px;color:#7090c0;">Researcher queries in natural language → hybrid semantic + metadata search across all sources</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Agent Synthesis</strong><br><span style="font-size:14px;color:#7090c0;">Research Agent synthesizes findings with citations — triggers follow-up queries via MCP</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab16:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST Event Broker</span>
      <span class="uc-tag tag-vast">VAST InsightEngine</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Network Telemetry</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Petabyte-scale telemetry ingestion, real-time threat detection, and AI-driven root cause analysis. Replace Splunk and Datadog's per-GB pricing with flat storage economics and infinite retention.</p>
    </div>
    """, unsafe_allow_html=True)
    col_nt1, col_nt2 = st.columns(2, gap="large")
    with col_nt1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Network Telemetry</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Flat Economics vs. Splunk/Datadog</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Per-GB ingestion pricing ($1–$4/GB) is untenable at petabyte scale. VAST runs the entire observability pipeline on-platform at cents/GB — infinite retention, no downsampling, no retention cliffs.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Real-Time Anomaly Detection</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Statistical anomaly detection learns per-service baselines and fires alerts based on deviations — catching novel attack patterns and network anomalies that rules-based systems miss entirely.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Unified Log + Metric + Trace</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">All three telemetry signals in one VastDB, queryable via one SQL engine (Trino). An AI agent joins a latency spike in traces with a CPU anomaly in metrics and an error in logs in a single query.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. AI-Driven Root Cause Analysis</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">LLMs query raw telemetry via standard SQL — engineers describe symptoms in natural language, the AI autonomously investigates and identifies root cause, reducing MTTR from hours to minutes.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Predictive Capacity Planning</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Historical telemetry queryable with sub-second latency — AI models identify growth trends and predict capacity requirements for data centers before constraints impact performance.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_nt2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Network Telemetry Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Ingest</strong><br><span style="font-size:14px;color:#7090c0;">Network logs + metrics + traces → VAST Event Broker at 1.4M events/sec per node</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Stream Store</strong><br><span style="font-size:14px;color:#7090c0;">Full-resolution telemetry stored in VastDB — no downsampling, years of retention</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Anomaly Detection</strong><br><span style="font-size:14px;color:#7090c0;">Statistical models detect deviations from learned baselines in real time</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">AI Investigation</strong><br><span style="font-size:14px;color:#7090c0;">LLM queries raw telemetry via SQL — root cause identified autonomously</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Closed-Loop Action</strong><br><span style="font-size:14px;color:#7090c0;">Low-risk: auto-remediate. Medium: one-click approval. High: ticket with full diagnostic context.</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab14:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST AIOS</span>
      <span class="uc-tag tag-vast">VAST DataSpace</span>
      <span class="uc-tag tag-mistral" style="background:rgba(0,180,216,0.12);color:#00b4d8;">NVIDIA NIM</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Defense & ISR</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">
        Sovereign AI inference in air-gapped facilities. NATO interoperability across 32 nations. Federated DataSpace for joint common operating pictures. 
        VAST provides the data foundation for classified drone video, multi-spectral ISR fusion, and autonomous mission planning — 
        with agencies retaining absolute control over both training data and inference models.
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_d1, col_d2 = st.columns(2, gap="large")
    with col_d1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">6 USPs for Defense & ISR</div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">6. Sovereign AI — The Inside-Out Intelligence Model</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">EU INTCEN scenario: detect patterns in classified drone video and signals intercepts without leaking data to public LLMs. Unstructured data (video/audio) → VAST DataEngine auto-vectorization → VAST Vector Store → NVIDIA NIM local AI agent. <strong style="color:#e8e8f0;">Agencies retain absolute control over both training data and inference models.</strong></div>
          </div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">7. NATO Interoperability — Breaking Protocol Barriers</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">32 nations, one mission, incompatible tools. VAST's multi-protocol namespace means Maritime Patrol uploads via S3, Land Commander reads via NFS, Analyst reads via SMB — all accessing the <strong style="color:#e8e8f0;">exact same dataset simultaneously with zero-copy sharing</strong>. No file conversion or duplication.</div>
          </div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">8. Federated DataSpace — Common Operating Picture</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST DataSpace creates a single global namespace across geographically dispersed sites. A surveillance image uploaded in Estonia is instantly accessible via metadata to HQ in Brussels. FMN alignment: "Federation over Centralization" — nations keep custody of physical storage while sharing the operational picture.</div>
          </div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">9. Capability Matrix — Tech to Mission</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:8px;font-size:13px;">
                <div style="color:#00c2e0;font-weight:700;">Mission</div><div style="color:#00c2e0;font-weight:700;">VAST Technology</div>
                <div style="color:#7090c0;">Threat Hunting</div><div style="color:#7090c0;">VAST DataBase — Log(N) lookup at exabyte scale</div>
                <div style="color:#7090c0;">NIS2 Log Retention</div><div style="color:#7090c0;">DataStore — 10-year flash endurance (QLC+SCM)</div>
                <div style="color:#7090c0;">Sovereign AI Inference</div><div style="color:#7090c0;">InsightEngine + NIM — Air-gapped RAG</div>
                <div style="color:#7090c0;">NATO Data Sharing</div><div style="color:#7090c0;">Multi-Protocol — Simultaneous NFS/S3/SMB</div>
                <div style="color:#7090c0;">Fleet Predictive Maint.</div><div style="color:#7090c0;">Event Broker — 500M+ msgs/sec (10x Kafka)</div>
                <div style="color:#7090c0;">Cyber Governance</div><div style="color:#7090c0;">VAST Data Shield — Atomic ACLs, Multi-Level Security</div>
              </div>
            </div>
          </div>

          <div style="margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">10. Robotic Workflows — Reinforcement Learning Loop</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">Sensor output/video from robotic control stack → Inference GPU cluster → RL/enforcement → Training GPU cluster (simulation, validation, reinforcement) → AI fine-tuning on VAST DB + DataStore → improved model reloaded. <strong style="color:#e8e8f0;">DataEngine orchestrates the entire continuous learning loop natively.</strong></div>
          </div>

          <div>
            <div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">11. Hard Multi-Level Security</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">FIPS 140-3 validated encryption, VAST Data Shield with atomic ACLs for multi-level security, hard multi-tenancy at the storage fabric — classified workloads air-gapped from unclassified on the same physical infrastructure.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_d2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Sovereign AI Pipeline — Air-Gapped Facility</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">ISR Ingest</strong><br><span style="font-size:14px;color:#7090c0;">EO/IR + SAR + SIGINT + UAV + classified drone video → VAST DataStore (encrypted, air-gapped)</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Auto-Vectorization</strong><br><span style="font-size:14px;color:#7090c0;">VAST DataEngine auto-vectorizes unstructured data — no public LLM contact, fully sovereign</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">VAST Vector Store</strong><br><span style="font-size:14px;color:#7090c0;">Multi-spectral vectors + geospatial metadata + timestamps stored as VastDB columns</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">NVIDIA NIM — Local AI Agent</strong><br><span style="font-size:14px;color:#7090c0;">On-premises inference only — classified patterns detected without data leaving the facility</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Mission Agent Action</strong><br><span style="font-size:14px;color:#7090c0;">Threat assessment + mission plan + RL feedback loop → continuous model improvement on-prem</span></div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1a2a1a;border-radius:10px;padding:18px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:14px;">Key Capabilities</div>
          <div style="font-size:15px;color:#6080b0;line-height:2.2;">
            ✓ &nbsp;Sovereign AI — agencies own all data + models<br>
            ✓ &nbsp;NATO multi-protocol: S3 + NFS + SMB simultaneously<br>
            ✓ &nbsp;Federated DataSpace — Estonia → Brussels in real time<br>
            ✓ &nbsp;Robotic RL training loop natively on DataEngine<br>
            ✓ &nbsp;500M+ msgs/sec Event Broker (10× Kafka)<br>
            ✓ &nbsp;VAST Data Shield — atomic ACLs, multi-level security
          </div>
        </div>
        """, unsafe_allow_html=True)

with tab15:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-vast">VAST DataSpace</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Energy & Seismic</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">Real-time sensor and safety data ingestion, operational inference at the edge, and petabyte-scale seismic analysis. Predictive maintenance, grid anomaly detection, and edge-to-cloud orchestration for critical infrastructure.</p>
    </div>
    """, unsafe_allow_html=True)
    col_e1, col_e2 = st.columns(2, gap="large")
    with col_e1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">Why VAST for Energy & Seismic</div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">1. Petabyte Seismic Data at NVMe Speed</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Seismic archives that previously took days to rehydrate are queryable in seconds on VAST. Geophysicists run pattern-matching across decades of records for exploration and hazard assessment without cold storage delays.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">2. Real-Time Safety Sensor Pipelines</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Industrial sensors stream directly to VAST — DataEngine triggers safety inference the moment anomalous readings appear, before equipment failure or safety incidents escalate to critical level.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">3. Predictive Maintenance</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">AI agents monitor equipment telemetry continuously — identifying degradation patterns weeks before failure, scheduling maintenance proactively and reducing unplanned downtime across the fleet.</div></div>
          <div style="margin-bottom:18px;"><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">4. Edge-to-Cloud for Remote Operations</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST DataSpace bridges offshore platforms, remote drilling sites, and grid substations to core data centers. Agents operate locally during connectivity loss — synchronizing automatically on reconnect.</div></div>
          <div><div style="font-size:17px;font-weight:700;color:#e8e8f0;margin-bottom:6px;">5. Grid Anomaly Detection & Forecasting</div><div style="font-size:15px;color:#5878a8;line-height:1.7;">Event Broker ingests smart grid telemetry at massive scale — AI detects anomalies, forecasts demand spikes, and orchestrates grid balancing responses in real time across the entire network.</div></div>
        </div>
        """, unsafe_allow_html=True)
    with col_e2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Energy & Seismic Pipeline</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#bfdbfe;font-size:15px;">Sensor Ingest</strong><br><span style="font-size:14px;color:#7090c0;">Industrial sensors + seismic feeds + smart grid telemetry → VAST DataStore at edge</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Real-Time Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Anomalous reading fires DataEngine pipeline immediately — no batch lag</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#7ee8f8;font-size:15px;">Safety Inference</strong><br><span style="font-size:14px;color:#7090c0;">AI model analyzes sensor pattern — classifies severity and identifies root cause</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#a7f3d0;font-size:15px;">Store + Trend</strong><br><span style="font-size:14px;color:#7090c0;">Reading + model output + equipment metadata in VastDB — trend and predictive analysis</span></div></div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>
          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;"><div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div><div><strong style="color:#fed7aa;font-size:15px;">Maintenance Action</strong><br><span style="font-size:14px;color:#7090c0;">Alert ops / schedule maintenance / adjust grid parameters — proactive, not reactive</span></div></div>
        </div>
        """, unsafe_allow_html=True)

with tab10:
    st.markdown("""
    <div style="padding:24px 0 8px;">
      <span class="uc-tag tag-vast">VAST DataEngine</span>
      <span class="uc-tag tag-vast">VAST Event Broker</span>
      <h3 style="font-size:34px;font-weight:800;letter-spacing:-0.8px;margin:16px 0 8px;color:#e8e8f0;">Data Classification & Security</h3>
      <p style="font-size:16px;color:#5878a8;line-height:1.7;max-width:820px;margin:0 0 8px;">
        56% of organizations report employees uploading sensitive data to unauthorized SaaS apps. 63% report external data oversharing. 
        Legacy regex tools cover only 10–25% of ingress/egress. VAST solves this with <strong style="color:#e8e8f0;">Classification-as-a-Service</strong> — 
        real-time classification on write, eliminating expensive third-party tools like Varonis, automating governance, and 
        providing full data estate visibility at exabyte scale.
      </p>
    </div>
    """, unsafe_allow_html=True)

    col_dc1, col_dc2 = st.columns(2, gap="large")
    with col_dc1:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #2a1a3a;border-radius:12px;padding:22px 26px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:18px;">The Problem — and Why Legacy Tools Fail</div>

          <div style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:16px;font-weight:700;color:#ef4444;margin-bottom:6px;">❌ What's Implemented Today</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">SaaS Platform Information Protection — point solutions scanning email and attachments only. Regex-based pattern matching running in batches, covering <strong style="color:#ef4444;">only 10–25% of ingress and egress</strong> during off-hours. Enterprise data lakes are almost completely uncovered — enumeration kills controls.</div>
          </div>

          <div style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:16px;font-weight:700;color:#ef4444;margin-bottom:6px;">❌ The Shadow AI / Shadow IT Problem</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">AI tools scatter sensitive data at machine speed across NAS, SaaS, shadow repositories. Expensive point solutions covering ¼ of your platforms, charging cents per API call, with 400% hyperscaler margin tacked on. Cyber-attacks, ransomware, extortion — all become easier as scale grows.</div>
          </div>

          <div style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:16px;font-weight:700;color:#10b981;margin-bottom:6px;">✅ VAST Perfection — Classification on Write</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">When data is created or changed, it's inspected in <strong style="color:#e8e8f0;">real-time using the actual value of the data — all data, everywhere</strong>. Not batches. Not samples. Not regex. An LLM parses the actual content and returns structured classification: sensitivity level, content type, regulatory flags, confidence scores.</div>
          </div>

          <div style="margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid #1e1e2e;">
            <div style="font-size:16px;font-weight:700;color:#10b981;margin-bottom:6px;">✅ Eliminate Varonis — Classification-as-a-Service</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST's built-in classification pipeline replaces expensive third-party DLP/classification products. Automated on ingest. Real-time risk reduction. Automated data governance for security teams and regulators. Full data estate visibility and searchability. <strong style="color:#e8e8f0;">Scales to petabytes without performance degradation.</strong></div>
          </div>

          <div>
            <div style="font-size:16px;font-weight:700;color:#10b981;margin-bottom:6px;">✅ VAST as DATA ARBITER</div>
            <div style="font-size:15px;color:#5878a8;line-height:1.7;">VAST combines legacy and modern AI controls across ALL data — File, SaaS, Sharing, Structured — into a single Data Arbiter that enforces Governance and Audit. No fragmented tools. One platform with full lineage tracking and audit trail for every classification decision.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_dc2:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:16px;">
          <div style="font-size:15px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">Classification-as-a-Service Pipeline</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#3b82f6;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#bfdbfe;font-size:15px;">Data Ingest</strong><br><span style="font-size:14px;color:#7090c0;">File written via S3, NFS, SMB — or VAST Sync Engine pulls from SaaS sources (SharePoint, Google Drive, Confluence)</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">Kafka Event Trigger</strong><br><span style="font-size:14px;color:#7090c0;">Built-in Kafka-compatible event broker fires instantly on write — 1.4M events/sec per node, no external broker</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">DataEngine Processing</strong><br><span style="font-size:14px;color:#7090c0;">Serverless functions chunk the file and prepare text for LLM inference — scale-to-zero when idle</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#f97316;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#fed7aa;font-size:15px;">LLM Semantic Analysis</strong><br><span style="font-size:14px;color:#7090c0;">LLM parses actual content → returns structured JSON: classification level (PUBLIC/RESTRICTED/PII), confidence score, content tags, regulatory flags, summary</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#10b981;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#a7f3d0;font-size:15px;">Metadata Persistence</strong><br><span style="font-size:14px;color:#7090c0;">Classification tags + vector embeddings + user attribution + file metadata written to VAST Database — full audit trail and lineage tracking</span></div>
          </div>
          <div style="padding-left:12px;color:#3a3a5a;">↓</div>

          <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
            <div style="width:7px;height:7px;border-radius:50%;background:#a78bfa;flex-shrink:0;margin-top:5px;"></div>
            <div><strong style="color:#7ee8f8;font-size:15px;">Semantic Search + Governance</strong><br><span style="font-size:14px;color:#7090c0;">Deep semantic search on demand across your AI Data Lake — regulators, security teams, and auditors query classification state across the full estate in real time</span></div>
          </div>
        </div>

        <div style="background:#080c1e;border:1px solid #1a2a1a;border-radius:10px;padding:18px 20px;">
          <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#3a5080;text-transform:uppercase;margin-bottom:14px;">Classification-as-a-Service Capabilities</div>
          <div style="font-size:15px;color:#6080b0;line-height:2.2;">
            ✓ &nbsp;Real-time classification on write — 100% coverage, no batches<br>
            ✓ &nbsp;Replaces Varonis and expensive DLP point solutions<br>
            ✓ &nbsp;LLM semantic analysis — not regex pattern matching<br>
            ✓ &nbsp;Full audit trail + lineage for every classification decision<br>
            ✓ &nbsp;DASE architecture — petabyte scale, no metadata hotspots<br>
            ✓ &nbsp;Automated governance for security teams and regulators<br>
            ✓ &nbsp;Data Passport: sovereignty rules travel with classified data
          </div>
        </div>
        """, unsafe_allow_html=True)


# ── VECTOR DATABASE ───────────────────────────────────────────────────────────
st.markdown('<div id="vectordb"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="padding:96px 0 48px;">
  <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">Vector Database</div>
  <div style="font-size:clamp(28px,4vw,48px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 16px;color:#e8e8f0;">Why Existing Vector Systems<br>Hit a Wall.</div>
  <div style="font-size:17px;color:#5878a8;max-width:620px;line-height:1.7;margin:0 0 0;">
    Legacy vector databases were designed for small-scale search, not enterprise AI at exabyte scale. VAST VectorDB takes a fundamentally different architectural approach.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Why existing systems fail ──────────────────────────────────────────────────
col_v1, col_v2 = st.columns([3, 2], gap="large")

with col_v1:
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:16px;">

      <div style="background:#0a0e1f;border-left:4px solid #f97316;border-radius:0 12px 12px 0;padding:22px 24px;display:flex;justify-content:space-between;align-items:center;gap:24px;">
        <div style="flex:1;">
          <div style="font-size:17px;font-weight:800;color:#e8e8f0;margin-bottom:8px;">Memory Costs Become Prohibitive</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">HNSW (industry default) needs 1.5–2× data in RAM. Indexing 1B vectors = ~4TB memory = <strong style="color:#f97316;">~$22K/month</strong> at cloud rates.</div>
        </div>
        <div style="text-align:center;flex-shrink:0;">
          <div style="font-size:42px;font-weight:900;color:#f97316;line-height:1;">~$22K</div>
          <div style="font-size:12px;color:#5878a8;margin-top:4px;">per 1B vectors/mo</div>
        </div>
      </div>

      <div style="background:#0a0e1f;border-left:4px solid #f97316;border-radius:0 12px 12px 0;padding:22px 24px;display:flex;justify-content:space-between;align-items:center;gap:24px;">
        <div style="flex:1;">
          <div style="font-size:17px;font-weight:800;color:#e8e8f0;margin-bottom:8px;">Sharding Creates Operational Complexity</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">Partitioning across nodes adds shard fan-out, routing overhead, and rebalancing events. Every growth event is a crisis.</div>
        </div>
        <div style="text-align:center;flex-shrink:0;">
          <div style="font-size:42px;font-weight:900;color:#f97316;line-height:1;">10×</div>
          <div style="font-size:12px;color:#5878a8;margin-top:4px;">more nodes to match<br>VAST at 50B vectors</div>
        </div>
      </div>

      <div style="background:#0a0e1f;border-left:4px solid #f97316;border-radius:0 12px 12px 0;padding:22px 24px;display:flex;justify-content:space-between;align-items:center;gap:24px;">
        <div style="flex:1;">
          <div style="font-size:17px;font-weight:800;color:#e8e8f0;margin-bottom:8px;">Scale Breaks RAG in Production</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">48% of enterprises report they can't keep RAG fast and responsive at scale. Pilot performance rarely survives enterprise rollout.</div>
        </div>
        <div style="text-align:center;flex-shrink:0;">
          <div style="font-size:42px;font-weight:900;color:#f97316;line-height:1;">48%</div>
          <div style="font-size:12px;color:#5878a8;margin-top:4px;">struggle at<br>production scale</div>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

with col_v2:
    st.markdown("""
    <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:32px;height:100%;">
      <div style="font-size:13px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:20px;">The Legacy Stack Problem</div>
      <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:24px;">
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">Pinecone / Milvus — RAM-bound HNSW index</div>
        </div>
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">Separate metadata DB (RDS/Postgres)</div>
        </div>
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">ETL pipeline to sync them</div>
        </div>
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">Shards to manage as scale grows</div>
        </div>
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">Index rebuilds on schema changes</div>
        </div>
        <div style="background:#080c18;border:1px solid #1e3060;border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:center;">
          <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;flex-shrink:0;"></div>
          <div style="font-size:14px;color:#7090c0;">6–8 FTEs just for patching at 58-DB scale</div>
        </div>
      </div>
      <div style="background:#0c1030;border:1px solid #0078ff;border-radius:10px;padding:16px 18px;text-align:center;">
        <div style="font-size:13px;color:#3a5080;margin-bottom:4px;">Result</div>
        <div style="font-size:16px;font-weight:700;color:#ef4444;">Architectural debt that makes<br>scaling impossible</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='padding:24px 0;'></div>", unsafe_allow_html=True)

# ── VAST's Different Architecture ─────────────────────────────────────────────
st.markdown("""
<div style="padding:48px 0 32px;">
  <div style="font-size:clamp(24px,3vw,40px);font-weight:900;letter-spacing:-1.2px;line-height:1.1;margin:0 0 12px;color:#e8e8f0;">A Fundamentally Different Architecture.</div>
  <div style="font-size:16px;color:#5878a8;max-width:600px;line-height:1.7;">VAST VectorDB uses a hierarchical clustering index stored on NVMe — not RAM. No shards. No rebuilds. Linear scale to trillions of vectors.</div>
</div>
""", unsafe_allow_html=True)

col_a1, col_a2 = st.columns([3, 2], gap="large")

with col_a1:
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:20px;">

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:24px;display:flex;gap:20px;align-items:flex-start;">
        <div style="font-size:32px;font-weight:900;color:#00c2e0;flex-shrink:0;line-height:1;width:48px;">01</div>
        <div>
          <div style="font-size:17px;font-weight:800;color:#00c2e0;margin-bottom:8px;">Hierarchical Clustering Index</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">Multi-level tree: Level 3 = ~1B, Level 4 = ~1T, Level 5 = ~1 quadrillion vectors. Each level multiplies capacity by 1,000×. <strong style="color:#e8e8f0;">No shards. No global rebuilds.</strong></div>
        </div>
      </div>

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:24px;display:flex;gap:20px;align-items:flex-start;">
        <div style="font-size:32px;font-weight:900;color:#00c2e0;flex-shrink:0;line-height:1;width:48px;">02</div>
        <div>
          <div style="font-size:17px;font-weight:800;color:#00c2e0;margin-bottom:8px;">Progressive Narrowing Search</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">Queries narrow through the hierarchy — bounded traversal, no shard fan-out, no full-graph traversal. <strong style="color:#e8e8f0;">Query cost depends on search depth, not corpus size.</strong></div>
        </div>
      </div>

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:24px;display:flex;gap:20px;align-items:flex-start;">
        <div style="font-size:32px;font-weight:900;color:#00c2e0;flex-shrink:0;line-height:1;width:48px;">03</div>
        <div>
          <div style="font-size:17px;font-weight:800;color:#00c2e0;margin-bottom:8px;">Vectors Native in VAST DataBase</div>
          <div style="font-size:15px;color:#5878a8;line-height:1.7;">Vector index embedded alongside structured data. <strong style="color:#e8e8f0;">Native SQL, hybrid vector + SQL joins, metadata filtering</strong> — no ETL, no external sync layers.</div>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

with col_a2:
    st.markdown("""
    <div style="display:flex;flex-direction:column;gap:14px;">

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:22px 24px;">
        <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:14px;">Benchmark: VAST vs Milvus</div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">Milvus 2.6 (AISAQ) @ 1B vectors</span>
          <span style="font-size:15px;font-weight:700;color:#ef4444;">~89 QPS</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">VAST @ 1B vectors</span>
          <span style="font-size:15px;font-weight:700;color:#00c2e0;">~1,000 QPS</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">VAST @ 50B vectors (8 CNodes)</span>
          <span style="font-size:15px;font-weight:700;color:#00c2e0;">1,026 QPS</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;">
          <span style="font-size:13px;color:#5878a8;">Recall rate</span>
          <span style="font-size:15px;font-weight:700;color:#10b981;">99%</span>
        </div>
      </div>

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:22px 24px;">
        <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:14px;">Cost per 1K Searches @ 50B Vectors</div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">Leading OSS hybrid vector DB</span>
          <span style="font-size:15px;font-weight:700;color:#ef4444;">$0.033</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;">
          <span style="font-size:13px;color:#5878a8;">VAST VectorDB</span>
          <span style="font-size:15px;font-weight:700;color:#10b981;">$0.003</span>
        </div>
        <div style="background:#052030;border-radius:8px;padding:12px;text-align:center;margin-top:12px;">
          <span style="font-size:24px;font-weight:900;color:#00c2e0;">91%</span>
          <span style="font-size:14px;color:#5878a8;margin-left:8px;">lower cost per query</span>
        </div>
      </div>

      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:22px 24px;">
        <div style="font-size:13px;font-weight:700;letter-spacing:1.5px;color:#00c2e0;text-transform:uppercase;margin-bottom:14px;">Continuous Ingest Performance</div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">Sustained ingest (Parquet)</span>
          <span style="font-size:14px;font-weight:700;color:#00c2e0;">~1M vectors/sec</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid #1a2540;">
          <span style="font-size:13px;color:#5878a8;">Background clustering</span>
          <span style="font-size:14px;font-weight:700;color:#00c2e0;">~290K vectors/sec</span>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;">
          <span style="font-size:13px;color:#5878a8;">Index freeze during ingest</span>
          <span style="font-size:14px;font-weight:700;color:#10b981;">None</span>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='padding:16px 0;'></div>", unsafe_allow_html=True)

# ── VAST vs competition summary ────────────────────────────────────────────────
st.markdown("""
<div style="padding:16px 0 48px;">
""", unsafe_allow_html=True)

col_b1, col_b2, col_b3, col_b4 = st.columns(4, gap="medium")
for col, stat, label, sublabel in [
    (col_b1, "11×", "Faster than Milvus", "1B vector benchmark, same hardware"),
    (col_b2, "91%", "Lower cost per query", "at 50B vectors vs leading OSS"),
    (col_b3, "50B+", "Vectors on 8 CNodes", "stable throughput, no shards"),
    (col_b4, "99%", "Recall rate", "no accuracy tradeoff for scale"),
]:
    with col:
        col.markdown(f"""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:12px;padding:24px;text-align:center;">
          <div style="font-size:40px;font-weight:900;background:linear-gradient(135deg,#fff,#00c2e0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:8px;">{stat}</div>
          <div style="font-size:14px;font-weight:700;color:#e8e8f0;margin-bottom:4px;">{label}</div>
          <div style="font-size:12px;color:#3a5080;">{sublabel}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ── SECTION 2: RESULTS ────────────────────────────────────────────────────────
st.markdown('<div id="results"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-alt">
  <div class="section-label">Results</div>
  <div class="section-title">The Scale of<br>the Mandate.</div>
  <div class="section-sub">Real performance numbers that underpin VAST's national AI infrastructure vision.</div>
  <div class="stats-grid">
    <div class="stat-cell">
      <div class="stat-number">500K</div>
      <div class="stat-label">Camera target for AI Cloud<br><span style="font-size:12px;color:#2a4070;">From 25K today — VAST scales linearly</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">20×</div>
      <div class="stat-label">Faster inference (TTFT)<br><span style="font-size:12px;color:#2a4070;">KV Cache offload: 63s → 3s</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">99.999%</div>
      <div class="stat-label">Uptime SLA<br><span style="font-size:12px;color:#2a4070;">AI training job failure rate −90%</span></div>
    </div>
    <div class="stat-cell">
      <div class="stat-number">3M+</div>
      <div class="stat-label">GPUs supported globally<br><span style="font-size:12px;color:#2a4070;">NVIDIA NCP certified · 3.9Gb/s per GPU</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 3: COST & TIME SAVINGS ───────────────────────────────────────────
st.markdown('<div id="savings"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Time &amp; Cost Savings</div>
  <div class="section-title">Legacy Architecture<br>vs. VAST AIOS.</div>
  <div class="section-sub">What VAST's public sector clients leave behind when they move to VAST.</div>
  <div class="ba-grid">
    <div class="ba-card ba-before">
      <div class="ba-header">❌ &nbsp;Legacy Approach</div>
      <div class="ba-row"><span class="ba-row-label">Observability storage cost</span><span class="ba-row-val">$1–$4 / GB ingestion</span></div>
      <div class="ba-row"><span class="ba-row-label">Inference latency (TTFT)</span><span class="ba-row-val">63 seconds</span></div>
      <div class="ba-row"><span class="ba-row-label">Edge deployment footprint</span><span class="ba-row-val">+12 hardware racks</span></div>
      <div class="ba-row"><span class="ba-row-label">Pipeline deployment time</span><span class="ba-row-val">Weeks</span></div>
      <div class="ba-row"><span class="ba-row-label">GPU memory efficiency</span><span class="ba-row-val">Low — KV cache on GPU</span></div>
      <div class="ba-row"><span class="ba-row-label">Data classification</span><span class="ba-row-val">Slow batch processing</span></div>
    </div>
    <div class="ba-card ba-after">
      <div class="ba-header">✅ &nbsp;VAST + NVIDIA</div>
      <div class="ba-row"><span class="ba-row-label">Observability storage cost</span><span class="ba-row-val">Cents / GB · infinite retention</span></div>
      <div class="ba-row"><span class="ba-row-label">Inference latency (TTFT)</span><span class="ba-row-val">3 seconds (20× faster)</span></div>
      <div class="ba-row"><span class="ba-row-label">Edge deployment footprint</span><span class="ba-row-val">75% less power · 12 racks removed</span></div>
      <div class="ba-row"><span class="ba-row-label">Pipeline deployment time</span><span class="ba-row-val">Under 1 working day</span></div>
      <div class="ba-row"><span class="ba-row-label">GPU memory efficiency</span><span class="ba-row-val">Up to 90% better · KV on NVMe</span></div>
      <div class="ba-row"><span class="ba-row-label">Data classification</span><span class="ba-row-val">Real-time via VAST DataEngine</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 4: WHY VAST NOW ───────────────────────────────────────────────────
st.markdown('<div id="why"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-alt">
  <div style="font-size:16px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">Why VAST for VAST</div>
  <div class="section-title">Built for AI Cloud.</div>
  <div class="section-sub">Four capabilities that make VAST the only platform for VAST's AI mandate.</div>

  <div class="zigzag-item">
    <div class="zigzag-text">
      <div class="section-label">Capability 01</div>
      <h3>NVIDIA NCP Certified — GPU Zero-Starvation</h3>
      <p>To compete with US-based Neoclouds, VAST must guarantee that expensive GPUs are never starved of data. VAST is the NVIDIA Cloud Partner (NCP) certified data layer powering the world's largest AI clouds — supporting over 3 million GPUs globally.</p>
      <p style="margin-top:16px;">VAST delivers linear performance scaling for VAST's GPU clusters:</p>
      <ul style="margin:12px 0 0;padding-left:20px;color:#5878a8;font-size:15px;line-height:2.0;">
        <li><strong style="color:#e8e8f0;">Read bandwidth exceeding 10TB/s</strong> — GPUs remain fully utilized, maximizing Revenue Per Watt</li>
        <li><strong style="color:#e8e8f0;">3.9Gb/s per Vera Rubin GPU</strong> — exceeding NCP max performance benchmarks</li>
        <li><strong style="color:#e8e8f0;">99.999% uptime</strong> — AI training job failure rates reduced by 90% vs. legacy parallel file systems</li>
        <li><strong style="color:#e8e8f0;">Non-Disruptive Upgrades</strong> — rolling updates of stateless containers; HUMAIN's AI cloud stays online 24/7/365</li>
      </ul>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#7ee8f8;">NVIDIA NCP Certified</strong><br><span style="font-size:14px;">3.9Gb/s per GPU — exceeds NCP max performance</span></div></div>
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">10TB/s+ Read Bandwidth</strong><br><span style="font-size:14px;">Zero GPU starvation across VAST's AI factory</span></div></div>
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">3M+ GPUs worldwide</strong><br><span style="font-size:14px;">Powering CoreWeave, xAI, and the world's largest AI clouds</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">99.999% uptime</strong><br><span style="font-size:14px;">Job failure rate −90% vs. legacy parallel file systems</span></div></div>
    </div>
  </div>

  <div class="zigzag-item reverse">
    <div class="zigzag-text">
      <div class="section-label">Capability 02</div>
      <h3>Sovereignty as a Service — 26 Ministries, One Platform</h3>
      <p>Security is VAST's competitive moat. VAST turns data sovereignty into a software feature — enforcing strict isolation at the storage fabric level so a Ministry of Finance dataset is logically air-gapped from a Ministry of Health dataset, even on shared hardware.</p>
      <p style="margin-top:16px;">Key sovereignty capabilities built into the storage layer:</p>
      <ul style="margin:12px 0 0;padding-left:20px;color:#5878a8;font-size:15px;line-height:2.0;">
        <li><strong style="color:#e8e8f0;">Hard Multi-Tenancy:</strong> Tenant-specific VIP pools, VLANs, and encryption keys — hard isolation, not soft</li>
        <li><strong style="color:#e8e8f0;">Data Passport:</strong> Every object carries immutable sovereignty metadata — rules travel with the data</li>
        <li><strong style="color:#e8e8f0;">Ransomware Protection:</strong> Indestructible Snapshots cannot be deleted by any user, including admins</li>
        <li><strong style="color:#e8e8f0;">FIPS 140-3 Encryption:</strong> At rest and in flight — compliance for regulated government workloads</li>
      </ul>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#7ee8f8;">26 enterprise Ministries</strong><br><span style="font-size:14px;">Hard isolated on a single VAST platform</span></div></div>
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">Data Passport</strong><br><span style="font-size:14px;">Sovereignty rules travel immutably with every object</span></div></div>
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">FIPS 140-3 Validated</strong><br><span style="font-size:14px;">Encryption at rest and in flight — government ready</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">Indestructible Snapshots</strong><br><span style="font-size:14px;">Ransomware-proof — no user, including admins, can delete</span></div></div>
    </div>
  </div>

  <div class="zigzag-item">
    <div class="zigzag-text">
      <div class="section-label">Capability 03</div>
      <h3>Global Namespace — Edge to Core to Cloud</h3>
      <p>The AI Factory fails if data is trapped in silos. VAST DataSpace creates a single global namespace that spans all of VAST's locations — from an edge node in edge locations to a training cluster in core data centers — without complex copy scripts.</p>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">edge locations → core data centers</strong><br><span style="font-size:14px;">Edge data instantly visible to core training clusters via metadata</span></div></div>
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#7ee8f8;">Global Snapshot Clones</strong><br><span style="font-size:14px;">Hydrate inference workspaces at the edge in seconds</span></div></div>
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">VAST Polaris</strong><br><span style="font-size:14px;">Kubernetes-based global control plane across hybrid + multicloud</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">Dark fiber resilience</strong><br><span style="font-size:14px;">Edge nodes continue locally during outages, sync on reconnect</span></div></div>
    </div>
  </div>

  <div class="zigzag-item reverse">
    <div class="zigzag-text">
      <div class="section-label">Capability 04</div>
      <h3>Flash Economics — Kill the Hard Drive Tax</h3>
      <p>To make VAST's AI Cloud profitable at scale, VAST breaks the cost curve of flash. Similarity-Based Data Reduction achieves an average 2.12:1 data reduction across global fleets — making all-flash performance economically viable for every workload, including long-term archival.</p>
    </div>
    <div class="zigzag-visual">
      <div class="pill pill-purple"><span class="pill-dot"></span><div><strong style="color:#7ee8f8;">2.12:1 Data Reduction</strong><br><span style="font-size:14px;">Avg across global fleets via similarity-based compression</span></div></div>
      <div class="pill pill-orange"><span class="pill-dot"></span><div><strong style="color:#fed7aa;">One Flash Tier</strong><br><span style="font-size:14px;">No hot/warm/cold tiering — one administrator manages exabytes</span></div></div>
      <div class="pill pill-green"><span class="pill-dot"></span><div><strong style="color:#a7f3d0;">Zero-Cost Snapshots</strong><br><span style="font-size:14px;">"Time Machine" for models — zero performance impact</span></div></div>
      <div class="pill pill-blue"><span class="pill-dot"></span><div><strong style="color:#bfdbfe;">API-First Design</strong><br><span style="font-size:14px;">REST API for every feature — click-to-deploy cloud experience</span></div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 5: ENTRY POINTS ───────────────────────────────────────────────────
st.markdown('<div id="entry"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="padding:96px 48px 24px; background:#05080f;">
  <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">Choose Your Entry Point</div>
  <div style="font-size:48px;font-weight:800;letter-spacing:-1.5px;line-height:1.1;margin:0 0 16px;color:#e8e8f0;">Build VAST's<br>AI Cloud.</div>
  <div style="font-size:17px;color:#5878a8;max-width:560px;line-height:1.7;margin:0 0 40px;">Three phases to a complete AI Operating System — from foundational storage to full agentic AI services.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:32px;height:100%;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#00c2e0;margin-bottom:12px;">Phase 1 · DataStore</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Deploy Fundamental Storage</div>
      <div style="font-size:14px;color:#5878a8;line-height:1.65;margin-bottom:24px;">Establish the foundation: high-performance, resilient, multi-tenant storage. Support NFS, SMB, S3 Object, and NVMe/TCP Block across all 26 tenant workloads simultaneously.</div>
      <div style="font-size:14px;color:#7090c0;line-height:2.2;">
        <div>✓ &nbsp;NFS / SMB / S3 Object / NVMe-TCP Block</div>
        <div>✓ &nbsp;Global namespaces &amp; instant snapshots</div>
        <div>✓ &nbsp;Wire encryption &amp; FIPS 140-3</div>
        <div>✓ &nbsp;10TB/s read bandwidth — GPU zero-starvation</div>
        <div>✓ &nbsp;Kubernetes install in 15 minutes</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Start with Infrastructure →", "#", use_container_width=True)

with col2:
    st.markdown("""
    <div style="background:linear-gradient(160deg,#13132a,#111120);border:2px solid #6d28d9;border-radius:16px;padding:32px;height:100%;box-shadow:0 0 40px rgba(109,40,217,0.2);">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#00c2e0;margin-bottom:12px;">Phase 2 — Recommended</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Add Advanced AI Data Services</div>
      <div style="font-size:14px;color:#5878a8;line-height:1.65;margin-bottom:24px;">Layer on VastDB, Event Broker, Vector Database, InsightEngine, AgentEngine, and Observability. Differentiate VAST's cloud from generic providers.</div>
      <div style="font-size:14px;color:#7090c0;line-height:2.2;">
        <div>✓ &nbsp;Vector DB + Transactional DB unified</div>
        <div>✓ &nbsp;Event Broker — 1M events/sec</div>
        <div>✓ &nbsp;Data Lakehouse with flat storage economics</div>
        <div>✓ &nbsp;Native Mistral LLM / VLM hosting</div>
        <div>✓ &nbsp;InsightEngine + Observability included</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Explore Full Platform →", "#", use_container_width=True, type="primary")

with col3:
    st.markdown("""
    <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:32px;height:100%;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#00c2e0;margin-bottom:12px;">Blueprints</div>
      <div style="font-size:20px;font-weight:800;color:#e8e8f0;margin-bottom:12px;">Deploy with Open-Source Blueprints</div>
      <div style="font-size:14px;color:#5878a8;line-height:1.65;margin-bottom:24px;">Production-ready VSS and Document RAG blueprints deploy in under a day. Fully open-source — customize for large-scale crowd management, tenant RAG, or traffic intelligence.</div>
      <div style="font-size:14px;color:#7090c0;line-height:2.2;">
        <div>✓ &nbsp;VSS Blueprint — Video Search Summarization</div>
        <div>✓ &nbsp;Document RAG Assistant Blueprint</div>
        <div>✓ &nbsp;Mistral models pre-integrated</div>
        <div>✓ &nbsp;NVIDIA Cosmos Reason 2 compatible</div>
        <div>✓ &nbsp;Open source — fork and extend freely</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 0 16px;'></div>", unsafe_allow_html=True)
    st.link_button("Browse Blueprints →", "https://github.com/vast-data/cosmos-labs", use_container_width=True)

# ── NCP Page ──────────────────────────────────────────────────────────────────
_params = st.query_params
if _params.get("ncp") == "1":
    if st.button("← Back to VAST AI Factory", key="back_ncp"):
        st.query_params.clear()
        st.rerun()
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)


    # Hero
    st.markdown("""
    <div style="padding:48px 0 24px;background:radial-gradient(ellipse 80% 50% at 50% 0%,rgba(0,120,255,0.15) 0%,transparent 70%);">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">NVIDIA Cloud Partner Program</div>
      <div style="font-size:clamp(32px,4vw,52px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 16px;color:#e8e8f0;">Why NCPs Choose VAST</div>
      <div style="font-size:17px;color:#5878a8;max-width:700px;line-height:1.7;margin:0 0 32px;">
        VAST is the NVIDIA Cloud Partner (NCP) certified data layer powering the world's largest AI clouds — 
        supporting over 3 million GPUs globally. As a NCP, VAST delivers the performance, reliability, economics, 
        and sovereignty required to compete with US-based hyperscalers.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:0 64px 48px;">
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px;background:#0f1535;border-radius:16px;overflow:hidden;border:1px solid #1a2540;">
        <div style="background:#080c18;padding:36px 28px;text-align:center;">
          <div class="stat-big">3M+</div>
          <div class="stat-label">GPUs supported globally<br>across NCP deployments</div>
        </div>
        <div style="background:#080c18;padding:36px 28px;text-align:center;">
          <div class="stat-big">3.9Gb/s</div>
          <div class="stat-label">Per Vera Rubin GPU<br>Exceeds NCP max performance</div>
        </div>
        <div style="background:#080c18;padding:36px 28px;text-align:center;">
          <div class="stat-big">99.999%</div>
          <div class="stat-label">Uptime SLA<br>Job failure rate reduced 90%</div>
        </div>
        <div style="background:#080c18;padding:36px 28px;text-align:center;">
          <div class="stat-big">2.12×</div>
          <div class="stat-label">Data reduction avg<br>Across global fleet</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 9 NCP Capabilities ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:0 0 16px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">9 Key Capabilities</div>
      <div style="font-size:clamp(28px,4vw,44px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 12px;color:#e8e8f0;">Built for the NCP Standard.</div>
      <div style="font-size:16px;color:#5878a8;max-width:700px;line-height:1.7;">Every capability VAST delivers to make NCPs competitive with AWS, Azure, and GCP.</div>
    </div>
    """, unsafe_allow_html=True)

    caps = [
        {
            "num": "01",
            "title": "NCP Certified Performance — GPU Zero-Starvation",
            "color": "#6d28d9",
            "body": "VAST is the NVIDIA Cloud Partner (NCP) certified data layer powering the world's largest AI clouds. For the AI Cloud, VAST delivers linear performance scaling that supports massive-scale training and inference without the \"east-west\" traffic bottlenecks of legacy shared-nothing architectures.",
            "bullets": [
                ("🟣", "Read bandwidth exceeding 10TB/s for large clusters — GPUs remain fully utilized, maximizing Revenue Per Watt"),
                ("🟣", "3.9Gb/s per Vera Rubin GPU — exceeding NCP max performance benchmarks"),
                ("🟣", "Linear scaling — no performance cliff as cluster size grows"),
                ("🟣", "Deployed at CoreWeave, xAI, and the world's largest AI neo-clouds"),
            ]
        },
        {
            "num": "02",
            "title": "High Availability — Enterprise-Grade 99.999% Resilience",
            "color": "#10b981",
            "body": "In the AI era, downtime means expensive GPUs sit idle, burning power without generating revenue. VAST just works — NCPs don't pay penalties for downtime and lost GPU time.",
            "bullets": [
                ("🟢", "Rack-Level Resilience (RLR): Each rack is an independent failure domain with N+4 protection (LDEC)"),
                ("🟢", "Job Failure Reduction: Architecture reduces AI training job failure rates by 90% — customers complete training runs faster and cheaper"),
                ("🟢", "Non-Disruptive Upgrades (NDU): Rolling updates of stateless containers — AI cloud stays online 24/7/365"),
                ("🟢", "Withstand loss of two full racks or multiple simultaneous SSD failures without data loss"),
            ]
        },
        {
            "num": "03",
            "title": "Flash Economics — Kill the Hard Drive Tax",
            "color": "#f97316",
            "body": "To make the AI Cloud profitable, NCPs must break the cost curve of flash. VAST's Similarity-Based Data Reduction is the economic engine of the AI cloud.",
            "bullets": [
                ("🟠", "2.12:1 average data reduction across global fleets — by identifying patterns across the entire global namespace"),
                ("🟠", "One Tier: VAST eliminates tiering — no hot/warm/cold complexity. Single all-flash tier for everything"),
                ("🟠", "Exabytes managed by a single administrator — minimal headcount, maximum scale"),
                ("🟠", "Flash performance at archive economics — makes the AI Cloud the most cost-competitive venue"),
            ]
        },
        {
            "num": "04",
            "title": "Security & Governance — Sovereignty-as-a-Service",
            "color": "#6d28d9",
            "body": "Security is a NCP's competitive moat. VAST turns data sovereignty into a software feature — enabling NCPs to host regulated government workloads that hyperscalers cannot touch.",
            "bullets": [
                ("🟣", "Hard Multi-Tenancy: Tenant-specific VIP pools, VLANs, and encryption keys — bank data air-gapped from startup data on shared hardware"),
                ("🟣", "Data Passport: Every object carries immutable sovereignty metadata — rules travel dynamically with the data"),
                ("🟣", "Ransomware Protection as a Service: Indestructible Snapshots that cannot be deleted by any user, including admins"),
                ("🟣", "FIPS 140-3 validated encryption at rest and in flight — GDPR, finance, government compliance"),
            ]
        },
        {
            "num": "05",
            "title": "Global Data Namespace — Unify On-Prem, Edge, and Cloud",
            "color": "#3b82f6",
            "body": "The AI Factory fails if data is trapped in silos. VAST DataSpace creates a single global namespace spanning all NCP locations — making the network behave like a single computer.",
            "bullets": [
                ("🔵", "Defying Data Gravity: A dataset ingested at an edge node is instantly visible to a training cluster in another region via metadata — no copy scripts"),
                ("🔵", "Global Snapshot Clones: Instantly provision massive models or datasets to any inference location in seconds"),
                ("🔵", "VAST Polaris: Kubernetes-based global control plane governing VAST AI OS clusters across hybrid and multicloud"),
                ("🔵", "Edge resilience: Sites dynamically toggle data ownership during connectivity loss — sync automatically on reconnect"),
            ]
        },
        {
            "num": "06",
            "title": "Simple Operation — Exabyte Scale with Zero Complexity",
            "color": "#10b981",
            "body": "Our largest customers support exabytes of data fueling 100Ks of GPUs, with as little as one full-time administrator. Complexity is the enemy of scale.",
            "bullets": [
                ("🟢", "One Cost-Efficient Tier built for AI: no tiers to manage, no data movement between hot and cold"),
                ("🟢", "Automated Lifecycle Management: VMS automates patching, expansion, and rebalancing"),
                ("🟢", "Focus engineering talent on revenue-generating AI services rather than storage maintenance"),
                ("🟢", "API-First Design: Every feature exposed via REST API — integrates directly into customer portals or Kubernetes workflows (CSI/COSI)"),
            ]
        },
        {
            "num": "07",
            "title": "Multi-Protocol — The Universal Data Platform",
            "color": "#f97316",
            "body": "NCPs serve diverse customer bases requiring different access methods for the same data — automotive, healthcare, media, government. VAST supports all simultaneously at native performance.",
            "bullets": [
                ("🟠", "Simultaneous NFS, SMB, S3, and NVMe-over-TCP on the same dataset — no copies, no conversion"),
                ("🟠", "Data scientist ingests via S3, cleans via NFS, streams to GPUs via GPUDirect — one dataset, three protocols"),
                ("🟠", "No gateway bottlenecks: S3 is a first-class citizen with native performance, not bolted on"),
                ("🟠", "Toggle between POSIX and S3 at no additional cost"),
            ]
        },
        {
            "num": "08",
            "title": "Cloud-Grade Data Management",
            "color": "#6d28d9",
            "body": "To compete with AWS/Azure, NCPs must offer a cloud-like experience. VAST delivers every cloud data management feature, natively.",
            "bullets": [
                ("🟣", "Zero-Cost Snapshots: 'Write-in-Free-Space' architecture — instant snapshots and clones with zero performance impact and zero initial capacity consumption"),
                ("🟣", "API-First: Every feature via REST API — click-to-deploy cloud experience for customer-facing portals"),
                ("🟣", "Deep Observability: Granular per-tenant usage visibility — accurate billing for exact storage consumption and bandwidth"),
                ("🟣", "Elastic scaling, data catalog, end-to-end encryption, replication, global namespace — all included"),
            ]
        },
        {
            "num": "09",
            "title": "KV Cache Acceleration — Breaking the GPU Memory Wall",
            "color": "#10b981",
            "body": "The bottleneck for the next wave of AI is the GPU Memory Wall. As inference contexts grow, GPU memory fills up. VAST and NVIDIA solve this together.",
            "bullets": [
                ("🟢", "Global KV Cache Acceleration: Offloading inference context from GPU HBM to VAST storage via RDMA"),
                ("🟢", "20× improvement in Time-To-First-Token (TTFT) — from 63 seconds to 3 seconds"),
                ("🟢", "Up to 90% improvement in GPU efficiency — customers run massive models on fewer GPUs"),
                ("🟢", "75% reduction in power consumption by offloading KV cache from GPU to NVMe via NVIDIA BlueField DPUs"),
            ]
        },
    ]

    for i in range(0, len(caps), 2):
        row = caps[i:i+2]
        cols = st.columns(len(row), gap="large")
        for col, cap in zip(cols, row):
            with col:
                bullets_html = ''.join([
                    f'<div class="pill"><div class="dot" style="background:{cap["color"]};"></div><div style="font-size:14px;color:#7090c0;line-height:1.6;">{b[1]}</div></div>'
                    for b in cap["bullets"]
                ])
                st.markdown(f"""
                <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;margin-bottom:24px;height:100%;">
                  <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
                    <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:{cap['color']};text-transform:uppercase;background:rgba(0,120,255,0.10);padding:4px 10px;border-radius:100px;border:1px solid {cap['color']}40;">{cap['num']}</div>
                  </div>
                  <div style="font-size:18px;font-weight:800;color:#e8e8f0;margin-bottom:10px;letter-spacing:-0.3px;">{cap['title']}</div>
                  <div style="font-size:14px;color:#5878a8;line-height:1.7;margin-bottom:16px;">{cap['body']}</div>
                  {bullets_html}
                </div>
                """, unsafe_allow_html=True)

    # ── AIOS Stack ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:48px 0 24px;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">Platform Architecture</div>
      <div style="font-size:clamp(28px,4vw,44px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 12px;color:#e8e8f0;">The VAST AI Operating System</div>
      <div style="font-size:16px;color:#5878a8;max-width:700px;line-height:1.7;">Just as Windows manages hardware for desktops, VAST provides the underlying device drivers and infrastructure layer to make massive GPU clusters usable.</div>
    </div>
    """, unsafe_allow_html=True)

    col_de, col_db, col_ds = st.columns(3, gap="medium")

    with col_de:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #0078ff;border-radius:16px;padding:28px;height:100%;">
          <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">DataEngine Layer</div>
          <div style="font-size:18px;font-weight:800;color:#e8e8f0;margin-bottom:4px;">DataEngine</div>
          <div style="font-size:14px;color:#5878a8;margin-bottom:16px;">Scalable, Event-Driven Computing · Triggers, Functions, Containers</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;">
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#00c2e0;">SyncEngine</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#00c2e0;">InsightEngine</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#00c2e0;">AgentEngine</span>
          </div>
          <div style="font-size:13px;color:#2a4070;">Index · RAG · Agents · Observability</div>
        </div>
        """, unsafe_allow_html=True)

    with col_db:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;height:100%;">
          <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">DataBase Layer</div>
          <div style="font-size:18px;font-weight:800;color:#e8e8f0;margin-bottom:4px;">DataBase</div>
          <div style="font-size:14px;color:#5878a8;margin-bottom:16px;">Transactional &amp; Analytical Database</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">EDW</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">Events</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">Vectors</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">SQL · Parquet · Kafka</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    with col_ds:
        st.markdown("""
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px;height:100%;">
          <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:16px;">DataStore Layer</div>
          <div style="font-size:18px;font-weight:800;color:#e8e8f0;margin-bottom:4px;">DataStore</div>
          <div style="font-size:14px;color:#5878a8;margin-bottom:16px;">Universal Storage Infrastructure</div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">NFS</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">SMB</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">S3</span>
            <span style="background:#0f1535;border:1px solid #1e3060;border-radius:6px;padding:5px 12px;font-size:13px;color:#7090c0;">NVMe/TCP</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:16px 0 48px;">
      <div style="background:#080c1e;border:1px solid #1a2540;border-radius:12px;padding:20px 28px;">
        <div style="font-size:13px;font-weight:700;color:#3a5080;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">DataSpace — Globally-Distributed Data Computing</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_hw, col_csp, col_gpu = st.columns(3, gap="medium")
    with col_hw:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;">
          <div style="font-size:12px;color:#2a4070;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Hardware Platforms</div>
          <div style="font-size:15px;color:#5878a8;">HPE · Dell · Supermicro · Cisco</div>
        </div>
        """, unsafe_allow_html=True)
    with col_csp:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;">
          <div style="font-size:12px;color:#2a4070;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Traditional CSPs</div>
          <div style="font-size:15px;color:#5878a8;">AWS · Google Cloud · Oracle · Equinix</div>
        </div>
        """, unsafe_allow_html=True)
    with col_gpu:
        st.markdown("""
        <div style="background:#080c1e;border:1px solid #1a2540;border-radius:10px;padding:16px 20px;">
          <div style="font-size:12px;color:#2a4070;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">GPU Clouds</div>
          <div style="font-size:15px;color:#5878a8;">CoreWeave · Core42 · Lambda · and more</div>
        </div>
        """, unsafe_allow_html=True)


    # ── NCP NVIDIA Architecture ────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:48px 64px 0;background:#080c18;">
      <div class="label">NVIDIA Cloud Partner Architecture</div>
      <div class="big-title">NVIDIA Certified Performance</div>
      <div class="sub">The full AI lifecycle — from data collection to inference — on a single VAST platform, certified by NVIDIA.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:0 64px 48px;background:#080c18;">
      <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:20px;padding:40px;">
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-bottom:24px;">
          <div style="background:#0c1030;border:1px solid #0078ff;border-radius:10px 0 0 10px;padding:20px 16px;text-align:center;">
            <div style="font-size:13px;font-weight:700;color:#00c2e0;margin-bottom:4px;">Data Collection</div>
            <div style="font-size:11px;color:#3a5080;margin-top:8px;">Upload</div>
          </div>
          <div style="background:#080c1e;border-top:1px solid #1e1e32;border-bottom:1px solid #1e1e32;padding:20px 16px;text-align:center;position:relative;">
            <div style="font-size:13px;font-weight:700;color:#e8e8f0;margin-bottom:4px;">Preprocessing</div>
            <div style="font-size:11px;color:#3a5080;margin-top:8px;">Load Data · Filtering</div>
            <div style="position:absolute;top:50%;right:-8px;transform:translateY(-50%);color:#00c2e0;font-size:18px;z-index:10;">→</div>
          </div>
          <div style="background:#080c1e;border-top:1px solid #1e1e32;border-bottom:1px solid #1e1e32;padding:20px 16px;text-align:center;position:relative;">
            <div style="font-size:13px;font-weight:700;color:#e8e8f0;margin-bottom:4px;">Data Access to HPS</div>
            <div style="font-size:11px;color:#3a5080;margin-top:8px;">Load · Store</div>
            <div style="position:absolute;top:50%;right:-8px;transform:translateY(-50%);color:#00c2e0;font-size:18px;z-index:10;">→</div>
          </div>
          <div style="background:#080c1e;border-top:1px solid #1e1e32;border-bottom:1px solid #1e1e32;padding:20px 16px;text-align:center;position:relative;">
            <div style="font-size:13px;font-weight:700;color:#e8e8f0;margin-bottom:4px;">Training</div>
            <div style="font-size:11px;color:#3a5080;margin-top:8px;">Load Dataset · Checkpoint</div>
            <div style="position:absolute;top:50%;right:-8px;transform:translateY(-50%);color:#00c2e0;font-size:18px;z-index:10;">→</div>
          </div>
          <div style="background:#0c1030;border:1px solid #0078ff;border-radius:0 10px 10px 0;padding:20px 16px;text-align:center;">
            <div style="font-size:13px;font-weight:700;color:#00c2e0;margin-bottom:4px;">Inference</div>
            <div style="font-size:11px;color:#3a5080;margin-top:8px;">Query · KV Cache</div>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
          <div style="background:#080c1e;border:1px solid #1e1e2e;border-radius:10px;padding:18px 20px;">
            <div style="font-size:12px;font-weight:700;color:#3a5080;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Data Lake</div>
            <div style="font-size:14px;color:#5878a8;">High-capacity, data reduction services · Ransomware detection</div>
          </div>
          <div style="background:#0c1030;border:1px solid #0078ff;border-radius:10px;padding:18px 20px;">
            <div style="font-size:12px;font-weight:700;color:#00c2e0;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">High-Performance Storage (HPS)</div>
            <div style="font-size:14px;color:#5878a8;">High read and write bandwidth with low latency · <strong style="color:#00c2e0;">Exceeding NCP Max Performance of 3.9Gb/s per GPU</strong></div>
          </div>
        </div>
        <div style="background:#080c1e;border:1px solid #1e3060;border-radius:10px;padding:18px 24px;">
          <div style="font-size:13px;font-weight:700;color:#00c2e0;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">VAST Data Platform — Underpinning Everything</div>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;font-size:13px;color:#5878a8;">
            <div>✓ &nbsp;High throughput &nbsp;&nbsp;✓ &nbsp;Multi-tenancy &nbsp;&nbsp;✓ &nbsp;Linear scale</div>
            <div>✓ &nbsp;Quality-of-Service &nbsp;&nbsp;✓ &nbsp;Highly-Available &nbsp;&nbsp;✓ &nbsp;Efficient All Flash</div>
            <div>✓ &nbsp;Data Services &nbsp;&nbsp;✓ &nbsp;Enforced governance &nbsp;&nbsp;✓ &nbsp;Encryption</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── KV Cache ───────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:48px 0 0;">
      <div style="font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:12px;">Future-Proofing</div>
      <div style="font-size:clamp(28px,4vw,44px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 12px;color:#e8e8f0;">Win the Race to Real-Time Inference</div>
      <div style="font-size:16px;color:#5878a8;max-width:700px;line-height:1.7;">The next wave of AI is inference and agentic workflows. VAST and NVIDIA solve the GPU Memory Wall together — giving NCPs superior inference economics vs. hyperscalers.</div>
    </div>
    <div style="padding:0 64px 64px;">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:32px;">
          <div style="font-size:16px;font-weight:800;color:#e8e8f0;margin-bottom:16px;">🧠 KV Cache Acceleration</div>
          <div style="font-size:14px;color:#5878a8;line-height:1.8;margin-bottom:20px;">
            As inference contexts grow (summarizing hours of video, massive legal documents), GPU memory fills up. VAST introduces persistent, shared KV Cache acceleration — moving AI conversation memory from expensive GPU HBM to VAST storage via RDMA.
          </div>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:14px;color:#5878a8;">TTFT improvement</span>
              <span style="font-size:16px;font-weight:700;color:#10b981;">20× faster</span>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:14px;color:#5878a8;">GPU efficiency improvement</span>
              <span style="font-size:16px;font-weight:700;color:#10b981;">Up to 90%</span>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:14px;color:#5878a8;">Power consumption reduction</span>
              <span style="font-size:16px;font-weight:700;color:#10b981;">Up to 75%</span>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:14px;color:#5878a8;">I/O path</span>
              <span style="font-size:16px;font-weight:700;color:#10b981;">Zero-copy via BlueField DPU</span>
            </div>
          </div>
        </div>
        <div style="background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:32px;">
          <div style="font-size:16px;font-weight:800;color:#e8e8f0;margin-bottom:16px;">🌐 Physical AI & Agentic Workloads</div>
          <div style="font-size:14px;color:#5878a8;line-height:1.8;margin-bottom:20px;">
            The market is shifting from model training to real-time inference and agentic workflows — Smart Cities, Robotics, Physical AI. VAST's AIOS is purpose-built for this shift, with native event-driven brokers that trigger immediate actions the moment patterns emerge.
          </div>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
              <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
              <div style="font-size:14px;color:#7090c0;">1.4M events/sec native Kafka-compatible broker — no external infrastructure</div>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
              <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
              <div style="font-size:14px;color:#7090c0;">Multi-protocol fluency: S3, NFS, SMB, NVMe-over-TCP — full AI lifecycle on one platform</div>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
              <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
              <div style="font-size:14px;color:#7090c0;">Scale-to-Zero compute — idle pipelines consume 2GB RAM and 2 cores</div>
            </div>
            <div style="background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;">
              <div style="width:7px;height:7px;border-radius:50%;background:#0078ff;flex-shrink:0;margin-top:5px;"></div>
              <div style="font-size:14px;color:#7090c0;">DataSpace global namespace — edge to metro to core, distance abstracted by software</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ──────────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="border-top:1px solid #1a1a2e;padding:32px 64px;display:flex;align-items:center;justify-content:space-between;">
      <div>
        <div style="font-size:15px;font-weight:800;background:linear-gradient(90deg,#fff,#00c2e0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">VAST AIOS</div>
        <div style="font-size:12px;color:#3030a0;margin-top:4px;">The AI Operating System for the Kingdom of Saudi Arabia</div>
      </div>
      <div style="font-size:12px;color:#3030a0;">© 2025 VAST Data. Confidential — prepared for Humain.</div>
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-brand">VAST AI Factory</div>
    <div style="font-size:12px;color:#1a3060;margin-top:4px;">The AI Operating System for Public &amp; Private Cloud</div>
  </div>
  <div style="font-size:12px;color:#1a3060;">© 2025 VAST Data. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)
