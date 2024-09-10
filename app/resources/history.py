from flask import Blueprint, jsonify, request
from services.history_service import HistoryService

history_service = HistoryService()
history_bp = Blueprint('history', __name__)

@history_bp.route('/math-histories', methods=['GET'])
def get_all_history():
    history = history_service.get_all_history()
    return jsonify([{"id": h.id, "question": h.question, "answer": h.answer, "user_id": h.user_id} for h in history])

@history_bp.route('/history/<int:history_id>', methods=['GET'])
def get_history(history_id):
    history = history_service.get_history(history_id)
    if history:
        return jsonify({"id": history.id, "question": history.question, "answer": history.answer, "user_id": history.user_id})
    else:
        return jsonify({"error": "History not found"}), 404


@history_bp.route('/history', methods=['POST'])
def create_history():
    data = request.get_json()
    new_history = history_service.create_history(data['question'], data['answer'], data['user_id'])
    return jsonify({"id": new_history.id, "question": new_history.question, "answer": new_history.answer, "user_id": new_history.user_id}), 201

@history_bp.route('/history/<int:history_id>', methods=['PUT'])
def update_history(history_id):
    data = request.get_json()
    updated_history = history_service.update_history(history_id, data['question'], data['answer'], data['user_id'])
    if updated_history:
        return jsonify({"id": updated_history.id, "question": updated_history.question, "answer": updated_history.answer, "user_id": updated_history.user_id})
    else:
        return jsonify({"error": "History not found"}), 404


@history_bp.route('/history/<int:history_id>', methods=['DELETE'])
def delete_history(history_id):
    history_service.delete_history(history_id)
    return jsonify({"message": "History deleted successfully"}), 200


# get history by user id
@history_bp.route('/history/user/<int:user_id>', methods=['GET'])
def get_history_by_user_id(user_id):
    history = history_service.get_history_by_user_id(user_id)
    if history:
        return jsonify({"id": history.id, "question": history.question, "answer": history.answer, "user_id": history.user_id})
    else:
        return jsonify({"error": "History not found"}), 404

@history_bp.route('/history/user/<int:user_id>', methods=['DELETE'])
def delete_history_by_user_id(user_id):
    history_service.delete_history_by_user_id(user_id)
    return jsonify({"message": "History deleted successfully"}), 200