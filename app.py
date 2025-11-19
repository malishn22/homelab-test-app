from flask import Flask
app = Flask(__name__)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

@app.get("/")
def home():
    app.logger.info("Home endpoint called")
    return "Homelab Test with logging"

port = int(os.environ.get("APP_PORT", 5000))
app.run(host="0.0.0.0", port=port)

