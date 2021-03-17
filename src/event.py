import logging

from .events import Contest


def new_event_listener(event):
    topic = event.topic
    key = event.key
    data = event.value

    if topic == 'contests':
        try:
            Contest().handle_event(key=key, data=data)
        except Exception as ex:
            print(ex)
            logging.error("Contest event err")
