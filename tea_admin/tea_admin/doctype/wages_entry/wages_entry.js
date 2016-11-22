// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Wages Entry", "validate", function(frm) {
  for(var i in frm.doc.attendence){
     frm.doc.attendence[i].date = frm.doc.date;
     }
  });


frappe.ui.form.on("Wages Entry", "button_13", function(frm) {  
      frappe.set_route("data-import-tool")
});