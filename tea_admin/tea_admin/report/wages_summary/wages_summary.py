# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
import math

def execute(filters=None):
	data = []
	columns = get_columns()
	
	add_total=0
	
	total_sub=0

	net_pay=0

	rep=get_report_entries(filters)
	adv=get_adv(filters)
	
	add_total=rep[0][0]+rep[0][1]+rep[0][2]+rep[0][3]+rep[0][4]
	total_sub=rep[0][0]*0.12+adv[0][0]
	
	net_pay=add_total-total_sub
	
	data.append([rep[0][0],rep[0][1],rep[0][2],rep[0][3],rep[0][4],add_total,rep[0][0]*0.12,adv,total_sub,net_pay])
	
	return columns, data


def get_report_entries(filters):
	return frappe.db.sql("""select sum(pay),sum(l_piece),sum(sick),sum(maternity),sum(other) from `tabattendence` group by book_code having book_code=%s """,(filters.book_code))

def get_adv(filters):
	return frappe.db.sql("""select sum(deducted_advance_amount) from `tabPayment` group by book_code having book_code=%s """,(filters.book_code))


def get_columns():
		
		columns = [{
				"fieldname": "pay",
				"label": _("Total Pay"),
				"fieldtype": "Data",
				"width": 80
	    }]
		

	    	columns.append({
				"fieldname": "l_piece",
				"label": _("Leaf Piece"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "sick",
				"label": _("Sick"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "mat",
				"label": _("Maternity"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "oth",
				"label": _("Other"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "tot_earn",
				"label": _("Total Earn"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	
	    	columns.append({
				"fieldname": "pf",
				"label": _("PF"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "adv",
				"label": _("Adv"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	
	    	columns.append({
				"fieldname": "deducted_value",
				"label": _("Deducted Value"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "net_pay",
				"label": _("Net Pay"),
				"fieldtype": "Data",
				"width": 80
	    })

	    

		return columns