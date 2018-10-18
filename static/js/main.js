$(function() {
    $('#select-file-btn').change(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/detect-whitespace',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                /*
                document.getElementById('results').innerHTML = "";
                var node = document.createElement('p');
                var textnode = document.createTextNode('This image is ' + data + ' white!');
                node.appendChild(textnode);
                document.getElementById('results').appendChild(node);
                */
                console.log(data);
            },
        });
    });
});