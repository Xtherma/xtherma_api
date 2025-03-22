from .coordinator import XthermaDataUpdateCoordinator

class XthermaData:
    coordinator: XthermaDataUpdateCoordinator
    sensors_initialized: bool
    serial_fp: str
    unique_id: str

    def __init__(self, unique_id: str):
        self.coordinator = None
        self.sensors_initialized = False
        self.unique_id = unique_id
        self.serial_fp = "()"

