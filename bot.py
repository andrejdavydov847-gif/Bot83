import telebot
from telebot import types
import logging
import datetime
import os

TOKEN = "8748706788:AAG2DTx3S_sGvTvqgB3O-OjISmDy_OA_Reg"
ADMINS = [8166720202, 8574406480]
CHANNEL_LINK = "https://t.me/SECREM_ROOM_MODEL0"
PAYMENT_LINK = "https://dalink.to/secret_room_"
CURATOR_USERNAME = "mar1hkaaa"
CURATOR_LINK = f"https://t.me/{CURATOR_USERNAME}"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

user_stats = {}
user_last_msg = {}

import json as _json
import os as _os

CURATED_REVIEWS = [
    {"name": "Андрей", "model": "Violetta", "rating": 5, "date": "12.04.2026", "text": "Шикарный вечер! Виолетта — настоящая богиня, всё прошло на высшем уровне. Девочка реально как на фото, никакого обмана. Обязательно вернусь!"},
    {"name": "Максим", "model": "Alina", "rating": 5, "date": "11.04.2026", "text": "Алина — это что-то нереальное. Нежная, ласковая, всё умеет. Минет от души, без презерватива по доп. договорённости. Кончил два раза за час, парни, рекомендую!"},
    {"name": "Дмитрий", "model": "Adriana", "rating": 5, "date": "10.04.2026", "text": "Адриана просто огонь! Сделала такой страстный массаж, что я забыл как меня зовут. Грудь натуральная, попа упругая. Бери ночь — не пожалеешь."},
    {"name": "Сергей", "model": "Violetta", "rating": 5, "date": "09.04.2026", "text": "Заказывал Виолетту на 2 часа. Куратор @mar1hkaaa всё чётко организовал, адрес выдал моментально после оплаты. Девочка приехала вовремя, всё прошло как в сказке."},
    {"name": "Алексей", "model": "Alina", "rating": 5, "date": "08.04.2026", "text": "Алина — лучшая блондиночка в Москве! Сделала глубокий минет с заглотом, потом классика в трёх позах. За 2500 это просто подарок!"},
    {"name": "Игорь", "model": "Adriana", "rating": 5, "date": "07.04.2026", "text": "Брал Адриану в БДСМ-сценарии. Парни, она знает своё дело. Доминировала меня по полной, чувствую себя обновлённым человеком. 10/10!"},
    {"name": "Виктор", "model": "Violetta", "rating": 5, "date": "06.04.2026", "text": "Сервис на высшем уровне. Виолетта приехала с приятным сюрпризом — белыми чулками и кружевным бельём. Всю ночь не давала спать, утром уехала с улыбкой."},
    {"name": "Роман", "model": "Alina", "rating": 4, "date": "05.04.2026", "text": "Алинка — милая девочка. Чуть опоздала (минут на 15), но компенсировала отличным сервисом. Грудь маленькая, но натуральная и очень чувствительная."},
    {"name": "Никита", "model": "Adriana", "rating": 5, "date": "04.04.2026", "text": "Заказал Адриану в дуэте с Виолеттой. Это была лучшая ночь в моей жизни. Девочки работали в команде, ласкали друг друга и меня. Незабываемо!"},
    {"name": "Артём", "model": "Violetta", "rating": 5, "date": "03.04.2026", "text": "Отдельное спасибо куратору @mar1hkaaa — всё четко, без лишних вопросов. Виолетта подъехала через 40 минут после оплаты. Час пролетел как 5 минут."},
    {"name": "Кирилл", "model": "Alina", "rating": 5, "date": "02.04.2026", "text": "Алина — нежнейшее создание. Сделала тантрический массаж с эротической составляющей, потом классический секс в миссионерской и наезднице. Кайф!"},
    {"name": "Михаил", "model": "Adriana", "rating": 5, "date": "01.04.2026", "text": "Адриана — секс-машина. Энергии у неё хоть отбавляй. За ночь успели всё: оральные ласки, классика, анал (доп. услуга), даже игрушки попробовали. Жаль только утро пришло."},
    {"name": "Павел", "model": "Violetta", "rating": 5, "date": "31.03.2026", "text": "Премиум сервис за адекватные деньги. Виолетта — образованная и интересная девушка, с ней приятно даже просто поговорить. Ну а в постели — отдельная история."},
    {"name": "Денис", "model": "Alina", "rating": 5, "date": "30.03.2026", "text": "Алинка пришла в школьной форме по моей просьбе. Отыграла роль на отлично, потом устроила такой минет, что я кончил за пару минут. Ребята, не упустите!"},
    {"name": "Олег", "model": "Adriana", "rating": 5, "date": "29.03.2026", "text": "Брал Адриану на корпоратив (выезд в загородный дом). Девочка отработала идеально, развлекла всех гостей, потом задержалась со мной до утра. Класс!"},
    {"name": "Евгений", "model": "Violetta", "rating": 5, "date": "28.03.2026", "text": "Виолетта — реально элитная модель. Манеры, фигура, умение держать себя — всё на высоте. Секс был страстным и нежным одновременно. Жду новой встречи."},
    {"name": "Антон", "model": "Alina", "rating": 5, "date": "27.03.2026", "text": "Алина — это чистая страсть в маленьком теле. Целовалась взасос, садилась сверху, стонала так, что соседи стучали в стену 😅. Очень рекомендую!"},
    {"name": "Станислав", "model": "Adriana", "rating": 5, "date": "26.03.2026", "text": "Адриана сделала мне сюрприз — приехала в латексе и с плёткой. Я в ступоре стоял первые минуты, потом всё понеслось. Парни, это пушка!"},
    {"name": "Илья", "model": "Violetta", "rating": 4, "date": "25.03.2026", "text": "Хороший сервис, девочка на уровне. Снял на час, всё успели. Единственное — хотелось бы скидку постоянным клиентам, ребята подумайте 😉"},
    {"name": "Геннадий", "model": "Alina", "rating": 5, "date": "24.03.2026", "text": "В свои 50 я уже многое повидал, но Алинка удивила. Молодая, энергичная, без капризов. За свои деньги — лучшее предложение в Москве."},
    {"name": "Тимур", "model": "Adriana", "rating": 5, "date": "23.03.2026", "text": "Адриана — королева оральных ласк. Делает это так, как будто всю жизнь только этим и занималась. Кончил себе на грудь, она потом весь язычком собрала 🔥"},
    {"name": "Руслан", "model": "Violetta", "rating": 5, "date": "22.03.2026", "text": "Чистая, ухоженная, пахнет шикарно. Виолетта — это эстетика во всём. Секс с ней — как занятие искусством. Спасибо Secret Room за идеальный вечер!"},
    {"name": "Владимир", "model": "Alina", "rating": 5, "date": "21.03.2026", "text": "Брал Алину второй раз. Девочка узнала меня, обняла как старого знакомого. Сразу перешли к делу. Минет от души, потом классика и душ вдвоём. Идеал!"},
    {"name": "Александр", "model": "Adriana", "rating": 5, "date": "20.03.2026", "text": "Адриана сделала ночь незабываемой. Я даже не думал что можно столько раз кончить за одну ночь. Ребята, не экономьте — берите ночь!"},
    {"name": "Григорий", "model": "Violetta", "rating": 5, "date": "19.03.2026", "text": "Виолетта приехала с бутылочкой шампанского — маленький приятный жест. Вечер прошёл романтично и страстно. Это не просто эскорт, это искусство!"},
]

