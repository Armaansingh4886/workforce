// Copyright (c) 2024, armaan,harshit and naman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Timesheet", {
	onload: function(frm) {
        if (!frm.doc.__islocal) {
            return;
        }
        frm.set_value('employee', frappe.session.user);
        // frm.fields_dict['time_log'].grid.get_field('start_time').set_input_mask('00:00');
    }
});


frappe.ui.form.on('TimeLog', {
    start_time: function(frm, cdt, cdn) {
        calculate_duration(frm, cdt, cdn);
    },
    end_time: function(frm, cdt, cdn) {
        calculate_duration(frm, cdt, cdn);
    }
});

function calculate_duration(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    if (row.start_time && row.end_time) {
        let startTime = moment(row.start_time, 'HH:mm:ss');
        let endTime = moment(row.end_time, 'HH:mm:ss');
        
        if (endTime.isAfter(startTime)) {
            let duration = moment.duration(endTime.diff(startTime));
            let totalSeconds = Math.floor(duration.asSeconds());
            
            // Set the duration in seconds
            frappe.model.set_value(cdt, cdn, 'duration', totalSeconds);
        } else {
            // Handle case where end time is not after start time
            frappe.model.set_value(cdt, cdn, 'duration', 0);
        }
    }
}