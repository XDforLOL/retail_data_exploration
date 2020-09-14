import random


def costumer_id() -> int:
    return

def costumer_name() -> str:
    with open ('names.txt', 'r', encoding='utf-8') as f:
        first_name = random.choice(f.readlines())
        # if first_name.startswith():
        print(random.choice(first_name.split()), random.choice(first_name.split()))


def costumer_phone() -> str:
    region_num = str(random.randint(9, 999))
    second = str(random.randint(1,999)).zfill(3)
    last = (str(random.randint(1, 1000))).zfill(4)
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return f'{region_num}-{second}{last}'


def complete_dataset() -> tuple:
    return


if __name__ == '__main__':
    costumer_name()
    print(costumer_phone())