# Load extra reviews from JSON (2000+ reviews)
REVIEWS = list(CURATED_REVIEWS)
try:
    _reviews_path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "reviews.json")
    if _os.path.exists(_reviews_path):
        with open(_reviews_path, "r", encoding="utf-8") as _f:
            _extra = _json.load(_f)
            REVIEWS.extend(_extra)
        logger.info(f"Loaded {len(_extra)} extra reviews from JSON. Total: {len(REVIEWS)}")
except Exception as _e:
    logger.error(f"Failed to load reviews.json: {_e}")

BASE_DIR = os.path.dirname(__file__)
LOGO_PATH = os.path.join(BASE_DIR, "logo.jpg")

MODELS = {
      "alina": {
          "name": "Алина",
          "emoji": "🦋",
          "age": 24,
          "height": "—",
          "weight": "—",
          "bust": "—",
          "hair": "—",
          "eyes": "—",
          "city": "Москва",
          "metro": "—",
          "price_hour": "6 000 ₽",
          "price_2hour": "12 000 ₽",
          "price_night": "22 000 ₽",
          "rating": "⭐️⭐️⭐️⭐️⭐️ 5.0",
          "reviews": 187,
          "about": "Очаровательная, ухоженная и невероятно женственная девушка с утончёнными манерами. Умею создавать атмосферу лёгкости, флирта и настоящего удовольствия от общения. Со мной вы забудете о суете и насладитесь приятной компанией и красивым вечером.",
          "services": ["💋 Обычный секс", "🔥 Грубый секс", "🍑 Анал", "🎁 С игрушками", "🛁 Массаж с интимом", "💦 Минет"],
          "status": "✅ Свободна сейчас",
          "photo": "model_alina.jpg",
      },
      "violetta": {
          "name": "Виолетта",
          "emoji": "🦋",
          "age": 19,
          "height": "—",
          "weight": "—",
          "bust": "—",
          "hair": "—",
          "eyes": "—",
          "city": "Москва",
          "metro": "—",
          "price_hour": "6 300 ₽",
          "price_2hour": "11 100 ₽",
          "price_night": "17 460 ₽",
          "rating": "⭐️⭐️⭐️⭐️⭐️ 4.9",
          "reviews": 142,
          "about": "Приглашаю отдаться чувствам, а также окунуться в мир похоти и разврата ❤️",
          "services": ["💋 МБР", "💦 Окончание на лицо", "✋ Фингеринг"],
          "status": "✅ Свободна сейчас",
          "photo": "model_violetta.jpg",
      },
      "adriana": {
          "name": "Адриана",
          "emoji": "🦋",
          "age": 24,
          "height": "—",
          "weight": "—",
          "bust": "—",
          "hair": "—",
          "eyes": "—",
          "city": "Москва",
          "metro": "—",
          "price_hour": "6 300 ₽",
          "price_2hour": "11 900 ₽",
          "price_night": "38 000 ₽",
          "rating": "⭐️⭐️⭐️⭐️⭐️ 5.0",
          "reviews": 96,
          "about": "Новенькая девочка в нашем агентстве, но уже успела получить положительные отзывы о работе. Готова подарить тебе незабываемые ощущения.",
          "services": ["💦 Минет в презервативе", "💋 Окончание на лицо", "👅 Кунилингус"],
          "status": "✅ Свободна сейчас",
          "photo": "model_adriana.jpg",
      },
      "marisha": {
          "name": "Мариша",
          "emoji": "🍑",
          "age": 25,
          "height": "—",
          "weight": "—",
          "bust": "—",
          "hair": "—",
          "eyes": "—",
          "city": "Москва",
          "metro": "—",
          "price_hour": "4 000 ₽",
          "price_2hour": "—",
          "price_night": "15 400 ₽",
          "rating": "⭐️⭐️⭐️⭐️⭐️ 4.8",
          "reviews": 78,
          "about": "Девчонка не из робких, люблю себя показать. С кайфом разминаю свои дырочки и даже тащусь от агрегата в попке 😊",
          "services": ["🍑 Анал", "💋 МБР", "🎁 Секс-игрушки", "👅 Анилингус"],
          "status": "✅ Свободна сейчас",
          "photo": "model_marisha.jpg",
      },
      "lenochka": {
          "name": "Леночка",
          "emoji": "🐱",
          "age": 23,
          "height": "—",
          "weight": "—",
          "bust": "—",
          "hair": "—",
          "eyes": "—",
          "city": "Москва",
          "metro": "—",
          "price_hour": "5 000 ₽",
          "price_2hour": "—",
          "price_night": "21 200 ₽",
          "rating": "⭐️⭐️⭐️⭐️⭐️ 4.9",
          "reviews": 64,
          "about": "Молоденькая кошечка хочет приехать к тебе в гости и показать всё, что умеет. Уже сегодня ночью 🥰",
          "services": ["💋 МБР", "💦 Окончание на грудь", "✋ Фингеринг"],
          "status": "✅ Свободна сейчас",
          "photo": "model_lenochka.jpg",
      }
  }


