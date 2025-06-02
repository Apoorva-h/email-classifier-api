# Email Classifier API

This project performs automatic PII masking and email classification using a trained machine learning model. It is deployed using FastAPI and Docker on Hugging Face Spaces.

---

## 📌 Features

- ✅ Detects and masks PII (like full names, emails, phone numbers, dates of birth, Aadhar, card numbers, etc.)
- ✅ Classifies emails into categories (e.g., Incident, Service Request, Inquiry)
- ✅ Exposes a REST API with `/classify` POST endpoint
- ✅ Deployed on Hugging Face Spaces using Docker

---

## 🚀 Live API

**POST Endpoint:**  
[`/classify`](https://apoorvagowda-email-classifier-appu.hf.space/classify)

---

## 📥 Example Input

```json
{
  "input_email_body": "Hi, I am Apoorva Gowda. My email is apoorva@gmail.com. I need help logging in."
}

📤 Example Output
'''json
{
  "masked_email": "Hi, I am [full_name]. My email is [email]. I need help logging in.",
  "category_of_the_email": "Incident",
  "list_of_masked_entities": [
    {
      "position": [9, 22],
      "classification": "full_name",
      "entity": "Apoorva Gowda"
    },
    {
      "position": [36, 55],
      "classification": "email",
      "entity": "apoorva@gmail.com"
    }
  ]
}


📁 Project Structure
File	Description
app.py	Launches FastAPI app
api.py	API endpoint logic (/classify)
masking.py	Contains logic to detect and mask PII
classification.py	Loads ML model and predicts category
classifier.joblib	Trained classifier model
vectorizer.joblib	Trained TF-IDF vectorizer
requirements.txt	Python dependencies
Dockerfile	Used by Hugging Face to deploy with Docker

⚙️ Local Setup (Optional)
If you want to run it locally:

bash
Copy
Edit
pip install -r requirements.txt
uvicorn app:app --reload
