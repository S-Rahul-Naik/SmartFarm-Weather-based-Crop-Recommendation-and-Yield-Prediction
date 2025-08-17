from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import joblib
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'smartfarm_secret_key'

# Load ML models (placeholders, replace with actual trained models)
crop_model = joblib.load(os.path.join('..', 'ml_models', 'crop_yield_model.joblib'))
flood_model = joblib.load(os.path.join('..', 'ml_models', 'flood_risk_model.joblib'))

OPENWEATHER_API_KEY = 'cf85fa57d8fd380d9acac6d11132bd28'  # Replace with your API key

SUPPORTED_CROPS = [
    'rice', 'wheat', 'ragi', 'maize', 'barley', 'corn', 'sorghum', 'millet', 'soybean', 'groundnut',
    'sugarcane', 'cotton', 'mustard', 'sunflower', 'chickpea', 'lentil', 'pea', 'pigeonpea', 'blackgram',
    'greengram', 'sesame', 'potato', 'onion', 'tomato', 'cabbage', 'cauliflower', 'carrot', 'spinach',
    'brinjal', 'okra', 'pumpkin', 'cucumber', 'radish', 'turnip', 'sweet potato', 'yam', 'beetroot',
    'garlic', 'ginger', 'turmeric', 'chili', 'pepper', 'cardamom', 'tea', 'coffee', 'banana', 'mango',
    'papaya', 'pineapple', 'guava', 'apple', 'grapes', 'orange', 'lemon', 'watermelon', 'muskmelon',
    'pomegranate', 'lychee', 'sapota', 'jackfruit', 'custard apple', 'fig', 'date palm', 'coconut',
    'arecanut', 'cashew', 'rubber', 'oil palm', 'betelvine', 'tobacco', 'jute', 'hemp', 'flax',
    'safflower', 'linseed', 'castor', 'other'
]

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'farmer' and password == 'smart123':
            session['user'] = username
            return redirect(url_for('form'))
        else:
            flash('Invalid login')
    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        location = request.form['location']
        crop = request.form['crop'].lower()
        if crop not in SUPPORTED_CROPS:
            flash('Unsupported crop selected.')
            return render_template('form.html')
        # Fetch weather data
        weather = fetch_weather(location)
        if not weather:
            flash('Could not fetch weather data.')
            return render_template('form.html')
        # ML predictions
        yield_pred = predict_yield(crop, weather)
        flood_risk = predict_flood_risk(weather)
        recommendation = get_recommendation(crop, weather, yield_pred, flood_risk)
        return render_template('result.html', location=location, crop=crop, weather=weather, yield_pred=yield_pred, flood_risk=flood_risk, recommendation=recommendation)
    return render_template('form.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

def fetch_weather(location):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric'
    print(f"Requesting weather data from: {url}")
    try:
        resp = requests.get(url)
        data = resp.json()
        if resp.status_code != 200:
            print(f"Weather API error: {data.get('message', 'Unknown error')} (status {resp.status_code})")
            return None
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        rain = data.get('rain', {}).get('1h', 0)
        return {'temp': temp, 'humidity': humidity, 'rain': rain}
    except Exception as e:
        print(f"Exception in fetch_weather: {e}")
        return None

def predict_yield(crop, weather):
    # Placeholder: Replace with actual model prediction
    features = np.array([[weather['temp'], weather['humidity'], weather['rain']]])
    return crop_model.predict(features)[0]

def predict_flood_risk(weather):
    # Placeholder: Replace with actual model prediction
    rain = weather['rain']
    return 'High' if rain > 70 else 'Low'

def get_recommendation(crop, weather, yield_pred, flood_risk):
    temp = weather['temp']
    rain = weather['rain']
    if crop == 'rice':
        if rain < 30:
            return 'Not enough rainfall for rice.'
        elif temp < 20 or temp > 35:
            return 'Temperature not suitable for rice.'
        else:
            return 'Good conditions for rice.'
    elif crop == 'wheat':
        if temp > 32:
            return 'Too hot for wheat.'
        elif rain > 60:
            return 'Too much rainfall for wheat.'
        else:
            return 'Suitable for wheat cultivation.'
    elif crop == 'ragi':
        if rain < 20:
            return 'Insufficient rainfall for ragi.'
        elif temp < 22 or temp > 35:
            return 'Temperature not suitable for ragi.'
        else:
            return 'Conditions are good for ragi.'
    # Generic recommendation for all other crops
    else:
        if rain < 10:
            return f'Rainfall may be insufficient for {crop}.'
        elif temp < 10 or temp > 40:
            return f'Temperature may not be suitable for {crop}.'
        else:
            return f'Weather conditions are generally suitable for {crop}.'

if __name__ == '__main__':
    app.run(debug=True)
