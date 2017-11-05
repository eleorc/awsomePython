import asyncio
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='root', password='root', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass