from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from messages import send_message_kiwi, send_message_scrouge, send_message_zelenka, send_other

app = Client("my_account")

scheduler = AsyncIOScheduler()

async def main():

    scheduler.add_job(send_message_scrouge, "cron", hour=12, day="*", args=[app,])
    scheduler.add_job(send_message_kiwi, "interval", hour=10, args=[app,])
    scheduler.add_job(send_message_zelenka, "interval", hour=8, args=[app,])
    scheduler.add_job(send_other, "interval", hour=8, args=[app,])
    scheduler.start()

app.run(main())