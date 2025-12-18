# 🚀 Agent Setup Guide

> **Learn how to add and use custom agents in VS Code with GitHub Copilot**

This guide will walk you through everything you need to know to start using the custom agents from this repository in your VS Code environment.

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Understanding Custom Agents](#-understanding-custom-agents)
3. [Installation Methods](#-installation-methods)
4. [Using Agents](#-using-agents)
5. [Troubleshooting](#-troubleshooting)
6. [Next Steps](#-next-steps)

---

## ✅ Prerequisites

Before you can use custom agents, ensure you have:

- **VS Code** installed (version 1.90 or later recommended)
- **GitHub Copilot** extension installed and activated
- **GitHub Copilot Chat** extension installed
- An active **GitHub Copilot subscription** (Individual, Business, or Enterprise)

### Verify Your Setup

1. Open VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type "GitHub Copilot: Chat" and verify the extension is active
4. Check the status bar for the Copilot icon (should be active, not crossed out)

---

## 🧠 Understanding Custom Agents

### What Are Custom Agents?

Custom agents are specialized AI assistants that you can create for GitHub Copilot. They are defined in `.agent.md` files that contain:

- **YAML Frontmatter**: Configuration (name, description, tools, handoffs)
- **Markdown Instructions**: Detailed instructions on how the agent should behave

### Agent File Structure

```markdown
---
name: AgentName
description: What the agent does
---

# Agent Instructions

Your detailed instructions here...
```

### Where Agents Live

Agents can be stored in two locations:

1. **Workspace Level**: `.github/agents/` folder in your project

   - Available only in that specific workspace
   - Great for project-specific agents

2. **User Profile Level**: Your VS Code user folder
   - Available across all workspaces
   - Perfect for agents you use frequently

---

## 📦 Installation Methods

### Method 1: Workspace Installation (Recommended for Project-Specific Agents)

**Use this method when**: You want agents available only in a specific project.

1. **Clone or download this repository**

   ```bash
   git clone https://github.com/RagnarPitla/CustomAgents4VSCode-by-RagnarPitla.git
   ```

2. **Navigate to your project directory**

   ```bash
   cd /path/to/your/project
   ```

3. **Create the agents folder if it doesn't exist**

   ```bash
   mkdir -p .github/agents
   ```

4. **Copy the agent files you want**

   ```bash
   # Example: Copy the frontend developer agent
   cp /path/to/CustomAgents4VSCode-by-RagnarPitla/01-Core-Development/frontend-developer.agent.md .github/agents/

   # Or copy multiple agents
   cp /path/to/CustomAgents4VSCode-by-RagnarPitla/01-Core-Development/*.agent.md .github/agents/
   ```

5. **Reload VS Code**
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
   - Type "Developer: Reload Window"
   - Press Enter

### Method 2: User Profile Installation (Recommended for Global Access)

**Use this method when**: You want agents available in all your workspaces.

#### macOS/Linux

1. **Navigate to your VS Code user folder**

   ```bash
   cd ~/.config/Code/User/
   ```

2. **Create the agents folder**

   ```bash
   mkdir -p .github/agents
   ```

3. **Copy the agents you want**
   ```bash
   cp /path/to/CustomAgents4VSCode-by-RagnarPitla/01-Core-Development/*.agent.md .github/agents/
   ```

#### Windows

1. **Navigate to your VS Code user folder**

   ```cmd
   cd %APPDATA%\Code\User\
   ```

2. **Create the agents folder**

   ```cmd
   mkdir .github\agents
   ```

3. **Copy the agents you want**

   ```cmd
   copy C:\path\to\CustomAgents4VSCode-by-RagnarPitla\01-Core-Development\*.agent.md .github\agents\
   ```

4. **Reload VS Code** (same as Method 1, step 5)

### Method 3: Manual File Creation

**Use this method when**: You want to customize an agent before adding it.

1. **Open VS Code in your project or user folder**

2. **Create the folder structure**

   - In your workspace: `.github/agents/`
   - Or in user profile (see paths above)

3. **Create a new file**

   - File → New File
   - Save it with `.agent.md` extension (e.g., `my-agent.agent.md`)

4. **Copy content from this repository**

   - Browse to the agent you want in this repo
   - Copy the entire content
   - Paste into your new file

5. **Customize as needed** (optional)

   - Modify the name, description, or instructions
   - Save the file

6. **Reload VS Code**

---

## 🎯 Using Agents

### Accessing Agents

1. **Open GitHub Copilot Chat**

   - Press `Cmd+I` (Mac) or `Ctrl+I` (Windows/Linux)
   - Or click the Copilot Chat icon in the sidebar

2. **Type `@` to see available agents**

   - A dropdown will appear showing all available agents
   - Custom agents will appear alongside built-in agents

3. **Select an agent**
   - Click on the agent or type its name
   - Example: `@frontend-developer`

### Chatting with Agents

Once an agent is selected:

```
@frontend-developer Create a responsive navigation component with dark mode support
```

The agent will:

- Follow its specialized instructions
- Use only the tools it has access to
- Provide responses tailored to its expertise

### Agent Handoffs

Some agents can hand off to other agents:

```
User: @code-reviewer Review my React component
Code Reviewer: [Finds issues]
Code Reviewer: @frontend-developer Can you fix these issues?
Frontend Developer: [Implements fixes]
```

This creates powerful workflows where agents collaborate!

---

## 🔧 Troubleshooting

### Agent Not Appearing in Dropdown

**Problem**: You copied an agent file but don't see it in the `@` menu.

**Solutions**:

1. ✅ Verify the file has `.agent.md` extension (not `.md`)
2. ✅ Check the file is in the correct location (`.github/agents/`)
3. ✅ Reload VS Code window (`Cmd/Ctrl+Shift+P` → "Reload Window")
4. ✅ Verify the YAML frontmatter is valid (no syntax errors)

### Agent Not Working as Expected

**Problem**: The agent is visible but doesn't behave correctly.

**Solutions**:

1. ✅ Check the agent file for syntax errors
2. ✅ Verify the YAML frontmatter is properly formatted
3. ✅ Ensure there's a `---` separator between YAML and Markdown
4. ✅ Check VS Code Developer Console for errors:
   - `Cmd/Ctrl+Shift+P` → "Developer: Toggle Developer Tools"
   - Look at the Console tab

### Agent Can't Access Certain Tools

**Problem**: Agent says it can't perform a specific action.

**Solutions**:

1. ✅ Check the agent's `tools` configuration in YAML frontmatter
2. ✅ Verify the required tools are included/excluded appropriately
3. ✅ Some tools require specific VS Code extensions to be installed

### Multiple Agents with Same Name

**Problem**: You have conflicts between workspace and user-level agents.

**Solutions**:

1. ✅ Rename one of the agents to make them unique
2. ✅ Workspace agents take precedence over user-level agents
3. ✅ Use unique names to avoid confusion

---

## 📚 Next Steps

### Explore Agent Categories

Now that you know how to install agents, explore what's available:

- **[01-Core-Development](01-Core-Development/)**: Full-stack, frontend, backend, mobile developers
- **[02-Language-Specialists](02-Language-Specialists/)**: Python, JavaScript, TypeScript, Rust, Go experts
- **[03-Infrastructure](03-Infrastructure/)**: DevOps, Kubernetes, Terraform, database specialists
- **[04-Quality-Security](04-Quality-Security/)**: Code reviewers, security auditors, QA experts
- **[05-Data-AI](05-Data-AI/)**: ML engineers, data scientists, AI architects
- **[06-Developer-Experience](06-Developer-Experience/)**: Documentation, refactoring, legacy modernization
- **[07-Specialized-Domains](07-Specialized-Domains/)**: Blockchain, gaming, IoT, fintech
- **[08-Business-Product](08-Business-Product/)**: Product managers, business analysts, UX researchers
- **[09-Meta-Orchestration](09-Meta-Orchestration/)**: Multi-agent coordinators
- **[10-Research-Analysis](10-Research-Analysis/)**: Trend analysts, competitive research
- **[11-D365-FnO-SCM](11-D365-FnO-SCM/)**: Dynamics 365 Finance & Operations specialists

### Create Your Own Agents

Want to build custom agents? Check out these resources:

- **[00-VSCode-Agent-Template.md](00-VSCode-Agent-Template.md)**: Base template for creating agents
- **[01-VSCode-Agentbuilder-Guide.agent.md](01-VSCode-Agentbuilder-Guide.agent.md)**: Comprehensive guide to building agents
- **[Official VS Code Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)**: Microsoft's official guide

### Contribute

Found a bug or want to improve an agent?

- Check out [CONTRIBUTING.md](CONTRIBUTING.md)
- Submit issues or pull requests
- Share your custom agents with the community!

---

## 🎓 Quick Tips

### Best Practices

1. **Start Small**: Install 2-3 agents first, get comfortable, then add more
2. **Workspace vs User**: Use workspace for project-specific, user-level for general-purpose
3. **Name Clearly**: Use descriptive names so you remember what each agent does
4. **Experiment**: Try different agents to find your favorites
5. **Combine Agents**: Use agent handoffs to create powerful workflows

### Common Use Cases

- `@frontend-developer` - Building UI components
- `@backend-developer` - Creating APIs and server logic
- `@code-reviewer` - Getting code reviews and suggestions
- `@debugger` - Troubleshooting issues
- `@documentation-engineer` - Writing docs and comments
- `@refactoring-specialist` - Improving existing code
- `@security-auditor` - Finding security vulnerabilities

---

## 📞 Need Help?

- **Issues**: [GitHub Issues](https://github.com/RagnarPitla/CustomAgents4VSCode-by-RagnarPitla/issues)
- **Discussions**: [GitHub Discussions](https://github.com/RagnarPitla/CustomAgents4VSCode-by-RagnarPitla/discussions)
- **VS Code Docs**: [Custom Agents Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## 📄 Additional Resources

- [Planning & Roadmap](Planning-Todo.md) - See what's coming next
- [Agent Template](00-VSCode-Agent-Template.md) - Base template for creating agents
- [Agent Builder Guide](01-VSCode-Agentbuilder-Guide.agent.md) - Comprehensive building guide
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute

---

**Happy agent building! 🚀**
