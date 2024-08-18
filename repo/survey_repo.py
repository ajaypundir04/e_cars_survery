import mysql.connector
import logging
import config

class SurveyRepository:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME
            )
            return connection
        except mysql.connector.Error as e:
            self.logger.error(f'Error connecting to MySQL: {e}')
            raise

    def save(self, survey_data):
        connection = self.create_connection()
        cursor = connection.cursor()
        try:
            self.logger.info(f'survey_data::::{survey_data}')
            
            # Construct the SQL query with named placeholders
            insert_query = """
                INSERT INTO survey_responses (
                    question1, question2, question3, question4, question5, question6, question7, question8, 
                    question9, question10, question11, question12, question12_other, question13, question14,
                    question15, question16, question17, question18, question19, question20, question21, 
                    question22, question23, question24, question25
                ) VALUES (
                    %(question1)s, %(question2)s, %(question3)s, %(question4)s, %(question5)s, %(question6)s, 
                    %(question7)s, %(question8)s, %(question9)s, %(question10)s, %(question11)s, %(question12)s, 
                    %(question12_other)s, %(question13)s, %(question14)s, %(question15)s, %(question16)s, 
                    %(question17)s, %(question18)s, %(question19)s, %(question20)s, %(question21)s, %(question22)s, 
                    %(question23)s, %(question24)s, %(question25)s
                )
            """
            
            self.logger.info(f'insert_query::::{insert_query}')
            
            # Execute the query using the survey_data dictionary
            cursor.execute(insert_query, survey_data)
            connection.commit()
            self.logger.info('Data inserted into database.')
        except Exception as e:
            self.logger.error(f'Error saving data to MySQL: {e}')
            raise
        finally:
            cursor.close()
            connection.close()
