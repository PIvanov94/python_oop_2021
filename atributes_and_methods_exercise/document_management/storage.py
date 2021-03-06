class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += f"{doc.__repr__()}\n"
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if category_id == c.id][0]
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if topic_id == t.id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [d for d in self.documents if document_id == d.id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if category_id == c.id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if topic_id == t.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [d for d in self.documents if document_id == d.id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        return [d for d in self.documents if document_id == d.id][0]


# from repo.python_oop_2021.atributes_and_methods_exercise.document_management.category import Category
# from repo.python_oop_2021.atributes_and_methods_exercise.document_management.document import Document
# from repo.python_oop_2021.atributes_and_methods_exercise.document_management.topic import Topic
