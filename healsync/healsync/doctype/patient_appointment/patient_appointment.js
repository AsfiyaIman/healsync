// Copyright (c) 2026, Asfiya Iman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patient Appointment", {
	refresh(frm) {
		// Show button only if document is saved
		if (!frm.is_new()) {
			frm.add_custom_button(
				__('Vital Signs'),
				function () {
					create_vital_signs(frm);
				},
				__('Create')
			);
		}
	}
});

function create_vital_signs(frm) {
	if (!frm.doc.patient) {
		frappe.throw(__('Please select Patient'));
	}

	frappe.new_doc('Vital Signs', {
		patient: frm.doc.patient,
		patient_appointment: frm.doc.name
	});
}