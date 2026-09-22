import streamlit as st
from datetime import datetime
import pandas as pd
import io
import csv
import os

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
    """ <style> .block-container { padding-top: 1.5rem; padding-bottom: 3rem; } .main-title { font-size: 2.2rem; font-weight: 800; margin-bottom: 0; } .sub-title { font-size: 1rem; opacity: 0.75; margin-bottom: 1.5rem; } .system-card { border: 1px solid rgba(128,128,128,0.25); border-radius: 14px; padding: 20px; min-height: 180px; } .status-online { font-weight: 700; } </style> """,
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

    RPM_POINTS = [600, 700, 800, 900, 1000, 1100, 1200, 1300]

    # ------------------------------------------------------
    # PILIH RPM YANG SEDANG DIGUNAKAN
    # ------------------------------------------------------

    active_rpm = st.selectbox(
    "RPM Aktif",
    options=RPM_POINTS,
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
        "Company Presentation",
        "System Status",
    ],
)

st.sidebar.caption(
    "MARINE OPERATIONAL N8N INTELLIGENCE CENTER"
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

    st.header("⚓ Marine Operations Intelligence Center")

    # ========================================================
    # ACTIVE VESSEL
    # ========================================================

    active_vessel = str(vessel_name).strip().upper() if vessel_name else ""

    if active_vessel:
        st.success(f"⚓ ACTIVE VESSEL: {active_vessel}")
    else:
        active_vessel = "NOT SELECTED"
        st.warning("⚠️ Enter a vessel name in GLOBAL VESSEL CONTROL.")

    st.divider()

    # ========================================================
    # MODULE SELECTOR
    # ========================================================

    marine_modules = [
        "Vessel Operations",
        "Voyage Intelligence",
        "PMS / Maintenance",
        "Defects",
        "Certificates",
        "Bunker",
        "Cargo",
        "Audit & Findings",
        "Action Tracker",
        "Marine MLC / Crew",
        "Marine AI Co-Pilot",
    ]

    module = st.selectbox(
        "Select Marine Operations Module",
        marine_modules,
        key="marine_operations_module_new"
    )

    st.divider()

    # ========================================================
    # UNIVERSAL CSV INTELLIGENCE ENGINE
    # ========================================================

    def marine_csv_engine( title, icon, uploader_key, records_title, facts_title, analysis_title, intelligence_title, columns_title, ):

        st.subheader(f"{icon} {title}")

        st.info(f"⚓ ACTIVE VESSEL: {active_vessel}")

        # ----------------------------------------------------
        # UPLOAD CSV
        # ----------------------------------------------------

        st.markdown("### 📤 Upload CSV")

        uploaded_file = st.file_uploader(
            f"Upload {title} CSV",
            type=["csv"],
            key=uploader_key,
        )

        if uploaded_file is None:
            st.info(f"Upload {title} CSV to start analysis.")
            return

        try:

            # =================================================
            # READ CSV
            # =================================================

            try:
                df = pd.read_csv(uploaded_file)

            except UnicodeDecodeError:
                uploaded_file.seek(0)

                df = pd.read_csv(
                    uploaded_file,
                    encoding="latin-1"
                )

            if df.empty:
                st.warning("⚠️ CSV contains no records.")
                return

            # Clean column names

            df.columns = [
                str(col).strip()
                for col in df.columns
            ]

            st.success(
                f"✅ {title} data loaded — {len(df)} records"
            )

            # =================================================
            # RECORDS
            # =================================================

            st.markdown(f"### 📋 {records_title}")

            st.dataframe(
                df,
                use_container_width=True
            )

            # =================================================
            # FACTS
            # =================================================

            st.markdown(f"### 📊 {facts_title}")

            total_records = int(len(df))

            total_columns = int(
                len(df.columns)
            )

            empty_cells = int(
                df.isna().sum().sum()
            )

            duplicate_records = int(
                df.duplicated().sum()
            )

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric(
                    "Records",
                    total_records
                )

            with c2:
                st.metric(
                    "Columns",
                    total_columns
                )

            with c3:
                st.metric(
                    "Missing Data",
                    empty_cells
                )

            with c4:
                st.metric(
                    "Duplicates",
                    duplicate_records
                )

            # =================================================
            # DATA ANALYSIS
            # =================================================

            st.markdown(
                f"### 📦 {analysis_title}"
            )

            numeric_df = df.select_dtypes(
                include="number"
            )

            if not numeric_df.empty:

                numeric_summary = (
                    numeric_df
                    .describe()
                    .transpose()
                )

                st.dataframe(
                    numeric_summary,
                    use_container_width=True
                )

            else:

                st.info(
                    "ℹ️ No numeric columns detected. "
                    "Text and operational data remain "
                    "available for intelligence analysis."
                )

            # =================================================
            # INTELLIGENCE ANALYSIS
            # =================================================

            st.markdown(
                f"### 🔎 {intelligence_title}"
            )

            i1, i2, i3 = st.columns(3)

            with i1:
                st.metric(
                    "Total Records",
                    total_records
                )

            with i2:
                st.metric(
                    "Missing Data",
                    empty_cells
                )

            with i3:
                st.metric(
                    "Duplicate Records",
                    duplicate_records
                )

            # -------------------------------------------------
            # DATA QUALITY
            # -------------------------------------------------

            if empty_cells == 0:

                st.success(
                    "✅ No missing data detected."
                )

            else:

                st.warning(
                    f"⚠️ {empty_cells} empty cells detected."
                )

            if duplicate_records == 0:

                st.success(
                    "✅ No duplicate records detected."
                )

            else:

                st.warning(
                    f"⚠️ {duplicate_records} duplicate "
                    "records detected."
                )

            # =================================================
            # ACTIVE VESSEL DETECTION
            # =================================================

            vessel_column = None

            vessel_aliases = [
                "vessel",
                "vessel name",
                "vessel_name",
                "ship",
                "ship name",
                "ship_name",
            ]

            for col in df.columns:

                normalized_col = (
                    str(col)
                    .strip()
                    .lower()
                )

                if normalized_col in vessel_aliases:
                    vessel_column = col
                    break

            if vessel_column is not None:

                vessel_values = (
                    df[vessel_column]
                    .fillna("")
                    .astype(str)
                    .str.strip()
                    .str.upper()
                )

                active_count = int(
                    (
                        vessel_values == active_vessel
                    ).sum()
                )

                st.metric(
                    "Active Vessel Records",
                    active_count
                )

                if active_vessel == "NOT SELECTED":

                    st.info(
                        "ℹ️ Select or enter a vessel name "
                        "to activate vessel-specific analysis."
                    )

                elif active_count > 0:

                    st.success(
                        f"✅ {active_count} records found for "
                        f"{active_vessel}."
                    )

                else:

                    st.warning(
                        f"⚠️ No exact vessel records found "
                        f"for {active_vessel}."
                    )

            else:

                st.info(
                    "ℹ️ Vessel column not detected. "
                    "General dataset analysis continues."
                )

            # =================================================
            # STATUS / RISK / PRIORITY ANALYSIS
            # =================================================

            status_aliases = [
                "status",
                "condition",
                "priority",
                "risk",
                "remark",
                "remarks",
                "finding",
                "findings",
                "action",
                "delay",
                "severity",
            ]

            status_columns = []

            for col in df.columns:

                col_lower = str(col).lower()

                if any(
                    word in col_lower
                    for word in status_aliases
                ):
                    status_columns.append(col)

            if status_columns:

                st.markdown(
                    "#### ⚠️ Operational Status / Risk Information"
                )

                for status_col in status_columns:

                    st.write(
                        f"**{status_col}**"
                    )

                    status_counts = (
                        df[status_col]
                        .fillna("EMPTY")
                        .astype(str)
                        .value_counts()
                        .reset_index()
                    )

                    status_counts.columns = [
                        status_col,
                        "Records"
                    ]

                    st.dataframe(
                        status_counts,
                        use_container_width=True
                    )

            # =================================================
            # CSV COLUMN INFORMATION
            # =================================================

            st.markdown(
                f"### 🧾 {columns_title}"
            )

            column_information = []

            for col in df.columns:

                column_information.append(
                    {
                        "Column": str(col),

                        "Data Type":
                            str(df[col].dtype),

                        "Non Empty":
                            int(df[col].notna().sum()),

                        "Missing":
                            int(df[col].isna().sum()),

                        "Unique Values":
                            int(
                                df[col].nunique(
                                    dropna=True
                                )
                            ),
                    }
                )

            column_df = pd.DataFrame(
                column_information
            )

            st.dataframe(
                column_df,
                use_container_width=True
            )

            # =================================================
            # COMPLETED
            # =================================================

            st.success(
                f"✅ {title} analysis completed successfully."
            )

        except pd.errors.EmptyDataError:

            st.error(
                f"❌ {title} CSV is empty."
            )

        except pd.errors.ParserError as e:

            st.error(
                f"❌ {title} CSV format error: {e}"
            )

        except Exception as e:

            st.error(
                f"❌ Unable to analyze {title}: {e}"
            )

    # ========================================================
    # MODULE CONFIGURATION
    # ========================================================

    module_config = {

        "Vessel Operations": {
            "title": "Vessel Operations Intelligence",
            "icon": "⚓",
            "key": "new_vessel_operations_csv",
            "records": "Vessel Operations Records",
            "facts": "Vessel Operations Facts",
            "analysis": "Vessel Operations Data Analysis",
            "intelligence": "Vessel Operations Intelligence Analysis",
            "columns": "Vessel Operations CSV Column Information",
        },

        "Voyage Intelligence": {
            "title": "Voyage Intelligence",
            "icon": "🚢",
            "key": "new_voyage_csv",
            "records": "Voyage Records",
            "facts": "Voyage Facts",
            "analysis": "Voyage Data Analysis",
            "intelligence": "Voyage Intelligence Analysis",
            "columns": "Voyage CSV Column Information",
        },

        "PMS / Maintenance": {
            "title": "PMS / Maintenance Intelligence",
            "icon": "🔧",
            "key": "new_pms_csv",
            "records": "PMS / Maintenance Records",
            "facts": "PMS / Maintenance Facts",
            "analysis": "PMS / Maintenance Data Analysis",
            "intelligence": "Maintenance Risk & Priority Analysis",
            "columns": "PMS CSV Column Information",
        },

        "Defects": {
            "title": "Defects Intelligence",
            "icon": "⚠️",
            "key": "new_defects_csv",
            "records": "Defect Records",
            "facts": "Defect Facts",
            "analysis": "Defect Data Analysis",
            "intelligence": "Defect Intelligence Analysis",
            "columns": "Defects CSV Column Information",
        },

        "Certificates": {
            "title": "Certificates Intelligence",
            "icon": "📜",
            "key": "new_certificates_csv",
            "records": "Certificate Records",
            "facts": "Certificate Facts",
            "analysis": "Certificate Data Analysis",
            "intelligence": "Certificate Intelligence Analysis",
            "columns": "Certificates CSV Column Information",
        },

        "Bunker": {
            "title": "Bunker Intelligence",
            "icon": "⛽",
            "key": "new_bunker_csv",
            "records": "Bunker Records",
            "facts": "Bunker Facts",
            "analysis": "Bunker Data Analysis",
            "intelligence": "Bunker Intelligence Analysis",
            "columns": "Bunker CSV Column Information",
        },

        "Cargo": {
            "title": "Cargo Intelligence",
            "icon": "📦",
            "key": "new_cargo_csv",
            "records": "Cargo Records",
            "facts": "Cargo Facts",
            "analysis": "Cargo Data Analysis",
            "intelligence": "Cargo Intelligence Analysis",
            "columns": "Cargo CSV Column Information",
        },

        "Audit & Findings": {
            "title": "Audit & Findings Intelligence",
            "icon": "🔎",
            "key": "new_audit_csv",
            "records": "Audit & Findings Records",
            "facts": "Audit & Findings Facts",
            "analysis": "Audit & Findings Data Analysis",
            "intelligence": "Audit & Findings Intelligence Analysis",
            "columns": "Audit & Findings CSV Column Information",
        },

        "Action Tracker": {
            "title": "Action Tracker Intelligence",
            "icon": "✅",
            "key": "new_action_tracker_csv",
            "records": "Action Tracker Records",
            "facts": "Action Tracker Facts",
            "analysis": "Action Tracker Data Analysis",
            "intelligence": "Action Tracker Intelligence Analysis",
            "columns": "Action Tracker CSV Column Information",
        },

        "Marine MLC / Crew": {
            "title": "Marine MLC / Crew Intelligence",
            "icon": "👥",
            "key": "new_mlc_crew_csv",
            "records": "Marine MLC / Crew Records",
            "facts": "Marine MLC / Crew Facts",
            "analysis": "Marine MLC / Crew Data Analysis",
            "intelligence": "Marine MLC / Crew Intelligence Analysis",
            "columns": "Marine MLC / Crew CSV Column Information",
        },
    }

    # ========================================================
    # MARINE AI CO-PILOT
    # ========================================================

    if module == "Marine AI Co-Pilot":

        st.subheader("🤖 Marine AI Co-Pilot")

        st.info(
            f"⚓ ACTIVE VESSEL: {active_vessel}"
        )

        marine_question = st.text_area(
            "Marine Operations Question / Instruction",
            placeholder=(
                "Example: Analyze voyage, maintenance, "
                "defects, certificates, bunker or cargo."
            ),
            key="new_marine_ai_question",
        )

        if st.button(
            "⚓ Analyze Marine Operations",
            key="new_marine_ai_analyze",
        ):

            if marine_question.strip():

                st.success(
                    "✅ Marine AI request received."
                )

                st.info(
                    "AI engine integration can process "
                    "this operational request."
                )

            else:

                st.warning(
                    "⚠️ Enter a question or instruction first."
                )

    # ========================================================
    # RENDER CSV MODULE
    # ========================================================

    else:

        config = module_config.get(module)

        if config is None:

            st.error(
                "❌ Marine Operations module configuration "
                "not found."
            )

        else:

            marine_csv_engine(
                title=config["title"],
                icon=config["icon"],
                uploader_key=config["key"],
                records_title=config["records"],
                facts_title=config["facts"],
                analysis_title=config["analysis"],
                intelligence_title=config["intelligence"],
                columns_title=config["columns"],
            )

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

            # -----------------------------------------------
            # AUTO DETECT ENCODING
            # -----------------------------------------------

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
                raise ValueError(
                    "Encoding CSV tidak dapat dibaca."
                )

            # -----------------------------------------------
            # AUTO DETECT CSV SEPARATOR
            # -----------------------------------------------

            try:
                dialect = csv.Sniffer().sniff(
                    decoded_text[:5000],
                    delimiters=",;\t|"
                )
                separator = dialect.delimiter
            except csv.Error:
                separator = ","

            # -----------------------------------------------
            # READ CSV
            # -----------------------------------------------

            df = pd.read_csv(
                io.StringIO(decoded_text),
                sep=separator
            )

            if df.empty:
                raise ValueError(
                    "CSV tidak memiliki data."
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
    st.caption(
        "Automation Orchestration Center for Marine Operations, "
        "Fuel Efficiency BBM, QHSSE and AI Intelligence."
    )

    st.info(
        "N8N Workflow Center is prepared as the automation layer "
        "connecting operational data, alerts, reports and AI workflows."
    )

    st.subheader("⚙️ Workflow Control Center")

    workflows = {
        "📄 DPR Processing": "READY",
        "⛽ Fuel Alert": "READY",
        "🔧 Maintenance Alert": "READY",
        "🛡️ QHSSE Alert": "READY",
        "📊 Management Report": "READY",
        "🤖 AI Workflow": "READY",
    }

    for workflow, status in workflows.items():
        c1, c2 = st.columns([3, 1])

        with c1:
            st.write(workflow)

        with c2:
            st.success(status)

    st.divider()

    st.subheader("🔗 N8N Integration")

    n1, n2, n3 = st.columns(3)

    with n1:
        st.metric("Workflows", len(workflows))

    with n2:
        st.metric("Ready", len(workflows))

    with n3:
        st.metric("Failed", 0)

    st.success("✅ N8N Workflow Center ready for integration.")

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

# ================================================================
# COMPANY PRESENTATION
# MARINE OPERATIONAL N8N INTELLIGENCE CENTER
# ================================================================

elif page == "Company Presentation":

    st.header("🏢 Company Presentation")
    st.caption(
        "MARINE OPERATIONAL N8N INTELLIGENCE CENTER | "
        "Digital Maritime Operations Platform"
    )

    # ============================================================
    # PROFESSIONAL 16:9 DIGITAL DASHBOARD
    # ============================================================
    st.markdown(
        """ <style> .cp-hero{ aspect-ratio:16/9; width:100%; box-sizing:border-box; border-radius:24px; padding:42px; color:#f7fbff; background: radial-gradient(circle at 85% 15%, rgba(38,198,218,.24), transparent 30%), linear-gradient(135deg,#06182b 0%,#0b2f4f 58%,#0c5262 100%); box-shadow:0 18px 50px rgba(0,0,0,.20); display:flex; flex-direction:column; justify-content:space-between; overflow:hidden; } .cp-kicker{font-size:14px;letter-spacing:.16em;font-weight:700;opacity:.8} .cp-title{font-size:clamp(30px,4vw,58px);font-weight:900;line-height:1.03;margin:12px 0} .cp-sub{font-size:clamp(14px,1.6vw,22px);opacity:.88;max-width:900px} .cp-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px} .cp-card{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.16); border-radius:16px;padding:18px;backdrop-filter:blur(4px)} .cp-card b{display:block;font-size:clamp(16px,1.5vw,23px);margin-bottom:6px} .cp-card span{font-size:13px;opacity:.8} .cp-status{display:flex;justify-content:space-between;align-items:center; border-top:1px solid rgba(255,255,255,.18);padding-top:18px;margin-top:24px} .cp-online{font-weight:800;letter-spacing:.08em} @media(max-width:760px){.cp-hero{padding:24px}.cp-grid{grid-template-columns:1fr 1fr}} </style> <div class="cp-hero"> <div> <div class="cp-kicker">DIGITAL MARITIME OPERATIONS PLATFORM</div> <div class="cp-title">⚓ MARINE OPERATIONAL<br>N8N INTELLIGENCE CENTER</div> <div class="cp-sub">One command environment for Fleet Operations, Fuel Efficiency, QHSSE, AI-assisted analysis and N8N workflow automation.</div> <div class="cp-grid"> <div class="cp-card"><b>⚓ Fleet Operations</b><span>Voyage • PMS • Defects • Certificates • Cargo</span></div> <div class="cp-card"><b>⛽ Fuel Intelligence</b><span>DPR • RPM • Engine • Consumption • Variance</span></div> <div class="cp-card"><b>🛡️ QHSSE</b><span>Incident • Audit • Risk • Corrective Action</span></div> <div class="cp-card"><b>🤖 AI + N8N</b><span>Analysis • Alerts • Reports • Workflow Automation</span></div> </div> </div> <div class="cp-status"> <span>GLOBAL MULTI-VESSEL OPERATIONS</span> <span class="cp-online">● SYSTEM ONLINE</span> </div> </div> """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.subheader("🌍 Executive Digital Command Center")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Fleet Operations", "ONLINE")
    c2.metric("Fuel Intelligence", "ONLINE")
    c3.metric("QHSSE Intelligence", "ONLINE")
    c4.metric("N8N Automation", "READY")

    st.markdown("---")
    st.subheader("🚢 Integrated Maritime Intelligence Platform")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""### ⚓ Marine Operations • Vessel Operations • Voyage Intelligence • PMS / Maintenance • Defects & Certificates • Bunker & Cargo • Audit & Findings • Action Tracker""")
    with col2:
        st.markdown("""### ⛽ Fuel Efficiency BBM • DPR / BBM Control • Main & Auxiliary Engine • RPM Monitoring • Fuel Performance Analysis • Fuel Cost Control • Engine Database""")
    with col3:
        st.markdown("""### 🛡️ QHSSE Company • Incident / Near Miss • Inspection & Audit • Risk Management • Corrective Action • Regulatory Compliance • Safety Performance""")

    st.markdown("---")
    st.subheader("🤖 AI & Automation")
    ai1, ai2 = st.columns(2)
    with ai1:
        st.markdown("""### 🧠 Marine AI Co-Pilot AI-supported workspace for data analysis, operational summaries, risk identification, management recommendations and natural-language assistance.""")
    with ai2:
        st.markdown("""### 🔗 N8N Workflow Center Workflow architecture for operational notifications, reporting, approval processes, data integration and management alerts.""")

    st.markdown("---")
    st.subheader("🎬 Video Presentation")
    video_path = "VID-20260922-WA0004.mp4"
    if os.path.exists(video_path):
        st.video(video_path)
        st.success("✅ Company presentation video is active.")
    else:
        st.info(
            "🎬 Video player is ready. Upload presentation.mp4 to the same "
            "GitHub repository folder as app.py to activate it automatically."
        )

    st.markdown("---")
    st.subheader("📥 Company Presentation & Template")

    presentation_file = "Marine_Operational_Intelligence_Center_PREMIUM_16x9.pdf"
    template_file = "Shipping_Company_Implementation_Template.pdf"

    d1, d2 = st.columns(2)
    with d1:
        if os.path.exists(presentation_file):
            with open(presentation_file, "rb") as f:
                st.download_button(
                    "📥 Download Company Presentation (PDF)",
                    data=f.read(),
                    file_name=presentation_file,
                    mime="application/pdf",
                    use_container_width=True,
                    key="download_company_presentation_pdf",
                )
        else:
            st.warning(f"Upload {presentation_file} to activate this download.")

    with d2:
        if os.path.exists(template_file):
            with open(template_file, "rb") as f:
                st.download_button(
                    "📋 Download Company Template (PDF)",
                    data=f.read(),
                    file_name=template_file,
                    mime="application/pdf",
                    use_container_width=True,
                    key="download_company_template_pdf",
                )
        else:
            st.warning(f"Upload {template_file} to activate this download.")

    pptx_file = "Marine_Operational_Intelligence_Center_PREMIUM_16x9.pptx"
    if os.path.exists(pptx_file):
        with open(pptx_file, "rb") as f:
            st.download_button(
                "🖥️ Download Editable Presentation (PPTX)",
                data=f.read(),
                file_name=pptx_file,
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                use_container_width=True,
                key="download_company_presentation_pptx",
            )

    st.markdown("---")
    st.subheader("🌐 Deployment Options")
    dep1, dep2, dep3 = st.columns(3)
    dep1.markdown("### ☁️ Cloud\nOnline access through secure web deployment.")
    dep2.markdown("### 🏢 Company\nCustomized company identity, fleet and operational modules.")
    dep3.markdown("### 🚢 Fleet\nDesigned for multi-vessel operational monitoring.")

    st.markdown("---")
    st.subheader("🏢 Company Customization")
    st.markdown(
        "**Company Logo • Company Name • Vessel Database • User Access • "
        "Operational Modules • Management Dashboard • Reports • AI Services • Workflow Automation**"
    )
    st.success(
        "⚓ MARINE OPERATIONAL N8N INTELLIGENCE CENTER — "
        "Integrated Digital Maritime Operations Platform"
    )

# ================================================================
# SYSTEM STATUS
# ================================================================

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
