import numpy as np
import pandas as pd
import random
import math
import timeit



def sigma(_lambda, network_length, inclusion_probability):
    sigma = _lambda / (network_length * inclusion_probability)
    return sigma

def edge_from_index(edge_index, network_length):
    start_vertex = (edge_index // network_length)
    end_vertex = (edge_index %  network_length)

    return start_vertex , end_vertex



def no_self_loop(start_vertex, end_vertex):
    if(start_vertex == end_vertex):
        return 0
    return 1

# ==============================================



# ==============================================
# Skip Value Generator:

def zer_skip_value_generator(inclusion_probability):
    
    uniform_random_number = random.random()
    gen_skip_value = (int(math.log((1 - uniform_random_number),(1 - inclusion_probability))) - 1) 

    return gen_skip_value


def cumulative_probability_list(network_length, inclusion_probability):
    max_rand_gen = int((network_length * inclusion_probability) ** 2)
    cumulative_probability = 1 - inclusion_probability
    skip_probability_list =  np.zeros(max_rand_gen)
    for i in range(len(skip_probability_list)):
        skip_probability_list[i] = 1 - (cumulative_probability)**(i+1)

    return skip_probability_list

def prezer_skip_value_generator(skip_probability_list, inclusion_probability):
    
    list_iterator = 0
    uniform_random_number = random.random()
    max_rand_gen = len(skip_probability_list)
    while (list_iterator < max_rand_gen):
        
        if (skip_probability_list[list_iterator] > uniform_random_number):
            gen_skip_value = list_iterator         
            break

        list_iterator += 1     

        if (list_iterator == (max_rand_gen)):
            
            gen_skip_value = (int(math.log((1 - uniform_random_number),(1 - inclusion_probability))) - 1)

    gen_skip_value = (int(math.log((1 - uniform_random_number),(1 - inclusion_probability))) - 1) #////////////=========================================

    return gen_skip_value




    
# ==============================================
# Neurons Weight:

def excitatory_inhibitory_list(excitatory_probability, network_length):
    neurons_list = np.random.choice([1, -1], size=network_length, p=[(excitatory_probability), (1-excitatory_probability)])
    return neurons_list


def neurons_weight():
    
    weight = random.random()
    # weight = random.normalvariate(mu, sigma)

    return weight



def neuron_weight_sigma(sigma):
    weight = random.random() * (2 * sigma)
    return weight


# ==============================================

def add_edge_from_index_to_sparse(adjacency_sparse,excitatory_inhibitory_neurons_list, network_length, edge_index, edge_weight):

    new_edge = edge_from_index(edge_index, network_length)
    start_vertex = new_edge[0]
    end_vertex = new_edge[1]

    print(new_edge)
    
    if (0 <= start_vertex < network_length and no_self_loop(start_vertex, end_vertex)):
        
        excitatory_inhibitory_neuron_weight = edge_weight * excitatory_inhibitory_neurons_list[start_vertex]
        sparse_array = np.array([[start_vertex, end_vertex, excitatory_inhibitory_neuron_weight]])
        adjacency_sparse = np.append(adjacency_sparse, sparse_array, axis = 0)

    return adjacency_sparse


# Sparse Generators:

def prezer_network_sparse_generator(network_length, inclusion_probability, excitatory_probability, _lambda):
    _sigma = sigma(_lambda, network_length, inclusion_probability)
    skip_probability_list = cumulative_probability_list(network_length, inclusion_probability)
    excitatory_inhibitory_neurons_list = excitatory_inhibitory_list(excitatory_probability, network_length)
    adjacency_sparse = np.empty((0,3))
    max_edge = (network_length) ** 2
    edge_index =  -1
    
    while (edge_index < max_edge):
        

        edge_weight = neuron_weight_sigma(_sigma)
        skip_value = prezer_skip_value_generator(skip_probability_list, inclusion_probability)
        if(edge_index >= max_edge):
            break
        adjacency_sparse = add_edge_from_index_to_sparse(adjacency_sparse, excitatory_inhibitory_neurons_list, network_length, edge_index, edge_weight)
        edge_index += (1 + skip_value)


    adjacency_sparse_dataframe = pd.DataFrame(adjacency_sparse, columns=['start_vertex', 'end_vertex', 'edge_ewight'])
    return adjacency_sparse_dataframe
        




def zer_network_sparse_generator(network_length, inclusion_probability, excitatory_probability, _lambda):
    _sigma = sigma(_lambda, network_length, inclusion_probability)
    excitatory_inhibitory_neurons_list = excitatory_inhibitory_list(excitatory_probability, network_length)
    adjacency_sparse = np.empty((0,3))
    max_edge = (network_length) ** 2
    edge_index =  -1


    
    while (edge_index < max_edge):
        

        edge_weight = neuron_weight_sigma(_sigma)
        skip_value = zer_skip_value_generator(inclusion_probability)
        # if(edge_index >= max_edge):
        #     break
        adjacency_sparse = add_edge_from_index_to_sparse(adjacency_sparse, excitatory_inhibitory_neurons_list, network_length, edge_index, edge_weight)
        edge_index += (1 + skip_value)


    adjacency_sparse_dataframe = pd.DataFrame(adjacency_sparse, columns=['start_vertex', 'end_vertex', 'edge_ewight'])
    return adjacency_sparse_dataframe