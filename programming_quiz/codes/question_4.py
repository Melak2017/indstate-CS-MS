import urllib.request

def count_uppercase_chars(filename):
    count = 0
    with urllib.request.urlopen(filename) as f:
        for line in f:
            line = line.decode()  # convert bytes to string
            for char in line:
                if char.isupper():
                    count += 1
    return count

print(count_uppercase_chars('https://cs.indstate.edu/info/files/text/shakespeare_random_85.txt'))

