#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum
from typing import List, Optional


class RoomType(Enum):
    ISOLATION = "Isolation"
    WARD = "Ward"
    PRIVATE = "Private"
    ICU = "ICU"


class Room:
 
    
    def __init__(self, room_number: str, room_type: RoomType, capacity: int, daily_rate: float):
       
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = capacity
        self.daily_rate = daily_rate
        self.current_patients = []
    
    def is_full(self) -> bool:
        
        return len(self.current_patients) >= self.capacity
    
    def add_patient(self, patient) -> bool:
       
        if self.is_full():
            return False
        
        if patient in self.current_patients:
            return False
        
        self.current_patients.append(patient)
        return True
    
    def remove_patient(self, patient) -> bool:
       
        if patient in self.current_patients:
            self.current_patients.remove(patient)
            return True
        return False
    
    def get_occupancy(self) -> int:
       
        return len(self.current_patients)
    
    def get_available_beds(self) -> int:
     
        return self.capacity - self.get_occupancy()
    
    def __str__(self) -> str:
       
        return (f"Room {self.room_number} - {self.room_type.value} - "
                f"{self.get_occupancy()}/{self.capacity} patients - "
                f"${self.daily_rate:.2f}/day")
