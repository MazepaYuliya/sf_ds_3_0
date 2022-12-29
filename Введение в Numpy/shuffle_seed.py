import numpy as np

def shuffle_seed(array):
    '''
    Вы разрабатываете приложение для прослушивания музыки. Там будет доступна функция перемешивания плейлиста.
    Пользователю может понравиться перемешанная версия плейлиста, он захочет сохранить его копию. 
    Однако вы не хотите хранить в памяти новую версию плейлиста, а просто хотите сохранять тот seed, 
    с которым он был сгенерирован.

    Функция, которая принимает на вход массив из чисел, генерирует случайное число для seed 
    в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает кортеж: перемешанный с данным seed массив 
    (исходный массив должен оставаться без изменений), а также seed, с которым этот массив был получен.
    '''
    number_for_seed = np.random.randint(0, 2**32 - 1)
    np.random.seed(number_for_seed)   
    return (np.random.permutation(array), number_for_seed)

array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))