# S.H.I.E.L.D. - Secure Helper for Intelligent Education and Learning Developments

This repository contains various scripts and data which we used in our paper to evaluate the S.H.I.E.L.D. architecture. Below is a breakdown of the directory structure and key files.

## Directory Structure

### **assessment specs/**
This folder contains various assessment specifications from the course _Software Engineering Fundamentals_ at the University of New South Wales, including:
- **lab01_academics.md, lab01_leap.md, ... lab08_snapnews.md**: Different lab assignments and specifications.
- **project.md**: Project-specific specifications.

### **scripts/**
This folder contains scripts related to vector store creation and evaluation:
- **create_vector_store.py**: Creates a ChromaDB instance from the assessment specs. (Note: A vector store already exists in _utils/vs_.)
- **eval_baseline.py**: Baseline evaluation script.
- **eval_courseassist.py**: Reproduced and used to evaluate the CourseAssist architecture (not completely compatible with S.H.I.E.L.D.).
- **eval_shield.py**: Evaluates the S.H.I.E.L.D. architecture.

### **testing data/**
- **test.json**: Contains testing data used in our evaluations.

### **utils/**
Helper functions and utilities:
- **vs/**: Subdirectory for vector store utilities.
- **call_gpts.py**: Script to call GPT models.
- **io_functions.py**: Handles input and output operations.
- **vector_store_functions.py**: Functions related to vector store management.

## Evaluation Process
The evaluation scripts generate JSON output files for manual review. These results should be stored in the `evaluations` folder.

## Notes
- OpenAI API keys are **not provided** in this repository. Ensure that your environment is configured with the necessary credentials before running any script that requires GPT-based models. For access to the fine-tuned intent classifier model in _eval_shield.py_ please email z5604369@ad.unsw.edu.au, or alternatively gpt-4o-mini can be used as a substitute.
- The outputs we got in our evaluation along with other details can be found here: https://sites.google.com/view/shield-tutor/home
