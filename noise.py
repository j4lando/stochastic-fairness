import random
import pandas as pd

def apply_noise(model_output_data, noise_chance, positive_noise_percentage):
    """Apply noise to the expected output data based on user-defined percentages."""
    noisy_data = model_output_data.copy()
    for idx, row in noisy_data.iterrows():
        if random.random() < noise_chance / 100:
            # Decide whether noise flips to positive or negative
            if random.random() < positive_noise_percentage / 100:
                noisy_data.at[idx, 'output'] = 1  # Positive noise
            else:
                noisy_data.at[idx, 'output'] = 0  # Negative noise

    return noisy_data


def compare_statistics(model_output, model_expected_output):
    """Compare model output to expected output and print statistics."""
    # Merge data on 'id' to align outputs
    merged = pd.merge(model_output, model_expected_output, on='id', suffixes=('_predicted', '_expected'))
    
    # Extract necessary columns
    predicted = merged['output_predicted']
    expected = merged['output_expected']
    
    # Calculate statistics
    total = len(merged)
    correct = (predicted == expected).sum()
    accuracy = correct / total * 100
    
    false_positives = ((predicted == 1) & (expected == 0)).sum() / total * 100
    false_negatives = ((predicted == 0) & (expected == 1)).sum() / total * 100
    
    # Print statistics
    return accuracy, false_positives, false_negatives


def display_statistics(accuracy, false_positives, false_negatives):
    print("Comparison Statistics:")
    print(f"Overall Accuracy: {accuracy:.2f}%")
    print(f"False Positives: {false_positives:.2f}%")
    print(f"False Negatives: {false_negatives:.2f}%")
    
def apply_noise_simulation(model_output_data, model_expected_output, noise_chance, positive_noise_percentage, epochs):
    overall_accuracy, overall_false_positives, overall_false_negatives = 0.0,0.0,0.0 
    for i in range(epochs):
        noisy_data = apply_noise(model_output_data, noise_chance, positive_noise_percentage)
        accuracy, false_positives, false_negatives = compare_statistics(noisy_data, model_expected_output)
        overall_accuracy += accuracy
        overall_false_positives += false_positives
        overall_false_negatives += false_negatives

    print(f"Noise applied successfully {epochs} times!")

    display_statistics(overall_accuracy / epochs, overall_false_positives / epochs, overall_false_negatives / epochs)