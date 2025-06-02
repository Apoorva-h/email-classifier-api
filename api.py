from fastapi import FastAPI
from pydantic import BaseModel
from masking import mask_pii
from classification import predict_category

app = FastAPI()

class EmailInput(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify_email(request: EmailInput):
    original_text = request.input_email_body
    masked_text, entities = mask_pii(original_text)
    category = predict_category(masked_text)
    return {
        "input_email_body": original_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }