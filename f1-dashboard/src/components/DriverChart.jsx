export default function DriverChart({ drivers }) {

  if (!drivers || drivers.length === 0) return null;

  return (
    <div style={{ textAlign: "center", color: "white" }}>
      <h2>📊 Analytics</h2>

      {drivers.map((d, i) => (
        <div key={i}>
          {d.driver} → Position {d.predicted_rank}
        </div>
      ))}
    </div>
  );
}