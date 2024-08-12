import json
from typing import List, Optional

from ifscloud.object.WorkTask import WorkTask

class WorkOrder:
    def __init__(self, RegDate: str, ErrDescr: str, OrgCode: str, Contract: str, OriginatingSystemId: str, 
                 WorkTaskArray: Optional[List['WorkTask']] = None):
        self.RegDate = RegDate
        self.ErrDescr = ErrDescr
        self.OrgCode = OrgCode
        self.Contract = Contract
        self.OriginatingSystemId = OriginatingSystemId
        self.WorkTaskArray = WorkTaskArray if WorkTaskArray is not None else []