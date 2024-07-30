class Todo:
    def __init__(self, id, text, completed):
        self.id = id
        self.text = text
        self.completed = completed

    def __repr__(self):
        return f"Todo(id={self.id}, text={self.text}, completed={self.completed})"
    
    @staticmethod
    def create(id, text, completed):
        return Todo(id, text, completed)

