# # read weights.npz(original E)
# import scipy.sparse as sp
# import pandas as pd

# def read_sparse_npz_file(file_path):
#     try:
#         sparse_matrix = sp.load_npz(file_path)
#         return sparse_matrix
#     except Exception as e:
#         print(f"读取npz文件时出错: {e}")
#         return None

# file_path = 'c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/weights.npz'

# sparse_matrix = read_sparse_npz_file(file_path)
# if sparse_matrix is not None:
#     print("稀疏矩阵:")
#     print(sparse_matrix)
#     print("稀疏矩阵转为密集矩阵:")
#     print(sparse_matrix.toarray())




# # read total_citation.npz(using)
# import scipy.sparse as sp
# import pandas as pd
# total_citation = pd.read_pickle('c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/total_citation.npz')
# print(total_citation.columns)
# print(total_citation.index)


# read pkl file(V)
import pickle

def read_pkl_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"读取pkl文件时出错: {e}")
        return None

file_path = 'c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/authors.pkl'

data = read_pkl_file(file_path)
if data is not None:
    print(data)
