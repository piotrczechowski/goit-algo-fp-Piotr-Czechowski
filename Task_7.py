import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_throws(num_throws):

    dice_1 = np.random.randint(1, 7, num_throws)
    dice_2 = np.random.randint(1, 7, num_throws)
    sums = dice_1 + dice_2

   
    sum_counts = np.zeros(13, dtype=int)  # Sums range from 2 to 12
    for s in sums:
        sum_counts[s] += 1


    probabilities = sum_counts / num_throws

    return probabilities[2:]  

def display_results(probabilities):
    
    sums = np.arange(2, 13)
    theoretical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

    # console
    print(f"{'Sum':<5} {'Simulated Probability':<20} {'Theoretical Probability':<20}")
    print("-" * 45)
    for i, s in enumerate(sums):
        print(f"{s:<5} {probabilities[i]:<20.4%} {theoretical_probabilities[i]:<20.4%}")

    # graphic
    plt.figure(figsize=(10, 6))
    plt.bar(sums - 0.2, probabilities, width=0.4, label='Simulated', color='b')
    plt.bar(sums + 0.2, theoretical_probabilities, width=0.4, label='Theoretical', color='g')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Simulated vs Theoretical Probabilities of Dice Sums')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

num_throws = 1000000
probabilities = simulate_dice_throws(num_throws)

# console 
display_results(probabilities)
