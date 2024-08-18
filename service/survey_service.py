from repo.survey_repo import SurveyRepository
import logging

class SurveyService:
    def __init__(self):
        self.repo = SurveyRepository()
        self.logger = logging.getLogger(self.__class__.__name__)

    def save_survey(self, survey_data):
        try:
            self.logger.info('Saving survey data...')
            self.logger.info(f'Saving survey data... ${survey_data}')
            self.repo.save(survey_data)
            self.logger.info('Survey data saved successfully.')
        except Exception as e:
            self.logger.error(f'Failed to save survey data: {e}')
            raise
