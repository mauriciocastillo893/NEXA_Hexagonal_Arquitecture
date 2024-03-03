class GetAwardUseCase:
    def __init__(self, award_repo):
        self.award_repo = award_repo

    def execute(self, award_id:str):
        return self.award_repo.get_by_id(award_id)