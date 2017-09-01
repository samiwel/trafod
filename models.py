from stringcase import spinalcase
from datetime import datetime


class Topic:

    def __init__(self, title):
        self.topic_id = spinalcase(title.lower())
        self.title = title
        self.open = True
        self.deleted = False
        self.threads = []


class Thread:

    def __init__(self, title, comment):
        self.thread_id = spinalcase(title.lower())
        self.title = title
        self.open = True
        self.deleted = False
        self.comments = [comment]


class Comment:

    def __init__(self, author_id, text):
        self.author_id = author_id
        self.text = text
        self.replies = []
        self.mentions = []
        self.created_at = datetime.now()
        self.edited_at = None
        self.deleted = False


class Author:

    def __init__(self, username, name, avatar=None):
        self.username = username
        self.name = name
        self.avatar = avatar
