# Gauntlet: General Project Overview

*Competitive landscape reflects public sources as of October 2026. This market moves fast, so re-check before you cite anything in a README or interview.*

---

## 1. What Gauntlet is

**Gauntlet is an open-source test-and-harden harness for AI agents that take actions.**

You give it an agent, and it:

1. **Attacks** the agent with a large, varied population of simulated users, some ordinary and some adversarial.
2. **Measures** exactly how the agent fails, using rule-based checks on what actually happened, not opinions.
3. **Defends** by proposing protections, such as hard policy rules before an action runs, output filters, and safer instructions.
4. **Verifies** that those protections work on attacks the defense-builder never saw, and that the agent can still do its normal job.

The result is a report you can trust more than "we tried some jailbreaks and it seemed fine."

**One-line pitch:** *a crash-test lab that crashes your agent, fixes it, and then proves the fix on a sealed final test.*

Gauntlet is **not tied to any one kind of agent**. It works through "scenarios", which are plug-in descriptions of an agent's world: what it can do, what it must never do, what normal tasks look like, and what attacks to try. A customer-support bot is simply the first reference scenario because it is easy to check (did a refund really happen?).

---

## 2. Why this is needed

### 2.1 Agents act, so failures become real events
A chatbot that says something wrong is embarrassing. An agent that sends the wrong email, issues a refund, deletes a file, or runs a command has caused something real. The risk moves from "bad words" to "bad actions."

### 2.2 Testing is mostly manual and shallow
Most teams test by typing a handful of sneaky prompts. That covers a tiny slice of how real people, and real attackers, behave. Results are anecdotes, not measurements, and they don't repeat when the model or prompt changes.

### 2.3 Fixes are unverified guesses
When a team patches one failure, they rarely know:
- whether the fix works on *slightly different* attacks (generalization), or only on the exact test they saw (overfitting);
- whether the fix broke normal behavior, such as an agent so cautious it refuses legitimate requests.

### 2.4 Two different questions get blurred together
"Is the AI gullible?" and "Can damage actually happen?" are different. A hard rule outside the model can block a bad action even when the model is easily fooled. Most reporting mixes these into one number, which hides what each protection really contributes.

### 2.5 Agent attack surface keeps growing
Agents now read emails, web pages, documents, and tool outputs that attackers can influence. Untrusted content hijacking an agent (indirect prompt injection) is widely treated as a leading agent threat. Teams need repeatable testing, not one-off audits.

---

## 3. What you get

| Output | Why it matters |
|---|---|
| **Attack matrix** (damage type × technique) | Shows where the agent is weak and which tricks matter most, with counts |
| **Attempted vs executed rates** | Separates "the model tried" from "it really happened" |
| **Rule-verified results** | Checks use world state, tool calls, and planted markers, so verdicts are yes/no facts |
| **Defense toolkit** | Tool-call policy gates, output filters, input screening, prompt hardening |
| **Honest fix loop** | Proposes fixes, accepts or rejects them with logged reasons |
| **Leak-resistant evaluation** | Practice, validation, and sealed test sets; related attacks stay together |
| **Normal-use score** | Confirms the agent still completes legitimate tasks |
| **Uncertainty reporting** | Counts and confidence intervals so small samples aren't oversold |
| **Ablations** | Shows which defense layer actually did the work |
| **Cost and latency report** | What the protection cost in money and speed |
| **Reusable datasets** | Attack and benign-task sets others can run or extend |

---

## 4. How it works (generic loop)

```
Scenario (agent's world + rules + tasks + seed attacks)
        │
        ▼
Simulated crowd (normal + adversarial, many styles)
        │
        ▼
Run against the agent, each in a fresh isolated world
        │
        ▼
Rule-based judges: attempted? executed? normal task completed?
        │
        ▼
Defender proposes protection → test on validation set → accept / reject
        │
        ▼
Sealed final test, run once → report
```

**Plug-in design:** everything domain-specific lives in the scenario. The harness, judges' structure, splits, defense loop, statistics, and reporting are reusable.

**Easy onboarding (planned):** a copy-paste prompt that a user gives their own coding agent. It reads their repo and drafts the scenario files, which the user reviews. A validation command then checks the generated checkers against known-good and known-bad examples before anything is trusted.

---

## 5. Core ideas in plain terms

- **Outcome vs technique.** *Outcome* is what went wrong (unauthorized action, secret leaked). *Technique* is how it was induced (impersonation, roleplay, hidden instructions in a document). Separating them gives a matrix instead of a flat list.
- **Attempted vs executed.** *Attempted*: the model tried. *Executed*: it really happened after any protections. A good defense stack drives "executed" down even if the model stays gullible.
- **Practice, check, final exam.** Defenders learn from the practice set, fixes are accepted on the validation set, and the finished defense is scored once on a sealed test set. Rewordings of the same attack always stay in one set.
- **Novel-technique test.** One technique is held out entirely, to see whether defenses handle a new kind of attack.
- **Normal use counts.** Ordinary tasks are scored too, verified by rules. A defense that blocks real users is a failed defense.
- **Capabilities.** Some agents expose their tool calls and let you block them, some are black boxes. Gauntlet states what it can and cannot measure for each, instead of faking it.

