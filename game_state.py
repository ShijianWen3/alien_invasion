

class GameState:
    def __init__(self,setting) -> None:
        self.setting=setting
        self.gamestate=False
        self.reset_states()

    def reset_states(self):
        self.ship_left=self.setting.ship_number
        # self.gamestate=False