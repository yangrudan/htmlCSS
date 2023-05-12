import asyncio
import aiohttp
import time
import json

class Win:
    async def post_request(self,session,t):
        print(t)
        url = 'https://ug.baidu.com/mcp/pc/pcsearch'
        data = {"invoke_info":{"pos_1":[{}],"pos_2":[{}],"pos_3":[{}]}}
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        }
        # proxy = 'http://143.25.222.12:50003'     # 使用代理ip时打开
        proxy = None
        try:
            async with session.post(url=url,headers=headers,data=json.dumps(data),proxy=proxy) as response:
                if response.status == 200:
                    text = await response.text()
                    print("Success",text)
        except aiohttp.ClientError as e:
            print("Error:", e)
    async def run(self,t):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(1):
                task = asyncio.ensure_future(self.post_request(session,t))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def main(self):
        loop = asyncio.get_event_loop()
        t = time.time()
        loop.run_until_complete(self.run(t))
        print(time.time() - t)


if __name__ == "__main__":
    a = Win()
    a.main()
