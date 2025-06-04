# Plant-Disease-Detection-By-Deeplearning

This project detects plant diseases using deep learning. It includes model training, saving the model as `model.h5`, and deploying a web app with Flask. The dataset is from Kaggle (see below).

## ⚠️ Important: TensorFlow & Python Version Compatibility

TensorFlow does **not** support Python 3.13 as of June 2025. Use **Python 3.10** for this project. If you see errors about TensorFlow or Keras not installing or loading, downgrade your Python version.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alwaysjeevanr/Disease-Predictive-Analytics-of-Plants-in-Agriculture.git
   ```

2. **Download the dataset:**

   - Kaggle: https://www.kaggle.com/datasets/neeleshj/plant-village/
   - Place the extracted dataset in the `PlantVillage` folder (already present in this repo).

3. **Set up your Python environment:**

   - Use Python 3.10 (not 3.13).
   - Create and activate a virtual environment:
     ```bash
     # For Windows (example with Python 3.10)
     py -3.10 -m venv venv
     venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

4. **Train the model (optional):**

   - Edit paths and run `train.ipynb` in Jupyter Notebook.
   - The notebook will generate `model.h5` (already included).
   - Ensure the `uploads` directory exists for file uploads.

5. **Run the Flask application:**

   ```bash
   flask run
   ```

   - The app will be available at [http://localhost:5000](http://localhost:5000)

6. **Usage:**

   - Open the web app in your browser.
   - Upload a plant leaf image to get a disease prediction.

7. **Contributing:**
   - Fork the repository on GitHub.
   - Create a new branch for your changes.
   - Make your changes and commit them.
   - Open a pull request.

## Troubleshooting

- **TensorFlow/Keras model loading error about `/` in layer names:**

  - Newer Keras/TensorFlow versions do **not** allow `/` in layer names.
  - If you see an error like `Argument name must be a string and cannot contain character '/'`, retrain or re-save your model with valid layer names (use `_` instead of `/`).
  - Example: `Conv2D(..., name='conv1_conv')`

- **TensorFlow not installing or import errors:**
  - Make sure you are using Python 3.10, .
  - Check your `requirements.txt` for compatible versions.

## Credits

Project by Jeevan R.  
Dataset: [Kaggle PlantVillage](https://www.kaggle.com/datasets/neeleshj/plant-village/)
