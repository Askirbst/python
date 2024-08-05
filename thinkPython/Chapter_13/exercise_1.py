import string
import structshape

white_punc = string.whitespace + string.punctuation
new_str = ''

with open("example_file.txt") as file:
    file_content = file.read()

remove_table = str.maketrans("", "", white_punc)

new_str = file_content.translate(remove_table)

print(new_str.lower())
