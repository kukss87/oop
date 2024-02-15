class Doctor:
    def __init__(self, name, specialisation, age):
        self.name = name
        self.specialisation = specialisation
        self.patients = []

    def __str__(self):
        return f'Doctor: {self.name} ({self.specialisation})'

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            print(f'{patient} added to {self}')

    def cancel_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f'{patient} removed from queue to see {self}')

    def show_patients(self):
        print(f'Patients of {self}:')
        if self.patients:
            for patient in self.patients:
                print(patient)
        else:
            print(f'{self} has no patients')


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.doctors = []

    def __str__(self):
        return f'Patient: {self.name} ({self.age})'

    def make_appointment(self, doctor):
        if doctor not in self.doctors:
            self.doctors.append(doctor)
            doctor.add_patient(self)
            print(f'{self} booked an appointment with {doctor}')
        else:
            print(f'{self} already has an appointment with {doctor}')

    def cancel_appointment(self, doctor):
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            doctor.cancel_patient(self)
            print(f'{self}\'s appointment with {doctor} cancelled')
        else:
            print(f'{self} has not yet appointment with {doctor}')

    def show_doctors(self):
        print(f'Doctors of {self}:')
        if self.doctors:
            for doctor in self.doctors:
                print(doctor)
        else:
            print(f'{self} has no doctors')


if __name__ == '__main__':
    doctor1 = Doctor(name='John', specialisation='Cardiology', age=40)
    doctor2 = Doctor(name='Jane', specialisation='Oncology', age=30)
    patient1 = Patient(name='Alice', age=25)
    patient2 = Patient(name='Bob', age=35)
    patient3 = Patient(name='Charlie', age=45)

    doctors = [doctor1, doctor2]
    patients = [patient1, patient2, patient3]

    for d in doctors:
        for p in patients:
            p.make_appointment(d)
    print('________')

    patient3.cancel_appointment(doctor1)
    patient2.cancel_appointment(doctor1)
    patient2.cancel_appointment(doctor2)
    patient3.cancel_appointment(doctor1)

    doctor1.show_patients()
    doctor2.show_patients()

