import logging
from flask import render_template, request, flash, jsonify
from service.survey_service import SurveyService

class SurveyController:
    def __init__(self):
        # Initialize the SurveyService
        self.survey_service = SurveyService()
        
        # Set up the logger
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)  # Set the logging level (adjust as needed)

    def render_survey_form(self):
        # Log the rendering of the survey form
        self.logger.info("Rendering the survey form.")
        return render_template('survey.html')

    def submit_survey(self):
        # Parse the JSON data from the request body
        survey_data = request.get_json()

        # Log the received survey data
        self.logger.info(f'Received survey data: {survey_data}')

        # Save the survey data using SurveyService
        try:
            self.survey_service.save_survey(survey_data)
            flash('Survey submitted successfully!', 'success')
            self.logger.info("Survey submitted successfully.")
        except Exception as e:
            self.logger.error(f"Failed to submit survey: {str(e)}")
            flash('Failed to submit survey. Please try again later.', 'danger')
            raise e

        # Redirect to the survey form after submission
        return jsonify({"message": "Survey submitted successfully!"}), 200

