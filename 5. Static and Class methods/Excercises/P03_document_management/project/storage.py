from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for current_category in self.categories:
            if current_category.id == category.id:
                return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for current_topic in self.topics:
            if current_topic.id == topic.id:
                return
        self.topics.append(topic)

    def add_document(self, document: Document):
        for current_doc in self.documents:
            if current_doc.id == document.id:
                return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for current_category in self.categories:
            if current_category.id == category_id:
                current_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for current_topic in self.topics:
            if current_topic.id == topic_id:
                current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        for current_doc in self.documents:
            if current_doc.id == document_id:
                current_doc.etit(new_file_name)

    def delete_category(self, category_id):
        for current_category in self.categories:
            if current_category.id == category_id:
                self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        for current_topic in self.topics:
            if current_topic.id == topic_id:
                self.topics.remove(current_topic)

    def delete_document(self, document_id):
        for current_document in self.documents:
            if current_document.id == document_id:
                self.documents.remove(current_document)

    def get_document(self, document_id):
        for current_document in self.documents:
            if current_document.id == document_id:
                return current_document

    def __repr__(self):
        result = '\n'.join(repr(x) for x in self.documents)
        return result
