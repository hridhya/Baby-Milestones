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
     		
     $("#babynames").click(function () {
     	$.getJSON('/baby_names', function(data) {
			console.log(data.result.length);
			var i = 1;
			var elements = [];
			for(x = 0; x < data.result.length; x++) {
				
    			var element = $('<div>'+ i + ". " +data.result[x]+'</div>' + '</br>');
    			elements.push(element);
    			i = i+1;
    			
			}
			$('#result').append(elements);
			
		});
	});
});