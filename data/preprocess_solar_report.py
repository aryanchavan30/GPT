import re

def clean_text_for_pretraining(input_path, output_path):
    """Clean a single text file for LLM pretraining."""

    with open(input_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove email/URL markdown links but keep the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Normalize multiple blank lines to double newlines
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)

    # Remove excessive whitespace but preserve paragraph structure
    text = re.sub(r' +', ' ', text)

    # Optional: Remove markdown headers ### if you want plain text
    # Uncomment the line below if you want to remove ### symbols
    text = re.sub(r'###\s+', '', text)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"[OK] Cleaned text saved to: {output_path}")
    print(f"[OK] File size: {len(text)} characters")

if __name__ == "__main__":
    input_file = r"D:\Aryan\Projects\TrainGPT\GPT\data\Cleaned_Solar_Data.txt"
    output_file = r"D:\Aryan\Projects\TrainGPT\GPT\data\New_Solar_Report_cleaned.txt"

    clean_text_for_pretraining(input_file, output_file)
# import re

# def clean_llm_pretraining_data(text):
#     # 1. Remove Source ID Tags (e.g., )
#     text = re.sub(r'\\', '', text)
    
#     # 2. Remove HTML span page markers
#     text = re.sub(r'<span id="page-\d+-\d+"></span>', '', text)
    
#     # 3. Handle Currency Artifacts (Converting J/H to Rs. or ₹)
#     text = re.sub(r'\b[JH]\s?(\d)', r'Rs. \1', text)
    
#     # 4. Remove Recurring Document Headers/Footers
#     boilerplate = [
#         r"Solar Industries India Limited Annual Report 2024-25",
#         r"### \d+-\d+", # Section ranges like 02-78
#         r"\d+ Solar Industries India Limited Annual Report 2024-25 \d+" # Page number lines
#     ]
#     for pattern in boilerplate:
#         text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
#     # 5. Clean Table Syntax
#     # Remove table dividers like |---|---|
#     text = re.sub(r'\|[\-\s|]+\|', '\n', text)
#     # Replace remaining pipes with spaces to preserve word boundaries
#     text = text.replace('|', ' ')
    
#     # 6. Normalize Whitespace and Line Breaks
#     # Join sentences split by single newlines (lowercase continuation)
#     text = re.sub(r'([a-z,])\n([a-z])', r'\1 \2', text)
#     # Replace 3+ newlines with 2 (paragraph separation)
#     text = re.sub(r'\n{3,}', '\n\n', text)
#     # Collapse multiple spaces
#     text = re.sub(r' +', ' ', text)
    
#     return text.strip()

# # Example usage
# with open('Solar Report 24-25.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     cleaned_content = clean_llm_pretraining_data(content)
#     with open('Cleaned_Solar_Data.txt', 'w', encoding='utf-8') as f_out:
#         f_out.write(cleaned_content)


# import json

# def merge_json_text_to_file(json_data, output_filename):
#     """
#     Reads a list of JSON objects and merges 'data' from entries 
#     with type 'text' into a single .txt file.
#     """
#     with open(output_filename, 'w', encoding='utf-8') as txt_file:
#         for entry in json_data:
#             # Check if the entry type is 'text'
#             if entry.get("type") == "text":
#                 text_content = entry.get("data", "")
                
#                 # Write the content to the file
#                 txt_file.write(text_content)
                
#                 # Ensure it ends with a newline for separation
#                 if not text_content.endswith('\n'):
#                     txt_file.write('\n')
                
#                 # Add an extra newline for block separation if desired
#                 txt_file.write('\n')
# import json
# # Example implementation
# if __name__ == "__main__":
#     # Your provided data sample
#     with open(file=r"C:\Users\SD12631\Downloads\Chunked JSON Data new 1.json", mode = "r", encoding="utf-8") as f:
#         data = json.load(f)

#     # Process and save to file
#     merge_json_text_to_file(data, "Solar_Report_Pretraining.txt")
#     print("Text extraction complete. Saved to 'Solar_Report_Pretraining.txt'.")