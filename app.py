from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def upload_form():
    """Render the upload form"""
    return render_template('upload_form.html')


@app.route('/', methods=['POST'])
def upload_image():
    """
    Upload an image

    :return: The result of the upload as a string
    """
    image = request.files.get('image')
    if image and image.filename:
        filename = image.filename
        image.save('static/' + filename)
        return 'Image %s uploaded successfully' % filename
    else:
        return 'Upload failed'



if __name__ == '__main__':
    app.run()
