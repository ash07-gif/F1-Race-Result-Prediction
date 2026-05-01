import "./Podium.css";

export default function Podium({ drivers }) {
  const top3 = drivers.slice(0, 3);

  return (
    <div className="podium">
      <div className="p2">🥈 {top3[1]?.driver}</div>
      <div className="p1">🥇 {top3[0]?.driver}</div>
      <div className="p3">🥉 {top3[2]?.driver}</div>
    </div>
  );
}