def __fix_import__():
    try:
        import MRP
    except Exception as e:
        import sys
        sys.path.insert(0, '..')
        sys.path.insert(0, '.')

#def __import_MRP__():
#    from MRP import MRPHal, MRPMagnetTypes, MRPHal, MRPReading, MRPMeasurementConfig, MRPMagnetTypes, MRPReadingEntry, MRPReadingEntry, MRPBaseSensor