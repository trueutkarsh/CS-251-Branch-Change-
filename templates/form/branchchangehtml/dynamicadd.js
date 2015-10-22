$(document).ready(function(){
    $("#pref1").change(function(){
        
      
	var newTextBoxDiv = $(document.createElement('div'))
	     .attr("id", 'TextBoxDiv');
                
	newTextBoxDiv.after().html('<label>Textbox #'+ counter + ' : </label>' +
	      '<input type="text" name="textbox' + 
	      '" id="textbox' + '" value="" >');
            
	newTextBoxDiv.appendTo("#pref1");
    });
});