from flask import Flask, render_template, request, jsonify
import pandas as pd
import pygwalker as pyg

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CSV Visualization</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: var(--background-color);
                color: var(--text-color);
                transition: background-color 0.3s, color 0.3s;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
            }
            h1 {
                text-align: center;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 10px;
            }
            input[type="file"] {
                border: 1px solid #ccc;
                padding: 5px;
                border-radius: 5px;
            }
            button {
                background-color: #007bff;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            #visualization {
                margin-top: 20px;
            }
            .theme-toggle {
                position: fixed;
                top: 20px;
                right: 20px;
                cursor: pointer;
                padding: 10px;
                border-radius: 50%;
                background-color: var(--toggle-background);
                color: var(--toggle-color);
                border: 2px solid var(--toggle-border);
            }
            .dark-mode {
                --background-color: #121212;
                --text-color: #e0e0e0;
                --toggle-background: #333;
                --toggle-color: #fff;
                --toggle-border: #444;
            }
            .light-mode {
                --background-color: #f0f0f0;
                --text-color: #000;
                --toggle-background: #fff;
                --toggle-color: #000;
                --toggle-border: #ccc;
            }
        </style>
    </head>
    <body class="light-mode">
        <div class="container">
            <h1>Upload CSV for Visualization</h1>
            <form id="upload-form" enctype="multipart/form-data">
                <input type="file" id="csv-file" name="csv-file" accept=".csv">
                <button type="submit">Upload</button>
            </form>
            <div id="visualization"></div>
        </div>
        <div class="theme-toggle" onclick="toggleTheme()">🌙</div>
        <script>
            function toggleTheme() {
                const body = document.body;
                const toggle = document.querySelector('.theme-toggle');
                if (body.classList.contains('light-mode')) {
                    body.classList.remove('light-mode');
                    body.classList.add('dark-mode');
                    toggle.textContent = '🌞';
                } else {
                    body.classList.remove('dark-mode');
                    body.classList.add('light-mode');
                    toggle.textContent = '🌙';
                }
            }

            document.addEventListener('DOMContentLoaded', function() {
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
                        document.getElementById('visualization').innerHTML = data.html;
                    })
                    .catch(error => console.error('Error:', error));
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['csv-file']
        df = pd.read_csv(file)
        
        # Create a Pygwalker visualization
        visualization_html = pyg.walk(df).to_html()
        
        return jsonify({'html': visualization_html})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'html': '<p>Error generating visualization. Please check your CSV file.</p>'})

if __name__ == '__main__':
    app.run(debug=True)
