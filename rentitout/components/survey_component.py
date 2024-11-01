from rentitout.repositories.client_survey_repository import ClientSurveyRepository
from rentitout.repositories.doner_survey_repository import DonerSurveyRepository


class ClientSurveyComponent:
    @staticmethod
    def get_survey(user_id):
        return ClientSurveyRepository.get_survey(user_id)

    @staticmethod
    def add_survey(user_id, survey):
        ClientSurveyRepository.update_survey(
            user_id, survey.get('first_name'), survey.get('second_name'), survey.get('third_name'),
            survey.get('last_name'), survey.get('id_number'), survey.get('date_of_birth'),
            survey.get('place_of_birth'), survey.get('address'), survey.get('marital_status'),
            survey.get('phone_number'), survey.get('spouse_name'), survey.get('number_of_sons'),
            survey.get('rent_value'), survey.get('income_value'), survey.get('home_status'),
            survey.get('other_funds', ''), survey.get('sons', [])
        )


class DonerSurveyComponent:
    @staticmethod
    def get_survey(user_id):
        return DonerSurveyRepository.get_survey(user_id)

    @staticmethod
    def add_survey(user_id, survey):
        DonerSurveyRepository.update_survey(
            user_id, survey.get('first_name'), survey.get('second_name'), survey.get('third_name'),
            survey.get('last_name'), survey.get('id_number'), survey.get('date_of_birth'),
            survey.get('place_of_birth'), survey.get('address'), survey.get('marital_status'),
            survey.get('number_of_family_members'), survey.get('phone_number'), survey.get('academic_qualification'),
            survey.get('job'), survey.get('place_of_work'), survey.get('number_of_sons'), has_accepted=True
        )
