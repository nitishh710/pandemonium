import random
import asyncio
from typing import Iterator, List
from models import AgentState, Position

class SwarmArena:
    def __init__(self, num_agents: int = 150):
        self.agents: List[AgentState] = [self._spawn_agent(f"agent_{i}") for i in range(num_agents)]
        self.running: bool = False

    def _spawn_agent(self, agent_id: str) -> AgentState:
        return AgentState(
            id=agent_id,
            role=random.choice(["Trader", "Predator", "Scavenger"]),
            wealth=random.uniform(10.0, 100.0),
            health=100.0,
            position=Position(x=random.uniform(0, 100), y=random.uniform(0, 100)),
            is_active=True
        )

    async def compute_step(self) -> None:
        """Asynchronous update loop for autonomous agents."""
        for agent in self.agents:
            if not agent.is_active:
                continue
                
            # Simulate autonomous movement/decisions
            agent.position.x = max(0, min(100, agent.position.x + random.uniform(-2, 2)))
            agent.position.y = max(0, min(100, agent.position.y + random.uniform(-2, 2)))
            
            # Simulate market drain
            agent.wealth -= 0.1 
            if agent.wealth <= 0:
                agent.is_active = False

        # Yield execution back to the event loop
        await asyncio.sleep(0.01) 

    def stream_state(self) -> Iterator[dict]:
        """Memory-efficient Generator yielding agent states one-by-one."""
        for agent in self.agents:
            # Only stream active agents to save bandwidth
            if agent.is_active:
                yield agent.model_dump()