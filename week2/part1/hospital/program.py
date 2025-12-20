class Patient:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name


class Ward:
    def __init__(self, ward_no):
        self.ward_no = ward_no
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.wards = []

    def add_ward(self, ward):
        self.wards.append(ward)

class Surgeon:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.hospitals = []
        self.operated_patients = []

    def add_hospital(self, hospital):
        self.hospitals.append(hospital)

    def operate_patient(self, patient):
        self.operated_patients.append(patient)


class SeniorSurgeon(Surgeon):
    pass


class NonSeniorSurgeon(Surgeon):
    pass

class SurgeonService:
    @staticmethod
    def total_operated_patients(surgeons):
        patients = set()
        for surgeon in surgeons:
            for p in surgeon.operated_patients:
                patients.add(p)
        return len(patients)
    @staticmethod
    def patients_by_surgeon(surgeon):
        return [p.name for p in surgeon.operated_patients]
    @staticmethod
    def patients_in_ward(ward):
        return [p.name for p in ward.patients]
    
if __name__ == "__main__":

    # Hospitals
    h1 = Hospital("City Hospital")
    h2 = Hospital("Care Hospital")

    # Wards
    w1 = Ward(101)
    w2 = Ward(102)

    h1.add_ward(w1)
    h1.add_ward(w2)

    # Patients
    p1 = Patient(1, "Ravi")
    p2 = Patient(2, "Anita")
    p3 = Patient(3, "Kumar")

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

    surgeons = [s1, s2]

    print("Total operated patients:",
          SurgeonService.total_operated_patients(surgeons))

    print("Patients operated by Dr. Mehta:",
          SurgeonService.patients_by_surgeon(s1))

    print("Patients in Ward 101:",
          SurgeonService.patients_in_ward(w1))
