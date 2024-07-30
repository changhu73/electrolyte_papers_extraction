import pickle
import numpy as np
import networkx as nx
from pyvis.network import Network
from sklearn.preprocessing import MinMaxScaler

with open('c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/author_weights.pkl', 'rb') as f:
    data = pickle.load(f)

G = nx.Graph()

# 做element_ID到数字的映射
id_list = list(data.keys())
id_mapping = {id_: i for i, id_ in enumerate(id_list)}

scaler = MinMaxScaler()
weights = np.array([data[id_][0] for id_ in id_list]).reshape(-1, 1)
scaled_weights = scaler.fit_transform(weights).flatten()

for id_, scaled_weight in zip(id_list, scaled_weights):
    G.add_node(id_mapping[id_], size=scaled_weight)

net = Network(notebook=True)

net.from_nx(G)


for node in net.nodes:
    node_id = node['id']
    node['size'] = G.nodes[node_id]['size'] * 200
    node['label'] = str(node_id)

# # testing for the nodes(too small)
# for node in net.nodes:
#     node_id = node['id']
#     node['size'] = max(G.nodes[node_id]['size'] * 200, 10)
#     node['label'] = str(node_id)

# # Gamma校正(替换三个)
# def gamma_correction(value, gamma=0.5):
#     return value ** gamma

# gamma_corrected_weights = np.array([gamma_correction(w) for w in scaled_weights])

# for id_, gamma_corrected_weight in zip(id_list, gamma_corrected_weights):
#     G.add_node(id_mapping[id_], size=gamma_corrected_weight)


net.show('author_weights_network.html')



