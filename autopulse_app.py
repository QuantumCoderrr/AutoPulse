import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime

# --- PAGE CONFIGURATION (Makes it look wide and professional) ---
st.set_page_config(
    page_title="AutoPulse AI | Intelligent Automotive Ecosystem",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR "STUNNING" LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stMetric {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #41444C;
    }
    h1, h2, h3 {
        color: #FF4B4B; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (To remember data between clicks) ---
if 'booking_confirmed' not in st.session_state:
    st.session_state.booking_confirmed = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3209/3209265.png", width=100) # Placeholder logo
    st.title("AutoPulse AI")
    st.markdown("---")
    user_role = st.radio("Select User View:", 
        ["🚗 Vehicle Owner", "🛠️ Service Center", "🏭 OEM / Manufacturer"])
    
    st.markdown("---")
    st.info("System Status: **Online**")
    st.caption("Agentic Orchestration: Active")
    st.caption("v1.0.2-Beta")

# ==========================================
# VIEW 1: VEHICLE OWNER (The Mobile App Experience)
# ==========================================
if user_role == "🚗 Vehicle Owner":
    st.title("👋 Welcome, Sandip")
    st.subheader("Vehicle Health Monitor: Tata Harrier (WB-02-AK-1234)")
    
    # Simulate Live Data
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Engine Temp", value="105°C", delta="High Risk", delta_color="inverse")
    with col2:
        st.metric(label="Battery Health", value="88%", delta="Good")
    with col3:
        st.metric(label="Tire Pressure", value="32 PSI", delta="Normal")
    with col4:
        st.metric(label="Oil Life", value="12%", delta="-5%", delta_color="inverse")

    st.markdown("---")

    # The "Agentic AI" Interface
    col_chat, col_action = st.columns([2, 1])

    with col_chat:
        st.subheader("💬 AutoPulse Voice/Chat Assistant")
        
        # Chat container
        chat_container = st.container()
        
        # Hardcoded "AI" logic for the demo
        with chat_container:
            st.chat_message("assistant").write("⚠️ **Alert:** I have detected an anomaly in your engine coolant temperature. It is rising 15% faster than normal.")
            
            # If the user has already booked, show the confirmation
            if st.session_state.booking_confirmed:
                st.chat_message("user").write("Book an appointment.")
                st.chat_message("assistant").write("✅ **Done.** Appointment scheduled at **AutoCare Kolkata** for **Tomorrow at 10:00 AM**. Towing service is on standby if needed.")
            
            # Simulated User Input (Buttons instead of typing for speed)
            elif not st.session_state.booking_confirmed:
                if st.button("Simulate Voice Command: 'What should I do?'"):
                    with st.spinner("Analyzing telemetry..."):
                        time.sleep(1.5) # Fake processing delay
                        st.chat_message("user").write("What should I do?")
                        st.chat_message("assistant").write("Based on the sensor data, this is likely a **Thermostat Failure**. Driving further may cause permanent engine damage. \n\nI can book a service slot at **AutoCare Kolkata (2km away)**. They have the spare part in stock.")

    with col_action:
        st.subheader("⚡ Quick Actions")
        if not st.session_state.booking_confirmed:
            st.warning("Action Required: Engine Overheating")
            if st.button("🤖 Auto-Schedule Repair", type="primary"):
                with st.spinner("Contacting Service Agent..."):
                    time.sleep(2)
                    st.session_state.booking_confirmed = True
                    st.rerun()
        else:
            st.success("✅ Appointment Confirmed")
            st.info("**Token:** #AP-9982")
            st.markdown("**Location:** AutoCare Kolkata")
            st.markdown("**Time:** 10:00 AM, Tomorrow")

# ==========================================
# VIEW 2: SERVICE CENTER (The Dashboard)
# ==========================================
elif user_role == "🛠️ Service Center":
    st.title("🛠️ Service Center Operations")
    st.subheader("Incoming Autonomous Bookings")

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Predicted Arrivals", "12", "+2")
    m2.metric("Parts Pre-Ordered", "85%", "+10%")
    m3.metric("Technician Utilization", "92%", "Optimized")

    # Dataframe simulating the booking made in Tab 1
    data = {
        "Token ID": ["AP-9980", "AP-9981", "AP-9982"],
        "Customer": ["Amit Sharma", "Priya Das", "Sandip Ghosh"],
        "Vehicle": ["Honda City", "Hyundai Creta", "Tata Harrier"],
        "Issue (AI Predicted)": ["Brake Pad Wear", "Battery Voltage Low", "Engine Overheating (Thermostat)"],
        "Urgency": ["Medium", "Low", "Critical"],
        "Parts Status": ["Ready", "Ready", "Allocated via AutoPulse"],
        "Time": ["09:00 AM", "09:30 AM", "10:00 AM"]
    }
    df = pd.DataFrame(data)

    # Highlight the Critical row
    def highlight_critical(val):
        color = '#ff4b4b' if val == 'Critical' else ''
        return f'background-color: {color}'

    st.dataframe(df.style.applymap(highlight_critical, subset=['Urgency']), use_container_width=True)
    
    st.markdown("### 🤖 Agent Logs")
    st.code("""
    [10:42:01] MASTER_AGENT: Received telemetry from Tata Harrier (WB-02-AK-1234)
    [10:42:02] DIAGNOSTIC_AGENT: Fault Code P0128 detected (Thermostat).
    [10:42:05] SCHEDULING_AGENT: Checked inventory for Part #TH-99. Status: Available.
    [10:42:06] SCHEDULING_AGENT: Slot booked for 10:00 AM.
    """, language="bash")

# ==========================================
# VIEW 3: MANUFACTURING / OEM (RCA Insights)
# ==========================================
elif user_role == "🏭 OEM / Manufacturer":
    st.title("🏭 Manufacturing Intelligence (RCA/CAPA)")
    st.markdown("Feedback loop from Field Data to R&D Teams")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Recurring Defect Analysis")
        # Dummy data for the chart
        chart_data = pd.DataFrame({
            "Component": ["Thermostat", "Fuel Pump", "Brake Sensor", "AC Compressor", "Clutch Assembly"],
            "Failures (Last 30 Days)": [145, 89, 45, 30, 22]
        })
        
        fig = px.bar(chart_data, x="Component", y="Failures (Last 30 Days)", 
                     color="Failures (Last 30 Days)", 
                     color_continuous_scale="Reds",
                     title="Top Failing Components (Field Data)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("AI Recommendations")
        st.warning("⚠️ Critical Alert: Thermostat")
        st.info("**Issue:** Premature failure in Batch #2024-Q1.")
        st.info("**Root Cause:** Plastic housing cracking under high heat.")
        st.success("**CAPA Suggestion:** Upgrade material to Reinforced Polymer (Grade X7).")
        
        st.markdown("---")
        st.button("📩 Send CAPA Report to Engineering")