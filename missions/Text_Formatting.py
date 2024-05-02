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
from textwrap import wrap

def text_formatting(text, width, style):
    lines = wrap(text, width=width)
    if style == 'l':
        return '\n'.join(lines)
    if style == 'c':
        return '\n'.join(' '*((width-len(line))//2) + line for line in lines)
    if style == 'r':
        return '\n'.join(line.rjust(width) for line in lines)
    for i in range(len(lines) - 1):
        gap, big_blocks = divmod(width - len(lines[i]), lines[i].count(' '))
        lines[i] = lines[i].replace(' ', ' '*(gap+1)) \
                           .replace(' '*(gap+1), ' '*(gap+2), big_blocks)
    return '\n'.join(lines)
    

# <><><><><> Best "Creative" Solution <><><><><>
from textwrap import wrap


def format_line(line, width, style):
    # first divmod argument is total spaces needed, second - intervals between words
    d, q = divmod(width - len(line) + len(lst := line.split()) - 1, max(1, len(lst) - 1))
    return f"{line:{'<^>'['lcr'.find(style)]}{width}}".rstrip() if style in 'lcr' \
        else ''.join(' ' * (i > 0) * (d + (i <= q)) + w for i, w in enumerate(lst))


def text_formatting(text: str, width: int, style: str) -> str:
    
    lst = wrap(text, width=width)
    return '\n'.join(line if style == 'j' and i+1 == len(lst) else 
                     format_line(line, width, style) for i, line in enumerate(lst))
    """
    # no wordwrap.wrap alternative with comments
    res = line = ''
    for w in text.split():
        if len(line) + len(w) + 1 > width:
            line, res = '', res + format_line(line, width, style) + '\n'
        line += ' ' * bool(line) + w
    return res + (line if style == 'j' else format_line(line, width, style))
    """


# <><><><><> Best "Speedy" Solution <><><><><>
def text_formatting(text: str, width: int, style: str) -> str:
    #Splitting text into lines for given width
    lines=[]
    line=""
    
    for word in text.split(" "):
        if len(word)+len(line)<=width:
            line+=word+" "
        
        else:
            line=line.rstrip()
            line+="\n"
            lines.append(line)
            line=word+" "
    
    line=line.rstrip()
    lines.append(line)
    
    #Creating formatted text
    formatted=""
    
    match style:
        case "l": #Left
            for line in lines:
                formatted+=line
        
        case "r": #Right
            for line in lines[:-1]:
                formatted+="{:{fill}{align}{width}}".format(line,fill=" ",align=">",width=width+1)
            
            formatted+="{:{fill}{align}{width}}".format(lines[-1],fill=" ",align=">",width=width)
        
        case "c": #Centered
            for line in lines[:-1]:
                formatted+="{:{fill}{align}{width}}".format(line,fill=" ",align=">",
                                                            width=len(line)+(width-len(line)+1)//2)
            
            formatted+="{:{fill}{align}{width}}".format(lines[-1],fill=" ",align=">",
                                                        width=len(lines[-1])+(width-len(lines[-1]))//2)
        
        case "j": #Justified
            for line in lines[:-1]:
                words=line.split(" ")
                spacenum=len(words)-1-sum([1 for word in words if word==""])
                totspace=width-sum([len(word) if word!="" else 1 for word in words])+1
                smallspacew=totspace//spacenum
                smallspace=" "*smallspacew
                bigspacenum=totspace-smallspacew*spacenum
                num=0
                
                for word in words:
                    if word=="":
                        formatted+=" "
                    
                    else:
                        formatted+=word+smallspace+(" " if num<bigspacenum else "")
                        num+=1
                
                formatted=formatted.rstrip(" ")
            
            formatted+=lines[-1]
    
    return formatted




# <><><><><> Best "3rd party" Solution <><><><><>
import numpy as np
import textwrap


def justify(line, width):
    splitted = line.split()
    without_space = len(''.join(splitted))
    pos = len(splitted) - 1
    p1, p2 = divmod(width - without_space, pos)
    spaces = list(np.array([p1] * pos) + np.array([1] * p2 + [0] * (pos - p2))) + [1]
    line = ''
    for i in range(len(splitted)):
        line += splitted[i] + ' ' * spaces[i]
    return line[:-1]


def text_formatting(text: str, width: int, style: str) -> str:
    text = textwrap.wrap(text, width)
    if style == 'l':
        return '\n'.join([line.ljust(width, ' ').rstrip() for line in text])
    elif style == 'c':
        return '\n'.join([line.center(width, ' ').rstrip() for line in text])
    elif style == 'r':
        return '\n'.join([line.rjust(width, ' ').rstrip() for line in text])
    justified = [justify(line, width) for line in text[:-1]]
    justified += [text[-1]]

    return '\n'.join(justified)


# <><><><><> Uncategorized <><><><><>
import textwrap


def adjust(data: str, width: int):
    completed_text = ""
    completed_line = []
    
    result = textwrap.wrap(data, width=width, break_long_words=False)
    text = ""
    
    for line in result:
        text += line + "\n"
        
    lines2adjust = text[:-1].split("\n")
    
    for num, line in enumerate(lines2adjust):
        last_line = len(lines2adjust) - 1
        
        if num == last_line:
            completed_text += ''.join(line)
            break
            
        words_len = len(line.replace(" ", ""))
        words_count = len(line.split())
        spaces_remain = width - words_len
        places_remain = words_count - 1
        spaces_to_add = " " * (spaces_remain // places_remain)

        for word in reversed(line.split()):

            if spaces_to_add:
            
                word = spaces_to_add + word.strip()
                completed_line.append(word)
                
                spaces_remain -= len(spaces_to_add)
                places_remain -= 1
                try:
                    spaces_to_add = " " * (spaces_remain // places_remain)
                except:
                    spaces_to_add = 0
            else:
                completed_line.append(word)
                line2string = ''.join(reversed(completed_line))
                completed_text += line2string + "\n"
                completed_line.clear()
                
    return completed_text

def text_formatting(text: str, width: int, style: str) -> str:

    result = textwrap.wrap(text, width=width, break_long_words=False)   
    final_text = ""
    new_line = "\n"
    
    for num, line in enumerate(result):
    
        if num == len(result) - 1:
            new_line = ""
    
        if style == "l":
            final_text += line + new_line
        elif style == "c":
            final_text += line.center(width).rstrip() + new_line
        elif style == "r":
            final_text += line.rjust(width, " ") + new_line
        else:
            final_text = adjust(text, width)
    
    return final_text
# ___________________________________________________________________________________
