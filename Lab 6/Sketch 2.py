# Разработать структуру классов с использованием
# механизмов наследования и агрегации для
# предметной области из лабораторной работы № 1
# Полную модель предметной области описывать в
# виде классов не обязательно (достаточно 3-4 классов)

# В работе должны быть использованы:
# 1. Отношение наследования (между одним базовым классом и
# как минимум двумя производными)
# 2. Не менее одного отношения агрегации между классами

class Patient:
    '''Система регистратуры стоматологии'''
    def __init__(self, dentist, cabinet):
        self.dentist = dentist
        self.cabinet = cabinet
        self.dates = {}

    def reserv(self, date, cabinet):
        reserved = self.dates[date]
        if cabinet + reserved > self.cabinet:
            raise Exception
        else:
            self.dates[date] = reserved + cabinet

class Recording:
    new = "New"
    reserved = "Reserved"
    performed = "Performed"
    canceled = "Canceled"

    def __init__(self, diagnosis, date, cabinet, patient):
        self.diagnosis = diagnosis
        self.date = date
        self.cabinet = cabinet
        self.patient = patient
        self.state = Recording.new

    def reserv(self):
        if self.state == Recording.new:
            try:
                self.patient.reserv()
                self.state = Recording.reserved
            except:
                raise Exception
        else:
            raise Exception

class System:
    u1 = "Patient №2005"
    u2 = "Patient №2010"
    u3 = "Patient №2015"

    rc1 = Patient(u1, 20)
    rc2 = Patient(u2, 25)
    rc3 = Patient(u3, 30)

    recordings = []

    def recording(self, patient, diagnosis, date, cabinet):
        new_recording = Recording(diagnosis, patient, date, cabinet)
        self.recordings.append(new_recording)

    def reserv(self, recording):
        recording.reserv()
