class SugleAccount(object):

    def __init__(self, username, name):
        self.username = username
        self.personal_info = {"name": name, "email": "", "favourite_food": ""}
        self.friends = {}
        self.news_list = []
        self.favourite_food = []
        self.messages = []
        """
        initialize the following attributes:
        - self.username using the argument username
        - self.personal_info: a dictionary with the following key:
          - name : initialize with the argument name
          - email: initialize with empty string
          - favourite_food: initialize with empty string
        - self.friends: initialize as an empty dictionary
        - self.news_list: initialize as an empty list
        - self.messages: initialize as an empty list
        """
        pass

    def add_friend(self, friend_account):
        """
        Add a new friend to the dictionary self.friends.
        Input: friend's account, i.e. friend_account, which is of SugleAccount
        Output: None
        Description: Add friend's account to self.friends,
         - key: friend's user name
         - value: friend's SugleAccount object instance
        """
        self.friends[friend_account.username] = friend_account
        pass

    def remove_friend(self, friend_username):
        """
        Remove friend's account from self.friends dictionary.
        Input: friend_username is a string
        Output: None
        Description:
        - Check if friend's username is in self.friends
        - If it is, remove the item from dictionary and return True
        - If not, return False
        """
        if friend_username in self.friends:
            del self.friends[friend_username]
            return True
        else:
            return False
        pass

    def add_news(self, new_news):
        """
        Add news to self.news_list
        Input: new_news is a string
        Output: None
        Description:
        - add to the end of the list self.news_list
        """
        self.news_list.append(new_news)
        pass

    def get_latest_news(self):
        """
        Returns the last news.
        Input: None
        Output: A string containing the last inserted news from self.news_list
        """
        return self.news_list[-1]
        pass

    def get_all_news(self):
        """
        Return self.news_list
        Input: None
        Output: A list containing all the news from self.news_list
        """
        return self.news_list
        pass

    def add_to_inbox(self,from_user, message):
        """
        Add message to self.messages list.
        Input:
         - from_user: a string containing username of sender
         - message: a string containing the message
        Output: None
        Description:
        - Add an new message into the list self.messages
        - Each item in the list is a tuple of (sender, message)
        """
        self.messages.append((from_user, message))
        pass

    def read_inbox(self):
        """
        Returns the list of all messages from self.messages
        Input: None
        Output: A list of all messages from self.messages
        """
        return self.messages
        pass
oka = SugleAccount("oka_k", "Oka")
maya = SugleAccount("maya_k", "Maya")
print(oka.news_list)
print(oka.friends)
oka.add_friend(maya)
print(oka.friends)
oka.remove_friend('maya')
print(oka.friends)
oka.add_news('I love Monday')
print(oka.get_latest_news())
print(oka.get_all_news())
oka.add_to_inbox('maya_k','I love you')
print(oka.read_inbox())       #fomratting can be done other places`
