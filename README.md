# Reprompt_Arc


# Reprompting Software: Code Optimization with LLMs + Structured Evaluation

This project is a **Reprompting Software** that takes an initial user prompt, generates code using a Language Model (LLM), evaluates the code's performance, and then automatically **refines the prompt** to generate **better, more optimized code** over multiple iterations. It uses **Qwen-Coder 2.5B** for generation and evaluates the code using metrics like **cyclomatic complexity, code quality, redundancy, runtime, and memory usage**.

After optimization, we apply **SCOT (Structured Chain of Thought)** to enhance the code’s readability, structure, and reasoning—before comparing the **initial and final outputs**.

---

## Features

- 🔁 Multi-step **Reprompting loop** (3 iterations)
- 🤖 Code generation using **Qwen-Coder 2.5B**
- 📊 Evaluation of:
  - Cyclomatic complexity
  - Code quality (lint, formatting)
  - Redundancy and structure
  - Syntax validity
  - Runtime performance
  - Memory profiling + **Time vs Memory Graph**
- **SCOT (Structured Chain of Thought)** post-processing
- Final Comparison: Initial vs Final Code (Performance + Memory)


## Architecture Overview


    A[Initial Prompt by User] --> B[Code Generation via Qwen-Coder];
    B --> C[Save Code to File];
    C --> D[Code Evaluation];
    D --> E[Metrics: Complexity, Quality, Redundancy, Syntax, Runtime, Memory];
    E --> F[Plot Time vs Memory Graph];
    F --> G{User wants Optimized Code?};
    G -->|Yes| H[Generate Refined Prompt using Evaluation Data];
    H --> I[New Code via LLM];
    I --> D;
    G -->|No or Max Iterations| J[SCOT Refinement];
    J --> K[Final Code Evaluation];
    K --> L[Compare Initial vs Final Results];



    
    
Installation
Requirements
Python 3.9+
Ollama 

