from flask import Blueprint, Response, current_app, request
from bl import BL
import json

routes = Blueprint('routes',__name__)

@routes.route("/get_data", methods = ["GET"])
async def get_str():
    current_app.logger.info("START")
    reservation_id = request.args.get('reservation_id')
    result = await BL.get_str()
    current_app.logger.info("END")
    return  Response(result, 200)

