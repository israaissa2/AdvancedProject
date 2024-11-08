from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.auth_models.adminAuth import AdminAuth
from rentitout.components.report_component import ReportComponent
from rentitout.models import User
from rentitout.serilaizers.report_serializer import ReportSerializer


class ReportController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (AdminAuth,)

    def list(self, request):
        reports = ReportComponent.get_reports(
            status=request.query_params.get('status', "PENDING"),
        )
        return Response(data={'reports': ReportSerializer(reports, many=True).data}, status=200)

    def update(self, request, pk=None):
        report = ReportComponent.update_report_status(pk, status=request.data.get('status'))
        return Response(data={'report': ReportSerializer(report, many=False).data}, status=200)
