user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    duplicate_user_pref = user_pref
    for key, value in user_pref.items():
        if value == None:
            del duplicate_user_pref[key] # this doesn't work
    return duplicate_user_pref


print(update_preferences(user_preferences))
print(user_preferences)
