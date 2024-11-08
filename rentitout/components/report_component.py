from rentitout.exceptions import InvalidReservation
from rentitout.repositories.item_repository import ItemReservationRepository
from rentitout.repositories.report_repository import ReportRepository


class ReportComponent:
    @staticmethod
    def get_reports(status="PENDING"):
        return ReportRepository.get_reports_by_status(status)

    @staticmethod
    def create_report(user_id, reservation_id, description):
        reservation = ItemReservationRepository.get_reservation_by_id(reservation_id)
        if not reservation or user_id != reservation.user_id:
            raise InvalidReservation()
        return ReportRepository.create_report(reservation_id, description)

    @staticmethod
    def update_report_status(report_id, status):
        return ReportRepository.update_report(report_id, status)
