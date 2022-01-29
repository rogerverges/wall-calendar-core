from datetime import date, datetime, timedelta

from pymeeus.Epoch import Epoch
from pymeeus.Sun import Sun
from pymeeus.Earth import Earth
from pymeeus.Moon import Moon


(
    JANUARY,
    FEBRUARY,
    MARCH,
    APRIL,
    MAY,
    JUNE,
    JULY,
    AUGUST,
    SEPTEMBER,
    OCTOBER,
    NOVEMBER,
    DECEMBER,
) = range(1, 13)
(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC) = range(1, 13)
LENGTH_OF_WEEK = 7  # days
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(LENGTH_OF_WEEK)
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(LENGTH_OF_WEEK)
(WEEK1, WEEK2, WEEK3, WEEK4) = (4, 11, 18, 25)

(
    NISAN,
    IYAR,
    SIVAN,
    TAMMUZ,
    AV,
    ELUL,
    TISHREI,
    CHESHVAN,
    KISLEV,
    TEVET,
    SHEVAT,
    ADAR,
    ADAR_SHENI,
) = range(1, 14)

LENGTH_OF_LUNAR_MONTH = 30
(NEW_MOON, FIRST_QUARTER_MOON, FULL_MOON, LAST_QUARTER_MOON) = (0, 8, 15, 22)

MOON_GLYPHS = [
    '🌑',  #  0 new moon
    '🌒',  #  1
    '🌒',  #  2
    '🌒',  #  3
    '🌒',  #  4 waxing crescent moon
    '🌒',  #  5
    '🌒',  #  6
    '🌒',  #  7
    '🌓',  #  8 first quarter moon
    '🌔',  #  9
    '🌔',  # 10
    '🌔',  # 11 waxing gibbous moon
    '🌔',  # 12
    '🌔',  # 13
    '🌔',  # 14
    '🌕',  # 15 full moon
    '🌖',  # 16
    '🌖',  # 17
    '🌖',  # 18
    '🌖',  # 19 waning gibbous moon
    '🌖',  # 20
    '🌖',  # 21
    '🌗',  # 22 last quarter moon
    '🌘',  # 23
    '🌘',  # 24
    '🌘',  # 25
    '🌘',  # 26 waning crescent moon
    '🌘',  # 27
    '🌘',  # 28
    '🌘',  # 29
]


def is_leap(year=date.today().year):
    ''' '''

    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return Epoch.is_leap(year)


def days_in_month(month=date.today().month, year=date.today().year):
    ''' '''

    DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    FEBRUARY_LEAP_YEAR = 29

    if month == FEBRUARY and is_leap(year=year):
        return FEBRUARY_LEAP_YEAR
    else:
        return DAYS_IN_MONTH[month]


def closest_date(desired_weekday, nearby_date=date.today(), last=False):
    ''' '''

    # Move the nearby_date to the end of the month
    if last:
        nearby_date = date(
            year=nearby_date.year,
            month=nearby_date.month,
            day=days_in_month(month=nearby_date.month, year=nearby_date.year),
        )

    # Determine how far away we are from our desired weekday
    offset = nearby_date.weekday() - (desired_weekday % LENGTH_OF_WEEK)

    # Force the offset back into the current week if it is too large
    if offset < -3:
        offset += LENGTH_OF_WEEK
    if offset > 3:
        offset -= LENGTH_OF_WEEK

    found_date = nearby_date - timedelta(days=offset)

    # Jump back into the correct month if we managed to leave it
    if last and found_date.month != nearby_date.month:
        return found_date - timedelta(days=LENGTH_OF_WEEK)
    else:
        return found_date


def repeat_date(start_date=date.today(), skip=LENGTH_OF_WEEK):
    ''' '''

    date_tracker = start_date
    while True:
        yield date_tracker
        date_tracker += timedelta(skip)


def ordinal(number, lang='en'):
    ''' '''

    #   https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
    match lang:
        case 'en':
            if number > 10 and number < 20:
                return f'{number}th'
            if number % 10 == 1:
                return f'{number}st'
            elif number % 10 == 2:
                return f'{number}nd'
            elif number % 10 == 3:
                return f'{number}rd'
            else:
                return f'{number}th'
        case 'fr':
            if number == 1:
                return f'{number}er'
            else:
                return f'{number}e'


# Easter is the 1st Sunday after the 1st full moon after the March equinox
# Passover is from 14 or 15 to 21 or 22 Nisan
# March 22nd is the earliest date when Easter may occur
# April 25nd is the latest date when Easter may occur
# ??? is the earliest date when Passover may occur
# ??? is the latest date when Passover may occur
# XXX FIXME TODO  Get this info from wikipedia page???


# Equinox/Équinoxe literally means "equal night"
# Solstice literally means "sun stands still" (longest/shortest day)
# March Equinox is the 1st Day of Spring/printemps in the Northern Hemisphere
# June Solstice is the 1st Day of Summer/été in the Northern Hemisphere
# September Equinox is the 1st Day of Fall/automne in the Northern Hemisphere
# December Solstice is the 1st Day of Winter/hiver in the Northern Hemisphere
# Perihelion/Périhélie is when the Earth is closest to the Sun
# Aphelion/Aphélie is when the Earth is farthest from the Sun


def easter(year=date.today().year):
    ''' '''

    month, day = Epoch.easter(year)
    return date(year=year, month=month, day=day)


def passover(year=date.today().year):
    ''' '''

    month, day = Epoch.jewish_pesach(year)
    return date(year=year, month=month, day=day)


