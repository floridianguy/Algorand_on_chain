
import click

from bitcoinetl.cli.export_blocks_and_transactions import export_blocks_and_transactions
from bitcoinetl.cli.enrich_transactions import enrich_transactions
from bitcoinetl.cli.export_all import export_all
from bitcoinetl.cli.filter_items import filter_items
from bitcoinetl.cli.get_block_range_for_date import get_block_range_for_date
from bitcoinetl.cli.stream import stream


@click.group()
@click.version_option(version='1.5.1')
@click.pass_context
def cli(ctx):
    pass


# export
cli.add_command(export_blocks_and_transactions, "export_blocks_and_transactions")
cli.add_command(enrich_transactions, "enrich_transactions")
cli.add_command(export_all, "export_all")

# streaming
cli.add_command(stream, "stream")

# utils
cli.add_command(filter_items, "filter_items")
cli.add_command(get_block_range_for_date, "get_block_range_for_date")
