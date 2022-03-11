import logging
import time

from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
from unicorn_fy.unicorn_fy import UnicornFy

from cryptogram import base

LOG = logging.getLogger()
FORMAT = ""


# anything_else
new_order = {
    "stream_type": "ORDER_TRADE_UPDATE",
    "event_type": "ORDER_TRADE_UPDATE",
    "event_time": 1644658129773,
    "symbol": "ETHUSDT",
    "client_order_id": "web_GifPFZUT7V7EgIiccmOF",
    "side": "BUY",
    "order_type": "LIMIT",
    "time_in_force": "GTC",
    "order_quantity": "0.057",
    "order_price": "2934.24",
    "order_avg_price": "0",
    "order_stop_price": "0",
    "current_execution_type": "NEW",
    "current_order_status": "NEW",
    "order_id": 8389765515802907901,
    "last_executed_quantity": "0",
    "cumulative_filled_quantity": "0",
    "last_executed_price": "0",
    "transaction_time": 1644658129767,
    "trade_id": 0,
    "net_pay": "167.25168",
    "net_selling_order_value": "0",
    "is_trade_maker_side": False,
    "reduce_only": False,
    "trigger_price_type": "CONTRACT_PRICE",
    "order_price_type": "LIMIT",
    "position_side": "BOTH",
    "order_realized_profit": "0",
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}

cancel_order = {
    "stream_type": "ORDER_TRADE_UPDATE",
    "event_type": "ORDER_TRADE_UPDATE",
    "event_time": 1644658555936,
    "symbol": "IOTAUSDT",
    "client_order_id": "0mEkRl1kMsdDnZ2bov2Rk5",
    "side": "SELL",
    "order_type": "TAKE_PROFIT",
    "time_in_force": "GTC",
    "order_quantity": "1350.9",
    "order_price": "0.9300",
    "order_avg_price": "0",
    "order_stop_price": "0.9300",
    "current_execution_type": "CANCELED",
    "current_order_status": "CANCELED",
    "order_id": 5043164675,
    "last_executed_quantity": "0",
    "cumulative_filled_quantity": "0",
    "last_executed_price": "0",
    "transaction_time": 1644658555931,
    "trade_id": 0,
    "net_pay": "0",
    "net_selling_order_value": "0",
    "is_trade_maker_side": False,
    "reduce_only": True,
    "trigger_price_type": "CONTRACT_PRICE",
    "order_price_type": "TAKE_PROFIT",
    "position_side": "BOTH",
    "order_realized_profit": "0",
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}

# anything_else
of_acc = {
    "stream_type": "ACCOUNT_UPDATE",
    "event_type": "ACCOUNT_UPDATE",
    "event_time": 1644658156875,
    "transaction": 1644658156861,
    "event_reason": "ORDER",
    "balances": [
        {
            "asset": "USDT",
            "wallet_balance": "779.04795602",
            "cross_wallet_balance": "408.18515009",
        }
    ],
    "positions": [
        {
            "symbol": "ETHUSDT",
            "position_amount": "0.057",
            "entry_price": "2934.24000",
            "accumulated_realized": "-393.47315001",
            "upnl": "0.04005083",
            "margin_type": "isolated",
            "isolated_wallet": "16.69171766",
            "position_side": "BOTH",
        }
    ],
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}
# anything_else
of_trade = {
    "stream_type": "ORDER_TRADE_UPDATE",
    "event_type": "ORDER_TRADE_UPDATE",
    "event_time": 1644658156875,
    "symbol": "ETHUSDT",
    "client_order_id": "web_GifPFZUT7V7EgIiccmOF",
    "side": "BUY",
    "order_type": "LIMIT",
    "time_in_force": "GTC",
    "order_quantity": "0.057",
    "order_price": "2934.24",
    "order_avg_price": "2934.24000",
    "order_stop_price": "0",
    "current_execution_type": "TRADE",
    "current_order_status": "FILLED",
    "order_id": 8389765515802907901,
    "last_executed_quantity": "0.057",
    "cumulative_filled_quantity": "0.057",
    "last_executed_price": "2934.24",
    "transaction_time": 1644658156861,
    "trade_id": 1424737840,
    "net_pay": "0",
    "net_selling_order_value": "0",
    "is_trade_maker_side": True,
    "reduce_only": False,
    "trigger_price_type": "CONTRACT_PRICE",
    "order_price_type": "LIMIT",
    "position_side": "BOTH",
    "order_realized_profit": "0",
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}