def get_age_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ Мне есть 18 лет — Войти", callback_data="confirm_age"))
    return markup


def get_main_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💎 Каталог моделей", callback_data="models"),
    )
    markup.add(
        types.InlineKeyboardButton("⭐️ Отзывы клиентов", callback_data="review_0"),
    )
    markup.add(
        types.InlineKeyboardButton("🛒 Как заказать", callback_data="order"),
        types.InlineKeyboardButton("💳 Оплата", callback_data="payment"),
    )
    markup.add(
        types.InlineKeyboardButton("📞 Куратор", url=CURATOR_LINK),
        types.InlineKeyboardButton("📸 Канал", url=CHANNEL_LINK),
    )
    markup.add(
        types.InlineKeyboardButton("ℹ️ О нас", callback_data="about"),
        types.InlineKeyboardButton("📋 Правила", callback_data="rules"),
    )
    return markup


def get_reviews_markup(index):
    total = len(REVIEWS)
    prev_idx = (index - 1) % total
    next_idx = (index + 1) % total
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
        types.InlineKeyboardButton("◀️", callback_data=f"review_{prev_idx}"),
        types.InlineKeyboardButton(f"{index + 1} / {total}", callback_data="review_noop"),
        types.InlineKeyboardButton("▶️", callback_data=f"review_{next_idx}"),
    )
    markup.add(
        types.InlineKeyboardButton("💎 Заказать модель", callback_data="models"),
    )
    markup.add(
        types.InlineKeyboardButton(f"📞 Куратор @{CURATOR_USERNAME}", url=CURATOR_LINK),
        types.InlineKeyboardButton("⬅️ В меню", callback_data="back"),
    )
    return markup


