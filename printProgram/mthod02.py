import win32print

# Get the default printer
default_printer = win32print.GetDefaultPrinter()

# Open the printer
printer = win32print.OpenPrinter(default_printer)

# Start a document
doc_info = {"DocName": "HelloWorld", "OutputFile": None, "DataType": "RAW"}
doc_handle = win32print.StartDocPrinter(printer, 1, doc_info)

# Start a page
win32print.StartPagePrinter(printer)

# Write the text to the printer
text = "Hello World"
win32print.WritePrinter(printer, text.encode('utf-8'))

# End the page
win32print.EndPagePrinter(printer)

# End the document
win32print.EndDocPrinter(printer)

# Close the printer
win32print.ClosePrinter(printer)
