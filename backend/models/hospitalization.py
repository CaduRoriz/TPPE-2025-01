
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from typing import List, Optional


class Hospitalization:
    
    def __init__(self, patient, doctor, room, start_date: datetime.date):
   
        self.patient = patient
        self.doctor = doctor
        self.room = room
        self.start_date = start_date
        self.end_date = None
        self.prescriptions = []
        
        self.doctor.register_hospitalization(self)
    
        self.room.add_patient(patient)
    
    def add_prescription(self, prescription):
        
        self.prescriptions.append(prescription)
    
    def end_stay(self, end_date: datetime.date) -> float:
      
        if self.end_date is not None:
            return 0
        
        self.end_date = end_date
        
        self.room.remove_patient(self.patient)
        
        return self.calculate_cost()
    
    def calculate_cost(self) -> float:
        
        if self.end_date is None:
           end_date = datetime.date.today()
        else:
            end_date = self.end_date
        
        
        days = (end_date - self.start_date).days
        if days <= 0:
            days = 1  

        room_cost = days * self.room.daily_rate
        
       
        medication_cost = sum(prescription.get_total_cost() for prescription in self.prescriptions)
        
        return room_cost + medication_cost
    
    def get_duration_days(self) -> int:
        if self.end_date is None:
            end = datetime.date.today()
        else:
            end = self.end_date
        
        return (end - self.start_date).days or 1 
    
    def is_active(self) -> bool:
        
        return self.end_date is None
    
    def __str__(self) -> str:
       
        status = "Active" if self.is_active() else "Discharged"
        duration = self.get_duration_days()
        return (f"Hospitalization of {self.patient.name}\n"
                f"Room: {self.room.room_number}\n"
                f"Doctor: {self.doctor.name}\n"
                f"Start date: {self.start_date}\n"
                f"End date: {self.end_date or 'Still active'}\n"
                f"Duration: {duration} day{'s' if duration != 1 else ''}\n"
                f"Status: {status}")