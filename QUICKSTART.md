# Quick Start Guide

## 🚀 Running the Application

### Step 1: Start the Backend Server

The backend server is **already running** on `http://localhost:8000`

To verify it's working, open this URL in your browser:
- **API Documentation**: http://localhost:8000/docs
- **API Root**: http://localhost:8000
- **Get All Properties**: http://localhost:8000/api/properties

### Step 2: Install Frontend Dependencies

Open a **new terminal** and run:

```bash
cd "c:\Users\kabir\property dealing website\frontend"
npm install
```

> **Note**: This will install React, Vite, Tailwind CSS, Shadcn/UI components, and Lucide React icons.

### Step 3: Start the Frontend Development Server

After installation completes, run:

```bash
npm run dev
```

The frontend will start on: **http://localhost:5173**

### Step 4: Open the Application

Open your browser and navigate to:
```
http://localhost:5173
```

---

## 🎯 Testing the Features

### Search and Filter
1. **City Filter**: Select "Pune" or "Hyderabad" from the dropdown
2. **Property Type**: Choose "For Rent" or "For Sale"
3. **Budget Range**: 
   - For Rent: Try min=10000, max=50000
   - For Sale: Try min=5000000, max=20000000
4. Click **Search** to apply filters
5. Click **Reset** to clear all filters

### Example Searches

**Rental Properties in Pune**
- City: Pune
- Property Type: For Rent
- Result: 5 properties ranging from ₹12,000 to ₹45,000/month

**Properties for Sale in Hyderabad under 1 Crore**
- City: Hyderabad
- Property Type: For Sale
- Max Budget: 10000000
- Result: 1 property (₹55L in Miyapur)

**All 3BHK Properties**
- Leave filters empty, browse all 20 properties
- Look for properties with 3 bedrooms

---

## 📊 What to Expect

### Main Page Features
- ✨ Clean header with PropertySearch branding
- 🔍 Search bar with multiple filters
- 📋 Grid of property cards (responsive: 1/2/3 columns)
- 🏠 Each card shows:
  - Property image with hover zoom effect
  - Title and location
  - Bedrooms, bathrooms, area
  - Price in Indian format (Cr/L)
  - Amenities tags
  - "For Rent" or "For Sale" badge

### Design Highlights
- Modern Airbnb-style aesthetics
- Smooth hover animations
- Clean white-space heavy layout
- Gradient background
- Inter font from Google Fonts

---

## 🛠️ Troubleshooting

### Backend Not Running?
```bash
cd "c:\Users\kabir\property dealing website\backend"
python -m uvicorn main:app --reload
```

### Frontend Shows "Failed to load properties"?
- Make sure backend is running on port 8000
- Check browser console for errors
- Verify CORS is working (should be automatic)

### npm Not Found?
- Install Node.js from: https://nodejs.org/
- Restart your terminal after installation

---

## 📁 Project Files

All files are located in:
```
c:\Users\kabir\property dealing website\
├── backend/          # FastAPI server (currently running)
└── frontend/         # React application (needs npm install)
```

See [README.md](file:///c:/Users/kabir/property%20dealing%20website/README.md) for complete documentation.
