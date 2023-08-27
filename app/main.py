import shutil

def copy_file(source_file: str, target_file: str) -> None:
    """
    Copy a file from the source to the target location.

    Args:
        source_file (str): The path to the source file.
        target_file (str): The path to the target file.

    Returns:
        None
    """
    try:
        shutil.copy(source_file, target_file)
        print(f"File '{source_file}' copied to '{target_file}' successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' does not exist.")
    except IsADirectoryError:
        print(f"'{source_file}' is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")


copy_file("file.txt", "file-copy.txt")
