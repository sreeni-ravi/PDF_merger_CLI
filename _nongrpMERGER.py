from PyPDF2 import PdfFileMerger
import os
import sys


files = []

#PDF Merger function
def merger(output_path, input_paths):    
    pdf_merger = PdfFileMerger() 
    for path in input_paths:
        if path.endswith(".pdf" or ".PDF"):
            pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

def main(_direct, _result):       
    for r, d, f in os.walk(_direct):
        for file in f:
            if file.endswith(".pdf" or ".PDF"):
                files.append(os.path.join(r, file))
            
    finalfile = _result + '\merged.pdf'   
    merger(finalfile, files)     
    FinalMessage = 'Merger Completed and file saved in ' + finalfile
    print(FinalMessage)

if __name__ == "__main__":
    directory = (sys.argv[1])
    main(directory, directory )