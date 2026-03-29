# Telemetry Data Format Converter

## 📌 Overview
This project converts telemetry data from two different input formats into a unified JSON format.  
It ensures consistency in structure and timestamp representation (milliseconds since epoch).

---

## 📂 Files Included
- data-1.json → Input Format 1  
- data-2.json → Input Format 2  
- data-result.json → Expected Output Format  
- main.py → Conversion logic + unit tests  

---

## ⚙️ Features
- Converts two different JSON formats into a single unified structure
- Handles ISO timestamp → milliseconds conversion
- Includes automated unit tests using Python `unittest`
- Optimized for performance and low memory usage

---

## 🔄 Conversion Logic

### Format 1
- Extracts location from a `/` separated string
- Maps:
  - `operationStatus → status`
  - `temp → temperature`
- Timestamp already in milliseconds

### Format 2
- Extracts nested device and data fields
- Converts ISO timestamp to milliseconds
- Directly maps structured location fields

---

## 🚀 How to Run

```bash
python main.py
