from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class Task(Document):
    meta = {'collection': 'tasks'}
    
    name = StringField(required=True)
    status = StringField(
        required=True,
        choices=('pending', 'running', 'success', 'failure'),
        default='pending'
    )
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Task, self).save(*args, **kwargs)
