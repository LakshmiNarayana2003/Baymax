# from hume import HumeVoiceClient

# client = HumeVoiceClient("51kDwMHG87GnykkoAhVMdXxeLUrtyyctUQfcb6Gmo9YqArwG")

# for config in client.iter_configs():
#     print(f"- {config.name} ({config.id})")


from hume import HumeVoiceClient


def list_configs(client):
    configs = [(config.name, config.id) for config in client.iter_configs()]
    for index, (name, config_id) in enumerate(configs, start=1):
        print(f"{index}. {name} ({config_id})")

    while True:
        choice = input("Enter the number of the configuration you want to use: ")
        try:
            choice_index = int(choice)
            if 1 <= choice_index <= len(configs):
                selected_config_name, selected_config_id = configs[
                    choice_index - 1]  # Get the selected config (name, id)
                return selected_config_name, selected_config_id
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
