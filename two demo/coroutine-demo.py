import asyncio
import random
async def coroutine_random_length(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print("Coroutine {} completed after {} seconds".format(id, process_time))
async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.ensure_future(coroutine_random_length(i)))
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
