import "./TimingTower.css";

export default function TimingTower({ drivers }) {

  if (!drivers || drivers.length === 0) return null;

  return (
    <div className="tower">
      {drivers.map((d, i) => {

        const gain = (d.grid_pos ?? 0) - (d.predicted_rank ?? 0);

        const gap = i === 0
          ? "LEADER"
          : `+${(i * 1.2).toFixed(1)}s`;

        return (
          <div key={i} className="row">

            <div className="left">
              <span>#{d.predicted_rank ?? "-"}</span>
              <span>{d.driver ?? "UNK"}</span>
            </div>

            <div className="right">
              <span>{gap}</span>
              <span>P{d.grid_pos ?? "-"}</span>
              <span>{gain}</span>
            </div>

          </div>
        );
      })}
    </div>
  );
}