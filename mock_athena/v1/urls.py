from django.urls import path

from . import views

defined_endpoints = {
        "practice appointment types": {"methods": ["GET"]},
        "practice appointments open": {"methods": ["GET"]},
        "practice departments": {"methods": ["GET"]},
        "practice employers": {"methods": ["GET"]},
        "practice insurance packages": {"methods": ["GET"]},
        "practice patient appointment reasons": {"methods": ["GET"]},
        "practice patients": {"methods": ["POST"]},
        "practice providers": {"methods": ["GET"]},
        "practice booked appointment": {"methods": ["GET"]},
        "practice reference medications": {"methods": ["GET"]},
        "practice reference allergies": {"methods": ["GET"]},
        "practice reference order procedure": {"methods": ["GET"]},
        "practice reference order dme": {"methods": ["GET"]},
        "practice patients enhanced best match": {"methods": ["GET"]},
        "practice chart configuration medical history": {"methods": ["GET"]},
        "practice chart configuration social history": {"methods": ["GET"]},
        "practice configuration facilities": {"methods": ["GET"]},
        "practice chart configuration medication history": {"methods": ["GET"]},
        "practice chart patient": {"methods": ["GET"]},
        "patient chart allergies": {"methods": ["GET"]},
        "patient chart encounters": {"methods": ["GET"]},
        "patient chart documents": {"methods": ["GET"]},
        "patient chart documents lab result": {"methods": ["GET"]},
        "patient chart drivers license": {"methods": ["GET"]},
        "patient chart family history": {"methods": ["GET"]},
        "patient chart insurances": {"methods": ["GET"]},
        "patient chart insurance image": {"methods": ["GET"]},
        "patient chart medical history": {"methods": ["GET"]},
        "patient chart medications": {"methods": ["GET"]},
        "patient chart default pharmacy ": {"methods": ["GET"]},
        "patient chart preferred pharmacy": {"methods": ["GET"]},
        "patient chart photo": {"methods": ["GET"]},
        "patient chart privacy information verified": {"methods": ["GET"]},
        "patient chart problems": {"methods": ["GET"]},
        "patient chart section note": {"methods": ["GET"]},
        "patient chart problem": {"methods": ["GET"]},
        "patient chart social history": {"methods": ["GET"]},
        "patient chart surgical history": {"methods": ["GET"]},
        "patient chart vaccines": {"methods": ["GET"]},
        "patient chart vitals": {"methods": ["GET"]},
        "patient chart vital": {"methods": ["GET"]},
        "patien appointments": {"methods": ["GET"]},
        "patient appointment check in": {"methods": ["GET"]},
        "patient appointment cancel": {"methods": ["GET"]},
        "patient appointment start check in": {"methods": ["GET"]},
        "patient appointment": {"methods": ["GET"]},
        "encounter diagnoses": {"methods": ["GET"]},
        "encounter reason note": {"methods": ["GET"]},
        "encounter hpi": {"methods": ["GET"]},
        "encounter orders prescription": {"methods": ["GET"]},
        "encounter physical exam": {"methods": ["GET"]},
        "encounter review of symptoms": {"methods": ["GET"]},
        "encounter vitals": {"methods": ["GET"]},
}
urlpatterns = [
    path("", views.index, name="index"),
    path("patterns", views.patterns, name="patterns"),
    path("endpoints", views.endpoints, name="endpoints"),
    path("<int:practice_id>/departments", views.api, name="practice departments"),
    path("<int:practice_id>/patients", views.api, name="practice patients"),
    path("<int:practice_id>/providers", views.api, name="practice providers"),
    path("<int:practice_id>/employers", views.api, name="practice employers"),
    path("<int:practice_id>/insurancepackages", views.api, name="practice insurance packages"),
    path("<int:practice_id>/patientappointmentreasons", views.api, name="practice patient appointment reasons"),
    path("<int:practice_id>/appointmenttypes", views.api, name="practice appointment types"),
    path("<int:practice_id>/appointments/open", views.api, name="practice appointments open"),
    path("<int:practice_id>/appointments/booked/<int:appointment_id>", views.api, name="practice booked appointment"),
    path("<int:practice_id>/reference/medications", views.api, name="practice reference medications"),
    path("<int:practice_id>/reference/allergies", views.api, name="practice reference allergies"),
    path("<int:practice_id>/reference/order/procedure", views.api, name="practice reference order procedure"),
    path("<int:practice_id>/reference/order/dme", views.api, name="practice reference order dme"),
    path("<int:practice_id>/patients/enhancedbestmatch", views.api, name="practice patients enhanced best match"),
    path("<int:practice_id>/chart/configuration/medicalhistory", views.api, name="practice chart configuration medical history"),
    path("<int:practice_id>/chart/configuration/socialhistory", views.api, name="practice chart configuration social history"),
    path("<int:practice_id>/chart/configuration/facilties", views.api, name="practice configuration facilities"),
    path("<int:practice_id>/chart/configuration/medicalhistory", views.api, name="practice chart configuration medication history"),
    path("<int:practice_id>/chart/<int:patient_id>", views.api, name="practice chart patient"),
    path("<int:practice_id>/chart/<int:patient_id>/allergies", views.api, name="patient chart allergies"),
    path("<int:practice_id>/chart/<int:patient_id>/encounters", views.api, name="patient chart encounters"),
    path("<int:practice_id>/chart/<int:patient_id>/documents", views.api, name="patient chart documents"),
    path("<int:practice_id>/chart/<int:patient_id>/documents/labresult", views.api, name="patient chart documents lab result"),
    path("<int:practice_id>/chart/<int:patient_id>/driverslicense", views.api, name="patient chart drivers license"),
    path("<int:practice_id>/chart/<int:patient_id>/familyhistory", views.api, name="patient chart family history"),
    path("<int:practice_id>/chart/<int:patient_id>/insurances", views.api, name="patient chart insurances"),
    path("<int:practice_id>/chart/<int:patient_id>/insurances/<int:insurance_id>/image", views.api, name="patient chart insurance image"),
    path("<int:practice_id>/chart/<int:patient_id>/medicalhistory", views.api, name="patient chart medical history"),
    path("<int:practice_id>/chart/<int:patient_id>/medications", views.api, name="patient chart medications"),
    path("<int:practice_id>/chart/<int:patient_id>/pharmacies/default", views.api, name="patient chart default pharmacy "),
    path("<int:practice_id>/chart/<int:patient_id>/pharmacies/preferred", views.api, name="patient chart preferred pharmacy"),
    path("<int:practice_id>/chart/<int:patient_id>/photo", views.api, name="patient chart photo"),
    path("<int:practice_id>/chart/<int:patient_id>/privacyinformationverfied", views.api, name="patient chart privacy information verified"),
    path("<int:practice_id>/chart/<int:patient_id>/problems", views.api, name="patient chart problems"),
    path("<int:practice_id>/chart/<int:patient_id>/problems/sectionnote", views.api, name="patient chart section note"),
    path("<int:practice_id>/chart/<int:patient_id>/problems/<int:problem_id>", views.api, name="patient chart problem"),
    path("<int:practice_id>/chart/<int:patient_id>/socialhistory", views.api, name="patient chart social history"),
    path("<int:practice_id>/chart/<int:patient_id>/surgicalhistory", views.api, name="patient chart surgical history"),
    path("<int:practice_id>/chart/<int:patient_id>/vaccines", views.api, name="patient chart vaccines"),
    path("<int:practice_id>/chart/<int:patient_id>/vitals", views.api, name="patient chart vitals"),
    path("<int:practice_id>/chart/<int:patient_id>/vitals/<int:vital_id>", views.api, name="patient chart vital"),
    path("<int:practice_id>/chart/<int:patient_id>/appointments", views.api, name="patien appointments"),
    path("<int:practice_id>/chart/<int:patient_id>/appointments/<int:appointment_id>/cancelcheckin", views.api, name="patient appointment check in"),
    path("<int:practice_id>/chart/<int:patient_id>/appointments/<int:appointment_id>/cancel", views.api, name="patient appointment cancel"),
    path("<int:practice_id>/chart/<int:patient_id>/appointments/<int:appointment_id>/startcheckin", views.api, name="patient appointment start check in"),
    path("<int:practice_id>/chart/<int:patient_id>/appointments/<int:appointment_id>", views.api, name="patient appointment"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/diagnoses", views.api, name="encounter diagnoses"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/encounterreasonnote", views.api, name="encounter reason note"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/hpi", views.api, name="encounter hpi"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/orders/presciption", views.api, name="encounter orders prescription"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/physicalexam", views.api, name="encounter physical exam"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/reviewofsystems", views.api, name="encounter review of symptoms"),
    path("<int:practice_id>/chart/encounter/<int:encounter_id>/vitals", views.api, name="encounter vitals"),


]
