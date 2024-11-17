import PyPDF2


class TEXT_EXTRAXTER():
    def __init__(self, pdf_file: str):
                                    #  read as bytes
        with open(file=pdf_file, mode="rb") as pdf:
            reader = PyPDF2.PdfReader(pdf, strict=False)

            # print(reader)

            self.pdf_text_as_list = []
            self.pdf_text_as_str = []

            # print(reader.pages)

            for page in reader.pages:
                # print(page)
                content = page.extract_text()
                # print(content)
                self.pdf_text_as_list.append(content)
                # self.pdf_text_as_str.append(f"\n{ content }")

            # for page in self.pdf_text_as_list:
            #     # print(page)
            #     self.pdf_text_as_str.append(f"\n {page}")
            #     # print(self.pdf_text_as_str)

