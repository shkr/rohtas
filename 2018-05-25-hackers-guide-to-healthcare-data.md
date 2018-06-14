---
layout: solitary
title:  "Hacker's guide to healthcare data"
comments: true
---



> Yesterday, 45 minutes of my life was taken up by scrawling my signature and date across the bottom of home care forms. Truth be told, I’m not really sure what these forms do, except allow the agencies that are delivering care to our patients in the community to say look, see this, Dr. Pelzman signed it and says we can do it, so therefore we are justified in getting paid.       
>
> [Show Me Where to Sign](https://www.medpagetoday.com/patientcenteredmedicalhome/patientcenteredmedicalhome/72962?xid=nl_mpt_Quiz_2018-05-18&eun=g972116d0r) by Fred N. Pelzman, MD May 18, 2018 on medpagetoday.com

Getting an introduction to healthcare data is hard. This is because it's not well standardized and comprehensive oversight needs to be painfully assembled by going through countless books, blogs, published work etc.  

Software engineers and analysts who have worked with healthcare data and consequently had to resolve issues by working with data escrows (companies that facilitate data exchanges) would echo these challenges. There is also a complete lack of standard protocols for data exchanges between software systems. Information about data sources and means to facilitate exchanges within regulatory requirements are closely guarded like trade secrets. 

Finding online documentation is plain difficult. So even if somehow you are in a company with access to healthcare data, data wrangling is slow, painful and sometimes impossible. Gathering domain knowledge resources sufficient enough to perform data wrangling in healthcare IT is a long educative process. After gathering knowledge resources, navigating those resource references is also a productivity killer, if you are writing code everyday and have other challenges to work with. I figured I could make my life easier by stitching together that knowledge into one comprehensive post, a guide to healthcare data. 

Table of Contents

* TOC
{:toc}
## Healthcare data

Healthcare data recorded at medical centers such as physician offices, hospitals, nursing homes in care management settings by medical personnel is called Electronic Health Records (EHR) or Electronic Medical Records. This includes data collected from preventative care checkups. Healthcare data is also present in insurance claims, insurance remittances and pharmacy prescriptions. Healthcare research organizations do surveys to collect data from self inspection or patient feedback. Individuals generate healthcare data through sensors such as Apple Watch and Fitbit. It is of high scientific worth. Same is true of genomics data collected from gene sequencing done at labs or through services such as 23andMe. Data is also collected at diagnostic laboratories through blood or urine analysis, MRIs, X-Rays, EKGs and many other tests. Diagnostic data is used for differential diagnosis by physicians. 

Hospitals collect and store electronic health records including but not limited to claims, prescriptions, orders for tests, laboratory or imaging results, and clinical progress notes. Each of these files, contain some level of information about healthcare services performed on the patient, incurred healthcare costs, diagnostic inference of the physician and overall health status of the patient. Medical providers which include hospitals, laboratories, physician offices, outpatient centers such as urgent care, pharmacies, rehab centers frequently exchange data with insurance companies (aka payers) to get payments, measure financial or quality risk metrics and perform administrative tasks. 

## Longitudinal Patient Data

Over time providers and payers aggregate massive amount of healthcare data for a single patient in on-premise data warehouses. When data is moved for analytics, it may require de-identification of personal information as per HIPPA rules. There are a countable vendors which provide de-identification services such as de-id (<http://www.de-id.com/>), Universal Patient Key (UPK) and Privacy-Analytics (http://privacy-analytics.com). A time ordered sequence of patient’s data is known as patient’s longitudinal health data. Just to get an idea about the potency of healthcare data, in a recent published deep learning work, Deep Patient: An Unsupervised Representation to Predict the Future of Patients from the Electronic Health Records the authors showed how one can process hospital data (results were shown on data sourced from Mount Sinai hospital system) and use a data driven method to identify key features in a patient's longitudinal health data to predict future diagnoses with high accuracy.

## EHR Software Systems

Electronic Health Records (EHR) software implementations are used by hospitals, clinics, rehab centers and other medical facilities to collect, analyze and share patient healthcare data internally for administrative, care management, clinical and financial risk assessment, and claims filing purposes. These softwares sometimes provide features like clinical decision support rules to aid a clinician’s workflow. Integrated software solutions for claims administration used at medical practises, scrubs the EHR data to submit electronic claim files to the payer. The file format of what is exchanged depends on the use case between the provider and payer.

![img](https://lh4.googleusercontent.com/R_S2FFaKuIaJKRmtNF6U-cF_o1YMmr8eTDylhzGuNtcl4nkeUj1PYDg3YrOnyJ8vMK8tBXtpcDaQcAcQVQ2-DaFX45HhvuDXAghCBXusu0xSvQBlaStz31lGmDrAKRXs0V5WXYlx)
This is webpage snapshot of OpenEMR, an open source EHR System. Open source EHR implementations are not popular among large healthcare providers.

## File Formats

Providers send these electronic claim files to clearing houses (<https://en.wikipedia.org/wiki/Clearing_(finance)> which act as a central hub where all the data files are sorted and directed to their respective insurance carriers. They have an important role because medical practices send large quantities of claim files on a frequent basis. Clearing houses use internal software to receive claims from healthcare providers, scrub them for errors and re-format the file if required as per HIPAA (Health Insurance Portability and Accountability Act of 1996) and insurance standards. The common practice for sharing definitions of field names in these different file formats is usage of data dictionaries. These data dictionaries are necessary to encode these files into an X12 (see <http://www.x12.org/>) format which is a standard file encoding system for exchange. CSV, XML or piped separation is sometimes also used to encode these files when exchanging. 

In the figure below, the left column and the right column shows the function performed by a provider and payer respectively and the file type used to perform the data exchange. These exchanges are facilitated by clearing houses.  

![img](https://lh4.googleusercontent.com/nQheJMaa776xYvNt0AOFFPtg3rqSzVXF-1Sf7frxFc0kDlEj6ql0O3GfW_zWeiRAIu_NLqvdN1NVLhnY9-sEA5aaK56ODb3UuB5Tus5bMmL8tWfchHDfvotv16ap8lXiZOQHLpuN)

One of the biggest consumers and producers of healthcare data such as Electronic Health Records and claims are therefore, insurance companies. Data aggregation by insurance corporations is core to their business of risk measurement. They use it to calculate and underwrite financial risk for the policies which they sell.

Actuaries group individuals based on the financial risk the company bears on behalf of them, a process known as classing. They collect structured data on policyholders to fit them into class variables and apply financial coefficients based on their historical data to calculate policy rates. In life insurance actuarial models, dividend rates are also calculated similarly. 

These models allow insurance corporations to measure risk of paying out policies before time. Better models translates into growth and preservation of large capital accounts required by insurance corporations. Increasingly clinical data about patients is being used in these models. These models make predictions about the risk profile of patients. It is useful because insurance corporations can proactively manage patients who might experience chronic problems or might require critical care treatment, and thus incur large expenses for their care. This has incentivized development of methods to recover clinical data from claim files. 

## Data Entry

In the past paper forms were designed by insurance companies and supplied to clinical personnel like nurses and doctors to aggregate information about patients in a structured manner conducive for their needs. Modern day EHR systems with integrated claim management have replaced paperwork, and data has moved from file cabinets to ftp (file transfer protocol) servers. Though the task of data entry in modern day EHR systems continues to be mostly still manual. Products such as Dragon by Nuance are trying to replace data entry with dictation. The goal is to reduce the cognitive workload of medical personnel who have to do the data entry task as well as more importantly take care of patients. 

## Structured data and medical coding systems

Because EHR data is used for insurance claims, medical practitioners carefully encode patient information into coding systems based on their semantic categories. Diagnosis information is encoded using International Classification of Diagnosis (ICD)  version 10. Procedure information is encoded using Current Procedural Terminology (CPT). Packaged drug names are encoded using National Drug Code (NDC), drug names used in pharmacy management are linked to a normalized name using RX Norm, and lab order and result information is encoded using Logical Observation Identifiers Names and Code (LOINC). These coding systems are applied on EHR data such as clinical progress notes to convert it  a structured data format. This allows tabulation of healthcare data which facilitates accurate billing and payment from payers to medical providers after adjudication. 

Often some codes in one coding system overlap in semantic meaning with codes another coding system. This creates a need for crosswalks. The National Library of Medicine, part of the National Institute of Health identified created a Unified Medical Language System (UMLS), which serves like a thesaurus. It lists groups code across the multiple coding systems under one concept identifier. It is a large tabular database available via UMLS Unified Terminology Services as an online browser or downloadable database. 

SNOMED is a unique coding system popular for its comprehensive coverage across multiple semantic categories including but not limited to diagnosis, symptoms and procedures. 

There are crosswalks available for SNOMED to ICD and SNOMED to CPT. These are available in UMLS. 

Crosswalks are also released by other institutions. When healthcare providers that serve medicare patients were asked to upgrade from ICD v9 and comply with ICD v10 by Centres of Medicare and Medicaid Services (CMS) starting October 1, 2015, a crosswalk from ICD v9 to ICD v10 was released by American Academy of Professional Coders (AAPC). 

## File Structure

Here is an example 837 file. The numbered list in the bottom of the image are the service lines.Each of the service lines has a revenue code, which is a medical coding system for categorizing facility charges by hospital department. More information available here http://valuehealthcareservices.com/education/understanding-hospital-revenue-codes/ 

Image taken from <http://www.hipaasuite.com/help/ClaimMaster/HTML/edi-displayed.png>

![img](https://lh6.googleusercontent.com/cJ9plxzOuauyKrkVqMSB5o-CGkYCgosGC_-aGcO3lrZb6aiyasn9-F2rvH6i4lWHyYOV8yDw6Fp1fsNZcr_IyreOTs170detu50mVcu-oR6SZM6ZfPT68dmtpUkxoObYnSxMROmK)

837 files are composed of two parts, a header and a list of service lines. The header contains primary and secondary diagnosis information about the patient encoded using ICD (v9 or v10) for the encounter period of the claim. Fields values required for routing the claim to payer at the clearing house and proper adjudication by the payer are also included in the 837 file. For example, electronic payer codes, filing indicator codes field values present in the file are used for routing claims to payers. The service lines use CPT, LOINC and other codes to itemize the services discharged to the patient during the encounter period, along with billed amount for the corresponding services. A total billed amount for the encounter period by the provider to the payer is also included in the header. 
After adjudication of the claim any adjustments to the amount billed is sent back to provider along with the final contracted network rate payable to the provider by the payer. This is the 835 file also called the remittance file, and it has both header and service lines. Fields which were used for adjudication and therefore, not required in the remittance post adjudication are often dropped from the header. Amount allowed is a term to define the contracted network rate that the payer agrees to pay the provider. If not present amount allowed field value can also be calculated from the total adjustment amount, contract adjustment amount and other fields sometimes available in the remit file.

Both 837 and 835 files have entity tokens referencing the providers involved in the encounter period. Providers are referenced using their National Provider Identifier (NPI) codes.

All providers, institutions as well as individuals are required to register themselves  in the NPPES database. However, once the NPI is assigned, the corresponding entity is not responsible for maintaining accurate information in the database for other fields in the database such as primary speciality for physicians. Some examples of identifier tokens which may be present in an 837 or 835 are Billing NPI, Rendering NPI, Referring NPI, Facility NPI and Payee NPI.  

## FHIR Protocol

In a recent work, “Scalable and accurate deep learning with electronic health records, Alvin Rajkomar et. al (2018)” present a process to restructure healthcare data from electronic health records and clinical progress notes into Fast Healthcare Interoperability Resources (FHIR). They show that applying machine learning workflows to a patient’s healthcare data in FHIR format can improve effectiveness of deep learning models which predict likely diagnosis and treatment outcomes. 

> Our central insight was that rather than explicitly harmonizing EHR data, mapping it into a highly curated set of structured predictors variables and then feeding those variables into a statistical model, we could instead learn to simultaneously harmonize inputs and predict medical events through direct feature learning.     
>
>  https://arxiv.org/ftp/arxiv/papers/1801/1801.07860.pdf

Fast Healthcare Interoperability Resources (abbrev. FHIR) is a data interchange specification. Software systems use the FHIR specification to define data schemas for encoding their data.  

Any data schema constructed as per FHIR specification, has semantically connected fields grouped into entities called resources. Some examples of resource types are Encounter, DiagnosticReport, PaymentNotice, Claim, Patient. These resources have the same field definitions independent of the software system using it to transfer data. Fields in a resource can be nested.  

Further, resources in a FHIR schema are packed together into groups called bundles. The nested nature of a FHIR schema is conducive for JSON or XML serialization, therefore often software systems supporting FHIR protocol use REST APIs to communicate with each other.  FHIR also supports construction of custom resources. The specification is lightly opinionated about how these custom resources have to be defined.  

The FHIR protocol is open and community driven. It is an initiative that can very much accelerate interoperability of software systems in healthcare IT which has always been quite a challenge and continues to be.

## Biomedical and Clinical trials data

There are vast resources of biomedical knowledge which includes pharma development available in journals and articles. A coding system MeSH (Medical Subject Headings) is used for indexing journals, books and articles in life sciences. Clinical trial study records are also indexed with MeSH headings. 

A clinical trial is a research study in which patients are assigned to interventions such as a drug, medical device or procedure and the effect of the intervention is calculated on the health outcomes that are measured. 

NIH’s ClinicalTrials.gov is a database of the research studies that are running or complete. But data is provided on a voluntary basis, so it has compliance issues. Clinical trial data is not submitted on time. This website/database was created as a result of FDA Modernization Act of 1997. Records are available as xml files, and notes are indexed with MeSH headings. These studies require specific composition of patient attributes in their patient sample used for the study. These attributes can be specific about genders, age groups, past medical histories and genetic traits. Recruiting for clinical trials is a cumbersome process. EHR and claims information on a patient which includes ICD codes, CPT codes, RX Norm medication names, NDC codes is used to aid the process of recruiting qualifying patients for a clinical study. Therefore, Pharma companies are big buyers of healthcare data since it can help to discover and filter patient samples for conducting clinical trials.

## Financial and Clinical risk assessment using healthcare data

![img](https://lh6.googleusercontent.com/IXxXPkljItndU_7MNwZJ01zGZWHo0mQBJvhFBwpA11SdMWcBfdwmWKIfstnKWjHM0ZaQcyOQrArSQvUCYDn5qBIAOv7LZY0JA-SvK5kiXnkdQSEUvzaeiO1KQGnHLGDFqm6WTvGe)

Healthcare companies, medical providers, and insurance companies alike leverage healthcare data for health and financial risk assessment of patients populations. The information is used for budgeting of their healthcare spending. 

CPT is developed and maintained by American Medical Association AMA. The CMS Physician Fee Schedule (PFS) is developed by CMS in joint partnership with the AMA. The fee schedule lists CPT codes for physician services, diagnostic services and radiology services and the corresponding amount payable by Medicare to the providers rendering those services. Prices are indexed by Medicare Administrative Contractor (MAC) Localities which is assigned a geographical area containing one or more zip codes. 

The price for a CPT code is calculated from a linear function composed of a base price for rendering the service and multiplicative weights which account for labour and non-labour cost variation by MAC localities. The weights are calculated through a complex process administered by members of the AMA and other CMS assigned administrative bodies which use incurred charges from historical claims data along with expert knowledge about healthcare. I must emphasize the weights and the base amount of a specific CPT code are a result of a very complex process. 

Given Medicare accounts for a large portion of the annual healthcare spending in the United States, corresponding fee schedules of commercial payers are highly influenced by the CMS Physician Fee Schedule. Other Fee Schedules such as the one for Outpatient Prospective Payment System and PFS are primarily Fee for Service payment models.

Clinical decision support rules make use of diagnosis codes to stratify patients into groups which help medical providers to organize and provide better care management services in a timely and effective manner. 

Framingham Risk Score is a gender specific rule to estimate the 10-year cardiovascular risk of an individual using age, gender, tobacco smoker indicator, systolic blood pressure along with HDL and total cholesterol levels. It has been found that thresholds on the scores does not generalize because it can overestimate or underestimate risks consistently for some population types. For example, Framingham Risk Score can overestimate or underestimate risk for hispanic and native american population in US as described in this work, Improving Global Vascular Risk Prediction With Behavioral and Anthropometric Factors: The Multiethnic NOMAS (Northern Manhattan Cohort Study) Ralph L.Sacco MD, MS et. al (2006).

For inpatient encounters, hospitals use Diagnosis Related Groups (DRG) classification system for encounters to assess its clinical severity. Information about the inpatient stay such as affected organ system, surgical procedures performed on patients, morbidity and sex of the patient are used. It accounts for up to eight diagnoses and a primary diagnosis, along with upto six procedures performed during the stay. Network rates are contracted between providers and payers based on these DRG codes. Similar to the CMS Physician Fee Schedule, base amounts and multiplicative weights are used to calculate network rates across multiple DRG codes in order to account for cost variation due to differences in clinical severity of the stay and, geographical cost variation of labour and non-labour charges incurred in providing services during the stay. Healthcare Cost Institute releases reports on historical commercial DRG rates using a database of commercial 835 and 837 files.

Healthcare Cost and Utilization Project (HCUP) develops and maintains many databases containing information about inpatient stays, pediatric inpatient discharges, emergency department visits and readmissions. National Inpatient Sample (NIS) has data on nationwide all-payer inpatient discharges by collecting ICD, CPT, Medicare Severity DRG codes, hospital information, patient demographic and location information along with total charges during the course of the stay.

There are many survey organizations which aggregate data from surveys or de-identified information summarized data available from healthcare providers and insurance companies. HCAHPS (the Hospital Consumer Assessment of Healthcare Providers and Systems) is a patient satisfaction survey developed and maintained by by CMS (the Centers for Medicare and Medicaid Services) for all hospitals in the United States. Leapfrog group collects and shares quality metrics on hospitals.

## Finally

Thanks for reading this far! Hopefully that was a good enough guide to get you started with [wrangling](https://en.wikipedia.org/wiki/Data_wrangling) healthcare data. Please make use of the datasets I have linked below, along with any other datasets that you have at your disposal to explore healthcare data on your own and try to verify my interpretations of it. These datasets are categorized as per the figure I have referenced above from the NEJM catalyst report. If you notice something wrong, confusing or missing, you can write to me at rohtas.space@gmail.com

| Clinical                                                     | Cost                                                         | Claims                                                       | Patient Generated                                           | Pharma                                                       | Patient Preference & Surveys                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [UMLS Browser](https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/) | [Healthcare Cost Institute (HCC)](http://www.healthcostinstitute.org/access-data/accessing-hcci-data-2018/) | [Physician Compare](https://www.medicare.gov/physiciancompare/) (entity data) | [Crowdsourced Fitbit data](https://zenodo.org/record/53894) | [ClinicalTrials](https://www.clinicaltrials.gov/ct2/search)  | [HCUP](https://www.clinicaltrials.gov/ct2/search)            |
| [Wikipedia Disease Pages](https://www.dropbox.com/s/9o4d5jbzrlmmih2/wikipedia_diseases.zip?dl=0) | [Physician Fee Schedule](https://www.cms.gov/apps/physician-fee-schedule/search/search-criteria.aspx) | [Hospital Compare](https://data.medicare.gov/data/hospital-compare) (entity data) |                                                             | [VA Drug Side effects](https://vaww.cmop.med.va.gov/MedSafe_Portal/) | [LeapfrogGroup](https://vaww.cmop.med.va.gov/MedSafe_Portal/) |
|                                                              | [ForwardHealth](https://www.dropbox.com/s/lvlagh95eqzglo7/wisconsin_data.zip?dl=0) (www.forwardhealth.wi.gov) | [NPPES](https://npiregistry.cms.hhs.gov/) (entity data)      |                                                             | [Uptodate Drug Information](https://www.uptodate.com/contents/table-of-contents/drug-information) |                                                              |
|                                                              | [Inpatient Charges](https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/w2du-it53/data) |                                                              |                                                             |                                                              |                                                              |


