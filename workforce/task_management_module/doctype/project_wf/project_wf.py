# Copyright (c) 2024, armaan,harshit and naman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Projectwf(Document):
    def validate(self):
        
        if self.start_date and self.end_date and self.end_date < self.start_date:
            frappe.throw("End Date cannot be before Start Date.")
