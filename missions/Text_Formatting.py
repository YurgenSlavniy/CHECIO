# Text Formatting >< 
# Отформатируйте текст в соответствии с заданным стилем ? 
# Elementary+ <>
# Русский text --
# ___________________________________________________________________________________
# Elementary+
# DE EN FR PL Русский UK ZH-HANS

# Вам предоставлена длинная строка (набранная моноширинным шрифтом), 
# и вы должны разбить ее, чтобы соблюсти заданную ширину. 
# После этого вам нужно отформатировать текст в соответствии с заданным стилем: 
# "l" означает, что вы должны выровнять текст по левому краю - left, 
# "c" - по центру - center, 
# "r" - по правому краю - right, 
# а "j" означает, что вы должны выровнять текст по ширине - justify. 
# И, наконец, строки вывода не должны заканчиваться пробелами.

# Если для центрирования строки необходимо поставить 2 * n + 1 пробела вокруг строки, 
# то перед ней ставится n пробелов, а не n + 1.

# Правила выравнивания текста:
# Поскольку мы не всегда можем поставить одинаковое количество пробелов между словами в строке, 
# поместите большие блоки пробелов сначала. 
# Например: X---X---X--X--X--X, когда вам нужно поместить 12 пробелов в 5 местах: 3-3-2-2-2.
# Не выравнивайте последнюю строку текста.

# Вам не нужно будет разбивать слово на две части, так как предоставленной ширины вполне достаточно.

# Входные данные: Текст (строка - str), ширина (целое число - int) и стиль (строка - str).
# Выходные данные: Отформатированный текст (строка - str).

# Примеры:
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    )
    == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    )
    == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    )
    == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
)

# Предварительное условие:
# - all(len(word) <= width for word in text.split());
# - '\n' нету в тексте;
# - варианты стиля в ("l", "c", "r", "j");
# - 0 < len(text) <= 1000.
# ___________________________________________________________________________________
# SOLUTION <>
from textwrap import wrap


def rjust(line, width):
    return line.rjust(width)


def ljust(line, width):
    return line


def cjust(line, width):
    return line.center(width).rstrip()


def jjust(line, width):
    words = line.split()
    space_to_fill = width - sum(len(word) for word in words)
    spaces = len(words)-1
    if not spaces:
        return line
    sep_width, wide_sep_count = divmod(space_to_fill, spaces)
    sep = ' '*sep_width
    return sep.join(words).replace(sep, sep+' ', wide_sep_count)


def text_formatting(text, width, style):
    d = dict(zip('rlcj', (rjust, ljust, cjust, jjust)))
    justify = d[style]
    lines = [justify(line, width) for line in wrap(text, width)]
    if style == 'j':  # De-justify last line
        last_line = lines.pop()
        lines.append(' '.join(last_line.split()))
    return '\n'.join(lines)


LINE = (
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure "
    "harum suscipit aperiam aliquam ad, perferendis ex molestias "
    "reiciendis accusantium quos, tempore sunt quod veniam, eveniet "
    "et necessitatibus mollitia. Quasi, culpa."
)
print("Example:")
print(text_formatting(LINE, 38, "l"))

# These "asserts" are used for self-checking
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    )
    == "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    )
    == " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    )
    == "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
)
assert (
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    )
    == "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
)


# <><><><><> Best "Clear" Solution <><><><><>
# <><><><><> Best "Creative" Solution <><><><><>
# <><><><><> Best "Speedy" Solution <><><><><>
# <><><><><> Best "3rd party" Solution <><><><><>
# <><><><><> Uncategorized <><><><><>
# ___________________________________________________________________________________
