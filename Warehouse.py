import os
import time

list = []

for address, dirs, files in os.walk('D:\\Тестовая папка'):
    for file in files:
        full = os.path.join(address, file)

        if time.time() - os.path.getatime(full) < 500:
            list.append(full)





for i in list:
    print(i)

print(time.time())
print(os.path.getatime(full))
print(time.time()-os.path.getatime(full))