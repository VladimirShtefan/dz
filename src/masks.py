def get_mask_card_number(card_2: str):
    """Функция, маскирующая номер карты"""
    for _card in card_2:
        mask_1 = card_2.replace(card_2[6:-4], "******")
        result = mask_1
        return result


def get_mask_account(card_1: str):
    """"Функция, маскирующая номер счета"""
    for _card in card_1:
        mask_2 = card_1.replace(card_1[:-4], '**')
        result = mask_2
        return result
