import psutil                                       #библиотека для работы с системными данными

interfaces = psutil.net_if_stats()                  #записываем данные о состоянии всех сетевых интерфейсов

for interface, stats in interfaces.items():         #перебираем данные и выводим их

    print(f"Интерфейс: {interface}")                #название интерфейса

    print(f"  Активен: {stats.isup}")               #состояние интерфейса

    print(f"  Скорость:  {stats.speed} Мбит/с")       #скорость соединения

    if stats.duplex == 2:
        duplex_mode = 'Duplex'
    elif stats.duplex == 1:
        duplex_mode = 'Half-duplex'
    else:
        duplex_mode = 'Unavailable'

    print(f"  Duplex mode: {duplex_mode} ")           #режим работы интерфейса

    print(f"  MTU: {stats.mtu}\n")                   #максимальный размер пакета