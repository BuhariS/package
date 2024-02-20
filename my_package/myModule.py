def top_n_values(array, n):
    """
    Retrieve the top n values from an array.

    Parameters:
        array (list or numpy.ndarray): The input array.
        n (int): The number of top values to retrieve.

    Returns:
        list: The top n values from the array.
    """
    # Sort the array in descending order
    sorted_array = sorted(array, reverse=True)
    
    # Return the top n values
    return sorted_array[:n]
