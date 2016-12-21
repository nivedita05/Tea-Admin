# Copyright (c) 2013, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
import math
import datetime

def execute(filters=None):
	data = []
	columns=get_columns()
	total_task_wk_1=0
	payment=1
	payment_for_extra_upto_6=1
	payment_for_extra_after_6=1.5
	now=datetime.datetime.now()
	month=now.month


	emp_code_and_name=get_emp_name_code(filters)

	for sle in emp_code_and_name:
		sirdar=get_sirdar(sle.name1)

		task_day1=get_task_for_a_date_1(filters,sle.name1,sle.date)
		task_day2=get_task_for_a_date_2(filters,sle.name1,sle.date)
		task_day3=get_task_for_a_date_3(filters,sle.name1,sle.date)
		task_day4=get_task_for_a_date_4(filters,sle.name1,sle.date)
		task_day5=get_task_for_a_date_5(filters,sle.name1,sle.date)
		task_day6=get_task_for_a_date_6(filters,sle.name1,sle.date)
		task_day7=get_task_for_a_date_7(filters,sle.name1,sle.date)


		pluc_day1=get_pluc_for_a_date_1(filters,sle.name1,sle.date)
		pluc_day2=get_pluc_for_a_date_2(filters,sle.name1,sle.date)
		pluc_day3=get_pluc_for_a_date_3(filters,sle.name1,sle.date)
		pluc_day4=get_pluc_for_a_date_4(filters,sle.name1,sle.date)
		pluc_day5=get_pluc_for_a_date_5(filters,sle.name1,sle.date)
		pluc_day6=get_pluc_for_a_date_6(filters,sle.name1,sle.date)
		pluc_day7=get_pluc_for_a_date_7(filters,sle.name1,sle.date)


		total_task_wk_1=get_task_for_1stwk(filters,sle.name1,sle.date)
		total_pluc_wk_1=get_pluc_for_1stwk(filters,sle.name1,sle.date)

		

		payment_for_1st_wk=total_task_wk_1
		extra_pluck_done=total_pluc_wk_1[0][0]-total_task_wk_1[0][0]
		if extra_pluck_done<=6:
			payment_for_1st_wk=extra_pluck_done*3
		else:
			extra_pluck_after_6=(extra_pluck_done-6)*3.5
			payment_for_1st_wk=18+extra_pluck_after_6
			

		

		task_day8=get_task_for_a_date_8(filters,sle.name1,sle.date)
		task_day9=get_task_for_a_date_9(filters,sle.name1,sle.date)
		task_day10=get_task_for_a_date_10(filters,sle.name1,sle.date)
		task_day11=get_task_for_a_date_11(filters,sle.name1,sle.date)
		task_day12=get_task_for_a_date_12(filters,sle.name1,sle.date)
		task_day13=get_task_for_a_date_13(filters,sle.name1,sle.date)
		task_day14=get_task_for_a_date_14(filters,sle.name1,sle.date)
		

		pluc_day8=get_pluc_for_a_date_8(filters,sle.name1,sle.date)
		pluc_day9=get_pluc_for_a_date_9(filters,sle.name1,sle.date)
		pluc_day10=get_pluc_for_a_date_10(filters,sle.name1,sle.date)
		pluc_day11=get_pluc_for_a_date_11(filters,sle.name1,sle.date)
		pluc_day12=get_pluc_for_a_date_12(filters,sle.name1,sle.date)
		pluc_day13=get_pluc_for_a_date_13(filters,sle.name1,sle.date)
		pluc_day14=get_pluc_for_a_date_14(filters,sle.name1,sle.date)

		total_task_wk_2=get_task_for_2ndwk(filters,sle.name1,sle.date)
		total_pluc_wk_2=get_pluc_for_2ndwk(filters,sle.name1,sle.date)



		payment_for_2nd_wk=total_task_wk_2
		extra_pluck_done=total_pluc_wk_2[0][0]-total_task_wk_2[0][0]
		if extra_pluck_done<=6:
			payment_for_2nd_wk=extra_pluck_done*3
		else:
			extra_pluck_after_6=(extra_pluck_done-6)*3.5
			payment_for_2nd_wk=18+extra_pluck_after_6
			



		data.append([sle.emp_code,sle.name1,sirdar,"Task",task_day1,task_day2,task_day3,task_day4,task_day5,task_day6,task_day7,task_day8,task_day9,task_day10,task_day11,task_day12,task_day13,task_day14,total_task_wk_1,payment_for_1st_wk,total_task_wk_2,payment_for_2nd_wk])
		data.append(["","","","Pluc",pluc_day1,pluc_day2,pluc_day3,pluc_day4,pluc_day5,pluc_day6,pluc_day7,pluc_day8,pluc_day9,pluc_day10,pluc_day11,pluc_day12,pluc_day13,pluc_day14,total_pluc_wk_1,'',total_pluc_wk_2])
	return columns, data


