# OCR - Only for Windows

Pyqt5 based GUI OCR for documents and clear picture using pytesseract

>Please visit the link below to download tesseract for windows and install it

https://github.com/UB-Mannheim/tesseract/wiki

>Guide:

Pip install the requirements listed in requirements.txt

After downloading and installing the tesseract from the link above. git clone the repo and and run the application.py

If errors show up, open the OCR_Application.py and change this line like this to your tesseracts path

>pytesseract.pytesseract.tesseract_cmd = os.path.join(os.getcwd(), 'OCR', 'Tesseract-OCR', 'tesseract.exe')

You might have installed the tesseract in C:\ directory. Change the directory accordingly. Above case was when i had the OCR software installed in the same directory as OCR_Application.py.
