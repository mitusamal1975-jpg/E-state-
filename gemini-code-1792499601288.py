from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS to allow the frontend to fetch data locally
CORS(app)

# Hardcoded mock properties for prototype
PROPERTIES = [
    {
        "id": 1,
        "title": "Luxury Sea-View Apartment",
        "location": "Worli, Mumbai",
        "price": "₹6.5 Cr",
        "bhk": 3,
        "area": "1,850 sqft",
        "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "title": "Modern Portuguese Villa",
        "location": "Assagao, Goa",
        "price": "₹12.2 Cr",
        "bhk": 4,
        "area": "4,200 sqft",
        "image": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "title": "Smart Tech Penthouse",
        "location": "Whitefield, Bengaluru",
        "price": "₹4.8 Cr",
        "bhk": 4,
        "area": "2,400 sqft",
        "image": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "title": "Eco-Friendly Golf Estate",
        "location": "Golf Course Ext, Gurugram",
        "price": "₹8.9 Cr",
        "bhk": 5,
        "area": "3,600 sqft",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 5,
        "title": "Heritage City Condo",
        "location": "Banjara Hills, Hyderabad",
        "price": "₹3.2 Cr",
        "bhk": 2,
        "area": "1,350 sqft",
        "image": "https://images.unsplash.com/photo-1502672260266-1c1e5240980c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    }
]

@app.route('/api/properties', methods=['GET'])
def get_properties():
    return jsonify(PROPERTIES)

if __name__ == '__main__':
    # Runs the app locally on port 5000
    app.run(debug=True, port=5000)
