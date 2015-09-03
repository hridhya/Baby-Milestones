$(document).ready(function() {
	$("#submitbutton").click(function () {
     			var msg = $('#name').val() + "\n" + $('#datepicker').val() + "\n" + $('#gender').val();
					
   	  			$.ajax({
    				url: "/start_album",
    				type: "POST",
    				data: JSON.stringify(msg),
    				contentType: "application/json; charset=utf-8",
    				success: function(dat) { console.log(dat); }
				});
     		});




});