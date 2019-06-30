import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print('### opened ###')
    ws.send('{"apikey": "a0398ad5cf0296745a0a517ac6013f70bae021b9", "channel": "bibox_sub_spot_ALL_ALL_login", '
            '"event": "addChannel", "sign": "0a5acb574aa8880a075350974d33400f"}')


if __name__ == "__main__":
    try:
        print(f'start balance websocket')

        ws = websocket.WebSocketApp(
            "wss://push.bibox.com/",
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close)

        ws.run_forever()
    except KeyboardInterrupt:
        exit()
