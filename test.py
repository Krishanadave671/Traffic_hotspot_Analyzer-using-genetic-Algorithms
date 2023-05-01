import random

# Define the binary representations for the 5 clusters
clusters = {
    'Cluster 1': '110',
    'Cluster 2': '001',
    'Cluster 3': '010',
    'Cluster 4': '111',
    'Cluster 5': '100'
}

# Define the objective function to maximize
def objective_function(solution):
    # Assign each location to a cluster based on the solution
    assignments = []
    for i in range(len(solution)):
        if solution[i] == '1':
            assignments.append(clusters[f'Cluster {i+1}'])
    # Calculate the total frequency of tweets across all locations
    total_frequency = 0
    for location in locations:
        for cluster in assignments:
            if cluster == location['cluster']:
                total_frequency += location['frequency']
                break
    # Return the total frequency
    return total_frequency

# Define the genetic algorithm
def genetic_algorithm(population_size, num_generations):
    # Initialize the population with random binary strings of length 5
    population = [ ''.join(random.choices(['0', '1'], k=5)) for i in range(population_size) ]
    # Evaluate each candidate solution
    fitness_scores = [ objective_function(solution) for solution in population ]
    # Loop over the generations
    for generation in range(num_generations):
        # Select the top 5 solutions
        top_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)[:5]
        top_solutions = [ population[i] for i in top_indices ]
        # Create new solutions using crossover and mutation
        new_population = []
        for i in range(population_size):
            if i < 5:
                # Copy over the top 5 solutions
                new_population.append(top_solutions[i])
            else:
                # Crossover two randomly selected top solutions
                parent1, parent2 = random.choices(top_solutions, k=2)
                crossover_point = random.randint(0, 4)
                child = parent1[:crossover_point] + parent2[crossover_point:]
                # Mutate the child with a small probability
                if random.random() < 0.1:
                    mutation_point = random.randint(0, 4)
                    child = child[:mutation_point] + ('0' if child[mutation_point] == '1' else '1') + child[mutation_point+1:]
                new_population.append(child)
        # Evaluate each new candidate solution
        fitness_scores = [ objective_function(solution) for solution in new_population ]
        # Update the population
        population = new_population
    # Return the best solution found
    best_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])
    return population[best_index]

# Define the locations as a list of dictionaries
locations = [
    {'id': 1, 'cluster': 'Cluster 1', 'latitude': 40.7128, 'longitude': -74.0060, 'frequency': 10},
    {'id': 2, 'cluster': 'Cluster 2', 'latitude': 51.5074, 'longitude': -0.1278, 'frequency': 20},
    {'id': 3, 'cluster': 'Cluster 1', 'latitude': 34.0522, 'longitude': -118.2437, 'frequency': 15},
    {'id': 4, 'cluster': 'Cluster 4', 'latitude': 39.9042, 'longitude': 116.4074, 'frequency': 30}
]


# Test the genetic algorithm
population_size = 20
num_generations = 10

best_solution = genetic_algorithm(population_size, num_generations)

print("Best solution found:", best_solution)


