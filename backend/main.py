from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from pydantic import BaseModel
from database import Database

app = FastAPI(title="Property Search API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
db = Database()

# Pydantic models
class Property(BaseModel):
    id: int
    title: str
    city: str
    property_type: str
    price: int
    bedrooms: int
    bathrooms: int
    area: int
    address: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    amenities: List[str] = []

class City(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Property Search API", "version": "1.0.0"}

@app.get("/api/properties", response_model=List[Property])
def get_properties(
    city: Optional[str] = Query(None, description="Filter by city (Pune or Hyderabad)"),
    property_type: Optional[str] = Query(None, description="Filter by property type (rent or buy)"),
    min_budget: Optional[int] = Query(None, description="Minimum budget"),
    max_budget: Optional[int] = Query(None, description="Maximum budget")
):
    """
    Get all properties with optional filters
    """
    try:
        properties = db.get_properties(
            city=city,
            property_type=property_type,
            min_budget=min_budget,
            max_budget=max_budget
        )
        return properties
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/properties/{property_id}", response_model=Property)
def get_property(property_id: int):
    """
    Get a single property by ID
    """
    property_data = db.get_property_by_id(property_id)
    if not property_data:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_data

@app.get("/api/cities", response_model=List[City])
def get_cities():
    """
    Get list of available cities
    """
    return [
        {"name": "Pune"},
        {"name": "Hyderabad"}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
