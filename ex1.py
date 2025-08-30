from http.server import HTTPServer, BaseHTTPRequestHandler

htmlcontent = '''
<!doctype html>
<html>
<head>
    <title>Sample</title>
</head>
<body>
    <center><font color=blue face="Arial" size="100">
   <b>List of Protocols in TCP/IP Model</b>
    </font></center>
    <font color="green">
    <h2>
        Application Layer - HTTP, FTP, DNS, Telnet & SSH<br>
        Transport Layer - TCP & UDP<br>
        Network Layer - IPV4/IPV6<br>
        Link Layer - Ethernet
    </h2>
    </font>
</body>
</html>
'''

class ServerResponse(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_add =('',8000)
httpd = HTTPServer(server_add,ServerResponse)
httpd.serve_forever()