number_of_video_cards = int(input('Кол-во видеокарт: '))
list_of_cards = []
new_list_of_cards = []
top_card = 0

for i in range(number_of_video_cards):
    print(i + 1, 'Видеокарта: ', end='')
    video_card = int(input())
    list_of_cards.append(video_card)
    if video_card > top_card:
        top_card = video_card

for card in list_of_cards:
    if card != top_card:
        new_list_of_cards.append(card)

print('Старый список видеокарт: ', list_of_cards)
print('Новый список видеокарт:', new_list_of_cards)
