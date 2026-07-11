# 😊 Task 2: Sentiment Analysis using Machine Learning and Deep Learning

## iNeuBytes Artificial Intelligence Internship

### 📌 Objective

The objective of this project is to perform sentiment analysis on the IMDb Movie Reviews dataset using both Machine Learning and Deep Learning models. The performance of Logistic Regression, Support Vector Machine (SVM), and Long Short-Term Memory (LSTM) models is compared using classification metrics and confusion matrices.

---

# 📂 Dataset

**Dataset:** IMDb Movie Reviews Dataset

- Total Reviews: **50,000**
- Positive Reviews: **25,000**
- Negative Reviews: **25,000**
- Training Split: **80%**
- Testing Split: **20%**

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Google Colab

---

# 📁 Project Structure

```text
Task_2/
│
├── Task2_Sentiment_Analysis.ipynb
├── logistic_model.pkl
├── svm_model.pkl
├── lstm_sentiment_model.keras
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── model_comparison.png
    ├── logistic_confusion_matrix.png
    ├── svm_confusion_matrix.png
    └── lstm_confusion_matrix.png
```

---

# 🧪 Models Implemented

## 1️⃣ Logistic Regression

- TF-IDF Vectorization
- Baseline Machine Learning Model
- Fast Training and Prediction

---

## 2️⃣ Support Vector Machine (SVM)

- TF-IDF Vectorization
- Linear Kernel
- High-dimensional Text Classification

---

## 3️⃣ Long Short-Term Memory (LSTM)

- Tokenizer
- Embedding Layer
- LSTM Layer
- Dense Output Layer
- Binary Classification

---

# 📊 Model Performance

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | **87.82%** |
| Support Vector Machine | **86.08%** |
| LSTM | **85.69%** |

---

# 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 📸 Results

## Model Comparison

![Model Comparison](screenshots/model_comparison.png)

---

## Logistic Regression Confusion Matrix

![Logistic Regression](screenshots/confusion_matrix_Logistic.png)

---

## Support Vector Machine Confusion Matrix

![SVM](screenshots/confusion_matrix_SVM.png)

---

## LSTM Confusion Matrix

![LSTM](screenshots/lstm_confusion_matrix.png)

---

# 🔍 Observations

- Logistic Regression achieved the **highest accuracy (87.82%)** among all models.
- Support Vector Machine achieved **86.08%** accuracy with competitive performance.
- LSTM achieved **85.69%** accuracy and effectively captured sequential text patterns.
- Classical Machine Learning models (Logistic Regression and SVM) performed slightly better than the LSTM model on this dataset while requiring less training time.
- Logistic Regression proved to be the most efficient model for IMDb sentiment classification in this project.

---

# 🚀 Future Improvements

- Bidirectional LSTM
- GRU Networks
- BERT Transformer
- RoBERTa
- Hyperparameter Optimization
- Attention Mechanism
- Transfer Learning
- Larger NLP Datasets

---

# 👨‍💻 Author

**Sanket Kolhe**

B.Tech Computer Engineering  
MIT Academy of Engineering, Pune

---

# 📄 License

This project was developed as part of the **iNeuBytes Artificial Intelligence Internship** for educational purposes.
