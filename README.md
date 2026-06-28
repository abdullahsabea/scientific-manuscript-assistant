# Scientific Manuscript Assistant for Additive Manufacturing and Computational Mechanics

<div align="center">
  <img src="https://img.shields.io/badge/Domain-Mechanical%20Engineering-blue" alt="Mechanical Engineering">
  <img src="https://img.shields.io/badge/Domain-Additive%20Manufacturing-orange" alt="Additive Manufacturing">
  <img src="https://img.shields.io/badge/Format-LaTeX-green" alt="LaTeX">
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License">
</div>

<br>

An AI agent **skill** tailored for PhD researchers and academic authors in the fields of mechanical engineering, additive manufacturing (LPBF/SLM), computational mechanics, fatigue analysis, and TPMS lattice structures. 

This skill provides a set of rigorous system instructions that constrain an AI assistant (like Copilot, Gemini, or ChatGPT) to act as a highly professional scientific drafting and review tool, enforcing strict guardrails against fabricated science, plagiarism, and unethical AI use.

---

## 🎯 Purpose

This skill helps researchers draft, refine, and check LaTeX manuscripts for top-tier journal submission (e.g., Nature group, Elsevier, Springer, Wiley). It acts as a constrained assistant that focuses purely on **language polishing, structural flow, and logical consistency checks**. 

**Key features include:**
- 🛡️ **Anti-Fabrication Guarantee:** Explicit instructions to never invent data, results, or fake citations.
- 🔬 **Scientific Plausibility Checks:** Evaluates process parameters, structural mechanics, and fatigue claims for conceptual consistency.
- ⚙️ **Automated Verification:** Includes local Python scripts for calculating Volumetric Energy Density (VED), checking Crossref for retractions, and validating LaTeX syntax.
- ✍️ **Human-centric Writing:** Actively discourages generic "AI tone" (e.g., overuse of "Moreover", "Significantly") and adapts to your unique writing voice.
- 📝 **LaTeX Preservation:** Maintains all LaTeX formatting, citations (`\cite`), labels (`\label`), and equations without breaking compilation.
- 🛑 **Ethical AI Disclosure:** Built-in configs for specific journals (Elsevier, Nature) for adherence to target journal AI-disclosure policies.

## ⚙️ Automated Workflows
This repository includes a `scripts/` directory with automated tools that your AI assistant can execute locally:
- `am_calculator.py`: Verifies Volumetric Energy Density (VED) and Basquin equation consistency based on your manuscript's stated values.
- `check_retractions.py`: Queries the Crossref API against your `.bib` file to flag potentially retracted or updated references.
- `latex_validator.py`: A local checker that ensures your LaTeX environments and braces are perfectly balanced.
- `self_plagiarism_check.py`: Compares your new draft against a directory of your past papers to prevent excessive boilerplate reuse.

## 🚀 How to Use

To use this skill, download or clone this repository and add it to your agent's custom skills or rules directory. When interacting with the AI agent, you can invoke the skill to set its context.

**1. Provide your Context**
Tell the agent what section you are working on and the target journal.
> *"I want to polish the Abstract and Introduction of my paper for Additive Manufacturing. Please use the scientific-manuscript-assistant skill."*

**2. Follow the Structured Output**
The assistant is instructed to always respond with:
1. **Section Summary:** A brief summary of the section and proposed improvements.
2. **Issue Checklist:** Any scientific, logical, or formatting concerns flagged for your review.
3. **Revised Text (LaTeX):** The refined, LaTeX-friendly text.
4. **Author Actions:** A short list of manual verification steps you must complete.

## 📖 Example Interactions

### Example 1: Polishing an Abstract
**You:** *"I need to polish the abstract of my paper on TPMS lattice fatigue. Target journal: Materials & Design. I only want language polishing."*  
**Assistant:** Will ask for the text, perform a quick analysis, and return a clean, concise, human-sounding abstract without altering any of your claims or numbers.

### Example 2: Checking Consistency in a TPMS Fatigue Section
**You:** *"Here is the Discussion section for my fatigue study on gyroid lattices. Please do a scientific check and refine the flow."*  
**Assistant:** Will scan your text to ensure that your claims about relative density, stress concentrations, and S-N curve trends align with standard physical principles. If you claim that higher porosity increased fatigue life without a clear geometrical explanation, the assistant will flag it as an issue for your review.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
