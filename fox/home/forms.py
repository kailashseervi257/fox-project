from .models import Subscribers, Engineering_form
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
    branch = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Engg_branches, required=True,help_text='Atleast one choice')
    # college=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Engg_colleges)
    class Meta:
        model = Engineering_form
        fields = ('name', 'phone','email', 'branch','TwelfthPercentage','applied_for')
        
# class Medical_Form(forms.ModelForm):
#     class Meta:
#         model = Medical_form
#         fields=('name','phone','branch', 'college')