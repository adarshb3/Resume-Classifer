import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
model = load_model('resume_classifier_model.h5')

# Preprocessing function
def preprocess_image(image):
    image = np.array(image)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit app
st.title('Resume Classifier')

st.write('Upload an image to classify whether it is a resume or not.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    
    # Make prediction
    prediction = model.predict(preprocessed_image)
    prediction_label = "Not a Resume" if prediction[0] > 0.5 else "Resume"
    
    st.write(f"Prediction: {prediction_label}")
