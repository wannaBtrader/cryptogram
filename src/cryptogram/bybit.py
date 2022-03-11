import logging
import time

from pybit import WebSocket

from cryptogram import base

DELAY = 10
LOG = logging.getLogger()


exec1 = [
    {
        "symbol": "XRPUSDT",
        "side": "Sell",
        "order_id": "d61c78da-ce24-4c50-8242-de3a821a111f",
        "exec_id": "99d4d52f-8a8a-57d5-8390-474b87988ad4",
        "order_link_id": "",
        "price": 0.7737,
        "order_qty": 23,
        "exec_type": "Trade",
        "exec_qty": 23,
        "exec_fee": 0.01334633,
        "leaves_qty": 0,
        "is_maker": False,
        "trade_time": "2022-02-12T08:12:19.984746Z",
    }
]

exec2 = [
    {
        "symbol": "XRPUSDT",
        "side": "Buy",
        "order_id": "f7f32e6a-0aa7-4543-9ceb-3bf910d68768",
        "exec_id": "97f2d58c-ddfb-5999-b03a-e24a995c3108",
        "order_link_id": "",
        "price": 0.7722,
        "order_qty": 23,
        "exec_type": "Trade",
        "exec_qty": 8,
        "exec_fee": 0.0046332,
        "leaves_qty": 15,
        "is_maker": False,
        "trade_time": "2022-02-12T08:13:08.851717Z",
    },
    {
        "symbol": "XRPUSDT",
        "side": "Buy",
        "order_id": "f7f32e6a-0aa7-4543-9ceb-3bf910d68768",
        "exec_id": "2bdd5fcd-c398-5b29-99f8-88b2958ba0dc",
        "order_link_id": "",
        "price": 0.7722,
        "order_qty": 23,
        "exec_type": "Trade",
        "exec_qty": 15,
        "exec_fee": 0.00868725,
        "leaves_qty": 0,
        "is_maker": False,
        "trade_time": "2022-02-12T08:13:08.851717Z",
    },
]


class ByBit(base.Processor):
    def config(self, config):
        self.name = config['name']
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.message = config["message"]

    def run(self):
        # Define your endpoint URLs and subscriptions.
        endpoint_private = "wss://stream.bybit.com/realtime_private"
        subs = [
            "execution",
            # "position",
        ]

        # Connect with authentication!
        ws_auth = WebSocket(
            endpoint_private,
            subscriptions=subs,
            api_key=self.api_key,
            api_secret=self.api_secret,
            logging_level=logging.DEBUG,
        )

        LOG.info("Starting bybit %s", self.name)

        while True:
            data = ws_auth.fetch("execution")
            # print(i, "EXEC", data)
            # print(i, 'TRADE', ws_auth.fetch('trade'))
            # print(i, 'POS', ws_auth.fetch('position'))
            if data:
                srows = [self.message.format(**row) for row in data]

                text = "\n".join(srows)
                self.notify(text=text)
            time.sleep(DELAY)
