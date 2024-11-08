from rentitout.model.report import Report


class ReportRepository:
    @staticmethod
    def get_reports_by_status(status):
        return Report.objects.filter(status=status).order_by('-id').all()

    @staticmethod
    def create_report(reservation_id, description, status="PENDING"):
        report = Report(
            reservation_id=reservation_id,
            description=description,
            status=status
        )
        report.save()
        return report

    @staticmethod
    def update_report(report_id, status):
        report = Report.objects.get(id=report_id)
        report.status = status
        report.save()
        return report

