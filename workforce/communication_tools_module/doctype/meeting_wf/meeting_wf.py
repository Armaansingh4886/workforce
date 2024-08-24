from frappe.model.document import Document
import frappe
from frappe.utils import nowdate
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

class Meetingwf(Document):
    def validate(self):
        if self.date and self.date < nowdate():
            frappe.throw("Meeting Date cannot be in the past. Please select today's date or a future date.")
        





    
