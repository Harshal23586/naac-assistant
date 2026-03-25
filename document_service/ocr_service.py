import PyPDF2
import io
import logging

logger = logging.getLogger(__name__)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts raw text content from PDF binary signatures.
    Essential for AI algorithms analyzing physical uploads.
    """
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += str(extracted) + "\n"  # type: ignore
        return text.strip()  # type: ignore
    except Exception as e:
        logger.error(f"OCR Extraction Failed: {e}")
        return ""
