#Duck typing-it is a concept where the type of an object is determined
#by its behaviour, not by it's class
class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet Printer printing: ",document)

class LaserPrinter:
    def printdocument(self,document):
        print("Laser Printer printing: ",document)


class PDFWriter:
    def printdocument(self,document):
        print(f"Saving : {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()




