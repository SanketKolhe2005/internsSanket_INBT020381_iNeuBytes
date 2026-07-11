# Task 1: Computer Vision using CNN Models

## Internship
**iNeuBytes Artificial Intelligence Internship**

## Objective
The objective of this project is to implement a Convolutional Neural Network (CNN) for image classification using the CIFAR-10 dataset and perform controlled experiments to improve the model's performance.

---

## Dataset

- Dataset: CIFAR-10
- Total Images: 60,000
- Training Images: 50,000
- Testing Images: 10,000
- Number of Classes: 10

Classes:
- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

---

## Project Structure

```
Task1_CNN/
│
├── Task1_CNN.ipynb
├── Final_CNN_Model.h5
├── Final_CNN_Results.csv
├── README.md
└── Report.pdf
```

---

## Experiments Performed

### Baseline CNN

- Two Convolution Layers
- MaxPooling
- Dense Layer

Accuracy:
**69.99%**

---

### Experiment 1

Added Dropout Layer

Accuracy:
**70.12%**

---

### Experiment 2

Added Batch Normalization

Accuracy:
**65.40%**

---

### Final CNN

Combined the best-performing techniques and evaluated the final model.

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Results

| Model | Accuracy |
|--------|----------|
| Baseline CNN | 69.99% |
| Dropout CNN | 70.12% |
| BatchNorm CNN | 65.40% |
| Final CNN | XX.XX% |

---

## Future Improvements

- Data Augmentation
- Transfer Learning
- ResNet50
- EfficientNet
- Hyperparameter Tuning

---

## Author

Sanket Kolhe

MIT Academy of Engineering

2026
