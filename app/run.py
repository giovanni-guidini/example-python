"""Run a small calculator example with Sentry error reporting."""

import os

import sentry_sdk

from calculator import Calculator


def main():
    sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        send_default_pii=False,
    )

    print(Calculator.percentage(25, 0))


if __name__ == "__main__":
    main()
