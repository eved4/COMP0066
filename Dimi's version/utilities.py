import pickle


def unpickle_data(file_name):
    """
    Loads data from a pickled text file. Returns empty dictionary if the file is empty.
    """
    infile = open(file_name, "rb")
    try:
        data = pickle.load(infile)
    except:
        data = {}
    infile.close()

    return data


def pickle_data(file_name, data):
    """
    Pickles any data type into a text file.
    """
    outfile = open(file_name, "wb")
    pickle.dump(data, outfile)
    outfile.close()
