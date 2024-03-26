import win32print
import sys

# printer_name = "Brother MFC-J6555DW" # Replace with your printer's name
# text_to_print = "Hello, World!"

# # Open the printer
# try:
#     p = win32print.OpenPrinter(printer_name)
#     # Code that might raise an exception
# except err:
#     print("Printer name is not defined.")

# # p = win32print.OpenPrinter(printer_name)

# # Start a print job
# job = win32print.StartDocPrinter(p, 1, (text_to_print, None, "RAW"))
# win32print.StartPagePrinter(p)

# # Write the text to the printer
# win32print.WritePrinter(p, text_to_print)

# # End the page and the print job
# win32print.EndPagePrinter(p)
# win32print.EndDocPrinter(p)

# # Close the printer
# win32print.ClosePrinter(p)



# Second method
# Get the default printer name
printer_name = win32print.GetDefaultPrinter()

# Prepare the data to print
if sys.version_info >= (3,):
    raw_data = bytes("This is a test", "utf-8")
else:
    raw_data = "This is a test"

# Open the printer
defaultPrint = win32print.OpenPrinter(printer_name)

try:
    # Start a document
    hJob = win32print.StartDocPrinter(defaultPrint, 1, ("test of raw data", None, "RAW"))
    try:
        # Start a page
        win32print.StartPagePrinter(defaultPrint)
        # Write the data to the printer
        win32print.WritePrinter(defaultPrint, raw_data)
        # End the page
        win32print.EndPagePrinter(defaultPrint)
    finally:
        # End the document
        win32print.EndDocPrinter(defaultPrint)
finally:
    # Close the printer
    win32print.ClosePrinter(defaultPrint)
