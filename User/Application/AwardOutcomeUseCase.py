import random
from User.Infrastructure.Repositories.MysqlRepository import Repository as UserRepository
from Awards.Infrastructure.Repositories.MysqlRepository import Repository as AwardRepository
from Surveys.Infrastructure.Repositories.MysqlRepository import Repository as SurveyRepository
class AwardOutcomeUseCase:
    def __init__(self):
        self.user_repository = UserRepository()
        self.award_repository = AwardRepository()
        self.get_survey = SurveyRepository()

    def execute(self, user_uuid, survey_uuid):
        user = self.user_repository.getByUuid(user_uuid)
        print("el usuario es", user.name)
        survey = self.get_survey.getByUuid(survey_uuid)

        if survey is None:
            raise ValueError(f"No se encontró ninguna encuesta con el UUID {survey_uuid}")
        # Verificar si todas las respuestas son correctas
        all_answers_correct = all(ask.correct_result == ask.result for ask in survey.asks)
        print("todas las respuestas son correctas", all_answers_correct)
        # Preparar el resultado
        result = {
            'user_name': user.name,
            'award': 'si premios para ti',
            'survey_status': 'Felicidades!! has ganado !!!' if all_answers_correct else 'Fallaste intenta de nuevo a la proxima',
        }

        if all_answers_correct:
            available_awards = self.award_repository.list_all()

            if available_awards:
                selected_award = random.choice(available_awards)
                result['award'] = selected_award.name

        return result