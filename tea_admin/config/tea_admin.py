from __future__ import unicode_literals
from frappe import _

def get_data():
	return [


		{
			"label": _("Transaction"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Wages Entry",
					"description": _("Default settings for buying transactions.")
				},

				{
					"type": "doctype",
					"name": "Make Payment",
					"description": _("Default settings for buying transactions.")
				},

				{
					"type": "doctype",
					"name": "Salary for Staff",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},


		{
			"label": _("Setup files"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Labour Information",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},


		{
			"label": _("Benefits Information"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Medical Benefit Entry",
					"description": _("Default settings for buying transactions.")
				},

				{
					"type": "doctype",
					"name": "Other Benefit Entry",
					"description": _("Default settings for buying transactions.")
				}
		
		]
		},

		{
			"label": _("House Information"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "House Repairing Entry",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},


		{
			"label": _("Leave"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Leave Application",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},

		

		{
			"label": _("Ration"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Ration Distribution",
					"description": _("Default settings for buying transactions.")
				}

				
		]
		},






		{
			"label": _("Reports"),
			"icon": "icon-cog",
			"items": [
				
				{
					"type": "report",
					"is_query_report": True,
					"name": "Pay Book",
					"doctype": "Salary Structure",
				},

				{
					"type": "report",
					"is_query_report": True,
					"name":"Consolodate Statement",
					"doctype": "Salary Structure",
				},

				{
					"type": "report",
					"is_query_report": True,
					"name":  "Wages Summary",
					"doctype": "Salary Structure",
				},

				{
					"type": "report",
					"is_query_report": True,
					"name": "Leaf Pice Payment",
					"doctype": "Salary Structure",
				}
			]
		},


		{
			"label": _("Attendance"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Attendance Sheet",
					"doctype": "Wages Entry",
				}
			]
		},


		{
			"label": _("Payment"),
			"icon": "icon-cog",
			"items": [
			{
					"type": "doctype",
					"name": "Make Payment",
					
				}
				
			]
		},



		{
			"label": _("Medical Reports"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Sick Register",
					"doctype": "Wages Entry",
				}
			]
		},




	]