def build_review_text(index):
    r = REVIEWS[index]
    stars = "⭐️" * r["rating"]
    text = (
        f"⭐️ <b>ОТЗЫВЫ КЛИЕНТОВ SECRET ROOM</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 <b>{r['name']}</b>\n"
        f"💎 <b>Модель:</b> {r['model']}\n"
        f"📅 <b>Дата:</b> {r['date']}\n"
        f"📊 <b>Оценка:</b> {stars}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💬 <i>«{r['text']}»</i>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📝 <b>Отзыв {index + 1} из {len(REVIEWS)}</b>\n"
        f"⭐️ <b>Средний рейтинг:</b> 4.9 / 5.0"
    )
    return text


def get_models_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for key, m in MODELS.items():
        markup.add(
            types.InlineKeyboardButton(
                f"{m['emoji']} {m['name']} • {m['age']} лет • {m['price_hour']}",
                callback_data=f"model_{key}"
            )
        )
    markup.add(
        types.InlineKeyboardButton("📸 Все модели в канале", url=CHANNEL_LINK),
        types.InlineKeyboardButton("⬅️ Главное меню", callback_data="back"),
    )
    return markup


def get_model_action_markup(model_key):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💳 Заказать и оплатить", callback_data=f"book_{model_key}"),
    )
    markup.add(
        types.InlineKeyboardButton("📸 Больше фото в канале", url=CHANNEL_LINK),
        types.InlineKeyboardButton(f"📞 Написать куратору @{CURATOR_USERNAME}", url=CURATOR_LINK),
    )
    markup.add(
        types.InlineKeyboardButton("⬅️ К моделям", callback_data="models"),
        types.InlineKeyboardButton("🏠 Меню", callback_data="back"),
    )
    return markup


def get_book_markup(model_key):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💳 Оплатить через Donation Alerts", url=PAYMENT_LINK),
        types.InlineKeyboardButton(f"📞 Написать куратору @{CURATOR_USERNAME}", url=CURATOR_LINK),
        types.InlineKeyboardButton("📸 Перейти в канал", url=CHANNEL_LINK),
    )
    markup.add(
        types.InlineKeyboardButton("⬅️ К моделям", callback_data="models"),
        types.InlineKeyboardButton("🏠 Меню", callback_data="back"),
    )
    return markup


