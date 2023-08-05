import math
import networkx as nx

def sk(n, k):
    """Calculate the sum of the digits of a natural number n in base k"""
    sum_digits = 0
    while n > 0:
        sum_digits += n % k
        n //= k
    return sum_digits

def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings of equal length"""
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def build_bricklayers_graph(sequence_length):
    """Build a bricklayer's graph, simulating the way a bricklayer fills a Hamming graph"""
    G = nx.Graph()
    for i in range(2**sequence_length):
        binary_i = format(i, f'0{sequence_length}b')
        G.add_node(binary_i)
        for j in range(sequence_length):
            neighbor = list(binary_i)
            neighbor[j] = '0' if neighbor[j] == '1' else '1'
            G.add_edge(binary_i, ''.join(neighbor))
    return G

def maximal_robustness(graph, base=10):
    """Calculate the maximal robustness using the sums-of-digits function"""
    robustness = 0
    for node in graph.nodes:
        fraction = sum(hamming_distance(node, neighbor) for neighbor in graph.neighbors(node)) / len(graph.nodes)
        correction = sk(int(fraction * base**10), base)
        robustness += math.log(fraction) + correction
    return robustness / len(graph.nodes)

# Example usage
sequence_length = 5
bricklayers_graph = build_bricklayers_graph(sequence_length)
max_robustness = maximal_robustness(bricklayers_graph)

print("Maximal robustness of the bricklayer's graph:", max_robustness)
