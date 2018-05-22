---
layout: post
title:  "Hacker's Guide to understanding healthcare claims data"
date:   2018-03-02 18:42:04 -0800
categories: analytical
---



>  Yesterday, 45 minutes of my life was taken up by scrawling my signature and date across the bottom of home care forms. Truth be told, I'm not really sure what these forms do, except allow the agencies that are delivering care to our patients in the community to say look, see this, Dr. Pelzman signed it and says we can do it, so therefore we are justified in getting paid.
>
> [medpagetoday.com](https://www.medpagetoday.com/patientcenteredmedicalhome/patientcenteredmedicalhome/72962?xid=nl_mpt_Quiz_2018-05-18&eun=g972116d0r) / Show Me Where to Sign  by Fred N. Pelzman, MD                                                                                                               May 18, 2018                                                                     



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

## Coding Systems

Another work quoted below on integrating machine learning workflows to healthcare data shows how custom electronics health records with clinical notes informtion can be transformed and stored as FHIR resources to improve effectiveness of deep learning models for personialized clinical prediction on patient data.

> Our central insight was that rather than explicitly harmonizing EHR data, mapping it into a highly curated set of structured predictors variables and then feeding those variables into a statistical model, we could instead learn to simultaneously harmonize inputs and predict medical events through direct feature learning.
>
> https://arxiv.org/ftp/arxiv/papers/1801/1801.07860.pdf

FHIR is a data interchange  specification supports semantic and encoding scheme interoperability between software systems. There are a standard set of field names and values defined as resource types in the FHIR specification. Usage of FHIR can allow any software to read and interpret data from a varierty of EHR systems. Patient, DiagnosticReport, Claim, Observation, PaymentNotice are some examples of  FHIR resource types. 

Because EHR data is used for insurance claims, medical practitioners carefully encode patient information in diagnosis codes such (ex: ICD9, ICD10), procedure codes (ex: CPT codes, HCPCS codes), medication codes (NDC, RXNORM) for prescriptions, lab result codes and lab order (LOINC) codes for accurate billing and payment from the  payers after adjudication. There exists redundancy across these coding systems. However the coding organizations rarely do official releases of crosswalks between these coding systems. SNOMED is a comprehensive coding system encompassing diagnosis, symptoms, procedures concepts, therefore there are crosswalks available between SNOMED and ICD, SNOMED and CPT. But fee schedules such as the CMS Physician Fee Schedule, Inpatient Billing Systems and most outpatient billing contracts between healthcare providers and payers set rules conditioned on ICD, CPT, revenue codes and DRG codes, not SNOMED codes. 

837 files are composed of two parts, a header and a list of service lines. The header contains primary and secondary diagnosis information about the patient encoded as ICD9 or ICD10 codes for the encounter period of the claim. These diagnosis codes are sometimes used for adjudication. Electronic claim filing code indicator, electronic payer code, allowed amount, allowed billed, and other fields that are required for routing the claim by the clearing house and generate a remittance response in return from the insurer are present in th header. The service lines have CPT, HCPCS and revenue codes which itemizes the procedures performed during the encounter period. 

ICD 9 codes are used for many purposes. In hospital claims diagnosis codes along with other codes and information are used to assign a diagnosis related group category code and a severity index during an inpatient stay. CMS uses Hierarchical Condition Category (HCC) coding to calculate different payments for medicare advantage patients based on the diagnosis codes present in their recent medical history, age, gender and other clinical rules. Healthcare IT is transitioning from ICD9 to ICD10.

CPT codes released by AAPC. These codes have an inherent hierarchy just like ICD codes. For outpatient procedures, the reimbursement is negotiated for groups of such codes. CMS releases a fee schedule that Medicare agrees to pay to clinics for each of the services.

Revenue codes

LOINC codes

RXNORM, Veteran NDC

The remittances or 835s contain most importantly cost information and line item based amt_allowed. Often the bill that you get from your hospital, where they calculate your co-pay etc contains most of the information present in remit. Fields in 835

## Entities

> 42 U.S. Code Subchapter XVIII - HEALTH INSURANCE FOR AGED AND DISABLED
>
> 42 U.S. Code § 1395ww - Payments to hospitals for inpatient hospital services
>
> (1)(A)(i) The Secretary, in determining the amount of the payments that may be made under this subchapter with respect to operating costs of inpatient hospital services (as defined in paragraph (4)) shall not recognize as reasonable (in the efficient delivery of health services) costs for the provision of such services by a hospital for a cost reporting period to the extent such costs exceed the applicable percentage (as determined under clause (ii)) of the average of such costs for all hospitals in the same grouping as such hospital for comparable time periods.
>
> —  https://www.law.cornell.edu/uscode/text/42/1395ww 

Setting prices is a billion dollar industry (rought estimate from 3M etc). Keeping in the spirit of the post, if you are in data science and
if you have dealt with remits or claims, you might have seen the provider billing npi field. This is the National Provider Identifier NPI used by 
healthcare service providers to  claim a reimbursement for your use of healthcare. They definitely maintain their own identifiers to group
of these NPIs since rates are generally negotiated at a level higher than NPIs. 

Insurers negotiate prices for individual services or blocks of services. These services are encoded using
Services given to the patient are itemized using Current Procedure Terminology codes. These codes
are used to calculate bills to be paid to the provider. The provider sends the codes in a claim
for adjudication and then the payer after processing the claim, sends an Electornic Remittance Advices
stating the amount it has agreed to pay to the provider.  

7. How does outpatient billing work and what is REVENUE_CODE?
The revenue codes are used by providers to charge a lump sum. 

8. How does inpatient billing work? (Acute Inpatient Care) and what is DRG?
	n July 2013 Medi-Cal adopted a diagnosis-related groups (DRG) Groups (DRG)	
reimbursement methodology for inpatient general acute care hospitals that do not 
participate in certified public expenditure reimbursement.  DRG is a reimbursement 
methodology that uses information on the claim form (including revenue codes, 
diagnosis and procedure codes, patient’s age, discharge status and complications) to 
classify the hospital stay into a group.  DRG payment is determined by multiplying a 
specific DRG relative weight of the individual group code by a DRG hospital’s specific 
DRG base price, with application of adjustors and add-on payments as applicable.  
If a Treatment Authorization Request (TAR) has been approved by the Department of 
Health Care Services (DHCS), DRG payment is for each admit through discharge claim.
Refer to the Diagnosis-Related Groups (DRG):  Inpatient Services section in this 
provider manual for additional information.

NPIs



Source:
https://files.medi-cal.ca.gov/pubsdoco/publications/masters-mtp/.../revcdip_i00.doc


9. Why is there a premium and what is an HSA, Classing vs Smoothing - The actuarials struggle
  What are these other things?
  Co-Pay, Deductibles, AMT_ALLOWED, PATIENT_RESPONSIBILITY_AMT, CONTRACT ADJUSTMENT AMOUNT
    Ask for contract adjustment, find deductible, find how much you have to pay


Sources and related reading
---


