import pyttsx3 as text2speech
import PyPDF2 as pdfreader

source = input('Enter your file location and name: ')
a = input('Enter the page you want to start with: ')
b = input('Enter the page of ending: ')

content = open(source,'rb')
Read = pdfreader.PdfFileReader(content)
page_no = Read.numPages
Gwen = text2speech.init()

voices = Gwen.getProperty("voices")
volume = Gwen.getProperty("volume")
rate = Gwen.getProperty("rate")

Gwen.setProperty("voice",voices[1].id)
Gwen.setProperty("volume",1)
Gwen.setProperty("rate",200)

if b == page_no:
    for num in range(int(a) - 1,page_no):
        page = Read.getPage(num)
        text = page.extractText()
        Gwen.say(text)
        Gwen.runAndWait()
else:
    for num in range(int(a) - 1,int(b)):
        page = Read.getPage(num)
        text = page.extractText()
        Gwen.say(text)
        Gwen.runAndWait()

