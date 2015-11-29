import core.events.Base

class Event(Base.Base):
    def __init__(eventType):
        self.type = eventType
        self.bubbles =False;
        self.cancelable= False;
        return;
    OBJECT_DETECTED = "object_detected"
    BEGIN= "begin"
    END = "end"
    ON = "on"
    OFF = "off"
    CHANGE = "update"
