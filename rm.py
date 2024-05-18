import sys
import os
import shutil

def create_trash_dir():
    trash_dir = os.path.expanduser('~/rm_trash')
    if not os.path.exists(trash_dir):
        os.makedirs(trash_dir)
    return trash_dir

def handle_duplicate(trash_dir, file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_base_name = "{}-{}{}".format(name, counter, ext)
    new_full_path = os.path.join(trash_dir, new_base_name)
    while os.path.exists(new_full_path):
        counter += 1
        new_base_name = "{}-{}{}".format(name, counter, ext)
        new_full_path = os.path.join(trash_dir, new_base_name)
    return new_full_path

def move_to_trash(trash_dir, file_path):
    if not os.path.exists(file_path):
        print("rm.py: cannot remove '{}': No such file or directory".format(file_path), file=sys.stderr)
        return
    target_path = os.path.join(trash_dir, os.path.basename(file_path))
    if os.path.exists(target_path):
        target_path = handle_duplicate(trash_dir, file_path)
    shutil.move(file_path, target_path)

def main():
    if '-r' in sys.argv:
        recursive = True
        sys.argv.remove('-r')
    else:
        recursive = False
    paths = sys.argv[1:]
    trash_dir = create_trash_dir()
    for path in paths:
        if os.path.isdir(path) and not recursive:
            print("rm.py: cannot remove '{}': Is a directory".format(path), file=sys.stderr)
            continue
        if os.path.isdir(path) and recursive:
            move_to_trash(trash_dir, path)
        elif os.path.isfile(path):
            move_to_trash(trash_dir, path)
        else:
            print("rm.py: cannot remove '{}': No such file or directory".format(path), file=sys.stderr)

if __name__ == '__main__':
    main()
