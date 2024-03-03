class DeleteAwardUseCase:
    def __init__(self, award_repository):
        self.award_repository = award_repository

    def execute(self, award_id):
        award = self.award_repository.get_by_id(award_id)
        if award is None:
            raise Exception('Award not found')
        else:
            self.award_repository.delete(award_id)
            return True