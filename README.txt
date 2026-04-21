SECRET ROOM TELEGRAM BOT — Railway Deploy
==========================================

ИНСТРУКЦИЯ ПО ДЕПЛОЮ НА RAILWAY:

1) Зарегистрируйся на https://railway.app

2) Нажми "New Project" → "Deploy from GitHub repo"
   (или "Empty Project" → потом загрузи файлы)

3) Загрузи все файлы из этого архива в репозиторий

4) Railway автоматически:
   - Определит Python проект (через nixpacks.toml)
   - Установит зависимости из requirements.txt
   - Запустит бота командой: python bot.py

5) Готово! Бот будет работать 24/7 на Railway

ВАЖНО:
- Токен бота уже прописан внутри bot.py
- Если хочешь скрыть токен, можно вынести в Environment Variables
  и читать через os.environ.get("BOT_TOKEN")

ФАЙЛЫ В АРХИВЕ:
- bot.py — основной код бота
- logo.jpg — логотип Secret Room
- requirements.txt — Python зависимости
- runtime.txt — версия Python
- Procfile — команда запуска (для Heroku/Railway)
- railway.json — конфиг Railway
- nixpacks.toml — конфиг сборки

КОМАНДЫ БОТА:
- /start — главное меню
- /menu — главное меню
- /Violetta, /Alina, /Adriana — анкеты моделей
- /stats — статистика (только админы)
- /broadcast Текст — рассылка (только админы)

КУРАТОР: @mar1hkaaa
