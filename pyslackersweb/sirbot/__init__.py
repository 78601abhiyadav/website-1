import logging

from aiohttp import web

from pyslackersweb.sirbot.views import routes

logger = logging.getLogger(__name__)


async def app_factory() -> web.Application:
    sirbot = web.Application()
    sirbot.update(  # pylint: disable=no-member
        client_session=None,  # populated via parent app signal
        redis=None,  # populated via parent app signal
        scheduler=None,  # populated via parent app signal
    )

    sirbot.add_routes(routes)
    return sirbot
