from typing import List, Any, Union


def lottery():
    from random import seed
    from random import randint
    seed(100)
    nummers= []
    for i in range(10):
        random= randint(1, 10)
        for t in range(1):
            nummers.append(random)
    print(nummers)
lottery()

