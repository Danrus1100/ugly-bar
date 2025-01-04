from .__widget__ import Widget

class Label(Widget):
    def __init__(
            self,
            text: str = "",
            turncate: bool = False,
            limit_width: int = 0,
            turncate_left: bool = False,
            show_truncated: bool = False,
            unindent: bool = False,
            markup: str = "",
            warp: bool = False,
            angle: float = 0.0,
            gravity: str = "auto",
            xalign: float = 0.5,
            yalign: float = 0.5,
            justify: str = "center",
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.turncate = turncate
        self.limit_width = limit_width
        self.turncate_left = turncate_left
        self.show_truncated = show_truncated
        self.unindent = unindent
        self.markup = markup
        self.warp = warp
        self.angle = angle
        self.gravity = gravity
        self.xalign = xalign
        self.yalign = yalign
        self.justify = justify

        for key, value in kwargs.items():
            if key in self.DEFAULT_PROPERTIES:
                setattr(self, key, value)
        
        self.DEFAULT_PROPERTIES.update({
            "text": "",
            "turncate": False,
            "limit_width": 0,
            "turncate_left": False,
            "show_truncated": False,
            "unindent": False,
            "markup": "",
            "warp": False,
            "angle": 0.0,
            "gravity": "auto",
            "xalign": 0.5,
            "yalign": 0.5,
            "justify": "center",
        })

        self.name = "label"