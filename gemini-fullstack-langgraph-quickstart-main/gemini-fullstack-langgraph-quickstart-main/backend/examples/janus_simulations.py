"""
Run Janus simulations against the Gemini LangGraph research agent.

Prereqs:
  - pip install janus-sdk (added to pyproject)
  - export JANUS_API_KEY and GEMINI_API_KEY
"""

import asyncio
import os
from typing import Any, Dict, Optional

from langchain_core.messages import HumanMessage

from agent.graph import graph

try:
    from janus_sdk import run_simulations, track
except ImportError as exc:
    raise SystemExit(
        "janus-sdk is required. Install with `pip install janus-sdk`."
    ) from exc


@track
async def run_research(
    prompt: str,
    *,
    initial_queries: int,
    max_loops: int,
    reasoning_model: str,
    **kwargs: Any,
) -> str:
    """Tracked wrapper around the LangGraph research run."""
    state: Dict[str, Any] = {
        "messages": [HumanMessage(content=prompt)],
        "initial_search_query_count": kwargs.get(
            "initial_search_query_count", initial_queries
        ),
        "max_research_loops": kwargs.get("max_research_loops", max_loops),
        "reasoning_model": kwargs.get("reasoning_model", reasoning_model),
    }
    result = await graph.ainvoke(state)
    messages = result.get("messages") or []
    return messages[-1].content if messages else ""


class GeminiResearchAgent:
    """Wraps the LangGraph research agent with a Janus-compatible chat method."""

    def __init__(
        self,
        *,
        initial_queries: int = 3,
        max_loops: int = 2,
        reasoning_model: str = "gemini-2.5-pro",
    ) -> None:
        self.initial_queries = initial_queries
        self.max_loops = max_loops
        self.reasoning_model = reasoning_model

    async def chat(self, prompt: str, **kwargs: Any) -> str:
        """Janus target function: accepts a prompt and returns the final answer."""
        return await run_research(
            prompt,
            initial_queries=self.initial_queries,
            max_loops=self.max_loops,
            reasoning_model=self.reasoning_model,
            **kwargs,
        )


async def main(
    *,
    num_simulations: int = 2,
    max_turns: int = 2,
    persona_kwargs: Optional[Dict[str, Any]] = None,
) -> None:
    api_key = os.getenv("JANUS_API_KEY")
    if not api_key:
        raise SystemExit("JANUS_API_KEY is not set")

    persona_kwargs = persona_kwargs or {
        "wearable_data": {"hr": 70},
        "questionnaire_data": {"stress": 8},
    }

    await run_simulations(
        target_agent=lambda: GeminiResearchAgent().chat,
        api_key=api_key,
        num_simulations=num_simulations,
        max_turns=max_turns,
        context="Smoke test Gemini research agent with Janus simulations.",
        goal="Verify the agent returns cited research answers without errors.",
        persona_kwargs=persona_kwargs,
    )


if __name__ == "__main__":
    asyncio.run(main())
