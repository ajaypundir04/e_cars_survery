from flask import Blueprint
from web.controllers.survey_controller import SurveyController

web_blueprint = Blueprint('web', __name__)
survey_controller = SurveyController()

# Route for displaying the survey form
@web_blueprint.route('/', methods=['GET'])
def render_survey_form():
    return survey_controller.render_survey_form()

# Route for handling survey submission
@web_blueprint.route('/submit-survey', methods=['POST'])
def submit_survey():
    return survey_controller.submit_survey()
