print("Hello world")

import asyncio

async def hello_world():
    print("Hello, World!")

    await asyncio.sleep(1)

    print("Welcome to Python World")


asyncio.run(hello_world())
