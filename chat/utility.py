from channels.db import database_sync_to_async

from .models import Message


def message2json(message: Message):
    return {
        'body': message.body
    }

@database_sync_to_async
def get_messages():
    messages = Message.objects.all()
    json_messages = []
    for m in messages:
        json_messages.append(message2json(m))
    return json_messages