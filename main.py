import random
import time


def keyspace(n):
    return 2 ** n


def random_value(length):
    return hex(random.getrandbits(length))


def brute_force(key):
    value = 0
    timer = round(time.time() * 1000)
    while hex(value) != key:
        value += 1
    timer = round(time.time() * 1000) - timer
    print(f'{key} - {timer}')


keys_length = []
random_keys = []

print('\nПространства ключей:')
i = 8
while 1:
    keys_length.append(i)
    print(f'{i} - {keyspace(i)}')
    if i == 4096:
        break
    i += i

i = 0
print('\nСлучайно сгенерированные ключи:')
for kl in keys_length:
    random_keys.append(random_value(kl))
    print(f'{kl} - {random_keys[i]}')
    i += 1

print('\nВремя, потраченное на брут-форс ключей, в миллисекундах:')
for rk in random_keys:
    brute_force(rk)
