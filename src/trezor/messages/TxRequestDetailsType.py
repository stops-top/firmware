# Automatically generated by pb2py
import protobuf as p

class TxRequestDetailsType(p.MessageType):
    FIELDS = {
        1: ('request_index', p.UVarintType, 0),
        2: ('tx_hash', p.BytesType, 0),
        3: ('extra_data_len', p.UVarintType, 0),
        4: ('extra_data_offset', p.UVarintType, 0),
    }
