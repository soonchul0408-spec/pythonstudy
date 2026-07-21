from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("bert-base-uncased")
sentence = "Transformers are amazing!"
ids = tok(sentence)["input_ids"]
print(tok.convert_ids_to_tokens(ids))

