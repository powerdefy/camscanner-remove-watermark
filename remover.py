from PyPDF2 import PdfFileReader, PdfFileWriter

input_file = PdfFileReader(open('input.pdf', 'rb'))
output = PdfFileWriter()
page_count = input_file.getNumPages()

for page_number in range(input_file.getNumPages()):
    page = input_file.getPage(page_number)
    page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 30)
    output.addPage(page)

output_stream = open('output.pdf', 'wb')
output.write(output_stream)