# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Patient ID", "fieldname": "name", "fieldtype": "Link", "options": "Patient", "width": 200},
		{"label": "Patient Name", "fieldname": "patient_name", "fieldtype": "Data", "width": 200},
		{"label": "Gender", "fieldname": "sex", "fieldtype": "Link", "options": "Gender", "width": 100},
		{"label": "Mobile", "fieldname": "mobile", "fieldtype": "Data", "width": 120},
		{"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 200},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
		{"label": "Inpatient Status", "fieldname": "inpatient_status", "fieldtype": "Data", "width": 150},
	]

	data = frappe.get_all(
		"Patient",
		fields=["name", "patient_name", "sex", "mobile", "email", "status", "inpatient_status"]
	)

	return columns, data
