# Python-based Replacement for rm Command

## Overview
This project contains `rm.py`, a Python script that serves as an alternative to the traditional UNIX `rm` command. Instead of permanently deleting files, `rm.py` moves them to a designated trash directory (`~/rm_trash`). This approach allows for the recovery of files, adding a layer of safety to file deletion.

## Features

- **Safe Deletion**: Moves files to `~/rm_trash` instead of permanent deletion.
- **Duplicate Handling**: Automatically manages duplicates by appending a number to the filenames if a file with the same name already exists in the trash.
- **Recursive Deletion**: Supports recursive deletion with the `-r` option, allowing entire directories to be moved to the trash.
- **Error Handling**: Provides clear error messages for non-existent files or attempts to delete directories without the recursive option.

## Usage

### Basic Command
To move files to the trash, simply pass the paths as arguments:
```bash
python rm.py /path/to/file1 /path/to/file2
