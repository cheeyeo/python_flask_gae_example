from flask import Flask
from flask import render_template
from flask import request
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("app")

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")

    if celsius:
        farenheit = farenheit_from(celsius)
        logger.info("Converted from Celsius {} to Farenheit {}".format(celsius, farenheit))
    else:
        farenheit = ""

    return render_template("index.html", farenheit=farenheit)

def farenheit_from(celsius):
    """
    Convert from celsius to farenheit
    """
    try:
        farenheit = float(celsius) * 9 / 5 + 32
        farenheit = round(farenheit, 3)
        return str(farenheit)
    except ValueError:
        logger.error("Invalid temp value")
        return "Invalid input"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)