# anything_else
market_close_acc = {
    "stream_type": "ACCOUNT_UPDATE",
    "event_type": "ACCOUNT_UPDATE",
    "event_time": 1644658233548,
    "transaction": 1644658233542,
    "event_reason": "ORDER",
    "balances": [
        {
            "asset": "USDT",
            "wallet_balance": "778.95712493",
            "cross_wallet_balance": "424.78603666",
        }
    ],
    "positions": [
        {
            "symbol": "ETHUSDT",
            "position_amount": "0",
            "entry_price": "0.00000",
            "accumulated_realized": "-393.49709001",
            "upnl": "0",
            "margin_type": "isolated",
            "isolated_wallet": "0",
            "position_side": "BOTH",
        }
    ],
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}
# anything_else
market_close_of = {
    "stream_type": "ORDER_TRADE_UPDATE",
    "event_type": "ORDER_TRADE_UPDATE",
    "event_time": 1644658233548,
    "symbol": "ETHUSDT",
    "client_order_id": "web_62eyAHxaEbskYcHEDNOq",
    "side": "SELL",
    "order_type": "MARKET",
    "time_in_force": "GTC",
    "order_quantity": "0.057",
    "order_price": "0",
    "order_avg_price": "2933.82000",
    "order_stop_price": "0",
    "current_execution_type": "TRADE",
    "current_order_status": "FILLED",
    "order_id": 8389765515802964974,
    "last_executed_quantity": "0.057",
    "cumulative_filled_quantity": "0.057",
    "last_executed_price": "2933.82",
    "transaction_time": 1644658233542,
    "trade_id": 1424738791,
    "net_pay": "0",
    "net_selling_order_value": "0",
    "is_trade_maker_side": False,
    "reduce_only": True,
    "trigger_price_type": "CONTRACT_PRICE",
    "order_price_type": "MARKET",
    "position_side": "BOTH",
    "order_realized_profit": "-0.02394000",
    "unicorn_fied": ["binance.com-futures", "0.11.1"],
}


