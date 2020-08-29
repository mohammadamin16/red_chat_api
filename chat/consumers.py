# chat/consumers.py
import json, time
from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

GROUP_NAME = 'chat_room'
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            GROUP_NAME,
            self.channel_name
        )
        name = 'amin'
        await self.send(f'connected {name}')

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            GROUP_NAME,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            GROUP_NAME,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

