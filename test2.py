from ws4py.client.threadedclient import WebSocketClient


class DummyClient(WebSocketClient):
    def opened(self):
        self.send('{"apikey": "a0398ad5cf0296745a0a517ac6013f70bae021b9", "channel": "bibox_sub_spot_ALL_ALL_login",'
                  '"event": "addChannel", "sign": "0a5acb574aa8880a075350974d33400f"}')

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)


if __name__ == '__main__':
    try:
        ws = DummyClient('wss://push.bibox.com/', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
