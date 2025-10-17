import threading
import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Simple HTTP server that returns a published APIs payload for /apis?public_only=true
class FakeProducerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/apis'):
            payload = {
                'count': 1,
                'items': [
                    {
                        'id': 'demo.api.1',
                        'name': 'Demo API',
                        'owner': 'tester',
                        'version': '1.0',
                        'description': 'A demo API',
                        'endpoints': ['/demo'],
                        'public': True
                    }
                ]
            }
            body = json.dumps(payload).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

def run_fake_producer(port=9001):
    server = HTTPServer(('localhost', port), FakeProducerHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def test_manager_sync():
    srv = run_fake_producer(9001)
    try:
        # call the manager sync endpoint
        resp = requests.post('http://localhost:8002/sync_from_producer', json={'producer_url': 'http://localhost:9001'})
        print('manager sync status:', resp.status_code)
        print('manager response:', resp.text)
    except Exception as e:
        print('error calling manager:', e)
    finally:
        srv.shutdown()

if __name__ == '__main__':
    test_manager_sync()
