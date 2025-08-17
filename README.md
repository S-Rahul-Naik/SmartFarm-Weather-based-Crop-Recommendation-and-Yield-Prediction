# SmartFarm: Weather-based Crop Recommendation and Yield Prediction

## Overview
SmartFarm is a web application that helps farmers make informed decisions by providing weather-based crop recommendations, yield predictions, and flood risk assessments for their location and selected crop. The system uses real-time weather data and machine learning models to generate actionable insights.

## Features
- User authentication (login/logout)
- Enter location and select/search crop (with support for many crops)
- Fetches real-time weather data using OpenWeatherMap API
- Predicts crop yield using a trained ML model
- Assesses flood risk using a trained ML model
- Provides tailored recommendations based on weather and crop
- Modern, responsive UI with background imagery and animations
- Searchable crop selection with autocomplete

## Project Structure
```
backend/
	app.py                # Flask backend, API, and ML integration
	requirements.txt      # Python dependencies
	static/
		image.png           # Background image
		style.css           # Main stylesheet
	templates/
		form.html           # Crop/location input form
		login.html          # Login page
		result.html         # Results and recommendations
ml_models/
	crop_yield_model.joblib      # Trained crop yield model
	flood_risk_model.joblib      # Trained flood risk model
	train_crop_yield_model.py    # Script to train crop yield model
	train_flood_risk_model.py    # Script to train flood risk model
README.md
```

## How It Works
1. **Login:** User logs in with credentials (default: farmer/smart123).
2. **Input:** User enters a location and selects or searches for a crop.
3. **Weather Fetch:** The app fetches current weather data for the location from OpenWeatherMap.
4. **Prediction:** ML models predict crop yield and flood risk based on weather and crop.
5. **Recommendation:** The app provides a recommendation message based on the crop, weather, and predictions.
6. **Result:** All details are shown in a visually appealing result card.

## Supported Crops
- Rice, Wheat, Ragi, Maize, Barley, Corn, Sorghum, Millet, Soybean, Groundnut, Sugarcane, Cotton, Mustard, Sunflower, Chickpea, Lentil, Pea, Pigeonpea, Blackgram, Greengram, Sesame, Potato, Onion, Tomato, Cabbage, Cauliflower, Carrot, Spinach, Brinjal, Okra, Pumpkin, Cucumber, Radish, Turnip, Sweet Potato, Yam, Beetroot, Garlic, Ginger, Turmeric, Chili, Pepper, Cardamom, Tea, Coffee, Banana, Mango, Papaya, Pineapple, Guava, Apple, Grapes, Orange, Lemon, Watermelon, Muskmelon, Pomegranate, Lychee, Sapota, Jackfruit, Custard Apple, Fig, Date Palm, Coconut, Arecanut, Cashew, Rubber, Oil Palm, Betelvine, Tobacco, Jute, Hemp, Flax, Safflower, Linseed, Castor, Other

## Setup Instructions
1. **Clone the repository** (or copy the project files to your machine).
2. **Install Python dependencies:**
	 ```bash
	 pip install -r backend/requirements.txt
	 ```
3. **Add your OpenWeatherMap API key** in `backend/app.py` (replace the placeholder).
4. **Ensure ML models are present** in the `ml_models/` directory. If not, train them using the provided scripts.
5. **Run the Flask app:**
	 ```bash
	 cd backend
	 python app.py
	 ```
6. **Open your browser** and go to `http://127.0.0.1:5000/`

## Notes
- The ML models are placeholders; for best results, train them with your own data.
- The crop recommendation logic can be extended in `app.py` for more crops.
- The UI is fully responsive and works on desktop and mobile.
- Scrollbars are hidden for a cleaner look.

## License
This project is for educational/demo purposes. Please adapt and extend as needed for production use.
