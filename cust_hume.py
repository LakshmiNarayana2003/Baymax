import asyncio

from hume import HumeVoiceClient, MicrophoneInterface


async def main() -> None:
    client = HumeVoiceClient("KEY")

    async with client.connect(config_id="con-fig") as socket:
        await MicrophoneInterface.start(socket)


asyncio.run(main())
