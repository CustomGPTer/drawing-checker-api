from fuzzywuzzy import fuzz

def is_similar_filename(name1, name2, threshold=90):
    return fuzz.ratio(name1.lower(), name2.lower()) >= threshold
