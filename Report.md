# 📧 Email Classification API with PII Masking

**Name:** APOORVA K R  
**Project:** Email Classifier API  
**Platform:** Hugging Face Spaces + GitHub

---

## 1. Introduction

This project aims to automate the classification of support emails into predefined categories such as Incident, Request, or Inquiry. It also ensures the masking of Personally Identifiable Information (PII) to protect user privacy.

---

## 2. Problem Statement

Customer support systems often receive large volumes of emails that must be categorized before being processed. However, these emails often contain sensitive personal information. The challenge is to both classify the emails accurately and ensure that PII like names, emails, phone numbers, etc., are masked before any machine learning processing.

---

## 3. PII Masking

PII masking is performed using a combination of regular expressions (for email, phone number, DOB, Aadhar, etc.) and named entity recognition (NER) using spaCy for identifying full names. Each identified entity is replaced with a placeholder (e.g., [email], [full_name]).

---

## 4. Email Classification

The email classification is handled using a TF-IDF vectorizer and a Logistic Regression model. The model is trained on masked email bodies and predicts a category for the email.

---

## 5. API Design and Deployment

The backend API is built using FastAPI. It is deployed as a Docker container on Hugging Face Spaces. The API accepts POST requests at the `/classify` endpoint and returns masked email, extracted PII, and predicted category.

---

## 6. Testing and Results

The API was tested using Swagger UI and Python requests. It returns correct classification and masks entities properly.

**Example input:**
```
Hi, I am Apoorva Gowda. My email is apoorva@example.com. I need help logging in.
```

**Example output:**
```
Masked email: Hi, I am [full_name]. My email is [email]. I need help logging in.
Category: Incident
```

---

## 7. Technologies Used

- Python  
- spaCy  
- Scikit-learn  
- FastAPI  
- Docker  
- Hugging Face Spaces

---

## 8. Conclusion

This project successfully implements a complete pipeline for PII masking and email classification, exposed as a REST API. The deployment on Hugging Face makes the service accessible publicly without needing separate hosting.

---

## 9. Useful Links

- 🔗 GitHub Repository: [https://github.com/ApoorvaGowda/email-classifier-api](https://github.com/ApoorvaGowda/email-classifier-api)  
- 🔗 Hugging Face API: [https://apoorvagowda-email-classifier-appu.hf.space/classify](https://apoorvagowda-email-classifier-appu.hf.space/classify)  
- 🔗 Swagger Docs: [https://apoorvagowda-email-classifier-appu.hf.space/docs](https://apoorvagowda-email-classifier-appu.hf.space/docs)

---

## ✅ Assignment Compliance

- ✔️ PII masking implemented using regex + spaCy  
- ✔️ Classification using TF-IDF + Logistic Regression  
- ✔️ POST `/classify` endpoint working and deployed  
- ✔️ Deployed on Hugging Face with FastAPI  
- ✔️ Input/output JSON format documented  
- ✔️ Markdown and DOCX reports prepared for GitHub
