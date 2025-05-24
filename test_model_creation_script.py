import pickle

dummy_model = {"model": "test"}
with open("test_model.pkl", "wb") as f:
    pickle.dump(dummy_model, f)
