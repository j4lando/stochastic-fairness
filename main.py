import random
import pandas as pd
from generater import generate_data

def load_csv(model_output_file, output_file):
    """Load data from model_output and output CSV files into pandas DataFrames."""
    model_output, expected_output_data = [], []
    try:
        model_output = pd.read_csv(model_output_file, names=['id', 'output'])
        expected_output_data = pd.read_csv(output_file, names=['id', 'output'])
        print("Data loaded successfully into pandas DataFrames!")
    except Exception as e:
        print(f"Error loading files: {e}")
    return model_output, expected_output_data


def main():
    print("Welcome to the Data Noise Generator!")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Load model_output.csv and expected_output.csv")
        print("2. Generate model_output and expected_output data")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            model_output_file = input("Enter the model_output CSV filename: ").strip()
            expected_output_file = input("Enter the expected_output CSV filename: ").strip()
            model_output_data, expected_output_data = load_csv(model_output_file, expected_output_file)
            break
        elif choice == '2':
            num_samples = int(input("Enter the number of samples to generate: ").strip())
            accuracy = int(input("Enter the accuracy of the samples generated: ").strip())
            model_output_data, expected_output_data = generate_data(num_samples, accuracy)
            break
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")
            continue

    while True:
        print("\nPlease choose an option:")
        print("1. Apply noise to the model_output")
        print("2. Quit")  

        choice = input("Enter your choice (1/2): ").strip()
        
        if choice == '1':
            noise_chance = float(input("Enter the percentage chance to apply noise (0-100): ").strip())
            positive_noise_percentage = float(input("Enter the percentage of positive noise (0-100): ").strip())
            noisy_expected_output = apply_noise(model_output_data, noise_chance, positive_noise_percentage)
            compare_statistics(noisy_expected_output, expected_output_data)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            return 
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
