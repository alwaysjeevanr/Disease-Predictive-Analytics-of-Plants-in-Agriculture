import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
from skimage import io
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('model.h5', compile=False)


def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


# Define the prediction route
@app.route('/analyze', methods=['GET','POST'])
def analyze():
    print("Analyze route hit")  # Debug print
    if request.method == 'POST':
        # Debugging: Ensure the file part is received
        if 'file' not in request.files:
            print("No file part")
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            print("No selected file")
            return redirect(request.url)
        if f:
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            preds = model_predict(file_path, model)
            print(preds[0])  # Debug print
            disease_class = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight', 
                        'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 
                        'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 
                        'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 
                        'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
            res = disease_class[np.argmax(preds)]
            print("Disease Name : " + res)  # Debug print
            return render_template('index.html', prediction_text=f'Disease Name: {res}')
    return None


if __name__ == '__main__':
    app.run(debug=True)