# Pandemonium: Real-Time Autonomous AI-Agent Swarm Arena

Pandemonium is a highly concurrent, real-time multi-agent simulation sandbox. It orchestrates hundreds of autonomous AI-driven entities (agents) that interact, survive, and navigate within a virtual arena. 

The project is built with a heavy focus on modern, asynchronous Python backend architecture, streaming live simulation state to a web dashboard via WebSockets.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn, WebSockets
* **Frontend:** React.js, HTML/CSS
* **Data Validation:** Pydantic

## Advanced Python Features Implemented
This project was engineered to demonstrate proficiency in high-performance Python patterns:
* **Async and Await:** The core simulation loop and WebSocket endpoints are entirely asynchronous, enabling the server to handle hundreds of concurrent agent calculations without blocking the main execution thread.
* **Generators:** Agent states are streamed memory-efficiently using Python generators, ensuring low RAM consumption even when scaling the simulation to massive numbers of entities.
* **Type Hints:** Strict static typing is enforced across all Pydantic data models and function signatures to eliminate state errors during dynamic payload processing.
* **Decorators:** Custom telemetry decorators are utilized to wrap execution loops, monitoring performance latency and logging execution times for asynchronous tasks.

## How to Run the Application

The application requires two terminal windows to run the backend and frontend simultaneously.

### 1. Start the Python Backend
Navigate to the backend directory, activate a virtual environment, install dependencies, and start the FastAPI server:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
