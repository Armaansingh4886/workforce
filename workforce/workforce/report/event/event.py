import frappe

def execute(filters=None):
    # Get the logged-in user's ID or email
    user_id = frappe.session.user

    # Query to get events where the logged-in user is a participant
    events = frappe.db.sql("""
        SELECT
            event.name as event_name,
            event.starts_on,
            event.ends_on,
            event.subject,
            event.description
        FROM
            `tabEvent` event
        INNER JOIN
            `tabEvent Participants` participants
        ON
            event.name = participants.parent
        WHERE
            participants.email= %s
        ORDER BY
            event.starts_on DESC
    """, (user_id,), as_dict=True)

    # Define the columns to display in the report
    columns = [
        {"label": "Event Name", "fieldname": "event_name", "fieldtype": "Data", "width": 200},
        {"label": "Starts On", "fieldname": "starts_on", "fieldtype": "Datetime", "width": 150},
        {"label": "Ends On", "fieldname": "ends_on", "fieldtype": "Datetime", "width": 150},
        {"label": "Subject", "fieldname": "subject", "fieldtype": "Data", "width": 200},
        {"label": "Description", "fieldname": "description", "fieldtype": "Text", "width": 300},
    ]

    # Return data and columns
    return columns, events