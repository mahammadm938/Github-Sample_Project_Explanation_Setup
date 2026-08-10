print("Hello world")

import asyncio

async def hello_world():
    name = input("Enter your name: ")

    print(f"Hello {name}!")

    await asyncio.sleep(1)

    print("Welcome to Python World")


asyncio.run(hello_world())