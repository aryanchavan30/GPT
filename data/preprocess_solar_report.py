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
    # text = re.sub(r'###\s+', '', text)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"[OK] Cleaned text saved to: {output_path}")
    print(f"[OK] File size: {len(text)} characters")

if __name__ == "__main__":
    input_file = r"F:\LLM Projects\SebastianRaschka\GPTV1\data\Solar Report 24-25.txt"
    output_file = r"F:\LLM Projects\SebastianRaschka\GPTV1\data\Solar_Report_cleaned.txt"

    clean_text_for_pretraining(input_file, output_file)
