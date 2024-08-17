def clean_line(line):
    translation_table = str.maketrans('', '', ',.=!;:-?')
    return line.lower().translate(translation_table)


def extract_words_from_file(file_name):
    words = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = clean_line(line)
            words.extend(line.split())
    return words


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = extract_words_from_file(file_name)
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            word_lower = word.lower()
            if word_lower in words:
                position = words.index(word_lower) + 1
                result[filename] = position
        return result

    def count(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            result[filename] = words.count(word.lower())
        return result


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
