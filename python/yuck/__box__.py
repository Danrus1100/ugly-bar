from .__widget__ import Widget

class Box(Widget):

    def __init__(
            self, 
            spacing: int = 0,
            orientation: str = "h",
            space_evenly: bool = False,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.spacing = spacing
        self.orientation = orientation
        self.space_evenly = space_evenly

        for key, value in kwargs.items():
            if key in self.DEFAULT_PROPERTIES:
                setattr(self, key, value)

        self.name = "box"

        self.DEFAULT_PROPERTIES.update({
            "spacing": 0,
            "orientation": "h",
            "space_evenly": False,
        })
        