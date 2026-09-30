import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Глобальные переменные
k = 120
t = 0
T = 300
r= [random.randint(-3, 3)for _ in range(60)]  # список случайных чисел для демонстрации
def f1():
    global t, T ,r# Даем функции доступ к изменению времени и температуры
    
    # 1. Создаем окно и настраиваем график ОДИН РАЗ до начала цикла
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("АСУ ТП: График изменения температуры турбины")
    ax.set_xlabel("Время (секунды)")
    ax.set_ylabel("Температура (°C)")
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 1300)
    ax.grid(True)
    
    # Создаем пустую линию, которую будем обновлять
    line, = ax.plot([], [], 'r-o', linewidth=2) 

    # Списки для хранения истории создаем ДО цикла, чтобы они не обнулялись
    x_data = []
    y_data = []

    for i in range(60):
        # Шаг времени (увеличиваем t на 1 каждую итерацию)
        t += 1
        
        time.sleep(0.1) # Задержка для анимации
        
        # Считаем физику
        T1 = r[i] - T + k * np.sqrt(t)+r[i]
        print(f"Секунда {t}: Температура = {round(T1, 1)} °C")
        
        # Сначала добавляем новые точки в списки истории
        x_data.append(t)
        y_data.append(T1)
        
        # Обновляем координаты нашей ЕДИНСТВЕННОЙ линии
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        
        # Перерисовываем экран
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.01)

        # Проверяем на аварию
        if T1 > 1200:
            print(f"\n[АВАРЯ!] Турбина перегрелась на секунде {t}! Текущая температура: {round(T1, 1)} °C")
            print("Система АСУ ТП активирует аварийную остановку!")
            break
    else:
        # Этот блок сработает, ТОЛЬКО если цикл завершился сам (без break)
        print("\nСистема работает стабильно. Перегрева не обнаружено.")

# Запуск функции
f1()
plt.show()
