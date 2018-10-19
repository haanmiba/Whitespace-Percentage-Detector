$(function() {
	$('#upload-file-btn').click(function() {
		var inputLink = document.createElement('input');
		inputLink.id = 'select-file-btn';
		inputLink.name = 'file';
		inputLink.type = 'file';
		inputLink.accept = 'image/png, image/jpg';
		inputLink.style = 'visibility:hidden;position:relative;display:block;line-height:0;height:0;overflow:hidden;';
		$('#upload-file').append(inputLink);
		inputLink.click();
		$(inputLink).change(function() {
	        var form_data = new FormData($('#upload-file')[0]);
	        $('#upload-file-btn').addClass('loading');
	        $.ajax({
	            type: 'POST',
	            url: '/detect-whitespace',
	            data: form_data,
	            contentType: false,
	            cache: false,
	            processData: false,
	            success: function(data) {
	                console.log(data);
	                document.getElementById('results').innerHTML = "";
	                var node = document.createElement('p');
	                var textnode = document.createTextNode('This image is ' + data + ' white!');
	                node.appendChild(textnode);
	                $('#results').append(node);
	                $('#upload-file-btn').removeClass('loading');
	                inputLink.remove();
	            },
	            error: function (request, status, error) {
	                document.getElementById('results').innerHTML = "";
	                var node = document.createElement('p');
	                var textnode = document.createTextNode('This file was unable to be read.');
	                node.append(textnode);
	                $('#results').append(node);
	                $('#upload-file-btn').removeClass('loading');
	                inputLink.remove();
	            }
	        });
	    });
	});
});