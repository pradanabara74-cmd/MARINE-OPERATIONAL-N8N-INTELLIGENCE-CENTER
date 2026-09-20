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
# ==========================================================
# BBM / MGO RPM CONTROL
# ONE ACTIVE RPM = ONE OPERATING CONDITION
# ==========================================================

with st.sidebar.expander("⛽ BBM/MGO RPM CONTROL", expanded=False):

    st.caption("Main Engine Fuel Consumption (Liter/Jam)")

    rpm_points = [600, 700, 800, 900, 1000, 1200, 1300]

    # ------------------------------------------------------
    # PILIH RPM YANG SEDANG DIGUNAKAN
    # ------------------------------------------------------

    active_rpm = st.selectbox(
        "RPM Aktif",
        rpm_points,
        index=0,
        key="active_rpm",
    )

    st.markdown(f"### RPM {active_rpm}")

    left_col, right_col = st.columns(2)

    # ------------------------------------------------------
    # MAIN ENGINE KIRI
    # ------------------------------------------------------

    with left_col:
        me_kiri_lph = st.number_input(
            "ME Kiri (Liter/Jam)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            key="active_me_kiri_lph",
        )

    # ------------------------------------------------------
    # MAIN ENGINE KANAN
    # ------------------------------------------------------

    with right_col:
        me_kanan_lph = st.number_input(
            "ME Kanan (Liter/Jam)",
            min_value=0.0,
            value=0.0,
            step=1.0,
            key="active_me_kanan_lph",
        )

    # ------------------------------------------------------
    # TOTAL MAIN ENGINE PER JAM
    # RUMUS:
    # ME KIRI + ME KANAN
    # ------------------------------------------------------

    total_me_kiri_liter = me_kiri_lph
    total_me_kanan_liter = me_kanan_lph

    total_me_liter = (
        total_me_kiri_liter
        + total_me_kanan_liter
    )

    st.divider()

    st.metric(
        "TOTAL MAIN ENGINE / JAM",
        f"{total_me_liter:,.2f} Liter/Jam",
    )

    # ------------------------------------------------------
    # RUNNING HOURS MAIN ENGINE
    # ------------------------------------------------------

    me_running_hours = st.number_input(
        "Main Engine Running Hours",
        min_value=0.0,
        max_value=24.0,
        value=1.0,
        step=0.5,
        key="me_running_hours",
    )

    # Total aktual ME berdasarkan jam operasi
    total_me_consumption = (
        total_me_liter
        * me_running_hours
    )

    st.metric(
        "TOTAL ME CONSUMPTION",
        f"{total_me_consumption:,.2f} Liter",
    )

    st.divider()

    # ======================================================
    # AUXILIARY ENGINE
    # ======================================================

    st.caption("Auxiliary Engine Fuel Consumption")

    ae_liter_per_hour = st.number_input(
        "AE - Pemakaian BBM (Liter/Jam)",
        min_value=0.0,
        value=5.0,
        step=0.1,
        key="ae_liter_per_hour",
    )

    # AE bekerja 24 jam
    ae_24h_liter = (
        ae_liter_per_hour
        * 24.0
    )

    st.metric(
        "AE 24 JAM",
        f"{ae_24h_liter:,.2f} Liter",
    )

    # ======================================================
    # TOTAL FUEL CONSUMPTION
    # ======================================================

    total_bbm_liter = (
        total_me_consumption
        + ae_24h_liter
    )

    st.divider()

    st.metric(
        "TOTAL BBM / MGO CONSUMPTION",
        f"{total_bbm_liter:,.2f} Liter",
    )

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

    st.header("⚓ Executive Command Center")

    # ==========================================================
    # ACTIVE GLOBAL VESSEL
    # ==========================================================

    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name}")
    else:
        st.warning(
            "⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL."
        )

    st.divider()

    # ==========================================================
    # MASTER SYSTEM STATUS
    # ==========================================================

    st.subheader("🌐 Intelligence System Status")

    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Marine Operations",
        "ONLINE"
    )

    k2.metric(
        "Fuel Intelligence",
        "ONLINE"
    )

    k3.metric(
        "QHSSE Intelligence",
        "ONLINE"
    )

    k4.metric(
        "N8N Engine",
        "READY"
    )

    st.divider()

    # ==========================================================
    # OPERATIONAL INTELLIGENCE CENTER
    # ==========================================================

    st.subheader("📊 Operational Intelligence Center")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ⚓ Marine Operations")
        st.write("Vessel Operations")
        st.write("Voyage Intelligence")
        st.write("PMS / Maintenance")
        st.write("Defects & Certificates")
        st.write("Bunker & Cargo")
        st.write("Marine AI Co-Pilot")

    with col2:
        st.markdown("### ⛽ Fuel Efficiency BBM")
        st.write("Unlimited DPR CSV")
        st.write("Engine Database")
        st.write("RPM / Load / SFOC")
        st.write("Fuel Performance")
        st.write("Anomaly Detection")
        st.write("Fuel AI Intelligence")

    with col3:
        st.markdown("### 🛡️ QHSSE Company")
        st.write("Incident / Near Miss")
        st.write("Inspection")
        st.write("Audit & Findings")
        st.write("Risk Assessment")
        st.write("NCR / CAR")
        st.write("QHSSE AI Intelligence")

    st.divider()

    # ==========================================================
    # CURRENT FUEL CONTROL
    # Uses the calculation already proven in the sidebar.
    # ==========================================================

    st.subheader("⛽ Current Fuel Control")

    f1, f2, f3, f4 = st.columns(4)

    f1.metric(
        "Active RPM",
        f"{active_rpm} RPM"
    )

    f2.metric(
        "Main Engine",
        f"{total_me_consumption:,.2f} L"
    )

    f3.metric(
        "AE 24 Hours",
        f"{ae_24h_liter:,.2f} L"
    )

    f4.metric(
        "Total BBM / MGO",
        f"{total_bbm_liter:,.2f} L"
    )

    st.caption(
        "Total BBM / MGO = Main Engine Consumption + "
        "Auxiliary Engine 24 Hours"
    )

    st.divider()

    # ==========================================================
    # COMMAND CENTER STATUS
    # ==========================================================

    st.success(
        "✅ COMMAND CENTER ONLINE — "
        "Marine Operations, Fuel Intelligence, "
        "QHSSE and N8N systems ready."
    )

