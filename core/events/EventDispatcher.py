import core.events.Base

class EventDispatcher(Base.Base):
    def __init__():
        self.subscribers = []
        return;
    def addEventListener(eventName,eventHandler):
        if (!self.subscribers[eventName]):
                self.subscribers[eventName]=[];
        self.subscribers[eventName].append(eventHandler)
    def dispatchEvent(event):
        for eventHandler in self.subscribers[eventName]:
            eventHandler(event)
        return;
