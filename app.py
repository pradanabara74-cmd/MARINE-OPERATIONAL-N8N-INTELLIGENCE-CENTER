import streamlit as st
from datetime import datetime
import pandas as pd
import io
import csv

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
# ============================================================
# BBM / MGO RPM CONTROL - LITER
# ============================================================

with st.sidebar.expander("⛽ BBM/MGO RPM CONTROL", expanded=False):

    st.caption("Main Engine Fuel Consumption (Liter)")

    rpm_points = [600, 700, 800, 900, 1000, 1200, 1300]

    bbm_me_kiri = {}
    bbm_me_kanan = {}

    for rpm in rpm_points:
        st.markdown(f"**RPM {rpm}**")

        left_col, right_col = st.columns(2)

        with left_col:
            bbm_me_kiri[rpm] = st.number_input(
                "ME Kiri (L)",
                min_value=0.0,
                value=0.0,
                step=1.0,
                key=f"bbm_me_kiri_{rpm}",
            )

        with right_col:
            bbm_me_kanan[rpm] = st.number_input(
                "ME Kanan (L)",
                min_value=0.0,
                value=0.0,
                step=1.0,
                key=f"bbm_me_kanan_{rpm}",
            )

    st.divider()

    ae_24h_liter = st.number_input(
        "AE 24 Jam - Pemakaian BBM (Liter)",
        min_value=0.0,
        value=0.0,
        step=1.0,
        key="ae_24h_liter",
    )

    total_me_kiri_liter = sum(bbm_me_kiri.values())
    total_me_kanan_liter = sum(bbm_me_kanan.values())

    total_me_liter = (
        total_me_kiri_liter
        + total_me_kanan_liter
    )

    total_bbm_liter = (
        total_me_liter
        + ae_24h_liter
    )

    st.divider()

    st.metric(
        "TOTAL ME KIRI",
        f"{total_me_kiri_liter:,.2f} Liter"
    )

    st.metric(
        "TOTAL ME KANAN",
        f"{total_me_kanan_liter:,.2f} Liter"
    )

    st.metric(
        "TOTAL MAIN ENGINE",
        f"{total_me_liter:,.2f} Liter"
    )

    st.metric(
        "AE 24 JAM",
        f"{ae_24h_liter:,.2f} Liter"
    )

    st.metric(
        "TOTAL BBM / MGO",
        f"{total_bbm_liter:,.2f} Liter"
    )

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
    # ============================================================
    # ACTIVE GLOBAL VESSEL
    # ============================================================
    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name}")
    else:
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

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
    # ============================================================
    # ACTIVE GLOBAL VESSEL
    # ============================================================
    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name}")
    else:
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

    # ============================================================
    # UNIVERSAL DPR CSV READER - UNLIMITED COLUMNS
    # ============================================================

    st.subheader("📄 DPR Vessel Data")

    uploaded_file = st.file_uploader(
        "Upload DPR Vessel (CSV)",
        type=["csv"],
        key="universal_dpr_csv",
        help=(
            "Upload DPR kapal dalam format CSV. "
            "Sistem menerima jumlah kolom secara dinamis."
        ),
    )

    if uploaded_file is not None:
        try:
                raw_data = uploaded_file.getvalue()

        # ----------------------------------------------
        # AUTO DETECT ENCODING
        # ----------------------------------------------
        decoded_text = None
        detected_encoding = None

        for encoding in [
            "utf-8-sig",
            "utf-8",
            "cp1252",
            "latin1",
        ]:
            try:
                decoded_text = raw_data.decode(encoding)
                detected_encoding = encoding
                break
            except UnicodeDecodeError:
                continue

        if decoded_text is None:
            raise ValueError("Encoding CSV tidak dapat dikenali.")

            # ----------------------------------------------------
            # AUTO DETECT DELIMITER
            # comma / semicolon / tab / pipe
            # ----------------------------------------------------
            sample = decoded_text[:10000]

            try:
                dialect = csv.Sniffer().sniff(
                    sample,
                    delimiters=",;\t|",
                )
                detected_separator = dialect.delimiter
            except csv.Error:
                detected_separator = ","

            # ----------------------------------------------------
            # READ DPR - UNLIMITED / DYNAMIC COLUMNS
            # ----------------------------------------------------
            df = pd.read_csv(
                io.StringIO(decoded_text),
                sep=detected_separator,
                engine="python",
            )

            # Bersihkan nama kolom
            df.columns = [
                str(column).strip()
                for column in df.columns
            ]

            # Buang kolom yang benar-benar kosong / Unnamed
            empty_columns = [
                column
                for column in df.columns
                if str(column).lower().startswith("unnamed:")
                and df[column].isna().all()
            ]

            if empty_columns:
                df = df.drop(columns=empty_columns)

            # ----------------------------------------------------
            # STORE DPR FOR OTHER MODULES
            # ----------------------------------------------------
            st.session_state["dpr_dataframe"] = df
            st.session_state["dpr_filename"] = uploaded_file.name
            st.session_state["dpr_vessel"] = vessel_name

            # ----------------------------------------------------
            # DPR STATUS
            # ----------------------------------------------------
            st.success(
                f"✅ DPR BERHASIL DIBACA | "
                f"{len(df):,} rows × {len(df.columns):,} columns"
            )

            d1, d2, d3 = st.columns(3)

            d1.metric(
                "DPR Rows",
                f"{len(df):,}",
            )

            d2.metric(
                "DPR Columns",
                f"{len(df.columns):,}",
            )

            d3.metric(
                "Active Vessel",
                vessel_name if vessel_name else "Not Selected",
            )

            st.caption(
                f"File: {uploaded_file.name} | "
                f"Encoding: {detected_encoding} | "
                f"Separator: {repr(detected_separator)}"
            )

            # ----------------------------------------------------
            # DPR DATA PREVIEW
            # ----------------------------------------------------
            st.subheader("📊 DPR Data Preview")

            st.dataframe(
                df,
                use_container_width=True,
                height=400,
            )

            # ----------------------------------------------------
            # DETECT ALL DPR COLUMNS
            # ----------------------------------------------------
            st.subheader("🔎 Detected DPR Columns")

            st.write(
                f"Total detected columns: {len(df.columns)}"
            )

            st.dataframe(
                pd.DataFrame(
                    {
                        "No.": range(1, len(df.columns) + 1),
                        "DPR Column": list(df.columns),
                        "Data Type": [
                            str(df[column].dtype)
                            for column in df.columns
                        ],
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

            # ----------------------------------------------------
            # DATA QUALITY
            # ----------------------------------------------------
            total_cells = int(df.shape[0] * df.shape[1])
            empty_cells = int(df.isna().sum().sum())

            if total_cells > 0:
                completeness = (
                    (total_cells - empty_cells)
                    / total_cells
                    * 100
                )
            else:
                completeness = 0.0

            st.subheader("🧠 DPR Intelligence Status")

            q1, q2, q3 = st.columns(3)

            q1.metric(
                "Data Completeness",
                f"{completeness:.1f}%",
            )

            q2.metric(
                "Empty Cells",
                f"{empty_cells:,}",
            )

            q3.metric(
                "Reader Status",
                "READY",
            )

            st.success(
                "🚢 DPR DATA READY FOR FUEL INTELLIGENCE"
            )

        except Exception as error:
            st.error(
                f"❌ DPR CSV tidak dapat dibaca: {error}"
            )

    # ==========================================================
    # ENGINE SPECIFICATION DATABASE & AUTO-FILL
    # ==========================================================

    st.divider()
    st.subheader("⚙️ Engine Specification Database")

    # Database dapat terus ditambah tanpa mengubah sistem utama
    ENGINE_DATABASE = {
        "Caterpillar": {
            "3512C": {
                "power_kw": 1902.0,
                "rated_rpm": 1800.0,
                "sfoc": 205.0,
            },
            "3516C": {
                "power_kw": 2525.0,
                "rated_rpm": 1800.0,
                "sfoc": 205.0,
            },
        },
        "Cummins": {
            "KTA38-M2": {
                "power_kw": 895.0,
                "rated_rpm": 1800.0,
                "sfoc": 210.0,
            },
            "KTA50-M2": {
                "power_kw": 1193.0,
                "rated_rpm": 1800.0,
                "sfoc": 210.0,
            },
        },
        "Yanmar": {
            "6EY18ALW": {
                "power_kw": 660.0,
                "rated_rpm": 900.0,
                "sfoc": 205.0,
            },
        },
        "MAN": {
            "D2862": {
                "power_kw": 1324.0,
                "rated_rpm": 2100.0,
                "sfoc": 205.0,
            },
        },
        "Custom / Other": {
            "Manual Entry": {
                "power_kw": 0.0,
                "rated_rpm": 0.0,
                "sfoc": 0.0,
            },
        },
    }

    engine_maker = st.selectbox(
        "Engine Maker",
        list(ENGINE_DATABASE.keys()),
        key="fuel_engine_maker",
    )

    engine_models = list(ENGINE_DATABASE[engine_maker].keys())

    engine_model = st.selectbox(
        "Engine Model",
        engine_models,
        key="fuel_engine_model",
    )

    selected_engine = ENGINE_DATABASE[engine_maker][engine_model]

    st.caption(
        "Select an engine from the database or use "
        "Custom / Other → Manual Entry."
    )

    e1, e2, e3 = st.columns(3)

    with e1:
        rated_power = st.number_input(
            "Rated Power (kW)",
            min_value=0.0,
            value=float(selected_engine["power_kw"]),
            step=1.0,
            key=f"rated_power_{engine_maker}_{engine_model}",
        )

    with e2:
        rated_rpm = st.number_input(
            "Rated RPM",
            min_value=0.0,
            value=float(selected_engine["rated_rpm"]),
            step=1.0,
            key=f"rated_rpm_{engine_maker}_{engine_model}",
        )

    with e3:
        base_sfoc = st.number_input(
            "Base SFOC (g/kWh)",
            min_value=0.0,
            value=float(selected_engine["sfoc"]),
            step=1.0,
            key=f"base_sfoc_{engine_maker}_{engine_model}",
        )

    # Basic validation
    engine_ready = (
        rated_power > 0
        and rated_rpm > 0
        and base_sfoc > 0
    )

    if engine_ready:
        st.success(
            f"⚙️ ENGINE READY | {engine_maker} {engine_model} | "
            f"{rated_power:,.0f} kW | {rated_rpm:,.0f} RPM | "
            f"SFOC {base_sfoc:,.1f} g/kWh"
        )
    else:
        st.info(
            "Enter Rated Power, Rated RPM and Base SFOC "
            "to activate the engine specification."
        )

    # ==========================================================
    # SYSTEM STATUS
    # ==========================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("Fuel Status", "READY")
    c2.metric(
        "Engine Database",
        "READY" if engine_ready else "INPUT REQUIRED",
    )
    c3.metric("AI Analysis", "NEXT STAGE")
    # ==========================================================
    # FUEL PERFORMANCE INTELLIGENCE
    # ==========================================================

    st.divider()
    st.subheader("📊 Fuel Performance Intelligence")

    if engine_ready:
        fp1, fp2, fp3 = st.columns(3)

        engine_load_pct = fp1.number_input(
            "Engine Load (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=1.0,
            key="fuel_engine_load",
        )

        running_hours = fp2.number_input(
            "Running Hours",
            min_value=0.0,
            value=24.0,
            step=1.0,
            key="fuel_running_hours",
        )

        actual_fuel_mt = fp3.number_input(
            "Actual Fuel Consumption (MT)",
            min_value=0.0,
            value=0.0,
            step=0.1,
            key="actual_fuel_mt",
        )

        calculated_power_kw = rated_power * (engine_load_pct / 100.0)

        expected_fuel_kg = (
            calculated_power_kw
            * running_hours
            * base_sfoc
        )

        expected_fuel_mt = expected_fuel_kg / 1_000_000

        variance_mt = actual_fuel_mt - expected_fuel_mt

        if expected_fuel_mt > 0:
            variance_pct = (variance_mt / expected_fuel_mt) * 100
        else:
            variance_pct = 0.0

        m1, m2, m3, m4 = st.columns(4)

        m1.metric(
            "Calculated Engine Power",
            f"{calculated_power_kw:,.0f} kW",
        )

        m2.metric(
            "Expected Fuel",
            f"{expected_fuel_mt:,.2f} MT",
        )

        m3.metric(
            "Actual Fuel",
            f"{actual_fuel_mt:,.2f} MT",
        )

        m4.metric(
            "Fuel Variance",
            f"{variance_pct:+.1f}%",
            delta=f"{variance_mt:+.2f} MT",
            delta_color="inverse",
        )

        if actual_fuel_mt <= 0:
            st.info("Enter actual fuel consumption to start performance analysis.")
        elif variance_pct > 10:
            st.error(
                "🔴 HIGH FUEL CONSUMPTION — actual consumption is more than "
                "10% above calculated baseline."
            )
        elif variance_pct > 5:
            st.warning(
                "🟠 FUEL PERFORMANCE WARNING — consumption is above calculated baseline."
            )
        else:
            st.success(
                "🟢 FUEL PERFORMANCE NORMAL — consumption is within calculated baseline."
            )

    else:
        st.warning(
            "Complete Engine Specification Database before running Fuel Performance Intelligence."
        )


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
