""" 
Description: 
 - Concatenates three PDF files together as "MergedFile.pdf".

Author: Jamey Kirk
Date: 05.28.2021
Assignment: 08
Class: CIS 112
"""

import os, pathlib
from PyPDF2 import PdfFileMerger
from pathlib import Path

pdf_path = os.path.join(pathlib.Path.cwd())
print("\n" + pdf_path + "\n")

for path in pdf_path.glob("*.pdf"):
    print(path.name)
#input_pdf = PdfFileReader(pdf_path)
