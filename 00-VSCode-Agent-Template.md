# VS Code Custom Agent Template Guide

> **Purpose**: This template helps you create custom agents (`.agent.md` files) for GitHub Copilot and other LLMs in VS Code. Copy the template, modify it for your use case, and save it to `.github/agents/` in your workspace or your user profile.

---

## Quick Reference (From VS Code Documentation)

**Source**: [VS Code Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

### Key Concepts

- **Custom agents** are `.agent.md` files with YAML frontmatter + Markdown instructions
- **Location**: `.github/agents/` folder in workspace OR user profile folder
- **Handoffs**: Enable guided workflows that transition between agents
- **Tools**: Restrict or expand what capabilities the agent has access to

### File Structure Overview

```
---
YAML Frontmatter (configuration)
---
Markdown Body (instructions)
```

---

## 🧩 Agent Template

Copy everything below this line into your `.agent.md` file:

```markdown
---
# ═══════════════════════════════════════════════════════════════
# AGENT CONFIGURATION (YAML Frontmatter)
# ═══════════════════════════════════════════════════════════════

# REQUIRED: Agent identity
name: MyAgent # Display name in agents dropdown
description: Brief description of what this agent does # Placeholder text in chat

# OPTIONAL: User guidance
argument-hint: Describe what input this agent expects # Hint shown in chat input

# OPTIONAL: Model selection (uses current model if not specified)
model: Claude Sonnet 4 # Options: Claude Sonnet 4, GPT-4o, etc.

# OPTIONAL: Agent discovery
infer: true # Allow use as subagent (default: true)
target: vscode # vscode or github-copilot

# ─────────────────────────────────────────────────────────────────
# TOOLS: Define what capabilities this agent has
# ─────────────────────────────────────────────────────────────────
tools:
  # === READ-ONLY / RESEARCH TOOLS ===
  - search # Workspace search
  - usages # Find symbol usages
  - problems # View diagnostics/errors
  - changes # View git changes
  - fetch # Fetch web content
  - githubRepo # Search GitHub repositories
  - testFailure # Get test failure info

  # === CODE EDITING TOOLS ===
  - editFiles # Edit files in workspace
  - createFile # Create new files
  - terminalLastCommand # Access terminal commands

  # === EXECUTION TOOLS ===
  - runSubagent # Launch subagents for complex tasks
  - runInTerminal # Execute terminal commands

  # === EXTENSION TOOLS (prefix with extension ID) ===
  # - github.vscode-pull-request-github/issue_fetch
  # - github.vscode-pull-request-github/activePullRequest

  # === MCP SERVER TOOLS (use server-name/* for all tools) ===
  # - github/github-mcp-server/get_issue
  # - my-mcp-server/*

# ─────────────────────────────────────────────────────────────────
# HANDOFFS: Define transitions to other agents
# ─────────────────────────────────────────────────────────────────
handoffs:
  - label: Next Action Button Text # Button text shown after response
    agent: target-agent-name # Target agent identifier
    prompt: Instructions for next agent # Prompt to send
    send: false # Auto-submit? (default: false)
    showContinueOn: true # Show continue option (optional)


  # Example: Planning → Implementation workflow
  # - label: Start Implementation
  #   agent: agent
  #   prompt: Implement the plan outlined above.
  #   send: false
# ─────────────────────────────────────────────────────────────────
# MCP SERVERS: For github-copilot target only
# ─────────────────────────────────────────────────────────────────
# mcp-servers:
#   - name: my-server
#     config: { ... }
---

# ═══════════════════════════════════════════════════════════════

# AGENT INSTRUCTIONS (Markdown Body)

# ═══════════════════════════════════════════════════════════════

# Agent Role Definition

You are a [ROLE NAME] agent. Your purpose is to [PRIMARY OBJECTIVE].

## Core Responsibilities

- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Behavioral Constraints

<constraints>
- [What the agent MUST do]
- [What the agent MUST NOT do]
- [Boundaries and limitations]
</constraints>

## Workflow

<workflow>
### Step 1: [Phase Name]
[Description of what to do in this phase]

### Step 2: [Phase Name]

[Description of what to do in this phase]

### Step 3: [Phase Name]

[Description of what to do in this phase]
</workflow>

## Output Format

<output_format>
[Describe the expected output structure, templates, or examples]
</output_format>

## Tool Usage Guidelines

Reference tools using `#tool:toolName` syntax in your instructions:

- Use #tool:search to find relevant code
- Use #tool:runSubagent for complex research tasks
- Use #tool:fetch to retrieve external documentation

## Additional Context

[Link to other instruction files using Markdown links]
[Any domain-specific knowledge or guidelines]
```

---

## 📚 Common Agent Patterns

### Pattern 1: Read-Only Research Agent

```yaml
tools: ["search", "usages", "fetch", "githubRepo", "problems"]
```

Use for: Planning, code review, analysis, documentation lookup

### Pattern 2: Full Implementation Agent

```yaml
tools: ["search", "editFiles", "createFile", "runInTerminal", "problems"]
```

Use for: Writing code, refactoring, fixing bugs

### Pattern 3: Orchestrator Agent (Uses Subagents)

```yaml
tools: ["runSubagent", "search", "fetch"]
```

Use for: Complex multi-step tasks that delegate work

### Pattern 4: Testing Agent

```yaml
tools: ["search", "testFailure", "editFiles", "runInTerminal"]
```

Use for: Writing tests, debugging test failures

---

## 🔄 Handoff Workflow Examples

### Linear Workflow: Plan → Implement → Review

```yaml
# In plan.agent.md
handoffs:
  - label: Start Implementation
    agent: implement
    prompt: Implement the plan outlined above.

# In implement.agent.md
handoffs:
  - label: Request Review
    agent: review
    prompt: Review the implementation for quality and security.
```

### Branching Workflow: Analysis → Multiple Options

```yaml
handoffs:
  - label: Fix the Issue
    agent: agent
    prompt: Fix the identified issues.
  - label: Document Findings
    agent: docs
    prompt: Document the analysis findings.
  - label: Create GitHub Issue
    agent: github
    prompt: Create a GitHub issue for tracking.
```

---

## ✅ Agent Design Checklist

Before publishing your agent, verify:

- [ ] **Name** is clear and descriptive (2-4 words)
- [ ] **Description** explains purpose in one sentence
- [ ] **Tools** are minimal and appropriate for the task
- [ ] **Instructions** clearly define the agent's role and constraints
- [ ] **Workflow** is documented step-by-step
- [ ] **Output format** is specified if applicable
- [ ] **Handoffs** connect to logical next steps (if applicable)
- [ ] **Stopping rules** prevent scope creep (if applicable)

---

## 🎯 Best Practices

### 1. Principle of Least Privilege

Only include tools the agent actually needs. A planning agent shouldn't have `editFiles`.

### 2. Clear Role Boundaries

Define what the agent IS and IS NOT responsible for. Use stopping rules to prevent scope creep.

### 3. Structured Output

Provide templates and examples for expected outputs to ensure consistency.

### 4. Iterative Workflows

Use `<workflow>` tags to define clear phases with user checkpoints.

### 5. Subagent Delegation

For complex research tasks, use `#tool:runSubagent` to delegate work autonomously.

### 6. Reusable Instructions

Link to shared instruction files using Markdown links to keep agents DRY.

---

## 📁 Recommended File Structure

```
.github/
└── agents/
    ├── plan.agent.md           # Planning agent
    ├── implement.agent.md      # Implementation agent
    ├── review.agent.md         # Code review agent
    ├── test.agent.md           # Testing agent
    └── docs.agent.md           # Documentation agent
```

---

## 🔗 Resources

- [VS Code Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Custom Instructions Guide](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Reusable Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Tools in Chat](https://code.visualstudio.com/docs/copilot/chat/chat-tools)
- [Awesome Copilot Examples](https://github.com/github/awesome-copilot/tree/main)
