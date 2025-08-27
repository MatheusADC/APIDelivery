from bson.objectid import ObjectId
from .interfaces.orders_repository import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data
    
    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, # filtro de busca
            { "_id": 0, "cupom": 0 } # opções de retorno
        )
        return data
     
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
            { "address": { "$exists": True } },
            { "_id": 0, "itens": 0 }
        )
        return response
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data
    
    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId('68a38c8389572a6b28f46fda') }, # Filtros
            { "$set": { "itens.energetico.quantidade": 30 } } # Edição
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            { "itens.doce": { "$exists": True } }, # Filtros
            { "$set": { "itens.doce.quantidade": 6 } } # Edição
        )

    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId('68a38c8389572a6b28f46fda') }, # Filtros
            { "$inc": { "itens.energetico.quantidade": 50 } } # Edição
        )

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({ "_id":ObjectId('68a38c6789572a6b28f46fd9') })

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many({ "itens.doce": { "$exists": True } })
