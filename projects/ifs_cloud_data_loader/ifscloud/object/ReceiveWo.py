import json
from ifscloud.object.WorkOrder import WorkOrder

class ReceiveWo:
    def __init__(self, WorkOrder: WorkOrder):
            self.ReceiveWo = WorkOrder

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)