from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

result = generator("Hello, I'm learning about transformers!", max_length=50, num_return_sequences=1)
print(result)
