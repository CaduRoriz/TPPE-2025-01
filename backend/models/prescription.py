#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prescription model for the Hospital Management System.
"""

import datetime
from typing import List, Dict, Optional


class PrescriptionItem:

    
    def __init__(self, medication, quantity: int, instructions: str):
      
        self.medication = medication
        self.quantity = quantity
        self.instructions = instructions
        self.fulfilled = False
    
    def fulfill(self) -> bool:
       
        if self.fulfilled:
            return False
        
        # Try to update medication stock
        if self.medication.update_stock(-self.quantity):
            self.fulfilled = True
            return True
        
        return False
    
    def get_cost(self) -> float:
        
        return self.medication.unit_price * self.quantity
    
    def __str__(self) -> str:
       
        status = "Fulfilled" if self.fulfilled else "Not fulfilled"
        return (f"{self.medication.name} - {self.quantity} units - "
                f"{self.instructions} - {status}")


class Prescription:

    
    def __init__(self, doctor, patient, date: datetime.date, observations: Optional[str] = None):
       
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.observations = observations
        self.items = []
    
    def add_item(self, medication, quantity: int, instructions: str) -> bool:
        
        if medication.has_sufficient_stock(quantity):
            item = PrescriptionItem(medication, quantity, instructions)
            self.items.append(item)
            return True
        return False
    
    def fulfill_all_items(self) -> bool:
       
        all_fulfilled = True
        for item in self.items:
            if not item.fulfill():
                all_fulfilled = False
        
        return all_fulfilled
    
    def get_total_cost(self) -> float:
       
        return sum(item.get_cost() for item in self.items)
    
    def __str__(self) -> str:
        
        items_str = "\n  ".join([str(item) for item in self.items])
        return (f"Prescription for {self.patient.name}\n"
                f"Date: {self.date}\n"
                f"Doctor: {self.doctor.name}\n"
                f"Items:\n  {items_str}\n"
                f"Observations: {self.observations or 'None'}")
