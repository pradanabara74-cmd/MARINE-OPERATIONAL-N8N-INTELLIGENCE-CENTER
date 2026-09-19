import streamlit as st
from datetime import datetime

# ============================================================
# MARINE OPERATIONAL N8N INTELLIGENCE CENTER
# Master Application
# ============================================================

st.set_page_config(
    page_title="Marine Operational N8N Intelligence Center",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# STYLE
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0;
    }

    .sub-title {
        font-size: 1rem;
        opacity: 0.75;
        margin-bottom: 1.5rem;
    }

    .system-card {
        border: 1px solid rgba(128,128,128,0.25);
        border-radius: 14px;
        padding: 20px;
        min-height: 180px;
    }

    .status-online {
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("⚓ N8N INTELLIGENCE")


# ============================================================
# GLOBAL VESSEL CONTROL
# Accept any vessel name worldwide
# ============================================================

st.sidebar.subheader("🌍 GLOBAL VESSEL CONTROL")

vessel_name = st.sidebar.text_input(
    "Vessel Name",
    placeholder="Type any vessel name...",
    key="global_vessel_name"
)

if vessel_name:
    vessel_name = vessel_name.strip().upper()
    st.sidebar.success(f"⚓ ACTIVE VESSEL: {vessel_name}")
else:
    st.sidebar.caption("Enter any vessel name worldwide")

st.sidebar.divider()


page = st.sidebar.radio(
    "INTELLIGENCE MODULE",
    [
        "Command Center",
        "Marine Operations",
        "Fuel Efficiency BBM",
        "QHSSE Company",
        "N8N Workflow Center",
        "AI Intelligence",
        "System Status",
    ],
)

st.sidebar.divider()

st.sidebar.caption(
    "MARINE OPERATIONAL N8N\n"
    "INTELLIGENCE CENTER"
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<div class="main-title">⚓ MARINE OPERATIONAL N8N INTELLIGENCE CENTER</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-title">'
    'MARINE OPERATIONS • FUEL EFFICIENCY BBM • '
    'QHSSE COMPANY • POWERED BY N8N'
    '</div>',
    unsafe_allow_html=True,
)

# ============================================================
# COMMAND CENTER
# ============================================================

if page == "Command Center":

    st.subheader("Executive Command Center")

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Marine Operations", "ONLINE")
    k2.metric("Fuel Intelligence", "ONLINE")
    k3.metric("QHSSE Intelligence", "ONLINE")
    k4.metric("N8N Engine", "READY")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="system-card">
            <h3>⚓ Marine Operations</h3>
            Vessel Operations<br>
            Voyage Intelligence<br>
            PMS / Maintenance<br>
            Defects & Certificates<br>
            Bunker & Cargo<br>
            Marine AI Co-Pilot
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="system-card">
            <h3>⛽ Fuel Efficiency BBM</h3>
            Unlimited DPR CSV<br>
            Engine Database<br>
            RPM / Load / SFOC<br>
            Fuel Performance<br>
            Anomaly Detection<br>
            Fuel AI Intelligence
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="system-card">
            <h3>🛡️ QHSSE Company</h3>
            Incident / Near Miss<br>
            Inspection<br>
            Audit & Findings<br>
            Risk Assessment<br>
            NCR / CAR<br>
            QHSSE AI Intelligence
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.info(
        "Master Command Center siap. "
        "Database, AI dan N8N workflow akan dihubungkan pada tahap berikutnya."
    )

# ============================================================
# MARINE OPERATIONS
# ============================================================

elif page == "Marine Operations":

    st.header("⚓ Marine Operations Intelligence")

    module = st.selectbox(
        "Select Module",
        [
            "Vessel Operations",
            "Voyage Intelligence",
            "PMS / Maintenance",
            "Defects",
            "Certificates",
            "Bunker",
            "Cargo",
            "Audit & Findings",
            "Action Tracker",
            "Marine AI Co-Pilot",
        ],
    )

    st.success(f"{module} module ready for integration.")

# ============================================================
# FUEL EFFICIENCY
# ============================================================

elif page == "Fuel Efficiency BBM":

    st.header("⛽ Fuel Efficiency BBM Intelligence")

    uploaded_file = st.file_uploader(
        "Upload DPR Vessel (CSV)",
        type=["csv"],
        help="Sistem dirancang untuk menerima jumlah kolom DPR secara dinamis.",
    )

    if uploaded_file is not None:
        import pandas as pd

        try:
            df = pd.read_csv(uploaded_file)

            st.success(
                f"DPR berhasil dibaca: "
                f"{len(df):,} rows × {len(df.columns):,} columns"
            )

            st.subheader("DPR Data Preview")
            st.dataframe(df, use_container_width=True)

            st.subheader("Detected DPR Columns")
            st.write(list(df.columns))

        except Exception as error:
            st.error(f"CSV tidak dapat dibaca: {error}")

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("Fuel Status", "READY")
    c2.metric("Engine Database", "NEXT STAGE")
    c3.metric("AI Analysis", "NEXT STAGE")

# ============================================================
# QHSSE
# ============================================================

elif page == "QHSSE Company":

    st.header("🛡️ QHSSE Company Intelligence")

    qhsse_module = st.selectbox(
        "QHSSE Module",
        [
            "Incident",
            "Near Miss",
            "Inspection",
            "Audit",
            "Risk Assessment",
            "NCR / CAR",
            "Corrective Action",
            "Action Tracker",
            "QHSSE AI",
        ],
    )

    st.success(f"{qhsse_module} module ready for integration.")

# ============================================================
# N8N
# ============================================================

elif page == "N8N Workflow Center":

    st.header("🔄 N8N Workflow Center")

    st.write(
        "N8N akan menjadi automation orchestration engine "
        "untuk seluruh sistem."
    )

    workflows = {
        "DPR Processing": "READY FOR BUILD",
        "Fuel Alert": "READY FOR BUILD",
        "Maintenance Alert": "READY FOR BUILD",
        "QHSSE Alert": "READY FOR BUILD",
        "Management Report": "READY FOR BUILD",
        "AI Workflow": "READY FOR BUILD",
    }

    for workflow, status in workflows.items():
        c1, c2 = st.columns([3, 1])
        c1.write(workflow)
        c2.write(status)

# ============================================================
# AI
# ============================================================

elif page == "AI Intelligence":

    st.header("🤖 AI Intelligence Center")

    prompt = st.text_area(
        "Ask Marine AI",
        placeholder=(
            "Contoh: Analyze vessel fuel consumption, "
            "maintenance risk atau QHSSE findings..."
        ),
        height=140,
    )

    if st.button("Analyze with AI", type="primary"):
        if prompt.strip():
            st.info(
                "AI interface sudah siap. "
                "AI provider akan dihubungkan setelah "
                "fondasi N8N selesai."
            )
        else:
            st.warning("Masukkan pertanyaan terlebih dahulu.")

# ============================================================
# SYSTEM STATUS
# ============================================================

elif page == "System Status":

    st.header("🖥️ System Status")

    st.write("Application: ONLINE")
    st.write("Marine Operations: READY")
    st.write("Fuel Efficiency: READY")
    st.write("QHSSE: READY")
    st.write("N8N Integration: PENDING")
    st.write("Database Integration: PENDING")
    st.write("AI Integration: PENDING")

    st.caption(
        "System check: "
        + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.caption(
    "MARINE OPERATIONAL N8N INTELLIGENCE CENTER | "
    "Marine Operations • Fuel Efficiency BBM • QHSSE Company"
)