def get_payment_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💳 Оплатить заказ", url=PAYMENT_LINK),
        types.InlineKeyboardButton(f"📞 Куратор @{CURATOR_USERNAME}", url=CURATOR_LINK),
        types.InlineKeyboardButton("⬅️ Главное меню", callback_data="back"),
    )
    return markup


def get_back_only_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(f"📞 Куратор @{CURATOR_USERNAME}", url=CURATOR_LINK),
        types.InlineKeyboardButton("⬅️ Главное меню", callback_data="back"),
    )
    return markup


WELCOME_TEXT = (
    "🔐 <b>SECRET ROOM • Премиум-эскорт сервис</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "💎 <b>У нас вы найдёте лучших девочек для интимных встреч.</b>\n\n"
    "🕐 <b>Выдача адресов круглосуточно — через бота или куратора.</b>\n\n"
    "⚠️ <b>Внимательно проверяйте Telegram-адрес куратора, остерегайтесь мошенников. Спасибо, что выбираете нас!</b>\n\n"
    "✨ <b>Хочешь скрасить свой день? Нажимай «Каталог моделей» и выбирай!</b>\n\n"
    f"📞 <b>Куратор:</b> @{CURATOR_USERNAME}"
)

ORDER_TEXT = (
    "🛒 <b>КАК ОФОРМИТЬ ЗАКАЗ</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "1️⃣ <b>Выберите модель</b> в разделе «Каталог моделей»\n"
    "2️⃣ <b>Изучите анкету</b> — фото, цены, услуги\n"
    "3️⃣ <b>Нажмите «Заказать и оплатить»</b>\n"
    "4️⃣ <b>Произведите оплату</b> через Donation Alerts\n"
    f"5️⃣ <b>Куратор @{CURATOR_USERNAME}</b> свяжется в течение 5 минут\n"
    "6️⃣ <b>Получите адрес</b> и наслаждайтесь встречей\n\n"
    "⚡️ <b>Работаем 24/7 — без выходных!</b>\n"
    "🔒 <b>Полная конфиденциальность.</b>"
)

PAYMENT_TEXT = (
    "💳 <b>ОПЛАТА ЗАКАЗА</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "🔐 <b>Безопасная оплата через Donation Alerts</b>\n\n"
    f"👉 <b>{PAYMENT_LINK}</b>\n\n"
    "✅ <b>Способы оплаты:</b>\n"
    "• 💳 Банковские карты (Visa, MasterCard, МИР)\n"
    "• ⚡️ СБП (Система быстрых платежей)\n"
    "• 💰 ЮMoney, QIWI\n"
    "• ₿ Криптовалюта (BTC, USDT, ETH)\n\n"
    f"💎 <b>После оплаты куратор @{CURATOR_USERNAME} свяжется и выдаст адрес!</b>\n\n"
    "🔒 <b>Все платежи защищены и анонимны.</b>"
)

ABOUT_TEXT = (
    "ℹ️ <b>О SECRET ROOM</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "🏆 <b>Премиальный сервис для организации интимных встреч.</b>\n\n"
    "🔒 <b>Полная конфиденциальность</b>\n"
    "⭐ <b>Только проверенные модели</b>\n"
    "🕐 <b>Работаем 24/7 без выходных</b>\n"
    "✅ <b>Гарантия безопасности и анонимности</b>\n"
    "💳 <b>Удобная оплата любым способом</b>\n"
    "📍 <b>Выезд и апартаменты по всей Москве</b>\n"
    "💰 <b>Доступные цены — от 2 500 ₽ за час</b>\n"
    "👯 <b>Возможен заказ дуэтом</b>\n\n"
    "💎 <b>Выбирай лучших — выбирай Secret Room!</b>"
)

RULES_TEXT = (
    "📋 <b>ПРАВИЛА СЕРВИСА</b>\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "1️⃣ <b>Сервис только для совершеннолетних (18+)</b>\n\n"
    "2️⃣ <b>Оплата производится заранее через Donation Alerts</b>\n\n"
    "3️⃣ <b>Адрес выдаётся только после подтверждения оплаты</b>\n\n"
    "4️⃣ <b>Отмена заказа — не позднее чем за 1 час</b>\n\n"
    f"5️⃣ <b>Единственный куратор: @{CURATOR_USERNAME} — мошенники копируют никнеймы!</b>\n\n"
    "6️⃣ <b>Запрещены фото- и видеосъёмка без согласия модели</b>\n\n"
    "7️⃣ <b>Уважительное отношение к моделям обязательно</b>\n\n"
    "8️⃣ <b>Алкоголь и наркотические вещества строго запрещены</b>\n\n"
    "⚠️ <b>Нарушение правил = блокировка без возврата средств!</b>"
)


