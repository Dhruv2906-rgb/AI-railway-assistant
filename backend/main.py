from fastapi import FastAPI, HTTPException

from backend.models import TravelRequest
from backend.llm_service import generate_route_advice

app = FastAPI(
    title="AI Railway Assistant"
)


@app.get("/")
def home():
    return {
        "message": "AI Railway Assistant Running"
    }


@app.post("/plan")
def plan_trip(data: TravelRequest):
    try:
        result = generate_route_advice(
            source=data.source,
            destination=data.destination,
            budget=data.budget,
            date=data.date
        )

        return {"response": result}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )