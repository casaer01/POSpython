import win32print
from gatherPrinters import *

content = readText()

brotherPrint = call_printer(1)

# # Get the default printer
# default_printer = win32print.GetDefaultPrinter()

# # Open the printer
# printer = win32print.OpenPrinter(brotherPrint)

# # Start a document
# doc_info = {"DocName": "Testing Print", "OutputFile": None , "DataType": "RAW"}
# doc_handle = win32print.StartDocPrinter(printer, 1, (doc_info["DocName"],doc_info["OutputFile"], doc_info["DataType"] ))

# # Start a page
# win32print.StartPagePrinter(printer)

# # Write the text to the printer
# text = content
# win32print.WritePrinter(printer, text.encode('utf-8'))

# # End the page
# win32print.EndPagePrinter(printer)

# # End the document
# win32print.EndDocPrinter(printer)

# # Close the printer
# win32print.ClosePrinter(printer)



# 2nd method


# Select a printer by name
printer_name = brotherPrint # Replace with your printer's name
printer_handle = win32print.OpenPrinter(printer_name)

# Set the printer properties (optional)
properties = win32print.GetPrinter(printer_handle, 2)
properties['pDevMode'].Duplex = win32print.DMDUP_SIMPLEX # Set duplex mode to simplex
properties['pDevMode'].Copies = 2 # Set number of copies to 2
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
