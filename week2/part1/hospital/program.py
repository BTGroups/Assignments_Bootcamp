from typing import List, Set


class Patient:
    _pid_counter = 0
    def __init__(self, name: str):
        if not name:
            raise ValueError("Patient name is required")

        self.pid = Patient._pid_counter
        Patient_pid_counter += 1
        self.name = name

    def __hash__(self): #removes duplicates( ignores if same patient)
        return hash(self.pid)

    def __eq__(self, other): #conforms match
        return isinstance(other, Patient) and self.pid == other.pid
    
    def __repr__(self):
        return f"Patient({self.name}, ID={self.pid})"


class Ward:
    def __init__(self, ward_no: int):
        self.ward_no = ward_no
        self.patients: Set[Patient] = set()

    def admit_patient(self, patient: Patient) -> None:
        if patient in self.patients:
            raise ValueError("Patient already admitted to this ward")
        self.patients.add(patient)


class Hospital:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Hospital name is required")

        self.name = name
        self.wards: List[Ward] = []

    def add_ward(self, ward: Ward) -> None:
        self.wards.append(ward)

    def has_patient(self, patient: Patient) -> bool:
        return any(patient in ward.patients for ward in self.wards)


class Surgeon:
    def __init__(self, sid: int, name: str):
        if not name:
            raise ValueError("Surgeon name is required")

        self.sid = sid
        self.name = name
        self.hospitals: Set[Hospital] = set()
        self.operated_patients: Set[Patient] = set()

    def add_hospital(self, hospital: Hospital) -> None:
        if not isinstance(hospital, Hospital):
            raise TypeError("Expected Hospital instance")
        if hospital in self.hospitals:
            raise ValueError(f"Hospital {hospital.name} already assigned to surgeon")
        self.hospitals.add(hospital)

    def can_operate(self, patient: Patient) -> bool:
        return any(hospital.has_patient(patient) for hospital in self.hospitals)

    def operate_patient(self, patient: Patient) -> None:
        if not self.can_operate(patient):
            raise ValueError("Surgeon cannot operate on patient not in their hospital")

        self.operated_patients.add(patient)


class SeniorSurgeon(Surgeon):
    pass


class NonSeniorSurgeon(Surgeon):
    pass


class SurgeonService:

    @staticmethod
    def total_operated_patients(surgeons: List[Surgeon]) -> int:
        unique_patients = set()
        for surgeon in surgeons:
            unique_patients.update(surgeon.operated_patients)
        return len(unique_patients)

    @staticmethod
    def patients_by_surgeon(surgeon: Surgeon) -> List[str]:
        return [p.name for p in surgeon.operated_patients]

    @staticmethod
    def patients_in_ward(ward: Ward) -> List[str]:
        return [p.name for p in ward.patients]



def create_sample_data():
    # Hospitals
    h1 = Hospital("City Hospital")
    h2 = Hospital("Care Hospital")

    # Wards
    w1 = Ward(101)
    w2 = Ward(102)

    h1.add_ward(w1)
    h1.add_ward(w2)

    # Patients
    p1 = Patient("Ravi")
    p2 = Patient("Anita")
    p3 = Patient("Kumar")

    w1.admit_patient(p1)
    w1.admit_patient(p2)
    w2.admit_patient(p3)

    # Surgeons
    s1 = SeniorSurgeon(1, "Dr. Mehta")
    s2 = NonSeniorSurgeon(2, "Dr. Rao")

    s1.add_hospital(h1)
    s1.add_hospital(h2)
    s2.add_hospital(h1)

    # Operations
    s1.operate_patient(p1)
    s1.operate_patient(p2)
    s2.operate_patient(p3)

    return s1, s2, w1


# =====================
# MAIN
# =====================

if __name__ == "__main__":
    s1, s2, w1 = create_sample_data()

    surgeons = [s1, s2]

    print("Total operated patients:", SurgeonService.total_operated_patients(surgeons))

    print("Patients operated by Dr. Mehta:", SurgeonService.patients_by_surgeon(s1))

    print("Patients in Ward 101:", SurgeonService.patients_in_ward(w1))
