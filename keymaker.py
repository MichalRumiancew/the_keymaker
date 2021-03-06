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
    new_word = ""
    reversed_alphabet = ALPHABET[::-1]  # odwrócenie listy
    for letter in word:
        letter_index = ALPHABET.index(letter)
        new_letter = reversed_alphabet[letter_index]
        new_word += new_letter
    return new_word
    """
    >>> abc_mirror('abcd')
    'zyxw'    """


def create_matrix(word1, word2):
    new_words = []
    for char in word2:
        letter_index = ALPHABET.index(char)
        temp_word = shift_characters(word1, letter_index)
        new_words.append(temp_word)

    return new_words

    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """


def zig_zag_concatenate(matrix):
    new_word = ""

    for index in range(len(matrix[0])):
        temp_word = ""
        for word in matrix:
            temp_word += word[index]
        if index % 2 == 1:
            new_word += temp_word[::-1]  # odwrócenie słowa
        else:
            new_word += temp_word
    return new_word

    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """


def rotate_right(word, n):

    new_word = word[len(word)-n:] + word[:len(word)-n]
    return new_word

    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """


def get_square_index_chars(word):

    new_word = ""
    n = 0
    while n**2 <= len(word):
        new_word += word[n**2]
        n += 1
    return new_word

    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """


def remove_odd_blocks(word, block_length):
    new_word = ""

    word_as_list = list(word)
    sliced_blocks = [word_as_list[i:i + block_length]
                     for i in range(0, len(word_as_list), block_length)]

    for index, block in enumerate(sliced_blocks):

        if index % 2 == 0:
            new_word += "".join(block)

    return new_word

    """    
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    new_word = word[:n]
    rotated_word = rotate_right(new_word, -n//3)
    final_word = rotate_word[::-1]

    return final_word



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
    # n = int(input("please provide a number of characters: "))
    # result = pad_up_to(word, shift, n)
    # result = abc_mirror(word)
    # word1 = input("Please enter word 1: ").lower()
    # word2 = input("Please enter word 2: ").lower()
    # result = create_matrix(word1, word2)
    # print(result)
    # name = input("Enter your name: ").lower()
    # matrix = create_matrix(name, name)
    # result = zig_zag_concatenate(matrix)
    # result = rotate_right(word, n)
    result = remove_odd_blocks(word, shift)
    print(result)

    # print(f'Your key: {hash_it(name)}')
