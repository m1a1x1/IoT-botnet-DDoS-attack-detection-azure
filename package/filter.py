import copy

filter_fields = {
    "SrcIP"     : None,
    "DstIP"     : None,
    "SrcPort"   : None,
    "DstPort"   : None,
    "Transport" : None,
    "Protocol"  : None
  }

class Filters():
    def __init__(self, name="filters", real=False, fcnt=10) -> None:
        self.name = name
        self.fcnt = fcnt
        self.filters_state      = [ False for i in range(fcnt) ]
        self.filters_statistics = [ 0     for i in range(fcnt) ]
        self.filters_fields     = [ copy.deepcopy( filter_fields ) for i in range(fcnt) ]
        self.real = real

    def set_filters( self, new_filters_fields ):
        #TODO: запись полей фильтров в FPGA
        self.filters_fields = new_filters_fields

    def get_telemetries( self ):
        #TODO: чтение статистики по фильтрам из FPGA
        data = [ 0 for i in range(fcnt) ]

        data = {}
        data[self.name] = {"x"
        return 
        if self.real : 
            data[self.name] = self.adxl345.get_axes()
            return data
        else : 
            logger.debug('{} sensor is dummy and if you want values to test, please use generate_dummy_value in threshold class.'.format(self.name))
            return False

    def create_component_telemetry(self, data_dict):
        msg = self.create_telemetry(data_dict)
        msg.custom_properties["$.sub"] = self.name
        return msg
