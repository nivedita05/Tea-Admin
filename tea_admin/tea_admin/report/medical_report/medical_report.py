# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils

def execute(filters=None):
	data = []
	columns = get_columns()
	return columns, data





def get_columns():
		
		columns = [{
			"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"width": 80

		}]

		columns.append({
				"fieldname": "emp_name",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"width": 90
	    })


		columns.append({
				"fieldname": "family_no",
				"label": _("Family Id"),
				"fieldtype": "Data",
				"width": 90
	    })


		

	    	columns.append({
				"fieldname": "cost",
				"label": _(" Medical Expenses "),
				"fieldtype": "Data",
				"width": 90
	    })

	    
	    
		return columns
