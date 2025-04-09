from datetime import datetime
from uuid import UUID, uuid4


class ToDo:
    def __init__(self, title: str, user_id: UUID, completed: bool = False):
        self.id = uuid4()
        self.title = title
        self.user_id = user_id
        self.completed = completed
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        return

    def __repr__(self):
        return f"<ToDo {self.id} title={self.title} user_id={self.user_id} completed={self.completed}>"

    def __str__(self):
        return f"ToDo(id={self.id}, title={self.title}, user_id={self.user_id}, completed={self.completed})"

    def mark_done(self):
        self.completed = True
        self.completed_at = datetime.utcnow()
        return self
