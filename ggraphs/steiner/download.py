from pathlib import Path
import requests
import os

classes_problems = {
        'b' : {'max' : 18},
        'c' : {'max' : 20},
        'd' : {'max' : 20},
        'e' : {'max' : 20},
        'dv' : ['dv80.txt', 'dv160.txt', 'dv320.txt' ]
    }


def get_file(file_name):

    url = f'http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/{file_name}'
    response = requests.get(url)
    data = response.content

    return data

def save(content, file_name, folder):

    local = os.path.join(folder, file_name)

    with open(local, "wb") as file:
        file.write(content)

    return True


def generate_file_names(key = None):
    if isinstance(classes_problems[key], list) :
        for item in classes_problems[key]:
            yield item
    elif isinstance(classes_problems[key], dict) :
        counter = 1
        MAX = classes_problems[key]['max']
        while counter <= MAX :
            yield f"stein{key}{counter}.txt"
            counter += 1

def download(which='all'):
    print('start download...')

    OUTPUT_FOLDER = Path('downloads', 'ORLibrary')

    if not OUTPUT_FOLDER.exists():
        OUTPUT_FOLDER.mkdir(parents=True)


    files = None
    if which == 'all':
        files = [file for key in classes_problems.keys()
                    for file in generate_file_names(key) ]
    elif which in classes_problems:
        files = [file for file in generate_file_names(which)]
    elif isinstance(which, (list, tuple)) and all([a in classes_problems for a in which]):
        files = [file for key in which for file in generate_file_names(key)]
    else:
        raise AttributeError(f"which parameters does not correspond to any value expected: {which}")

    # download each file from files
    count = 1
    for f in files:
            data = get_file(f)
            save(data, f, OUTPUT_FOLDER)
            print(f'files: {count}', end="\r")
            count += 1

    count -= 1
    print(f'Obtained {count} files.')
