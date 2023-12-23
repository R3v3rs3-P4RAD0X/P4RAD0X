from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

import subprocess as sp
import json

@app.route('/')
def index():
    res = sp.call('python tracker/tracker.py -a', shell=True, stdout=sp.PIPE, stderr=sp.DEVNULL)

    # Check if the command was successful
    if res != 0:
        return render_template('index.html', **{
            'title': 'Error',
            'description': 'There was an error fetching the projects.',
            'content': 'Please try again later.'
        })
    
    # Get the output of the command
    output = sp.check_output('python tracker/tracker.py -a', shell=True).decode('utf-8')

    # Convert the output to a JSON object
    result = json.loads(output)

    # Create a data list
    data = []

    # Convert result to a list of dictionaries
    for key in result:
        name = result[key]['name']
        lang = result[key]['language']

        data.append({
            'name': name,
            'language': lang,
            'key': key
        })
    
    print(data)

    return render_template('index.html', **{
        'title': 'Hello, World!',
        'description': 'This is a description.',
        'content': 'This is the content.',
        'projects': data
    })

# Create a route for static files
@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
