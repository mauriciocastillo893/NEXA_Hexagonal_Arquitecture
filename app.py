from User.Infrastructure.Repositories.MysqlRepository import Repository as UserRepository
from Awards.Infrastructure.Repositories.MysqlRepository import Repository as AwardRepository
from Results.Infrastructure.Repositories.MysqlRepository import Repository as ResultRepository
from CorrectResults.Infrastructure.Repositories.MysqlRepository import Repository as CorrectRepository

from CorrectResults.Infrastructure.Routes.Routes import initialize_app as initialize_app_correct
from Results.Infrastructure.Routes.Routes import initialize_app as initialize_app_result

from Surveys.Infrastructure.Repositories.MysqlRepositoryAsk import Repository as AskRepository
from Surveys.Infrastructure.Routers.RoutesAsk import initialize_app as initialize_app_ask
from Surveys.Infrastructure.Repositories.MysqlRepository import Repository as SurveyRepository
from Surveys.Infrastructure.Routers.Routes import initialize_app as initialize_app_survey

from User.Infrastructure.Routes.Routes import initialize_app as initialize_app_user
from Awards.Infrastructure.Routes.Routes import initialize_app as initialize_app_award

from flask import Flask
app = Flask(__name__)

repository_user = UserRepository()
repository_award = AwardRepository()
repository_survey = SurveyRepository()
repository_ask = AskRepository()
repository_result = ResultRepository()
repository_correct = CorrectRepository()

initialize_app_user(app, repository_user)
initialize_app_award(app, repository_award)
initialize_app_survey(app, repository_survey)
initialize_app_ask(app,repository_ask)
initialize_app_result(app, repository_result)
initialize_app_correct(app, repository_correct)

if __name__ == "__main__":
    app.run(debug=True)