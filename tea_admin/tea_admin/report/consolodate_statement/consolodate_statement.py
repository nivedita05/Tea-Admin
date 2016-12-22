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
	pay=0
	l_piece=0
	sick=0
	maternity=0
	other=0
	total_add=0
	pf=0


	advance=0
	kharcha=0
	ration=0
	lic=0
	total_sub=0

	net_pay=0

	report_entries=get_report_entries(filters)
	
	for i in report_entries:
		pay=get_sum_pay(i.book_code)[0][0]
		l_piece=get_sum_l_piece(i.book_code)[0][0]
		sick=get_sum_sick(i.book_code)[0][0]
		maternity=get_sum_maternity(i.book_code)[0][0]
		other=get_sum_other(i.book_code)[0][0]


		total_add=pay+l_piece+sick+maternity+other

		pf+=round(pay*0.12,2)


		advance=get_sum_advance(i.book_code)[0][0]
		kharcha=get_sum_kharcha(i.book_code)[0][0]
		ration=get_sum_ration(i.book_code)[0][0]
		lic=get_sum_lic(i.book_code)[0][0]

		total_sub=pf

		net_pay=total_add-total_sub

		data.append([i.book_code,pay,l_piece,sick,maternity,other,total_add,pf,advance,kharcha,ration,lic,total_sub,net_pay])
	
	return columns, data


def get_report_entries(filters):
	return frappe.db.sql("""select distinct book_code from `tabattendence` where  garden=%s""",(filters.garden),as_dict=1)





def get_sum_pay(book_code):
	return frappe.db.sql("""select sum(pay) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_l_piece(book_code):
	return frappe.db.sql("""select sum(l_piece) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_sick(book_code):
	return frappe.db.sql("""select sum(sick) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_maternity(book_code):
	return frappe.db.sql("""select sum(maternity) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_other(book_code):
	return frappe.db.sql("""select sum(other) from `tabattendence` where book_code=%s""",(book_code))




def get_sum_advance(book_code):
	return frappe.db.sql("""select sum(advance) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_kharcha(book_code):
	return frappe.db.sql("""select sum(kharcha) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_ration(book_code):
	return frappe.db.sql("""select sum(ration) from `tabattendence` where book_code=%s""",(book_code))

def get_sum_lic(book_code):
	return frappe.db.sql("""select sum(lic) from `tabattendence` where book_code=%s""",(book_code))




def get_columns():
		
		columns = [{
				"fieldname": "book_code",
				"label": _("Book Code"),
				"fieldtype": "Data",
				"width": 120
	    }]
		

	    	columns.append({
				"fieldname": "pay",
				"label": _("Total Pay"),
				"fieldtype": "Data",
				"width": 80
	    })

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
				"fieldname": "kharcha",
				"label": _("Kharcha"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	
	    	columns.append({
				"fieldname": "ration",
				"label": _("Ration"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "lic",
				"label": _("LIC"),
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