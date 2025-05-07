#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
from enum import Enum
from typing import List, Optional


class HealthStatus(Enum):
    
    INFECTED = "Infected"
    NOT_INFECTED = "Not Infected"
    RECOVERED = "Recovered"
    DECEASED = "Deceased"


class Patient:

    
    def __init__(self, name: str, cpf: str, birth_date: datetime.date):
       
        self.name = name
        self.cpf = cpf
        self.birth_date = birth_date
        self.health_status = HealthStatus.NOT_INFECTED
        self.prescriptions = []
        self.hospitalization_history = []
        self.active_hospitalization = None
    
    @property
    def age(self) -> int:
        
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    
    def update_health_status(self, status: HealthStatus) -> None:
        
        self.health_status = status
    
    def add_prescription(self, prescription) -> None:
        
        self.prescriptions.append(prescription)
    
    def is_currently_hospitalized(self) -> bool:
      
        return self.active_hospitalization is not None
    
    def start_hospitalization(self, hospitalization) -> bool:
        
        if self.is_currently_hospitalized():
            return False
        
        self.active_hospitalization = hospitalization
        self.hospitalization_history.append(hospitalization)
        return True
    
    def end_hospitalization(self, end_date: datetime.date) -> Optional[float]:
        
        if not self.is_currently_hospitalized():
            return None
        
        cost = self.active_hospitalization.end_stay(end_date)
        self.active_hospitalization = None
        return cost
    
    def __str__(self) -> str:
      
        hospitalization_status = "Currently hospitalized" if self.is_currently_hospitalized() else "Not hospitalized"
        return f"Patient: {self.name}, CPF: {self.cpf}, Status: {self.health_status.value}, {hospitalization_status}"
