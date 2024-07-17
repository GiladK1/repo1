from flask import current_app
import pandas as pd


class DL:

    @staticmethod
    async def get_str():
        try:
            current_app.logger.info("START")
            current_app.logger.info("Getting data from reservation file")
            data = "DATA FROM DB SERVICE"
            current_app.logger.info("END")
            return data
        except Exception as error:
            current_app.logger.error(f"Error {error}")




