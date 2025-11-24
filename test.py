  
import os, asyncio
from pathlib import Path
from dotenv import load_dotenv
from google.genai import Client
from janus_sdk import run_simulations, track

@track                          # ① traces this helper (inputs • output • timing)
def add(a: int, b: int) -> int:
    return a + b

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / "gemini-fullstack-langgraph-quickstart-main" / "gemini-fullstack-langgraph-quickstart-main" / "backend" / ".env"
load_dotenv(ENV_PATH)


class Agent:                    # ② exactly one async chat method
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set. Check backend/.env.")
        self.llm = Client(api_key=api_key)
        self.model = "gemini-2.0-flash"

    async def chat(self, prompt: str, **kwargs) -> str:
        prompt += f"  (2+3={add(2,3)})"     # use the tracked helper
        response = self.llm.models.generate_content(
            model=self.model,
            contents=prompt,
            config={"temperature": 0.8, "max_output_tokens": 256},
        )
        return response.text

from janus_sdk import record_tool_event, start_tool_event, finish_tool_event

# One-shot tracing for simple operations
record_tool_event("weather_api", "location: NYC", "temperature: 72°F")

# Start/finish pattern for long-running operations
handle = start_tool_event("database_query", "SELECT * FROM users")
# ... do work ...
finish_tool_event(handle, "1000 rows returned")

# Error handling
try:
    result = call_external_api()
    record_tool_event("api_call", "request", result)
except Exception as e:
    record_tool_event("api_call", "request", error=e)

async def main():             

  persona_kwargs = {
    "wearable_data": {"hr": 70},
    "questionnaire_data": {"stress": 8}
} # user context data
  
  await run_simulations(
      target_agent=lambda: Agent().chat,   
      api_key=os.getenv("JANUS_API_KEY"),
      num_simulations=5,                   
      max_turns=2,
      persona_kwargs=persona_kwargs              
  )

if __name__ == "__main__":
  asyncio.run(main())