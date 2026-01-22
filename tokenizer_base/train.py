"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from regex1 import RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open(r"D:\Aryan\Projects\TrainGPT\GPT\data\New_Solar_Report_cleaned.txt", "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
for TokenizerClass, name in zip([ RegexTokenizer], ["regex"]):

    # construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    tokenizer.train(text, 1024*2, verbose=True)
    special_tokens = {"<|endoftext|>": 2048}
    tokenizer.register_special_tokens(special_tokens)
    # writes two files in the models directory: name.model, and name.vocab
    prefix = os.path.join("models", name)
    tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")