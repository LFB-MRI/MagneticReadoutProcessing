def __fix_import_udpp__():
    try:
        import MRPudpp
    except Exception as e:
        import sys
        sys.path.insert(0, '..')

