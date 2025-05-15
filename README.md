# Code-Watchdog
Detecting model that can be used in computer based coding-test.
Detects AI generated code and keystroke anomaly detection(copy&paste, or using LLM..).

## Dataset
- [Typing Behaivor Dataset](https://cvlab.cse.msu.edu/typing-behavior-dataset.html)
- [IKDD: A Keystroke Dynamics Dataset for User Classification](https://www.mdpi.com/2078-2489/15/9/511)
- [AIGCodeSet]()

## Process

### Trainig

| Sub-task                        | Model type                           | Objective                                                                                                     | Loss / Metric                            |
| ------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Code origin detection**       | *Supervised* MLP (or any classifier) | Predict whether a code snippet was written by a human (`HUMAN`) or an LLM name (`Gemini`, `Llama`, …) | Binary-cross-entropy (BCE); AUC          |
| **Keystroke anomaly detection** | *Unsupervised* Auto-Encoder          | Reproduce normal keystroke feature vectors; high reconstruction error ⇒ anomaly                               | Mean-squared-error (MSE); AUROC over MSE |


### Real-time Application
- Implemented in web, React-wasm
- Real time keystroke-ai gen code detection

