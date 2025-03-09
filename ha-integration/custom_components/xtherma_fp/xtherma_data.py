from .coordinator import XthermaDataUpdateCoordinator

class XthermaData:
    coordinator: XthermaDataUpdateCoordinator
    sensors_initialized: bool
    model: str

    def __init__(self):
        self.coordinator = None
        self.sensors_initialized = False
        self.model = "()"

