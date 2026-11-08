

from vaccination_tracker import (
    Vaccine, Patient,
    add_patient, add_vaccine,
    display_all_patients, display_all_vaccines,
    patients_db, vaccines_db,
)


# ======================================================================
# MENU
# ======================================================================
def show_menu():
    print("\n" + "=" * 55)
    print("   COMMUNITY VACCINATION TRACKER (DPG-Compliant)")
    print("=" * 55)
    print("1. Register a new vaccine")
    print("2. Register a new patient")
    print("3. Record a vaccination")
    print("4. View all vaccines")
    print("5. View all patients")
    print("6. Show summary")
    print("7. Exit")
    print("=" * 55)


# ======================================================================
# OPTION 1 — Register vaccine
# ======================================================================
def register_vaccine():
    print("\n--- Register New Vaccine ---")
    vid = input("Enter vaccine ID (e.g., V001): ").strip()
    name = input("Enter vaccine name (e.g., Measles): ").strip()

    try:
        doses = int(input("Enter doses required (1-5): ").strip())
    except ValueError:
        print("Error: doses must be a number.")
        return

    if not Vaccine.is_valid_dose_count(doses):
        print("Error: dose count must be between 1 and 5.")
        return

    vaccine = Vaccine(vid, name, doses)
    print(add_vaccine(vaccine))


# ======================================================================
# OPTION 2 — Register patient
# ======================================================================
def register_patient():
    print("\n--- Register New Patient ---")
    pid = input("Enter patient ID (e.g., P001): ").strip()

    if not Patient.is_valid_id(pid):
        print("Error: patient ID must start with 'P' and be at least 2 characters.")
        return

    try:
        age = int(input("Enter patient age: ").strip())
    except ValueError:
        print("Error: age must be a number.")
        return

    patient = Patient(pid, age)
    print(add_patient(patient))


# ======================================================================
# OPTION 3 — Record vaccination
# ======================================================================
def record_vaccination():
    print("\n--- Record Vaccination ---")

    if not patients_db:
        print("No patients registered yet.")
        return
    if not vaccines_db:
        print("No vaccines registered yet.")
        return

    pid = input("Enter patient ID: ").strip()
    if pid not in patients_db:
        print(f"Error: patient {pid} not found.")
        return

    vid = input("Enter vaccine ID: ").strip()
    if vid not in vaccines_db:
        print(f"Error: vaccine {vid} not found.")
        return

    try:
        dose = int(input("Enter dose number: ").strip())
    except ValueError:
        print("Error: dose must be a number.")
        return

    patient = patients_db[pid]
    vaccine = vaccines_db[vid]
    print(patient.record_vaccination(vaccine, dose))


# ======================================================================
# OPTION 6 — Summary
# ======================================================================
def show_summary():
    print("\n=== SUMMARY ===")
    print(f"Total vaccines registered: {Vaccine.total_vaccines_registered}")
    print(f"Total patients registered: {len(patients_db)}")
    total_doses = sum(len(p.vaccinations) for p in patients_db.values())
    print(f"Total doses administered: {total_doses}")


# ======================================================================
# MAIN LOOP
# ======================================================================
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            register_vaccine()
        elif choice == "2":
            register_patient()
        elif choice == "3":
            record_vaccination()
        elif choice == "4":
            print(display_all_vaccines())
        elif choice == "5":
            print(display_all_patients())
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Goodbye! Stay healthy.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()