## Refs:
# Info on auto-classes: https://huggingface.co/docs/transformers/en/model_doc/auto
# Info on Tokenizer: https://huggingface.co/docs/transformers/en/main_classes/tokenizer
# Info on training: https://huggingface.co/docs/trl/en/sft_trainer
# Info on GGUF: https://huggingface.co/docs/transformers/en/gguf

## Import libraries
import langchain
import transformers
import peft
import trl
from langchain_community.llms import Ollama
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from peft import PeftModel


## Define global variables
training_dataset = load_dataset("jsonl", example_file = "examples.jsonl")

## Defining the model
#llm = Ollama(model="llama2", temperature=0.5)
model_name = "meta-llama/Llama-2-7b-chat-hf"

## Set up tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,
    device_map="auto"
)



## Functions

# name: tokenize_examples
# input: jsonl example file
# return: 
# description: use huggingface datasets library for support here
def tokenize_examples(examples):
    input_texts = []

    # put examples in a good format for tokenizing
    for example in examples:
        paperID = example ["paperID"]
        question = example["question"]
        answer = example["answer"]
        reasoning = example["reasoning"]
        input_text = f"###PaperID:\n{paperID}\n\n###Instruction:\n{question}\n\n### Response:\n{answer}\n\n### Reasoning:\n{reasoning}"
        input_texts.append(input_text)

    # tokenize the data
    tokenized_data = tokenizer(input_texts, truncation=True, padding="max_length", max_length=512, return_tensors="pt")

    # return tokenized data
    return tokenized_data

# name: train_model
# input: 
# return: 
# description: use huggingface train functionality
def train_model(tokenized_data):
    # Set up training args
    training_args = SFTConfig(output_dir="/model_files")

    ## Set up trainer
    trainer = SFTTrainer(
        model,
        args = training_args,
        train_dataset=tokenized_data["train"],
        tokenizer=tokenizer
    )

    trainer.train()

# name: save_model
# input: 
# return: 
# description: use huggingface save_pretrained functionality
def save_model():
    model.save_pretrained("sft-output")
    tokenizer.save_pretrained("sft-output")


# name: tailor_ollama
# input: 
# return: 
# description: use huggingface save_pretrained functionality
def tailor_ollama():
    # merge base and tuned models
    base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    lora_model = PeftModel.from_pretrained(base_model, "sft-output")
    lora_model = lora_model.merge_and_unload()
    lora_model.save_pretrained("merged-model")

    # convert to GGUF format for Ollama


## main function
def main():
    pass

if __name__ == "__main__":
    main()