import pickle
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)
