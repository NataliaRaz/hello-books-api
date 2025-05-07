from flask import Blueprint, abort, make_response, request
import json
from app.models.book import Book
from .route_utilities import create_model, validate_model, get_models_with_filters
from flask import Response
from ..db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)


@books_bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)
@books_bp.get("/<book_id>")
def get_one_book(book_id):
    book = validate_model(Book, book_id)

    return book.to_dict()

@books_bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    #return book.to_dict(), 200
    return Response(status=204, mimetype="application/json")