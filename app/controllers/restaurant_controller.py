from flask import Blueprint, request, jsonify
from models.restaurant_model import restaurant
from views.restaurant_view import render_restaurant_list, render_restaurant_detail
from utils.decorators import jwt_required, role_required


restaurant_bp = Blueprint("restaurant", __name__)


@restaurant_bp.route("/restaurants", methods=["GET"])
@jwt_required
@role_required(role=["admin", "customer"])
def get_restaurants():
   restaurants = restaurant.get_all()
   return jsonify(render_restaurant_list(restaurants))


@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@role_required(role=["admin", "user"])
def get_restaurant(id):
   restaurant = restaurant.get_by_id(id)
   if restaurant:
      return jsonify(render_restaurant_detail(restaurant))
   return jsonify({"error": "Restaurant no encontrado"}), 404
