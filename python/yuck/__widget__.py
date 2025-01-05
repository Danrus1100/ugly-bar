from typing import Literal

class Widget():
    def __init__(
            self, 
            css_class: str = "", 
            valign: Literal["fill", "baseline", "start", "end", "center"] = "fill", 
            halign: Literal["fill", "baseline", "start", "end", "center"] = "fill",
            vexpand: bool = False,
            hexpand: bool = False,
            width: int = 0,
            height: int = 0,
            active: bool = True,
            tooltip: str = "",
            visible: bool = True,
            style: str = "",
            css: str = "",
            **kwargs
        ):
        self.css_class: str = css_class
        self.valign: Literal["fill", "baseline", "start", "end", "center"] = valign
        self.halign: Literal["fill", "baseline", "start", "end", "center"] = halign
        self.vexpand: bool = vexpand
        self.hexpand: bool = hexpand
        self.width: int = width
        self.height: int = height
        self.active: bool = active
        self.tooltip: str = tooltip
        self.visible: bool = visible
        self.style: str = style
        self.css: str = css
        for key, value in kwargs.items():
            if key in self.DEFAULT_PROPERTIES:
                setattr(self, key, value)

        self.name: str = ""

        self.children: list[Widget] = []

        self.DEFAULT_PROPERTIES = {
            "css_class": "",
            "valign": "fill",
            "halign": "fill",
            "vexpand": False,
            "hexpand": False,
            "width": 0,
            "height": 0,
            "active": True,
            "tooltip": "",
            "visible": True,
            "style": "",
            "css": "",
        }
    
    def append_child(self, child: 'Widget'):
        if child is self:
            raise ValueError("Cannot add the widget to itself.")
        self.children.append(child)
    
    def insert_child(self, index: int, child: 'Widget'):
        if child is self:
            raise ValueError("Cannot add the widget to itself.")
        self.children.insert(index, child)
    
    def remove_child(self, child: 'Widget'):
        self.children.remove(child)
    
    def draw(self):
        print(self.__repr__())
    
    def __repr__(self):
        s = f"({self.name} "
        for default_param, default_value in self.DEFAULT_PROPERTIES.items():
            if getattr(self, default_param) != default_value:
                param_str = getattr(self, default_param)
                match str(type(param_str)):
                    case "<class 'int'>":
                        param_str = str(param_str)
                    case "<class 'str'>":
                        param_str = f"'{param_str}'"
                    case "<class 'bool'>":
                        param_str = str(param_str).lower()
                    case "<class 'float'>":
                        param_str = str(param_str)
                s += f":{default_param} {param_str} "
        for child in self.children:
            s += f"{child}"
        s += ")"
        return s
        