from django.contrib.auth import logout
from rest_framework import serializers
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .apps import VigourApiConfig


from vigour_app import models
from vigour_app.models import PatientAppointment, Patients, NotificationPatient, FeedBackPatient
from vigour_app.models import Doctors, CustomUser
from .serializers import PatientSerializer, CustomUserSerializer, PatientAppointmentSerializer, \
    PatientNotificationSerializer, PatientFeedbackSerializer, HospitalViewBeds
from .serializers import DoctorSerializer, DoctorAppointmentSerializer, DoctorLeave, DoctorNotificationSerializer, \
    DoctorFeedbackSerializer, HospitalFeedbackSerializer, HospitalNotificationSerializer
from rest_framework.exceptions import NotFound


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    logout(request)
    return Response('User Logged out successfully')


# FOR PATIENT

class PatientDetails(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            patient = Patients.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Patient")
        return Patients.objects.filter(id=patient)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Patients.objects.all()
    serializer_class = PatientSerializer


class HospitalBedView(generics.RetrieveAPIView):
    queryset = models.Hospital.objects.all()
    serializer_class = HospitalViewBeds


class HospitalBedViewAll(generics.ListAPIView):
    queryset = models.Hospital.objects.all()
    serializer_class = HospitalViewBeds


class LoggedInUserView(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)


class AppointmentDetails(generics.ListCreateAPIView):
    serializer_class = PatientAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            patient = Patients.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Patient")
        obj = PatientAppointment.objects.filter(patient_id_id=patient)
        if not obj.count():
            raise NotFound("No Appointments Found")
        else:
            return obj

    def create(self, request, *args, **kwargs):
        user = self.request.user
        doc = Patients.objects.only('id').get(admin_id=user.id).id
        patient_data = request.data
        response = models.PatientAppointment.objects.create(patient_id_id=doc, leave_date=patient_data["leave_date"],
                                                            leave_message=patient_data["leave_message"],
                                                            doctor_pref=patient_data["doctor_pref"],
                                                            leave_status=0)
        response.save()
        ser = PatientAppointmentSerializer(response)
        return Response(ser.data, status=201)


class PatientNotification(generics.ListAPIView):
    serializer_class = PatientNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            patient = Patients.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Patient")
        obj = NotificationPatient.objects.filter(patient_id_id=patient)
        if not obj.count():
            raise NotFound("No Notifications Found")
        else:
            return obj


class PatientFeedback(generics.ListCreateAPIView):
    serializer_class = PatientFeedbackSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            patient = Patients.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Patient")
        obj = FeedBackPatient.objects.filter(patient_id_id=patient)
        if not obj.count():
            raise NotFound("No Feedback Messages Found")
        else:
            return obj

    def create(self, request, *args, **kwargs):
        user = self.request.user
        patient = Patients.objects.only('id').get(admin_id=user.id).id
        patient_data = request.data
        response = models.FeedBackPatient.objects.create(patient_id_id=patient, feedback=patient_data["feedback"])
        response.save()
        ser = PatientFeedbackSerializer(response)
        return Response(ser.data, status=201)


# -----------------------------------------FOR DOCTOR--------------------------------------------


class DoctorDetails(generics.ListAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            doctor = Doctors.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Doctor")
        return Patients.objects.filter(id=doctor)


class AppointmentDoctor(generics.ListAPIView):
    serializer_class = DoctorAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            doctor = CustomUser.objects.only('username').get(id=user.id).username
        except:
            raise NotFound("You are not Doctor")
        obj = PatientAppointment.objects.filter(doctor_pref=doctor)
        if not obj.count():
            raise NotFound("No Appointments Found")
        else:
            return obj


class AppointmentDoctorUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorAppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            doctor = CustomUser.objects.only('username').get(id=user.id).username
        except:
            raise NotFound("You are not Doctor")
        obj = PatientAppointment.objects.filter(doctor_pref=doctor)
        if not obj.count():
            raise NotFound("No Appointments Found")
        else:
            return obj


class DoctorLeaveLog(generics.ListCreateAPIView):
    serializer_class = DoctorLeave

    def get_queryset(self):
        user = self.request.user
        try:
            doctor = Doctors.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Doctor")
        obj = models.LeaveReportDoctor.objects.filter(doctor_id_id=doctor)
        if not obj.count():
            raise NotFound("No Leaves Found")
        else:
            return obj

    def create(self, request, *args, **kwargs):
        user = self.request.user
        doc = Doctors.objects.only('id').get(admin_id=user.id).id
        doctor_data = request.data
        response = models.LeaveReportDoctor.objects.create(doctor_id_id=doc, leave_date=doctor_data["leave_date"],
                                                           leave_message=doctor_data["leave_message"], leave_status=0)
        response.save()
        ser = DoctorLeave(response)
        return Response(ser.data, status=201)


class DoctorNotification(generics.ListAPIView):
    serializer_class = DoctorNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            doc = models.Doctors.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Doctor")
        obj = models.NotificationDoctors.objects.filter(doctor_id_id=doc)
        if not obj.count():
            raise NotFound("No Notifications Found")
        else:
            return obj


class DoctorFeedback(generics.ListCreateAPIView):
    serializer_class = DoctorFeedbackSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            doc = Doctors.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Doctor")
        obj = models.FeedBackDoctors.objects.filter(doctor_id_id=doc)
        if not obj.count():
            raise NotFound("No Feedback Messages Found")
        else:
            return obj

    def create(self, request, *args, **kwargs):
        user = self.request.user
        doc = Doctors.objects.only('id').get(admin_id=user.id).id
        doctor_data = request.data
        response = models.FeedBackDoctors.objects.create(doctor_id_id=doc, feedback=doctor_data["feedback"])
        response.save()
        ser = DoctorFeedbackSerializer(response)
        return Response(ser.data, status=201)


# -----------------------------------------------HOSPITAL---------------------------------------------------------------


class ManageBeds(generics.ListAPIView):
    serializer_class = HospitalViewBeds

    def get_queryset(self):
        user = self.request.user
        try:
            obj = models.Hospital.objects.filter(admin_id=user.id)
        except:
            raise NotFound("You are not Hospital Staff!")
        if not obj.count():
            raise NotFound("No Hospitals Found")
        else:
            return obj


class UpdateBeds(generics.RetrieveUpdateAPIView):
    serializer_class = HospitalViewBeds

    def get_queryset(self):
        user = self.request.user
        try:
            obj = models.Hospital.objects.filter(admin_id=user.id)
        except:
            raise NotFound("You are not Hospital Staff!")
        if not obj.count():
            raise NotFound("No Hospitals Found")
        else:
            return obj


class HospitalNotification(generics.ListAPIView):
    serializer_class = HospitalNotificationSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            hos = models.Hospital.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Hospital Staff!")
        obj = models.NotificationHospital.objects.filter(hospital_id_id=hos)
        if not obj.count():
            raise NotFound("No Notifications Found")
        else:
            return obj


class HospitalFeedback(generics.ListCreateAPIView):
    serializer_class = HospitalFeedbackSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            hos = models.Hospital.objects.only('id').get(admin_id=user.id).id
        except:
            raise NotFound("You are not Hospital Staff!")
        obj = models.FeedBackHospital.objects.filter(hospital_id_id=hos)
        if not obj.count():
            raise NotFound("No Feedback Messages Found")
        else:
            return obj

    def create(self, request, *args, **kwargs):
        user = self.request.user
        hos = models.Hospital.objects.only('id').get(admin_id=user.id).id
        hos_data = request.data
        response = models.FeedBackHospital.objects.create(hospital_id_id=hos, feedback=hos_data["feedback"])
        response.save()
        ser = HospitalFeedbackSerializer(response)
        return Response(ser.data, status=201)


# ----------------------------------------------HEART DISEASE-----------------------------------------------------------


class HeartDiseasePrediction(APIView):
    def post(self, request):
        data = request.data
        p1 = data['age']
        p2 = data['gender']
        p3 = data['cp']
        p4 = data['trestbps']
        p5 = data['chol']
        p6 = data['fbs']
        p7 = data['restecg']
        p8 = data['thalach']
        p9 = data['exang']
        p10 = data['oldpeak']
        p11 = data['slope']
        p12 = data['ca']
        p13 = data['thal']

        random_model = VigourApiConfig.model_random
        logistic_model = VigourApiConfig.model_logistic

        random_prediction = random_model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]])
        logistic_prediction = logistic_model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]])
        response_dict = {"Random Forest Prediction": random_prediction, "Logistic Regression Prediction": logistic_prediction}
        return Response(response_dict, status=200)
