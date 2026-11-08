# Project Instructions

## Handoff after every prompt

Read and follow `skills/update-handoff/SKILL.md` for every user-prompt turn in this project, including questions, reviews, and turns waiting for input. On a fresh session or after context loss, read `HANDOFF.md` before continuing.

After completing the turn's work, update the root `HANDOFF.md` before the final response. Keep it concise and specifically for agent-to-agent continuation: current goal, relevant constraints, confirmed decisions, files changed, verification status, unfinished work, and next steps. Include a brief reason only when it affects continuation. Detailed explanations and teaching belong in the conversation. If work is waiting or interrupted, record that state honestly. The handoff is context; current instructions and verified files take precedence.

## Learning as we build

The user invoked `vibe-wise:learn` and wants to understand Gauntlet's concepts, patterns, design choices, and tradeoffs as they arise during development. Explain these in the conversation by default when relevant to the current work; avoid an upfront course or an unsolicited long lesson.

For meaningful Gauntlet design choices, invite the user's reasoning and follow the active VibeWise learning workflow. Distinguish proposals from confirmed choices and implementation. Preserve learning state in `.vibe-wise/`; the handoff needs only the active mode, any pending checkpoint, and pointers to those files. Do not invent experience levels or demonstrated understanding.
