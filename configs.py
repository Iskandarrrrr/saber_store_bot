CATEGORIES = {
    'WOMEN': 'category/48/',
    'GIRLS': 'category/86/',
    'MAN': 'category/47/',
    'BOYS': 'category/49/',
    'ACCESSORS': 'category/96/'
}


def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v

