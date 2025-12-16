# 🚗 AutoPulse AI
### *Redefining Automotive Reliability with Agentic AI*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Prototype-success?style=for-the-badge)]()

**Team MotorCoderrrs** | **EY Techathon 6.0 Submission**

---

## 📖 Executive Summary
**AutoPulse AI** is an intelligent ecosystem that transforms vehicle maintenance from **reactive to proactive**. By leveraging Agentic AI, we enable vehicles to "think" and "act"—predicting mechanical failures before they happen, autonomously scheduling repairs with service centers, and providing critical Root Cause Analysis (RCA) data back to manufacturers to fix design defects.

---

## 🚩 Problem Statement
The current automotive maintenance lifecycle is broken:
1.  **Vehicle Owners** face unexpected breakdowns and safety hazards.
2.  **Service Centers** suffer from inefficient manual scheduling and uneven workload.
3.  **OEMs (Manufacturers)** lack real-time field data to identify and fix recurring design flaws.

---

## 💡 Solution Overview
AutoPulse AI bridges these gaps using a multi-agent orchestration layer:

### 1. 🚗 For Vehicle Owners (Mobile App View)
**Predictive Alerts:** Real-time warnings for "Engine Overheating" or "Battery Failure" before breakdown occurs.
**Agentic Assistance:** A Voice/Chat bot that answers queries ("What should I do?") and handles logistics.
**One-Click Booking:** Autonomous negotiation with service centers for the best available slot.

### 2. 🛠️ For Service Centers (Dashboard View)
**Autonomous Inflow:** Bookings appear automatically with pre-diagnosed issues.
**Parts Prediction:** Inventory is allocated before the vehicle arrives, reducing turnaround time.

### 3. 🏭 For OEMs (Manufacturing View)
**Closed-Loop Feedback:** Field failure data is aggregated to identify recurring defects.
**Automated CAPA:** The system generates Corrective Action/Preventive Action reports for R&D teams.

---

## ⚙️ Tech Stack
**Prototype (Current Submission):**
* **Language:** Python 3.10
* **Frontend/UI:** Streamlit (Simulating Mobile, Web, and Analytics Dashboards)
* **Visualization:** Plotly & Pandas

**Proposed Architecture (Full Scale):**
**AI Framework:** LangGraph / CrewAI (for multi-agent orchestration).
**ML Models:** LSTM & Isolation Forest (for anomaly detection).
**Backend:** FastAPI & PostgreSQL.

---

## 🚀 How to Run Locally

### Prerequisites
* Python 3.10 or higher installed.

### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/quantumcoderrr/autopulse.git
    cd autopulse
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the application:
    ```bash
    streamlit run autopulse_app.py
    ```

---

## 📸 Screenshots / Prototype Video

*(Add your video link or screenshots here)*
* [https://autopulse-lq6sc7u3truuqgn6tt8szq.streamlit.app](#)

---

## 👥 Team MotorCoderrrs

| Name | Role | College |
| :--- | :--- | :--- |
| **Sandip Ghosh** | System Architect & AI/ML Integration | St. Thomas' College of Engineering & Technology |
| **Sandhita Poddar** | UI/UX & Frontend Developer | St. Thomas' College of Engineering & Technology |
| **Abhirup Raha** | Backend & Data Integration | St. Thomas' College of Engineering & Technology |
