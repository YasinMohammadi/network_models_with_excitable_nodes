from activity_dependent import active_nodes
import sparse_graph
import spiking_neurons

import numpy as np
import random
import timeit



network_length = 10000
inclusion_probability = 0.01
excitatory_probability = 0.8
spike_probability = 0.2
_lambda = 2.5
active_nodes = 1

start = timeit.default_timer()#============================================
adjacency_sparse = sparse_graph.zer_network_sparse_generator(network_length, inclusion_probability, excitatory_probability, _lambda)
adjacency_sparse.to_csv('adjacency_sparse_N=10e4_p=0.01_eiP=0.8_lambda=2.5', index=False)
stop = timeit.default_timer()#===================================================
print('sparse_graph.prezer_network_sparse_generator Time: ', stop - start) #=====================================================


spike_list = spiking_neurons.spike_list_generator(network_length,active_nodes)


start = timeit.default_timer()#============================================
for index in range(10):
    spike_list = spiking_neurons.excite_network(adjacency_sparse, spike_list)
    stop = timeit.default_timer()#===================================================
    print('spiking_neurons.excite_network Time: ', stop - start) #=====================================================
    # print(spike_list,'\n')


# skip_probability_list = sparse_graph.cumulative_probability_list(network_length, inclusion_probability)
# print(skip_probability_list)