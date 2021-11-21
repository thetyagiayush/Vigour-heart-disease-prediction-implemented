from rest_framework import serializers
from vigour_app import models
from vigour_app.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
            'user_type',
        )
        model = models.CustomUser


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'gender',
            'address',
        )
        model = models.Patients


class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'patient_id_id',
            'leave_date',
            'leave_message',
            'doctor_pref',
            'created_at',
            'leave_status',
        )
        read_only_fields = ('leave_status', 'patient_id_id')
        model = models.PatientAppointment


class PatientNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'message',
            'read_status',
        )
        model = models.NotificationPatient


class PatientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feedback',
            'feedback_reply',
        )
        read_only_fields = ['feedback_reply']
        model = models.FeedBackPatient


# ----------------------------------------------DOCTOR----------------------------------------------


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'address',
        )
        model = models.Doctors


class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'patient_id_id',
            'leave_date',
            'leave_message',
            'created_at',
            'leave_status',
        )
        read_only_fields = ['patient_id_id', 'leave_date', 'leave_message']
        model = models.PatientAppointment


class DoctorLeave(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'leave_date',
            'leave_message',
            'leave_status',
            'created_at'
        )
        read_only_fields = ['id', 'created_at', 'leave_status']
        model = models.LeaveReportDoctor


class DoctorNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'message',
            'read_status',
        )
        model = models.NotificationDoctors


class DoctorFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feedback',
            'feedback_reply',
        )
        read_only_fields = ['feedback_reply']
        model = models.FeedBackDoctors

# ---------------------------------------------HOSPITAL-----------------------------------------------------------------


class HospitalViewBeds(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'address',
            'max_bed',
            'available_bed',
        )
        read_only_fields = ['address']
        model = models.Hospital

class HospitalNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'message',
            'read_status',
        )
        model = models.NotificationHospital


class HospitalFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'feedback',
            'feedback_reply',
        )
        read_only_fields = ['feedback_reply']
        model = models.FeedBackHospital
