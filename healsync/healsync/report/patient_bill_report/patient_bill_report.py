# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{"label": "Bill ID", "fieldname": "name", "fieldtype": "Link", "options": "Patient Bill", "width": 200},
		{"label": "Patient", "fieldname": "patient", "fieldtype": "Link", "options": "Patient", "width": 200},
		{"label": "Bill Date", "fieldname": "bill_date", "fieldtype": "Date", "width": 120},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
		{"label": "Mode of Payment", "fieldname": "mode_of_payment", "fieldtype": "Link", "options": "Mode of Payment", "width": 150},
		{"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
	]

	conditions = {"docstatus": 1}

	if filters.get("from_date"):
		conditions["bill_date"] = [">=", filters.get("from_date")]

	if filters.get("to_date"):
		conditions.setdefault("bill_date", [])
		conditions["bill_date"].append(filters.get("to_date"))

	data = frappe.get_all(
		"Patient Bill",
		fields=[
			"name",
			"patient",
			"bill_date",
			"status",
			"mode_of_payment",
			"total_amount"
		],
		filters=conditions
	)

	return columns, data