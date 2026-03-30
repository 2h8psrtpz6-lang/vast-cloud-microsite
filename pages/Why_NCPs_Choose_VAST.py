import streamlit as st

st.set_page_config(
    page_title="Why NCPs Choose VAST",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Password Gate (shared session state with main app) ─────────────────────────
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
    </style>
    <div class="auth-container">
      <div style="font-size:36px;margin-bottom:16px;">⚡</div>
      <div style="font-size:28px;font-weight:900;color:#e8e8f0;margin-bottom:8px;">VAST AI Factory</div>
      <div style="font-size:15px;color:#5878a8;margin-bottom:32px;">Enter your access code to continue</div>
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

# Back button
st.markdown('<a href="/" class="back-btn" style="display:inline-block;padding:10px 20px;background:rgba(0,120,255,0.12);border:1px solid rgba(0,194,224,0.4);border-radius:8px;color:#00c2e0;font-size:13px;font-weight:600;text-decoration:none;margin-bottom:32px;">← Back to VAST AI Factory</a>', unsafe_allow_html=True)

# Hero
st.markdown("""
<div style="padding:48px 64px 24px;background:radial-gradient(ellipse 80% 50% at 50% 0%,rgba(0,120,255,0.15) 0%,transparent 70%),#0a0a0f;">
  <div class="label">NVIDIA Cloud Partner Program</div>
  <div class="big-title">Why NCPs Choose VAST</div>
  <div class="sub">
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
<div style="padding:0 64px 16px;">
  <div class="label">9 Key Capabilities</div>
  <div class="big-title">Built for the NCP Standard.</div>
  <div class="sub">Every capability VAST delivers to make NCPs competitive with AWS, Azure, and GCP.</div>
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
<div style="padding:48px 64px 24px;">
  <div class="label">Platform Architecture</div>
  <div class="big-title">The VAST AI Operating System</div>
  <div class="sub">Just as Windows manages hardware for desktops, VAST provides the underlying device drivers and infrastructure layer to make massive GPU clusters usable.</div>
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
<div style="padding:48px 64px 0;">
  <div class="label">Future-Proofing</div>
  <div class="big-title">Win the Race to Real-Time Inference</div>
  <div class="sub">The next wave of AI is inference and agentic workflows. VAST and NVIDIA solve the GPU Memory Wall together — giving NCPs superior inference economics vs. hyperscalers.</div>
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
