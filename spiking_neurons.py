import numpy as np
import random



def spike_list_generator(network_length, active_nodes):
    spike_list = np.zeros(network_length, dtype=int)
    spike_list[:active_nodes] = 1
    np.random.shuffle(spike_list)
    # spike_list = np.random.choice([0, 1], size=network_length, p=[(1 - spike_probability), spike_probability])
    return spike_list



def neuron_neighbours(neuron_index, adjacency_sparse_dataframe):
    neighbours_dataframe = adjacency_sparse_dataframe.loc[adjacency_sparse_dataframe['end_vertex'] == neuron_index]
    neighbours = neighbours_dataframe.to_numpy()
    return neighbours



def neuron_activation_weight(neighbours, spike_list):
    weight = 0

    for neighbour in neighbours:
        neighbour_weight = neighbour[2]
        activision_status = spike_list[int(neighbour[0])]
        weight += neighbour_weight * activision_status
    return weight



def excite_network(adjacency_sparse_dataframe, spike_list):

    network_length = len(spike_list)
    new_spike_list = np.zeros(network_length)

    for neuron in range(network_length):
        neighbours = neuron_neighbours(neuron, adjacency_sparse_dataframe)
        activision_weight = neuron_activation_weight(neighbours, spike_list) 
        activision_chance = random.random()
        # if  (activision_weight > 0): new_spike_list[neuron] = 1
        if (activision_weight > 1):
            new_spike_list[neuron] = 1
        elif (activision_weight < activision_chance and activision_weight > 0):
            new_spike_list[neuron] = 1
            
    return new_spike_list



