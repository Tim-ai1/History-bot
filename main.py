import telebot
from telebot import types
import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup
from random import choice
from dotenv import load_dotenv
import os


load_dotenv()
bot = telebot.TeleBot(token=os.getenv("BOT_TOKEN"))


questions = {
    'ancient': [
        {'question': 'Какая древняя цивилизация построила пирамиды в Гизе?',
         'answers': ['Древняя Греция', 'Древний Египет', 'Древний Рим', 'Месопотамия'],
         'right_answer': 2,
         'url': 'https://ethnomir.ru/upload/medialibrary/292/giza.jpg'},
        {'question': 'Кто был первым императором Древнего Рима?',
         'answers': ['Юлий Цезарь', 'Октавиан Август', 'Нерон', 'Марк Аврелий'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Какое из этих чудес света древнего мира сохранилось до наших дней?',
         'answers': ['Висячие сады Семирамиды', 'Колосс Родосский', 'Пирамида Хеопса',
                     'Александрийский маяк'],
         'right_answer': 3,
         'url': ''},
        {'question': 'Какой древний город был разрушен в результате извержения вулкана Везувий в 79 году н.э.?',
         'answers': ['Афины', 'Помпеи', 'Карфаген', 'Вавилон'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Кто был автором "Илиады" и "Одиссеи"?',
         'answers': ['Софокл', 'Гомер', 'Геродот', 'Платон'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Какой материал использовали древние египтяне для письма?',
         'answers': ['Пергамент', 'Глиняные таблички', 'Бамбуковые дощечки', 'Папирус'],
         'right_answer': 4,
         'url': 'https://avatars.mds.yandex.net/i?id=20b986d86ed05d9a5faa290f0521bcdd_l-5283109-images-thumbs&n=13'},
        {'question': 'Кто был последним фараоном Древнего Египта перед завоеванием Римом?',
         'answers': ['Тутмос III', 'Рамзес II', 'Клеопатра VII', 'Эхнатон'],
         'right_answer': 3,
         'url': ''},
        {'question': 'Кто был знаменитым правителем Вавилона, создавшим свод законов "Око за око"?',
         'answers': ['Навуходоносор II', 'Хаммурапи', 'Саргон Великий', 'Ашшурбанапал'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Какое государство считается первым в истории человечества?',
         'answers': ['Древний Египет', 'Шумер', 'Древний Китай', 'Древняя Греция'],
         'right_answer': 2,
         'url': ''},
        {'question': 'В какой стране возникла философия конфуцианства?',
         'answers': ['Индия', 'Персия', 'Китай', 'Япония'],
         'right_answer': 3,
         'url': 'https://get.pxhere.com/photo/monument-statue-red-monk-asia-sculpture-art-figure-gold-temple-culture-china-stature-priest-stone-figure-confucius-temple-complex-buddah-666414.jpg'}
    ],
    'middle': [
        {'question': 'Какой период времени охватывает эпоха Средневековья?',
         'answers': ['III–X века', 'X–XVIII века', 'V–XV века', 'I–X века'],
         'right_answer': 3,
         'url': ''},
        {'question': 'Какое событие считается началом Средневековья?',
         'answers': ['Падение Римской империи', 'Крестовые походы', 'Великое переселение народов',
                     'Открытие Америки'],
         'right_answer': 1,
         'url': ''},
        {'question': 'Кто был королём франков, коронованным императором в 800 году?',
         'answers': ['Ричард Львиное Сердце', 'Карл Великий', 'Вильгельм Завоеватель', 'Людовик IX'],
         'right_answer': 2,
         'url': 'https://images-bonnier.imgix.net/files/his/production/2020/12/01122946/Danevirke_Karl-den-Store.jpg?auto=compress,format&w=1024&fit=crop&crop'},
        {'question': 'Как называлась эпидемия, унёсшая жизни трети населения Европы в XIV веке?',
         'answers': ['Испанка', 'Оспа', 'Чёрная смерть', 'Холера'],
         'right_answer': 3,
         'url': ''},
        {'question': 'Какое сооружение было символом могущества средневековых феодалов?',
         'answers': ['Собор', 'Монастырь', 'Ратуша', 'Замок'],
         'right_answer': 4,
         'url': ''},
        {'question': 'Какое государство было главным противником Византии в Средние века?',
         'answers': ['Священная Римская империя', 'Османская империя', 'Персидская империя', 'Арабский халифат'],
         'right_answer': 2,
         'url': 'https://i.pinimg.com/736x/ec/7b/a1/ec7ba1306ea53db3741024863d8b42ca.jpg'},
        {
            'question': 'Кто возглавил первую успешную экспедицию из Европы в Индию морским путём?',
            'answers': ['Христофор Колумб', 'Фернан Магеллан', 'Васко да Гама', 'Марко Поло'],
            'right_answer': 3,
            'url': 'https://avatars.dzeninfra.ru/get-zen_doc/1640172/pub_6375fd1ed0e533762b581229_637600f46f26361dd672c495/scale_1200'
        },
        {
            'question': 'Кто был королём рыцарей Круглого стола в английских легендах?',
            'answers': ['Ричард Львиное Сердце', 'Король Артур', 'Карл Великий', 'Вильгельм Завоеватель'],
            'right_answer': 2,
         'url': ''
        },
        {
            'question': 'Как назывались воины в доспехах, служившие сеньорам?',
            'answers': ['Викинги', 'Рыцари', 'Самураи', 'Легионеры'],
            'right_answer': 2,
         'url': ''
        },
        {
            'question': 'Какой город был столицей Византийской империи?',
            'answers': ['Рим', 'Афины', 'Константинополь', 'Иерусалим'],
            'right_answer': 3,
         'url': ''
        }],
    'new': [
        {'question': 'Какое событие считается началом эпохи Нового времени?',
         'answers': ['Великие географические открытия', 'Промышленная революция', 'Реформация',
                     'Независимость США'],
         'right_answer': 1,
         'url': ''},
        {'question': 'Кто был первым президентом США?',
         'answers': ['Томас Джефферсон', 'Джордж Вашингтон', 'Авраам Линкольн', 'Бенджамин Франклин'],
         'right_answer': 2,
         'url': 'https://avatars.mds.yandex.net/i?id=577aab1ff7355ea61fc3a2fd180a8e38_l-5234706-images-thumbs&n=13'},
        {'question': 'Какая революция положила начало промышленному перевороту в XVIII веке?',
         'answers': ['Американская революция', 'Французская революция', 'Промышленная революция',
                     'Научная революция'],
         'right_answer': 3,
         'url': ''},
        {'question': 'Кто написал "Декларацию независимости США"?',
         'answers': ['Джордж Вашингтон', 'Томас Джефферсон', 'Бенджамин Франклин', 'Джон Адамс'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Какое изобретение Джеймса Уатта стало символом промышленной революции?',
         'answers': ['Паровой двигатель', 'Ткацкий станок', 'Телеграф', 'Локомотив'],
         'right_answer': 1,
         'url': ''},
        {
            'question': 'Какая революция произошла во Франции в конце XVIII века?',
            'answers': ['Промышленная', 'Научная', 'Великая французская', 'Славная'],
            'right_answer': 3,
         'url': 'https://assets.sutori.com/user-uploads/image/8ceed41c-4a82-4571-b603-38ff647d079f/eee07c14005c30b0526091c6abb52d45.jpeg'
        },
        {
            'question': 'Какая страна первой начала промышленную революцию?',
            'answers': ['Франция', 'Германия', 'Англия', 'США'],
            'right_answer': 3,
         'url': ''
        },
        {
            'question': 'Как называлась эпоха возрождения науки и искусства в Европе?',
            'answers': ['Просвещение', 'Ренессанс', 'Реформация', 'Барокко'],
            'right_answer': 2,
         'url': ''
        },
        {
            'question': 'В каком году была принята Декларация независимости США?',
            'answers': ['1776', '1789', '1812', '1492'],
            'right_answer': 1,
         'url': 'https://i.pinimg.com/736x/d3/75/f6/d375f6385846ba3abeb950faa52bdb8f.jpg'
        },
        {
            'question': 'Какой город стал столицей России при Петре I?',
            'answers': ['Москва', 'Киев', 'Санкт-Петербург', 'Новгород'],
            'right_answer': 3,
         'url': ''
        }
    ],
    'modern': [
        {
            'question': 'Какое событие считается началом Первой мировой войны?',
            'answers': ['Убийство эрцгерцога Франца Фердинанда', 'Бомбардировка Перл-Харбора',
                        'Октябрьская революция',
                        'Подписание Версальского договора'],
            'right_answer': 1,
         'url': ''},
        {'question': 'Кто был первым человеком, побывавшим в космосе?',
         'answers': ['Нил Армстронг', 'Алан Шепард', 'Валентина Терешкова', 'Юрий Гагарин'],
         'right_answer': 4,
         'url': ''},
        {'question': 'В каком году произошло падение Берлинской стены?',
         'answers': ['1985', '1989', '1991', '1975'],
         'right_answer': 2,
         'url': ''},
        {'question': 'Какая страна первой запустила искусственный спутник Земли?',
         'answers': ['США', 'Китай', 'Франций', 'СССР'],
         'right_answer': 4,
         'url': 'https://avatars.yandex.net/get-music-content/13663712/a1dc327e.a.33122247-1/m1000x1000?webp=false'},
        {'question': 'Какое событие произошло 24 августа 2006 года?',
         'answers': ['Лишение Плутона статуса планеты', 'Создание YouTube', 'Запуск первого iPhone',
                     'Создание Bitcoin'],
         'right_answer': 1,
         'url': ''},
        {'question': (
            'Как называется международная организация, основанная в 1919 — 1920 годах с целью предотвращения военных'
            ' действий и обеспечения безопасности в мире?'),
         'answers': ['НАТО', 'ЮНЕСКО', 'Лига Наций', 'ООН'],
         'right_answer': 3,
         'url': 'https://cdn.am.sputniknews.ru/img/160/33/1603352_509:0:3766:2047_1920x0_80_0_0_1f3fb1edd2cd0a69001b664771ef550b.jpg'},
        {
            'question': 'Какой договор официально завершил Первую мировую войну?',
            'answers': ['Потсдамское соглашение', 'Брест-Литовский мир',
                        'Ялтинская конференция', 'Версальский мир'],
            'right_answer': 4,
         'url': ''
        },
        {
            'question': 'Какой телефон первым получил сенсорный экран?',
            'answers': ['iPhone', 'IBM Simon', 'Nokia 3310', 'Motorola Razr'],
            'right_answer': 2,
         'url': ''
        },
{
            'question': 'Какая компания разработала ChatGPT?',
            'answers': ['OpenAI', 'Google', 'Yandex', 'Apple'],
            'right_answer': 1,
         'url': 'https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png'
        },
{
    'question': 'Какое историческое событие произошло НЕ в 2023 году?',
    'answers': [
        'Коронация Карла III', 'Запуск ChatGPT 4', 'Олимпийские игры в Париже',
        'Первый успешный запуск Starship Илона Маска'],
    'right_answer': 3,
    'url': '' }
] }

historical_figures = {
    'Лев Толстой': 'Автор романа "Война и мир"',
    'Наполеон Бонапарт': 'Император Франции, прославившийся завоеваниями в Европе',
    'Иван Грозный': 'Первый русский царь, который провел реформы и расширил территорию России',
    'Клеопатра': 'Последняя царица Египта, известная своими союзами с Римом',
    'Альберт Эйнштейн': 'Создатель теории относительности',
    'Христофор Колумб': 'Мореплаватель, открывший Новый Свет (Америку)',
    'Чарльз Дарвин': 'Учёный, пришедший к выводу о том, что все виды живых организмов эволюционируют со временем',
    'Джеймс Уатт': 'Инженер, изобретатель, ввёл первую единицу мощности — лошадиную силу. Создал универсальную паровую машину двойного действия.',
    'Мартин Лютер': 'Немецкий христианский богослов, инициатор Реформации. Ключевой создатель протестантизма ',
    'Джордж Вашингтон': 'Первый президент Соединённых Штатов Америки, один из отцов-основателей США',
    'Вильгельм Рентген': 'Физик, первый лауреат Нобелевской премии, изобретатель рентгена',
    'Пётр Великий': 'Первый российский император, развернул масштабные реформы российского государства',
    'Илон Маск': 'Основатель и гендиректор SpaceX, самый богатый человек в мире на февраль 2025 года'
}

user_data = {}


@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    """Обработчик команды /quiz"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("Античность", callback_data='epoch_ancient'),
        types.InlineKeyboardButton("Средневековье", callback_data='epoch_middle'),
        types.InlineKeyboardButton("Новое время", callback_data='epoch_new'),
        types.InlineKeyboardButton("Современность", callback_data='epoch_modern')
    ]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "🎮 Выберите эпоху для викторины:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('epoch_'))
def choose_epoch(call):
    """Обработчик выбора эпохи"""
    chat_id = call.message.chat.id
    epoch = call.data.split('_')[1]

    user_data[chat_id] = {
        'epoch': epoch,
        'current_question': 0,
        'score': 0
    }

    bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text=f"🏁 Вы выбрали: {epoch.replace('ancient', 'Античность').replace('middle', 'Средневековье').replace('new', 'Новое время').replace('modern', 'Современность')}"
    )
    ask_question(chat_id)


def ask_question(chat_id):
    """Задаем вопрос пользователю"""
    data = user_data.get(chat_id)
    if not data:
        return

    epoch = data['epoch']
    current = data['current_question']

    if current >= len(questions[epoch]):
        # Завершаем викторину
        final_score = data['score']
        total = len(questions[epoch])
        del user_data[chat_id]
        bot.send_message(
            chat_id,
            f"🏆 Викторина завершена!\n"
            f"Правильных ответов: {final_score}/{total}\n"
            f"Успех: {final_score / total * 100:.1f}%"
        )
        return

    question = questions[epoch][current]
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки с вариантами ответов
    for i, answer in enumerate(question['answers']):
        callback_data = f"answer_{current}_{i + 1}"
        markup.add(types.InlineKeyboardButton(answer, callback_data=callback_data))

    if question['url']:
        bot.send_photo(chat_id, question['url'])
    # Отправляем вопрос
    bot.send_message(
        chat_id,
        f"❓ Вопрос {current + 1}/{len(questions[epoch])}:\n{question['question']}",
        reply_markup=markup
    )



@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_answer(call):
    """Обработка ответа пользователя"""
    chat_id = call.message.chat.id
    data = user_data.get(chat_id)

    if not data:
        bot.answer_callback_query(call.id, "Викторина не активна. Начните заново /quiz")
        return

    # Парсим данные из callback
    _, question_idx, answer_idx = call.data.split('_')
    question_idx = int(question_idx)
    answer_idx = int(answer_idx)

    # Проверяем актуальность вопроса
    if question_idx != data['current_question']:
        bot.answer_callback_query(call.id, "Этот вопрос уже пройден!")
        return

    epoch = data['epoch']
    question = questions[epoch][question_idx]

    # Проверяем ответ
    if answer_idx == question['right_answer']:
        data['score'] += 1
        feedback = "✅ Правильно!"
    else:
        correct = question['right_answer']
        feedback = f"❌ Неправильно! Правильный ответ: {question['answers'][correct - 1]}"

    # Обновляем данные
    data['current_question'] += 1

    # Отправляем результат
    bot.answer_callback_query(call.id)
    bot.send_message(chat_id, feedback)

    # Задаем следующий вопрос
    ask_question(chat_id)


def get_history_fact():
    today = dt.now().strftime('%d_мая').lstrip('0')
    url = f"https://ru.wikipedia.org/wiki/{today}"
    response = requests.get(url)
    event = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        events = soup.find_all('li')
        for el in events[50:79]:
            event.append(el.get_text())

    return f"Интересный факт \n{str(today).replace('_', ' ')} {choice(event)}"


@bot.message_handler(commands=['fact'])
def random_fact(message):
    bot.send_message(message.chat.id, get_history_fact())


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     'Привет! Я бот-историк. Я могу помочь тебе с изучением истории. Список команд: \n /quiz - '
                     'Викторина \n /fact - Случайное историческое событие \n /guess_person - Игра "Угадай личность", я '
                     'называю описание исторической личности, а вы должны понять кто это  \n\n\nСсылка на наш чат '
                     't.me/+lxmh6J_-aqNiZTQ6')


current_person = None


@bot.message_handler(commands=['guess_person'])
def handle_start(message):
    global current_person
    current_person = choice(list(historical_figures.keys()))
    bot.send_message(message.chat.id, f"{historical_figures[current_person]} \n\nНапишите имя и фамилию/прозвище")


@bot.message_handler(func=lambda message: True)
def handle_guess(message):
    global current_person
    if current_person:
        if message.text.lower() in current_person.lower():
            bot.send_message(message.chat.id, f'Всё верно, это {current_person}')
        else:
            bot.send_message(message.chat.id, f'Неверно, это {current_person}')
        current_person = None


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
