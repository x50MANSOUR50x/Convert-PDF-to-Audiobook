from PDF_reader import PDF_READER
from text_extraxter import TEXT_EXTRAXTER
from text_converter import TEXT_CONVERTER

def program():
    reader = PDF_READER()

    pdf_path = reader.file_path

    # print(pdf_path)

    text_extraxter = TEXT_EXTRAXTER(pdf_file=pdf_path)

    text = text_extraxter.pdf_text_as_list

    # print(len(text))
    # print(type(text))
    # print(text)

    audiobook = TEXT_CONVERTER(text=text, pdf_path=pdf_path)

    if (input('Would you like to try again? Enter "yes" or "no"\n').lower() == "yes"):
        program()

if "__main__" == __name__:
    program()
