#!/usr/bin/env python3

import asyncio
import aiohttp


async def all_orphanned():
    url = 'https://src.fedoraproject.org/extras/pagure_owner_alias.json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            rpms = (await resp.json())['rpms']
    for pkg in rpms:
        if 'orphan' in rpms[pkg]:
            yield pkg


async def print_if_not_retired(pkg, semaphore, sleep=1):
    url = f'https://src.fedoraproject.org/rpms/{pkg}/blob/rawhide/f/dead.package'
    async with semaphore, aiohttp.ClientSession() as session:
        try:
            async with session.head(url) as resp:
                if resp.status == 404:
                    print(pkg)
                elif resp.status >= 400:
                    raise aiohttp.client_exceptions.ServerConnectionError()
        except (aiohttp.client_exceptions.ClientError, asyncio.TimeoutError):
            if sleep > 15 * 60:
                raise
            await asyncio.sleep(sleep)
            return await print_if_not_retired(pkg, semaphore, sleep*2)


async def main():
    tasks = []
    semaphore = asyncio.Semaphore(512)
    async for pkg in all_orphanned():
        tasks.append(asyncio.create_task(print_if_not_retired(pkg, semaphore)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
