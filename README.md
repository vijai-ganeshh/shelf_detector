# 🛒 Shelf Detector – Retail Inventory & Defect Tracking System

A lightweight web-based shelf auditing and defect management application built with **Python**, **Streamlit**, and **MySQL**. This tool allows retail store auditors and QA teams to log shelf discrepancies (such as out-of-stock items, misplaced goods, and damaged packaging), manage defect lifecycles, and persist all records in a relational MySQL database.

---

## ✨ Key Features

- **Defect & Discrepancy Logging:** Record product names/SKUs, aisle locations, issue categories, severity levels, and detailed audit notes.
- **Relational Data Persistence:** Powered by MySQL with auto-incrementing primary keys, strict `ENUM` state enforcement, and automated creation timestamps.
- **Defect Lifecycle Management:** Transition logged issues seamlessly across `Open`, `In Progress`, `Resolved`, and `Closed` stages.
- **Live Audit Dashboard:** Query and view all active shelf discrepancies in real time using parameterized SQL statements and Pandas DataFrames.
- **Input Validation:** Built-in form checks prevent blank submissions and ensure clean data entry into the database.

---

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit
- **Backend / Logic:** Python 3
- **Database:** MySQL
- **Database Driver:** `mysql-connector-python`
- **Data Formatting:** Pandas

---

## 📂 Project Structure

```text
shelf_detector/
│
├── app.py               # Main Streamlit web application and UI workflows
├── db_config.py         # MySQL database connection and parameterized query helpers
├── schema.sql           # SQL script to initialize the database and table schema
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
