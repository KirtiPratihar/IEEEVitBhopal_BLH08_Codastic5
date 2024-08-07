document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let fileInput = document.getElementById('csv-file');
    let file = fileInput.files[0];
    
    let formData = new FormData();
    formData.append('csv-file', file);
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display Pygwalker visualization
        document.getElementById('visualization').innerHTML = data.html;
    });
});
