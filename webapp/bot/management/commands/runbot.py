from django.core.management.base import BaseCommand
import asyncio

from webapp.bot_main import bot

class Command(BaseCommand):
    help = 'Lunching bot'

    def handle(self, *args, **options):
        print("Bot is running")
        asyncio.run(bot.polling())