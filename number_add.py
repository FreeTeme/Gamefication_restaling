from telethon.sync import TelegramClient

api_id = "20211195"
api_hash = "900a88063d66744450d23f6ddd52af6e"
phone = "+375295332073"

client = TelegramClient(phone, api_id, api_hash)

async def main():
    async with client:
        print("Сессия успешно создана и сохранена.")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