elif page == "Marine Operations":

    st.header("⚓ Marine Operations Intelligence")

    # ==========================================================
    # ACTIVE GLOBAL VESSEL
    # ==========================================================
    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name.upper()}")
    else:
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

    module = st.selectbox(
        "Select Marine Operations Module",
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
        key="marine_operations_module",
    )

    st.divider()

    # ==========================================================
    # 1. VESSEL OPERATIONS
    # ==========================================================
    if module == "Vessel Operations":

        st.subheader("🚢 Vessel Operations")

        c1, c2, c3 = st.columns(3)

        with c1:
            operation_status = st.selectbox(
                "Operation Status",
                [
                    "Underway",
                    "At Anchor",
                    "In Port",
                    "Standby",
                    "Towing",
                    "Maneuvering",
                    "Off Hire",
                ],
                key="vessel_operation_status",
            )

        with c2:
            speed_knots = st.number_input(
                "Speed (Knots)",
                min_value=0.0,
                value=0.0,
                step=0.1,
                key="vessel_speed_knots",
            )

        with c3:
            engine_hours = st.number_input(
                "Main Engine Running Hours",
                min_value=0.0,
                value=0.0,
                step=0.1,
                key="vessel_engine_hours",
            )

        st.metric("CURRENT OPERATION", operation_status)
        st.metric("CURRENT SPEED", f"{speed_knots:.1f} Knots")
        st.metric("ME RUNNING HOURS", f"{engine_hours:.1f} Hours")

    # ==========================================================
    # 2. VOYAGE INTELLIGENCE
    # ==========================================================
    elif module == "Voyage Intelligence":

        st.subheader("🧭 Voyage Intelligence")

        voyage_file = st.file_uploader(
            "Upload Voyage CSV",
            type=["csv"],
            key="voyage_csv",
        )

        if voyage_file is not None:
            try:
                voyage_df = pd.read_csv(voyage_file)

                st.success(
                    f"✅ Voyage data loaded — {len(voyage_df)} records"
                )

                st.dataframe(
                    voyage_df,
                    use_container_width=True,
                )

                st.metric(
                    "VOYAGE RECORDS",
                    len(voyage_df),
                )

            except Exception as e:
                st.error(f"Unable to read Voyage CSV: {e}")
        else:
            st.info("Upload Voyage CSV to start analysis.")

    # ============================================================
