import gtts
import os
import re
from pdfreader import SimplePDFViewer, PDFDocument



def pdf_audio():

    # Leer el archivo PDF
    file = open('La-cuarta-revolucion-industrial.pdf', 'rb') # aqui va el nombre de tu archivo pdf
    doc = PDFDocument(file)
    all_pages = [p for p in doc.pages()]
    pages = len(all_pages)
    print(pages)
    viewer = SimplePDFViewer(file)

    # iteramos en las paginas del archivo pdf 
    for page in range(pages):
        if page <= pages:

            try :
                # Limpiar el texto obtenido del archivo pdf
                viewer.navigate(page + 1)
                viewer.render()
                page_8_canvas = viewer.canvas
                text_content = str(page_8_canvas.strings).replace("'", "").replace(",", "").replace("[", "").replace("]", "")
                text_content1 = re.sub(r'(?<=\w)\s(?=\w)', '', text_content)
                print(text_content1)
            except AssertionError:
                continue

            try :
                # Convertir el texto a voz en español
                tts = gtts.gTTS(text_content1, lang='es')
                tts.save('documento.mp3')
                os.system("mpg123 documento.mp3")
                os.remove("documento.mp3")
            except AssertionError:
                continue

if __name__ == "__main__":
    pdf_audio()