# Fine-Tuning LLaMA 2: A Comprehensive Guide

This repository demonstrates the end-to-end process of fine-tuning the LLaMA 2 model using **QLoRA** on the **Guanaco dataset**. The fine-tuned model, `Llama-2-7b-chat-finetune`, is designed for enhanced performance on instruction-following tasks.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Steps for Fine-Tuning](#steps-for-fine-tuning)
  - [1. Setup and Installation](#1-setup-and-installation)
  - [2. Fine-Tuning Configuration](#2-fine-tuning-configuration)
  - [3. Training Process](#3-training-process)
  - [4. Deployment and Testing](#4-deployment-and-testing)
- [Model Upload to Hugging Face Hub](#model-upload-to-hugging-face-hub)
- [Installation and Usage](#installation-and-usage)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Overview

This project fine-tunes the **LLaMA 2 (7B)** model using the **QLoRA** technique. It involves:
1. Training on the **Guanaco-1k dataset** for instruction-based tasks.
2. Leveraging 4-bit quantization for efficient training.
3. Deploying the fine-tuned model for interactive text generation.

---

## Features

- Fine-tunes LLaMA 2 with **4-bit precision** for efficiency.
- Utilizes the **QLoRA** technique to reduce resource usage.
- Implements a supervised fine-tuning trainer for streamlined processing.
- Generates human-like text responses with the fine-tuned model.
- Supports easy deployment on Hugging Face Hub.

---

## Steps for Fine-Tuning

### 1. Setup and Installation
Install the required packages:
```bash
!pip install accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7
```
### 2. Fine-Tuning Configuration
- Model: LLaMA 2 (7B chat variant)
- Dataset: Guanaco-1k
- LoRA Parameters:
    - lora_r: 64
    - lora_alpha: 16
    - lora_dropout: 0.1
- Training Parameters:
    - Epochs: 1
    - Batch size: 4
    - Learning rate: 2e-4
### 3. Training Process
- Load the dataset:
```bash
dataset = load_dataset("mlabonne/guanaco-llama2-1k", split="train")
```
- Configure QLoRA:
```bash
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16
)
```
- Initialize the model and tokenizer:
```bash
model = AutoModelForCausalLM.from_pretrained("NousResearch/Llama-2-7b-chat-hf", quantization_config=bnb_config)
tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf")
```
- Train the model using the SFTTrainer.
### 4. Deployment and Testing
Save the fine-tuned model:
```bash
trainer.model.save_pretrained("Llama-2-7b-chat-finetune")
```
Test the model with sample prompts:
```bash
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])
```

## Model Upload to Hugging Face Hub
Push the fine-tuned model and tokenizer to the Hugging Face Hub:
```bash
!huggingface-cli login
model.push_to_hub("tanvir007v/Llama-2-7b-chat-finetune")
tokenizer.push_to_hub("tanvir007v/Llama-2-7b-chat-finetune")
```

## Installation and Usage
### 1. Install Required Libraries:
Save the fine-tuned model:
```bash
pip install transformers accelerate
```
### 2. Load the Fine-Tuned Model:
Save the fine-tuned model:
```bash
from transformers import AutoTokenizer, pipeline
model = "tanvir007v/Llama-2-7b-chat-finetune"
tokenizer = AutoTokenizer.from_pretrained(model)
pipe = pipeline("text-generation", model=model, torch_dtype=torch.float16, device_map="auto")
```
### 3. Run Sample Prompts:
Save the fine-tuned model:
```bash
prompt = "What is a large language model?"
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])
```

## Acknowledgments
- Hugging Face for providing pre-trained models and datasets.
- Meta for LLaMA 2.
- The QLoRA paper for inspiring efficient training methods.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Created with ❤️ by Tanvir Ahmed.
This README file provides a clear and comprehensive guide for using and understanding your fine-tuning application. Replace placeholders (e.g., `tanvir007v`) with actual values and add a LICENSE file to complete the project.