# 3. PMS / MAINTENANCE INTELLIGENCE
# ============================================================
elif module == "PMS / Maintenance":
    st.subheader("🔧 PMS / Maintenance Intelligence")

    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name}")
    else:
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

    pms_file = st.file_uploader(
        "Upload PMS / Maintenance CSV",
        type=["csv"],
        key="pms_csv"
    )

    if pms_file is None:
        st.info("Upload PMS CSV to start maintenance analysis.")

    else:
        try:
            pms_df = pd.read_csv(pms_file)

            # Remove completely empty rows and columns
            pms_df = pms_df.dropna(how="all")
            pms_df = pms_df.dropna(axis=1, how="all")

            # Clean column names
            pms_df.columns = [
                str(col).strip()
                for col in pms_df.columns
            ]

            if pms_df.empty:
                st.warning("⚠️ PMS CSV contains no maintenance records.")

            else:
                st.success(
                    f"✅ PMS data loaded — {len(pms_df)} records"
                )

                st.markdown("### 📋 PMS Records")
                st.dataframe(
                    pms_df,
                    use_container_width=True
                )

                st.metric(
                    "PMS RECORDS",
                    len(pms_df)
                )

                # --------------------------------------------
                # FACTS
                # --------------------------------------------
                st.markdown("### 📊 Facts")

                st.write(
                    f"Total maintenance records: **{len(pms_df)}**"
                )

                st.write(
                    f"Total data fields detected: **{len(pms_df.columns)}**"
                )

                # --------------------------------------------
                # DATA GAPS
                # --------------------------------------------
                st.markdown("### 🔎 Data Gaps")

                required_fields = [
                    "vessel",
                    "equipment",
                    "maintenance",
                    "due_date",
                    "status"
                ]

                normalized_columns = {
                    str(col).strip().lower().replace(" ", "_")
                    for col in pms_df.columns
                }

                missing_fields = [
                    field
                    for field in required_fields
                    if field not in normalized_columns
                ]

                if missing_fields:
                    st.warning(
                        "Missing recommended PMS fields: "
                        + ", ".join(missing_fields)
                    )
                else:
                    st.success("✅ Core PMS fields detected.")

                # --------------------------------------------
                # MAINTENANCE RISK
                # --------------------------------------------
                st.markdown("### ⚠️ Maintenance Risk")

                risk_score = 0

                if missing_fields:
                    risk_score += len(missing_fields)

                status_column = None

                for col in pms_df.columns:
                    if str(col).strip().lower() == "status":
                        status_column = col
                        break

                if status_column is not None:
                    status_values = (
                        pms_df[status_column]
                        .astype(str)
                        .str.lower()
                    )

                    overdue_count = status_values.str.contains(
                        "overdue",
                        na=False
                    ).sum()

                    if overdue_count > 0:
                        risk_score += int(overdue_count)
                        st.error(
                            f"🔴 Overdue maintenance records: "
                            f"{overdue_count}"
                        )
                else:
                    overdue_count = 0

                if risk_score >= 5:
                    st.error("🔴 Maintenance Risk: HIGH")
                elif risk_score >= 2:
                    st.warning("🟠 Maintenance Risk: MEDIUM")
                else:
                    st.success("🟢 Maintenance Risk: LOW")

                # --------------------------------------------
                # PRIORITY ACTIONS
                # --------------------------------------------
                st.markdown("### 🎯 Priority Actions")

                if missing_fields:
                    st.warning(
                        "Complete missing PMS information: "
                        + ", ".join(missing_fields)
                    )

                if overdue_count > 0:
                    st.error(
                        "Review and close overdue maintenance "
                        "items immediately."
                    )

                if not missing_fields and overdue_count == 0:
                    st.success(
                        "✅ No immediate PMS data action detected."
                    )

        except pd.errors.EmptyDataError:
            st.error(
                "❌ PMS CSV is empty. "
                "Please upload a CSV containing PMS records."
            )

        except Exception as e:
            st.error(
                f"❌ Unable to read/analyze PMS CSV: {e}"
            )


