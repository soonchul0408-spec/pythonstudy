from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
text = "The future of AI is"
print(text)
inputs = tokenizer(text, return_tensors="pt")
print(inputs)
outputs = model(**inputs)
print(outputs.logits.shape)
next_token_logits =outputs.logits[:, -1, :]
print(next_token_logits.shape)