class BinanceWebSocketApiProcessStreams:
    def process_stream_data(
        self,
        received_stream_data_json,
        exchange="binance.com",
        stream_buffer_name="False",
    ):

        exchange = "binance.com-futures"

        #
        #  START HERE!
        #
        # `received_stream_data_json` contains one record of raw data from the stream
        # print it and you see the data like its given from Binance, its hard to work with them, because keys of
        # parameters are changing from stream to stream and they are not self explaining.
        #
        # So if you want, you can use the class `UnicornFy`, it converts the json to a dict and prepares the values.
        # `depth5` for example doesnt include the symbol, but the unicornfied set includes them, because the class
        # extracts it from the channel name, makes it upper size and adds it to the returned values.. just print both
        # to see the difference.
        # Github: https://github.com/LUCIT-Systems-and-Development/unicorn-fy
        # PyPI: https://pypi.org/project/unicorn-fy/
        if exchange == "binance.com" or exchange == "binance.com-testnet":
            unicorn_fied_stream_data = UnicornFy.binance_com_websocket(
                received_stream_data_json
            )
        elif (
            exchange == "binance.com-futures"
            or exchange == "binance.com-futures-testnet"
        ):
            unicorn_fied_stream_data = UnicornFy.binance_com_futures_websocket(
                received_stream_data_json
            )
        elif (
            exchange == "binance.com-margin" or exchange == "binance.com-margin-testnet"
        ):
            unicorn_fied_stream_data = UnicornFy.binance_com_margin_websocket(
                received_stream_data_json
            )
        elif (
            exchange == "binance.com-isolated_margin"
            or exchange == "binance.com-isolated_margin-testnet"
        ):
            unicorn_fied_stream_data = UnicornFy.binance_com_margin_websocket(
                received_stream_data_json
            )
        elif exchange == "binance.je":
            unicorn_fied_stream_data = UnicornFy.binance_je_websocket(
                received_stream_data_json
            )
        elif exchange == "binance.us":
            unicorn_fied_stream_data = UnicornFy.binance_us_websocket(
                received_stream_data_json
            )
        else:
            logging.error("Not a valid exchange: " + str(exchange))

        # Now you can call different methods for different `channels`, here called `event_types`.
        # Its up to you if you call the methods in the bottom of this file or to call other classes which do what
        # ever you want to be done.
        try:
            if unicorn_fied_stream_data["event_type"] == "aggTrade":
                self.aggtrade(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "trade":
                self.trade(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "kline":
                self.kline(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "24hrMiniTicker":
                self.miniticker(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "24hrTicker":
                self.ticker(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "depth":
                self.miniticker(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data["event_type"] == "ORDER_TRADE_UPDATE":
                self.order_update(unicorn_fied_stream_data)
            else:
                self.anything_else(unicorn_fied_stream_data)
        except KeyError:
            self.anything_else(unicorn_fied_stream_data)
        except TypeError:
            pass

    def aggtrade(self, stream_data):
        # print `aggTrade` data
        LOG.debug(f"aggTrade {stream_data}")

    def trade(self, stream_data):
        # print `trade` data
        LOG.debug(f"trade {stream_data}")

    def kline(self, stream_data):
        # print `kline` data
        LOG.debug(f"kline {stream_data}")

    def miniticker(self, stream_data):
        # print `miniTicker` data
        LOG.debug(f"miniTicker {stream_data}")

    def ticker(self, stream_data):
        # print `ticker` data
        LOG.debug(f"ticker {stream_data}")

    def depth(self, stream_data):
        # print `depth` data
        LOG.debug(f"depth {stream_data}")

    def outboundAccountInfo(self, stream_data):
        # print `outboundAccountInfo` data from userData stream
        LOG.debug(f"outboundAccountInfo {stream_data}")

    def executionReport(self, stream_data):
        # print `executionReport` data from userData stream
        LOG.debug(f"executionReport {stream_data}")

    def order_update(self, stream_data):
        if stream_data["current_execution_type"] == "TRADE":
            self.order_trade(stream_data)
        elif stream_data["current_execution_type"] == "NEW":
            self.order_new(stream_data)
        elif stream_data["current_execution_type"] == "CANCELED":
            self.order_canceled(stream_data)
        else:
            LOG.debug(f"order_update_else {stream_data}")

    def order_trade(self, stream_data):
        LOG.debug(f"order_trade {stream_data}")

    def order_new(self, stream_data):
        LOG.debug(f"order_new {stream_data}")

    def order_canceled(self, stream_data):
        LOG.debug(f"order_canceled {stream_data}")

    def anything_else(self, stream_data):
        LOG.debug(f"anything_else {stream_data}")


class Binance(base.Processor):
    def config(self, config):
        self.name = config['name']
        self.api_key = config["api_key"]
        self.api_secret = config["api_secret"]
        self.message = config["message"]
        self.exchange = config.get("exchange", "binance.com-futures")

    def _notify(self, stream_data):
        text = self.message.format(**stream_data)
        self.notify(text=text)

    def run(self):
        LOG.info("Starting binance %s", self.name)

        fmt = BinanceWebSocketApiProcessStreams()
        fmt.order_trade = self._notify

        # create instances of BinanceWebSocketApiManager
        ubwa = BinanceWebSocketApiManager(
            fmt.process_stream_data,
            exchange=self.exchange,
        )

        # create the userData streams
        ubwa.create_stream(
            "arr", "!userData", api_key=self.api_key, api_secret=self.api_secret
        )

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            LOG.info("Stopping ... just wait a few seconds!")
            ubwa.stop_manager_with_all_streams()