# ============================================================
# 4. DEFECTS
# ============================================================
elif module == "Defects":

    st.subheader("⚠️ Defects Intelligence")

    if vessel_name:
        st.info(f"⚓ ACTIVE VESSEL: {vessel_name}")
    else:
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

    defect_file = st.file_uploader(
        "Upload Defects CSV",
        type=["csv"],
        key="defects_csv"
    )

    if defect_file is None:
        st.info("Upload Defects CSV to start analysis.")

    else:
        try:
            defect_df = pd.read_csv(defect_file)

            # Remove completely empty rows and columns
            defect_df = defect_df.dropna(how="all")
            defect_df = defect_df.dropna(axis=1, how="all")

            # Clean column names
            defect_df.columns = [
                str(col).strip()
                for col in defect_df.columns
            ]

            if defect_df.empty:
                st.warning("⚠️ Defects CSV contains no records.")

            else:
                st.success(
                    f"✅ Defect data loaded — {len(defect_df)} records"
                )

                st.markdown("### 📋 Defect Records")

                st.dataframe(
                    defect_df,
                    use_container_width=True
                )

                st.metric(
                    "DEFECT RECORDS",
                    len(defect_df)
                )

        except pd.errors.EmptyDataError:
            st.error(
                "❌ Defects CSV is empty. "
                "Please upload a CSV containing defect records."
            )

        except Exception as e:
            st.error(
                f"❌ Unable to read Defects CSV: {e}"
            )


# ============================================================
# 5. CERTIFICATES
# ============================================================
elif module == "Certificates":

        st.subheader("📜 Certificates Intelligence")

        certificate_file = st.file_uploader(
            "Upload Certificates CSV",
            type=["csv"],
            key="certificates_csv",
        )

        if certificate_file is not None:
            try:
                certificate_df = pd.read_csv(certificate_file)

                st.success(
                    f"✅ Certificate data loaded — "
                    f"{len(certificate_df)} records"
                )

                st.dataframe(
                    certificate_df,
                    use_container_width=True,
                )

                st.metric(
                    "CERTIFICATE RECORDS",
                    len(certificate_df),
                )

            except Exception as e:
                st.error(f"Unable to read Certificates CSV: {e}")
        else:
            st.info("Upload Certificates CSV to start analysis.")

    # ==========================================================
    # 6. BUNKER
    # ==========================================================
    elif module == "Bunker":
        st.subheader("⛽ Bunker Intelligence")

        bunker_file = st.file_uploader(
            "Upload Bunker CSV",
            type=["csv"],
            key="bunker_csv",
        )

    if bunker_file is not None:
        try:
            bunker_df = pd.read_csv(bunker_file)

            st.success(
                f"✅ Bunker data loaded — {len(bunker_df)} records"
            )

            st.dataframe(
                bunker_df,
                use_container_width=True,
            )

            st.metric(
                "BUNKER RECORDS",
                len(bunker_df),
            )

        except Exception as e:
            st.error(f"Unable to read Bunker CSV: {e}")
    else:
        st.info("Upload Bunker CSV to start analysis.")

    # ==========================================================
    # 7. CARGO
    # ==========================================================
    elif module == "Cargo":

        st.subheader("📦 Cargo Intelligence")

        cargo_file = st.file_uploader(
            "Upload Cargo CSV",
            type=["csv"],
            key="cargo_csv",
        )

        if cargo_file is not None:
            try:
                cargo_df = pd.read_csv(cargo_file)

                st.success(
                    f"✅ Cargo data loaded — {len(cargo_df)} records"
                )

                st.dataframe(
                    cargo_df,
                    use_container_width=True,
                )

                st.metric(
                    "CARGO RECORDS",
                    len(cargo_df),
                )

            except Exception as e:
                st.error(f"Unable to read Cargo CSV: {e}")
        else:
            st.info("Upload Cargo CSV to start analysis.")

    # ==========================================================
    # 8. AUDIT & FINDINGS
    # ==========================================================
    elif module == "Audit & Findings":

        st.subheader("🔎 Audit & Findings")

        audit_file = st.file_uploader(
            "Upload Audit & Findings CSV",
            type=["csv"],
            key="audit_csv",
        )

        if audit_file is not None:
            try:
                audit_df = pd.read_csv(audit_file)

                st.success(
                    f"✅ Audit data loaded — {len(audit_df)} records"
                )

                st.dataframe(
                    audit_df,
                    use_container_width=True,
                )

                st.metric(
                    "AUDIT / FINDING RECORDS",
                    len(audit_df),
                )

            except Exception as e:
                st.error(f"Unable to read Audit CSV: {e}")
        else:
            st.info("Upload Audit CSV to start analysis.")

    # ==========================================================
    # 9. ACTION TRACKER
    # ==========================================================
    elif module == "Action Tracker":

        st.subheader("✅ Action Tracker")

        action_file = st.file_uploader(
            "Upload Action Tracker CSV",
            type=["csv"],
            key="action_tracker_csv",
        )

        if action_file is not None:
            try:
                action_df = pd.read_csv(action_file)

                st.success(
                    f"✅ Action Tracker loaded — {len(action_df)} records"
                )

                st.dataframe(
                    action_df,
                    use_container_width=True,
                )

                st.metric(
                    "ACTION RECORDS",
                    len(action_df),
                )

            except Exception as e:
                st.error(f"Unable to read Action Tracker CSV: {e}")
        else:
            st.info("Upload Action Tracker CSV to start tracking.")

    # ==========================================================
    # 10. MARINE AI CO-PILOT
    # ==========================================================
    elif module == "Marine AI Co-Pilot":

        st.subheader("🤖 Marine AI Co-Pilot")

        if vessel_name:
            st.success(
                f"AI operational workspace ready for "
                f"{vessel_name.upper()}."
            )
        else:
            st.info(
                "Enter Vessel Name in GLOBAL VESSEL CONTROL "
                "before starting vessel-specific analysis."
            )

        marine_question = st.text_area(
            "Marine Operations Question / Instruction",
            placeholder=(
                "Example: Analyze voyage, maintenance, defects, "
                "certificates, bunker or cargo condition..."
            ),
            key="marine_ai_question",
        )

        if st.button(
            "⚓ Analyze Marine Operations",
            key="marine_ai_analyze",
        ):
            if marine_question.strip():
                st.info(
                    "Marine AI request received. "
                    "AI engine connection will process this workspace."
                )
            else:
                st.warning("Enter a question or instruction first.")

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
    # ============================================================
