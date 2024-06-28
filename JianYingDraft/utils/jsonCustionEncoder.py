import dataclasses
import json

from JianYingDraft.utils.dataStruct import ColorData


class JsonCustomEncoder(json.JSONEncoder):

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, ColorData):
            return o.serialize()
        return super().default(o)
