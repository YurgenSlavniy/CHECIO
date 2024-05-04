# Sun Angle >< 
# Определите угол солнца над горизонтом ? 
# Simple <>
# Русский geometry logic math --
# ___________________________________________________________________________________
# Simple
# DE EN FR JA PL Русский UK ZH-HANS

# Любой настоящий путешественник должен уметь делать три вещи: 
# - добывать огонь, 
# - находить воду 
# - извлекать полезную информацию из природы, окружающей его. 
# Программирование не поможет вам с огнем и водой, но с добычей информации справится вполне.

# Ваша задача - определить угол солнца над горизонтом, зная время суток. 
# Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов. 
# В 12:00 солнце в зените, а значит угол = 90 градусов. 
# В 18:00 солнце садится за горизонт и угол равен 180 градусов. 
# В случае, если указано ночное время (раньше 6:00 или позже 18:00), 
# функция должна вернуть фразу "I don't see the sun!".

# Входные данные: Время.
# Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой.

# Пример:
assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

# Как это используется: Жизненно необходимый навык для любого путешественника, 
# особенно в случае утери компаса и разрядившегося мобильного телефона с GPS. Правда, 
# в такой ситуации приходится решать обратную задачу - определять 
# время по углу солнца и производить несколько дополнительных расчетов.

# Предусловия:
# - 00:00 <= время <= 23:59
# ___________________________________________________________________________________
# SOLUTION <>

from typing import Union
from itertools import product
import numpy as np


def sun_angle(time: str) -> Union[float, str]:
    
    angles = np.arange(0, 180.25, 0.25)
    timeline = [f"{h:02d}:{m:02d}" for h,m in product(range(6, 18), range(0, 60, 1))]
    timeline.append('18:00')
    dict_time_angle = dict(zip(timeline, angles))
    
    if time in dict_time_angle:
        return dict_time_angle.get(time)
    else:
        return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75


# <><><><><> Best "Clear" Solution <><><><><>
def sun_angle(time):
    h, m = list(map(int, time.split(':')))
    angle = 15 * h + m / 4 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"


# <><><><><> Best "Creative" Solution <><><><><>
sun_angle=lambda t:["I don't see the sun!",int(t[:2])*15+int(t[~1:])/4-90][6<=int(t[:2])+int(t[~1:])/60<=18]


# <><><><><> Best "Speedy" Solution <><><><><>
def sun_angle(time):
    hh, mm = map(int, time.split(':'))
    tt = hh*60+mm
    
    return "I don't see the sun!" if (tt < 360 or 1080 < tt) else (tt-360)*0.25


# <><><><><> Best "3rd party" Solution <><><><><>
from typing import Union
import pandas as pd
import numpy as np
from datetime import datetime

def sun_angle(time: str) -> Union[int, str]:
    minutes = list(pd.date_range("06:00", "18:00", freq="1min").strftime('%H:%M'))
    if time not in minutes:
        return "I don't see the sun!"

    degrees = np.linspace(0,180,len(minutes))
    
    return list(filter(lambda t: t[0] == time, zip(minutes,degrees)))[0][1]


# <><><><><> Uncategorized <><><><><>
from typing import Union
from datetime import datetime as dt


def sun_angle(time: str) -> Union[float, str]:
    dawn = 0
    dusk = 180
    hour_degree = 15
    min_degree = .25
    hour, minute = dt.strptime(time, "%H:%M").hour, dt.strptime(time, "%H:%M").minute
    if hour < 6:
        return "I don't see the sun!"
    
    degrees = (hour - 6) * hour_degree + (minute * min_degree)

    return degrees if dawn <= degrees <= dusk else "I don't see the sun!"
    

# ___________________________________________________________________________________
