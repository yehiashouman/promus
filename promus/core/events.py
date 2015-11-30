
from promus.core.Base import Base
class Event(Base):
    def __init__(self,eventType):
        super(Event,self).__init__()
        self.type = eventType
        self.bubbles =False
        self.cancelable= False
        self.target = None
        return;
    EVT_OBJECT_DETECTED = "object_detected"
    EVT_START= "start"
    EVT_COMPLETE = "complete"
    EVT_ON = "on"
    EVT_OFF = "off"
    EVT_CHANGE = "update"

class EventDispatcher(Base):
    def __init__(self):
        super(EventDispatcher,self).__init__()
        #TODO: Make subscribers list dynamically filled
        self.__subscribers = {"complete":[],"start":[],"on":[],"off":[],"flash":[]}
        return;

    def addEventListener(self,eventName,eventHandler):
        if (eventName in self.__subscribers.keys()==False):
                self.__subscribers[eventName]=[]
        self.__subscribers[eventName].append(eventHandler)

    def dispatchEvent(self,event):
        for subscriber in self.__subscribers[event.type]:
            subscriber(event)
        return;
