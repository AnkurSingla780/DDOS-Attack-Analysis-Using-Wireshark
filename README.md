# 📡 Network Traffic Simulation & Analysis (TCP & UDP)

## 📖 Overview

This project demonstrates how to generate controlled TCP and UDP traffic using Python and analyze it using Wireshark. It is designed for cybersecurity labs to understand packet behavior, protocol differences, and how high-traffic patterns appear in captures.

---

## 📁 Project Structure

```
.
├── tcp.py        # TCP traffic generator (multithreaded)
├── udp.py        # UDP traffic generator (continuous stream)
└── README.md
```

---

## ⚙️ Requirements

* Python 3
* Wireshark


---

## 📦 Setup

### 1) Update system

```bash
sudo apt update && sudo apt upgrade -y
```

### 2) Install Wireshark

```bash
sudo apt install wireshark -y
```

Allow non-root capture when prompted. If not prompted:

```bash
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark $USER
```

Log out and back in.

---

## 🚀 How to Run

### Step 1: Start a Local Test Server (for TCP)

```bash
python3 -m http.server 8080
```

Keep this running.

---

### Step 2: Run TCP Script

Open a new terminal:

```bash
python3 tcp_traffic.py
```

This generates many parallel TCP connections to `127.0.0.1:8080`.

---

### Step 3: Run UDP Script

In another terminal:

```bash
python3 udp_traffic.py
```

This sends continuous UDP packets to `127.0.0.1:9999`.

---

## 📊 Capture Traffic (Wireshark)

1. Open Wireshark
2. Select **Loopback interface (lo)**
3. Click **Start Capture**
4. Run the scripts (TCP/UDP)
5. Capture for 20–30 seconds
6. Click **Stop**

---

## 🔎 Filters to Use

### TCP (port 8080)

```
tcp.port == 8080
```

### TCP SYN packets only

```
tcp.flags.syn == 1
```

### UDP (port 9999)

```
udp.port == 9999
```

---

## 📈 How to Analyze (Step-by-Step)

### 1) Packet List Inspection

* Sort by **Time** and **Protocol**
* Observe rapid increase in packet count
* Note source/destination IP (127.0.0.1)

### 2) TCP Analysis

Look for:

* SYN → SYN-ACK → ACK sequences
* Frequent connection open/close
* Many short-lived sessions

Go to:

* **Statistics → Conversations → TCP**
* **Statistics → Flow Graph** (to visualize handshakes)

### 3) UDP Analysis

Look for:

* Continuous stream of UDP packets
* No handshake
* Similar packet sizes

Go to:

* **Statistics → Conversations → UDP**

### 4) Traffic Rate (Important for Marks)

* Go to **Statistics → I/O Graph**
* Observe spikes in packets/second
* Compare TCP vs UDP rates

### 5) Protocol Distribution

* Go to **Statistics → Protocol Hierarchy**
* Identify percentage of TCP vs UDP traffic

---

## 📌 Expected Observations

### TCP Script

* High number of connection attempts
* Clear 3-way handshake
* Rapid session creation/termination

### UDP Script

* Continuous packet flow
* No connection establishment
* Higher packet rate than TCP

---

## 🔁 Key Differences

| Feature     | TCP                  | UDP               |
| ----------- | -------------------- | ----------------- |
| Type        | Connection-oriented  | Connectionless    |
| Handshake   | Yes                  | No                |
| Reliability | Reliable             | Unreliable        |
| Pattern     | Repeated connections | Continuous stream |

---

## ⚠️ Safety Note

This project is for **educational use only**. Run only on `localhost (127.0.0.1)` or a controlled lab environment. Do not target external systems without permission.

---

## 🎯 Learning Outcomes

* Understand TCP vs UDP behavior
* Analyze packet-level data in Wireshark
* Identify high-traffic patterns
* Gain hands-on experience with network analysis

---

## 👨‍💻 Author

Add your name here
