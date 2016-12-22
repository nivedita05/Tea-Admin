// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt


frappe.ui.form.on('Make Payment', {
	refresh: function(frm) {

	}
});


cur_frm.fields_dict['pay'].grid.get_field('emp_code').get_query = function(doc, cdt, cdn) {
    var d = locals[cdt][cdn]
    return {
        filters: [
            ['Labour Information', 'book_code', '=', doc.book_code]
        ]
    }
}



frappe.ui.form.on('Make Payment', {

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

  	{fieldname:'from_date', fieldtype:'Date', label: __('From Date')},
  	{fieldname:'to_date', fieldtype:'Date', label: __('To Date')},
  	{fieldname:'payment_date', fieldtype:'Date', label: __('Payment Date')},
    {fieldname:'book_code', fieldtype:'Link', options: 'Salary Structure', label: __('Book Code')},
    {fieldname:'garden', fieldtype:'Link', options: 'Estate', label: __('Garden')},
    
  ]
});
frm.$emp_dialog.set_primary_action(__("Add"), function() {
  frm.trigger('get_employees');
});
frm.$emp_dialog.show();
},

get_employees:function (frm) {
    var filters = frm.$emp_dialog.get_values();
    if ('from_date' in filters) {
      delete filters.from_date
    }
    if ('to_date' in filters) {
      delete filters.to_date
    }
    if ('payment_date' in filters) {
      delete filters.payment_date
    }

    
    frappe.call({
      method:'tea_admin.tea_admin.doctype.wages_entry.wages_entry.get_employees',
      args:{
        filters: filters
      },
      callback:function (r) {
        var pay = $.map(frm.doc.pay, function(d) { return d.pay });
        frm.set_value("garden",filters.garden)
        frm.set_value("book_code",filters.book_code)
        frm.set_value("from_date",frm.$emp_dialog.get_value('from_date'))
        frm.set_value("to_date",frm.$emp_dialog.get_value('to_date'))
        frm.set_value("payment_date",frm.$emp_dialog.get_value('payment_date'))
        

        for (var i=0; i< r.message.length; i++) {
          if (pay.indexOf(r.message[i].name1) === -1) {
            var row = frappe.model.add_child(frm.doc, frm.fields_dict.pay.df.options, frm.fields_dict.pay.df.fieldname);
            row.emp_name = r.message[i].name1;
            row.emp_code= r.message[i].emp_id;
            row.to_date= frm.$emp_dialog.get_value('to_date');
            row.from_date= frm.$emp_dialog.get_value('from_date');
            row.book_code= frm.$emp_dialog.get_value('book_code');
            
          }
        }
        frm.refresh_field('pay');
        frm.$emp_dialog.hide()
      }
    })
}


});
