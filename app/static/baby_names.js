$(document).ready(function() {
	$.getJSON('/baby_names', function(data) {
			var list = document.getElementById("mydropdown"); 
			for(x = 0; x < data.result['baby_names'].length; x++) {
				var li = document.createElement("li");
            	var link = document.createElement("a");             
            	var text = document.createTextNode(data.result['baby_names'][x]);
            	link.appendChild(text);
            	link.href = "/view_milestone" + data.result['id'][x];
            	li.appendChild(link);
            	list.appendChild(li);
    			
    			
			}
			
			
	});         
});                     