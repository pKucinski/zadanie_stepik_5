import hashlib
import random
import string
import time

def generate_md5_hash(strings):
    t = time.process_time()
    list_of_hash = []
    for string in strings:
        hash_object = hashlib.md5(string.encode())
        list_of_hash.append(hash_object.hexdigest())
    elapsed_time = time.process_time() - t
    return list_of_hash, elapsed_time

def generate_sha256_hash(strings):
    t = time.process_time()
    list_of_hash = []
    for string in strings:
        hash_object = hashlib.sha256(string.encode())
        list_of_hash.append(hash_object.hexdigest())
    elapsed_time = time.process_time() - t
    return list_of_hash, elapsed_time

def generate_sha3_hash(strings):
    t = time.process_time()
    list_of_hash = []
    for string in strings:
        hash_object = hashlib.sha3_256(string.encode())
        list_of_hash.append(hash_object.hexdigest())
    elapsed_time = time.process_time() - t
    return list_of_hash, elapsed_time

def generate_sha1_hash(strings):
    t = time.process_time()
    list_of_hash = []
    for string in strings:
        hash_object = hashlib.sha1(string.encode())
        list_of_hash.append(hash_object.hexdigest())
    elapsed_time = time.process_time() - t
    return list_of_hash, elapsed_time

def generate_blake2s_hash(strings):
    t = time.process_time()
    list_of_hash = []
    for string in strings:
        hash_object = hashlib.blake2s(string.encode())
        list_of_hash.append(hash_object.hexdigest())
    elapsed_time = time.process_time() - t
    return list_of_hash, elapsed_time


def generate_random_strings(length, loops):
    list_of_random_strings = []

    for _ in range(loops):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        list_of_random_strings.append(result_str)
    return list_of_random_strings


def count_duplicate_words(words_list):
    word_counts = {}
    for word in words_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    duplicate_count = 0
    for count in word_counts.values():
        if count > 1:
            duplicate_count += 1

    return duplicate_count


def measurement():
    length_of_strings = [10, 100, 1000, 10000, 1000000]
    for i in length_of_strings:
        strings = generate_random_strings(i, 10000)
        print("String length:", i)

        hash_list, time = generate_md5_hash(strings)
        collisions = count_duplicate_words(hash_list)
        print("MD5 - Time: ", time, " seconds", ", Collisions:", collisions, sep="")

        hash_list, time = generate_sha256_hash(strings)
        collisions = count_duplicate_words(hash_list)
        print("SHA-256 - Time: ", time, " seconds", ", Collisions:", collisions, sep="")

        hash_list, time = generate_sha3_hash(strings)
        collisions = count_duplicate_words(hash_list)
        print("SHA3-256 - Time: ", time, " seconds", ", Collisions:", collisions, sep="")

        hash_list, time = generate_sha1_hash(strings)
        collisions = count_duplicate_words(hash_list)
        print("SHA1 - Time: ", time, " seconds", ", Collisions:", collisions, sep="")

        hash_list, time = generate_blake2s_hash(strings)
        collisions = count_duplicate_words(hash_list)
        print("BLAKE2S - Time: ", time, " seconds", ", Collisions:", collisions, sep="")

        print("")




if __name__ == '__main__':
    measurement()