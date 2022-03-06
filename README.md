# cryptogram

Tired of crypto exchanges not notifying on executed trades?
Set this up and enjoy any sort of notification that can be done via command line.
Be it telegram, IFTTT, linux desktop notification, whatever.

## Configuration

Done with `~/.cryptogram.json`:

    {
      "exchanges":
        [
          {
            "type": "bybit",
            "name": "my bybit account",
            "api_key": "xxx",
            "api_secret": "yyy",
            "message": "bybit order executed: {side} {symbol} {exec_qty} {price}"
           },
          {
            "type": "binance",
            "name": "my binance account",
            "api_key": "zzz",
            "api_secret": "yyy",
            "exchange": "binance.com-futures",
            "message": "binance order executed: {side} {symbol} {last_executed_quantity} {last_executed_price}"
          }
        ],
      "notifications":
        [
          "telegram {text}"
        ]
    }

Any number of accounts can be added.
At the moment only bybit and binance exchange `type`s are supported.
Look into the appropriate source file to have an idea about the fields you can use for formatting the `message`.

Any number of notifications can be added.
**telegram** is a script that takes the text to notify. See https://github.com/fabianonline/telegram.sh

