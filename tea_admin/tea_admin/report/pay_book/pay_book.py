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

	# initialized the variables with zero

	total_other=0
	total_sick=0
	total_pay=0
	total_maternity=0
	tota_leave=0
	total_food_conssesion=0
	total_l_piece=0

	total_addition=0
	
	total_p_per_fund=0
	total_kharcha=0
	total_lp_paid=0
	total_advance=0
	total_ration=0
	total_electricity=0
	total_lic=0

	total_deduction=0

	report_entries = get_report_entries(filters)
	


	for sle in report_entries:

		number_of_day_present= get_number_of_days_work(sle.emp_code)

		present_as_special_cat=get_number_of_days_work_as_special(sle.emp_code,filters)
		present_as_normal_cat=get_number_of_days_work_as_normal(sle.emp_code,filters)

		

		pf=get_pf_no(sle.emp_code)

		desig=get_des_category(sle.emp_code)

		# ADDITION REALATED

		pay=get_pay(pf)
#get the total pay for a time span and for a particular emp
		total_pay=pay[0][0]*number_of_day_present[0][0]

		food_conssesion=get_food_conssesion(pf)
#get the total food conssesion for a time span and for a particular emp
		total_food_conssesion=food_conssesion[0][0]*number_of_day_present[0][0]

		l_piece=get_l_piece(pf)
#get the total leave piece for a time span and for a particular emp
		total_l_piece=l_piece[0][0]*number_of_day_present[0][0]

		sick=get_sick(pf)
#get the total sick pay  for a time span and for a particular emp
		total_sick=sick[0][0]*number_of_day_present[0][0]

		maternity=get_maternity(pf)
#get the total maternity pay for a time span and for a particular emp
		total_maternity=maternity[0][0]*number_of_day_present[0][0]

		leave_pay=get_leave_pay(pf)
#get the total leave pay  for a time span and for a particular emp
		tota_leave=leave_pay[0][0]*number_of_day_present[0][0]

		other=get_other(pf)
#get the total other pay  for a time span and for a particular emp
		total_other=other[0][0]*number_of_day_present[0][0]

#get the total addative value  for a time span and for a particular emp
		total_addition=total_other+total_sick+total_pay+total_maternity+tota_leave+total_food_conssesion+total_l_piece



		# DEDUCTION RELATED
		p_per_fund=get_pay(pf)
#get the total pf fun for a time span and for a particular emp which is 12% of the basic
		total_p_per_fund=total_addition*0.12

		kharcha=get_kharcha(pf)
#get the total kharcha for a time span and for a particular emp
		total_kharcha=kharcha[0][0]*number_of_day_present[0][0]

		lp_paid=get_lp_paid(pf)
#get the total lp paid for a time span and for a particular emp
		total_lp_paid=lp_paid[0][0*number_of_day_present[0][0]]

		advance=get_advance(pf)  
#get the total advance for a time span and for a particular emp
		total_advance=advance[0][0]*number_of_day_present[0][0]

		ration=get_ration(pf)
#get the total ration for a time span and for a particular emp
		total_ration=ration[0][0]*number_of_day_present[0][0]

		electricity=get_electricity(pf)
#get the total electricity for a time span and for a particular emp
		total_electricity=electricity[0][0]*number_of_day_present[0][0]

		lic=get_lic(pf)
#get the total lic for a time span and for a particular emp
		total_lic=lic[0][0]*number_of_day_present[0][0]

#get the total deduction for a time span and for a particular emp
		total_deduction=total_p_per_fund+total_kharcha+total_lp_paid+total_advance+total_ration+total_electricity+total_lic

		gross_pay=total_addition-(total_deduction+total_food_conssesion)

		net_pay=gross_pay-(gross_pay%10)
		
		carry_forward=gross_pay%10

		b_forward=0
		
		data.append([sle.emp_code,sle.name1,desig,number_of_day_present,present_as_special_cat,present_as_normal_cat,pf,round(pay[0][0]*number_of_day_present[0][0],2),round(food_conssesion[0][0]*number_of_day_present[0][0],2),round(l_piece[0][0]*number_of_day_present[0][0],2),round(sick[0][0]*number_of_day_present[0][0],2),round(maternity[0][0]*number_of_day_present[0][0],2),round(leave_pay[0][0]*number_of_day_present[0][0],2),round(other[0][0]*number_of_day_present[0][0],2),round(total_addition,2),round(total_addition*0.12,0),round(kharcha[0][0]*number_of_day_present[0][0],2),round(lp_paid[0][0]*number_of_day_present[0][0],2),round(advance[0][0]*number_of_day_present[0][0],2),round(ration[0][0]*number_of_day_present[0][0],2),round(electricity[0][0]*number_of_day_present[0][0],2),round(lic[0][0]*number_of_day_present[0][0],2),round(total_deduction,2),round(gross_pay,2),round(b_forward,2),round(net_pay,2),round(carry_forward,2)])
		

		
	return columns, data

				# SOME BASIC INFORMATION RELATED TO THE REPORT #
#--------------------------------------------------------------------------------------
#fetch labour name and code from attendence table
def get_report_entries(filters):
	return frappe.db.sql(""" select distinct  emp_code,name1 from `tabattendence` where date between %s  and %s  order by date asc""",(filters.date1,filters.date2),as_dict=1)

