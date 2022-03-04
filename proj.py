import json
import random


def call_process(request):
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    dialog(request.json, response)

    return json.dumps(response, ensure_ascii=False, indent=2)


sessionStorage = {}

towns = {
    'а': ['Ангкор', 'Анапа', 'Абакан', 'Алушта', 'Анталия', 'Астана', 'Афины', 'Актау', 'Аликанте',
          'Амстердам', 'Астрахань', 'Архангельск', 'Александрия', 'Александров', 'Армавир', 'Ашхабад', 'Атланта',
          'Ангарск', 'Алматы', 'Алжир', 'Армавир', 'Алания', 'Айя-Напа', 'Антиб', 'Аделаида', 'Агджабеди', 'Алжир',
          'Андорра-ла-Велья', 'Айзенштадт', 'Арарат', 'Армавир', 'Ангтхонг', 'Аюттхая', 'Алесунд', 'Асуан',
          'Антверпен', 'Абомей', 'Аракажу', 'Абердин', 'Айронбридж', 'Аккра', 'Антигуа-Гватемала', 'Аахен', 'Афины',
          'Александрия', 'Акко', 'Ашдод', 'Агра'],
    'б': ['Барселона', 'Баку', 'Брянск', 'Белгород', 'Брест', 'Борисов', 'Бишкек', 'Берлин', 'Будапешт', 'Балашиха',
          'Будва', 'Бухара', 'Благовещенск', 'Бельцы', 'Балаково', 'Белек', 'Барнаул', 'Бургас', 'Брюссель',
          'Белград', 'Братск', 'Бремен', 'Бобруйск', 'Белокуриха', 'Брисбен', 'Баку', 'Бенгела', 'Буэнос-Айрес',
          'Бриджтаун', 'Белиз', 'Бельмопан', 'Бангкок', 'Бурирам', 'Бангсапхан', 'Берген', 'Багерхат', 'Бобруйск',
          'Борисов', 'Брест', 'Брюгге', 'Брюссель', 'Бургас', 'Баня-Лука', 'Бихач', 'Бузиос', 'Белен',
          'Белу-Оризонти', 'Бразилиа'],
    'в': ['Воронеж', 'Владимир', 'Волгоград', 'Вена', 'Владивосток', 'Венеция', 'Вашингтон', 'Виктория', 'Витебск',
          'Валенсия', 'Винница', 'Вологда', 'Варна', 'Вильнюс', 'Владикавказ', 'Варшава', 'Волгодонск',
          'Великий Новгород', 'Верона', 'Выборг', 'Виндзор', 'Валдай', 'Воркута', 'Вентспилс', 'Вена', 'Вельс',
          'Вагаршапат', 'Вааса', 'Вильнюс', 'Витебск', 'Варна', 'Велико-Тырново', 'Винчестер', 'Валенсия',
          'Висбаден', 'Варанаси', 'Валенсия', 'Венеция', 'Верона', 'Виченца', 'Ванкувер', 'Виктория', 'Виндзор',
          'Варадеро', 'Вьентьян', 'Вентспилс', 'Вадуц', 'Валлетта'],
    'г': ['Грозный', 'Гагра', 'Гомель', 'Гродно', 'Геленджик', 'Гюмри', 'Гамбург', 'Гянджа', 'Гонконг', 'Гуанчжоу',
          'Генуя', 'Гёйнюк', 'Гудаута', 'Гент', 'Грац', 'Гатчина', 'Грасс', 'Галле', 'Гданьск', 'Гранада', 'Гаага',
          'Гавана', 'Галифакс', 'Гранада', 'Грац', 'Гянджа', 'Гюмри', 'Герат', 'Гетеборг', 'Гирокастра', 'Гардая',
          'Гомель', 'Гродно', 'Гент', 'Габороне', 'Гояния', 'Глазго', 'Гамбург', 'Ганновер', 'Гейдельберг', 'Гиза',
          'Гангток', 'Гвалиор', 'Голуэй', 'Гранада', 'Генуя', 'Губбио', 'Галифакс'],
    'д': ['Дели', 'Донецк', 'Дмитров', 'Душанбе', 'Детройт', 'Долгопрудный', 'Дубай', 'Дубно', 'Днепропетровск',
          'Дюссельдорф', 'Дения', 'Дербент', 'Дрезден', 'Дортмунд', 'Друскининкай', 'Дубровник', 'Дзержинск',
          'Денвер', 'Джалал-Абад', 'Дьер', 'Даллас', 'Дублин', 'Дарвин', 'Дидим', 'Дарвин', 'Дуррес', 'Джелалабад',
          'Дакка', 'Дарем', 'Дебрецен', 'Дьер', 'Дили', 'Далат', 'Дананг', 'Джорджтаун', 'Дрезден', 'Дюссельдорф',
          'Джибути', 'Дарджилинг', 'Дели', 'Джайпур', 'Джайсалмер', 'Джодхпур', 'Джакарта', 'Джокьякарта', 'Дублин',
          'Дуала', 'Доха'],
    'е': ['Екатеринбург', 'Ейск', 'Ереван', 'Ессентуки', 'Евпатория', 'Елабуга', 'Ереван', 'Екатеринбург',
          'Евпатория', 'Елабуга', 'Ессентуки', 'Ейск'],
    'ж': ['Железноводск', 'Женева', 'Жирона', 'Жилина', 'Жабляк', 'Жатец', 'Жилина', 'Жабляк', 'Жатец', 'Женева',
          'Жирона', 'Железноводск'],
    'з': ['Запорожье', 'Зальцбург', 'Задонск', 'Золочев', 'Загреб', 'Задар', 'Занзибар', 'Закопане', 'Заандам',
          'Зеленоградск', 'Зула', 'Зальцбург', 'Закопане', 'Занзибар', 'Запорожье', 'Загреб', 'Задар', 'Зула',
          'Золочев', 'Заандам', 'Задонск', 'Зеленоградск'],
    'к': ['Куйбышев', 'Кенигсберг', 'Константинополь', 'Котор', 'Киев', 'Коломна', 'Краснодар', 'Калуга', 'Казань',
          'Керчь', 'Курск', 'Кострома', 'Кемер',
          'Киров', 'Красноярск', 'Калининград', 'Константина', 'Кишинёв', 'Кёльн', 'Комсомольск-на-Амуре', 'Курган',
          'Кемерово', 'Канберра', 'Катания', 'Кривой Рог', 'Костанай', 'Калязин', 'Канберра', 'Кэрнс', 'Клагенфурт',
          'Куба', 'Константина', 'Кордова', 'Кабул', 'Краби', 'Као-Лак', 'Кхонкэн', 'Копенгаген', 'Каунас',
          'Кандагар', 'Котону', 'Кочабамба', 'Куяба', 'Кардифф', 'Кембридж', 'Кентербери', 'Ковентри', 'Кечкемет',
          'Кабимас', 'Каракас', 'Коро'],
    'л': ['Ленинград', 'Львов', 'Липецк', 'Луганск', 'Лондон', 'Лос-Анджелес', 'Лиссабон', 'Люксембург', 'Ливерпуль',
          'Лион',
          'Луцк', 'Ломе', 'Лимассол', 'Лас-Вегас', 'Ларнака', 'Ллорет-де-Мар', 'Лас-Пальмас', 'Лима', 'Лейпциг',
          'Ла-Романа', 'Люцерн', 'Любляна', 'Луксор', 'Лиепая', 'Лодзь', 'Линц', 'Луанда', 'Лампанг', 'Лампхун',
          'Лопбури', 'Лиепая', 'Льеж', 'Ла-Пас', 'Ленакел', 'Луганвилл', 'Лестер', 'Ливерпуль', 'Лидс', 'Лондон',
          'Лондондерри', 'Люблин', 'Либревиль', 'Лейпциг', 'Любек', 'Лубумбаши', 'Луксор', 'Лусака', 'Лакнау',
          'Лимерик'],
    'м': ['Москва', 'Минск', 'Мариуполь', 'Муром', 'Магадан', 'Мадрид', 'Мытищи', 'Монастир', 'Мышкин', 'Милан',
          'Мюнхен', 'Мармарис', 'Мурманск', 'Могилев', 'Магнитогорск', 'Марсель', 'Махачкала', 'Минеральные Воды',
          'Манчестер', 'Муйне', 'Макеевка', 'Малага', 'Мары', 'Марбелья', 'Мельбурн', 'Мингечаур', 'Мельк',
          'Мар-дель-Плата', 'Мазари-Шариф', 'Манама', 'Мэхонгсон', 'Мальмё', 'Мендоса', 'Минск', 'Могилев',
          'Мехелен', 'Мостар', 'Манаус', 'Манчестер', 'Мишкольц', 'Маракайбо', 'Магдебург', 'Мюнхен', 'Митилини',
          'Матади', 'Мумбаи', 'Майсур', 'Маргао'],
    'н': ['Нур-Султан', 'Николаев', 'Находка', 'Нью-Йорк', 'Нижний Новгород', 'Новосибирск', 'Нячанг', 'Новороссийск',
          'Нетания',
          'Ницца', 'Нальчик', 'Норильск', 'Нарва', 'Новокузнецк', 'Набережные Челны', 'Неаполь', 'Новый Афон',
          'Новочеркасск', 'Несвиж', 'Нагасаки', 'Ниш', 'Нижневартовск', 'Нюрнберг', 'Ним', 'Нукус', 'Неукен',
          'Нассау', 'Накхонпатхом', 'Накхонпханом', 'Накхонратчасима', 'Накхонсаван', 'Нан', 'Накхонситхаммарат',
          'Наратхиват', 'Нонг Кхай', 'Нонтхабури', 'Нахичевань', 'Намюр', 'Несебр', 'Нитерой', 'Норидж',
          'Ноттингем', 'Ньюкасл-апон-Тайн', 'Нюрнберг', 'Назарет', 'Неаполь', 'Ното', 'Найроби', 'Ньери'],
    'о': ['Одесса', 'Орёл', 'Омск', 'Ош', 'Оренбург', 'Орджоникидзе', 'Осло', 'Осака', 'Олюдениз', 'Ольбия',
          'Орландо', 'Орлеан', 'Остин', 'Оксфорд', 'Оттава', 'Оденсе', 'Остенде', 'Острава', 'Опатия', 'Охрид',
          'Орвието', 'Оранж', 'Ольгин', 'Омиш', 'Оран', 'Оулу', 'Осло', 'Ольборг', 'Орхус', 'Обзор', 'Ору-Прету',
          'Оксфорд', 'Оденсе', 'Орчха', 'Орвието', 'Оттава', 'Ош', 'Ольгин', 'Охрид', 'Оахака', 'Окленд', 'Омск',
          'Орёл', 'Оренбург', 'Остин', 'Омдурман', 'Одесса', 'Оранж'],
    'п': ['Париж', 'Прага', 'Пенза', 'Пушкин', 'Пермь', 'Подольск', 'Пятигорск', 'Пекин', 'Питкяранта', 'Псков',
          'Пафос', 'Пицунда', 'Полтава', 'Павлодар', 'Плес', 'Полоцк', 'Пиза', 'Петровац', 'Переславль-Залесский',
          'Порт-Эль-Кантауи', 'Претория', 'Пула', 'Петрозаводск', 'Печ', 'Перт', 'Паттайя', 'Паттани',
          'Патхумтхани', 'Пхангнга', 'Пхаттхалунг', 'Пхаяу', 'Пхетчабури', 'Пхимай', 'Пхитсанулок', 'Пхрэ',
          'Пхукет', 'Прачинбури', 'Прачуапкхирикхан', 'Полоцк', 'Порто-Ново', 'Пловдив', 'Порту-Алегри', 'Пунакха',
          'Пхунчхолинг', 'Порт-Вила', 'Печ', 'Порт-о-Пренс', 'Потсдам'],
    'р': ['Рим', 'Ростов Великий', 'Рязань', 'Рига', 'Ростов-на-Дону', 'Римини', 'Ровно', 'Рыбинск', 'Родос',
          'Рио-де-Жанейро', 'Рас-эль-Хайма', 'Рустави', 'Ретимно', 'Руан', 'Роттердам', 'Ровинь', 'Рогашка Слатина',
          'Ротенбург-на-Таубере', 'Равенна', 'Регенсбург', 'Ренн', 'Реймс', 'Рабат', 'Рейкьявик', 'Росарио',
          'Районг', 'Ранонг', 'Ратчабури', 'Рейкьявик', 'Рига', 'Ресифи', 'Рио-де-Жанейро', 'Регенсбург', 'Родос',
          'Рустави', 'Розо', 'Ришон-ле-Цион', 'Равенна', 'Реджо-ди-Калабрия', 'Рим', 'Расон', 'Рабат', 'Роттердам',
          'Рабаул', 'Ростов-на-Дону', 'Рыбинск', 'Рязань', 'Раки-Раки'],
    'с': ['Санкт-Петербург', 'Сочи', 'Севастополь', 'Сумы', 'Смоленск', 'Саратов', 'Самара', 'Саранск',
          'Сергиев Посад', 'Сингапур', 'Стамбул', 'Сусс', 'София', 'Салоу', 'Суздаль', 'Ставрополь', 'Санья',
          'Самарканд', 'Сан-Франциско', 'Сидней', 'Светлогорск', 'Симферополь', 'Сургут', 'Сороки', 'Сидней',
          'Сент-Джонс', 'Сатун', 'Самутпракан', 'Самутсакхон', 'Сарабури', 'Саттахип', 'Си Сатчаналай', 'Ситхеп',
          'Сонгкхла', 'Сукхотхай', 'Сураттхани', 'Сурин', 'Ставангер', 'Стокгольм', 'Сальта', 'Созополь', 'София',
          'Санта-Крус-де-ла-Сьерра', 'Сукре', 'Сараево', 'Салвадор', 'Сан-Луис', 'Сан-Паулу'],
    'т': ['Тула', 'Тверь', 'Токио', 'Ташкент', 'Тунис', 'Тамбов', 'Тиват', 'Тольятти', 'Тюмень', 'Томск',
          'Тель-Авив', 'Тбилиси', 'Таллин', 'Таганрог', 'Тирасполь', 'Торжок', 'Туапсе', 'Торунь', 'Тобольск',
          'Тарту', 'Торонто', 'Тараз', 'Темрюк', 'Турин', 'Тирана', 'Тенес', 'Так', 'Трат', 'Турку', 'Тромсё',
          'Тронхейм', 'Таллин', 'Тариха', 'Терезина', 'Тхимпху', 'Труро', 'Трир', 'Тюбинген', 'Тегусигальпа',
          'Тбилиси', 'Телави', 'Танта', 'Тель-Авив', 'Тегеран', 'Толедо', 'Таормина', 'Торре-Аннунциата', 'Турин'],
    'у': ['Уфа', 'Ульяновск', 'Ухта', 'Углич', 'Улан-Удэ', 'Усть-Каменогорск', 'Ужгород', 'Улан-Батор', 'Уппсала',
          'Ухань', 'Убуд', 'Утрехт', 'Урбино', 'Уотерфорд', 'Уагадугу', 'Удонтхани', 'Ушуайя', 'Уссурийск',
          'Уэст-Айленд', 'Удайпур', 'Утхонг', 'Убонратчатхани', 'Уамбо', 'Уамбо', 'Ушуайя', 'Убонратчатхани',
          'Удонтхани', 'Утхонг', 'Уагадугу', 'Удайпур', 'Убуд', 'Уотерфорд', 'Урбино', 'Усть-Каменогорск', 'Ухань',
          'Улан-Батор', 'Утрехт', 'Улан-Удэ', 'Ульяновск', 'Уфа', 'Уппсала', 'Ужгород', 'Уэст-Айленд', 'Углич',
          'Уссурийск', 'Ухта'],
    'ф': ['Флоренция', 'Франкфурт-на-Майне', 'Фамагуста', 'Фергана', 'Фетхие', 'Фантьет', 'Феодосия', 'Форос',
          'Филадельфия', 'Фивы', 'Фуджейра', 'Фатима', 'Фес', 'Финикс', 'Феррара', 'Фукуока', 'Форталеза',
          'Фонтенбло', 'Фалун', 'Фучжоу', 'Филлах', 'Форт-Уэрт', 'Филипсбург', 'Фунафути', 'Филлах', 'Фанг',
          'Форталеза', 'Франкфурт-на-Майне', 'Фивы', 'Феррара', 'Флоренция', 'Фамагуста', 'Фучжоу', 'Фес', 'Фатима',
          'Филадельфия', 'Фритаун', 'Фунафути', 'Фалун', 'Фукуока', 'Феодосия', 'Фонтенбло', 'Филипсбург', 'Финикс',
          'Форт-Уэрт', 'Фантьет', 'Фетхие', 'Форос'],
    'х': ['Харьков', 'Хабаровск', 'Ханой', 'Хаммамет', 'Херсон', 'Худжанд', 'Хайфа', 'Хельсинки', 'Хиросима',
          'Ханты-Мансийск', 'Харбин', 'Хошимин (Сайгон)', 'Хиккадува', 'Хасавюрт', 'Херсониссос', 'Хива', 'Хьюстон',
          'Хама', 'Хум', 'Хотин', 'Ханчжоу', 'Хеб', 'Хюэ', 'Хойан', 'Хобарт', 'Хуа Хин', 'Хельсинки', 'Хайфон',
          'Ханой', 'Хойан', 'Хошимин (Сайгон)', 'Хюэ', 'Хараре', 'Хайдарабад', 'Харидвар', 'Ханчжоу', 'Харбин',
          'Ховд', 'Хабаровск', 'Хама', 'Хьюстон', 'Хониара', 'Хартум', 'Худжанд', 'Хива', 'Харьков', 'Хеб',
          'Хальмстад'],
    'ц': ['Цюрих', 'Циндао', 'Цетинье', 'Цзинань', 'Целье', 'Цюйфу', 'Цзинань', 'Циндао', 'Цюйфу', 'Цюрих',
          'Цетинье', 'Целье'],
    'ч': ['Челябинск', 'Чикаго', 'Чита', 'Чебоксары', 'Черкассы', 'Чернигов', 'Череповец', 'Честер', 'Чианграй',
          'Чешский Крумлов', 'Чунцин', 'Черчилл', 'Чэнду', 'Черняховск', 'Челаковице', 'Ческе-Будеёвице', 'Чорум',
          'Чэндэ', 'Ченнаи', 'Чонбури', 'Чиангмай', 'Чагуанас', 'Чингола', 'Чумпхон', 'Чиполлетти', 'Читтагонг',
          'Чиангмай', 'Чианграй', 'Чайя', 'Чантхабури', 'Чианг Саен', 'Чом Тонг', 'Чонбури', 'Чумпхон', 'Честер',
          'Чингола', 'Ченнаи', 'Чунцин', 'Чэнду', 'Чэндэ', 'Чебоксары', 'Челябинск', 'Череповец', 'Чита', 'Чикаго',
          'Чагуанас', 'Чорум', 'Ческе-Будеёвице'],
    'ш': ['Шэньчжэнь', 'Шанхай', 'Шарм-эль-Шейх', 'Штутгарт', 'Шымкент', 'Шеки', 'Шлиссельбург', 'Шахрисабз',
          'Шарджа', 'Шеффилд', 'Шибеник', 'Шефшауен', 'Шираз', 'Шауляй', 'Шибам', 'Шарлеруа', 'Шкодер',
          'Шарлотта-Амалия', 'Шартр', 'Шарлотсвилл', 'Шалон-сюр-Сон', 'Шеки', 'Шауляй', 'Шкодер', 'Шарлеруа',
          'Шеффилд', 'Шарм-эль-Шейх', 'Шираз', 'Шибам', 'Шымкент', 'Шанхай', 'Шефшауен', 'Шарджа', 'Шарлотсвилл',
          'Шахрисабз', 'Шалон-сюр-Сон', 'Шартр', 'Шибеник', 'Шарлотта-Амалия', 'Штутгарт', 'Шэньчжэнь',
          'Шлиссельбург'],
    'э': ['Эйлат', 'Энгельс', 'Элиста', 'Эдинбург', 'Эрдэнэт', 'Эвора', 'Эр-Рияд', 'Эдмонтон', 'Этрета', 'Эрзурум',
          'Эль-Джем', 'Эстергом', 'Эксетер', 'Эдфу', 'Эль-Пасо', 'Эребру', 'Экс-ан-Прованс', 'Эдирне', 'Эс-Сувейра',
          'Эль-Кувейт', 'Эсбьерг', 'Эпидавр', 'Эринген', 'Эбебьин', 'Эльбасан', 'Эдинбург', 'Эксетер', 'Эстергом',
          'Эсбьерг', 'Эр-Рамади', 'Эн-Наджаф', 'Эдеа', 'Эдмонтон', 'Этумби', 'Эль-Ахмади', 'Эль-Кувейт',
          'Эс-Сувейра', 'Эрдэнэт', 'Эвора', 'Эр-Рияд', 'Эль-Джем', 'Эдирне', 'Эрзурум', 'Экс-ан-Прованс', 'Этрета',
          'Эребру', 'Эбебьин', 'Эринген'],
    'ю': ['Южно-Сахалинск', 'Юрьев-Польский', 'Юрмала', 'Южная Тарава', 'Южная Тарава', 'Юрмала', 'Юрьев-Польский',
          'Южно-Сахалинск'],
    'я': ['Ярославль', 'Якутск', 'Ялта', 'Яссы', 'Янгон', 'Ямусукро', 'Яунде', 'Яла', 'Яффа', 'Ярен', 'Ясотхон',
          'Яла', 'Ясотхон', 'Яунде', 'Ямусукро', 'Янгон', 'Якутск', 'Ярославль', 'Яссы', 'Ялта', 'Ярен', 'Яффа'],
}

