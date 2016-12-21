// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Wages Entry", "validate", function(frm) {
  frm.attn_id="";
  
  name=frm.doc.date+":"+frm.doc.book_code;
  frm.set_value("attn_id",name);   
});



frappe.ui.form.on("Wages Entry", "button_13", function(frm) {  
      frappe.set_route("data-import-tool")
});

//cur_frm.add_custom_button(__('Get Employee from Book'), this.make_wages_entry, __("Get Items"));

cur_frm.fields_dict['attendence'].grid.get_field('emp_code').get_query = function(doc, cdt, cdn) {
    var d = locals[cdt][cdn]
    return {
        filters: [
            ['Labour Information', 'book_code', '=', doc.book_code]
        ]
    }
}






frappe.ui.form.on('Wages Entry', {

refresh: function(frm) {
    frm.trigger("toggle_fields");
    frm.add_custom_button(__("Add Employees"),function () {
      frm.trigger('add_employees')
    })
    
  },


add_employees:function (frm) {
frm.$emp_dialog = new frappe.ui.Dialog({
  title: __("Add Employees"),
  fields: [
    {fieldname:'date', fieldtype:'Date', label: __('Date')},
    {fieldname:'book_code', fieldtype:'Link', options: 'Salary Structure', label: __('Book Code')},
    {fieldname:'garden', fieldtype:'Link', options: 'Estate', label: __('Garden')}
    
  ]
});
frm.$emp_dialog.set_primary_action(__("Add"), function() {
  frm.trigger('get_employees');
});
frm.$emp_dialog.show();
},

get_employees:function (frm) {
    var filters = frm.$emp_dialog.get_values();
    if ('date' in filters) {
      delete filters.date
    }

    frappe.call({
      method:'tea_admin.tea_admin.doctype.wages_entry.wages_entry.get_employees',
      args:{
        filters: filters
      },
      callback:function (r) {
        var attendence = $.map(frm.doc.attendence, function(d) { return d.attendence });
        frm.set_value("garden",filters.garden)
        frm.set_value("book_code",filters.book_code)
        frm.set_value("date",frm.$emp_dialog.get_value('date'))


        for (var i=0; i< r.message.length; i++) {
          if (attendence.indexOf(r.message[i].name1) === -1) {
            var row = frappe.model.add_child(frm.doc, frm.fields_dict.attendence.df.options, frm.fields_dict.attendence.df.fieldname);
            row.name1 = r.message[i].name1;
            row.emp_code= r.message[i].emp_id;
            row.book_code=r.message[i].book_code;
            row.garden= r.message[i].garden;
            row.date = frm.$emp_dialog.get_value('date');                                 
            if(row.date>="2016-05-15" && row.date<="2016-10-31"){
              row.attendance_3rd_char="Peak period";
            }
            if(row.date>="2016-11-01" && row.date<="2017-05-14"){
              row.attendance_3rd_char=" Non Peak period";
            }
            
          }
        }
        frm.refresh_field('attendence');
        frm.$emp_dialog.hide()
      }
    })
}


});



frappe.ui.form.on('Wages Entry', {

refresh: function(frm) {
    frm.trigger("toggle_fields");
    frm.add_custom_button(__("Upload"),function () {
      frm.trigger('upload')
    })
    
  }
});





frappe.ui.form.on("Wages Entry", "validate", function(frm) {
  for(var i in frm.doc.attendence){
    if(frm.doc.date>="2016-05-15" && frm.doc.date<="2016-10-31"){
      frm.doc.attendence[i].attendance_3rd_char="Peak Period";
   }
    if(frm.doc.date>="2016-11-01" && frm.doc.date<="2017-05-14" ){
    frm.doc.attendence[i].attendance_3rd_char="Non Peak Period";
    }
   if(frm.doc.attendence[i].attendance_2nd_char==="F-factory"){
    frm.doc.attendence[i].attendance_3rd_char="NA";
    }
   if(frm.doc.attendence[i].attendance_2nd_char==="O-miscellaneous"){
     frm.doc.attendence[i].attendance_3rd_char="NA";
    }
    
    
   }
 });

