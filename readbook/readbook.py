from gtts import gTTS as gt



import PyPDF2 as pdf
pdfFileObj = open('read.pdf','rb')
pdfReader = pdf.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()


tts = gt(pageObj.extractText())
tts.save('hello.mp3')