import logging

from .services import Sport


def new_event_listener(event):
    topic = event.topic
    key = event.key
    data = event.value

    if topic == 'contests':
        try:
            Sport().handle_event(key=key, data=data)
        except Exception:
            logging.error("Sport event err")
