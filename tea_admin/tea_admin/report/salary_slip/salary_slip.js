// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Salary slip"] = {
	"filters": [

	
    {
            "fieldname":"date",
            "label": __(" DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":1
        },
	{

            "fieldname":"garden",
            "label": __("Garden"),
            "fieldtype": "Link",
            "options":"Estate",
            "default":"",
            "reqd":1



        },
    {

            "fieldname":"book_code",
            "label": __("Book Code"),
            "fieldtype": "Link",
            "options":"Salary Structure",
            "default":"",
            "reqd":1



        }




	]
}
