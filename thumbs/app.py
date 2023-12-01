from flask import Flask, request, send_file
import fitz  # PyMuPDF
from PIL import Image


app = Flask(__name__)


@app.route("/generate-preview", methods=["GET"], strict_slashes=False)
def generate_preview():
    """ Generates the preview """
    return """
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="pdf" accept="application/pdf" />
        <input type="submit" />
    </form>
    """


@app.route("/generate-preview", methods=["POST"], strict_slashes=False)
def generate_preview_post():
    """ Generates the preview """
    # Get the uploaded PDF file
    pdf_file = request.files["pdf"]

    # Open the PDF file
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    # Get the page
    page = pdf_document.load_page(0)

    # Define the image matrix to set DPI
    matrix = fitz.Matrix(200 / 72, 200 / 72)

    # Render the page as an image
    pix = page.get_pixmap(matrix=matrix)

    # Convert the PyMuPDF Pixmap to a PIL Image
    pil_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the image to the specified image path
    pil_image.save("preview.png")

    # Close the PDF document
    pdf_document.close()

    return send_file("preview.png", mimetype="image/png", as_attachment=False)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
