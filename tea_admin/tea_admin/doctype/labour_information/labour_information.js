// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Labour Information", "validate", function(frm) {
    frm.lab_id="";
    name=frm.doc.abb+"-"+frm.doc.emp_code;
    frm.set_value("lab_id",name);
});


frappe.ui.form.on("Labour Information", "validate", function(frm) {

	var birth_date=frm.doc.dob
	var ret_date=frappe.datetime.add_days(birth_date,60*365)
   
    frm.set_value("dor",ret_date);
});

frappe.ui.form.on("Labour Information", "validate", function(frm) {
    if (frm.doc.name1===frm.doc.head_of_the_family_name){
    	frm.set_value("is_dependent","No");
    	frm.set_value("dependent_name",frm.doc.head_of_the_family_name)
    }
    else {
    	frm.set_value("is_dependent","Yes");
    	frm.set_value("dependent_name",frm.doc.head_of_the_family_name)
    }
       
});

frappe.ui.form.on("Labour Information", "validate", function(frm) {
  for(var i in frm.doc.salary_structure){
     frm.doc.salary_structure[i].category = frm.doc.category;
     }
  });
   