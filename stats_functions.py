import numpy as np

def diff_frac(data_A, data_B):
    frac_A = np.sum(data_A) / np.sum(split_test['Website_A']['Visits'])
    frac_B = np.sum(data_B) / np.sum(split_test['Website_B']['Visits'])
    return frac_B - frac_A

def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((data1['Orders'], data2['Orders']))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1['Visits'])]
    perm_sample_2 = permuted_data[len(data1['Visits']):]

    return perm_sample_1, perm_sample_2
    
def draw_perm_reps(data_1, data_2, func, size=1):
    """Generate multiple permutation replicates."""

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)
        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates
