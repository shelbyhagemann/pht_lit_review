## References:
# https://python.langchain.com/docs/tutorials/rag/
# https://python.langchain.com/api_reference/langchain/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html
# https://python.langchain.com/docs/concepts/vectorstores/
# https://python.langchain.com/api_reference/ollama/llms/langchain_ollama.llms.OllamaLLM.html
# https://python.langchain.com/api_reference/huggingface/embeddings/langchain_huggingface.embeddings.huggingface.HuggingFaceEmbeddings.html
# used gpt for debugging and suggestions

## BEFORE RUNNING: Have ollama installed locally, run "ollama serve" in another terminal

## import libraries and modules
import pymupdf
import langchain
from langchain_community.document_loaders import PyMuPDFLoader
import pymupdf4llm
import pathlib
from langchain.text_splitter import MarkdownTextSplitter
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.chains import LLMChain
from langchain.llms.base import LLM
from typing import Optional, List, Mapping
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import subprocess
import json
from typing import TypedDict
from langchain_core.vectorstores import InMemoryVectorStore
import langchain_community.vectorstores
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from typing_extensions import List, TypedDict
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

## declare classes
class OllamaLLM(LLM):
    model: str = "llama2"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print("Ollama subprocess failed")
            print("Exit Code:", e.returncode)
            print("Stdout:", e.stdout[:300])  # Truncated
            print("Stderr:", e.stderr[:300])  # Truncated
            raise RuntimeError(f"Ollama call failed: {e.stderr}")

    @property
    def _identifying_params(self) -> Mapping[str, any]:
        return {"model": self.model}

    @property
    def _llm_type(self) -> str:
        return "ollama"

## declare global variables
# metrics list
# note: adding rest later, want to run on smaller scale for proof-of-concept
pht_framework = [
    "Please rate on a scale of 1 to 5: is the game fun-first (1) or utility-first (5)?",
    "Please rate on a scale of 1 to 5: Is the design play-first(1) or game-first (5)?",
    "Please rate on a scale of 1 to 5: Is the game social (1) or solo (5)?",
    "Please rate on a scale of 1 to 5: Is the game sequential (1) or simultaneous (5)?", 
    "Please rate on a scale of 1 to 5: Is the game competitive (1) or collaborative (5)?",
    "Please rate on a scale of 1 to 5: Is the game symmetrical (1) or assymetrical (5)?"
]

# set up llm
llm = OllamaLLM(model="llama2")
# ref for model: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

### functions ###

# name: load_pdf
# input: file path
# return: markdown object
# description: loads in pdf, converts to markdown
def load_pdf(file_path):
    ## convert file to markdown format so it can be chunked
    markdown_text = pymupdf4llm.to_markdown(file_path)
    ## write to a file using UTF-8 encoding
    pathlib.Path("output.md").write_bytes(markdown_text.encode())
    chunked_data = chunk_data(markdown_text)
    return chunked_data

# name: chunk_data
# input: markdown text
# return: chunked data of type TYPE
# description: chunks text for further processing
def chunk_data(text):
    split_text = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    chunked_doc = split_text.create_documents([text])
    return chunked_doc

# name: create_vec
# input: chunked_data
# return: vector_store
# description: places chunked data into a vector store
def create_vec(chunked_data):
    vector_store = InMemoryVectorStore(embedding=embedding_model)
    vector_store.add_documents(documents=chunked_data)
    return vector_store

# name: prompt
# input: vector_store
# return: list of annotations
# description: prompts the model to apply annotations
def prompt(vector_store):
    # list of annotations
    annotations = []
    # for each metric
    for metric in pht_framework:
        # retrieve context using vector_store
        context = retrieve(vector_store, metric)

        # full prompt
        full_prompt = """Use the following pieces of context to answer the question at the end.
        Answer as if you are a human-centered computer science researcher.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Use three sentences maximum and keep the answer as concise as possible.

        {context}

        Question: {metric}

        Answer:"""

        # generate response using llm
        response = generate(context, metric, full_prompt)
        annotations.append(response)
    return annotations


# name: retrieve
# input: vector_store, metric
# return: context
# description: uses metric and vector_store to gather context for prompting
def retrieve(vector_store, metric):
    retrieved_context = vector_store.similarity_search(metric)
    return retrieved_context

# name: generate
# input: context, metric
# return: annotation
# description: uses context and metric to apply annotation
def generate(context, metric, full_prompt):
    docs_content = "\n\n".join(doc.page_content for doc in context)
    prompt_text = full_prompt.format(context = docs_content, metric = metric)
    response = llm(prompt_text)
    return {"answer": response}

# name: generate_json
# input: annotation_list
# return: json output
# description: creates json file based on annotations
def generate_json(annotation_list, output_path="annotations.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(annotation_list, f, indent=2, ensure_ascii=False)

## main function
def main():
    # load file path (will set up to iterate over list of file paths later)
    file_path = "digitalplay.pdf"
    # break data into chunks
    chunked_data = load_pdf(file_path)
    # store chunks in vector
    vector_store = create_vec(chunked_data)
    # apply annotations to paper
    annotations = prompt(vector_store)
    # generate json file containing annotations for that specific paper
    generate_json(annotations)
    print("Complete.")

if __name__ == "__main__":
    main()