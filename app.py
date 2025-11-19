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

app.run(host="0.0.0.0", port=5000)

