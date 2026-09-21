def add_setting(dictionary, tupla):
    for key, value in [tupla]:
        key = key.lower()
        value = value.lower()

        if key in dictionary:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."

        if key not in dictionary:
            dictionary[key] = value
            return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionary, tupla):
    for key, value in [tupla]:
        key = key.lower()
        value = value.lower()

        if key in dictionary:
            dictionary[key] = value
            return f"Setting '{key}' updated to '{value}' successfully!"

        if key not in dictionary:
            return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dictionary, key):
    key = key.lower()

    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return "Setting not found!"


def view_settings(dictionary):
    if not dictionary:
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in dictionary.items():
        result += f"{key.capitalize()}: {value}\n"

    return result


test_settings = {
    "theme": "light",
    "notifications": "enabled",
    "volume": "high"
}

delete_setting(test_settings, ('Theme'))
update_setting(test_settings, ('Notifications', 'disabled'))
add_setting(test_settings, ('Bluetooth', 'on'))

print(view_settings(test_settings))
