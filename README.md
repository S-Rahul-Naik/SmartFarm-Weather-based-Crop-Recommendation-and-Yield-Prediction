# 🌾 SmartFarm - Weather-based Crop Recommendation & Yield Prediction

A comprehensive smart agriculture platform that empowers farmers with AI-driven crop recommendations, yield predictions, and flood risk analysis using real-time weather and environmental data.

---

## ✨ Features

### For Farmers & Users
- 🌱 **Crop Recommendation** — Get the best crop suggestions based on your local weather and soil data
- 📈 **Yield Prediction** — Predict expected crop yield using advanced machine learning models
- 🌊 **Flood Risk Assessment** — Analyze flood risk for your region using weather and environmental factors
- 📝 **User-friendly Forms** — Simple and intuitive data entry for weather, soil, and crop details
- 🔒 **User Authentication** — Secure login and data privacy
- 📊 **Result Visualization** — Clear, actionable results and recommendations
- 🖼️ **Modern UI** — Responsive and visually appealing web interface

### For Administrators
- 🛠️ **Admin Panel** — Manage users, monitor system health, and oversee model performance
- 📈 **Analytics Dashboard** — Track usage, predictions, and trends
- 🔧 **Model Management** — Retrain and update ML models as needed

---

## 🚀 Tech Stack

### Frontend
- **HTML5, CSS3** — Responsive design
- **Vanilla JS** (or integrate with React/Vue as needed)
- **Bootstrap/Tailwind** (optional for rapid UI)

### Backend
- **Python 3.8+**
- **Flask** — Web framework
- **scikit-learn, joblib** — ML model training and inference
- **Pandas, NumPy** — Data processing
- **Jinja2** — Templating

### ML Models
- **Crop Yield Model** — Predicts yield based on input features
- **Flood Risk Model** — Classifies flood risk using weather/environmental data

---

## 📁 Project Structure

```
SmartFarm/
├── backend/
│   ├── app.py                # Flask backend server
│   ├── requirements.txt      # Python dependencies
│   ├── static/
│   │   ├── image.png
│   │   └── style.css
│   └── templates/
│       ├── form.html
│       ├── login.html
│       └── result.html
├── frontend/
│   └── style.css
├── ml_models/
│   ├── crop_yield_model.joblib
│   ├── flood_risk_model.joblib
│   ├── train_crop_yield_model.py
│   └── train_flood_risk_model.py
└── README.md
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### 1. Clone the Repository
```bash
git clone https://github.com/S-Rahul-Naik/SmartFarm-Weather-based-Crop-Recommendation-and-Yield-Prediction.git
cd SmartFarm-Weather-based-Crop-Recommendation-and-Yield-Prediction
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### 3. Start the Application
```bash
python app.py
```

The application will be available at:
- Frontend: `http://127.0.0.1:5000/`
- Backend API: `http://127.0.0.1:5000/api` (if applicable)

---

## 🤖 Machine Learning Models

- Models are stored in the `ml_models/` directory
- To retrain models, run:
	- `python train_crop_yield_model.py`
	- `python train_flood_risk_model.py`
- Models are loaded automatically by the backend

---

## 🌟 Key Features Explained

### Crop Recommendation
- Suggests optimal crops based on weather, soil, and environmental data
- Utilizes historical and real-time data for accuracy

### Yield Prediction
- Predicts expected yield for selected crops
- Considers weather, soil, and crop management practices

### Flood Risk Assessment
- Analyzes flood risk using rainfall, soil moisture, and topography
- Provides actionable alerts and recommendations

### User Authentication
- Secure login and registration
- User data privacy ensured

### Admin Dashboard
- Manage users and monitor predictions
- Analytics on usage and model performance

---

## 🔐 Authentication & Authorization

- **Users** — Register, login, and access personalized recommendations
- **Admins** — Manage users, monitor system, and retrain models

---

## 📊 Result Visualization

- Clear tables and charts for recommendations and predictions
- Downloadable reports (future enhancement)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

- **Developer:** Sugali Rahul Naik
- **GitHub:** [@S-Rahul-Naik](https://github.com/S-Rahul-Naik)
- **Email:** [23rahul54@gmail.com](mailto:23rahul54@gmail.com)

## 📞 Support

For support and questions, please:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

## 🚧 Future Enhancements

- [ ] Weather API integration for real-time data
- [ ] Mobile app version
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] SMS/Email notifications
- [ ] Integration with government agri-data
- [ ] Downloadable reports
- [ ] More crop and risk models

---

⭐ **Star this repository if you find it helpful!**

Built with ❤️ by [Sugali Rahul Naik](https://github.com/S-Rahul-Naik)

**SmartFarm** — Empowering farmers with data-driven decisions for a sustainable future.
