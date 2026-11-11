"""Shared data models for Gauntlet episodes."""

from typing import Literal

from pydantic import BaseModel, ConfigDict


class Turn(BaseModel):
    """One user or assistant message in an episode's conversation history."""

    model_config = ConfigDict(extra="forbid", strict=True)

    role: Literal["user", "assistant"]
    content: str
