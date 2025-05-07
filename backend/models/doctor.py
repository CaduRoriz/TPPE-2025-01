#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List, Optional


class Doctor:
    
    
    def __init__(self, name: str, crm: str, specialty: str):
       
        self.name = name
        self.crm = crm
        self.specialty = specialty
        self.prescriptions = []
        self.hospitalizations = []
    
    def create_prescription(self, patient, date, observations=None):
       
        from models.prescription import Prescription
        
        prescription = Prescription(self, patient, date, observations)
        self.prescriptions.append(prescription)
        patient.add_prescription(prescription)
        return prescription
    
    def register_hospitalization(self, hospitalization):

        self.hospitalizations.append(hospitalization)
    
    def __str__(self) -> str:
    
        return f"Dr. {self.name}, CRM: {self.crm}, Specialty: {self.specialty}"
