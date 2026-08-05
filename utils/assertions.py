def assert_book_schema(book):

    required_fields = [
        "isbn",
        "title",
        "author",
        "publisher",
        "pages",
    ]

    for field in required_fields:
        assert field in book, f"Missing field: {field}"