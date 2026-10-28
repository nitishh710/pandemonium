from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from agents import SwarmArena
from utils import telemetry_tracker

app = FastAPI(title="Pandemonium Swarm API")
arena = SwarmArena(num_agents=200)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@telemetry_tracker
async def simulation_loop():
    """Background task orchestrating the arena."""
    while arena.running:
        await arena.compute_step()
        await asyncio.sleep(0.05) # Tick rate of 20 FPS

@app.on_event("startup")
async def startup_event():
    arena.running = True
    asyncio.create_task(simulation_loop())

@app.websocket("/ws/arena")
async def arena_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Construct payload using the Generator
            payload = list(arena.stream_state())
            await websocket.send_json({"agents": payload})
            await asyncio.sleep(0.05) # Frontend update rate
    except WebSocketDisconnect:
        print("Dashboard client disconnected")