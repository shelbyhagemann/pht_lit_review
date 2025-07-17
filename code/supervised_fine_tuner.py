## Going to use this document to apply supervised fine-tuning to model
## Referenses:
# https://docs.unsloth.ai/basics/tutorials-how-to-fine-tune-and-run-llms/tutorial-how-to-finetune-llama-3-and-use-in-ollama

## Import libraries
from unsloth import FastLanguageModel
import torch

## Define global variables
MAX_SEQ_LENGTH = 2048
dtype = None # None means auto detection (not sure what this means, following tutorial)
load_in_4bit = True # Use 4bit quant to reduce memory usage --> prob good for now

## Defining the model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "PUT MODEL NAME HERE",
    dtype = dtype,
    load_in_4bit = load_in_4bit
)

## Functions

## Main function