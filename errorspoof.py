import time
import logging

# Configure logging to use the root logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s.%(msecs)03d ERROR %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

def log_error():
    error_message = 'http.handlers.reverse_proxy aborting with incomplete response {"error": "context canceled"}'
    logging.error(error_message)
    print(f'<script>console.error("{error_message}")</script>')  # Log to browser console

# Log error every set amount of seconds
while True:
    log_error()
    time.sleep(0.42)
