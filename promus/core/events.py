import Base from promus.core.Base

class Event(Base):
    def __init__(eventType):
        self.type = eventType
        self.bubbles =False
        self.cancelable= False
        self.target = None
        return;
    OBJECT_DETECTED = "object_detected"
    START= "start"
    COMPLETE = "complete"
    ON = "on"
    OFF = "off"
    CHANGE = "update"

class EventDispatcher(Base.Base):
    def __init__():
        self.__subscribers = []
        return;
    def addEventListener(eventName,eventHandler):
        if (!self.__subscribers[eventName]):
                self.__subscribers[eventName]=[]
        self.__subscribers[eventName].append(eventHandler)
    def dispatchEvent(event):
        for eventHandler in self.__subscribers[eventName]:
            eventHandler(event)
        return;
