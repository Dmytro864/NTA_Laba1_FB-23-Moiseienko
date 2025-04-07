import matplotlib.pyplot as plt

# Дані для графіка
numbers = [2500744714570633849, 96267366284849, 123456789012345]
trial_times = {
    "Trial Division": [0.005, 0.002, 0.004],
    "Pollard's Rho": [0.03, 0.01, 0.02],
    "Miller-Rabin": [0.01, 0.005, 0.007]
}

# Створення графіка
plt.figure(figsize=(10, 6))

for label, times in trial_times.items():
    plt.plot(numbers, times, label=label, marker='o')

plt.xlabel('Число')
plt.ylabel('Час виконання (сек.)')
plt.title('Порівняння часу виконання алгоритмів факторизації')
plt.legend()
plt.grid(True)
plt.show()
