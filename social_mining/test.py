# # read npz file
import numpy as np

def read_npz_file(file_path):
    try:
        data = np.load(file_path)
        data_dict = {key: data[key] for key in data}
        return data_dict
    except Exception as e:
        print(f"读取npz文件时出错: {e}")
        return None

file_path = 'c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/weights.npz'

data_dict = read_npz_file(file_path)
if data_dict is not None:
    for key, value in data_dict.items():
        print(f"键: {key}, 值: {value}")




# # read pkl file
# import pickle

# def read_pkl_file(file_path):
#     try:
#         with open(file_path, 'rb') as file:
#             data = pickle.load(file)
#         return data
#     except Exception as e:
#         print(f"读取pkl文件时出错: {e}")
#         return None

# file_path = 'c:/Users/13772/OneDrive/文档/GitHub/electrolyte_papers_extraction/social_mining/authors.pkl'

# data = read_pkl_file(file_path)
# if data is not None:
#     print(data)
