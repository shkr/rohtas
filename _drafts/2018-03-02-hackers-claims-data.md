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

Hospitals collect and store electronic health records including but not limited to claims, prescriptions, orders for tests, viewing laboratory or imaging results, and clinical progress notes. In a published deep learning work, "Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records" showed how one can process hospital data (they used data from Mount Sinai hospital system) and using a data driven way identify key features that can identify future diagnoses for a patient. 

EHR/EMR software is used by hospitals, clinics, rehab centers and other medical facilities to collect this type of healthcare data. These softwares sometimes provide features like clinical decision support rules or system to aid the clinician's workflow. Integrated software solutions scrubs the EHR data to submit electronic claim files to the payer. The file format depends on the use case between the provider and payer.

| Provider                |                 Semantic File Type                 |                 Payer |
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

Often providers often send these electronic claim submissions to clearinghouses which act as a central hub where all the data files are sorted and directed to their respective insurance carriers. They use internal software to receive claims from healthcare providers, scrub them for errors and formats if required as per HIPAA and insurance standards. The field name definitions of these file formats are maintained in a data dictionary which is used to encode data into an X12 formt during exchange. CSV, XML or piped separation is also sometimes used to encode these files when exchanging. They have an important role because medical practises send high quantities of insurance claim files.

Another recent work on https://arxiv.org/abs/1801.07860 https://www.nature.com/articles/srep26094 talks about how "We propose a representation of patients’ entire, raw EHR records based on the Fast Healthcare Interoperability Resources (FHIR) format. "

So what is this FHIR and what is good about it? FHIR is data format for storing EHR data, just how 'graph' database like neo4j is a better way to store network data rather than a bunch of PostGREs tables, because data and metadata is easily retreivable. 
FHIR specification is publicly available, it defines where the diagnosis, procedure, encountry type etc information should be stored so that it is indexed in a way that makes the writing data pipelines code, easier. In this work they were able to leverage it to pull together all the EHR stored in FHIR format about a patient and condense it into a semantic vector.

Sending over the claims is just the first part, it is followed by adjudiction. This is where your insurance company runs it checks and sends an adjustment file, a remit file with an approved/denied flag to notify the provider whether the provider is going to get paid or not.

So why does it happen can't the provider do the checks on their own? In the process they make necessary adjustments to the claims based on information that better maintained by insurance companies.

Claim or Encounter 837 files or 837 There is purpose behind each of those data types, ICDs are diagnoses, NDCs are medication, CPTs are procedures, LOINCs are laboratory 
tests and clinical notes are generally written by the doctor.  

Each of the coding system has a fully fledged ontology which is also consistently evolving. For example ICD coding system has moved from
version 9 to version 10 as per regulation, and there is already ICD11 on the way. Each of these codes is an identifier for a diagnosis
at a varying levels of granularities. 

CPTs are released by AAPC. They have over the years, evolved into being very specific. For outpatient procedures, the reimbursement is negotiated
for groups of such codes. CMS releases a fee schedule that Medicare agrees to pay to clinics for each of the services.


The remittances or 835s contain most importantly cost information and line item based amt_allowed. Often the bill that you get from your hospital, where they calculate your co-pay etc contains most of the information present in remit.

'''
42 U.S. Code Subchapter XVIII - HEALTH INSURANCE FOR AGED AND DISABLED
42 U.S. Code § 1395ww - Payments to hospitals for inpatient hospital services

(1)(A)(i) The Secretary, in determining the amount of the payments that may be made under this subchapter with 
respect to operating costs of inpatient hospital services (as defined in paragraph (4)) shall not recognize as 
reasonable (in the efficient delivery of health services) costs for the provision of such services by a hospital for a 
cost reporting period to the extent such costs exceed the applicable percentage (as determined under clause (ii)) of the average
 of such costs for all hospitals in the same grouping as such hospital for comparable time periods.
'''https://www.law.cornell.edu/uscode/text/42/1395ww 


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

Source:
https://files.medi-cal.ca.gov/pubsdoco/publications/masters-mtp/.../revcdip_i00.doc


Part 3
---
How is it related to cashflow, or how does it link to real dollars?
9. Why is there a premium and what is an HSA, Classing vs Smoothing - The actuarials struggle
  What are these other things?
  Co-Pay, Deductibles, AMT_ALLOWED, PATIENT_RESPONSIBILITY_AMT, CONTRACT ADJUSTMENT AMOUNT
    Ask for contract adjustment, find deductible, find how much you have to pay
10. Who owns the data pipelines?
  The data pipelines 
11. Market Share of different hospital chains and labs in the provider space
12. Market Share of different payers


Part 4
---
Resources for

13. Hospital Compare and other datasets like physician compare
14. CMS Medicare Physician Fee Schedule and other medicare release fee schedule
15. Cost for Inpatient (Average cost statistics for Hospitals)
16. Cost for Outpatient (Amino.com)