def get_emp_name_code(filters):
	return frappe.db.sql("""select distinct emp_code,name1 from `tabattendence` where garden=%s and attendance_2nd_char="P-plucking" and date between %s and %s order by emp_code""",(filters.garden,filters.date1,filters.date2),as_dict=1)

def get_sirdar(name1):
	return frappe.db.sql("""select sirdar from `tabLabour Information` where name1=%s""",(name1))


#1ST WK TASK
#---------

def get_task_for_a_date_1(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-01",name1))

def get_task_for_a_date_2(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-02",name1))

def get_task_for_a_date_3(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-03",name1))

def get_task_for_a_date_4(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-04",name1))

def get_task_for_a_date_5(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-05",name1))

def get_task_for_a_date_6(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-06",name1))

def get_task_for_a_date_7(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-07",name1))

def get_task_for_1stwk(filters,name1,date):
	return frappe.db.sql("""select sum(quantity_to_be_plucked) from `tabattendence` where garden=%s and date between %s and %s and  name1=%s """,(filters.garden,"2016-10-31","2016-11-07",name1))



#1ST WK PLUC
#---------


def get_pluc_for_a_date_1(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-01",name1))

def get_pluc_for_a_date_2(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-02",name1))

def get_pluc_for_a_date_3(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-03",name1))

def get_pluc_for_a_date_4(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-04",name1))

def get_pluc_for_a_date_5(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-05",name1))

def get_pluc_for_a_date_6(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-06",name1))

def get_pluc_for_a_date_7(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-07",name1))

def get_pluc_for_1stwk(filters,name1,date):
	return frappe.db.sql("""select sum(quantity) from `tabattendence` where garden=%s and date between %s and %s and  name1=%s """,(filters.garden,"2016-10-31","2016-11-07",name1))



#2ND WK TASK
#--------

def get_task_for_a_date_8(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-08",name1))

def get_task_for_a_date_9(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-09",name1))


def get_task_for_a_date_10(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-10",name1))

def get_task_for_a_date_11(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-11",name1))


def get_task_for_a_date_12(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-12",name1))

def get_task_for_a_date_13(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-13",name1))


def get_task_for_a_date_14(filters,name1,date):
	return frappe.db.sql("""select quantity_to_be_plucked from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-14",name1))

def get_task_for_2ndwk(filters,name1,date):
	return frappe.db.sql("""select sum(quantity_to_be_plucked) from `tabattendence` where garden=%s and date between %s and %s and  name1=%s """,(filters.garden,"2016-11-08","2016-11-14",name1))


#2ND WK PLUC
#--------


def get_pluc_for_a_date_8(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-01",name1))

def get_pluc_for_a_date_9(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-02",name1))

def get_pluc_for_a_date_10(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-03",name1))

def get_pluc_for_a_date_11(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-04",name1))

def get_pluc_for_a_date_12(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-05",name1))

def get_pluc_for_a_date_13(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-06",name1))

def get_pluc_for_a_date_14(filters,name1,date):
	return frappe.db.sql("""select quantity from `tabattendence` where garden=%s and date=%s and name1=%s """,(filters.garden,"2016-11-07",name1))

def get_pluc_for_2ndwk(filters,name1,date):
	return frappe.db.sql("""select sum(quantity) from `tabattendence` where garden=%s and date between %s and %s and  name1=%s """,(filters.garden,"2016-11-08","2016-11-14",name1))








def get_columns():
		
		columns = [{
				"fieldname": "emp_code",
				"label": _("Emp Code"),
				"fieldtype": "Data",
				"width": 120
	    }]
		

	    	columns.append({
				"fieldname": "emp_name",
				"label": _("Emp Name"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	

	    	columns.append({
				"fieldname": "sirdar",
				"label": _("Sirdar"),
				"fieldtype": "Data",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "a",
				"label": _(""),
				"fieldtype": "Data",
				"width": 80
	    })

	    	
	    	columns.append({
				"fieldname": "day1",
				"label": _("day1"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day2",
				"label": _("day2"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day3",
				"label": _("day3"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day4",
				"label": _("day4"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day5",
				"label": _("day5"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day6",
				"label": _("day6"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day7",
				"label": _("day7"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "day8",
				"label": _("day8"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "day9",
				"label": _("day9"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "day10",
				"label": _("day10"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day11",
				"label": _("day11"),
				"fieldtype": "Int",
				"width": 80
	    })
	    	columns.append({
				"fieldname": "day12",
				"label": _("day12"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "day13",
				"label": _("day13"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "day14",
				"label": _("day14"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "wk1_task",
				"label": _("wk1 task"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "wk1_task_amt",
				"label": _("wk1 task amount"),
				"fieldtype": "Float",
				"width": 80
	    })


	    	columns.append({
				"fieldname": "wk2_task",
				"label": _("wk2 task"),
				"fieldtype": "Int",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "wk2_task_amt",
				"label": _("wk2 task amount"),
				"fieldtype": "Float",
				"width": 80
	    })

	    	columns.append({
				"fieldname": "chk",
				"label": _(""),
				"fieldtype": "Date",
				"width": 180
	    })



	    	
		return columns