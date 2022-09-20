import re

phrases = "пара-рам пара" #input("Введите кричалку или шумелку-пыхтелку: ")

vow_count = lambda x: len(re.findall("[аеёиоуэюя]", x))
def parse_phrases(phrases):
    list
    counts = [vow_count(phrase) for phrase in phrases.split(" ")]
    if len(counts) == 0:
        return "Пам парам"
    if counts.count(counts[0]) == len(counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"    

print(parse_phrases(phrases))
