from qreader import QReader
import cv2
import webbrowser
import tkinter as tk
from tkinter import filedialog

# Create a QReader instance
qreader = QReader()
root = tk.Tk()
root.withdraw()

pth = tk.filedialog.askopenfilename()
# pth = str(input('Filepath to image: ')).strip()
# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread(pth), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)

webbrowser.open_new_tab(decoded_text[0])