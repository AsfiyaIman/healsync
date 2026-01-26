// Copyright (c) 2026, Asfiya Iman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patient Bill Item", {
	qty(frm, cdt, cdn) {
		calculate_row(frm, cdt, cdn);
	},
	service(frm, cdt, cdn) {
		calculate_row(frm, cdt, cdn);
	}
});

frappe.ui.form.on("Patient Bill", {
	items_remove(frm) {
		calculate_total(frm);
	}
});

function calculate_row(frm, cdt, cdn) {
	let row = locals[cdt][cdn];

	row.amount = (row.qty || 1) * (row.rate || 0);

	frm.refresh_field("items");
	calculate_total(frm);
}

function calculate_total(frm) {
	let total = 0;

	(frm.doc.items || []).forEach(row => {
		total += row.amount || 0;
	});

	frm.set_value("total_amount", total);
}