import asyncio
import shlex
import sys


async def update_requirements(deploy: str, plugins: str) -> None:
    modules = compare_requirements(deploy, plugins)
    try:
        for module in modules:
            await runcmd(f"pip install {module}")
            print(f">> Installed Requirement: {module}")
    except Exception as e:
        print(f"Error installing requirments: {str(e)}")


asyncio.run(update_requirements(sys.argv[1], sys.argv[2]))
