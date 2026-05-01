import "./SimulationPanel.css";
import { useState, useEffect } from "react";

export default function SimulationPanel({ drivers, setDrivers }) {

  if (!drivers || drivers.length === 0) return null;

  const [grid, setGrid] = useState([]);

  useEffect(() => {
    setGrid(drivers);
  }, [drivers]);

  const simulate = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/simulate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ drivers: grid })
      });

      const data = await res.json();
      setDrivers(data);
    } catch {
      console.log("Simulation failed");
    }
  };

  return (
    <div className="sim-panel">
      <h2>Simulation</h2>

      {grid.map((d, i) => (
        <div key={i}>
          {d.driver}
        </div>
      ))}

      <button onClick={simulate}>Run Simulation</button>
    </div>
  );
}