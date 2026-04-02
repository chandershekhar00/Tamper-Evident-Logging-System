# 🔐 Tamper-Evident Logging System

A secure logging system designed to ensure **integrity, traceability, and tamper detection** of log data using cryptographic techniques.

---

## 📌 Overview

In modern systems, logs are critical for monitoring, auditing, and detecting malicious activities. However, attackers may attempt to modify or delete logs to hide their actions.

This project implements a **tamper-evident logging system** where:

* Log entries are **cryptographically linked**
* Any modification, deletion, or reordering is **detectable**
* Integrity of the entire log chain can be verified

---

## 🎯 Objectives

* Prevent undetected modification of logs
* Ensure integrity and reliability of log data
* Detect:

  * Altered log entries
  * Deleted entries
  * Reordered entries
* Simulate real-world secure audit logging systems

---

## ⚙️ How It Works

Each log entry contains:

* Timestamp
* Event Type
* Description
* Hash of the previous log entry

### 🔗 Hash Chaining Mechanism

Every log is linked to the previous one using a cryptographic hash:

Log1 → Hash1
Log2 → Hash2 (includes Hash1)
Log3 → Hash3 (includes Hash2)

If any log is modified:

* The hash changes
* The chain breaks
* Tampering is detected

---

## 🧠 Core Concepts Used

* Cryptographic Hashing (e.g., SHA-256)
* Data Integrity
* Chain of Trust
* Tamper Detection

---

## 🚀 Features

* Add new log entries
* Verify log integrity
* Detect tampering
* Secure hash chaining
* Scalable for multiple log entries

---

## 🛠️ Installation & Setup

1. Clone the repository:
   git clone [Git Repo clone](https://github.com/chandershekhar00/Tamper-Evident-Logging-System.git)
   cd tamper-evident-logging

2. Run the program:
   temper_evident.py

---

## 📘 Usage

### Add Log Entry

Enter event details → System generates hash → Entry added

### Verify Logs

Run verification function → System checks hash chain

### Simulate Tampering

* Modify any log manually
* Run verification again
* System detects inconsistency

---

## 🧪 Example Output

Log 1: User Login
Hash: abc123...

Log 2: File Access
Hash: def456...

✔ Logs are valid

--- After Tampering ---

❌ Tampering detected at log entry 2

---

## 📊 Results

* Successfully detects:

  * Log modification
  * Log deletion
  * Log reordering
* Ensures complete log integrity
* Demonstrates real-world applicability in cybersecurity systems

---

## 🔒 Security Benefits

* Prevents unauthorized log manipulation
* Provides accountability
* Supports forensic analysis
* Enhances system trust

---

## 📂 Project Structure

tamper-evident-logging/
│── temper_evident.py
│── logs.json
│── README.md

---

🎥 Demo Video

👉 Add your demo video link here:[Video](https://drive.google.com/file/d/1ez0PvpWwFAroAw4AQaus3ZsqonQzqadH/view?usp=sharing)

 --- 

## ⚠️ Limitations

* Does not prevent deletion at storage level (only detects it)
* Requires secure storage for full protection
* Performance may decrease with very large logs

---

## 🔮 Future Improvements

* Use blockchain-based logging
* Store logs in distributed systems
* Add real-time alerting
* Integrate with SIEM tools

---

## 📚 References

* Cryptographic Hash Functions
* Secure Logging Systems
* Blockchain Concepts

---

## 👨‍💻 Author

* Chandrashekhar Tyagi
* chandershekhar8433@gmail.com
* +918439443923

---

## ⭐ Acknowledgment

This project is developed as part of a cybersecurity assignment to demonstrate secure logging and tamper detection techniques.

---
