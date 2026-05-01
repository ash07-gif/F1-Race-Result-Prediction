# 🏎️ F1 Race Intelligence System

### AI-Powered Race Prediction • Performance Analytics • Simulation Engine

An advanced machine learning system designed to **predict Formula 1 race outcomes** and extract **deep performance insights** from race data.

This project goes beyond prediction—focusing on **race dynamics, driver behavior, and strategic intelligence**.

---

## 🎥 Preview

> Live dashboard featuring race predictions, timing tower, performance analytics, and driver insights.

*(Add screenshots here later for maximum impact)*

---

## 🚀 What This Project Does

* Predicts race finishing positions using machine learning
* Converts predictions into realistic race rankings
* Analyzes driver performance and consistency
* Simulates alternative race scenarios
* Provides interpretable insights into race dynamics

---

## 🧠 Core Capabilities

### 🏁 Race Outcome Prediction

* XGBoost-based regression model
* Converts predicted values → ranked positions
* Designed to mimic real race ordering

---

### 📊 Performance Analytics

* **Spearman Rank Correlation** → ranking accuracy
* **Mean Absolute Error (MAE)** → prediction quality
* **Position gain/loss analysis**

---

### 🎮 Simulation Engine

* Modify starting grid positions
* Re-run model predictions dynamically
* Observe impact on race outcome

---

### 🔍 Driver Intelligence System

* Driver performance trends over time
* Overtake skill estimation
* Consistency and variability analysis

---

### 🧊 Interactive Dashboard (Streamlit)

* F1-style “Race Control” interface
* Custom timing tower visualization
* Multi-tab analytical layout
* Real-time styled UI with glass effects

---

## 🏗️ System Architecture

```id="arch001"
             ┌──────────────────────────┐
             │     Raw Race Data        │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Feature Engineering      │
             │ (driver, team, track)    │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │   ML Model (XGBoost)     │
             │ Predict Finish Position  │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Rank Conversion Engine   │
             │ (Prediction → Ranking)   │
             └────────────┬─────────────┘
                          │
                          ▼
             ┌──────────────────────────┐
             │ Streamlit Dashboard      │
             │ Visualization + Insights │
             └──────────────────────────┘
```

---

## 📂 Project Structure

```id="struct001"
RACE RESULT ML/
│
├── backend/                  # Core ML pipeline
│   ├── f1_features.csv
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predict_race.py
│
├── streamlit_app/            # Interactive dashboard
│   ├── app.py
│
├── frontend-old/             # Frozen React UI (future upgrade)
│
├── notebooks/                # Experiments & exploration
│
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **Pandas / NumPy**
* **XGBoost**
* **Streamlit**
* **SciPy (Spearman correlation)**

---

## 🧪 Model Design

### 🔑 Features Used

* Grid position
* Average performance (last 5 races)
* Team strength
* Driver overtake skill
* Track characteristics

---

### ⚙️ Model

* **XGBoost Regressor**
* Outputs predicted finish position
* Converted into ranked race order

---

### 📏 Evaluation Metrics

| Metric               | Purpose                      |
| -------------------- | ---------------------------- |
| MAE                  | Measures prediction error    |
| Spearman Correlation | Measures ranking accuracy    |
| Gain/Loss            | Measures overtaking behavior |

---

## ▶️ How to Run

### 1. Activate environment

```id="run001"
source ~/f1env/bin/activate
```

### 2. Install dependencies

```id="run002"
pip install streamlit pandas numpy xgboost scipy
```

### 3. Run dashboard

```id="run003"
cd streamlit_app
streamlit run app.py
```

---

## 📊 Example Outputs

* 🏁 Live timing-style leaderboard
* 📊 Feature importance visualization
* 📈 Prediction error distribution
* 🎮 Simulation results

---

## 🧠 Key Insights This System Explores

* How much does qualifying impact final results?
* Which drivers consistently outperform expectations?
* How do team strength and track type affect outcomes?
* What factors drive overtaking ability?

---

## 🚀 Future Enhancements

* Advanced feature engineering (weather, tyre strategy)
* Ensemble models (LightGBM, Random Forest)
* Probabilistic predictions (win probability)
* Multi-race validation pipeline
* Real-time telemetry integration
* Full high-fidelity React UI

---

## 💡 Project Philosophy

This project prioritizes:

* **Depth over decoration**
* **Explainability over black-box prediction**
* **System design over isolated scripts**

---

## 📌 Status

🚧 Actively evolving — currently focused on improving model accuracy and feature engineering.

---

## 👨‍💻 Author

**Ashwi Porob**

---

## 🏁 Closing Note

> This is not just a race predictor.
> It is a step toward building an intelligent racing system.
