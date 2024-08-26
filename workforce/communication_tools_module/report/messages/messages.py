# Copyright (c) 2024, armaan,harshit and naman and contributors
# For license information, please see license.txt

import frappe
from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]


# import frappe

def execute(filters=None):
    # Get the logged-in user's ID
    user_id = frappe.session.user

    # Query the messages where the logged-in user is the recipient
    messages = frappe.db.sql("""
        SELECT sender, COUNT(name) as message_count, GROUP_CONCAT(subject SEPARATOR ', ') as subjects
        FROM `tabMessage-wf`
        WHERE recipient = %s
        GROUP BY sender
        ORDER BY sender
    """, (user_id,), as_dict=True)

    # Define columns
    columns = [
        {"label": "Sender", "fieldname": "sender", "fieldtype": "Data", "width": 200},
        {"label": "Message Count", "fieldname": "message_count", "fieldtype": "Int", "width": 100},
        {"label": "Subjects", "fieldname": "subjects", "fieldtype": "Data", "width": 300},
    ]

    # Return data and columns
    return columns, messages