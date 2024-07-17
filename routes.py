from flask import Blueprint, Response, current_app

routes = Blueprint('routes',__name__)

@routes.route("/hello", methods = ["GET"])
async def hello():
    current_app.logger.info("START")
    return Response("Hello World from app 1!", 200)
