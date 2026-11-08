# Community Vaccination Tracker

**PROG211: Object-Oriented Programming 1 - Individual Assignment**
**Domain:** Health (Vaccination Tracker)
**Developer:** [Your Name] (Student ID: [Your ID])
**Examiner:** Amandus Benjamin Coker

##  Project Description
The **Community Vaccination Tracker** is a Python-based, interactive console application designed to help health workers manage vaccine distribution and patient records. Built entirely using Object-Oriented Programming (OOP) principles, this tool allows users to register different vaccines, register patients using privacy-compliant anonymous IDs, record administered doses, and view summary reports.

The system runs entirely in the terminal, ensuring it is lightweight, fast, and capable of running on low-spec hardware often found in local clinics.

##  Key Features
*   **Interactive Menu:** A user-friendly, numbered menu system for easy navigation.
*   **Data Validation:** Robust error handling (via static methods and `try/except` blocks) ensures invalid IDs, incorrect dose counts, or text inputs do not crash the program.
*   **Record Tracking:** Automatically timestamps administered vaccinations with the current date.
*   **Summary Reports:** Quick overview of total registered vaccines, patients, and doses administered.

##  Digital Public Goods (DPG) Alignment
This project strictly adheres to the Digital Public Goods (DPG) standards required by the assignment brief:

1.  **Open-Source:** Built entirely with Python's standard library (no paid dependencies). Free for anyone to clone, modify, and deploy.
2.  **Inclusive and Accessible:** Uses a lightweight text-based interface. No internet connection is required to run the core application, making it accessible in remote areas.
3.  **Privacy-Respecting:** **Zero Personally Identifiable Information (PII) is stored.** The system only records anonymous Patient IDs (e.g., `P001`) and age. No names, addresses, or phone numbers are collected.
4.  **Modular and Reusable:** The architecture separates the UI (`main.py`) from the business logic (`vaccination_tracker.py`), allowing the core classes to be reused in future GUI applications.

##  OOP Concepts Demonstrated
*   **Classes & Objects:** `Vaccine` and `Patient`.
*   **Instance Methods:** `display_info()`, `record_vaccination()`.
*   **Class Methods (`@classmethod`):** `Vaccine.from_string()`, `Patient.create_anonymous()`.
*   **Static Methods (`@staticmethod`):** `Vaccine.is_valid_dose_count()`, `Patient.is_valid_id()`.
*   **Data Structures:** Dictionaries (`patients_db`, `vaccines_db`) used for efficient O(1) data retrieval.
*   **Composition:** A `Patient` object contains a list of vaccination records.

##  File Structure
```text
vaccination-tracker/
│
├── main.py                  # Interactive CLI menu and user input handling
├── vaccination_tracker.py   # Core OOP logic (Classes and Data Structures)
└── README.md                # Project documentation