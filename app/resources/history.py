from flask import Blueprint, request
from utils.response import success_response, error_response
from utils.auth_decorator import jwt_required, is_admin
from services.history_service import HistoryService

history_service = HistoryService()
history_bp = Blueprint('history', __name__)

@history_bp.route('/math-histories', methods=['GET'])
@jwt_required
def get_all_history():
    history = history_service.get_all_histories()
    return success_response([{"id": h.id, "question": h.question, "answer": h.answer, "user_id": h.user_id} for h in history])

@history_bp.route('/history/<int:history_id>', methods=['GET'])
@jwt_required
def get_history(history_id):
    history = history_service.get_history(history_id)
    if history:
        return success_response({"id": history.id, "question": history.question, "answer": history.answer, "user_id": history.user_id})
    else:
        return error_response("History not found", status_code=404)


@history_bp.route('/math-history', methods=['POST'])
@jwt_required
def create_history():
    data = request.get_json()
    new_history = history_service.create_history(data.get('question'), data.get('answer'), data.get('user_id'))
    return success_response({"id": new_history.id, "question": new_history.question, "answer": new_history.answer, "user_id": new_history.user_id}, status_code=201)

@history_bp.route('/math-history/<int:history_id>', methods=['PUT'])
@jwt_required
def update_history(history_id):
    data = request.get_json()
    updated_history = history_service.update_history(history_id, data.get('question'), data.get('answer'), data.get('user_id'))
    if updated_history:
        return success_response({"id": updated_history.id, "question": updated_history.question, "answer": updated_history.answer, "user_id": updated_history.user_id})
    else:
        return error_response( "History not found", status_code=404)


@history_bp.route('/math-history/<int:history_id>', methods=['DELETE'])
@jwt_required
def delete_history(history_id):
    history_service.delete_history(history_id)
    return success_response("History deleted successfully",status_code=204)


# get all history by user id
@history_bp.route('/user/<int:user_id>/math-history', methods=['GET'])
@jwt_required
@is_admin
def get_all_history_by_user_id(user_id):
    history = history_service.get_all_histories_by_user_id(user_id)
    return success_response([{"id": h.id, "question": h.question, "answer": h.answer, "user_id": h.user_id} for h in history])

# delete user history record
@history_bp.route('/user/<int:user_id>/math-history/<int:history_id>', methods=['DELETE'])
@jwt_required
@is_admin
def delete_user_history(user_id):
    #  Add user permission check
    # user_id = request.user_id
    history_service.delete_history_by_user(user_id)
    return success_response( "History deleted successfully", status_code=204)

# get all user history
@history_bp.route('/user/math-history', methods=['GET'])
@jwt_required
def get_all_user_history():
    user_id = request.user_id
    history = history_service.get_all_histories_by_user_id(user_id)
    return success_response([{"id": h.id, "question": h.question, "answer": h.answer, "user_id": h.user_id} for h in history])


# delete user history record
@history_bp.route('/user/math-history/<int:history_id>', methods=['DELETE'])
@jwt_required
def delete_history_by_user():
    user_id = request.user_id
    history_service.delete_history_by_user(user_id)
    return success_response("History deleted successfully", status_code=204)