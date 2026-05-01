import Dashboard from "./pages/Dashboard";
import "./App.css";

function App() {
  return (
    <>
      {/* <video autoPlay loop muted className="bg-video">
        <source src="/f1.mp4" type="video/mp4" />
      </video> */}

      <div className="overlay">
        <Dashboard />
      </div>
    </>
  );
}

export default App;