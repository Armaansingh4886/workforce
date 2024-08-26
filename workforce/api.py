import frappe

@frappe.whitelist()
def get_total_hours_worked():
    # Get the logged-in user's ID
    user_id = frappe.session.user
    
    # Get the employee linked to the logged-in user
    employee = frappe.get_value("User",  user_id)
    
    if not employee:
        frappe.throw("Employee not found for the logged-in user.")
    
    # Sum the duration for all timesheets linked to the employee
    total_hours = frappe.db.get_value(
        "Timesheet",
        {"employee": employee},
        "SUM(duration)"
    )
    
    # Return the total hours, defaulting to 0 if no entries found
    print(total_hours)
    return total_hours/100+total_hours%100 or 0



@frappe.whitelist()
def get_average_hours_worked():
    # Get the logged-in user's ID
    user_id = frappe.session.user
    
    # Get the employee linked to the logged-in user
    employee = frappe.get_value("User",  user_id)
    
    if not employee:
        frappe.throw("Employee not found for the logged-in user.")
    
    # Sum the duration for all timesheets linked to the employee
    total_hours,count = frappe.db.get_value(
        "Timesheet",
        {"employee": employee},
        ["SUM(duration)","COUNT(name)"]
    )
    
    # Return the total hours, defaulting to 0 if no entries found
    print(total_hours)
    return (total_hours/100+total_hours%100)/count or 0




@frappe.whitelist()
def get_employee_count_for_role():
    # Role Profile ke andar se user count nikalna
    user_list = frappe.get_list('User Role Profile', 
        filters={'role_profile_name': "Employee"},
        fields=['name']
    )
    
    # Employee count return karna
    return len(user_list)



# SELECT role_profile, COUNT(*) as count
# FROM `tabUser Role Profile`
# WHERE role_profile = 'Employee'
# GROUP BY role_profile;
