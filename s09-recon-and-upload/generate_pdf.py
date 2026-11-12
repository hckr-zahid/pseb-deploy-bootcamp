import os
import sys
import win32com.client

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCX_PATH = os.path.join(BASE_DIR, "S09_Recon_and_Upload_Report.docx")
PDF_PATH = os.path.join(BASE_DIR, "S09_Recon_and_Upload_Report.pdf")

def convert_to_pdf():
    if not os.path.exists(DOCX_PATH):
        print(f"Error: {DOCX_PATH} does not exist.")
        sys.exit(1)
        
    print(f"Converting {DOCX_PATH} to {PDF_PATH} via Microsoft Word COM...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(DOCX_PATH)
        doc.SaveAs(PDF_PATH, FileFormat=17) # 17 = wdFormatPDF
        doc.Close()
        print(f"Successfully generated PDF at: {PDF_PATH}")
    except Exception as e:
        print(f"Error during PDF conversion: {e}")
        sys.exit(1)
    finally:
        word.Quit()

if __name__ == "__main__":
    convert_to_pdf()
