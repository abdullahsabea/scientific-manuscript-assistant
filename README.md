# Universal Scientific Manuscript Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Domain-STEM-blue" alt="STEM">
  <img src="https://img.shields.io/badge/Format-LaTeX-green" alt="LaTeX">
  <img src="https://img.shields.io/badge/Tool-AI%20Assistant-orange" alt="AI Agent">
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License">
</div>

<br>

An AI agent **skill** tailored for PhD researchers and academic authors across **all STEM disciplines** (Engineering, Physics, Biology, Computer Science, Chemistry, etc.).

This skill provides a set of rigorous system instructions that constrain an AI assistant (like Copilot, Gemini, or ChatGPT) to act as a highly professional scientific drafting and review tool, enforcing strict guardrails against fabricated science, plagiarism, and unethical AI use.

---

## 🎯 Purpose

This skill helps researchers draft, refine, and check LaTeX manuscripts for top-tier journal submission (e.g., Nature group, Elsevier, Springer, Wiley). It acts as a constrained assistant that focuses purely on **language polishing, structural flow, and logical consistency checks**. 

**Key features include:**
- 🛡️ **Anti-Fabrication Guarantee:** Explicit instructions to never invent data, results, or fake citations.
- 🔬 **Universal Scientific Checks:** Evaluates parameters, mathematical consistency, and logical deductions based on your stated STEM field.
- ⚙️ **Automated Verification:** Includes local Python scripts for universally checking Crossref for retractions, validating LaTeX syntax, and preventing self-plagiarism.
- ✍️ **Human-centric Writing:** Actively discourages generic "AI tone" (e.g., overuse of "Moreover", "Significantly") and adapts to your unique writing voice.
- 📝 **LaTeX Preservation:** Maintains all LaTeX formatting, citations (`\cite`), labels (`\label`), and equations without breaking compilation.
- 🛑 **Ethical AI Disclosure:** Built-in configs for specific journals (Elsevier, Nature) for adherence to target journal AI-disclosure policies.

## ⚙️ Automated Workflows & Domain Extensions
This repository includes a `scripts/` directory with automated tools that your AI assistant can execute locally while reviewing your paper:

**Universal Tools:**
- `check_retractions.py`: Queries the Crossref API against your `.bib` file to flag potentially retracted or updated references.
- `latex_validator.py`: A local checker that ensures your LaTeX environments and braces are perfectly balanced.
- `self_plagiarism_check.py`: Compares your new draft against a directory of your past papers to prevent excessive boilerplate reuse.

**Domain Extensions:**
Because this assistant is universal, it supports "Domain Extensions"—custom scripts tailored for specific fields.
- `am_calculator.py` *(Included)*: A specific calculator for **Additive Manufacturing** that verifies Volumetric Energy Density (VED) and Basquin equation consistency.
*Are you in a different field? Feel free to add your own Python calculators to the `scripts/` folder so the AI can verify your specific domain equations!*

## 🚀 How to Use

To use this skill, download or clone this repository and add it to your agent's custom skills or rules directory. When interacting with the AI agent, you can invoke the skill to set its context.

**1. Provide your Context**
Tell the agent what section you are working on, your specific domain, and the target journal.
> *"I want to polish the Abstract and Introduction of my biology paper for Nature. Please use the universal-scientific-manuscript-assistant skill."*

**2. Follow the Structured Output**
The assistant is instructed to always respond with:
1. **Section Summary:** A brief summary of the section and proposed improvements.
2. **Issue Checklist:** Any scientific, logical, or formatting concerns flagged for your review.
3. **Revised Text (LaTeX):** The refined, LaTeX-friendly text.
4. **Author Actions:** A short list of manual verification steps you must complete.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
