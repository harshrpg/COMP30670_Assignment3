# -*- coding: utf-8 -*-

"""Console script for led_solve."""

import click
# import solve_led

@click.command()
def main(args=None):
    solve_led.solve_led()


if __name__ == "__main__":
    import sys
    sys.exit(main())
