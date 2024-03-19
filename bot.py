import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import load_config, Config


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
                                               u'[%(asctime)s] - %(name)s - %(message)s')


async def main():
    logger.info('Starting Bot')

    config: Config = load_config()
    memory: MemoryStorage = MemoryStorage()

    bot: Bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=memory)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")