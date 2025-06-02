# 📧 Email Classification API with PII Masking

This project implements a backend-only API that classifies support emails into predefined categories — while masking all Personally Identifiable Information (PII) before classification.

It is designed for use by customer support systems to improve ticket triaging while ensuring user data privacy.

---

## 🚀 Deployed API

**POST Endpoint:**  
👉 [`/classify`](https://apoorvagowda-email-classifier-appu.hf.space/classify)

**Interactive API Docs (Swagger):**  
👉 [`/docs`](https://apoorvagowda-email-classifier-appu.hf.space/docs#/default/classify_email_classify_post)

**GET Endpoint (browser-friendly):**  
👉 [`/`](https://apoorvagowda-email-classifier-appu.hf.space) — returns a welcome message

> Deployed on [Hugging Face Spaces](https://huggingface.co/spaces/apoorvagowda/email-classifier-appu)

---

## 📥 Input Format

Send a **POST request** to `/classify` with this JSON body:

```json
{
  "input_email_body": "Hi, my name is Apoorva Gowda. My email is apoorva@example.com and my Aadhar is 1234 5678 9012."
}
```

---

## 📤 Output Format

You’ll receive a JSON response with:

```json
{
  "input_email_body": "Hi, my name is Apoorva Gowda. My email is apoorva@example.com and my Aadhar is 1234 5678 9012.",
  "list_of_masked_entities": [
    {
      "position": [26, 48],
      "classification": "email",
      "entity": "apoorva@example.com"
    },
    {
      "position": [66, 81],
      "classification": "aadhar_num",
      "entity": "1234 5678 9012"
    }
  ],
  "masked_email": "Hi, my name is [full_name]. My email is [email] and my Aadhar is [aadhar_num].",
  "category_of_the_email": "Incident"
}
```

---

## 🧠 Model Pipeline

### 🔐 PII Masking:
- **Regex patterns** for: `email`, `phone_number`, `dob`, `aadhar_num`, `cvv_no`, `credit_debit_no`, `expiry_no`
- **spaCy NER (`en_core_web_sm`)** for identifying `full_name`

### 🧠 Classification:
- `TfidfVectorizer` to extract text features from the masked email
- `LogisticRegression` to predict the category

### 📦 Framework:
- FastAPI (for serving)
- Deployed on Hugging Face Spaces (no frontend, backend-only API)

---

## 📦 Requirements

Install required libraries using:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🧪 How to Test the API

### Using Python:

```python
import requests

url = "https://apoorvagowda-email-classifier-appu.hf.space/classify"
data = {
    "input_email_body": "Hi, I am Apoorva Gowda. My email is apoorva@example.com. I need help with login."
}
res = requests.post(url, json=data)
print(res.status_code)
print(res.json())
```

### Using Postman:
- Method: `POST`
- URL: `https://apoorvagowda-email-classifier-appu.hf.space/classify`
- Body: raw JSON as shown above
- Headers: `Content-Type: application/json`

---

## 🗂 File Structure

```plaintext
.
├── app.py                # FastAPI app starter
├── api.py                # API route logic
├── masking.py            # PII masking logic
├── classification.py     # Model prediction logic
├── classifier.joblib     # Trained model
├── vectorizer.joblib     # TF-IDF vectorizer
├── requirements.txt      # Dependencies
└── README.md             # This file
```

---

## 👩‍💻 Author

- GitHub: [@ApoorvaGowda](https://github.com/Apoorva-h)
- Hugging Face Space: [email-classifier-appu](https://huggingface.co/spaces/apoorvagowda/email-classifier-appu)

---

## ✅ Assignment Compliance

✔️ PII masking without LLMs  
✔️ Classification into required labels  
✔️ `/classify` endpoint deployed on Hugging Face  
✔️ `/` GET endpoint added for browser users  
✔️ Input/output format as per spec  
✔️ No frontend (backend-only FastAPI)
