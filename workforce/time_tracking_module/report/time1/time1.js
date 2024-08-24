frappe.query_reports["time1"] = {
    "filters": [
        {
            "fieldname": "employee",
            "label": __("Employee"),
            "fieldtype": "Link",
            "options": "Ufser",
            "default": "",
            "reqd": 0
        },
        {
            "fieldname": "date_from",
            "label": __("Date From"),
            "fieldtype": "Date",
            "default": "",
            "reqd": 0
        },
        {
            "fieldname": "date_to",
            "label": __("Date To"),
            "fieldtype": "Date",
            "default": "",
            "reqd": 0
        },
        {
            "fieldname": "duration_min",
            "label": __("Minimum Duration (hours)"),
            "fieldtype": "Time",
            "default": "",
            "reqd": 0
        },
        {
            "fieldname": "duration_max",
            "label": __("Maximum Duration (hours)"),
            "fieldtype": "Time",
            "default": "",
            "reqd": 0
        }
    ]
};