from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="PocketSmart AI: Your Smart Budget & Recommendation Assistant"
)


# ---------------------------------------------------------
# Templates
# ---------------------------------------------------------

templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------
# Data models
# ---------------------------------------------------------

class HomePlanner(BaseModel):
    budget: float
    furniture: str
    lighting: str
    decoration: str


class PartyPlanner(BaseModel):
    budget: float
    guests: int
    event_type: str
    decoration: str


class JewelryPlanner(BaseModel):
    budget: float
    jewelry_type: str
    material: str


# ---------------------------------------------------------
# Home page
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


# ---------------------------------------------------------
# Home planner POST route
# ---------------------------------------------------------

@app.post("/home-planner")
async def home_planner(data: HomePlanner):

    recommendations = [
        {
            "name": data.furniture,
            "details": "Furniture recommendation based on your budget",
            "price": min(25000, data.budget)
        },
        {
            "name": data.lighting,
            "details": "Suitable lighting option for your home",
            "price": min(5000, data.budget)
        },
        {
            "name": data.decoration,
            "details": "Decoration option suitable for your requirements",
            "price": min(3000, data.budget)
        }
    ]

    return {
        "planner": "Home",
        "message": "Home planner submitted successfully",
        "budget": data.budget,
        "furniture": data.furniture,
        "lighting": data.lighting,
        "decoration": data.decoration,
        "recommendations": recommendations
    }


# ---------------------------------------------------------
# Party planner POST route
# ---------------------------------------------------------

@app.post("/party-planner")
async def party_planner(data: PartyPlanner):

    recommendations = [
        {
            "name": data.event_type,
            "details": f"Party planning for {data.guests} guests",
            "price": min(15000, data.budget)
        },
        {
            "name": data.decoration,
            "details": "Decoration recommendation for your event",
            "price": min(7000, data.budget)
        },
        {
            "name": "Food & Refreshments",
            "details": f"Estimated arrangement for {data.guests} guests",
            "price": min(8000, data.budget)
        }
    ]

    return {
        "planner": "Party",
        "message": "Party planner submitted successfully",
        "budget": data.budget,
        "guests": data.guests,
        "event_type": data.event_type,
        "decoration": data.decoration,
        "recommendations": recommendations
    }


# ---------------------------------------------------------
# Jewelry planner POST route
# ---------------------------------------------------------

@app.post("/jewelry-planner")
async def jewelry_planner(data: JewelryPlanner):

    recommendations = [
        {
            "name": data.jewelry_type,
            "details": f"{data.material} jewelry within your selected budget",
            "price": min(50000, data.budget)
        },
        {
            "name": f"{data.material} Collection",
            "details": "Recommended material option for your jewelry",
            "price": min(15000, data.budget)
        },
        {
            "name": "Jewelry Accessories",
            "details": "Matching accessories for your selected jewelry",
            "price": min(5000, data.budget)
        }
    ]

    return {
        "planner": "Jewelry",
        "message": "Jewelry planner submitted successfully",
        "budget": data.budget,
        "jewelry_type": data.jewelry_type,
        "material": data.material,
        "recommendations": recommendations
    }


# ---------------------------------------------------------
# Main entry point
# ---------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000
    )