new_names = {'Константинополь': 'Стамбул',
             'Куйбышев': 'Самара',
             'Кенигсберг': 'Калиниград',
             'Астана': 'Нур-Султан',
             'Стамбул': 'Константинополь',
             'Самара': 'Куйбышев',
             'Калиниград': 'Кенигсберг',
             'Нур-Султан': 'Астана',
             'Ленинград': 'Санкт-Петербург',
             'Санкт-Петербург': 'Ленинград',
             }


def erase(town, towns_left):
    if town in new_names.keys():
        towns_left[new_names[town[0]]].remove(new_names[town])
    towns_left[town[0]].remove(town)


def dialog(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        sessionStorage[user_id] = {
            'towns_left': towns,
        }
        print("New user")
        res['response']['text'] = 'Давайте сыграем в города. Вы начинаете'
        return
    msg = sessionStorage[user_id]['message'] = req['request']['original_utterance']

    letter = msg.lower()[-1]
    town = sessionStorage[user_id]['towns_left'][letter][
        random.randint(0, len(sessionStorage[user_id]['towns_left'][letter]))]
    print(town)
    if msg in towns[letter] and msg not in sessionStorage[user_id]['towns_left'][letter]:
        res['response']['text'] = "Вы уже называли данный город или его другое название"
        return
    elif msg not in towns[letter]:
        res['response']['text'] = "Такой город я не знаю. Назовите другой"
        return
    else:
        erase(msg, sessionStorage[user_id]['towns_left'])
        erase(town, sessionStorage[user_id]['towns_left'])
        res['response']['text'] = town
        return