---

## 6. Use cases

| Use case | What you do with Gauntlet |
|---|---|
| **Pre-release safety gate** | Run before shipping an agent; fail the release if executed attack rate or normal-use score crosses a threshold |
| **Regression testing** | Re-run the same suite when the model, prompt, or tools change, to see whether robustness got better or worse |
| **Evaluating a defense** | Test a guardrail, policy layer, or prompt change and see its real effect on both attacks and usability |
| **Comparing models or frameworks** | Same scenario, different models, a fair robustness and utility comparison |
| **Building a domain benchmark** | Create a scenario for your own domain (finance ops, HR, DevOps) and publish the dataset |
| **Evidence for reviews and audits** | Reproducible results with methodology, rather than "we red-teamed it" |
| **Teaching and research** | A small, readable reference for studying agent security and evaluation methodology |
| **Portfolio and hiring signal** | Demonstrates evaluation rigor, systems design, and safety thinking in one repo |

### Example scenarios (beyond customer support)

| Agent type | Sample outcomes to test |
|---|---|
| **Email or calendar assistant** | Sends sensitive data to an outsider after reading a malicious email; deletes or forwards without approval |
| **Coding agent with shell access** | Runs a destructive command or leaks secrets after reading a poisoned file or README |
| **Finance or operations agent** | Initiates a transfer or order outside limits after social engineering |
| **IT helpdesk or HR agent** | Resets credentials for the wrong person; reveals another employee's data |
| **Research or browsing agent** | Follows instructions hidden in a web page and exfiltrates context |
| **DevOps agent** | Changes cloud permissions or deploys on an unauthorized request |

Email and coding agents are especially strong second scenarios because indirect injection is natural there.

---

## 7. Who it is for

- **Agent developers** who want a measurable pre-launch check.
- **Small teams without a security group** who need something repeatable and affordable.
- **Security and red-team practitioners** who want structured coverage with evidence.
- **Researchers and students** studying attack and defense methodology.
- **You**, as a portfolio piece that shows depth beyond "I built another agent."

---

## 8. Competitive landscape

The space is **active and crowded**. Know it well before you claim anything.

### 8.1 Open-source red-team scanners
| Tool | What it does | Notes |
|---|---|---|
| **garak** (NVIDIA) | Command-line vulnerability scanner with a very large probe library, including encoding and obfuscation attacks | Broad coverage; dense output; CI polish is weaker than some alternatives |
| **PyRIT** (Microsoft) | Toolkit for building custom, adaptive, multi-turn and multimodal attack campaigns | Powerful but more of a toolkit for security teams; needs an attacker model |
| **Promptfoo** | CLI for evaluation plus red teaming, strong CI/CD workflow, plugins including tool misuse and injection | Reported acquired by OpenAI in March 2026, with a commitment to keep the core open source |
| **DeepTeam** | Open-source red teaming mapped to OWASP LLM categories | Framework-style, standards-oriented |
| **Giskard** | Testing framework for LLM apps | Testing and quality focus |

### 8.2 Agent security research and benchmarks
| Tool | What it does | Notes |
|---|---|---|
| **AgentDojo** (ETH Zurich, NeurIPS 2024) | Extensible environment for evaluating prompt-injection attacks and defenses on tool-using agents, with stateful simulated worlds (workspace, Slack, travel, banking), utility measured with and without attack | **Closest overlap with Gauntlet.** Focused on indirect injection and on evaluating existing defenses and attacks |

### 8.3 Runtime guardrails and firewalls
Lakera Guard (reported acquired by Check Point), LLM Guard, NeMo Guardrails, LlamaFirewall, and several smaller open-source middleware projects that enforce tool-call policy outside the model. These *are* defenses, deployed in production. They don't test themselves.

### 8.4 Commercial agent-security platforms
Prompt Security, Pillar Security (acquired by Zscaler), Cisco AI Defense, Mindgard, Akto, Highflame, HiddenLayer, Protect AI and others. Several advertise automated agent red teaming plus guardrails configured from findings, so **the idea of "close the loop between testing and enforcement" is already being sold commercially.**

### 8.5 Evaluation and observability platforms
Braintrust, Galileo (including an "eval-to-guardrail" lifecycle and an open-source agent control plane), Arize Phoenix. They focus on quality, monitoring, and turning evaluators into runtime checks.

### 8.6 Where Gauntlet sits (qualitative, from public docs I could find)