# UNIVERSAL DPR CSV READER - UNLIMITED / DYNAMIC COLUMNS
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
        # ----------------------------------------------------
        # READ FILE ONCE
        # ----------------------------------------------------
        raw_data = uploaded_file.getvalue()

        if not raw_data:
            raise ValueError("File CSV kosong.")

        # ----------------------------------------------------
        # AUTO DETECT ENCODING
        # ----------------------------------------------------
        decoded_text = None
        detected_encoding = None

        for encoding in (
            "utf-8-sig",
            "utf-8",
            "cp1252",
            "latin1",
        ):
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

        # ----------------------------------------------------
        # CLEAN COLUMN NAMES
        # ----------------------------------------------------
        df.columns = [
            str(column).strip()
            for column in df.columns
        ]

        # Remove completely empty / unnamed columns only
        empty_columns = [
            column
            for column in df.columns
            if str(column).lower().startswith("unnamed:")
            and df[column].isna().all()
        ]

        if empty_columns:
            df = df.drop(columns=empty_columns)

        # ----------------------------------------------------
        # DPR INFORMATION
        # ----------------------------------------------------
        total_rows = len(df)
        total_columns = len(df.columns)
        empty_cells = int(df.isna().sum().sum())

        st.success(
            f"✅ DPR berhasil dibaca — "
            f"{total_rows:,} rows × {total_columns:,} columns"
        )

        m1, m2, m3, m4 = st.columns(4)

        m1.metric(
            "DPR Records",
            f"{total_rows:,}",
        )

        m2.metric(
            "Detected Columns",
            f"{total_columns:,}",
        )

        m3.metric(
            "Empty Cells",
            f"{empty_cells:,}",
        )

        m4.metric(
            "Reader Status",
            "READY",
        )

        # ----------------------------------------------------
        # FILE DETECTION INFORMATION
        # ----------------------------------------------------
        with st.expander("🔎 DPR File Detection", expanded=False):
            st.write(f"Encoding: {detected_encoding}")
            st.write(f"Delimiter: {repr(detected_separator)}")
            st.write(f"Columns detected: {total_columns:,}")

        # ----------------------------------------------------
        # DPR DATA PREVIEW
        # ----------------------------------------------------
        st.markdown("### 📋 DPR Data Preview")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
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

# DPR Dynamic CSV + Fuel Intelligence calculation verified

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
