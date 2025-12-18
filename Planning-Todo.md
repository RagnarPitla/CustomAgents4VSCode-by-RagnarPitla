# VSCode Agents Repository - Planning & Action Items

> **Created:** December 18, 2025  
> **Status:** Planning Phase  
> **Reference:** Claude Code Subagents Repository Structure

---

## 📋 Executive Summary

This document outlines the plan to build a comprehensive **VSCode Agents** repository, inspired by the Claude Code Subagents architecture but adapted for the VS Code ecosystem using GitHub Copilot Chat Agents.

### Key Differences: Claude Code vs VSCode Agents

| Aspect      | Claude Code Subagents          | VSCode Agents                 |
| ----------- | ------------------------------ | ----------------------------- |
| Platform    | Claude Code CLI                | VS Code + GitHub Copilot      |
| File Format | Markdown with YAML frontmatter | `.agent.md` files             |
| Storage     | `.claude/agents/`              | `.github/` or workspace root  |
| Invocation  | Natural language + `/agents`   | `@agent-name` mentions        |
| Tool Access | Built-in Claude tools          | Copilot Chat Participants API |

---

## 🎯 Action Items & Todo List

### Phase 1: Foundation (Priority: HIGH)

- [ ] **1.1** Define the standard VSCode Agent template structure
- [ ] **1.2** Create a comprehensive README.md for the repository
- [ ] **1.3** Set up folder structure for agent categories
- [ ] **1.4** Create CONTRIBUTING.md guidelines
- [ ] **1.5** Define naming conventions for agents

### Phase 2: Core Agent Development (Priority: HIGH)

- [ ] **2.1** Build core development agents (frontend, backend, fullstack)
- [ ] **2.2** Build language-specific agents (TypeScript, Python, etc.)
- [ ] **2.3** Build quality & security agents (code-reviewer, debugger)
- [ ] **2.4** Build documentation agents

### Phase 3: Advanced Agents (Priority: MEDIUM)

- [ ] **3.1** Build infrastructure agents (DevOps, cloud)
- [ ] **3.2** Build data & AI agents
- [ ] **3.3** Build specialized domain agents
- [ ] **3.4** Build business & product agents

### Phase 4: Orchestration & Meta (Priority: MEDIUM)

- [ ] **4.1** Build multi-agent coordination system
- [ ] **4.2** Create workflow orchestration agents
- [ ] **4.3** Define inter-agent communication protocols

### Phase 5: Documentation & Community (Priority: LOW)

- [ ] **5.1** Create usage examples for each agent
- [ ] **5.2** Build a searchable catalog/index
- [ ] **5.3** Set up community contribution workflow
- [ ] **5.4** Create video tutorials/demos

---

## 📁 Proposed Repository Structure

```
CustomAgents4VSCode-by-RagnarPitla/
├── README.md                          # Main documentation
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── 00-VSCode-Agent-Template.md        # Base template (existing)
├── Planning-Todo.md                   # This file
│
├── 01-Core-Development/
│   ├── api-designer.agent.md
│   ├── backend-developer.agent.md
│   ├── frontend-developer.agent.md
│   ├── fullstack-developer.agent.md
│   ├── mobile-developer.agent.md
│   └── ui-designer.agent.md
│
├── 02-Language-Specialists/
│   ├── typescript-pro.agent.md
│   ├── python-pro.agent.md
│   ├── javascript-pro.agent.md
│   ├── react-specialist.agent.md
│   ├── nextjs-developer.agent.md
│   ├── golang-pro.agent.md
│   ├── rust-engineer.agent.md
│   └── csharp-developer.agent.md
│
├── 03-Infrastructure/
│   ├── azure-infra-engineer.agent.md
│   ├── cloud-architect.agent.md
│   ├── devops-engineer.agent.md
│   ├── kubernetes-specialist.agent.md
│   ├── terraform-engineer.agent.md
│   └── database-administrator.agent.md
│
├── 04-Quality-Security/
│   ├── code-reviewer.agent.md
│   ├── debugger.agent.md
│   ├── security-auditor.agent.md
│   ├── qa-expert.agent.md
│   ├── performance-engineer.agent.md
│   └── accessibility-tester.agent.md
│
├── 05-Data-AI/
│   ├── ai-engineer.agent.md
│   ├── data-scientist.agent.md
│   ├── ml-engineer.agent.md
│   ├── prompt-engineer.agent.md
│   └── llm-architect.agent.md
│
├── 06-Developer-Experience/
│   ├── documentation-engineer.agent.md
│   ├── refactoring-specialist.agent.md
│   ├── git-workflow-manager.agent.md
│   ├── cli-developer.agent.md
│   └── legacy-modernizer.agent.md
│
├── 07-Specialized-Domains/
│   ├── blockchain-developer.agent.md
│   ├── game-developer.agent.md
│   ├── iot-engineer.agent.md
│   └── fintech-engineer.agent.md
│
├── 08-Business-Product/
│   ├── product-manager.agent.md
│   ├── technical-writer.agent.md
│   ├── business-analyst.agent.md
│   └── ux-researcher.agent.md
│
├── 09-Meta-Orchestration/
│   ├── agent-organizer.agent.md
│   ├── workflow-orchestrator.agent.md
│   └── multi-agent-coordinator.agent.md
│
├── 10-Research-Analysis/
│   ├── research-analyst.agent.md
│   ├── competitive-analyst.agent.md
│   └── trend-analyst.agent.md
│
└── Knowledge-Resources/               # Existing folder
    ├── ClaudeCode_instructions-BaseTemplate.md
    └── linkedinframework.md
```

