from modules.api import *

from modules.ey_msg import *

logging.info("Eybie запущен")

if settings['token'] == "TOKEN" or "":
    logging.error("Ууупс... вы забыли добавить токен для Eybie. Получить токен можно тут: https://discord.com/developers/applications, токен вписывается в config_eybie.py")
else:
    bot.run(settings['token'])

if KeyboardInterrupt:
    logging.info("Выключение бота...")