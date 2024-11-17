import PyPDF2
from certifi import contents


class TEXT_EXTRAXTER():
    def __init__(self, pdf_file: str):
                                    #  read as bytes
        with open(file=pdf_file, mode="rb") as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)

            # print(reader)

            self.pdf_text = []

            # print(reader.pages)

            for page in reader.pages:
                # print(page)
                content = page.extract_text()
                # print(content)
                self.pdf_text.append(content)



