import http.server
import socketserver

# Define the port and directory
host = "localhost"
port = 80
# directory = r"E:\Desktop\UNSW\2024\COMP6841\SAP\dist"  # Replace with the directory containing your file

# Change directory to the one with the file
# import os
# os.chdir(directory)

# Start the server
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()