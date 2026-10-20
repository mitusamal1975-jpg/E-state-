from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Frontend ko backend se connect karne ke liye

# Seminar ke liye Realistic Mock Data
properties_data = [
    {
        "id": 1,
        "title": "Luxury 3BHK Apartment",
        "location": "Bhubaneswar, Odisha",
        "price": "₹80 Lakh",
        "bhk": 3,
        "area": "1500 sqft",
        "type": "Buy",
        "image": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=400&q=80"
    },
    {
        "id": 2,
        "title": "Modern Studio Rent",
        "location": "Andheri, Mumbai",
        "price": "₹35,000/month",
        "bhk": 1,
        "area": "600 sqft",
        "type": "Rent",
        "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=400&q=80"
    },
    {
        "id": 3,
        "title": "Sea-View Villa",
        "location": "Goa, India",
        "price": "₹2.5 Crore",
        "bhk": 4,
        "area": "3200 sqft",
        "type": "Buy",
        "image": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=400&q=80"
    }
]

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # Yeh API frontend ko ghar recommend karegi
    return jsonify({
        "status": "success",
        "message": "AI Recommendations loaded",
        "data": properties_data
    })

if __name__ == '__main__':
    print("EstateAI Backend Server is running on port 5000...")
    app.run(debug=True, port=5000)
