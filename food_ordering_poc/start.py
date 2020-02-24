from injection import get_injector
from micropy.axon_server_adapter.client import AxonServerClient

from micropy.core.command_handling.registry import CommandHandlingRegistry


def autodiscover():
    # TODO: implement real autodiscover
    # noinspection PyUnresolvedReferences
    from command import food_cart


injector = get_injector()
autodiscover()
axon_server_client = AxonServerClient('poc-foodordering')
axon_server_client.run()
commands = list(CommandHandlingRegistry.get_command_handlers())
axon_server_client.subscribe_commands(commands)
