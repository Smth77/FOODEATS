from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Food Recommendation API")

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load sample data
with open("data/sample_foods.json") as f:
    FOODS = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Food Recommendation API"}

@app.get("/foods")
def get_foods():
    """Return all food items"""
    return FOODS

@app.get("/foods/{food_id}")
def get_food(food_id: int):
    """Return specific food item"""
    for food in FOODS:
        if food["id"] == food_id:
            return food
    return {"error": "Food not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
