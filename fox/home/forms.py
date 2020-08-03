from .models import Subscribers, Engineering_form, Medical_form, Aviation_form, Architecture_form, PGMedical_form
from django import forms

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)


# -----------Engineering Form-------------------



class Engineering_Form(forms.ModelForm):
    ComputerScienceEngineering='Computer Science Engineering'
    ElectronicsandCommunication='Electronics & Communication'
    MechanicalEngineering='Mechanical Engineering'
    InformationScienceEngineering='Information Science Engineering'
    Biotechnology='Biotechnology'
    ElectricalandElectronicsEngineering='Electrical & ElectronicsEngineering'
    InformationTechnology='Information Technology'
    AerospaceEngineering='Aerospace Engineering'
    AeronauticalEngineering='Aeronautical Engineering'
    IndustrialEngineeringandManagement='Industrial Engineering & Management'
    AutomobileEngineering='Auto-mobile Engineering'
    BioMedicalEngineering='BioMedical Engineering'
    CivilEngineering='Civil Engineering'
    IndustrialandProductionEngineering='Industrial & Production Engineering'
    ChemicalEngineering='Chemical Engineering'
    other='Other'

    Engg_branches = [
        (ComputerScienceEngineering,'Computer Science Engineering'),
        (ElectronicsandCommunication,'Electronics & Communication'),
        (MechanicalEngineering,'Mechanical Engineering'),
        (InformationScienceEngineering,'Information Science Engineering'),
        (Biotechnology,'Biotechnology'),
        (ElectricalandElectronicsEngineering,'Electrical & ElectronicsEngineering'),
        (InformationTechnology,'Information Technology'),
        (AerospaceEngineering,'Aerospace Engineering'),
        (AeronauticalEngineering,'Aeronautical Engineering'),
        (IndustrialEngineeringandManagement,'Industrial Engineering & Management'),
        (AutomobileEngineering,'Auto-mobile Engineering'),
        (BioMedicalEngineering,'BioMedical Engineering'),
        (CivilEngineering,'Civil Engineering'),
        (IndustrialandProductionEngineering,'Industrial & Production Engineering'),
        (ChemicalEngineering,'Chemical Engineering'),
        (other,'Other'),
    ]
    MSRIT='MSRIT'
    RVCollegeOfEngineering='RV College Of Engineering'
    BMSCollegeOfEngineering='BMS College Of Engineering'
    DayanandSagarInstitutions='Dayanand Sagar Institutions'
    PESUniversity='PES University'
    NewHorizonCollegeOfEngineering='New Horizon College Of Engineering'
    CambridgeInstituteOfTechnology='Cambridge Institute Of Technology'
    MVJCollegeOfEngineering='MVJ College Of Engineering'
    SeaCollegeOfEngineering='Sea College Of Engineering'
    GopalanCollegeOfEngineeringandManagement='Gopalan College Of Engineering & Management'
    VenkateswaraCollegeOfEngineering='Venkateswara College Of Engineering'
    BNMInstituteOfTechnology='BNM Institute Of Technology'
    JainUniversity='Jain University'
    BangaloreInstituteOfTechnology='Bangalore Institute Of Technology'
    AcharyaInstituteOfTechnology='Acharya Institute Of Technology'
    DrAmbedkarInstituteOfTechnology='Dr. Ambedkar Institute Of Technology'
    PresidencyUniversity='Presidency University'
    ChristUniversity='Christ University'
    TheOxfordInstitutions='The Oxford Institutions'
    CMRIT='CMR Institute Of Technology'
    AmrithaSchoolOfEngineering='Amritha School Of Engineering'
    RNSInstituteOfTechnology='RNS Institute Of Technology'
    PESInstituteofTechnologySouthCampus='PES Institute of Technology= South Campus'
    AllianceCollegeOfEngineeringandDesign='Alliance College Of Engineering & Design'
    RajarajeshwariCollegeOfEngineering='Rajarajeshwari College Of Engineering'
    EastWestInstituteOfTechnology='East West Institute Of Technology'
    SJBIT='SJB Institute Of Technology'
    HKBK='HKBK College Of Engineering'
    DBIT='Don Bosco Institute Of Technology'
    AtriaInstituteOfTechnology='Atria Institute Of Technology'
    EastPointCollegeOfEngineeringandTechnology='East Point College Of Engineering & Technology'
    Other='Other'



    Engg_colleges = [
        (Other,'Other'),
        (MSRIT,'MSRIT'),
        (RVCollegeOfEngineering,'RV College Of Engineering'),
        (BMSCollegeOfEngineering,'BMS College Of Engineering'),
        (DayanandSagarInstitutions,'Dayanand Sagar Institutions'),
        (PESUniversity,'PES University'),
        (NewHorizonCollegeOfEngineering,'New Horizon College Of Engineering'),
        (CambridgeInstituteOfTechnology,'Cambridge Institute Of Technology'),
        (MVJCollegeOfEngineering,'MVJ College Of Engineering'),
        (SeaCollegeOfEngineering,'Sea College Of Engineering'),
        (GopalanCollegeOfEngineeringandManagement,'Gopalan College Of Engineering & Management'),
        (VenkateswaraCollegeOfEngineering,'Venkateswara College Of Engineering'),
        (BNMInstituteOfTechnology,'BNM Institute Of Technology'),
        (JainUniversity,'Jain University'),
        (BangaloreInstituteOfTechnology,'Bangalore Institute Of Technology'),
        (AcharyaInstituteOfTechnology,'Acharya Institute Of Technology'),
        (DrAmbedkarInstituteOfTechnology,'Dr. Ambedkar Institute Of Technology'),
        (PresidencyUniversity,'Presidency University'),
        (ChristUniversity,'Christ University'),
        (TheOxfordInstitutions,'The Oxford Institutions'),
        (CMRIT,'CMR Institute Of Technology'),
        (AmrithaSchoolOfEngineering,'Amritha School Of Engineering'),
        (RNSInstituteOfTechnology,'RNS Institute Of Technology'),
        (PESInstituteofTechnologySouthCampus,'PES Institute of Technology, South Campus'),
        (AllianceCollegeOfEngineeringandDesign,'Alliance College Of Engineering & Design'),
        (RajarajeshwariCollegeOfEngineering,'Rajarajeshwari College Of Engineering'),
        (EastWestInstituteOfTechnology,'East West Institute Of Technology'),
        (SJBIT,'SJB Institute Of Technology'),
        (HKBK,'HKBK College Of Engineering'),
        (DBIT,'Don Bosco Institute Of Technology'),
        (AtriaInstituteOfTechnology,'Atria Institute Of Technology'),
        (EastPointCollegeOfEngineeringandTechnology,'East Point College Of Engineering & Technology'),
    ]
    phone=forms.CharField(required=True, help_text='Your 10 digit mobile number.')
    email=forms.EmailField(required=True)
    TwelfthPercentage = forms.FloatField(label='12th/2nd PUC Percentage',required=True)
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Engg_branches, required=True,help_text="Branches you're interested in.")
    # college=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Engg_colleges)
    class Meta:
        model = Engineering_form
        fields = ('name', 'phone','email', 'branch','TwelfthPercentage','applied_for')
        


