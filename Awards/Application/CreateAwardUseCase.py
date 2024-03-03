from Awards.Domain.Entities.AAward import AAward as AwardDomain

class CreateAwardUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, award: AwardDomain):
        name_exist = self.repository.get_by_name(award.name)
        if name_exist is not None:
            return False, {"error": "Award already exists"}
        try:
            self.repository.save(award)
            return True, award
        except Exception as e:
            return False, {"error": str(e)}