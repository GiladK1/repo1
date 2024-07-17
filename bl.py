import pandas as pd
from flask import current_app
from dl import DL
import json
import datetime


class BL:

    @staticmethod
    async def get_str():
        try:
            current_app.logger.info("START")
            current_app.logger.info("Calling DL.get_reservation")
            result = await DL.get_str()
            return result
        except Exception as error:
            current_app.logger.error(f"Error {error}")
