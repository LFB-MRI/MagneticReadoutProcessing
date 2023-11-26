from MRP import MRPHal, MRPReadingSource, MRPReadingSourceStatic, MRPReadingSourceFullsphere

class MRPReadingSourceHelper:


    @staticmethod
    def createReadingSourceInstance(_hal: MRPHal.MRPHal) -> MRPReadingSource.MRPReadingSource:

        caps: [str] = _hal.get_sensor_capabilities()

        if len(caps) <= 0:
            raise MRPReadingSource.MRPReadingSourceException("createReadingSourceInstance given hal sensor capabilities are empty")

        if 'fullsphere' in caps and 'static' in caps:
            return MRPReadingSourceFullsphere.MRPReadingSourceFullsphere(_hal)
        elif 'static' in caps:
            return MRPReadingSourceStatic.MRPReadingSourceStatic(_hal)
        else:
            raise Exception("createReadingSourceInstance no readingsource class implemented")


