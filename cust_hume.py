import asyncio

from hume import HumeVoiceClient, MicrophoneInterface


async def main() -> None:
    client = HumeVoiceClient("51kDwMHG87GnykkoAhVMdXxeLUrtyyctUQfcb6Gmo9YqArwG")

    async with client.connect(config_id="620afc8d-1826-4869-9aff-7eda8ad68a16") as socket:
        await MicrophoneInterface.start(socket)


asyncio.run(main())
