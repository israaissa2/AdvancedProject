from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from rentitout.auth import SafeJWTAuthentication
from rentitout.components.report_component import ReportComponent
from rentitout.serilaizers.report_serializer import ReportSerializer


class UserReportController(ViewSet):

    authentication_classes = (SafeJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        report = ReportComponent.create_report(
            user_id=request.user.id,
            reservation_id=request.data.get('reservation_id'),
            description=request.data.get('description'),
        )

        return Response(data={'report': ReportSerializer(report, many=False).data}, status=200)