# get the number of days the labour worked within the time span
def get_number_of_days_work(emp_code):
	return frappe.db.sql(""" select count(attendance_3rd_char_1) from `tabattendence` where emp_code=%s order by date asc""",(emp_code))


def get_number_of_days_work_as_special(emp_code,filters):
	return frappe.db.sql(""" select count(attendance_3rd_char_1) from `tabattendence` where emp_code=%s and  attendance_3rd_char_1="Special Category"  and  date between %s  and %s order by date asc""",(emp_code,filters.date1,filters.date2))

def get_number_of_days_work_as_normal(emp_code,filters):
	return frappe.db.sql(""" select count(attendance_3rd_char_1) from `tabattendence` where emp_code=%s and  attendance_3rd_char_1="Normal Category"  and  date between %s  and %s order by date asc""",(emp_code,filters.date1,filters.date2))

# get the category in which the labour belongs to
def get_des_category(emp_code):
	return frappe.db.sql(""" select category from `tabLabour Information` where emp_id=%s""",(emp_code))


#get the pf no of the labour
def get_pf_no(emp_code):
	return frappe.db.sql(""" select pf_no from `tabLabour Information` where emp_id=%s""",(emp_code))

#--------------------------------------------------------------------------------------

# EVERYTHING RELATED TO ADDITION

# Select additive the values from salary structure

def get_pay(pf):
	return frappe.db.sql(""" select sum(pay) from `tabSalary Structure`  where pf_no = %s group by pf_no""",(pf))


def get_food_conssesion(pf):
	return frappe.db.sql(""" select sum(food_conssesion) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_l_piece(pf):
	return frappe.db.sql(""" select sum(l_piece) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_sick(pf):
	return frappe.db.sql(""" select sum(sick) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_maternity(pf):
	return frappe.db.sql(""" select sum(maternity) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_leave_pay(pf):
	return frappe.db.sql(""" select sum(leave_pay) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_other(pf):
	return frappe.db.sql(""" select sum(other) from `tabSalary Structure` where pf_no = %s""",(pf))

#--------------------------------------------------------------------------------------

# EVERYTHING RELATED TO DEDUCTION

# Select deductive values from salary structure

#def get_p_per_fund(pf):
	#return frappe.db.sql(""" select sum(p_per_fund) from `tabSalary Structure` where pf_no = %s """,(pf))


def get_kharcha(pf):
	return frappe.db.sql(""" select sum(kharcha) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_lp_paid(pf):
	return frappe.db.sql(""" select sum(lp_paid) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_advance(pf):
	return frappe.db.sql(""" select sum(advance) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_ration(pf):
	return frappe.db.sql(""" select sum(ration) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_electricity(pf):
	return frappe.db.sql(""" select sum(electricity) from `tabSalary Structure` where pf_no = %s""",(pf))


def get_lic(pf):
	return frappe.db.sql(""" select sum(lic) from `tabSalary Structure` where pf_no = %s""",(pf))


#--------------------------------------------------------------------------------------

# THE COLUMNS SHOWN IN THE REPORT


def get_columns():
		
		columns = [{
				"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 90
	    }]
		
		columns.append({
				"fieldname": "name1",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "attendance_2nd_char",
				"label": _("Designated Category"),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 90
	    })

	    	

	    	
	    	columns.append({
				"fieldname": "count_attendance_3rd_char_1",
				"label": _(" Total Persent "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "count_attendance_special",
				"label": _(" Special "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "count_attendance_normal",
				"label": _(" Normal "),
				"fieldtype": "Data",
				"option":"attendence",
				"width": 120
	    })

	    	columns.append({
				"fieldname": "pf_no",
				"label": _("PF No"),
				"fieldtype": "Data",
				"option":"Labour Information",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "pay",
				"label": _("Pay"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "food_conssesion",
				"label": _("Food Conssesion"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "l_piece",
				"label": _("L/Piece"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "sick",
				"label": _("Sick"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "maternity",
				"label": _("Maternity"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "leave_pay",
				"label": _("Leave Pay"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "other",
				"label": _("Other"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "total_addition",
				"label": _("After Addition"),
				"fieldtype": "Float",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "p_per_fund",
				"label": _("P/Fund"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "kharcha",
				"label": _("Kharcha"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "lp_paid",
				"label": _("Lp Paid"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "advance",
				"label": _("Advance"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "ration",
				"label": _("Ration"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "electricity",
				"label": _("Electricity"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "lic",
				"label": _("LIC"),
				"fieldtype": "Float",
				"option":"Salary Structure",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "total_deduction",
				"label": _("After Deduction"),
				"fieldtype": "Float",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "gross_amount",
				"label": _("Gross Amount"),
				"fieldtype": "Float",
				"width": 90
	    })

	    	
	    	columns.append({
				"fieldname": "b_forward",
				"label": _("Brought Forward"),
				"fieldtype": "Float",
				"width": 90
	    })



	    	columns.append({
				"fieldname": "net_amount",
				"label": _("Net Amount"),
				"fieldtype": "Float",
				"width": 90
	    })


	    	columns.append({
				"fieldname": "carry_forward",
				"label": _("Carry Forward"),
				"fieldtype": "Float",
				"width": 90
	    })



		return columns
