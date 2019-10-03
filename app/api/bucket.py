import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from app import app
import uuid
from google.cloud import storage
from app.GCP.googleStorage import GoogleStorage
import os.path

@app.route('/api/bucket', methods=['POST'])
def api_bucket_post():
    google_storage = GoogleStorage('thehut')
    # check if the post request has the file part
    try:
        if 'file' not in request.files:
            raise Exception("No file part.")
            return 'No file part', 500
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            raise Exception("No selected file.")
    except Exception as e:
        return jsonify({"message": str(e)}), 500

    extension = os.path.splitext(file.filename)[1]
    file.filename = str(uuid.uuid4()) + extension
    url = google_storage.upload_file(
        file.read(),
        file.filename,
        file.content_type
    )
    response = {"url": url}
    return jsonify(response)
