"Task69"
def read_file(file_path, line_by_line=False):
    try:
        with open(file_path,'r') as file:
            if line_by_line:
                file_content = file.readlines()
            else:
                file_content = file.read()
        return file_content
    except FileNotFoundError as e:
        print(f'''Opps ! File "{file_path}" is not found !
                  Make sure from the file path or create it first :)''')


def remove_symbols(symbols, text):
    if text != None:
        return text.strip(f"{symbols}")
    

def replace_empty_with_dashes(text):
    text_with_dashes = []
    for line in text:
        if line =='\n':
           text_with_dashes.append(f"{'--'*20}\n")
        else:
           text_with_dashes.append(line)
    return "".join(text_with_dashes)   


def captalize_text(text):
    if text != None:
        return text.upper()
    else:
        print('no text to captlize :( ')


def write_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except TypeError as e:
        print(e)


if __name__ == "__main__":

    file_path = 'file_1.txt'
    dest_path = 'file_2.txt'
    symbols = ' .#%&'

    orginal_content = read_file(file_path)
    print(f'Original content is:\n {orginal_content}\n')

    orginal_content_lines = read_file(file_path, line_by_line=True)
    content_with_dashes = replace_empty_with_dashes(orginal_content_lines)

    cleaned_content = remove_symbols(symbols, content_with_dashes)
    captlized_content = captalize_text(cleaned_content)
    write_to_file(dest_path, captlized_content)

    print(f'\nCaptlized cleaned content in file_2.txt:\n{read_file(dest_path)}')
