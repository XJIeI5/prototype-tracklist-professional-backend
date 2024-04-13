calls_test = [
    {
        'name': 'Заказ №12314',
        'dateCreate': '18.04.24',
        'dateExpected': '28.04.24',
        'paid': True,
        'imageUrls': ['https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png'],
        'stageId': 3,
        'productTotals': 1
    },
    {
        'name': 'Заказ №14515',
        'dateCreate': '10.04.24',
        'dateExpected': '30.04.24',
        'paid': True,
        'imageUrls': ['https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png',
                      'https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png',
                      'https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png'],
        'stageId': 1,
        'productTotals': 3
    },
    {
        'name': 'Заказ №12151',
        'dateCreate': '20.04.24',
        'dateExpected': '27.04.24',
        'paid': False,
        'imageUrls': ['https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png'],
        'stageId': 0,
        'productTotals': 1
    },
    {
        'name': 'Заказ №12662',
        'dateCreate': '18.04.24',
        'dateExpected': '28.04.24',
        'paid': True,
        'imageUrls': ['https://detalneftehim.ru/wp-content/uploads/2020/11/bolty.png'],
        'stageId': 4,
        'productTotals': 1
    },
]