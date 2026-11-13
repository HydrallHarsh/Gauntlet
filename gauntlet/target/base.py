"""Shared capabilities and interfaces for target adapters."""

from enum import Enum
from typing import Protocol

from gauntlet.models import AgentResponse, Turn


class Capability(str, Enum):
    """Operations a target adapter supports for evaluation and defense."""

    MULTI_TURN = "multi_turn"  # Accepts conversation history.
    TOOL_INSPECTION = "tool_inspection"  # Exposes tool calls and their results.
    TOOL_BLOCKING = "tool_blocking"  # Intercepts tool calls before execution.
    PROMPT_EDIT = "prompt_edit"  # Allows changes to the system prompt.
    STATE_VERIFICATION = "state_verification"  # Exposes world state for checks.


class TargetAgent(Protocol):
    """Target metadata and creation of a fresh episode session.

    Each new session must have its own world state. Concrete adapters supply
    the implementation; this protocol only describes their interface.
    """

    id: str
    version: str
    capabilities: frozenset[Capability]

    async def new_session(self, seed: int) -> "Session": ...


class Session(Protocol):
    """One episode's target interaction and optional world-state inspection.

    Tool interception is not yet part of this interface.
    """

    async def respond(self, history: list[Turn]) -> AgentResponse: ...

    def world_snapshot(self) -> dict | None:
        """Return world state, or None without STATE_VERIFICATION support."""
        ...
