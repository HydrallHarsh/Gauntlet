---
name: update-handoff
description: Maintain concise agent-to-agent continuation context. Read the handoff when resuming and update it before ending every user-prompt turn when enabled, including questions, reviews, and unfinished work.
---

# Update Handoff

Maintain one current `HANDOFF.md` specifically for an agent continuing without chat history. Include only context needed to resume correctly. Explain concepts, designs, and tradeoffs to the user in the conversation as required by the active workflow; do not copy those explanations into the handoff.

## When and where

- When this workflow is enabled by the user or project instructions, update the handoff after every user prompt, immediately before the final response. Include turns that only answer questions or wait for input.
- On a fresh session or after losing context, read the applicable project guidance and the handoff before continuing work.
- Use an explicitly configured handoff path. Otherwise use `HANDOFF.md` at the current project/worktree root, or the working directory if there is no repository. Keep different projects and worktrees separate.
- Use project `AGENTS.md` instructions to require this workflow every turn; skill selection alone is not an unconditional trigger.

## Refresh procedure

1. Read the existing handoff, if present, and reconcile it with the latest instructions and observed files. Current instructions and verified state take precedence.
2. Complete the authorized work, or record the exact pending question and scope waiting on input.
3. Refresh the snapshot, retaining relevant constraints and unresolved tasks. Replace stale status and remove resolved or redundant history. Label proposals, assumptions, confirmed choices, and implemented changes accurately.
4. Check the saved file for accuracy and a concrete continuation point. Report failed writes honestly.

## Context to preserve

Use short bullets under a few relevant headings; omit empty sections.

- **Goal and status:** timestamp with timezone, current objective, latest steering, and request/project completion state.
- **Constraints and decisions:** continuing user requirements, confirmed choices, and relevant authorization boundaries. Add at most a brief reason when it prevents a concrete continuation mistake. For learning mode, record active mode, pending checkpoint, and pointers to learning-state files; leave lesson details there.
- **Current state:** relevant entry points, changed files, partial/uncommitted work, and verified versus proposed components. Include environment, branch, running sessions, and temporary artifacts only when needed to resume.
- **Verification:** checks actually run and their results; distinguish failures and untested work. Include exact commands when needed to reproduce a failure or resume a check, otherwise a concise result and relevant path suffice.
- **Open work and next step:** unresolved tasks, blockers, exact pending input, and the next concrete file or decision to revisit. Label suggestions as proposals.

Prefer pointers to existing project docs, decision records, and learning notes over duplicating their content. Do not perform broad discovery merely to populate the handoff.

## Continuity rules

- Apply a relevance test: would omitting this fact make the next agent lose necessary context, repeat work, violate a constraint, or take the wrong next step? If not, omit it.
- Keep the file a compact current snapshot. Exclude detailed reasoning, tutorials, exhaustive tradeoff discussions, transcripts, long logs, and routine tool narration. There is no fixed word cap if necessary continuation context requires more space.
- Do not store credentials, tokens, private keys, or sensitive payloads. Record configuration names and retrieval locations instead.
- Updating the handoff does not authorize commits, deployments, messages, or additional project work.
- If multiple agents are already working, reread the shared file before writing and preserve their unrelated current state. Do not spawn agents for this workflow.
- During long work, checkpoint after significant decisions or changes when useful. After an abrupt cancellation, reconcile partial edits on the next turn; a final update cannot be guaranteed if execution is forcibly stopped.
- For a prompt with no material project change, record that fact and retain the active work. Do not invent progress or erase unresolved context.
