class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax(self, piece_property):
        return int(piece_property) / 1


class Apartment(Property):

    def tax(self, tax_piece_property):
        return int(tax_piece_property) / 1000


class Car(Property):

    def tax(self, tax_piece_property):
        return int(tax_piece_property) / 200


class CountryHouse(Property):

    def tax(self, tax_piece_property):
        return int(tax_piece_property) / 500


money = int(input('Сколько у Вас денег? '))
worth_apart = int(input('Введите стоимость апартаментов: '))
worth_car = int(input('Введите стоимость машины: '))
worth_country_house = int(input('Введите стоимость дома: '))
if worth_apart > 0:
    person = Apartment(worth_apart)
    tax_apart = int(person.tax(worth_apart))
    print('Ваш налог на апартаменты составил {}'.format(tax_apart))
if worth_car > 0:
    person = Car(worth_car)
    tax_car = int(person.tax(worth_car))
    print('Ваш налог на машину составил {}'.format(tax_car))
if worth_country_house > 0:
    person = CountryHouse(worth_country_house)
    tax_house = int(person.tax(worth_country_house))
    print('Ваш налог на дом составил {}'.format(tax_house))
all_tax = tax_apart + tax_car + tax_house
if money < all_tax:
    print('У Вас недостаточно денег для уплаты налога!')
else:
    print('Ваших средств хватает для уплаты налога!')
