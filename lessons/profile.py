"""Examples of Object-oriented programming"""

class Profile:
    """An example of a simple social media profile model."""
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
        """Initializes all attributes of an object."""
        self.handle = handle 
        self.followers = 0
        self.is_private = False

    def tweet(self, message: str) -> None:
        print(f"@{self.handle} tweets {message}")


my_profile: Profile = Profile("wbenchesser")
my_profile.tweet("\"Hello, world.\"")