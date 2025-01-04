from .__widget__ import Widget

class Image(Widget):
    def __init__(
            self,
            path: str = "",
            image_width: int = 0,
            image_height: int = 0,
            preserve_aspect_ratio: bool = True,
            fill_svg: str = "",
            icon: str = "",
            icon_size: str = "",
            **kwargs
    ):
        super().__init__()
        self.path = path
        self.image_width = image_width
        self.image_height = image_height
        self.preserve_aspect_ratio = preserve_aspect_ratio
        self.fill_svg = fill_svg
        self.icon = icon
        self.icon_size = icon_size

        for key, value in kwargs.items():
            if key in self.DEFAULT_PROPERTIES:
                setattr(self, key, value)

        self.name = "image"

        self.DEFAULT_PROPERTIES.update({
            "path": "",
            "image_width": 0,
            "image_height": 0,
            "preserve_aspect_ratio": True,
            "fill_svg": "",
            "icon": "",
            "icon_size": "",
        })