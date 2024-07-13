from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
IMAGE_DIR = '/home/joseph/Pictures'

@app.route('/')
def index():
    try:
        # Get the latest image file
        latest_image = max([f for f in os.listdir(IMAGE_DIR) if f.endswith('.png')], key=lambda x: os.path.getctime(os.path.join(IMAGE_DIR, x)))
        image_path = os.path.join(IMAGE_DIR, latest_image)
        download_time = os.path.getctime(image_path)
        return render_template_string('''
            <h1>Latest Image</h1>
            <p>Downloaded at: {{ download_time }}</p>
            <img src="/images/{{ latest_image }}" alt="Latest Image">
        ''', latest_image=latest_image, download_time=download_time)
    except ValueError:
        return '<h1>No images found in the directory.</h1>'

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(IMAGE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
