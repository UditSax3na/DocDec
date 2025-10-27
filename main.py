# python anywhere

import traceback
import datetime
from config.path import *

# import joblib
import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from core.DocDec import DocDec

class SymptomInput(BaseModel):
    text: str|list
    multiple: bool
    
dirCheck()

try:
    # api routes
    Router = APIRouter()

    @Router.post("/status")
    def TestingStatus():
        return {"Message": "API IS LIVE!"}
    
    @Router.post("/predict")
    def PredictResult(Data: SymptomInput):
        """
            "Payment receipt for transaction ID 5008.",
            "Employee leave request form.",
            "Monthly sales report for department A.",
            "Invoice for supplier XYZ.",
            "Meeting minutes of HR department.",
            "Purchase order for office supplies.",
            "Customer complaint about product quality.",
            "IT system maintenance r`eport.",
            "Budget proposal for marketing campaign.",
            "Training schedule for new employees."]
        """
        DocDecM = DocDec()
        if Data.multiple:
            datalst = []
            for i in Data.text:
                result = DocDecM.Predict(i)
                datalst.append(result)
            return {'data': datalst, 'multiple':Data.multiple}

        else:
            result = DocDecM.Predict(Data.text)
            return {'data': result,'multiple':Data.multiple}
        
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # or ["http://localhost:3000"]
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(Router)

except Exception as e:
    with open(LOG_FILE, 'a') as myfile:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_trace = traceback.format_exc()
        myfile.write(f"[{timestamp}] Error: {str(e)}\n")
        myfile.write(f"[{timestamp}] Traceback:\n{error_trace}\n")
        myfile.write(f"[{timestamp}] File Location: {__file__}\n")
        myfile.write("-" * 60 + "\n")

# made by Udit Saxena(www.github.com/UditSax3na)