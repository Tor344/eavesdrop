import asyncio
import re
import subprocess

import pyrcrack


async def get_id_process(string_process:str) -> list:
    pattern = r"\d{2,}"
    return re.findall(pattern, string_process)


async def kill_process(id_list: list) -> None:
    for id in id_list:
        subprocess.run(["kill",str(id)])


# help(pyrcrack.AirmonNg)
async def check():
    airmon = pyrcrack.AirmonNg()
    
    process = await airmon.run('check', 'wlp3s0f3u2')
    output = await process.stdout.read()

    list_id = await get_id_process(str(output))
    await kill_process(list_id)
    
    start = await airmon.run("start", "wlp3s0f3u2")
    output = await process.stdout.read()



if __name__ == "__main__":
    asyncio.run(check())

