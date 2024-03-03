class ListAwardsUseCase:
    def __init__(self, award_repo):
        self.award_repo = award_repo

    def execute(self):
        return self.award_repo.list_all()