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
