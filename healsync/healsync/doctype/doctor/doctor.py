# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Doctor(Document):
	def validate(self):
		self.set_full_name()

	def set_full_name(self):
		first = self.first_name or ""
		middle = self.middle_name or ""
		last = self.last_name or ""
		self.doctor_name = first + " " + middle + " " + last
