# Iris-Flower-Species-Prediction
A Flask-based web application to predict the species of Iris flowers using a machine learning model.
This project provides a simple web interface where users can input flower measurements, and the app returns a prediction of the flower species based on the trained machine learning model.

## Files in This Project
+ **app.py** - The main Flask application script
+ **iris.csv** - The dataset used to train the model.
+ **iris_class.ipynb** - The jupyter notebook file used to train and load the model.
+ **model.pkl** - The pre-trained model file used for predictions.
+ **model.py** - A python file also used to train the model (same as jupyter notebook file).

  ## Technologies used
  + **Flask** - Web framework to handle  HTTP requests.
  + **Pandas** - For data manipulation and preprocessing.
  + **Pickle** - To load the model
  + **Sklearn** - To train,test, preprocess , and Classify the model metrics

    ## Installation
    1. **Clone the repository**
Download or clone this project to your local machine.
2. Navigate into the project directory
3. Create and activate a virtual environment
4. Install the required dependencies 
5. Run the Flask application
   Execute the following command to start the Flask application:
   _python app.py_

   ## Usage
   1. Open your web browser and go to http://127.0.0.1:5000.
2. Enter the measurements for the Iris flower in the provided input fields.
3. Click "Predict" to see the model’s prediction of the flower species.

   ## Model training
   The model was trained on the popular Iris dataset, saved as model.pkl. You can retrain the model if needed using the iris.csv dataset.
