import www.orm as orm
import logging; logging.basicConfig(level=logging.INFO)
import asyncio
import random
from www.models import User
loop = asyncio.get_event_loop()
async def insert():
    await orm.create_pool(user='www-data', password='mysql', db='awesome')

    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank',loop=loop)

    await u.save()

    r = await User.findALL()
    print(r)


    loop.run_until_complete(insert())
    await orm.destroy_pool()