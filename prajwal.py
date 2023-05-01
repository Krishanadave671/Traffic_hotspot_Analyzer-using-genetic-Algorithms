import itertools

def select_cluster_pair(cluster_data, max_distance):
    # Create a list of all possible cluster pairs
    cluster_pairs = list(itertools.combinations(range(len(cluster_data)), 2))
    
    # Calculate the total frequency of each cluster and store in a dictionary
    cluster_frequencies = {}
    for i in range(len(cluster_data)):
        cluster_frequencies[i] = sum([location[-1] for location in cluster_data[i]])
    
    # Find the pair of clusters with the highest sum of frequency that also satisfy the distance constraint
    best_pair = None
    best_frequency = 0
    for pair in cluster_pairs:
        distance = np.linalg.norm(np.array(cluster_data[pair[0]])[:,:-1] - np.array(cluster_data[pair[1]])[:,:-1])
        if distance <= max_distance:
            frequency = cluster_frequencies[pair[0]] + cluster_frequencies[pair[1]]
            if frequency > best_frequency:
                best_frequency = frequency
                best_pair = pair
    
    return best_pair
