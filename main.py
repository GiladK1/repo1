import asyncio
from flask import Flask
from routes import routes
import logging

FORMAT = "[%(asctime)s] File name: %(filename)s | Function Name:%(funcName)s: %(levelname)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format= FORMAT)

app = Flask(__name__)
app.register_blueprint(routes)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

if __name__ == "__main__":
    try:
        app.logger.info("SERVER START")
        loop.run_until_complete(app.run(debug=False, use_reloader=False))
    except Exception as error:
        app.logger.error(f"Error {error}")
        loop.close()
