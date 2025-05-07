#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Medication:
    
    def __init__(self, name: str, dosage: str, unit_price: float, initial_stock: int = 0):
        
        self.name = name
        self.dosage = dosage
        self.unit_price = unit_price
        self.stock_quantity = initial_stock
    
    def update_stock(self, quantity: int) -> bool:
       
        if self.stock_quantity + quantity < 0:
            return False
        
        self.stock_quantity += quantity
        return True
    
    def has_sufficient_stock(self, quantity: int) -> bool:
        
        return self.stock_quantity >= quantity
    
    def __str__(self) -> str:
        
        return f"{self.name} ({self.dosage}) - Stock: {self.stock_quantity} units - ${self.unit_price:.2f}/unit"
