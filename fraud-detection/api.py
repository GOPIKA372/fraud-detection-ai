from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- REQUEST FORMAT ----------------
class Transaction(BaseModel):
    data: list


# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}


# ---------------- PREDICT ----------------
@app.post("/predict")
def predict(transaction: Transaction):

    try:
        data = transaction.data

        # safety check
        if not data:
            return {
                "result": "Invalid Input",
                "confidence": 0
            }

        amount = float(data[-1])

        print("Received Amount:", amount)

        # ---------------- RULE-BASED LOGIC ----------------

        if amount > 200000:
            return {
                "result": "Fraud Transaction (High Amount Alert)",
                "confidence": 95
            }

        elif amount > 50000:
            return {
                "result": "Suspicious Transaction",
                "confidence": 75
            }

        elif amount > 1000:
            return {
                "result": "Medium Risk Transaction",
                "confidence": 60
            }

        else:
            return {
                "result": "Normal Transaction",
                "confidence": 90
            }

    except Exception as e:
        print("ERROR:", e)
        return {
            "result": "Backend Error",
            "confidence": 0
        }