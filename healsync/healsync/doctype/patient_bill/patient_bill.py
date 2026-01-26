# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PatientBill(Document):
	def on_submit(self):
		if self.patient_appointment:
			frappe.db.set_value(
				"Patient Appointment",
				self.patient_appointment,
				"invoiced",
				1
			)
