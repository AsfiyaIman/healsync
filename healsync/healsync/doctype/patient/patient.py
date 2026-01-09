# Copyright (c) 2026, Asfiya Iman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import load_address_and_contact


class Patient(Document):
	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)
		
	def validate(self):
		self.set_full_name()

	def set_full_name(self):
		self.patient_name = " ".join(
			[name for name in [self.first_name, self.middle_name, self.last_name] if name]
		)
