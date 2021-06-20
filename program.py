import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry, we can\'t search that location.')
        return
    text = get_search_text_from_user()
    if not text:
        print('Sorry, we can\'t search for nothing.')
        return

    matches = search_folders(folder,text)
    match_count = 0
    for m in matches:
        match_count += 1
        # print(f"\n{'-' * 10} MATCH {'-' * 10}")
        # print("file: " + m.file)
        # print(f"line: {m.line}")
        # print('match: ' + m.text.strip())

    print(f"Found {match_count} matches.")

def print_header():
    print(f"{'-' * 50}")
    print(f"{' ' * 17}" + "File Search App")
    print(f"{'-' * 50}")

def get_folder_from_user():
    folder = input('What folder do you want to search? \n \n >>> ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def get_search_text_from_user():
    text = (input('What phrase are you looking for? *** Single Phrases Only*** \n \n >>> ')).lower()
    return text

def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:


        line_num = 0
        for line in fin:
            line_num += 1
            if line.find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m


def search_folders(folder,text):

    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)

    return all_matches

if __name__ == '__main__':
    main()