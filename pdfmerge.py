import os
from PyPDF2 import PdfMerger

def merge_pdfs_with_bookmarks(folder_path, output_file):
    """
    Merges all PDF files in a folder into one PDF, adding bookmarks for each file.

    Args:
        folder_path (str): The path to the folder containing the PDF files.
        output_file (str): The output merged PDF file path.
    """
    # Create a PdfMerger object
    merger = PdfMerger()

    # Get a list of PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    # Sort the files to ensure they are added in order
    pdf_files.sort()

    # Loop through the PDF files and merge them with bookmarks
    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)
        # Add the PDF to the merger with a bookmark
        merger.append(file_path, outline_item=os.path.splitext(pdf_file)[0])

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output_pdf:
        merger.write(output_pdf)

    print(f"Merged PDF saved to: {output_file}")

# Example usage
folder_path = input("Enter the folder path containing PDF files: ").strip()  # Specify folder containing PDFs
output_file = input("Enter the output file path for the merged PDF (include filename and .pdf extension): ").strip()  # Specify output file path

merge_pdfs_with_bookmarks(folder_path, output_file)
