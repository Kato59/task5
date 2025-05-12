import asyncio

should_abort = {"flag": False}  # Shared state to simulate cancellation

async def async_map_callback(arr, func, callback):
    result = []

    async def process():
        for item in arr:
            if should_abort["flag"]:
                callback("Aborted")
                return
            await asyncio.sleep(0.1)  # затримка
            result.append(func(item))
        callback(result)

    await process()

async def async_map_promise(arr, func):
    await asyncio.sleep(0.1)  # затримка
    return [func(x) for x in arr]

def cancel_async_operations():
    should_abort["flag"] = True

