import random
import matplotlib.pyplot as plt


def main():
    numbers = []
    results = {}
    range_of_numbers = 45
    rounds = 100000

    for x in range(range_of_numbers):
        x = x + 1
        results[x] = 0
        numbers.append(x)

    for f in range(rounds):
        for i in range(6):
            results[draw(i, numbers, range_of_numbers)] += 1

    print(results)
    plt.bar(results.keys(), results.values())
    plt.xlabel('Zahlen')
    plt.ylabel('Anzahl der gezogenen Zahl')
    plt.title('Lottoziehungen')
    plt.show()

  
def draw(aufrufe, numbers, range_of_numbers):
    i = range_of_numbers - 1 - aufrufe
    index = random.randint(0, i)
    numbers[index], numbers[i] = numbers[i], numbers[index]
    return numbers[i]
    

if __name__ == "__main__":
    main()
