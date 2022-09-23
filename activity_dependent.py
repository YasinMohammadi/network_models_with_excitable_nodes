
# Numerical calculation of b(M)

def active_nodes(_spike_list):
    _atctive_nodes = sum(_spike_list)
    return _atctive_nodes


def branching_ratio(_spike_list):
    _branching_ratio = _branching_expectation_value / active_nodes(_spike_list)
    return _branching_ratio


# Avalanche statistics
def avalanche_size(_spike_list):
    _avalanche_size = sum(_spike_list)
    return _avalanche_size
