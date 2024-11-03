import binascii

def convert_to_hex(filename, output_file):
    with open(filename, 'rb') as file:
        binary_data = file.read()

    hex_code = binascii.hexlify(binary_data).decode()

    with open(output_file, 'w') as output:
        output.write(hex_code)

# Esempio di utilizzo
exe_filename = r'E:\Desktop\UNSW\2024\COMP6841\SAP\dist\keylogger.exe'
output_filename = r'E:\Desktop\UNSW\2024\COMP6841\SAP\dist\keylogger.txt'
convert_to_hex(exe_filename, output_filename)