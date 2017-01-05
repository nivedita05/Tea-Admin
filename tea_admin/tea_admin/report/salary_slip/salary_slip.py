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

	add=get_add_fileld(filters)
	for i in add:
		pf_no=get_pf_no(i.emp_code)

		data.append([i.emp_code,i.emp_name,i.days_present,pf_no,i.basic,i.da,i.vda,i.allowence,i.other,i.fc,i.hra,i.elf
			,i.salary,i.pf,i.p_tax,i.advance,i.rev,i.lic,i.ration,i.welfare_fund,i.mislleneous_ded,i.ded_total,i.gross_salary,i.net_salary])
	return columns, data

def get_add_fileld(filters):
	return frappe.db.sql("""select emp_code,emp_name,days_present,basic,da,vda,allowence,
		other,fc,hra,elf,salary,pf,p_tax,advance,rev,lic,ration,welfare_fund,mislleneous_ded,ded_total,
		gross_salary,net_salary from `tabSalary for Staff` where date=%s and book_code=%s""",(filters.date,filters.book_code),as_dict=1)

def get_pf_no(emp_code):
	return frappe.db.sql(""" select pf_no from `tabLabour Information` where emp_id=%s """,(emp_code))

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
				"fieldname": "days",
				"label": _("Days"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "pf_no",
				"label": _("PF No"),
				"fieldtype": "Data",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "basic",
				"label": _("Basic"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "da",
				"label": _("DA"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "vda",
				"label": _("VDA"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "allowence",
				"label": _("Allowence"),
				"fieldtype": "Data",
				"width": 90
	    })
	    	columns.append({
				"fieldname": "other",
				"label": _("Other"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "fc",
				"label": _("FC"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "hra",
				"label": _("HRA"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "el",
				"label": _("EL/FU"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "add_total",
				"label": _("Total"),
				"fieldtype": "Data",
				"width": 90
	    })

	    

	    	columns.append({
				"fieldname": "pf",
				"label": _("PF"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "p_tax",
				"label": _("P Tax"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	

	    	columns.append({
				"fieldname": "adv",
				"label": _("Advance"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "rev",
				"label": _("Revenue"),
				"fieldtype": "Data",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "lic",
				"label": _("LIC"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "ration",
				"label": _("Ration"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "well_fare",
				"label": _("Wellfare Tax"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "mis_ded",
				"label": _("Mis Ded"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "sub_total",
				"label": _("Total"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "gross_pay",
				"label": _("Gross Pay"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "net_pay",
				"label": _("Net Pay"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "pf_adv",
				"label": _("Pf Adv"),
				"fieldtype": "Data",
				"width": 90
	    })









	    
	    
		return columns
