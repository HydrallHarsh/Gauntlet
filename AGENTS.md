# Project Instructions

## Handoff after implementation changes

Read and follow `skills/update-handoff/SKILL.md` when maintaining continuation context in this project. On a fresh session or after context loss, read `HANDOFF.md` before continuing.

Update the root `HANDOFF.md`, then commit and push its separate history, only when the current turn makes implementation changes to project code, tests, or configuration, including explicitly requested workflow-instruction changes. Questions, explanations, learning discussions, read-only reviews/checks, planning, and waiting for input leave the handoff and its history untouched when no implementation changes were made. Learning-state edits alone and pre-existing uncommitted files do not trigger an update. An explicit user request to update or synchronize the handoff also applies.

On qualifying turns, keep the handoff concise and specifically for agent-to-agent continuation: current goal, relevant constraints, confirmed decisions, files changed, verification status, unfinished work, and next steps. Include a brief reason only when it affects continuation. Detailed explanations and teaching belong in the conversation. Record unfinished or interrupted implementation honestly. The handoff is context; current instructions and verified files take precedence.

## Learning as we build

The user invoked `vibe-wise:learn` and wants to understand Gauntlet's concepts, patterns, design choices, and tradeoffs as they arise during development. Explain these in the conversation by default when relevant to the current work; avoid an upfront course or an unsolicited long lesson.

For meaningful Gauntlet design choices, invite the user's reasoning and follow the active VibeWise learning workflow. Distinguish proposals from confirmed choices and implementation. Preserve learning state in `.vibe-wise/`; the handoff needs only the active mode, any pending checkpoint, and pointers to those files. Do not invent experience levels or demonstrated understanding.
