# -*- coding: utf-8 -*-

"""Console script for led_solve."""

import click


@click.command()
def main(args=None):
    """Console script for led_solve."""
    click.echo("Replace this message by putting your code into "
               "led_solve.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
