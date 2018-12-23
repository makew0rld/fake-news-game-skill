from mycroft import MycroftSkill, intent_file_handler


class FakeNewsGame(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('game.news.fake.intent')
    def handle_game_news_fake(self, message):
        headline = ''

        self.speak_dialog('game.news.fake', data={
            'headline': headline
        })


def create_skill():
    return FakeNewsGame()

