from flask import Flask, request, jsonify, send_file, redirect
import os
import uuid

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 128 * 1024 * 1024 * 1024 # 128 GB

# A route for static files, e.g. CSS, JS, images
@app.route("/static/<path:path>")
def static_files(path):
    # This function will return the static file to the user
    # It will use the send_file function to return the file
    # The send_file function will take the path to the file as an argument
    # The path to the file will be the static folder and the path
    return send_file(os.path.join("static", path))

# A route for static api
@app.route("/api/static/<path:path>")
def api_static_files(path):
    # This function will return the static file to the user
    # It will use the send_file function to return the file
    # The send_file function will take the path to the file as an argument
    # The path to the file will be the static folder and the path
    return send_file(os.path.join("static", path))

# Create a route for the home page
@app.route("/")
def home():
    # Load the html file in the html folder
    return open("html/index.html").read()

# Create a route to handle the files page
@app.route("/files")
def files():
    return open("html/files.html").read().replace("{{files}}", handle_files())

# Create a route to handle the upload page
@app.route("/upload")
def upload():
    return open("html/upload.html").read()

# Create API routes
@app.route("/api/upload", methods=["POST"])
def api_upload():
    if request.method == "POST":
        if request.files:
            file = request.files["file"]
            file.save(os.path.join("uploads", file.filename))

            # Use the response.html file to display the result
            return redirect(f"/response?response=<p>File {file.filename} uploaded successfully.</p>")
    # If the request is not POST, return a 405 error
    return jsonify({"error": "Method not allowed"}), 405

# API route for deleting a file
@app.route("/api/delete/<path:path>")
def api_delete(path):
    # Check if the file exists
    if os.path.exists(os.path.join("uploads", path)):
        # Delete the file
        os.remove(os.path.join("uploads", path))

        # Redirect to response
        return redirect(f"/response?response=File {path} deleted successfully")

    # If the file does not exist, return an error
    return jsonify({"error": "File not found"}), 404

# API route for downloading a file
@app.route("/api/download/<path:path>")
def api_download(path):
    # Check if the file exists
    if os.path.exists(os.path.join("uploads", path)):
        # Return the file to the user
        return send_file(os.path.join("uploads", path))
    # If the file does not exist, return an error
    return jsonify({"error": "File not found"}), 404


def handle_files():
    # Returns all the files in the uploads folder
    # As a html list

    # Get all the files in the uploads folder
    files = os.listdir("uploads")

    # Create a variable to store the html
    entries = []

    # Loop through all the files
    for file in files:
        # Create a div for the file
        div = "<div class='file'>"
        div += f"<p>{file}</p>"
        div += f"<a class='download' href='/api/download/{file}'>Download</a>"
        div += f"<a class='delete' href='/api/delete/{file}'>Delete</a>"
        div += "</div>"

        li = f"<li>{div}</li>"
        entries.append(li)

    # Join the list with a new line
    return "\n".join(entries)

# Create a route for response
@app.route("/response")
def response():
    # Get the query string
    query = request.args.get("response")

    # Check if the query string is empty
    if not query:
        # If the query string is empty, return an error
        return jsonify({"error": "No response given"}), 400

    # Load the html file in the html folder
    return open("html/response.html").read().replace("{{response}}", query)


if __name__ == "__main__":
    app.run(debug=True)
