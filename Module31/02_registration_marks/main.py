import re


if __name__ == '__main__':
    cars = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666 QZ233787'

    cur_letters = 'АВЕКМНОРСТУ'
    pattern_privat = r'\b[letters]\d{3}\w+[letters]\d{2,3}'.replace('letters', cur_letters)
    pattern_taxi = r'\b[letters]{2}\d{3}\d{2,3}'.replace('letters', cur_letters)

    result_privat = re.findall(pattern_privat, cars)
    print(result_privat)
    result_taxi = re.findall(pattern_taxi, cars)
    print(result_taxi)
