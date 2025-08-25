from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args

class DbCollectionMock:
    def __init__(self, collection) -> None:
        self.get_collection_attributes = {}
        self.collection = collection

    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection

def test_insert_document():
    collection = CollectionMock()
    db_collection = DbCollectionMock(collection)
    repo = OrdersRepository(db_collection)

    doc = { "alguma": "coisa" }
    repo.insert_document(doc)

    print()
    print(collection.insert_one_attributes)
    assert collection.insert_one_attributes["dict"] == doc

# pytest src/models/repository/orders_repository_test.py