# https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer
from movement import create_graph


HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 3000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """
        Respond to a GET request.
        """
        try:
            # get info from systems
            steps   = int(s.path.split('/')[1])
            systems = int(s.path.split('/')[2])

            # create graph
            create_graph(steps, systems)
            img = open("plt.png")

            # write headers
            s.send_response(200)
            s.send_header("Content-type", "image/png")
            s.end_headers()

            # write content
            s.wfile.write(img.read())
            img.close()
        except:
            s.send_response(404)
            s.send_header("Content-type", "text/html")
            s.end_headers()

            s.wfile.write("Error. path should be site___.com/NUM_STEPS/NUM_PRESSURE_SYSTEMS")
            s.wfile.write("site___.com/10000/4")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)