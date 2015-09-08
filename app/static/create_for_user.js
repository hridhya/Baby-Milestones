$(document).ready(function() {
	$("#submitbutton1").click(function () {
     			var msg = $('#datepicker').val() + "\n" + $('#title').val() + "\n" + $('#details').val();
					
   	  			$.ajax({
    				url: "/add_milestone_new",
    				type: "POST",
    				data: JSON.stringify(msg),
    				contentType: "application/json; charset=utf-8",
    				success: function(dat) { console.log(dat); }
				});
     		});

});