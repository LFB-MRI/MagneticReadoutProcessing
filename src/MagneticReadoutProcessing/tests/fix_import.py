def __fix_import__fix_import():
    #pass
    from pathlib import Path
    print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())