# -----------Medical Form-------------------

class Medical_Form(forms.ModelForm):
    MBBS='MBBS (Bachelor of Medicine and Bachelor of Surgery)'
    BDS='BDS (Bachelor of Dental Surgery)'
    BScNursing='B.SC. NURSING'
    B_PHARMA='B.PHARM. (BACHELOR OF PHARMACY)'
    PHARM_D='PHARM D ( Doctor of Pharmacy)'
    BAMS='BAMS (Bachelor of Ayurvedic Medicine and Surgery)'
    BHMS='BHMS (Bachelor of Homeopathic Medicine and Surgery)'
    BUMS='BUMS ( Bachelor of Unani Medicine and Surgery)'
    BPT='BPT (Bachelor of Physiotherapy)'
    B_V_SC_and_A_H='B.V.SC. & A.H. (Bachelor of Veterinary Science and Animal Husbandry)'
    BOT='BOT (BACHELOR OF OCCUPATIONAL THERAPY)'
    BASLP='BASLP (BACHELOR OF AUDIOLOGY SPEECH LANGUAGE PATHOLOGY)'
    Other = 'Other'
    
    Medical_branches = [
        (MBBS,'MBBS (Bachelor of Medicine and Bachelor of Surgery)'),
        (BDS,'BDS (Bachelor of Dental Surgery)'),
        (BScNursing,'B.SC. NURSING'),
        (B_PHARMA,'B.PHARM. (BACHELOR OF PHARMACY)'),
        (PHARM_D,'PHARM D ( Doctor of Pharmacy)'),
        (BAMS,'BAMS (Bachelor of Ayurvedic Medicine and Surgery)'),
        (BHMS,'BHMS (Bachelor of Homeopathic Medicine and Surgery)'),
        (BUMS,'BUMS ( Bachelor of Unani Medicine and Surgery)'),
        (BPT,'BPT (Bachelor of Physiotherapy)'),
        (B_V_SC_and_A_H,'B.V.SC. & A.H. (Bachelor of Veterinary Science and Animal Husbandry)'),
        (BOT,'BOT (BACHELOR OF OCCUPATIONAL THERAPY)'),
        (BASLP,'BASLP (BACHELOR OF AUDIOLOGY SPEECH LANGUAGE PATHOLOGY)'),
        (Other , 'Other'),
    ]

    BangaloreMedicalCollegeandResearchInstitute='Bangalore Medical College and Research Institute'
    St_JohnsMedicalCollege='St Johns Medical College, Bangalore'
    MS_RamaiahMedicalCollege='MS Ramaiah Medical College'
    KempegowdaInstituteofMedicalSciences='Kempegowda Institute of Medical Sciences'
    VydehiInstituteofMedicalSciencesandResearchCentre='Vydehi Institute of Medical Sciences and Research Centre'
    Dr_BR_Ambedkar_Medical_College='Dr BR Ambedkar Medical College'
    KasturbaMedicalCollege='Kasturba Medical College'
    SapthagiriInstituteofMedicalSciencesandResearchCenter='Sapthagiri Institute of Medical Sciences and Research Center, Bangalore'
    VeterinaryCollege='Veterinary College, Hebbal'
    NationalInstituteofMentalHealthandNeuroSciences='National Institute of Mental Health and Neuro Sciences Bangalore'
    BGS_GlobalInstituteofMedicalSciences='BGS Global Institute of Medical Sciences, Bangalore'
    InstituteofAerospaceMedicine='Institute of Aerospace Medicine, Bangalore'
    St_Johns_NationalAcademyofHealthSciences="St John's National Academy of Health Sciences, Bangalore"
    GovernmentHomeopathicMedicalCollegeandHospital='Government Homeopathic Medical College and Hospital, Bangalore'
    GovernmentDentalCollegeandResearchInstitute='Government Dental College and Research Institute, Bangalore'
    DayanandaSagarCollegeofPhysiotherapy='Dayananda Sagar College of Physiotherapy, Banglore'
    MS_RamaiahDentalCollegeandHospital='MS Ramaiah Dental College and Hospital, Bangalore'
    EastPointCollegeofMedicalSciencesandResearchCentre='East Point College of Medical Sciences and Research Centre, Bangalore'
    SriKalabyraveshwaraSwamyAyurvedicMedicalCollege='Sri Kalabyraveshwara Swamy Ayurvedic Medical College, Bangalore'
    TheOxfordMedicalCollegeHospitalandResearchCentre='The Oxford Medical College Hospital and Research Centre, Bangalore'
    TheOxfordDentalCollegeandHospital='The Oxford Dental College and Hospital, Bangalore'
    MVJMedicalCollegeandResearchHospital='MVJ Medical College and Research Hospital, Hoskote'
    RajaRajeshwariMedicalCollegeandHospital='Raja Rajeshwari Medical College and Hospital'
    Other = 'Other'
    
    Medical_colleges = [
    (Other,'Other'),
    (BangaloreMedicalCollegeandResearchInstitute,'Bangalore Medical College and Research Institute'),
    (St_JohnsMedicalCollege,'St Johns Medical College, Bangalore'),
    (MS_RamaiahMedicalCollege,'MS Ramaiah Medical College'),
    (KempegowdaInstituteofMedicalSciences,'Kempegowda Institute of Medical Sciences'),
    (VydehiInstituteofMedicalSciencesandResearchCentre,'Vydehi Institute of Medical Sciences and Research Centre'),
    (Dr_BR_Ambedkar_Medical_College,'Dr BR Ambedkar Medical College'),
    (KasturbaMedicalCollege,'Kasturba Medical College'),
    (SapthagiriInstituteofMedicalSciencesandResearchCenter,'Sapthagiri Institute of Medical Sciences and Research Center, Bangalore'),
    (VeterinaryCollege,'Veterinary College, Hebbal'),
    (NationalInstituteofMentalHealthandNeuroSciences,'National Institute of Mental Health and Neuro Sciences Bangalore'),
    (BGS_GlobalInstituteofMedicalSciences,'BGS Global Institute of Medical Sciences, Bangalore'),
    (InstituteofAerospaceMedicine,'Institute of Aerospace Medicine, Bangalore'),
    (St_Johns_NationalAcademyofHealthSciences,"St John's National Academy of Health Sciences, Bangalore"),
    (GovernmentHomeopathicMedicalCollegeandHospital,'Government Homeopathic Medical College and Hospital, Bangalore'),
    (GovernmentDentalCollegeandResearchInstitute,'Government Dental College and Research Institute, Bangalore'),
    (DayanandaSagarCollegeofPhysiotherapy,'Dayananda Sagar College of Physiotherapy, Banglore'),
    (MS_RamaiahDentalCollegeandHospital,'MS Ramaiah Dental College and Hospital, Bangalore'),
    (EastPointCollegeofMedicalSciencesandResearchCentre,'East Point College of Medical Sciences and Research Centre, Bangalore'),
    (SriKalabyraveshwaraSwamyAyurvedicMedicalCollege,'Sri Kalabyraveshwara Swamy Ayurvedic Medical College, Bangalore'),
    (TheOxfordMedicalCollegeHospitalandResearchCentre,'The Oxford Medical College Hospital and Research Centre, Bangalore'),
    (TheOxfordDentalCollegeandHospital,'The Oxford Dental College and Hospital, Bangalore'),
    (MVJMedicalCollegeandResearchHospital,'MVJ Medical College and Research Hospital, Hoskote'),
    (RajaRajeshwariMedicalCollegeandHospital,'Raja Rajeshwari Medical College and Hospital'),
    ]
    phone=forms.CharField(required=True, help_text='Your 10 digit mobile number.')
    email=forms.EmailField(required=True)
    TwelfthPercentage = forms.FloatField(label='12th/2nd PUC Percentage',required=True)
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Medical_branches, required=True,help_text="Branches you're interested in.")

    class Meta:
        model = Medical_form
        fields = ('name', 'phone', 'email', 'branch', 'TwelfthPercentage', 'applied_for')
        
