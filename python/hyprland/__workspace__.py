import os
import json
from .__client__ import Client

class Workspace():
    def __init__(self, id):
        self.id = id
        self.clients: list[Client] = []

    def set_clients(self):
        info = json.loads(os.popen("hyprctl clients -j").read())
        for client in info:
            if client["workspace"]["id"] == self.id:
                self.clients.append(Client(client["class"], client["title"], client["address"]))
    
    def switch_to(self):
        os.system(f"hyprctl dispatch workspace {self.id}")