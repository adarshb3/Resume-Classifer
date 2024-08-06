# Resume Classifier

## Overview
This project aims to develop a resume classifier using Python and computer vision techniques. The goal is to accurately classify whether a given image is a resume or not without utilizing OCR or any textual features.

## Objective
- Classify images as resumes or non-resumes using only visual characteristics.
- Avoid using OCR or any textual features in the classification process.

## Tasks
1. **Dataset Collection:**
   - Gather a diverse dataset of resume and non-resume images.
   - Ensure the dataset covers a wide range of visual characteristics.

2. **Data Augmentation and Preprocessing:**
   - Apply data augmentation techniques such as rotation, width and height shifts, shear, zoom, and horizontal flips to enhance model robustness.
   - Preprocess images by resizing them to 224x224 pixels and normalizing pixel values.

3. **Model Selection:**
   - Chose the VGG16 architecture from the Keras library for its suitability in image classification tasks.
   - Fine-tuned the pre-trained model for the specific task of resume classification.

4. **Model Training:**
   - Split the dataset into training and validation sets (80% training, 20% validation).
   - Train the model using the augmented data.
   - Experiment with hyperparameters to optimize the model's performance.

5. **Testing and Evaluation:**
   - Evaluate the model on the validation set.
   - Achieve high accuracy and other relevant metrics.
   - Generate a confusion matrix to visually represent the model's performance.

6. **Confusion Matrix:**
   - Discuss the significance of true positives, false positives, and false negatives in the context of the classifier's performance.

7. **Documentation:**
   - Summarize the approach, including dataset details, model architecture, training strategy, and evaluation metrics.
   - Create a one-pager document highlighting key aspects of the work.

8. **Code Repository:**
   - Organize the code following best practices.
   - Ensure the code is well-structured, readable, and includes necessary comments.
   - Provide Jupyter notebooks for detailed explanations and visualizations.

![App Interface](https://github.com/adarshb3/Resume-Classifer/blob/main/images/Capture1.JPG)
![](https://github.com/adarshb3/Resume-Classifer/blob/main/images/Capture2.JPG)
