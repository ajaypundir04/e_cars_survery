import os
from pyliquibase import Pyliquibase

class LiquibaseService:
    def __init__(self, liquibase_dir='liquibase', change_log_file='db.changelog.xml'):
        """
        Initialize the LiquibaseService with the path to the Liquibase executable and the change log file.

        Args:
            liquibase_dir (str): Directory to store Liquibase files.
            change_log_file (str): Path to the Liquibase changelog file.
        """
        # Ensure liquibase_dir exists
        if not os.path.exists(liquibase_dir):
            os.makedirs(liquibase_dir)

        
        # Initialize Pyliquibase with essential parameters
        self.liquibase = Pyliquibase(
            liquibaseDir=liquibase_dir
        )

    def update_database(self):
        """
        Runs the Liquibase update command to apply changes to the database.

        Returns:
            str: The output from the Liquibase update command.
        """
        return self.liquibase.update()

    def status(self):
        """
        Runs the Liquibase status command to check for pending changesets.

        Returns:
            str: The output from the Liquibase status command.
        """
        return self.liquibase.status()

    def rollback(self, tag):
        """
        Rolls back the database to a specified tag using the Liquibase rollback command.

        Args:
            tag (str): The tag to roll back to.

        Returns:
            str: The output from the Liquibase rollback command.
        """
        return self.liquibase.rollback(tag)
