# Copyright (c) 2024, armaan,harshit and naman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe.utils import today

class Taskwf(Document):
    def validate(self):
        
        if self.due_date and self.due_date < today():
            frappe.throw("Due Date cannot be in the past.")

