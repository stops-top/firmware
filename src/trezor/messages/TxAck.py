# Automatically generated by pb2py
import protobuf as p
from .TransactionType import TransactionType

class TxAck(p.MessageType):
    FIELDS = {
        1: ('tx', TransactionType, 0),
    }
    MESSAGE_WIRE_TYPE = 22
