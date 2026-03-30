import streamlit as st

st.set_page_config(
    page_title="Why NCPs Choose VAST",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05080f; color: #e8e8f0; }
.main { background-color: #05080f; }
.block-container { padding: 2rem 3rem 2rem 3rem !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
header { display: none !important; }
footer { display: none !important; }
.section { padding: 64px 64px; }
.section-alt { background: #080c18; }
.label { font-size:11px;font-weight:700;letter-spacing:2px;color:#00c2e0;text-transform:uppercase;margin-bottom:10px; }
.big-title { font-size:clamp(32px,4vw,52px);font-weight:900;letter-spacing:-1.5px;line-height:1.1;margin:0 0 16px;color:#e8e8f0; }
.sub { font-size:17px;color:#5878a8;max-width:700px;line-height:1.7;margin:0 0 48px; }
.card { background:#0a0e1f;border:1px solid #1a2540;border-radius:16px;padding:28px 32px;margin-bottom:24px; }
.card-purple { background:#0a0e1f;border:1px solid #0078ff;border-radius:16px;padding:28px 32px;margin-bottom:24px;box-shadow:0 0 30px rgba(109,40,217,0.1); }
.card h3 { font-size:20px;font-weight:800;color:#e8e8f0;margin:0 0 10px;letter-spacing:-0.5px; }
.card p { font-size:15px;color:#5878a8;line-height:1.7;margin:0; }
.stat-big { font-size:clamp(40px,5vw,64px);font-weight:900;letter-spacing:-2px;background:linear-gradient(135deg,#fff,#00c2e0);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1; }
.stat-label { font-size:14px;color:#3a5080;margin-top:6px;line-height:1.5; }
.pill { background:#080c1e;border:1px solid #1e3060;border-radius:8px;padding:12px 16px;display:flex;gap:10px;align-items:flex-start;margin-bottom:8px; }
.dot { width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:5px; }
.back-btn { display:inline-block;padding:10px 20px;background:rgba(0,120,255,0.12);border:1px solid rgba(109,40,217,0.4);border-radius:8px;color:#00c2e0;font-size:13px;font-weight:600;text-decoration:none;margin-bottom:32px; }
div[data-testid="stTabs"] button { color: #5878a8 !important; font-size: 15px !important; font-weight: 500 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: #00c2e0 !important; border-bottom-color: #00c2e0 !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

# Back button
st.markdown('<a href="/" class="back-btn">← Back to VAST AI Factory</a>', unsafe_allow_html=True)

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
