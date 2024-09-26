import aiogram
from .create_dispatcher import dispatcher
@dispatcher.message()
async def message_handler(message):
    await message.answer("Hello!")