# ref: https://ollama.readthedocs.io/en/modelfile/#format
FROM llama2
# sets the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1
# sets the context window size to 4096, this controls how many tokens the LLM can use as context to generate the next token
PARAMETER num_ctx 4096

# sets a custom system message to specify the behavior of the chat assistant
SYSTEM You are a human-centered computer science specialist, assisting with a literature review.