"""Shared capability vocabulary for target adapters."""

from enum import Enum


class Capability(str, Enum):
    """Operations a target adapter supports for evaluation and defense."""

    MULTI_TURN = "multi_turn"  # Accepts conversation history.
    TOOL_INSPECTION = "tool_inspection"  # Exposes tool calls and their results.
    TOOL_BLOCKING = "tool_blocking"  # Intercepts tool calls before execution.
    PROMPT_EDIT = "prompt_edit"  # Allows changes to the system prompt.
    STATE_VERIFICATION = "state_verification"  # Exposes world state for checks.