LESBI_SERVICES = [
    "👅 Глубокий куннилингус до оргазма",
    "💋 Французские поцелуи взасос",
    "🍑 Анилингус (рим-джоб)",
    "✋ Фистинг вагинальный (по согласованию)",
    "🍑 Фистинг анальный (по согласованию)",
    "🎁 Игры со страпоном (актив/пассив)",
    "💦 Сквирт от ласк языком",
    "🔥 Скаут-69 (взаимные оральные ласки)",
    "🪢 Лёгкий BDSM, шибари, верёвки",
    "👯 Лесби-шоу для пары / в дуэте",
    "🎀 Ролевые игры: госпожа/рабыня, школьница/учительница",
    "🛁 Эротический массаж с переходом во влажные ласки",
    "🍓 Игры с фруктами, сливками, льдом",
    "📹 Запись интимного видео для тебя (по договорённости)",
    "💎 Squirting show — обильное сквиртование",
]


def build_model_card(model_key):
    m = MODELS[model_key]
    services_str = "\n".join(m["services"])
    lesbi_str = "\n".join(LESBI_SERVICES)
    text = (
        f"{m['emoji']} <b>{m['name'].upper()}</b> {m['emoji']}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"{m['rating']} <b>({m['reviews']} отзывов)</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🔞 <b>Возраст:</b> {m['age']} лет\n"
        f"📏 <b>Рост:</b> {m['height']}\n"
        f"⚖️ <b>Вес:</b> {m['weight']}\n"
        f"🍑 <b>Грудь:</b> {m['bust']} размер\n"
        f"💇‍♀️ <b>Волосы:</b> {m['hair']}\n"
        f"👁 <b>Глаза:</b> {m['eyes']}\n"
        f"📍 <b>Город:</b> {m['city']}\n"
        f"🚇 <b>Метро:</b> {m['metro']}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💰 <b>1 час:</b> {m['price_hour']}\n"
        f"💰 <b>2 часа:</b> {m['price_2hour']}\n"
        f"🌙 <b>Ночь:</b> {m['price_night']}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🎯 <b>Услуги (мужчинам):</b>\n{services_str}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🚗 <b>ВЫЕЗД:</b> ✅ Москва и МО\n"
        f"🏨 <b>Апартаменты / гостиница / квартира клиента — без проблем</b>\n"
        f"🌆 <b>Выезд за город — обсуждается отдельно (+трансфер)</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"👭 <b>ВЫЕЗД ДЛЯ ДЕВУШЕК / ЛЕСБИ-ВСТРЕЧИ:</b> ✅\n"
        f"<i>Девочки приедут к одной даме или к паре девушек. Полная конфиденциальность, без табу. Можно заказать дуэт двух наших моделей для лесби-шоу или совместного отдыха втроём.</i>\n\n"
        f"🔥 <b>Лесби-услуги (самые развратные):</b>\n{lesbi_str}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"💬 <b>О себе:</b>\n<i>{m['about']}</i>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📊 <b>Статус:</b> {m['status']}"
    )
    return text


def notify_admins(text):
    for admin_id in ADMINS:
        try:
            bot.send_message(admin_id, text, parse_mode="HTML")
        except Exception as e:
            logger.warning(f"Could not notify admin {admin_id}: {e}")


