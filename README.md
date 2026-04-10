# 🚀 SDN Port Status Monitoring Tool (POX + Mininet)

## 📌 Overview
This project implements a **Software Defined Networking (SDN)** based Port Status Monitoring Tool using **Mininet** and **POX Controller**.

The system detects and logs **switch port status changes (UP/DOWN)** in real-time and demonstrates controller-switch interaction using OpenFlow.

---

## 🎯 Objective
- Monitor switch port status dynamically
- Detect port UP/DOWN events
- Log and display alerts
- Demonstrate SDN controller behavior

---

## 🧠 Key Concepts
- Software Defined Networking (SDN)
- OpenFlow Protocol
- POX Controller
- Event-driven networking (PortStatus, PacketIn)

---

## 🏗️ Architecture

Mininet (Topology)  
⬇  
OpenFlow Switch  
⬇  
POX Controller  
⬇  
Port Monitoring Logic  

---

## ⚙️ Technologies Used
- Python
- Mininet
- POX Controller
- OpenFlow Protocol

---

## 🛠️ Commands Used

# ================================
# SDN PORT MONITORING PROJECT RUN
# ================================

# STEP 1: Go to POX directory
cd ~/pox

# STEP 2: Start POX Controller with OpenFlow + your module
./pox.py openflow.of_01 misc.port_monitor
# This starts the controller and loads your port monitoring logic

# --------------------------------
# OPEN NEW TERMINAL (IMPORTANT)
# --------------------------------

# STEP 3: Clean Mininet (if needed)
sudo mn -c
# Removes old/stuck network configurations

# STEP 4: Start Mininet topology
sudo mn --controller=remote --topo=single,3
# Creates 1 switch (s1) and 3 hosts (h1, h2, h3)
# Connects switch to POX controller

# STEP 5: Test connectivity
pingall
# Verifies all hosts can communicate (should show 0% dropped)

# STEP 6: Simulate port DOWN event
link s1 h1 down
# Disables link between switch and host
# POX will log: Port is DOWN

# STEP 7: Simulate port UP event
link s1 h1 up
# Restores link
# POX will log: Port is UP

# STEP 8: (Optional) Test other ports
link s1 h2 down
link s1 h2 up

link s1 h3 down
link s1 h3 up


# STEP 9: Exit Mininet
exit

# STEP 10: Stop POX controller
# Go to POX terminal and press:
# Ctrl + C


<img width="939" height="456" alt="Screenshot 2026-04-10 114718" src="https://github.com/user-attachments/assets/7f4a5efe-692c-415a-90df-eab0ffd3c789" />
<img width="907" height="626" alt="Screenshot 2026-04-10 114728" src="https://github.com/user-attachments/assets/45af516b-98fd-45c0-884b-b2a6ed86a6f0" />

