import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import PyPDF2

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.pdf'):
            self.process_pdf(event.src_path)

    def process_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            fields = reader.get_form_text_fields()  # Extract form fields
            print(fields)  # Print or save the extracted fields

observer = Observer()
folder_to_watch = ""C:\Users\wmpinkerton\OneDrive - JSJ Corporation\OCR""  # Replace with your folder path
observer.schedule(PDFHandler(), path=folder_to_watch, recursive=False)
observer.start()

try:
    while True:
        pass  # Keeps the script running
except KeyboardInterrupt:
    observer.stop()
observer.join()
