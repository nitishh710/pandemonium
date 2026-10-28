from pydantic import BaseModel
from typing import Literal

# Strict Type Hints applied across all data structures
class Position(BaseModel):
    x: float
    y: float

class AgentState(BaseModel):
    id: str
    role: Literal["Trader", "Predator", "Scavenger"]
    wealth: float
    health: float
    position: Position
    is_active: bool