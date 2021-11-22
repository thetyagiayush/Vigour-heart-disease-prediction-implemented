from django.urls import path
from .views import User_logout, HospitalBedViewAll, ManageBeds, UpdateBeds, HospitalNotification, HospitalFeedback, HeartDiseasePrediction
from .views import PatientDetails, PatientDetail, LoggedInUserView, AppointmentDetails, PatientNotification, PatientFeedback, HospitalBedView
from .views import DoctorDetails, AppointmentDoctor, AppointmentDoctorUpdate, DoctorLeaveLog, DoctorNotification, DoctorFeedback
from vigour_api.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', LoggedInUserView.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', User_logout),
    path('<int:pk>/', PatientDetail.as_view()),
    path('patientdetails', PatientDetails.as_view()),
    path('patientappointments/', AppointmentDetails.as_view()),
    path('patientnotifications/', PatientNotification.as_view()),
    path('patientfeedbacks/', PatientFeedback.as_view()),


    path('showbed/', HospitalBedViewAll.as_view()),
    path('showbed/<int:pk>/', HospitalBedView.as_view()),
    path('hospitalbeds/', ManageBeds.as_view()),
    path('hospitalbeds/<int:pk>/', UpdateBeds.as_view()),
    path('hospitalnotifications/', HospitalNotification.as_view()),
    path('hospitalfeedbacks/', HospitalFeedback.as_view()),


    path('doctordetails', DoctorDetails.as_view()),
    path('doctorappointments/', AppointmentDoctor.as_view()),
    path('doctorappointments/<int:pk>/', AppointmentDoctorUpdate.as_view()),
    path('doctorleaves/', DoctorLeaveLog.as_view()),
    path('doctornotifications/', DoctorNotification.as_view()),
    path('doctorfeedbacks/', DoctorFeedback.as_view()),

    path('heartdisease/', HeartDiseasePrediction.as_view(), name = 'heartdisease_prediction'),
]