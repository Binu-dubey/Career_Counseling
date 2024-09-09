import csv
import os
from django.core.management.base import BaseCommand
from assessment.models import Question

class Command(BaseCommand):
    help = 'Load questions from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Define the path to your CSV file
        file_path = os.path.join('data', 'questions.csv')

        # Check if the file exists
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File {file_path} does not exist."))
            return

        # Open the CSV file and read it
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Check if the CSV has the required columns (strip any whitespace)
            expected_columns = ['question_text', 'category', 'subcategory', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option', 'option_1_score', 'option_2_score', 'option_3_score', 'option_4_score']
            missing_columns = [col for col in expected_columns if col not in [header.strip() for header in reader.fieldnames]]

            if missing_columns:
                self.stdout.write(self.style.ERROR(f"Missing columns in CSV: {', '.join(missing_columns)}"))
                return

            # Iterate over each row and create the Question objects
            for row_number, row in enumerate(reader, start=1):
                # Clean up all fields by stripping whitespace, tabs, and newlines
                question_text = row['question_text'].strip()
                category = row['category'].strip()
                subcategory = row['subcategory'].strip()
                option_1 = row['option_1'].strip()
                option_2 = row['option_2'].strip()
                option_3 = row['option_3'].strip()
                option_4 = row['option_4'].strip()
                correct_option = row['correct_option'].strip()

                # Log and skip rows where category or subcategory is missing after stripping
                if not category or not subcategory:
                    self.stdout.write(self.style.WARNING(f"Row {row_number}: Missing category or subcategory. Skipping row."))
                    continue  # Skip the row if category or subcategory is missing

                # Handle score fields safely and convert to integers, filling missing or invalid values with 0
                try:
                    option_1_score = int(row['option_1_score'].strip())
                except ValueError:
                    option_1_score = 0

                try:
                    option_2_score = int(row['option_2_score'].strip())
                except ValueError:
                    option_2_score = 0

                try:
                    option_3_score = int(row['option_3_score'].strip())
                except ValueError:
                    option_3_score = 0

                try:
                    option_4_score = int(row['option_4_score'].strip())
                except ValueError:
                    option_4_score = 0

                # Ensure that all required fields are not empty after stripping
                if all([question_text, category, subcategory, option_1, option_2, option_3, option_4, correct_option]):
                    # Create the Question object
                    Question.objects.create(
                        question_text=question_text,
                        category=category,
                        subcategory=subcategory,
                        option_1=option_1,
                        option_2=option_2,
                        option_3=option_3,
                        option_4=option_4,
                        correct_option=correct_option,
                        option_1_score=option_1_score,
                        option_2_score=option_2_score,
                        option_3_score=option_3_score,
                        option_4_score=option_4_score
                    )
                else:
                    self.stdout.write(self.style.WARNING(f"Row {row_number}: Missing required fields. Skipping row."))

        # Feedback to the terminal
        self.stdout.write(self.style.SUCCESS('Successfully loaded questions'))
