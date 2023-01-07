import discord, random, datetime, time, os, art, logging, zipfile
from time import sleep
from discord.ext import commands
from asyncio import sleep as asleep
from discord.ext.commands import has_permissions
from config_eybie import settings, version_info, splashes

print(datetime.datetime.now())

#Необходимые директории для нормальной работы
if not os.path.isdir(f"logs"):
    os.mkdir(f'logs')

if os.path.isfile("logs/latest.log"):
    with zipfile.ZipFile(f'logs/{str(datetime.datetime.now())}.zip', 'w') as log_archive:
        log_archive.write('logs/latest.log')
    os.remove("logs/latest.log")

#Информация о текущей версии бота
eybie_codename = version_info['codename']
eybie_reldate = version_info['rel_date']
eybie_ver = version_info['version']
eybie_distro = version_info['distribution']

#Необходимо для работоспособности основных функций
bot = discord.Bot()
startTime = time.time()

#Сокращения сообщений на все случаи жизни
error_text = "Возникла ошибка при выполнении данной команды :("
message_sent = "Сообщение отправлено ✅"

#Стандартные функции
logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/latest.log"),
        logging.StreamHandler()
    ]
)

def module_loaded(module_name):
    return logging.info(f"Загружен {module_name}")

@bot.event
async def on_ready():
    while True:
        random_splash = random.randint(0, len(splashes) - 1)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"v{eybie_ver} | {splashes[random_splash]}"))
        await asleep(7)

@bot.command(name="devinf", description="Краткая информация для разработчиков")
@has_permissions(administrator=True)
async def devinf(ctx):
    cursession = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    embed = discord.Embed(title="Eybie", description=f"Версия: {eybie_ver} \n Кодовое имя: {eybie_codename} \n Дистрибутив: {eybie_distro} \n Дата релиза: {eybie_reldate} \n Длительность текущей сессии: {cursession}", colour=0xFFE933)
    embed.add_field(name="Список сплешей", value=f"{splashes}", inline=True)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.info(f"Использование команды: /devinf пользователем {ctx.author.name}, с id: {ctx.author.id}")

@devinf.error
async def devinf_error(ctx, error):
    embed = discord.Embed(title=error_text, description=" ", colour=0xFFE933)
    await ctx.response.send_message(embed=embed, ephemeral=True)
    logging.error(f"Возникла ошибка при использовании команды: /devinf пользователем {ctx.author.name}, с id: {ctx.author.id}")

#Скрипты при запуске
art.tprint(f"|Eybie  v{eybie_ver}|") #Поставил два пробела из-за слишком малого расстояния между символами в art.tprint
print("============================================================\n")
sleep(3)
logging.info("Запуск модулей...")