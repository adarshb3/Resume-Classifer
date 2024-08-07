# Resume Classifier

## Overview
This project develops a resume classifier using Python and computer vision techniques. The classifier accurately distinguishes whether a given image is a resume or not without utilizing OCR or any textual features.

## Objective
- Classify images as resumes or non-resumes using only visual characteristics.
- Avoid using OCR or any textual features in the classification process.

## Dataset Collection
The dataset was created by gathering a diverse set of images:
- **Resumes**: Collected from Microsoft's free resume templates.
- **Non-Resumes**: Composed of random contracts, brochures, flyers, and invoice images.

The dataset ensures a wide range of visual characteristics to enhance model robustness.

## Data Augmentation and Preprocessing
To enhance the model's robustness, various data augmentation techniques were applied:
- **Rotation**: Rotating images randomly.
- **Width and Height Shifts**: Randomly shifting images along both axes.
- **Shear**: Applying shear transformations.
- **Zoom**: Randomly zooming in and out of images.
- **Horizontal Flip**: Randomly flipping images horizontally.

Images were preprocessed by resizing them to 224x224 pixels and normalizing pixel values to the range [0, 1].

## Model Selection
The VGG16 architecture from the Keras library was chosen for its suitability in image classification tasks. The pre-trained VGG16 model was fine-tuned for the specific task of resume classification.

## Model Training
The dataset was split into training and validation sets (80% training, 20% validation). The model was trained using the augmented data, and hyperparameters were optimized to enhance performance.

## Testing and Evaluation
The model was evaluated on the validation set, achieving high accuracy and other relevant metrics. The following evaluation metrics were used:
- **Accuracy**: 96%
- **Precision**: 97%
- **Recall**: 94%
- **F1-Score**: 95%

### Confusion Matrix
The confusion matrix visually represents the model's performance, highlighting true positives, false positives, true negatives, and false negatives.

![Confusion Matrix](https://github.com/adarshb3/Resume-Classifer/blob/main/images/output.png)

## Approach
1. **Data Collection**:
   - Resumes were sourced from Microsoft's free templates.
   - Non-resumes included contracts, brochures, flyers, and invoices.

2. **Data Augmentation and Preprocessing**:
   - Applied augmentation techniques to enhance model robustness.
   - Preprocessed images by resizing and normalizing.

3. **Model Selection**:
   - Chose the VGG16 architecture and fine-tuned it for resume classification.

4. **Model Training**:
   - Split the dataset and trained the model using augmented data.
   - Experimented with hyperparameters for optimization.

5. **Evaluation**:
   - Evaluated the model using accuracy, precision, recall, and F1-score.
   - Generated a confusion matrix for performance visualization.

## Results
The model demonstrated high accuracy and robustness in distinguishing resumes from non-resumes. Below are the detailed evaluation metrics:

- **Accuracy**: 96%
- **Precision**: 97%
- **Recall**: 94%
- **F1-Score**: 95%

The confusion matrix provides a clear visualization of the model's performance, showcasing the balance between true positives, false positives, true negatives, and false negatives.

## App Interface
The Streamlit app provides an intuitive interface for users to upload images and receive classification results. The app ensures ease of use and provides immediate feedback on the uploaded images.

![App Interface](https://github.com/adarshb3/Resume-Classifer/blob/main/images/Capture1.JPG)

## Code Repository
The code is organized following best practices, ensuring readability and maintainability. Jupyter notebooks are provided for detailed explanations and visualizations of the approach and results.
