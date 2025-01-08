import pickle
data = {'name': 'John', 'age': 30, 'is_student': False}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
