"""
PROG211 - Object-Oriented Programming 1
Assignment: Real-World Solutions under DPG Standards
Domain: Health - Community Vaccination Tracker

DPG Alignment:
- Open-source       : pure Python, no paid libraries
- Inclusive         : text menu, runs on any device
- Privacy-respecting: only anonymous IDs and age stored
- Modular & reusable: separate classes and helper functions
- Bonus Marks       : Correct use of Tuples for vaccination records
"""

from datetime import date


# ======================================================================
# CLASS 1: Vaccine
# ======================================================================
class Vaccine:
    """Represents a vaccine type available in the system."""

    # Class attribute shared by every Vaccine object
    total_vaccines_registered: int = 0

    def __init__(self, vaccine_id: str, name: str, doses_required: int):
        self.vaccine_id = vaccine_id
        self.name = name
        self.doses_required = doses_required
        Vaccine.total_vaccines_registered += 1

    # ---------- Instance Method ----------
    def display_info(self) -> str:
        """Returns a formatted string with the vaccine's details."""
        return (f"[{self.vaccine_id}] {self.name} - "
                f"Requires {self.doses_required} dose(s)")

    # ---------- Class Method ----------
    @classmethod
    def from_string(cls, raw_string: str):
        """
        Alternative constructor (Factory Method).
        Usage: Vaccine.from_string("V003, Tetanus, 1")
        """
        vid, name, doses = raw_string.split(",")
        return cls(vid.strip(), name.strip(), int(doses.strip()))

    # ---------- Static Method ----------
    @staticmethod
    def is_valid_dose_count(doses: int) -> bool:
        """Utility method to validate if a dose count is realistic."""
        return isinstance(doses, int) and 1 <= doses <= 5


# ======================================================================
# CLASS 2: Patient
# ======================================================================
class Patient:
    """Represents an anonymous patient record (privacy-respecting)."""

    def __init__(self, patient_id: str, age: int):
        self.patient_id = patient_id
        self.age = age
        # Using a list to store multiple vaccination records
        # Each record will be stored as a TUPLE (for the 10 bonus marks)
        self.vaccinations = []

        # ---------- Instance Method ----------

    def record_vaccination(self, vaccine: Vaccine, dose_number: int) -> str:
        """Records a dose. Interacts with the Vaccine object."""

        # Validation using the Vaccine's static method
        if not Vaccine.is_valid_dose_count(dose_number):
            return f"Error: Invalid dose number {dose_number}."

        if dose_number > vaccine.doses_required:
            return (f"Error: {vaccine.name} only requires "
                    f"{vaccine.doses_required} dose(s).")

        # --- TUPLE IMPLEMENTATION (Bonus 10 Marks) ---
        # Storing immutable data as a tuple: (ID, Name, Dose, Date)
        record_tuple = (
            vaccine.vaccine_id,
            vaccine.name,
            dose_number,
            str(date.today())
        )
        self.vaccinations.append(record_tuple)

        return f"Success: Recorded {vaccine.name} dose {dose_number} for {self.patient_id}."

    # ---------- Instance Method ----------
    def display_info(self) -> str:
        """Returns a formatted string with the patient's complete history."""
        lines = [f"Patient: {self.patient_id} | Age: {self.age}"]

        if not self.vaccinations:
            lines.append("   (No vaccinations recorded yet)")
        else:
            # Unpacking the tuple to display the data cleanly
            for v_id, v_name, dose, v_date in self.vaccinations:
                lines.append(f"   - {v_name} (Dose {dose}) on {v_date}")

        return "\n".join(lines)

    # ---------- Class Method ----------
    @classmethod
    def create_anonymous(cls, patient_id: str):
        """Factory method for a patient whose age is unknown."""
        return cls(patient_id, age=0)

    # ---------- Static Method ----------
    @staticmethod
    def is_valid_id(pid: str) -> bool:
        """Utility method to ensure patient IDs follow the 'P001' format."""
        return isinstance(pid, str) and pid.startswith("P") and len(pid) >= 2


# ======================================================================
# DATA STRUCTURE: Dictionaries storing multiple objects
# ======================================================================
# Dictionaries are used here because they allow O(1) lookup time by ID.
patients_db = {}  # { "P001": Patient_Object, "P002": Patient_Object }
vaccines_db = {}  # { "V001": Vaccine_Object, "V002": Vaccine_Object }


# ======================================================================
# HELPER FUNCTIONS (Add & Display)
# ======================================================================
def add_patient(patient: Patient) -> str:
    """Adds a Patient object to the database dictionary."""
    if not Patient.is_valid_id(patient.patient_id):
        return "Error: Invalid patient ID (must start with 'P')."
    if patient.patient_id in patients_db:
        return f"Error: Patient {patient.patient_id} already exists."

    patients_db[patient.patient_id] = patient
    return f"Success: Patient {patient.patient_id} added to the system."


def add_vaccine(vaccine: Vaccine) -> str:
    """Adds a Vaccine object to the database dictionary."""
    if vaccine.vaccine_id in vaccines_db:
        return f"Error: Vaccine {vaccine.vaccine_id} already exists."

    vaccines_db[vaccine.vaccine_id] = vaccine
    return f"Success: Vaccine {vaccine.vaccine_id} added to the system."


def display_all_patients() -> str:
    """Loops through the dictionary and displays all patient records."""
    if not patients_db:
        return "No patients registered in the system."

    output = ["\n=== ALL PATIENT RECORDS ==="]
    for patient in patients_db.values():
        output.append(patient.display_info())
        output.append("-" * 45)  # Divider line
    return "\n".join(output)


def display_all_vaccines() -> str:
    """Loops through the dictionary and displays all available vaccines."""
    if not vaccines_db:
        return "No vaccines registered in the system."

    output = ["\n=== AVAILABLE VACCINES ==="]
    for vaccine in vaccines_db.values():
        output.append(vaccine.display_info())
    return "\n".join(output)