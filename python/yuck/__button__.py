from .__widget__ import Widget

class Button(Widget):
    
    def __init__(
            self, 
            timeout: str = "200ms",
            onclick: str = "",
            onmiddleclick: str = "",
            onrightclick: str = "",
            **kwargs
    ):
        super().__init__(**kwargs)
        self.timeout = timeout
        self.onclick = onclick
        self.onmiddleclick = onmiddleclick
        self.onrightclick = onrightclick

        for key, value in kwargs.items():
            if key in self.DEFAULT_PROPERTIES:
                setattr(self, key, value)

        self.name = "button"

        self.DEFAULT_PROPERTIES.update({
            "timeout": "200ms",
            "onclick": "",
            "onmiddleclick": "",
            "onrightclick": "",
        })