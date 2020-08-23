from .services import Sport


def new_event_listener(event):
    topic = event.topic
    key = event.key
    data = event.value

    if topic == 'contests':
        Sport().handle_event(key=key, data=data)
