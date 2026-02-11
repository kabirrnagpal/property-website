from database import Database

def seed_properties():
    """Seed the database with mock properties for Pune and Hyderabad"""
    db = Database()
    
    # Clear existing data
    db.clear_all_properties()
    
    # Pune Properties
    pune_properties = [
        {
            "title": "Luxurious 3BHK Apartment in Koregaon Park",
            "city": "Pune",
            "property_type": "rent",
            "price": 45000,
            "bedrooms": 3,
            "bathrooms": 2,
            "area": 1650,
            "address": "Koregaon Park, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800",
            "description": "Beautiful 3BHK apartment with modern amenities in the heart of Koregaon Park",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup"]
        },
        {
            "title": "Spacious 2BHK Flat in Hinjewadi",
            "city": "Pune",
            "property_type": "rent",
            "price": 28000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1200,
            "address": "Hinjewadi Phase 1, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "description": "Well-maintained 2BHK flat close to IT parks and shopping centers",
            "amenities": ["Parking", "Gym", "Security", "Power Backup", "Clubhouse"]
        },
        {
            "title": "Premium 4BHK Villa in Baner",
            "city": "Pune",
            "property_type": "buy",
            "price": 18500000,
            "bedrooms": 4,
            "bathrooms": 4,
            "area": 2800,
            "address": "Baner, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800",
            "description": "Stunning independent villa with garden and premium finishes",
            "amenities": ["Parking", "Garden", "Security", "Power Backup", "Modular Kitchen"]
        },
        {
            "title": "Cozy 1BHK Apartment in Kothrud",
            "city": "Pune",
            "property_type": "rent",
            "price": 15000,
            "bedrooms": 1,
            "bathrooms": 1,
            "area": 650,
            "address": "Kothrud, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800",
            "description": "Compact and affordable 1BHK perfect for singles or couples",
            "amenities": ["Parking", "Security", "Power Backup"]
        },
        {
            "title": "Modern 3BHK Penthouse in Viman Nagar",
            "city": "Pune",
            "property_type": "buy",
            "price": 12500000,
            "bedrooms": 3,
            "bathrooms": 3,
            "area": 2100,
            "address": "Viman Nagar, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800",
            "description": "Luxurious penthouse with terrace and city views",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Terrace"]
        },
        {
            "title": "Affordable 2BHK in Wakad",
            "city": "Pune",
            "property_type": "buy",
            "price": 6500000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1050,
            "address": "Wakad, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800",
            "description": "Great value 2BHK apartment in developing area",
            "amenities": ["Parking", "Gym", "Security", "Power Backup"]
        },
        {
            "title": "Elegant 3BHK in Magarpatta City",
            "city": "Pune",
            "property_type": "rent",
            "price": 38000,
            "bedrooms": 3,
            "bathrooms": 2,
            "area": 1500,
            "address": "Magarpatta City, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800",
            "description": "Premium apartment in self-sustained township",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Clubhouse", "Shopping Complex"]
        },
        {
            "title": "Spacious 4BHK Duplex in Aundh",
            "city": "Pune",
            "property_type": "buy",
            "price": 22000000,
            "bedrooms": 4,
            "bathrooms": 4,
            "area": 3200,
            "address": "Aundh, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800",
            "description": "Luxurious duplex with modern architecture and premium amenities",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Home Theater", "Garden"]
        },
        {
            "title": "Budget-Friendly 1BHK in Pimple Saudagar",
            "city": "Pune",
            "property_type": "rent",
            "price": 12000,
            "bedrooms": 1,
            "bathrooms": 1,
            "area": 600,
            "address": "Pimple Saudagar, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "description": "Affordable rental option near IT hubs",
            "amenities": ["Parking", "Security", "Power Backup"]
        },
        {
            "title": "Premium 2BHK in Kalyani Nagar",
            "city": "Pune",
            "property_type": "rent",
            "price": 35000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1300,
            "address": "Kalyani Nagar, Pune, Maharashtra",
            "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
            "description": "High-end apartment in upscale neighborhood",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Clubhouse"]
        }
    ]
    
    # Hyderabad Properties
    hyderabad_properties = [
        {
            "title": "Luxurious 3BHK in Gachibowli",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 42000,
            "bedrooms": 3,
            "bathrooms": 3,
            "area": 1800,
            "address": "Gachibowli, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=800",
            "description": "Modern apartment in IT corridor with excellent connectivity",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Clubhouse"]
        },
        {
            "title": "Spacious 2BHK in HITEC City",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 30000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1250,
            "address": "HITEC City, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800",
            "description": "Well-furnished apartment near major IT companies",
            "amenities": ["Parking", "Gym", "Security", "Power Backup"]
        },
        {
            "title": "Premium 4BHK Villa in Jubilee Hills",
            "city": "Hyderabad",
            "property_type": "buy",
            "price": 28000000,
            "bedrooms": 4,
            "bathrooms": 5,
            "area": 3500,
            "address": "Jubilee Hills, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800",
            "description": "Luxurious independent villa in prestigious location",
            "amenities": ["Parking", "Garden", "Swimming Pool", "Security", "Power Backup", "Home Theater"]
        },
        {
            "title": "Cozy 1BHK in Kondapur",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 16000,
            "bedrooms": 1,
            "bathrooms": 1,
            "area": 700,
            "address": "Kondapur, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=800",
            "description": "Compact apartment ideal for working professionals",
            "amenities": ["Parking", "Security", "Power Backup"]
        },
        {
            "title": "Modern 3BHK Penthouse in Banjara Hills",
            "city": "Hyderabad",
            "property_type": "buy",
            "price": 19500000,
            "bedrooms": 3,
            "bathrooms": 3,
            "area": 2400,
            "address": "Banjara Hills, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=800",
            "description": "Stunning penthouse with panoramic city views",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Terrace", "Clubhouse"]
        },
        {
            "title": "Affordable 2BHK in Miyapur",
            "city": "Hyderabad",
            "property_type": "buy",
            "price": 5500000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1100,
            "address": "Miyapur, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=800",
            "description": "Budget-friendly apartment with good connectivity",
            "amenities": ["Parking", "Security", "Power Backup", "Gym"]
        },
        {
            "title": "Elegant 3BHK in Madhapur",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 36000,
            "bedrooms": 3,
            "bathrooms": 2,
            "area": 1600,
            "address": "Madhapur, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=800",
            "description": "Premium apartment in prime IT location",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup"]
        },
        {
            "title": "Spacious 4BHK Duplex in Kokapet",
            "city": "Hyderabad",
            "property_type": "buy",
            "price": 16500000,
            "bedrooms": 4,
            "bathrooms": 4,
            "area": 2900,
            "address": "Kokapet, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800",
            "description": "Modern duplex in upcoming residential area",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Clubhouse"]
        },
        {
            "title": "Budget-Friendly 1BHK in Kukatpally",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 13000,
            "bedrooms": 1,
            "bathrooms": 1,
            "area": 650,
            "address": "Kukatpally, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600585154363-67eb9e2e2099?w=800",
            "description": "Affordable rental with easy access to metro",
            "amenities": ["Parking", "Security", "Power Backup"]
        },
        {
            "title": "Premium 2BHK in Financial District",
            "city": "Hyderabad",
            "property_type": "rent",
            "price": 38000,
            "bedrooms": 2,
            "bathrooms": 2,
            "area": 1400,
            "address": "Financial District, Hyderabad, Telangana",
            "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
            "description": "High-end apartment in business district",
            "amenities": ["Parking", "Gym", "Swimming Pool", "Security", "Power Backup", "Clubhouse", "Concierge"]
        }
    ]
    
    # Add all properties to database
    print("Seeding Pune properties...")
    for prop in pune_properties:
        db.add_property(prop)
    
    print("Seeding Hyderabad properties...")
    for prop in hyderabad_properties:
        db.add_property(prop)
    
    print(f"Successfully seeded {len(pune_properties) + len(hyderabad_properties)} properties!")

if __name__ == "__main__":
    seed_properties()
