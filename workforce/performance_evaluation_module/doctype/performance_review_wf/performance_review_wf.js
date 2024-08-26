// Copyright (c) 2024, armaan,harshit and naman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Performance Review_wf", {
	onload: function(frm) {
        if (!frm.doc.__islocal) {
            return;
        }
        frm.set_value('reviewer', frappe.session.user);
    }
});
