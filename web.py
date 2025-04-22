

from http.server import HTTPServer,BaseHTTPRequestHandler

content='''<!doctype html>
<html>
<head>
<title>WEBSERVER</title>
<style>
    table,tr,td,th
    {
    
    border:1px solid #000000;
    border-collapse: separate;
    padding:10px;
    text-align:center;
    background-color: aquamarine;
    }
    </style>
</head>
<body>
<left><h1 style="font-family: 'Times New Roman', Times, serif;"><b><u>TCP/IP PROTOCOLS</u></b></h1><br>
</left>
<table>
<tr>
<th>S.NO</th>
<th>LAYER</th>
<th>PROTOCOLS</th>
</tr>
<tr>
    <td>1.</td>
    <td>Transport layer protocol</td>
    <td>TCP</td>
    
<tr>
<td>2.</td>
<td>Application layer protocol</td>
<td>HTTPS,FTP</td>
</tr>
    

    
</tr>
<tr>
    <td>3.</td>
    <td>Link layer protocol</td>
    <td>MAC</td>
    </tr>
    
<tr>
<td>4.</td>
<td>Internet layer protocol</td>
<td>IP</td>
</tr>
    

</table>
</body>
</html>

'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("My webserver is running") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8000)
httpd=HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()