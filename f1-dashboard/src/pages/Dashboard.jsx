import { useEffect, useState, useRef } from "react";
import Header from "../components/Header";
import Tabs from "../components/Tabs";
import TimingTower from "../components/TimingTower";
import SimulationPanel from "../components/SimulationPanel";
import DriverChart from "../components/DriverChart";
import "./Dashboard.css";

export default function Dashboard() {

  const [drivers, setDrivers] = useState([]);
  const [activeTab, setActiveTab] = useState(0);

  const startX = useRef(0);

  // 🔹 FETCH DATA
  useEffect(() => {
    fetch("http://127.0.0.1:8000/predict")
      .then(res => res.json())
      .then(data => setDrivers(data))
      .catch(() => setDrivers([]));
  }, []);

  // ⚡ REAL-TIME RACE SIMULATION (SAFE)
  useEffect(() => {
    const interval = setInterval(() => {
      setDrivers(prev => {
        if (!prev || prev.length === 0) return prev;

        let updated = [...prev];

        // simulate overtakes
        const i = Math.floor(Math.random() * (updated.length - 1));

        if (Math.random() > 0.7) {
          [updated[i], updated[i + 1]] = [updated[i + 1], updated[i]];
        }

        return updated.map((d, index) => ({
          ...d,
          predicted_rank: index + 1
        }));
      });
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  // 👉 SWIPE SUPPORT (mobile feel)
  const handleTouchStart = (e) => {
    startX.current = e.touches[0].clientX;
  };

  const handleTouchEnd = (e) => {
    const diff = startX.current - e.changedTouches[0].clientX;

    if (diff > 50 && activeTab < 2) setActiveTab(activeTab + 1);
    if (diff < -50 && activeTab > 0) setActiveTab(activeTab - 1);
  };

  return (
    <div className="dashboard">

      {/* HEADER */}
      <Header />

      {/* TABS */}
      <Tabs active={activeTab} setActive={setActiveTab} />

      {/* LOADING STATE */}
      {drivers.length === 0 ? (
        <div style={{ textAlign: "center", color: "white" }}>
          Loading race data...
        </div>
      ) : (

        <div
          className="slider-container"
          onTouchStart={handleTouchStart}
          onTouchEnd={handleTouchEnd}
        >

          <div
            className="slider"
            style={{
              transform: `translateX(-${activeTab * 100}%)`
            }}
          >

            {/* 🏁 TAB 1 — LEADERBOARD */}
            <div className="slide">
              <TimingTower drivers={drivers} />
            </div>

            {/* 🎮 TAB 2 — SIMULATION */}
            <div className="slide">
              <SimulationPanel
                drivers={drivers}
                setDrivers={setDrivers}
              />
            </div>

            {/* 📊 TAB 3 — ANALYTICS */}
            <div className="slide">
              <DriverChart drivers={drivers} />
            </div>

          </div>

        </div>
      )}

    </div>
  );
}