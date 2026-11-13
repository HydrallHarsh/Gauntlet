"""Shared data models for Gauntlet episodes."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue


class Turn(BaseModel):
    """One user or assistant message in an episode's conversation history."""

    model_config = ConfigDict(extra="forbid", strict=True)

    role: Literal["user", "assistant"]
    content: str


class ToolCall(BaseModel):
    """A tool request and its observed execution state, not a policy verdict.

    ``executed`` means the tool implementation was invoked. Its result and
    world-state evidence determine whether the requested action succeeded.
    """

    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)

    name: str
    args: dict[str, JsonValue]
    status: Literal["requested", "blocked", "executed"]
    result: JsonValue = None


class AgentResponse(BaseModel):
    """One target response, with observed tool calls and adapter-supplied metrics."""

    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)

    text: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    latency_ms: float = Field(ge=0)
    tokens_in: int = Field(ge=0)
    tokens_out: int = Field(ge=0)
