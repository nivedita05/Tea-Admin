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
				"fieldname": "days",
				"label": _("Days"),
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









	    
	    
		return columns
