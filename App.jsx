import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    // Connect to FastAPI WebSocket
    const ws = new WebSocket('ws://localhost:8000/ws/arena');

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setAgents(data.agents);
    };

    return () => ws.close();
  }, []);

  return (
    <div style={{ textAlign: 'center' }}>
      <h2>PANDEMONIUM: Swarm Arena</h2>
      <p>Active Autonomous Agents: {agents.length}</p>
      
      <div className="arena-container">
        {agents.map((agent) => (
          <div
            key={agent.id}
            className={`agent-node role-${agent.role}`}
            style={{
              left: `${agent.position.x}%`,
              top: `${agent.position.y}%`,
              opacity: agent.health / 100
            }}
            title={`${agent.id} | Wealth: $${agent.wealth.toFixed(2)}`}
          />
        ))}
      </div>
    </div>
  );
}

export default App;