import json
from typing import List, Optional

from ifscloud.object.WorkTaskResource import WorkTaskResource
from ifscloud.object.WorkTaskAddress import WorkTaskAddress

class WorkTask:
    def __init__(self, Site: str, OrganizationSite: str, OrganizationId: str, Description: str, ExcludeFromScheduling: bool,
                 WorkTypeId: str, EarliestStart: str, LatestFinish: str, Duration: float, 
                 WorkTaskResourceArray: Optional[List['WorkTaskResource']] = None, 
                 WorkTaskAddressArray: Optional[List['WorkTaskAddress']] = None):
        self.Site = Site
        self.OrganizationSite = OrganizationSite
        self.OrganizationId = OrganizationId
        self.Description = Description
        self.ExcludeFromScheduling = ExcludeFromScheduling
        self.WorkTypeId = WorkTypeId
        self.EarliestStart = EarliestStart
        self.LatestFinish = LatestFinish
        self.Duration = Duration
        self.WorkTaskResourceArray = WorkTaskResourceArray if WorkTaskResourceArray is not None else []
        self.WorkTaskAddressArray = WorkTaskAddressArray if WorkTaskAddressArray is not None else []

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)