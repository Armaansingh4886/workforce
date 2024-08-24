import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Employee"), "fieldname": "employee", "fieldtype": "Link", "options": "User", "width": 150},
        {"label": _("Date"), "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": _("Duration (hours)"), "fieldname": "duration", "fieldtype": "Time", "width": 150}
    ]
    
    conditions = "1=1"
    
    if filters.get("employee"):
        conditions += f" AND employee = '{filters.get('employee')}'"
    
    if filters.get("date_from"):
        conditions += f" AND date >= '{filters.get('date_from')}'"
    
    if filters.get("date_to"):
        conditions += f" AND date <= '{filters.get('date_to')}'"
    
    if filters.get("duration_min"):
        min_duration = convert_time_to_seconds(filters.get("duration_min"))
        conditions += f" AND TIME_TO_SEC(duration) >= {min_duration}"
    
    if filters.get("duration_max"):
        max_duration = convert_time_to_seconds(filters.get("duration_max"))
        conditions += f" AND TIME_TO_SEC(duration) <= {max_duration}"
    
    data = frappe.db.sql(f"""
        SELECT employee, date, duration
        FROM `tabTimesheet`
        WHERE {conditions}
        ORDER BY date
    """, as_dict=True)
    
    return columns, data

def convert_time_to_seconds(time_str):
    """Converts time in HH:MM:SS format to total seconds."""
    if time_str:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    return 0