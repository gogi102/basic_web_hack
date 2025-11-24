from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parse

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        f = open("index.html", "r")
        data = f.read()
        f.close()
        self.wfile.write(data.encode())
        # self.wfile.write('<p>hello world get</p>'.encode())
        # print("get")
        # self.wfile.write(self.path.encode())
        # self.wfile.write('<br>'.encode())
        # if "?" in self.path:
        #     self.wfile.write(str(self.path.split("?")[1].split("&")).encode())  
        #     print(parse.parse_qsl(self.path.split("?")[1]))
        #     print(dict(parse.parse_qsl(self.path.split("?")[1])))

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        print("post")
        self.wfile.write(self.path.encode())
        self.wfile.write('<br>'.encode())
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data is not None :
            data_decode = dict(parse.parse_qs(data.decode()))
        if data_decode['id'] == ['yjs'] and data_decode['pw'] == ['9312']:
            self.wfile.write('login succsess'.encode())
        else :
            f = open("index_fail.html", "r")
            data = f.read()
            f.close()
            self.wfile.write(data.encode())
        print(f'post params = {data_decode}')

PORT = 8080
server = HTTPServer(('',PORT),ServerHandler)
print(f'서버가 {PORT}로 구동중임')
server.serve_forever()