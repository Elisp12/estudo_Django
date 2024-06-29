from random import randint

from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')

def make_parts():
    return {
            'id' : fake.random_number(digits=2, fix_len=True),
            'title' : fake.sentence(nb_words=6),
            'description': fake.sentence(nb_words=12), 
            'quant_part':fake.random_number(digits=2, fix_len=True), # preparo
            'quant_uf': 'Unidades', #preparo
            'model': fake.random_number(digits=6,fix_len=True),#porcoes
            'model_record': 'Official',# porcoes
            'preparation_steps': fake.text(3000),
            'created_at': fake.date_time(),
            'author': {
                'firts_name': fake.first_name(),
                'last_name': fake.last_name(),
                },
            'category': {
                'name': fake.word(),
                },
            'cover': {
                'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
                }
            }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_parts())
