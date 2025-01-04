from .__workspace__ import Workspace
from .__client__ import Client

import os
import json

def get_workspaces() -> list[Workspace]:
    workspaces = []
    info = json.loads(os.popen("hyprctl workspaces -j").read())
    for workspace in info:
        workspaces.append(Workspace(workspace["id"]))
    return workspaces