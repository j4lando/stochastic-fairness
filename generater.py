import random
import pandas as pd

def generate_data(num_samples, accuracy):
    """Generate random model output and expected output data as pandas DataFrames with specified accuracy."""
    ids = list(range(1, num_samples + 1))
    expected_output_data = pd.DataFrame({'id': ids, 'output': [random.choice([0, 1]) for _ in range(num_samples)]})
    model_output = expected_output_data.copy()

    # Adjust model_output to achieve the desired accuracy
    num_correct = int(num_samples * accuracy / 100)
    correct_indices = random.sample(range(num_samples), num_correct)

    for idx in range(num_samples):
        if idx not in correct_indices:
            # Flip the output to introduce incorrect predictions
            model_output.at[idx, 'output'] = 1 - expected_output_data.at[idx, 'output']

    print(f"Generated {num_samples} samples with {accuracy}% accuracy as pandas DataFrames.")
    return model_output, expected_output_data