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

	report_entries=get_report_entries(filters)

	for i in report_entries:
		
		p_tax=get_p_tax(i.emp_code,filters)

		data.append([i.emp_code,i.emp_name,p_tax])
	
	return columns, data

def get_report_entries(filters):
	return frappe.db.sql("""select emp_code,emp_name from `tabSalary for Staff` where date between %s and %s """,(filters.date1,filters.date2),as_dict=1)

def get_p_tax(emp_code,filters):
	return frappe.db.sql("""select sum(p_tax) from `tabSalary for Staff` where date between %s and %s and emp_code=%s""",(filters.date1,filters.date2,emp_code))


def get_columns():
		
		columns = [{
				"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 150
	    }]
		
		columns.append({
				"fieldname": "name1",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 150
	    })

	    	

	    	

	    	columns.append({
				"fieldname": "p_tax",
				"label": _("Provisional Tax Amount"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 150
	    })

	   
		return columns
