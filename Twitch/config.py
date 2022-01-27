import os

def profile():
    """
    Returns:
        Str: Chrome profile path
    """
    return f"user-data-dir={os.getcwd()}/Twitch/chrome_profile"

