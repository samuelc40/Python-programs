import pdfkit

# configuring pdfkit to point to our installation of wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# converting html file to pdf file
# pdfkit.from_file('sample.html', 'output.pdf', configuration=config)
pdfkit.from_url('https://spsonline.in','sps.pdf')