def safe_delete(chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
    except Exception:
        pass


def send_with_photo(chat_id, photo_path, caption, markup, user_id=None):
    try:
        with open(photo_path, "rb") as photo:
            msg = bot.send_photo(chat_id, photo, caption=caption, reply_markup=markup, parse_mode="HTML")
        if user_id:
            user_last_msg[user_id] = msg.message_id
        return msg
    except Exception as e:
        logger.error(f"Failed to send photo {photo_path}: {e}")
        msg = bot.send_message(chat_id, caption, reply_markup=markup, parse_mode="HTML")
        if user_id:
            user_last_msg[user_id] = msg.message_id
        return msg


def send_with_logo(chat_id, caption, markup, user_id=None):
    return send_with_photo(chat_id, LOGO_PATH, caption, markup, user_id)


def send_model_card(chat_id, model_key, user_id=None):
    m = MODELS[model_key]
    caption = build_model_card(model_key)
    photo_file = m.get("photo")
    photo_path = os.path.join(BASE_DIR, photo_file) if photo_file else None
    # Telegram caption limit is 1024 chars — if longer, send photo + separate text
    if photo_path and os.path.exists(photo_path):
        try:
            if len(caption) <= 1024:
                with open(photo_path, "rb") as ph:
                    msg = bot.send_photo(chat_id, ph, caption=caption,
                                         reply_markup=get_model_action_markup(model_key),
                                         parse_mode="HTML")
            else:
                with open(photo_path, "rb") as ph:
                    bot.send_photo(chat_id, ph)
                msg = bot.send_message(chat_id, caption,
                                       reply_markup=get_model_action_markup(model_key),
                                       parse_mode="HTML")
            if user_id:
                user_last_msg[user_id] = msg.message_id
            return msg
        except Exception as e:
            logger.error(f"Failed to send model photo {photo_path}: {e}")
    msg = bot.send_message(
        chat_id, caption,
        reply_markup=get_model_action_markup(model_key),
        parse_mode="HTML"
    )
    if user_id:
        user_last_msg[user_id] = msg.message_id
    return msg


@bot.message_handler(commands=["start"])
def cmd_start(message):
    uid = message.from_user.id
    username = message.from_user.username or "без юзернейма"
    first_name = message.from_user.first_name or "гость"

    is_new = uid not in user_stats
    user_stats[uid] = {
        "joined": datetime.datetime.now().isoformat(),
        "username": username,
        "first_name": first_name,
    }

    if is_new:
        notify_admins(
            f"👤 <b>Новый пользователь!</b>\n"
            f"ID: <code>{uid}</code>\n"
            f"Имя: {first_name}\n"
            f"Username: @{username}"
        )

    logger.info(f"User /start: {uid} (@{username})")

    caption = (
        f"🔐 <b>Добро пожаловать, {first_name}!</b>\n\n"
        "<b>Чтобы пользоваться ботом и делать заказы — подтвердите свой возраст.</b>\n\n"
        "⚠️ <b>Сервис предназначен исключительно для лиц 18+</b>"
    )
    send_with_logo(message.chat.id, caption, get_age_markup(), uid)


@bot.message_handler(commands=["Violetta", "violetta"])
def cmd_violetta(message):
    send_model_card(message.chat.id, "violetta", message.from_user.id)


@bot.message_handler(commands=["Alina", "alina"])
def cmd_alina(message):
    send_model_card(message.chat.id, "alina", message.from_user.id)


@bot.message_handler(commands=["Adriana", "adriana"])
def cmd_adriana(message):
    send_model_card(message.chat.id, "adriana", message.from_user.id)


@bot.message_handler(commands=["Marisha", "marisha"])
def cmd_marisha(message):
    send_model_card(message.chat.id, "marisha", message.from_user.id)


@bot.message_handler(commands=["Lenochka", "lenochka"])
def cmd_lenochka(message):
    send_model_card(message.chat.id, "lenochka", message.from_user.id)


@bot.message_handler(commands=["menu"])
def cmd_menu(message):
    send_with_logo(message.chat.id, WELCOME_TEXT, get_main_markup(), message.from_user.id)


@bot.message_handler(commands=["stats"])
def cmd_stats(message):
    if message.from_user.id not in ADMINS:
        return
    total = len(user_stats)
    text = (
        f"📊 <b>СТАТИСТИКА БОТА</b>\n\n"
        f"👥 <b>Всего пользователей:</b> {total}\n"
        f"🕐 <b>Время запроса:</b> {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}"
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["broadcast"])
def cmd_broadcast(message):
    if message.from_user.id not in ADMINS:
        return
    text = message.text.replace("/broadcast", "", 1).strip()
    if not text:
        bot.send_message(message.chat.id, "<b>Использование: /broadcast Текст сообщения</b>")
        return
    sent = 0
    for uid in list(user_stats.keys()):
        try:
            bot.send_message(uid, f"📢 <b>ОБЪЯВЛЕНИЕ</b>\n\n<b>{text}</b>")
            sent += 1
        except Exception:
            pass
    bot.send_message(message.chat.id, f"<b>✅ Рассылка отправлена: {sent} пользователей</b>")


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        cid = call.message.chat.id
        mid = call.message.message_id
        uid = call.from_user.id

        def replace_with_logo(caption, markup):
            safe_delete(cid, mid)
            send_with_logo(cid, caption, markup, uid)

        def replace_with_model(model_key):
            safe_delete(cid, mid)
            send_model_card(cid, model_key, uid)

        if call.data == "confirm_age":
            replace_with_logo(WELCOME_TEXT, get_main_markup())

        elif call.data == "back":
            replace_with_logo(WELCOME_TEXT, get_main_markup())

        elif call.data == "order":
            replace_with_logo(ORDER_TEXT, get_back_only_markup())

        elif call.data == "payment":
            replace_with_logo(PAYMENT_TEXT, get_payment_markup())

        elif call.data == "about":
            replace_with_logo(ABOUT_TEXT, get_back_only_markup())

        elif call.data == "rules":
            replace_with_logo(RULES_TEXT, get_back_only_markup())

        elif call.data == "review_noop":
            pass

        elif call.data.startswith("review_"):
            try:
                idx = int(call.data.replace("review_", ""))
                idx = idx % len(REVIEWS)
            except ValueError:
                idx = 0
            replace_with_logo(build_review_text(idx), get_reviews_markup(idx))

        elif call.data == "models":
            models_header = (
                "💎 <b>КАТАЛОГ МОДЕЛЕЙ SECRET ROOM</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n\n"
                "✅ <b>Все модели проверены и готовы к встрече!</b>\n"
                "🕐 <b>Работаем круглосуточно</b>\n"
                "💰 <b>Доступные цены — от 2 500 ₽ за час</b>\n\n"
                "<b>Выберите модель для просмотра анкеты:</b>"
            )
            replace_with_logo(models_header, get_models_markup())

        elif call.data.startswith("model_"):
            model_key = call.data.replace("model_", "")
            if model_key in MODELS:
                replace_with_model(model_key)

        elif call.data.startswith("book_"):
            model_key = call.data.replace("book_", "")
            model = MODELS.get(model_key, {})
            model_name = model.get("name", "модель")
            price_hour = model.get("price_hour", "—")
            book_text = (
                f"💳 <b>ЗАКАЗ — {model_name}</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n\n"
                f"✅ <b>Вы выбрали {model_name}!</b>\n"
                f"💰 <b>Стоимость от {price_hour} за час</b>\n\n"
                "📋 <b>Что делать дальше:</b>\n"
                "1️⃣ Нажмите «Оплатить через Donation Alerts»\n"
                "2️⃣ Произведите оплату удобным способом\n"
                f"3️⃣ Куратор @{CURATOR_USERNAME} свяжется в течение 5 минут\n"
                "4️⃣ Получите адрес и наслаждайтесь встречей\n\n"
                "🔒 <b>Все платежи защищены и анонимны!</b>\n"
                "⚡️ <b>Среднее время ответа куратора: 5 минут</b>"
            )
            name = call.from_user.first_name or ""
            username = call.from_user.username or "нет"
            notify_admins(
                f"🛒 <b>Новый заказ!</b>\n"
                f"Модель: <b>{model_name}</b>\n"
                f"От: {name} (@{username})\n"
                f"ID: <code>{uid}</code>"
            )
            replace_with_logo(book_text, get_book_markup(model_key))

        bot.answer_callback_query(call.id)

    except Exception as e:
        logger.error(f"Callback error: {e}")
        try:
            bot.answer_callback_query(call.id, text="Попробуйте снова")
        except Exception:
            pass


if __name__ == "__main__":
    logger.info("Secret Room Bot started...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
