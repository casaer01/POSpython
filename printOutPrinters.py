import win32print

printers = win32print.EnumPrinters(2)
# Print the list of printers
for printer in printers:
    print(printer[2])