from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMessageRequest(_message.Message):
    __slots__ = ("name", "msg")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    name: str
    msg: str
    def __init__(self, name: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...

class ChatMessageResponse(_message.Message):
    __slots__ = ("name", "msg")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    name: str
    msg: str
    def __init__(self, name: _Optional[str] = ..., msg: _Optional[str] = ...) -> None: ...
