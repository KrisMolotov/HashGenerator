import hashlib
import argparse
from enum import Enum
from random import randint


class HashFunctions(Enum):
    md4 = 'md4'
    md5 = 'md5'
    sha1 = 'sha1'
    sha256 = 'sha256'
    sha512 = 'sha512'

    def str(self):
        return self.value

    def get_hash_object(self):
        return hashlib.new(self.value)


class Encoding(Enum):
    ascii = 'ascii'
    utf8 = 'utf-8'
    utf16le = 'utf-16-le'
    utf16be = 'utf-16-be'

    def str(self):
        return self.value


def createParser():
    prs = argparse.ArgumentParser()
    prs.add_argument('--file', type=str, metavar='file')
    prs.add_argument('-e', '--encoding', type=Encoding, default=Encoding.ascii)
    prs.add_argument('-f', '--function', type=HashFunctions, default=HashFunctions.md5)
    prs.add_argument('-n', '--number', type=int)
    prs.add_argument('-o', '--output', type=str)
    return prs


parser = createParser()
args = parser.parse_args()
input_file = args.file
encoding = args.encoding.value
hash_function_name = args.function
number_of_hash_codes = args.number
output_file = args.output


def create_hash(hash_line):
    hash_object = hash_function_name.get_hash_object()
    hash_object.update(hash_line.encode(encoding=encoding))
    return hash_object.hexdigest()


with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
    i = 0
    line = input_file.readline()
    while i < number_of_hash_codes and len(line) != 0:
        hashed_line = create_hash(line.rstrip('\n'))
        output_file.write(hashed_line + '\n')
        i += 1
        line = input_file.readline()
    while i < number_of_hash_codes:
        random_number = str(randint(1, 1_000_000))
        hashed_line = create_hash(random_number)
        output_file.write(hashed_line + '\n')
        i += 1
