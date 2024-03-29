def call_printer(num: int):
    if num == 1:
        return "Brother MFC-J6555DW"
    else:
        return "HP LaserJet M15w (C0D8CE)"

# brotherPrinter = "Brother MFC-J6555DW"
# hpPrinter = "HP LaserJet M15w (C0D8CE)"

def readText():

    file_path = "texttest.txt"

    with open(file_path, 'r') as file:
        content = file.read()

    return content