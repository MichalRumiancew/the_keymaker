import string

ALPHABET = string.ascii_lowercase


def shift_characters(word, shift):
    new_word = ""
    for char in word:
        char_index = ALPHABET.index(char)
        new_index = (char_index + shift) % len(ALPHABET)
        new_word += ALPHABET[new_index]
    return new_word

    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    


def pad_up_to(word, shift, n):
    new_word = ""
    new_word += word
    while len(new_word) < n:
        next_word = shift_characters(word, shift)
        new_word += next_word
        word = next_word
    return new_word[:n]


    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    pass


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    word = input("Enter word to shift: ").lower()
    shift = int(input("Please select the shift: "))
    n = int(input("please provide a number of characters: "))
    result = pad_up_to(word, shift, n)
    print(result)
  
    # print(f'Your key: {hash_it(name)}')
