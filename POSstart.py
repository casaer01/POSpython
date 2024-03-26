import win32print

printer_name = "Brother MFC-J6555DW" # Replace with your printer's name
text_to_print = "Hello, World!"

# Open the printer
try:
    p = win32print.OpenPrinter(printer_name)
    # Code that might raise an exception
except err:
    print("Printer name is not defined.")
    break

# p = win32print.OpenPrinter(printer_name)

# Start a print job
job = win32print.StartDocPrinter(p, 1, (text_to_print, None, "RAW"))
win32print.StartPagePrinter(p)

# Write the text to the printer
win32print.WritePrinter(p, text_to_print)

# End the page and the print job
win32print.EndPagePrinter(p)
win32print.EndDocPrinter(p)

# Close the printer
win32print.ClosePrinter(p)
