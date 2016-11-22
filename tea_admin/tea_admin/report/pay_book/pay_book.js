// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Pay Book"] = {
	"filters": [
	{
            "fieldname":"date1",
            "label": __("FROM DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":0
        },

    {
            "fieldname":"date2",
            "label": __(" TO DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":0
        },
	{

            "fieldname":"garden",
            "label": __("Garden"),
            "fieldtype": "Link",
            "options":"Estate",
            "default":"",
            "reqd":0



        }

	]
}
