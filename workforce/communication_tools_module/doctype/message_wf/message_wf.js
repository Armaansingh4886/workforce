// Copyright (c) 2024, armaan,harshit and naman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Message-wf", {
	onload: function(frm) {
        if (!frm.doc.__islocal) {
            return;
        }
        frm.set_value('sender', frappe.session.user);
    }





});
