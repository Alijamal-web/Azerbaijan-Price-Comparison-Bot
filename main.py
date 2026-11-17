import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8627482803:AAHw6z9A7i2q_n_WfRsLrJovYmkQoYGCf7I"
bot = telebot.TeleBot(TOKEN)

products = {
    "iphone 17 pro": [
        {"shop": "Kontakt Home", "price": 3419, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 4259, "link": "https://www.bakuelectronics.az"},
        {"shop": "Irshad", "price": 3079, "link": "https://irshad.az"}
    ],
    
    "hp victus": [
        {"shop": "Kontakt Home", "price": 1899, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1849, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1869, "link": "https://irshad.az"}
    ],

    "lenovo legion 5": [
        {"shop": "Kontakt Home", "price": 2599, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2499, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2549, "link": "https://irshad.az"}
    ],

    "asus rog strix": [
        {"shop": "Kontakt Home", "price": 3199, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 3099, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 3149, "link": "https://irshad.az"}
    ],

    "macbook pro": [
        {"shop": "Kontakt Home", "price": 3499, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 3399, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 3449, "link": "https://irshad.az"}
    ],

    "acer nitro 5": [
        {"shop": "Kontakt Home", "price": 1999, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1949, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1970, "link": "https://irshad.az"}
    ],

    "dell g15": [
        {"shop": "Kontakt Home", "price": 2299, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2249, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2269, "link": "https://irshad.az"}
    ],

    "msi katana": [
        {"shop": "Kontakt Home", "price": 2699, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2649, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2669, "link": "https://irshad.az"}
    ],

    "asus tuf gaming": [
        {"shop": "Kontakt Home", "price": 2199, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2149, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2169, "link": "https://irshad.az"}
    ],

    "razer blade 15": [
        {"shop": "Kontakt Home", "price": 4299, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 4199, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 4249, "link": "https://irshad.az"}
    ],

    "hp omen": [
        {"shop": "Kontakt Home", "price": 2899, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2849, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2869, "link": "https://irshad.az"}
    ],

    "iphone 15": [
        {"shop": "Kontakt Home", "price": 1599, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1549, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1620, "link": "https://irshad.az"}
    ],

    "samsung s24": [
        {"shop": "Kontakt Home", "price": 1899, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1849, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1799, "link": "https://irshad.az"}
    ],

    "iphone 14": [
        {"shop": "Kontakt Home", "price": 1399, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1349, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1379, "link": "https://irshad.az"}
    ],

    "xiaomi 14": [
        {"shop": "Kontakt Home", "price": 1199, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1149, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1169, "link": "https://irshad.az"}
    ],

    "google pixel 8": [
        {"shop": "Kontakt Home", "price": 1499, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1449, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1469, "link": "https://irshad.az"}
    ],

    "oneplus 12": [
        {"shop": "Kontakt Home", "price": 1299, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1249, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1269, "link": "https://irshad.az"}
    ],

    "huawei pura 70": [
        {"shop": "Kontakt Home", "price": 1699, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1649, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1669, "link": "https://irshad.az"}
    ],

    "nothing phone 2": [
        {"shop": "Kontakt Home", "price": 1099, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1049, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1069, "link": "https://irshad.az"}
    ],

    "realme gt": [
        {"shop": "Kontakt Home", "price": 999, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 949, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 969, "link": "https://irshad.az"}
    ],

    "sony xperia 1": [
        {"shop": "Kontakt Home", "price": 1799, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1749, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1769, "link": "https://irshad.az"}
    ],
    "ipad air": [
        {"shop": "Kontakt Home", "price": 1399, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1349, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1369, "link": "https://irshad.az"}
    ],

    "ipad pro": [
        {"shop": "Kontakt Home", "price": 2199, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2149, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2169, "link": "https://irshad.az"}
    ],

    "samsung tab s9": [
        {"shop": "Kontakt Home", "price": 1599, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1549, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1569, "link": "https://irshad.az"}
    ],

    "xiaomi pad 6": [
        {"shop": "Kontakt Home", "price": 899, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 849, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 869, "link": "https://irshad.az"}
    ],

    "lenovo tab p12": [
        {"shop": "Kontakt Home", "price": 799, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 749, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 769, "link": "https://irshad.az"}
    ],

    "huawei matepad": [
        {"shop": "Kontakt Home", "price": 999, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 949, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 969, "link": "https://irshad.az"}
    ],

    "surface pro 9": [
        {"shop": "Kontakt Home", "price": 2499, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 2449, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 2469, "link": "https://irshad.az"}
    ],

    "realme pad": [
        {"shop": "Kontakt Home", "price": 699, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 649, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 669, "link": "https://irshad.az"}
    ],

    "oppo pad 2": [
        {"shop": "Kontakt Home", "price": 1099, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 1049, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 1069, "link": "https://irshad.az"}
    ],
    "airpods pro": [
        {"shop": "Kontakt Home", "price": 599, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 579, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 589, "link": "https://irshad.az"}
    ],

    "sony wh1000xm5": [
        {"shop": "Kontakt Home", "price": 799, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 769, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 779, "link": "https://irshad.az"}
    ],

    "jbl tune 770": [
        {"shop": "Kontakt Home", "price": 299, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 279, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 289, "link": "https://irshad.az"}
    ],

    "beats studio": [
        {"shop": "Kontakt Home", "price": 699, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 669, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 679, "link": "https://irshad.az"}
    ],

    "razer blackshark": [
        {"shop": "Kontakt Home", "price": 399, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 379, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 389, "link": "https://irshad.az"}
    ],

    "hyperx cloud": [
        {"shop": "Kontakt Home", "price": 349, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 329, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 339, "link": "https://irshad.az"}
    ],

    "logitech g733": [
        {"shop": "Kontakt Home", "price": 449, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 429, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 439, "link": "https://irshad.az"}
    ],

    "steelseries arctis": [
        {"shop": "Kontakt Home", "price": 499, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 479, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 489, "link": "https://irshad.az"}
    ],

    "anker soundcore": [
        {"shop": "Kontakt Home", "price": 199, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 179, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 189, "link": "https://irshad.az"}
    ],

    "marshall major iv": [
        {"shop": "Kontakt Home", "price": 549, "link": "https://kontakt.az"},
        {"shop": "Baku Electronics", "price": 529, "link": "https://bakuelectronics.az"},
        {"shop": "Irshad", "price": 539, "link": "https://irshad.az"}
    ]
}

