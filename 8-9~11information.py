messages = ['aaa', 'bbb', 'ccc']


def show_message(messages):
    for message in messages:
        print(message)


show_message(messages)
sent_messages = []


def sent(messages):
    while messages:
        sented = messages.pop()
        sent_messages.append(sented)


sent(messages[:])
print(messages)
print(sent_messages)
