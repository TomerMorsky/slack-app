from abc import ABC, abstractmethod

from slack_bolt import App


class Listenable(ABC):

    @abstractmethod
    def listen(self, app: App):
        pass
