# Property Search Website

A modern property search website for finding rental and sale properties in Pune and Hyderabad.

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS + Shadcn/UI
- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **Icons**: Lucide React

## Features

- Search properties by city (Pune/Hyderabad)
- Filter by property type (Rent/Buy)
- Budget range filtering (min/max)
- Clean, Airbnb-style design
- 20 mock properties (10 per city)

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Seed the database with mock properties:
```bash
python seed_data.py
```

4. Start the FastAPI server:
```bash
python -m uvicorn main:app --reload
```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

## Usage

1. Make sure both backend and frontend servers are running
2. Open your browser to `http://localhost:5173`
3. Use the search bar to filter properties by:
   - City (Pune or Hyderabad)
   - Property Type (Rent or Buy)
   - Budget Range (Min/Max)
4. Click "Search" to apply filters or "Reset" to clear them

## API Endpoints

- `GET /api/properties` - Get all properties with optional filters
  - Query params: `city`, `property_type`, `min_budget`, `max_budget`
- `GET /api/properties/{id}` - Get a single property by ID
- `GET /api/cities` - Get list of available cities

## Project Structure

```
property dealing website/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database operations
│   ├── seed_data.py      # Mock data seeding
│   └── requirements.txt  # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/   # React components
    │   ├── services/     # API services
    │   ├── lib/          # Utilities
    │   ├── App.jsx       # Main app component
    │   └── main.jsx      # Entry point
    ├── index.html
    └── package.json
```
