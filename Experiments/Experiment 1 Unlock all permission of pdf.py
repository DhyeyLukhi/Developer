import os
import PyPDF2

def unlock_pdf_permissions(pdf_path):
    """
    Remove all restrictions and permissions from a PDF file
    """
    try:
        # Open the PDF file in read binary mode
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Create PDF writer object
            pdf_writer = PyPDF2.PdfWriter()
            
            # Copy all pages to writer
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            # Remove all encryption and restrictions
            pdf_writer.encrypt('', '') # Empty passwords remove restrictions
            
            # Create output filename
            output_path = pdf_path.rsplit('.', 1)[0] + '_unlocked.pdf'
            
            # Write the unlocked PDF to a new file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
                
        print(f"Successfully unlocked PDF: {pdf_path}")
        return True
        
    except Exception as e:
        print(f"Error unlocking PDF {pdf_path}: {str(e)}")
        return False

def unlock_pdfs_in_folder(folder_path):
    """
    Unlock all PDF files in the specified folder
    """
    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return
    
    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the folder")
        return
    
    success_count = 0
    total_files = len(pdf_files)
    
    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        if unlock_pdf_permissions(pdf_path):
            success_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully unlocked {success_count} out of {total_files} PDF files")

# Example usage
if __name__ == "__main__":
    folder_path = "D:\\Study\\IC\\"  # Replace with your folder path
    unlock_pdfs_in_folder(folder_path)

