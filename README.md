# Code-Watchdog
Detecting model that can be used in computer based coding-test.
Detects AI generated code and keystroke anomaly detection(copy&paste, or using LLM..)
## Process

### Trainig

| Sub-task                        | Model type                           | Objective                                                                                                     | Loss / Metric                            |
| ------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Code origin detection**       | *Supervised* MLP (or any classifier) | Predict whether a code snippet was written by a human (`HUMAN`) or an LLM name (`Gemini`, `Llama`, …) | Binary-cross-entropy (BCE); AUC          |
| **Keystroke anomaly detection** | *Unsupervised* Auto-Encoder          | Reproduce normal keystroke feature vectors; high reconstruction error ⇒ anomaly                               | Mean-squared-error (MSE); AUROC over MSE |


### Real-time Application
- Implemented in web, React-wasm
- Real time keystroke-ai gen code detection