---

## 🏗️ VSCode Agent Template Structure

Based on the existing template, here's the recommended structure:

```markdown
---
name: "agent-name"
description: "One-line description of when to invoke this agent"
category: "Core Development | Language | Infrastructure | etc."
tools: ["semantic_search", "read_file", "grep_search", "run_in_terminal"]
version: "1.0.0"
---

# Agent Name

## Role & Expertise

[Description of the agent's role and areas of expertise]

## When to Use This Agent

- Scenario 1
- Scenario 2
- Scenario 3

## Core Capabilities

1. Capability 1
2. Capability 2
3. Capability 3

## Workflow & Process

### Phase 1: [Name]

- Step 1
- Step 2

### Phase 2: [Name]

- Step 1
- Step 2

## Best Practices

- Practice 1
- Practice 2

## Communication Protocol

[How this agent communicates and collaborates]

## Example Prompts

- "Help me with X"
- "Review my Y"
```

---

## 🚀 Priority Agents to Build First

### Tier 1 - Essential (Build First)

| Agent                    | Description                 | Impact |
| ------------------------ | --------------------------- | ------ |
| `code-reviewer`          | Automated code review       | High   |
| `debugger`               | Error analysis & resolution | High   |
| `documentation-engineer` | Auto-generate docs          | High   |
| `refactoring-specialist` | Code modernization          | High   |
| `typescript-pro`         | TypeScript expertise        | High   |

### Tier 2 - High Value (Build Second)

| Agent                 | Description            | Impact      |
| --------------------- | ---------------------- | ----------- |
| `api-designer`        | API architecture       | Medium-High |
| `fullstack-developer` | End-to-end development | Medium-High |
| `devops-engineer`     | CI/CD automation       | Medium-High |
| `security-auditor`    | Security scanning      | Medium-High |
| `prompt-engineer`     | AI prompt optimization | Medium-High |

### Tier 3 - Specialized (Build Later)

| Agent                   | Description              | Impact |
| ----------------------- | ------------------------ | ------ |
| `azure-infra-engineer`  | Azure specialist         | Medium |
| `ai-engineer`           | AI/ML systems            | Medium |
| `workflow-orchestrator` | Multi-agent coordination | Medium |

---

## 📝 Key Decisions to Make

### 1. Tool Permissions Strategy

**Question:** How do we handle tool permissions in VSCode Agents?

**Options:**

- A) Define recommended tools in the agent file (documentation only)
- B) Create VS Code extension that enforces tool permissions
- C) Trust Copilot to use appropriate tools based on context

**Recommendation:** Option A for now, with Option B as future enhancement

### 2. Agent Invocation Method

**Question:** How should users invoke specific agents?

**Options:**

- A) Use `@agent-name` syntax in Copilot Chat
- B) Use slash commands `/use agent-name`
- C) Natural language detection

**Recommendation:** Option A - aligns with Copilot Chat participant pattern

### 3. Agent Customization

**Question:** Should users be able to customize agents?

**Options:**

- A) Fork and modify agent files
- B) Create extension layer for customizations
- C) Environment variables/settings

**Recommendation:** Option A for simplicity

---

## 📊 Success Metrics

| Metric                     | Target | Timeline |
| -------------------------- | ------ | -------- |
| Number of agents created   | 20+    | Q1 2026  |
| GitHub stars               | 100+   | Q2 2026  |
| Community contributors     | 5+     | Q2 2026  |
| Documentation completeness | 100%   | Q1 2026  |

---

## 🔗 Resources & References

- [Claude Code Subagents Repo](https://github.com/VoltAgent/awesome-claude-code-subagents) - Inspiration source
- [VS Code Chat Extensions](https://code.visualstudio.com/api/extension-guides/chat) - Official API docs
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- Existing template: [00-VSCode-Agent-Template.md](00-VSCode-Agent-Template.md)

---

## 📅 Timeline

| Phase                    | Duration | Target Completion |
| ------------------------ | -------- | ----------------- |
| Phase 1: Foundation      | 1 week   | Dec 25, 2025      |
| Phase 2: Core Agents     | 2 weeks  | Jan 8, 2026       |
| Phase 3: Advanced Agents | 3 weeks  | Jan 29, 2026      |
| Phase 4: Orchestration   | 2 weeks  | Feb 12, 2026      |
| Phase 5: Documentation   | Ongoing  | Continuous        |

---

## 📌 Next Steps (Immediate Actions)

1. ✅ Create Planning-Todo.md (this file)
2. [ ] Review and finalize the template in `00-VSCode-Agent-Template.md`
3. [ ] Create the folder structure for categories
4. [ ] Build the first agent: `code-reviewer.agent.md`
5. [ ] Create comprehensive README.md for the repository
6. [ ] Set up GitHub repository settings (topics, description, etc.)

---

_Last Updated: December 18, 2025_
