# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Appointment ID", "fieldname": "name", "fieldtype": "Link", "options": "Patient Appointment", "width": 150},
		{"label": "Patient", "fieldname": "patient", "fieldtype": "Link", "options": "Patient", "width": 150},
		{"label": "Doctor", "fieldname": "doctor", "fieldtype": "Link", "options": "Doctor", "width": 150},
		{"label": "Appointment Date", "fieldname": "appointment_date", "fieldtype": "Date", "width": 150},
		{"label": "Visit Type", "fieldname": "visit_type", "fieldtype": "Data", "width": 120},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
	]

	data = frappe.get_all(
		"Patient Appointment",
		fields=[
			"name",
			"patient",
			"doctor",
			"appointment_date",
			"visit_type",
			"status"
		]
	)

	return columns, data
