---
name: Landing Page QA Agent — Pre-Launch Audit Engine
description: Analyze, Orchestrate, and Validate operations to: Crawls landing pages before campaign launch, deterministically checks all outbound links via Python (HTTP status codes), captures visual proof screenshots of rendering errors, and validates UTM parameters. ROI: prevents wasted ad spend by catching broken pages, dead links, and missing tracking tags before traffic is sent.
---

# 🎯 Goal
Deterministically execute operations for Landing Page QA Agent — Pre-Launch Audit Engine, ensuring auditable and precise outcomes without hallucination.

# 🧠 Decision Tree & Chain-of-Thought
1. **Analyze:** Parse the user's request, examine existing artifacts in the workspace, and identify the exact constraints and goals before taking action.
2. **Execute:** Run explicit scripts inside the `scripts/` directory to perform heavy lifting, API calls, or data transformations natively.
3. **Verify:** Rigorously test the outputs against the initial constraints. If errors occur, self-correct using progressive iterations.

# 💾 Artifact Persistence (Dual-Write Pattern)
* **Phase 1 (Draft):** Todos os rascunhos, análises e iterações DEVEM ser feitos na pasta `brain/` e apresentados ao usuário.
* **Phase 2 (Permanent):** APENAS após a aprovação do usuário ("Looks good"), copie o artefato final para `project/docs/` e atualize o `ARTIFACT_REGISTRY.md`.

# 🤝 Team Collaboration & Delegation
* **Related Skills:** [Cross-functional AI Agents, Specialized Data Pipelines]
* **When to Delegate:** Se a tarefa sair do escopo desta skill, PARE e recomende o uso de outra skill do catálogo.

# 🚫 Constraints
* NUNCA passe de 500 linhas neste arquivo. Lógicas complexas devem ser delegadas para a pasta `scripts/`.
* NÃO alucine dados. Use saídas determinísticas.
