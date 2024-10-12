class Exercise:

    def __init__(self):
        pass

    def count_occurences(self, file_name, word):
        global stream
        try:
            stream = open(file_name)
            text = stream.read().lower().replace(',', ' ').replace('.', ' ')
            return text.split().count(word.lower())
        except Exception as e:
            print('Error occured: ', e)
        finally:
            stream.close()


if __name__ == '__main__':
    print(Exercise().count_occurences('first_text_file.txt', 'bit'))
