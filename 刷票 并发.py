#coding:utf-8
import time,asyncio,aiohttp
import random
import string
url = 'http://msg.jzsyishu.com/vote/Receive'
async def hello(url,semaphore):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    ran_str2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    data = {    
    "ids" : 102,
    "went" : ran_str2+"-dO3crX8H_zQe6d"+ran_str
    }
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.post(url = url,data = data) as response:
                return await response.read()


async def run():
    semaphore = asyncio.Semaphore(500) # 限制并发量为500
    to_get = [hello(url.format(),semaphore) for _ in range(400000)] #总共1000任务
    await asyncio.wait(to_get)


if __name__ == '__main__':
#    now=lambda :time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()