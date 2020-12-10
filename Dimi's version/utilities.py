import pickle


def unpickle_data(file_name):
    # Load the list of patients from the pickled file; create and empty list if the pickled file is empty
    infile = open(file_name, "rb")
    try:
        data = pickle.load(infile)
    except:
        data = {}
    infile.close()

    return data


def pickle_data(file_name, data):
    # Pickle the list of patients into a file
    outfile = open(file_name, "wb")
    pickle.dump(data, outfile)
    outfile.close()
