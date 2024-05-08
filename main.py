from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from messages import send_message_kiwi, send_message_scrouge, send_message_zelenka, send_other

api_id = 22254967
api_hash = "b877800157e0d8e995d87b04dc3cc977"

app = Client("my_account")
scheduler = AsyncIOScheduler()

async def main():

    scheduler.add_job(send_message_scrouge, "cron", hour=12, day="*")
    scheduler.add_job(send_message_kiwi, "interval", hour=10)
    scheduler.add_job(send_message_zelenka, "interval", hour=8)
    scheduler.add_job(send_other, "interval", hour=8)
    scheduler.start()

app.run(main())