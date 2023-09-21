from MRP import MRPReading, MRPAnalysis

import inspect
from optparse import OptionParser
from UDPPFFunctionCollection import UDPFFunctionCollection
def foo(a, b, x='blah'):
    pass


# (a, b, x='blah')

class UDPPFunctionTranslator():
    @staticmethod
    def strip_function_parameter_types(_typestr: str) -> str:
        return _typestr.replace("<class '", "").replace("'>", "")

    @staticmethod
    def listfunctions() -> dict:
        method_list = [func for func in dir(UDPFFunctionCollection) if callable(getattr(UDPFFunctionCollection, func)) and not func.startswith("__")]

        resultdict = {}

        for method in method_list:
            # get function object by name:string
            function_obj = getattr(UDPFFunctionCollection, method)
            # get
            inspect_result: inspect.FullArgSpec = inspect.getfullargspec(function_obj)


            return_type = None
            parameter_types = {}
            for k in inspect_result.annotations:
                v= inspect_result.annotations[k]

                if k == 'return':
                    return_type = UDPPFunctionTranslator.strip_function_parameter_types(str(v))
                else:
                    parameter_types[k] = UDPPFunctionTranslator.strip_function_parameter_types(str(v))

            resultdict[method] = {
                'name': method,
                'parameter_names': inspect_result.args,
                'parameter_types': parameter_types,
                'default': inspect_result.defaults,
                'return': return_type
            }
            # inspect_result.annotations['return'][0]
            #print(inspect_result)

        return resultdict
    def __init__(self):
        pass


