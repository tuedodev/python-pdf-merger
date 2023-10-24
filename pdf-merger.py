from os import mkdir
from os.path import join
from pathlib import Path
from pypdf import PdfMerger

path = './test'
pdf_merger_path = Path(join(path, 'merged'))
filename = 'Merged_PDF_File.pdf'

try:
    filelist = sorted([f.name for f in Path(path).iterdir() if f.is_file() and f.suffix.lower() == '.pdf'])
    if len(filelist) > 0:
        if filename[-4:] == '.pdf':
            pdf_merger = PdfMerger()
            for count, value in enumerate(filelist):
                pdf_merger.append(join(path, value))
                print(f"{count + 1}. {value} merged.")
            if not pdf_merger_path.is_dir():
                mkdir(pdf_merger_path)
            pdf_merger.write(join(pdf_merger_path, filename))
            print(f"==> Merged {count + 1} PDF file{'' if count == 0 else 's'}: {filename} created inside {pdf_merger_path} directory.")
        else: 
            print(f"Incorrect filename {filename} for PDF files.")
    else:
        print(f"No PDF files(s) found in the {path} directory.")
except FileNotFoundError:
    print (f"Directory {path} not found.")