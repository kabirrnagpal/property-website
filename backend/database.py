import sqlite3
from typing import List, Dict, Optional
import json

class Database:
    def __init__(self, db_name: str = "properties.db"):
        self.db_name = db_name
        self.init_db()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Initialize the database with properties table"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                city TEXT NOT NULL,
                property_type TEXT NOT NULL,
                price INTEGER NOT NULL,
                bedrooms INTEGER NOT NULL,
                bathrooms INTEGER NOT NULL,
                area INTEGER NOT NULL,
                address TEXT NOT NULL,
                image_url TEXT,
                description TEXT,
                amenities TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_property(self, property_data: Dict):
        """Add a new property to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO properties 
            (title, city, property_type, price, bedrooms, bathrooms, area, address, image_url, description, amenities)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            property_data['title'],
            property_data['city'],
            property_data['property_type'],
            property_data['price'],
            property_data['bedrooms'],
            property_data['bathrooms'],
            property_data['area'],
            property_data['address'],
            property_data['image_url'],
            property_data['description'],
            json.dumps(property_data['amenities'])
        ))
        
        conn.commit()
        property_id = cursor.lastrowid
        conn.close()
        return property_id
    
    def get_properties(self, city: Optional[str] = None, 
                      property_type: Optional[str] = None,
                      min_budget: Optional[int] = None,
                      max_budget: Optional[int] = None) -> List[Dict]:
        """Get properties with optional filters"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM properties WHERE 1=1"
        params = []
        
        if city:
            query += " AND city = ?"
            params.append(city)
        
        if property_type:
            query += " AND property_type = ?"
            params.append(property_type)
        
        if min_budget is not None:
            query += " AND price >= ?"
            params.append(min_budget)
        
        if max_budget is not None:
            query += " AND price <= ?"
            params.append(max_budget)
        
        query += " ORDER BY price ASC"
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        properties = []
        for row in rows:
            prop = dict(row)
            prop['amenities'] = json.loads(prop['amenities']) if prop['amenities'] else []
            properties.append(prop)
        
        conn.close()
        return properties
    
    def get_property_by_id(self, property_id: int) -> Optional[Dict]:
        """Get a single property by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM properties WHERE id = ?", (property_id,))
        row = cursor.fetchone()
        
        if row:
            prop = dict(row)
            prop['amenities'] = json.loads(prop['amenities']) if prop['amenities'] else []
            conn.close()
            return prop
        
        conn.close()
        return None
    
    def clear_all_properties(self):
        """Clear all properties from the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM properties")
        conn.commit()
        conn.close()
