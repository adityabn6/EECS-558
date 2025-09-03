#!/usr/bin/env python3
"""
PDF Text Extraction Script for EECS 558 Course Materials
"""

import os
import sys

def install_and_import(package):
    """Install and import a package if not available"""
    try:
        __import__(package)
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        __import__(package)

def extract_pdf_text(pdf_path, output_path):
    """Extract text from PDF and save to file"""
    try:
        # Try to install and import PyPDF2
        install_and_import('PyPDF2')
        import PyPDF2
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
                text += "\n"
        
        # Save extracted text
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        
        print(f"Successfully extracted text from {pdf_path}")
        print(f"Text saved to {output_path}")
        return True
        
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {str(e)}")
        return False

def main():
    """Main function to process all PDFs"""
    pdf_files = [
        ("Lecture Notes/Lecture1_August25.pdf", "extracted_text/lecture1_august25.txt"),
        ("Lecture Notes/Lecture2_August27.pdf", "extracted_text/lecture2_august27.txt"),
        ("Preliminary Material/Lecture1.pdf", "extracted_text/prelim_lecture1.txt"),
        ("Preliminary Material/Lecture2.pdf", "extracted_text/prelim_lecture2.txt"),
        ("Preliminary Material/Lecture3.pdf", "extracted_text/prelim_lecture3.txt"),
        ("Preliminary Material/prob-theory2.pdf", "extracted_text/prob_theory2.txt")
    ]
    
    # Create output directory
    os.makedirs("extracted_text", exist_ok=True)
    
    success_count = 0
    for pdf_path, output_path in pdf_files:
        if os.path.exists(pdf_path):
            if extract_pdf_text(pdf_path, output_path):
                success_count += 1
        else:
            print(f"File not found: {pdf_path}")
    
    print(f"\nProcessed {success_count} out of {len(pdf_files)} PDF files successfully.")

if __name__ == "__main__":
    main()