# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.utils import cstr, flt
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe import _
from frappe import utils
from frappe.desk.notifications import clear_doctype_notifications
from dateutil.relativedelta import relativedelta

class WagesEntry(Document):

	# ADDITIONAL FIELD FUNCTION CALLING
	def validate(self):

		self.get_task()
		self.get_base_task()
		self.get_pay()
		self.get_fc()
		self.get_l_piece()
		self.get_sick()
		self.get_maternity()
		self.get_leave_pay()
		self.get_other()
		


	
		
# GET ADDITIONAL FIELDS 
	
	

	def get_pay(self):
		for i in self.get('attendence'):

			pay = frappe.db.sql("""select pay from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if pay:
				if(i.attendence=="PRESENT" or i.attendence=="HOLIDAY"):
					i.pay =str(round(pay[0][0],2))
				
				elif (i.attendence=="HALF DAY"):
					i.pay =str(round(pay[0][0]/2,2))
			
			#elif (i.attendence=="SICK"):
				#i.pay =str(round(pay[0][0]*2/3,2))

				elif (i.attendence=="LEAVE"):
					i.pay =	"0.0"


				else:
					i.pay="0.0"

	
	def get_task(self):
		for i in self.get('attendence'):
			task = frappe.db.sql("""select task from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if task:
				i.quantity_to_be_plucked =str(round(task[0][0]))
			else:
				i.quantity_to_be_plucked="0.0"
			


	def get_base_task(self):
		for i in self.get('attendence'):

			base_task = frappe.db.sql("""select task from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if base_task:
				if(i.attendence=="HOLIDAY" or i.attendence=="MATERNITY" or i.attendence=="SICK" or i.attendence=="LEAVE" or i.attendence=="ABSENT" or i.attendance_2nd_char=="FACTORY" or i.attendance_2nd_char=="MISCELLANEOUS"):
					i.base_task="0.0"
					i.quantity="0.0"
				else:
					if(i.attendance_3rd_char=="Non Peak Period"):
						i.base_task= str(round(base_task[0][0]*0.70,2))
					if(i.attendance_3rd_char=="Peak Period" and i.round_days =="8"):
						i.base_task= str(round(base_task[0][0],2))	
					if(i.attendance_3rd_char=="Peak Period" and i.round_days=="7"):
						i.base_task= str(round(base_task[0][0]*0.85,2))	
					if(i.attendance_3rd_char=="Peak Period" and i.round_days=="6"):
						i.base_task= str(round(base_task[0][0]*0.70,2))	
					if(i.attendance_3rd_char=="Peak Period" and i.round_days>="1" and i.round_days<="5"):
						i.base_task= str(round(base_task[0][0]*0.60,2))	
					if(i.attendance_3rd_char=="Peak Period" and i.round_days =="10"):
						i.base_task= str(round(base_task[0][0],2))	
					



	def get_fc(self):
		for i in self.get('attendence'):
			food_conssesion = frappe.db.sql("""select food_conssesion from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if food_conssesion:
				i.food_conssesion = str(round(food_conssesion[0][0],2))
			else:
				i.food_conssesion="0.0"
			

	
	def get_l_piece(self):
		for i in self.get('attendence'):
			l_piece = frappe.db.sql("""select l_piece from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if l_piece:
				i.l_piece = str(round(l_piece[0][0],2))
			else:
				i.l_piece="0.0"
			



	def get_sick(self):
		for i in self.get('attendence'):
			if(i.attendence=="SICK"):
				sick = frappe.db.sql("""select sick from `tabSalary Structure` where book_code=%s""",(self.book_code))
				i.sick = str(round(sick[0][0],2))
			else:
				i.sick="0.0"

	def get_maternity(self):
		for i in self.get('attendence'):
			if(i.attendence=="MATERNITY"):
				gender=frappe.db.sql("""select gender1 from `tabLabour Information` where emp_id=%s""",(i.emp_code))
				if (gender[0][0]=="Female"):
					maternity = frappe.db.sql("""select maternity from `tabSalary Structure` where book_code=%s""",(self.book_code))
					i.maternity = str(round(maternity[0][0],2))
			else:
				i.maternity = "0.0"
			

	def get_leave_pay(self):
		for i in self.get('attendence'):
			leave_pay = frappe.db.sql("""select leave_pay from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if leave_pay:
				i.leave_pay =str(round(leave_pay[0][0],2))
			else:
				i.leave_pay="0.0"
			


	def get_other(self):
		for i in self.get('attendence'):
			other = frappe.db.sql("""select other from `tabSalary Structure` where book_code=%s""",(self.book_code))
			if other:
				i.other = str(round(other[0][0],2))
			else:
				i.other="0.0"
			


@frappe.whitelist()
def get_employees(**args):
	return frappe.get_list('Labour Information',filters=args['filters'], fields=['name1','emp_id','book_code','garden'])