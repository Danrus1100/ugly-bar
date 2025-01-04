import yuck.widgets as yuck
import hyprland.hyprland as hyprland

def main():
    workspaces: list[hyprland.Workspace] = hyprland.get_workspaces()
    workspaces.sort(key=lambda x: x.id)
    main_box = yuck.Box()
    for workspace in workspaces:
        workspace_button = yuck.Button(onclick=f"hyprctl dispatch workspace {workspace.id}")
        workspace_button.append_child(yuck.Label(text=workspace.id))
        main_box.append_child(workspace_button)
    
    print(main_box)

if __name__ == "__main__":
    main()