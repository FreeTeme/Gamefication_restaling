from telethon.sync import TelegramClient
from telethon import functions, types

# Пример вызова функции
# channel = '@studeventsmsk'  # Канал должен быть в формате '@channelusername'
# total_reactions = await get_total_reactions(channel)

api_id = "20211195"
api_hash = "900a88063d66744450d23f6ddd52af6e"
phone = "+375295332073"

client = TelegramClient(phone, api_id, api_hash)

async def get_total_reactions(channel):
    async with client:
        messages = await client.get_messages(channel, limit=1)

        if messages:
            msg_id = messages[0].id
            print(f"Используемый msg_id: {msg_id}")

            # Получение списка реакций
            result = await client(functions.messages.GetMessagesReactionsRequest(
                peer=channel,
                id=[msg_id]
            ))

            # Подсчет общего количества реакций
            total_reactions = 0
            for update in result.updates:
                if isinstance(update, types.UpdateMessageReactions):
                    total_reactions += sum(reaction.count for reaction in update.reactions.results)
            print(f"Общее количество реакций: {total_reactions}")

            return total_reactions


