import fitz  # PyMuPDF
from PIL import Image

def generate_pdf_preview(pdf_path, page_number, image_path, dpi=200):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Get the page
    page = pdf_document.load_page(page_number - 1)

    # Define the image matrix to set DPI
    matrix = fitz.Matrix(dpi / 72, dpi / 72)

    # Render the page as an image
    pix = page.get_pixmap(matrix=matrix)

    # Convert the PyMuPDF Pixmap to a PIL Image
    pil_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the image to the specified image path
    pil_image.save(image_path)

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    pdf_path = "1984.pdf"  # Replace with the path to your PDF file
    page_number = 1  # Replace with the page number you want to generate a preview for
    image_path = "1984_preview.png"  # Replace with the desired image file path

    generate_pdf_preview(pdf_path, page_number, image_path)
