# def test_create_book_with_author(client, two_saved_authors):
#     resp = client.post("/authors/1/books", json={
#         "title": "New Tale", "description": "Fun read"
#     })
#     assert resp.status_code == 201
#     body = resp.get_json()
#     assert body["author_id"] == 1
#     assert body["title"] == "New Tale"

# def test_get_books_by_author(client, two_saved_authors, two_saved_books):
#     resp = client.get("/authors/1/books")
#     assert resp.status_code == 200
#     books = resp.get_json()