---
name: update-handoff
description: Maintain concise agent-to-agent continuation context after implementation changes to code, tests, or project configuration. Read when resuming; skip updates and history pushes for questions, learning, and read-only work.
---

# Update Handoff

Maintain one current `HANDOFF.md` specifically for an agent continuing without chat history. Include only context needed to resume correctly. Explain concepts, designs, and tradeoffs to the user in the conversation as required by the active workflow; do not copy those explanations into the handoff.

## When and where

- When this workflow is enabled, update the handoff before the final response only if the current turn makes implementation changes to project code, tests, or configuration. Explicitly requested changes to project workflow instructions, including this skill or AGENTS.md, count as configuration changes. Record partial implementation honestly when work is unfinished or interrupted.
- Questions, explanations, learning discussions, read-only reviews/checks, planning, and waiting for input do not trigger handoff updates or history commits/pushes when no implementation changes were made. Learning-state edits alone and pre-existing uncommitted changes do not count. Do not change the handoff just to refresh its timestamp or record a question.
- On a fresh session or after losing context, read the applicable project guidance and the handoff before continuing work.
- Use an explicitly configured handoff path. Otherwise use `HANDOFF.md` at the current project/worktree root, or the working directory if there is no repository. Keep different projects and worktrees separate.
- Keep project `AGENTS.md` instructions consistent with this implementation-only trigger; skill selection alone does not require an update. Follow an explicit user request to update or synchronize the handoff even without implementation changes.

## Refresh procedure

1. Read the existing handoff, if present, and reconcile it with the latest instructions and observed files. Current instructions and verified state take precedence.
2. Complete the authorized work, or record the exact pending question and scope waiting on input.
3. Refresh the snapshot, retaining relevant constraints and unresolved tasks. Replace stale status and remove resolved or redundant history. Label proposals, assumptions, confirmed choices, and implemented changes accurately.
4. Check the saved file for accuracy and a concrete continuation point. Report failed writes honestly.
5. If separate history is explicitly configured and authorized, commit and push the updated handoff using that repository, following the section below. Complete this before the final response.

## Gauntlet separate handoff history

The user has authorized committing and pushing each `HANDOFF.md` update to `https://github.com/HydrallHarsh/gauntlet-handoff.git`, branch `main`. Its bare Git metadata is stored at `../config-history.git` relative to the Gauntlet project root; the work tree is the project root itself. Run history commands from that root with explicit `--git-dir` and `--work-tree` arguments. This configuration applies to this project; do not publish another project's handoff without its own authorization.

- Keep `/HANDOFF.md` ignored and untracked in the main repository. The user alone commits in the main repository, including changes to this skill. Never create main-repository commits for this workflow.
- Track only `HANDOFF.md` in the history repository. Do not add this skill, learning notes, or application files there. Use `add -f -- HANDOFF.md` because the shared work tree's `.gitignore` excludes it; never use broad staging commands.
- The user remains the commit author. Include `Co-authored-by: Codex <noreply@openai.com>` as a separate commit-message trailer on each handoff commit, as explicitly requested by the user.
- The bare repository is already initialized. If it is missing, initialize with `git init --bare --initial-branch=main ../config-history.git`, then add the configured origin. Never replace or move the main `.git`, or initialize a second repository in the project root. If existing history or remote configuration differs, inspect it before making changes.
- After saving and reviewing the handoff, stage it, verify that the index contains only `HANDOFF.md`, commit with a concise description of the update, and push:

```powershell
git --git-dir=../config-history.git --work-tree=. add -f -- HANDOFF.md
git --git-dir=../config-history.git --work-tree=. ls-files
git --git-dir=../config-history.git --work-tree=. diff --cached --name-only
git --git-dir=../config-history.git --work-tree=. commit -m "Update handoff: describe current step" -m "Co-authored-by: Codex <noreply@openai.com>"
git --git-dir=../config-history.git --work-tree=. push origin main
```

Run history commands only on a turn that qualifies for a handoff update, or when the user explicitly requests synchronization. Stop on a failed command or unexpected tracked/staged path. On a qualifying turn, if the saved handoff is unchanged, skip the empty commit but push any pending local commits. Verify the local `HEAD` matches the remote `main` after pushing. On push failure, retain the local commit and report the failure and pending push honestly; do not force-push, reset history, or silently declare synchronization complete. Avoid repeated retries without fixing the cause. Retry pending pushes on the next qualifying implementation turn or explicit synchronization request, not during questions or learning-only turns.

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
- Updating the handoff alone does not authorize commits, pushes, deployments, messages, or additional project work. The configured Gauntlet history workflow above has explicit standing authorization only for handoff commits and pushes to its separate repository.
- If multiple agents are already working, reread the shared file before writing and preserve their unrelated current state. Do not spawn agents for this workflow.
- During long implementation work, checkpoint after significant implementation changes when useful. After an abrupt cancellation, reconcile partial edits on the next turn; a final update cannot be guaranteed if execution is forcibly stopped.
- For a turn with no qualifying implementation change, leave HANDOFF.md and its history untouched. Preserve learning state separately under the active learning workflow. Do not invent implementation progress or erase unresolved context.
