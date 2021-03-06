class Trainer:
    trainer_id = 0

    def __init__(self, name):
        Trainer.trainer_id = Trainer.get_next_id()
        self.name = name
        self.t_id = Trainer.trainer_id

    def __repr__(self):
        return f"Trainer <{self.t_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.trainer_id + 1