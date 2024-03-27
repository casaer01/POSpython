import win32print
import sys

# Second method
# Get the default printer name
# printer_name = win32print.GetDefaultPrinter()

brotherPrinter = "Brother MFC-J6555DW"
hpPrinter = "HP LaserJet M15w (C0D8CE)"

#using a text file to test with print api
file_path = 'texttest.txt'

with open(file_path, 'r') as file:
    content = file.read()


# # Prepare the data to print
if sys.version_info >= (3,):
    raw_data = bytes(content, "utf-8")
else:
    raw_data = content

# Method number 3
     

# Open the printer
printer_name = win32print.GetDefaultPrinterW()
try:
    p = win32print.OpenPrinter(hpPrinter)
except:
    p = win32print.OpenPrinter(printer_name)

# p = win32print.OpenPrinter(printer_name)

# Start a print job
job = win32print.StartDocPrinter(p, 1, ("Test document", None, "raw"))
win32print.StartPagePrinter(p)


# Write data to the printer
# Replace "data to print" with the actual data you want to print

win32print.WritePrinter(p, raw_data)

# End the print job
win32print.EndPagePrinter(p)
win32print.EndDocPrinter(p)

# Close the printer
win32print.ClosePrinter(p)


# third method

printer_name = "Printer Name"
printer_handle = win32print.OpenPrinter(printer_name)
# Set the printer properties
properties = win32print.GetPrinter(printer_handle, 2)
properties['pDevMode'].Duplex = win32print.DMDUP_SIMPLEX  # Set duplex mode to simplex
properties['pDevMode'].Copies = 2  # Set number of copies to 2
win32print.SetPrinter(printer_handle, 2, properties, 0)
# Print a document
job_info = ('Test Document', None, {'DesiredAccess': win32print.PRINTER_ALL_ACCESS})
job_handle = win32print.StartDocPrinter(printer_handle, 1, job_info)
win32print.StartPagePrinter(printer_handle)
win32print.WritePrinter(printer_handle, b'This is a test document')
win32print.EndPagePrinter(printer_handle)
win32print.EndDocPrinter(printer_handle)
# Close the printer handle
win32print.ClosePrinter(printer_handle)