| Capability | Scanners | AgentDojo | Runtime guardrails | Commercial platforms | **Gauntlet** |
|---|---|---|---|---|---|
| Broad attack library | Strong | Narrow (injection) | n/a | Strong | Narrow by design |
| Stateful tool-using world with rule-checked outcomes | Limited | Strong | n/a | Varies | Core (planned) |
| Utility measured alongside security | Limited | Yes | Varies | Varies | Core (planned) |
| Proposes and tests defenses automatically | No | Evaluates existing defenses | They are the defense | Partial | Core (planned) |
| Held-out validation to prevent overfitting defenses | Not a focus | Not a focus | n/a | Unclear | Core (planned) |
| Attempted vs executed reporting | Unclear | Unclear | n/a | Unclear | Core (planned) |
| Bring-your-own-agent onboarding | Endpoint-based | Add environments in code | n/a | Yes | Scenario builder (planned) |
| Open, small, readable, hackable | Yes | Yes | Varies | No | Yes |

"Unclear" means I could not confirm it from public material. Verify before making comparative claims.

---

## 9. Honest positioning

**What is not new**
- Automated red teaming of agents is an established category.
- "Close the loop from testing to guardrails" is already marketed by commercial vendors.
- Measuring utility under attack in stateful agent environments is already done by AgentDojo.

**What can still be distinctive (the defensible claim)**
1. **Methodological care around the defense step:** lineage-grouped splits, a validation gate for accepting fixes, a sealed test run once, and a held-out technique, so reported improvements are less likely to be overfitting.
2. **Attempted vs executed** as a first-class metric pair, which shows what each layer contributes.
3. **Rule-verified utility** next to security, so "safe but useless" shows up in the numbers.
4. **Scenario builder:** a coding-agent-driven onboarding path with validation of the generated checkers.
5. **Open, small, and understandable**, which makes it useful for learning and for extending.

**Where it is weaker**
- Attack breadth versus garak, Promptfoo, or commercial platforms.
- No multimodal attacks, no production monitoring, no enterprise features.
- Solo-maintained, with one reference scenario at first.
- Generated scenarios are only as good as human review of the policies.

**Recommended stance: build on, don't compete.**
- Import attack ideas or probes from existing tools as seed sources.
- Sanity-check your harness on an AgentDojo-style task so your numbers can be compared with published ones.
- Describe Gauntlet as *"a small, open, methodologically careful harness for the attack → defend → verify loop on tool-using agents."* Avoid "first," "only," or "complete."

---

## 10. Limitations and non-goals

- **Not proof of safety.** It measures resistance to the attacks it contains. Unknown attacks may still work.
- **Not a general benchmark.** Results are specific to the scenario and its policies.
- **Judges can be wrong.** Rule checks are strong but only as good as the scenario definition. LLM judges, if added, are noisy and reported separately.
- **Not a substitute for human security review or runtime monitoring.**
- **Authorized use only.** Run it against agents you own or have permission to test.

---

## 11. Roadmap

| Stage | Contents |
|---|---|
| **Core** | Scenario interface, reference scenario, rule-based judges, attack library, lineage splits, baseline report |
| **Swarm** | Personas, mutations, adaptive attacker loop, benign tasks with checkers |
| **Defender** | Guarded target, tool gate, output filter, prompt patch, validation-gated fix loop, ablations |
| **Sealed test** | One-shot final evaluation, novel-technique slice, final report |
| **Onboarding** | Scenario-builder prompt, `validate-scenario` command, black-box HTTP adapter |
| **Generality proof** | A second scenario with a different shape (for example an email assistant) |
| **Later** | Failure clustering, dashboard, LLM-judged outcomes with a calibration set, trace export |

---

## 12. Glossary

| Term | Meaning |
|---|---|
| **Agent** | An AI that can take actions through tools, not just chat |
| **Scenario** | A plug-in description of an agent's world, rules, tasks, and attacks |
| **Outcome** | The damage that results |
| **Technique** | The method used to cause it |
| **Persona** | A simulated user with a goal and style |
| **Oracle** | A rule-based checker that decides yes/no whether something bad happened |
| **ASR** | Attack success rate |
| **Attempted / executed** | The model tried / it actually happened |
| **Tool gate** | A hard rule that blocks an action before it runs |
| **Lineage** | A family of attacks that are rewordings of one original |
| **Train / validation / test** | Practice / fix-acceptance / sealed final exam |
| **Indirect injection** | Malicious instructions hidden in content the agent reads (emails, pages, tool output) |
| **Over-refusal** | The agent blocking legitimate requests out of excess caution |

---

## 13. Sources used for the landscape section

- appsecsanta.com: LLM red teaming tools overview, Promptfoo alternatives, and AI security tools comparisons (2026)
- braintrust.dev: Best LLM red teaming tools for production in 2026
- qawerk.com: LLM red teaming tools compared
- NeurIPS 2024 Datasets and Benchmarks: AgentDojo paper (Debenedetti et al.)
- guptadeepak.com: agent security red teaming vendor roundup
- prompt.security: announcement of automated AI red teaming (January 2026)
- akto.io and galileo.ai vendor pages and blog posts on agent guardrails and governance (2026)

Vendor pages are marketing material. Treat them as evidence of what is being claimed, not independent verification.
