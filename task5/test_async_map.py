import asyncio
from async_map import async_map_callback, async_map_promise

def print_callback(result):
    print("Callback result:", result)

async def run_all_tests():
    print("Testing callback-based async_map:")
    await async_map_callback([1, 2, 3], lambda x: x * 2, print_callback)

    print("Testing promise-based async_map:")
    result = await async_map_promise([1, 2, 3], lambda x: x * 2)
    print("Promise result:", result)

# Для запуску в IDLE
if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(run_all_tests())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_all_tests())
