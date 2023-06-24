import asyncio

async def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1
    return

async def main():
    async for number in count_up_to(5):
        if number == 3:
            return
        print(number)

asyncio.run(main())