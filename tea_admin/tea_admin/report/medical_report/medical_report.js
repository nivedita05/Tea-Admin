// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Medical Report"] = {
	"filters": [
    {
            "fieldname":"date",
            "label": __("DATE"),
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



        },

        {

            "fieldname":"company_name",
            "label": __("Company"),
            "fieldtype": "Select",
            "options":["Rungamattee", "Rawjute"],
            "default": "",
            "reqd":0



        },


       
        {

            "fieldname":"type_of_treatment",
            "label": __("Type of Treatment"),
            "fieldtype": "Select",
            "options":["Outdoor", "Indoor"],
            "default": "",
            "reqd":0



        }
    ]
}
