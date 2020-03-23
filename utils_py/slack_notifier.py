"""
Slack Notifier Class.
"""
import requests


class SlackNotifier:
    """
    SlackNotifier is responsible for sending messages over slackself.
    """
    # Storing a single instance like a singleton
    __instance = None

    def __init__(self, webhook_url, local=True):
        self.__webhook_url = webhook_url
        self.__local = local

    @staticmethod
    def init(webhook_url, local):
        """
        Initialises the singleton
        """
        SlackNotifier.__instance = SlackNotifier(webhook_url, local)

    @staticmethod
    def send(msg):
        """
        Sends a notification via slack.
        Returns True if the notitication was successfully sent,
        False otherwise.
        """
        if SlackNotifier.__instance is None:
            return False
        return SlackNotifier.__instance.__send(msg)

    def __send(self, msg):
        """
        Sends a notification via slack.
        Returns True if the notitication was successfully sent,
        False otherwise.
        """
        if not self.__webhook_url or self.__local:
            return False

        data = {"text": msg}
        res = requests.post(self.__webhook_url, json=data)
        return res.status_code == requests.codes.ok