def spring(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Sun.get_equinox_solstice(
        year, target='spring'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def summer(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Sun.get_equinox_solstice(
        year, target='summer'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def autumn(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Sun.get_equinox_solstice(
        year, target='autumn'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def winter(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Sun.get_equinox_solstice(
        year, target='winter'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def perihelion(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Earth.perihelion_aphelion(
        Epoch(date(year, JANUARY, 1)), perihelion=True
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def aphelion(year=date.today().year):
    ''' '''

    _, month, day, hour, minute, _ = Earth.perihelion_aphelion(
        Epoch(date(year, JULY, 1)), perihelion=False
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def new_moon(moon_date=date.today()):
    ''' '''

    year, month, day, hour, minute, _ = Moon.moon_phase(
        Epoch(moon_date - timedelta(days=6)), target='new'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def first_moon(moon_date=date.today()):
    ''' '''

    year, month, day, hour, minute, _ = Moon.moon_phase(
        Epoch(moon_date - timedelta(days=6)), target='first'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def full_moon(moon_date=date.today()):
    ''' '''

    year, month, day, hour, minute, _ = Moon.moon_phase(
        Epoch(moon_date - timedelta(days=6)), target='full'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


def last_moon(moon_date=date.today()):
    ''' '''

    year, month, day, hour, minute, _ = Moon.moon_phase(
        Epoch(moon_date - timedelta(days=6)), target='last'
    ).get_full_date()
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute)


# https://en.wikipedia.org/wiki/Chinese_zodiac
# https://en.wikipedia.org/wiki/Chinese_astrology
# https://en.wikipedia.org/wiki/Sexagenary_cycle
# https://en.wikipedia.org/wiki/Heavenly_Stems
# https://en.wikipedia.org/wiki/Earthly_Branches

# 年 (year)
SPINS = [
    '陽',  # yáng (white side) 阳
    '陰',  # yīn (black side) 阴
]  # year mod 2
MAJOR_ELEMENTS = [
    '金',  # jīn (metal)
    '金',  # jīn (metal)
    '水',  # shuǐ (water)
    '水',  # shuǐ (water)
    '木',  # mù (wood)
    '木',  # mù (wood)
    '火',  # huǒ (fire)
    '火',  # huǒ (fire)
    '土',  # tǔ (earth)
    '土',  # tǔ (earth)
]  # year mod 10
CHINESE_ZODIAC = [
    '猴',  # hóu (monkey)
    '雞',  # jī (rooster) 鸡
    '狗',  # gǒu (dog)
    '豬',  # zhū (pig/boar) 猪
    '鼠',  # shǔ (rat)
    '牛',  # niú (ox)
    '虎',  # hǔ (tiger)
    '兔',  # tù (rabbit)
    '龍',  # lóng (dragon) 龙
    '蛇',  # shé (snake)
    '馬',  # mǎ (horse) 马
    '羊',  # yáng (goat)
]  # year mod 12
HEAVENLY_STEMS = [
    '庚',  # gēng (white metal)
    '辛',  # xīn (wrought metal)
    '壬',  # rén (black running water)
    '癸',  # guǐ (stagnant water)
    '甲',  # jiǎ (green shield wood)
    '乙',  # yǐ (timber wood)
    '丙',  # bǐng (red fire)
    '丁',  # dīng (artificial fire)
    '戊',  # wù (yellow earth)
    '己',  # jǐ (pottery)
]  # year mod 10
EARTHLY_BRANCHES = [
    '申',  # shēn
    '酉',  # yǒu
    '戌',  # xū
    '亥',  # hài
    '子',  # zǐ
    '丑',  # chǒu
    '寅',  # yín
    '卯',  # mǎo
    '辰',  # chén
    '巳',  # sì
    '午',  # wǔ
    '未',  # wèi
]  # year mod 12
CORRELATIONS = [
    '西',  # (west)
    '西',  # (west)
    '北',  # (north)
    '北',  # (north)
    '東',  # (east)
    '東',  # (east)
    '南',  # (south)
    '南',  # (south)
    '中',  # (middle)
    '中',  # (middle)
]  # year mod 10


# https://dateutil.readthedocs.io/en/stable/rrule.html

# Seasons and Moon Phases
# https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight
# https://rhodesmill.org/skyfield/almanac.html#the-seasons

# Chinese New Year
# https://humanoriginproject.com/the-chinese-calendar-how-to-calculate-chinese-new-year/
# Chinese New Year falls between January 21 and February 20.
# The precise date is the second new moon after the December solstice (December
# 21).

# Zodiac
# https://en.wikipedia.org/wiki/Astrological_symbols

# Chinese/Lunar New Year is between Jan 21 and Feb 20 on the day after the
# new moon

# January
#   Wolf Moon
#   Old Moon
#   Spirit Moon
#   Moon After Yule
# February
#   Hunger Moon
#   Snow Moon
#   Bear Moon
# March
#   Worm Moon
#   Crow Moon
#   Crust Moon
#   Sap Moon
#   Lenten Moon
#   Sugar Moon
# April
#   Pink Moon
#   Sprouting Grass Moon
#   Egg Moon
#   Fish Moon
#   Sucker Moon
# May
#   Flower Moon
#   Corn Planting Moon
#   Milk Moon
# June
#   Strawberry Moon
#   Rose Moon
# July
#   Buck Moon
#   Thunder Moon
#   Hay Moon
#   Raspberry Moon
# August
#   Sturgeon Moon
#   Red Moon
#   Green Corn Moon
#   Grain Moon
#   Thimbleberry Moon
# September
#   Harvest Moon
#   Corn Moon
# October
#   Hunter's Moon
#   Falling Leaves Moon
# November
#   Beaver Moon
#   Frosty Moon
#   Freezing Moon
# December
#   Cold Moon
#   Long Nights Moon
#   Little Spirit Moon
#   Moon Before Yule
