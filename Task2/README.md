# 😊 Task 2: Sentiment Analysis using Machine Learning and Deep Learning

## iNeuBytes Artificial Intelligence Internship

## 📌 Objective

The objective of this project is to develop a sentiment analysis system capable of classifying IMDb movie reviews as **Positive** or **Negative** using both **Machine Learning** and **Deep Learning** techniques. The project compares the performance of Logistic Regression, Support Vector Machine (SVM), and Long Short-Term Memory (LSTM) models using multiple evaluation metrics.

---

# 📂 Dataset

**Dataset:** IMDb Movie Reviews Dataset

- Total Reviews: **50,000**
- Positive Reviews: **25,000**
- Negative Reviews: **25,000**
- Training Split: **80%**
- Testing Split: **20%**

---

# 🔄 Data Preprocessing

The dataset was preprocessed before model training:

- Text Cleaning
- Tokenization
- TF-IDF Vectorization (Machine Learning Models)
- Padding Sequences (LSTM)
- Label Encoding
- Train-Test Split

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

```
Task_2/
│
├── Task_2_Sentiment_Analysis_using_Machine_Learning_and_Deep_Learning.ipynb
├── logistic_model.pkl
├── svm_model.pkl
├── lstm_sentiment_model.keras
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── Logistic Regression Classification Report.png
    ├── Logistic Regression Confusion Matrix.png
    ├── SVM Classification Report.png
    ├── SVM Confusion Matrix.png
    ├── LSTM Accuracy Graph.png
    ├── LSTM Loss Graph.png
    ├── LSTM Classification Report.png
    ├── LSTM Confusion Matrix.png
    ├── Custom Review Prediction.png
```

---

# 🤖 Models Implemented

## 1️⃣ Logistic Regression

- TF-IDF Vectorization
- Binary Sentiment Classification
- Fast Training and Prediction

**Accuracy:** **87.82%**

---

## 2️⃣ Support Vector Machine (SVM)

- TF-IDF Vectorization
- LinearSVC Classifier
- High-Dimensional Text Classification

**Accuracy:** **86.08%**

---

## 3️⃣ Long Short-Term Memory (LSTM)

- Embedding Layer
- LSTM Layer
- Dense Output Layer
- Binary Classification

**Accuracy:** **85.69%**

---

# 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **87.82%** |
| Support Vector Machine | **86.08%** |
| LSTM | **85.69%** |

---

# 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

---

# 📸 Results

### Figure 1: Logistic Regression Classification Report

Classification report of the Logistic Regression model showing **87.82% accuracy** with balanced Precision, Recall, and F1-Score.

---

### Figure 2: Logistic Regression Confusion Matrix

Visualization of correctly and incorrectly classified positive and negative movie reviews.

---

### Figure 3: Support Vector Machine Classification Report

Performance metrics of the SVM model including Precision, Recall, F1-Score, and Accuracy.

---

### Figure 4: Support Vector Machine Confusion Matrix

Confusion matrix showing prediction performance of the SVM classifier.

---

### Figure 5: LSTM Accuracy Graph

Training and validation accuracy curves over multiple epochs.

---

### Figure 6: LSTM Loss Graph

Training and validation loss curves demonstrating convergence of the LSTM model.

---

### Figure 7: LSTM Classification Report

Detailed classification metrics for the LSTM model.

---

### Figure 8: LSTM Confusion Matrix

Visualization of sentiment prediction results for the LSTM model.

---

### Figure 9: Custom Review Prediction

Sentiment prediction on custom movie reviews demonstrating real-world model usage.

---

# 🔍 Observations

- Logistic Regression achieved the highest accuracy (**87.82%**).
- Support Vector Machine achieved **86.08%** with competitive performance.
- LSTM achieved **85.69%** while effectively learning sequential information.
- Logistic Regression produced the fewest misclassifications.
- Machine Learning models slightly outperformed the LSTM model on the IMDb dataset.

---

# 🚀 Future Improvements

- Bidirectional LSTM
- GRU Networks
- BERT
- RoBERTa
- Hyperparameter Optimization
- Attention Mechanism
- Transfer Learning
- Real-Time Sentiment Analysis Web Application

---

# 👨‍💻 Author

**Sanket Kolhe**

B.Tech Computer Engineering

MIT Academy of Engineering, Pune

GitHub: https://github.com/SanketKolhe2005

LinkedIn: https://www.linkedin.com/in/sanket-kolhe-b2683525b

---

# 📄 License

This project was developed as part of the **iNeuBytes Artificial Intelligence Internship** for educational purposes.

---

⭐ If you found this project helpful, don't forget to **Star ⭐ the repository**.