categories = {
    "computer": [
        "hp victus",
        "lenovo legion 5",
        "asus rog strix",
        "macbook pro",
        "acer nitro 5",
        "dell g15",
        "msi katana",
        "asus tuf gaming",
        "razer blade 15",
        "hp omen"
    ],

    "phone": [
    "iphone 15",
    "samsung s24",
    "iphone 14",
    "xiaomi 14",
    "google pixel 8",
    "oneplus 12",
    "huawei pura 70",
    "nothing phone 2",
    "realme gt",
    "sony xperia 1",
    "iphone 17 pro"

    ],  
    "tablet": [
        "ipad air",
        "ipad pro",
        "samsung tab s9",
        "xiaomi pad 6",
        "lenovo tab p12",
        "huawei matepad",
        "surface pro 9",
        "amazon fire hd",
        "realme pad",
        "oppo pad 2"
    ],

    "headphones": [
        "airpods pro",
        "sony wh1000xm5",
        "jbl tune 770",
        "beats studio",
        "razer blackshark",
        "hyperx cloud",
        "logitech g733",
        "steelseries arctis",
        "anker soundcore",
        "marshall major iv"
    ]
}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hello!\n\nSelect a category:\n\ncomputer\nphone\ntablet\nheadphones"
    )


@bot.message_handler(func=lambda message: True)
def show_category(message):
    query = message.text.lower()

    if query not in categories:
        bot.send_message(
            message.chat.id,
            "There is no such category.\nEnter: Computer, Phone, Tablet or Headphones"
        )
        return

    keyboard = InlineKeyboardMarkup()

    for product in categories[query]:
        button = InlineKeyboardButton(
            text=product.title(),
            callback_data=product
        )
        keyboard.add(button)

    bot.send_message(
        message.chat.id,
        "Select a product:",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def show_prices(call):
    product_name = call.data
    offers = products[product_name]

    best_offer = min(offers, key=lambda x: x["price"])

    text = f"Цены на {product_name.title()}:\n\n"

    for offer in offers:
        text += f"{offer['shop']}\n"
        text += f"Price: {offer['price']} AZN\n"
        text += f"Link: {offer['link']}\n\n"

    text += (
        f"Best option:\n"
        f"{best_offer['shop']} — {best_offer['price']} AZN"
    )

    bot.send_message(call.message.chat.id, text)


bot.polling()
