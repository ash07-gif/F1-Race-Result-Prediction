import pandas as pd
import streamlit as st
from xgboost import XGBRegressor
from scipy.stats import spearmanr
import time

# -----------------------------------
# 🎨 PAGE CONFIG
# -----------------------------------
st.set_page_config(layout="wide")

# -----------------------------------
# 🎥 BACKGROUND VIDEO
# -----------------------------------
st.markdown("""
<style>
video {
    position: fixed;
    top: 0;
    left: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    object-fit: cover;
    opacity: 0.15;
}
</style>

<video autoplay muted loop>
    <source src="https://cdn.coverr.co/videos/coverr-formula-race-car-1603/1080p.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# -----------------------------------
# 🎨 F1 FONT + GLASS UI
# -----------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
    color: white;
}

/* Background overlay */
.stApp {
    background: linear-gradient(135deg, rgba(11,15,26,0.9), rgba(17,24,39,0.9));
}

/* Glass effect */
[data-testid="stDataFrame"], .stMetric {
    background: rgba(17, 24, 39, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    padding: 10px;
}

/* Headers */
h1, h2, h3 {
    color: #ff1e1e;
    letter-spacing: 1px;
}

/* Pulse animation */
@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}

.live {
  animation: pulse 1.5s infinite;
  text-align: center;
  font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# 🏎️ HEADER
# -----------------------------------
st.markdown("<h1>🏎️ F1 RACE CONTROL</h1>", unsafe_allow_html=True)
st.caption("Live Prediction Engine • ML Powered")
st.markdown('<div class="live">🔴 LIVE TIMING</div>', unsafe_allow_html=True)

# -----------------------------------
# ⏳ LOADING EFFECT
# -----------------------------------
with st.spinner("Loading race intelligence..."):
    time.sleep(1)

# -----------------------------------
# 📂 LOAD DATA
# -----------------------------------
df = pd.read_csv("f1_features.csv")

race_id = df['race'].max()

train_df = df[df['race'] < race_id]
test_df = df[df['race'] == race_id].copy()

features = [
    'grid_pos',
    'avg_last5',
    'team_strength',
    'driver_overtake_skill',
    'track_type_power',
    'track_type_street'
]

# -----------------------------------
# 🧠 MODEL
# -----------------------------------
model = XGBRegressor(n_estimators=150, learning_rate=0.08)
model.fit(train_df[features], train_df['finish_pos'])

test_df['predicted_pos'] = model.predict(test_df[features])

test_df = test_df.sort_values(by='predicted_pos')
test_df['predicted_rank'] = range(1, len(test_df)+1)

corr, _ = spearmanr(test_df['predicted_rank'], test_df['finish_pos'])

# -----------------------------------
# 🏁 TIMING TOWER
# -----------------------------------
def timing_tower(df):
    for _, row in df.iterrows():
        pos = int(row['predicted_rank'])
        driver = row['driver']
        grid = int(row['grid_pos'])
        actual = int(row['finish_pos'])

        diff = pos - actual

        if abs(diff) <= 2:
            color = "#00ff88"
        elif abs(diff) <= 5:
            color = "#ffaa00"
        else:
            color = "#ff4d4d"

        st.markdown(f"""
        <div style="
            display:flex;
            justify-content:space-between;
            background: rgba(17,24,39,0.7);
            padding:12px;
            margin:6px 0;
            border-left:5px solid {color};
            border-radius:8px;
        ">
            <span><b>#{pos}</b></span>
            <span>{driver}</span>
            <span>Grid: {grid}</span>
            <span>Δ {grid - pos:+}</span>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------
# 🧭 HORIZONTAL TABS
# -----------------------------------
tab1, tab2, tab3 = st.tabs([
    "🏁 Race Control",
    "📊 Performance",
    "🔍 Driver Analysis"
])

# -----------------------------------
# 🏁 TAB 1 — RACE CONTROL
# -----------------------------------
with tab1:

    st.markdown("## 🏁 LIVE TIMING TOWER")
    timing_tower(test_df)

    st.markdown("## 🏆 Predicted Podium")

    podium = test_df.head(3)

    col1, col2, col3 = st.columns(3)

    with col2:
        st.success(f"🥇 {podium.iloc[0]['driver']}")
    with col1:
        st.info(f"🥈 {podium.iloc[1]['driver']}")
    with col3:
        st.warning(f"🥉 {podium.iloc[2]['driver']}")

# -----------------------------------
# 📊 TAB 2 — PERFORMANCE
# -----------------------------------
with tab2:

    st.markdown("## 📈 Model Performance")
    st.metric("Spearman Rank Correlation", f"{corr:.2f}")

    test_df['positions_gained'] = test_df['grid_pos'] - test_df['finish_pos']

    st.markdown("## 📊 Positions Gained")

    st.bar_chart(
        test_df.set_index('driver')['positions_gained']
    )

# -----------------------------------
# 🔍 TAB 3 — DRIVER ANALYSIS
# -----------------------------------
with tab3:

    st.markdown("## 🔍 Driver Deep Dive")

    driver = st.selectbox("Select Driver", df['driver'].unique())

    driver_data = df[df['driver'] == driver]

    st.line_chart(
        driver_data.set_index('race')['finish_pos']
    )