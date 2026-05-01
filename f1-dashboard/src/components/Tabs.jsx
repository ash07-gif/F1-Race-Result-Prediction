import "./Tabs.css";

export default function Tabs({ active, setActive }) {
  const tabs = ["Leaderboard", "Simulation", "Analytics"];

  return (
    <div className="tabs">
      {tabs.map((tab, i) => (
        <div
          key={i}
          className={`tab ${active === i ? "active" : ""}`}
          onClick={() => setActive(i)}
        >
          {tab}
        </div>
      ))}

      <div
        className="underline"
        style={{ transform: `translateX(${active * 100}%)` }}
      />
    </div>
  );
}