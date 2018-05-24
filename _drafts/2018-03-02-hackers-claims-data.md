---
layout: post
title:  "Hacker's summary of healthcare data"
date:   2018-05-24 18:42:04 -0800
categories: analytical
---



>  Yesterday, 45 minutes of my life was taken up by scrawling my signature and date across the bottom of home care forms. Truth be told, I'm not really sure what these forms do, except allow the agencies that are delivering care to our patients in the community to say look, see this, Dr. Pelzman signed it and says we can do it, so therefore we are justified in getting paid.
>
> [medpagetoday.com](https://www.medpagetoday.com/patientcenteredmedicalhome/patientcenteredmedicalhome/72962?xid=nl_mpt_Quiz_2018-05-18&eun=g972116d0r) / Show Me Where to Sign  by Fred N. Pelzman, MD                                                                                                               May 18, 2018                                                                     



![OpenEMR - Web snapshot of an open source implementation of an EMR System](https://www.dropbox.com/s/08c7lzxq4kvt8v3/Screen%20Shot%202018-05-23%20at%207.33.29%20AM.png?dl=1)

​							https://www.open-emr.org/



I read "How are days became numbered" around the same time I had decided to put together a 
hackers guide to healthcare data. A stitched together version of healthcare claims data knowledge I have accumulated from books, blog, published work and people who have worked in the healthcare industry. As a software engineer I was not able to find one good introduction of healthcare claims data that would let me just focus on figuring out what code I had to write for making data pipelines. This challenge is not unknown, healthcare IT is a tough space to break into as a software engineer or a software company. 

"How are days became numbered" is a book which describes the evolution of data aggregation practises at insurance corporations. Data aggregation by insurance corporations has way over a century now has  allowed them to calculate and underwrite risk of policies that they sell. Companies used data aggregated from large letter writing networks, research organizations and sometimes even individualized risk cards much like credit score reporting agencies of today for assessing risk of policyholders. They grouped individuals into risk pools, a process described as classing. In order to underwrite they just needed a way to assess the risk of paying out policies before time. Companies hired actuaries and experts to set these premiums and dividend returns and provided them with the data for it. Today, healthcare data has moved from paper to ftp servers and data collection work has moved into doctors offices. But, the biggest consumers of healthcare data continue to be insurance companies and they have a strong influence on the supply side of healthcare data.

## File Types

Hospitals collect and store electronic health records including but not limited to claims, prescriptions, orders for tests, viewing laboratory or imaging results, and clinical progress notes. In a published deep learning work, "Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records" showed how one can process hospital data (they used data from Mount Sinai hospital system) and using a data driven way identify key features that can identify future diagnoses for a patient. 

EHR/EMR software is used by hospitals, clinics, rehab centers and other medical facilities to collect this type of healthcare data. These softwares sometimes provide features like clinical decision support rules or system to aid the clinician's workflow. Integrated software solutions scrubs the EHR data to submit electronic claim files to the payer. The file format depends on the use case between the provider and payer.

| Provider                |                Semantic File Format                |                 Payer |
| ----------------------- | :------------------------------------------------: | --------------------: |
| Admitting               |              Eligibility Inquiry 270               | Verification Function |
| Admitting               |              Eligibility Inquiry 271               | Verification Function |
| Utilization Review      |             Certification Request 278              |    Utilization Review |
| Utilization Review      |             Certification Response 278             |    Utilization Review |
| Billing and Collections |                Claim/Encounter 837                 |     Claims Processing |
| Billing and Collections |                 Status Inquiry 276                 |     Claims Processing |
| Billing and Collections |                Status Response 277                 |     Claims Processing |
| Billing and Collections |               Payment/Remittance 835               |     Claims Processing |
| Treasury                | 835 with payment from providers to payers via bank |              Treasury |

Providers send these electronic claim submissions to clearinghouses which act as a central hub where all the data files are sorted and directed to their respective insurance carriers. They use internal software to receive claims from healthcare providers, scrub them for errors and formats if required as per HIPAA and insurance standards. The field name definitions of these file formats are maintained in a data dictionary which is used to encode data into an X12 formt during exchange. CSV, XML or piped separation is also sometimes used to encode these files when exchanging. They have an important role because medical practises send high quantities of insurance claim files.

## Concept Identifiers

Another work quoted below on integrating machine learning workflows to healthcare data shows how custom electronics health records with clinical notes information can be transformed and stored as FHIR resources to improve effectiveness of deep learning models for personialized clinical prediction on patient data.

> Our central insight was that rather than explicitly harmonizing EHR data, mapping it into a highly curated set of structured predictors variables and then feeding those variables into a statistical model, we could instead learn to simultaneously harmonize inputs and predict medical events through direct feature learning.
>
> https://arxiv.org/ftp/arxiv/papers/1801/1801.07860.pdf

FHIR is a data interchange specification which supports a semantic encoding scheme that can be used to exchange data between software systems. There are a standard set of field names and values defined as resource types in the FHIR specification. Usage of FHIR can allow any software to read and interpret data from a varierty of EHR systems. Patient, DiagnosticReport, Claim, Observation, PaymentNotice are some examples of  FHIR resource types. 

![Scalable and accurate deep learning with electronic health records, Alvin Rajkomar et. Al 2018](https://www.dropbox.com/s/kp1p3ayve1nrukr/Screen%20Shot%202018-05-23%20at%207.41.33%20AM.png?dl=1)

​         Scalable and accurate deep learning with electronic health records, Alvin Rajkomar et. al (2018) 



Because EHR data is used for insurance claims, medical practitioners carefully encode patient information in diagnosis codes such (ex: ICD9, ICD10), procedure codes (ex: CPT codes, HCPCS codes), medication codes (NDC, RXNORM) for prescriptions, lab result codes and lab order (LOINC) codes for accurate billing and payment from the  payers after adjudication. There exists redundancy across these coding systems. However the coding organizations rarely do official releases of crosswalks between these coding systems. SNOMED is a comprehensive coding system encompassing diagnosis, symptoms, procedures concepts, therefore there are crosswalks available between SNOMED and ICD, SNOMED and CPT. But fee schedules such as the CMS Physician Fee Schedule, Inpatient Billing Systems and most outpatient billing contracts between healthcare providers and payers set rules conditioned on ICD, CPT, revenue codes and DRG codes, not SNOMED codes. 

837 files are composed of two parts, a header and a list of service lines. The header contains primary and secondary diagnosis information about the patient encoded as ICD9 or ICD10 codes for the encounter period of the claim. Electronic claim filing code indicator, electronic payer code, allowed amount, allowed billed, and other fields. The service lines have CPT (HCPCS Level I), HCPCS (Level 2) and revenue codes for the services rendered during the encounter period. CPT, HCPCS Level 2 were developed and currently maintained by American Medical Association AMA, ICD Panel, HCPCS National Panel respectively. Based on information from their [website](https://www.cdc.gov/nchs/icd/index.htm), National Center for Health Statistics (NCHS) has a role in the development of ICD9 and ICD10.  

ICD, CPT, HCPCS are some examples of medical coding systems, there are plenty. LOINC is a coding system for health measurements, observations, and documents such as lab test orders and lab results. There is overlap between coding systems. A GFRAA > 120 in LOINC is equal to CARDIAC DEFIB in ICD. There are no official crosswalks between any two of these coding systems. SNOMED Clinical Terminology has a coding system which is expansive and covers services rendered, diagnosis, symptom, demographi information. SNOMED has released crosswalk between SNOMED CT codes and ICD10. Crosswalks between coding systems can be created via SNOMED-CT.

ICDs and CPTs have a hierarchichal coding structure. Adjacent codes in a sorted list of CPTs and ICDs are mean different versions of the same procedure such as abdominal-mri with contrast 74182 and abdominal-mri without contrast 74181. Unless the codes belong to two different groups. The group of a CPT or ICD code can be identified from the first two digits of the code. NDC is a coding system used to identify prescrition drugs in claims. RXNORM is standardized name respository for medication and links to NDC and other prescription drug coding systems. 

These coding systems are used to calculate some weighted risk formula in value based payment systems. Insurance corporations can also use them to negotiate cost of service. For example, CMS developed and maintains a physician fee schedule with medicare's amount allowed for each of the outpatient services identified using CPT codes. 

835 files are sent after the claim is submitted. It might include adjustments such as denial or partial payment for the encounter period on the claim. It is composed of two parts, header and service lines. It has the codes submitted in the claim and the amount allowed for the corresponding submitted claim. Both 837 and 835 files have NPI in the form of BILLING NPI, PROVIDER NPI, REFERRING PROVIDER NPI which identifies the National Provider Identification code of the medical facility which is billing, the medical practitioner who rendered services listed on the claim, the medical practitioner who referred the patient to the provider mentioned in the submitted claim. 835 files contain fields such AMOUNT ALLOWED, BILLED AMOUNT, CO-PAY AMOUNT, DEDUCTIBLE etc. These values can be used to calculate the discount offered to the payer by the provider. 



## Sources of healthcare data 

![](https://s86vkjuqei14qm8e2sawxz2m-wpengine.netdna-ssl.com/wp-content/uploads/Most-Useful-Sources-of-Health-Care-Data-Today-and-in-5-Years.png)

>  42 U.S. Code Subchapter XVIII - HEALTH INSURANCE FOR AGED AND DISABLED
>
> 42 U.S. Code § 1395ww - Payments to hospitals for inpatient hospital services
>
> (1)(A)(i) The Secretary, in determining the amount of the payments that may be made under this subchapter with respect to operating costs of inpatient hospital services (as defined in paragraph (4)) shall not recognize as reasonable (in the efficient delivery of health services) costs for the provision of such services by a hospital for a cost reporting period to the extent such costs exceed the applicable percentage (as determined under clause (ii)) of the average of such costs for all hospitals in the same grouping as such hospital for comparable time periods.
>
> — https://www.law.cornell.edu/uscode/text/42/1395ww 

Clinical Data

CMS Medicare Advantage uses HCC Coding in its payment system to create a risk score for patients based on their past medical history represented using ICD diagnosis codes and other information such as age about the patients. Clinicial decision support rules also make use of coding systems for stratitifying patient populations for assigning better care management practicesby their hospital systems and payers.  For example, Framingham Risk Score is a gender specific used to estimate the 10-year cardiovascular risk of an individual using age, gender, tobacco smoker indicator, Systolic blood pressure along with HDL and total cholesterol levels. The thresholds on scores have been found to underestimate or overestimate risk in some population types. For example Framingham Risk Score can overestimate or underestimate risk for hispanic and native american population in US as described in this work, <u>Improving Global Vascular Risk Prediction With Behavioral and Anthropometric Factors: The Multiethnic NOMAS (Northern Manhattan Cohort Study) Ralph L.Sacco MD, MS et. al (2006).</u> 

Cost data

Diagnosis-related groups (DRG) Groups (DRG) reimbursement methodology used at inpatient general acute care hospitals uses information on the claim form (including revenue codes, diagnosis and procedure codes, patient’s age, discharge status and complications) to classify the hospital stay into a group.  DRG payment is determined by multiplying a specific DRG relative weight of the individual group code by a DRG hospital’s specific DRG base price, with application of adjustors and add-on payments as applicable. Before this they used revenue codes. These DRG codes are calculated based on patient's health status at the time of admission. APR-DRG coding system has a severity level defined for each of its DRG codes, it requires very detailed information about the healthcare profile of the patient in order to be assigned. Refer to cost files. 

Patient generated data or data not in EHR systems thus way more efficient, is aggregated from Fitbit, MapMyRun, Apple Health and other software products which are directly used by consumers. This algorithm on cardiac arrythmia uses heart pulse rate. This data sources are also administered by HIPAA regulation however, the practices may differ between companies. 

Patient Preference or Survey data

HCAHPS (the Hospital Consumer Assessment of Healthcare Providers and Systems) is a patient satisfaction survey required by CMS (the Centers for Medicare and Medicaid Services) for all hospitals in the United States.  The Survey is for adult inpatients, excluding psychiatric patients.  MGH administers the survey to our patients by phone shortly after discharge. 

Leapfrog and quality scores

Other survey data

Pharma & Genomics data 

In clinical trials, patient health status has to be assessed with finer details. Genomics data about a patient have seen to correlate with trails outcomes. This level of data is tedious to extract because these are often handwritten clinical notes, chart information, and file uploads of genomic text files. 

Parsing Patient Qualification Criteria, clinicaltrials.gov

NDC, VETERANS, RXNORM, UPTODATE are sources on medication. There are companies like generable that hope to bring bayesian statistics to pharmacokinetics.



-----



If you have ideas, criticism or data for new sections that should have been present here but I missed it, please write to me at hackersguidetohealthcaredata@gmail.com or discuss in the comments section below.