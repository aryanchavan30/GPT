import os
import json
# Assuming you have the minbpe library or similar implementation in regex1.py
from regex1 import RegexTokenizer 
import tiktoken




def load_custom_tokenizer(model_path):
    """
    Loads the custom regex.model and regex.vocab files.
    """
    tokenizer = RegexTokenizer()
    # Loading typically expects the prefix without extension if following minbpe patterns
    # or the specific .model file.
    tokenizer.load(model_path) 
    return tokenizer

# Usage
# If your files are 'regex.model' and 'regex.vocab' in the current directory:
tokenizer = load_custom_tokenizer(r"D:\Aryan\Projects\TrainGPT\GPT\tokenizer_base\models\regex.model")

# Test it
# with open(r"D:\Aryan\Projects\TrainGPT\GPT\data\Cleaned_Solar_Data.txt", "r", encoding='utf-8') as file :
#     text = file.read()
text = "<|endoftext|>"
tokens = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

# print(f"Token IDs: {tokens}")

print(tokens)
print(f"Len of token {len(tokens)}")

# print(f"Decoded Text: {tokenizer.decode(tokens)}")