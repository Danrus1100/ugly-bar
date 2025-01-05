import yuck.widgets as yuck
import hyprland.hyprland as hyprland
from settings_reader import Settings

def main():
    settings = Settings('hyprland_workspaces')

    workspaces: list[hyprland.Workspace] = hyprland.get_workspaces()
    workspaces.sort(key=lambda x: x.id)
    main_box = yuck.Box()
    main_box.space_evenly = False
    main_box.vexpand = True
    main_box.halign = "start"
    for workspace in workspaces:
        workspace_button = yuck.Button(onclick=f"hyprctl dispatch workspace {workspace.id}")
        workspace_button.append_child(yuck.Label(text=str(workspace.id)))
        if settings.show_icons == True:
            workspace_button.append_child(yuck.Image(icon='discord'))
        main_box.append_child(workspace_button)
        
    
    main_box.draw()

if __name__ == "__main__":
    main()