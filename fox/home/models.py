from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime



class Enquiry(models.Model):
    JEE = 'JEE'
    NEET = 'NEET'
    NEET_PG = 'NEET-PG'
    CET = 'CET'
    COMED_K = 'COMED-K'
    OTHER='Other'
    APPLIEDFOR = [
        (JEE,'JEE'),
        (NEET ,'NEET'),
        (NEET_PG,'NEET-PG'),
        (CET,'CET'),
        (COMED_K,'COMED-K'),
        (OTHER,'Other'),
    ]
    full_name = models.CharField(max_length=50)
    interested_in = models.CharField(max_length=255)
    ph = models.CharField(max_length=12)
    applied_for = models.CharField(max_length=10,choices=APPLIEDFOR, default=OTHER)
    post_date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Contact_request(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(default=None)
    requested_on=models.DateTimeField(auto_now=True)
    
class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    created_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email


class Engineering_form(models.Model):
    JEE = 'JEE'
    NEET = 'NEET'
    NEET_PG = 'NEET-PG'
    CET = 'CET'
    COMED_K = 'COMED-K'
    OTHER='Other'
    APPLIEDFOR = [
        (JEE,'JEE'),
        (NEET ,'NEET'),
        (NEET_PG,'NEET-PG'),
        (CET,'CET'),
        (COMED_K,'COMED-K'),
        (OTHER,'Other'),
    ]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    TwelfthPercentage = models.CharField(max_length=10)
    applied_for=models.CharField(max_length=10,choices=APPLIEDFOR, default=OTHER)
    branch = models.CharField(max_length=1000)
    college = models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return 'By {} on {}'.format(self.name,self.created_on)

# class Medical_form(models.Model):
#     MBBS='MBBS (Bachelor of Medicine and Bachelor of Surgery)'
#     BDS='BDS (Bachelor of Dental Surgery)'
#     BScNursing='B.SC. NURSING'
#     B_PHARMA='B.PHARM. (BACHELOR OF PHARMACY)'
#     PHARM_D='PHARM D ( Doctor of Pharmacy)'
#     BAMS='BAMS (Bachelor of Ayurvedic Medicine and Surgery)'
#     BHMS='BHMS (Bachelor of Homeopathic Medicine and Surgery)'
#     BUMS='BUMS ( Bachelor of Unani Medicine and Surgery)'
#     BPT='BPT (Bachelor of Physiotherapy)'
#     B_V_SC_and_A_H='B.V.SC. & A.H. (Bachelor of Veterinary Science and Animal Husbandry)'
#     BOT='BOT (BACHELOR OF OCCUPATIONAL THERAPY)'
#     BASLP='BASLP (BACHELOR OF AUDIOLOGY SPEECH LANGUAGE PATHOLOGY)'
#     Other = 'Other'
    
#     Medical_branches = [
#         (MBBS,'MBBS (Bachelor of Medicine and Bachelor of Surgery)'),
#         (BDS,'BDS (Bachelor of Dental Surgery)'),
#         (BScNursing,'B.SC. NURSING'),
#         (B_PHARMA,'B.PHARM. (BACHELOR OF PHARMACY)'),
#         (PHARM_D,'PHARM D ( Doctor of Pharmacy)'),
#         (BAMS,'BAMS (Bachelor of Ayurvedic Medicine and Surgery)'),
#         (BHMS,'BHMS (Bachelor of Homeopathic Medicine and Surgery)'),
#         (BUMS,'BUMS ( Bachelor of Unani Medicine and Surgery)'),
#         (BPT,'BPT (Bachelor of Physiotherapy)'),
#         (B_V_SC_and_A_H,'B.V.SC. & A.H. (Bachelor of Veterinary Science and Animal Husbandry)'),
#         (BOT,'BOT (BACHELOR OF OCCUPATIONAL THERAPY)'),
#         (BASLP,'BASLP (BACHELOR OF AUDIOLOGY SPEECH LANGUAGE PATHOLOGY)'),
#         (Other , 'Other'),
#     ]

#     BangaloreMedicalCollegeandResearchInstitute='Bangalore Medical College and Research Institute'
#     St_JohnsMedicalCollege='St Johns Medical College, Bangalore'
#     MS_RamaiahMedicalCollege='MS Ramaiah Medical College'
#     KempegowdaInstituteofMedicalSciences='Kempegowda Institute of Medical Sciences'
#     VydehiInstituteofMedicalSciencesandResearchCentre='Vydehi Institute of Medical Sciences and Research Centre'
#     Dr_BR_Ambedkar_Medical_College='Dr BR Ambedkar Medical College'
#     KasturbaMedicalCollege='Kasturba Medical College'
#     SapthagiriInstituteofMedicalSciencesandResearchCenter='Sapthagiri Institute of Medical Sciences and Research Center, Bangalore'
#     VeterinaryCollege='Veterinary College, Hebbal'
#     NationalInstituteofMentalHealthandNeuroSciences='National Institute of Mental Health and Neuro Sciences Bangalore'
#     BGS_GlobalInstituteofMedicalSciences='BGS Global Institute of Medical Sciences, Bangalore'
#     InstituteofAerospaceMedicine='Institute of Aerospace Medicine, Bangalore'
#     St_Johns_NationalAcademyofHealthSciences="St John's National Academy of Health Sciences, Bangalore"
#     GovernmentHomeopathicMedicalCollegeandHospital='Government Homeopathic Medical College and Hospital, Bangalore'
#     GovernmentDentalCollegeandResearchInstitute='Government Dental College and Research Institute, Bangalore'
#     DayanandaSagarCollegeofPhysiotherapy='Dayananda Sagar College of Physiotherapy, Banglore'
#     MS_RamaiahDentalCollegeandHospital='MS Ramaiah Dental College and Hospital, Bangalore'
#     EastPointCollegeofMedicalSciencesandResearchCentre='East Point College of Medical Sciences and Research Centre, Bangalore'
#     SriKalabyraveshwaraSwamyAyurvedicMedicalCollege='Sri Kalabyraveshwara Swamy Ayurvedic Medical College, Bangalore'
#     TheOxfordMedicalCollegeHospitalandResearchCentre='The Oxford Medical College Hospital and Research Centre, Bangalore'
#     TheOxfordDentalCollegeandHospital='The Oxford Dental College and Hospital, Bangalore'
#     MVJMedicalCollegeandResearchHospital='MVJ Medical College and Research Hospital, Hoskote'
#     RajaRajeshwariMedicalCollegeandHospital='Raja Rajeshwari Medical College and Hospital'
#     Other = 'Other'
    
#     Medical_colleges = [
#     (Other,'Other'),
#     (BangaloreMedicalCollegeandResearchInstitute,'Bangalore Medical College and Research Institute'),
#     (St_JohnsMedicalCollege,'St Johns Medical College, Bangalore'),
#     (MS_RamaiahMedicalCollege,'MS Ramaiah Medical College'),
#     (KempegowdaInstituteofMedicalSciences,'Kempegowda Institute of Medical Sciences'),
#     (VydehiInstituteofMedicalSciencesandResearchCentre,'Vydehi Institute of Medical Sciences and Research Centre'),
#     (Dr_BR_Ambedkar_Medical_College,'Dr BR Ambedkar Medical College'),
#     (KasturbaMedicalCollege,'Kasturba Medical College'),
#     (SapthagiriInstituteofMedicalSciencesandResearchCenter,'Sapthagiri Institute of Medical Sciences and Research Center, Bangalore'),
#     (VeterinaryCollege,'Veterinary College, Hebbal'),
#     (NationalInstituteofMentalHealthandNeuroSciences,'National Institute of Mental Health and Neuro Sciences Bangalore'),
#     (BGS_GlobalInstituteofMedicalSciences,'BGS Global Institute of Medical Sciences, Bangalore'),
#     (InstituteofAerospaceMedicine,'Institute of Aerospace Medicine, Bangalore'),
#     (St_Johns_NationalAcademyofHealthSciences,"St John's National Academy of Health Sciences, Bangalore"),
#     (GovernmentHomeopathicMedicalCollegeandHospital,'Government Homeopathic Medical College and Hospital, Bangalore'),
#     (GovernmentDentalCollegeandResearchInstitute,'Government Dental College and Research Institute, Bangalore'),
#     (DayanandaSagarCollegeofPhysiotherapy,'Dayananda Sagar College of Physiotherapy, Banglore'),
#     (MS_RamaiahDentalCollegeandHospital,'MS Ramaiah Dental College and Hospital, Bangalore'),
#     (EastPointCollegeofMedicalSciencesandResearchCentre,'East Point College of Medical Sciences and Research Centre, Bangalore'),
#     (SriKalabyraveshwaraSwamyAyurvedicMedicalCollege,'Sri Kalabyraveshwara Swamy Ayurvedic Medical College, Bangalore'),
#     (TheOxfordMedicalCollegeHospitalandResearchCentre,'The Oxford Medical College Hospital and Research Centre, Bangalore'),
#     (TheOxfordDentalCollegeandHospital,'The Oxford Dental College and Hospital, Bangalore'),
#     (MVJMedicalCollegeandResearchHospital,'MVJ Medical College and Research Hospital, Hoskote'),
#     (RajaRajeshwariMedicalCollegeandHospital,'Raja Rajeshwari Medical College and Hospital'),
#     ]

#     name = models.CharField(max_length=20)
#     phone = models.CharField(max_length=12)
#     branch = models.CharField(max_length=100, choices=Medical_branches, default=Other)
#     college = models.CharField(max_length=100, choices=Medical_colleges, default=Other)
#     created_on=models.DateField(auto_now_add=True)
#     class Meta:
#         ordering = ['created_on']
        
#     def __str__(self):
#         return 'By {} on {}'.format(self.name,self.created_on)
    