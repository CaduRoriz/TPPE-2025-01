#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from typing import List, Dict, Optional
from models.pharmacy import Pharmacy
from models.room import Room, RoomType


class Hospital:
  
    
    def __init__(self, name: str):
    
        self.name = name
        self.patients = {}  
        self.doctors = {}   
        self.rooms = {}     
        self.pharmacy = Pharmacy()
    
    def register_patient(self, patient) -> bool:
      
        if patient.cpf in self.patients:
            return False
        
        self.patients[patient.cpf] = patient
        return True
    
    def get_patient(self, cpf: str) -> Optional:
      
        return self.patients.get(cpf)
    
    def register_doctor(self, doctor) -> bool:
    
        if doctor.crm in self.doctors:
            return False
        
        self.doctors[doctor.crm] = doctor
        return True
    
    def get_doctor(self, crm: str) -> Optional:
      
        return self.doctors.get(crm)
    
    def add_room(self, room) -> bool:
      
        if room.room_number in self.rooms:
            return False
        
        self.rooms[room.room_number] = room
        return True
    
    def get_room(self, room_number: str) -> Optional:
      
        return self.rooms.get(room_number)
    
    def get_available_rooms(self, room_type: Optional[RoomType] = None) -> List:
        available_rooms = []
        
        for room in self.rooms.values():
            if not room.is_full():
                if room_type is None or room.room_type == room_type:
                    available_rooms.append(room)
        
        return available_rooms
    
    def hospitalize_patient(self, patient, doctor, room, date=None) -> Optional:
      
        from models.hospitalization import Hospitalization
        
        if patient.is_currently_hospitalized():
            return None
        if room.room_number not in self.rooms or room.is_full():
            return None
        

        if date is None:
            date = datetime.date.today()
        
        hospitalization = Hospitalization(patient, doctor, room, date)
        
        patient.start_hospitalization(hospitalization)
        
        return hospitalization
    
    def discharge_patient(self, patient, date=None) -> Optional[float]:
      
        if not patient.is_currently_hospitalized():
            return None
             
        if date is None:
            date = datetime.date.today()
        
        return patient.end_hospitalization(date)
    
    def __str__(self) -> str:
        return (f"{self.name}\n"
                f"- Patients: {len(self.patients)}\n"
                f"- Doctors: {len(self.doctors)}\n"
                f"- Rooms: {len(self.rooms)}\n")