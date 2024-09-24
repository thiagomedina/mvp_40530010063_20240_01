import { useState, useEffect } from "react";
import "./App.css";

const API_URL = 'http://localhost:5000'
const App = () => {
  const [trend, setTrend] = useState("");

  useEffect(() => {
    fetch(`${API_URL}/trend`)
      .then((response) => response.json())
      .catch((error) => console.error("error", error));
  }, []);


  const getTrend = () => {
    fetch(`${API_URL}/trend`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setTrend(data.description);
      })
      .catch((error) => console.error("error:", error));
  }
  return (
    <div className="App">
      <h1>Veja a tendencia do Bitcoin para amanhã</h1>
      <h2>{trend}</h2>
      <button onClick={getTrend}>Ver tendência</button>
    </div>
  );
};

export default App;