class Aviation_Form(forms.ModelForm):
    phone=forms.CharField(required=True, help_text='Your 10 digit mobile number.')
    email=forms.EmailField(required=True)
    TwelfthPercentage = forms.FloatField(label='12th/2nd PUC Percentage',required=True)
    class Meta:
        model = Aviation_form
        fields = ('name', 'phone', 'email', 'TwelfthPercentage')
        
class Architecture_Form(forms.ModelForm):
    choice=[('1','Yes'),('2','No')]
    phone=forms.CharField(required=True, help_text='Your 10 digit mobile number.')
    email=forms.EmailField(required=True)
    TwelfthPercentage = forms.FloatField(label='12th/2nd PUC Percentage', required=True)
    applied_for_NATA=forms.ChoiceField(widget=forms.RadioSelect,choices=choice,label='Applied for NATA?')
    class Meta:
        model = Architecture_form
        fields = ('name', 'phone', 'email', 'TwelfthPercentage', 'applied_for_NATA')
        
class PGMedical_Form(forms.ModelForm):
    Radiology='Radiology'
    Dermatology='Dermatology'
    Peadiatrics='Peadiatrics'
    Anaesthesiology='Anaesthesiology'
    GeneralMedicine='General Medicine'
    GeneralSurgery='General Surgery'
    Obstetrics='Obstetrics and Gynaecology'
    Orthopedics='Orthopedics'
    Opthalmology='Opthalmology'
    ForensicMedicine='Forensic Medicine'
    Anatomy='Anatomy'
    ENT='ENT'
    AnyNonClinical='AnyNonClinical'


    PGMedical_branches = [
        (Radiology, 'Radiology'),
        (Dermatology, 'Dermatology'),
        (Peadiatrics, 'Peadiatrics'),
        (Anaesthesiology, 'Anaesthesiology'),
        (GeneralMedicine, 'General Medicine'),
        (GeneralSurgery, 'General Surgery'),
        (Obstetrics, 'Obstetrics and Gynaecology'),
        (Orthopedics, 'Orthopedics'),
        (Opthalmology, 'Opthalmology'),
        (ForensicMedicine, 'Forensic Medicine'),
        (Anatomy, 'Anatomy'),
        (ENT, 'ENT'),
        (AnyNonClinical, 'AnyNonClinical'),
        
    ]
    phone=forms.CharField(required=True, help_text='Your 10 digit mobile number.')
    email=forms.EmailField(required=True)
    neet_score = forms.IntegerField(label='NEET score out of 1200',required=True)
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=PGMedical_branches, required=True,help_text="Branches you're interested in.")

    class Meta:
        model = PGMedical_form
        fields = ('name', 'phone', 'email', 'neet_score','branch')