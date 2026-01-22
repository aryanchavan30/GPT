
# pip install pdfminer.six
from pdfminer.high_level import extract_text

def pdf_to_txt_pdfminer(input_pdf_path: str, output_txt_path: str):
    text = extract_text(input_pdf_path)  # You can set laparams for layout tweaks
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(text or "")
    print(f"Saved text to: {output_txt_path}")

# Usage
pdf_to_txt_pdfminer(r"C:\Users\ac12860\Downloads\Shruti_Kawale_Resume.9011286361.pdf", "Shruti_Kawale_Resume.txt")
