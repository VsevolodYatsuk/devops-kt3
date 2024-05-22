import http.server
import threading
import time
from prometheus_client import start_http_server, Gauge


INPROGRESS = Gauge('hello_words_inprogress', 'Number of Hello Words in progress')
LAST = Gauge('hello_word_last_time_seconds', 'The last time a Hello World was served')
COUNTER = Gauge('periodic_hello_count', 'Periodic Hello Count')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @INPROGRESS.track_inprogress()
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World')
        LAST.set_to_current_time()
    
    def log_message(self, format, *args):
        print("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format % args))

def periodic_task():
    while True:
        COUNTER.inc() 
        print("Periodic task executed. Counter incremented.")
        time.sleep(30) 

if __name__ == "__main__":
    start_http_server(8000)
    
    thread = threading.Thread(target=periodic_task)
    thread.daemon = True
    thread.start()

    server = http.server.HTTPServer(('0.0.0.0', 8001), MyHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()