from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(list_of_objs, object_id: int):
        return next((object_info for object_info in list_of_objs if object_info.id == object_id), None)

    def edit_category(self, category_id: int, new_name: str):
        cat_obj = self.__find_object(self.categories, category_id)
        cat_obj.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_obj = self.__find_object(self.topics, topic_id)
        topic_obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        doc_obj = self.__find_object(self.documents, document_id)
        doc_obj.edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories.remove(self.__find_object(self.categories, category_id))

    def delete_topic(self, topic_id: int):
        self.topics.remove(self.__find_object(self.topics, topic_id))

    def delete_document(self, document_id: int):
        self.documents.remove(self.__find_object(self.documents, document_id))

    def get_document(self, document_id: int):
        return self.__find_object(self.documents, document_id)

    def __repr__(self):
        return "\n".join(repr(doc) for doc in self.documents)
