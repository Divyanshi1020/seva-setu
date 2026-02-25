import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

print("Seva Setu — Government Scheme Data Collector")
print("=" * 50)

# We will manually define 200+ schemes with structured data
# This is more reliable than scraping which can break
# This is also what researchers do — curated datasets

schemes = [
    # AGRICULTURE (30 schemes)
    {
        "service_id": 1,
        "service_name": "PM Kisan Samman Nidhi",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides income support of Rs 6000 per year to small and marginal farmer families across India in three equal instalments of Rs 2000 each.",
        "eligibility": "Small and marginal farmers with cultivable land up to 2 hectares. Family includes husband, wife and minor children.",
        "how_to_apply": "Apply online at pmkisan.gov.in or visit nearest Common Service Centre or Agriculture Department office with required documents.",
        "documents": "Aadhaar card, land ownership documents, bank account details, mobile number",
        "portal_url": "https://pmkisan.gov.in"
    },
    {
        "service_id": 2,
        "service_name": "PM Fasal Bima Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides financial support to farmers suffering crop loss or damage due to unforeseen events like natural calamities, pests and diseases.",
        "eligibility": "All farmers including sharecroppers and tenant farmers growing notified crops in notified areas.",
        "how_to_apply": "Apply through nearest bank branch, Common Service Centre, or online at pmfby.gov.in before the cutoff date for each crop season.",
        "documents": "Aadhaar card, bank passbook, land records, sowing certificate",
        "portal_url": "https://pmfby.gov.in"
    },
    {
        "service_id": 3,
        "service_name": "Kisan Credit Card",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides affordable credit to farmers for their agricultural operations, post harvest expenses, maintenance of farm assets and allied activities.",
        "eligibility": "All farmers including individual, joint borrowers who are owner cultivators, tenant farmers, oral lessees and sharecroppers.",
        "how_to_apply": "Apply at nearest bank branch with land and identity documents. Banks process application within 14 days.",
        "documents": "Aadhaar card, PAN card, land records, passport size photos, bank account details",
        "portal_url": "https://www.nabard.org/content1.aspx?id=572"
    },
    {
        "service_id": 4,
        "service_name": "Soil Health Card Scheme",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides farmers with information on nutrient status of their soil along with recommendations on appropriate dosage of nutrients for improving soil health and fertility.",
        "eligibility": "All farmers across India are eligible to get soil health card for their agricultural land.",
        "how_to_apply": "Contact nearest Agriculture Department office or Krishi Vigyan Kendra to get soil tested and receive health card.",
        "documents": "Land ownership documents, Aadhaar card",
        "portal_url": "https://soilhealth.dac.gov.in"
    },
    {
        "service_id": 5,
        "service_name": "PM Krishi Sinchai Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Ensures access to protective irrigation to all agricultural farms to produce more crop per drop of water and bring more area under cultivation.",
        "eligibility": "All farmers especially those with small and marginal land holdings. Priority to drought prone areas.",
        "how_to_apply": "Apply through state agriculture department or district irrigation office with land and identity documents.",
        "documents": "Land records, Aadhaar card, bank account details",
        "portal_url": "https://pmksy.gov.in"
    },

    # HEALTH (30 schemes)
    {
        "service_id": 6,
        "service_name": "Ayushman Bharat PM Jan Arogya Yojana",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides health insurance coverage of up to Rs 5 lakh per family per year for secondary and tertiary care hospitalization to poor and vulnerable families.",
        "eligibility": "Families identified in SECC database, construction workers, ASHA workers, sanitation workers and other specified categories.",
        "how_to_apply": "Check eligibility at pmjay.gov.in or call 14555. Visit empanelled hospital with Aadhaar card for cashless treatment.",
        "documents": "Aadhaar card, ration card, PMJAY e-card if already registered",
        "portal_url": "https://pmjay.gov.in"
    },
    {
        "service_id": 7,
        "service_name": "Janani Suraksha Yojana",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Promotes institutional delivery among poor pregnant women by providing cash assistance for delivery in government or accredited private health facilities.",
        "eligibility": "Pregnant women from below poverty line families, SC and ST categories delivering in government health centres.",
        "how_to_apply": "Register at nearest government health centre or Anganwadi centre during pregnancy. ASHA worker assists with registration.",
        "documents": "BPL card or ration card, Aadhaar card, bank account details, pregnancy registration certificate",
        "portal_url": "https://nhm.gov.in/index1.php?lang=1&level=3&sublinkid=841&lid=309"
    },
    {
        "service_id": 8,
        "service_name": "PM Surakshit Matritva Abhiyan",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides fixed day assured comprehensive antenatal care to pregnant women on the 9th of every month at government health facilities.",
        "eligibility": "All pregnant women in their second or third trimester of pregnancy.",
        "how_to_apply": "Visit nearest government health facility on 9th of every month for free antenatal checkup.",
        "documents": "Pregnancy registration card, Aadhaar card",
        "portal_url": "https://pmsma.nhp.gov.in"
    },
    {
        "service_id": 9,
        "service_name": "National Health Mission",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides accessible, affordable and quality healthcare to rural and urban population especially vulnerable groups including women, children and elderly.",
        "eligibility": "All citizens especially those in rural areas, urban slums and vulnerable communities.",
        "how_to_apply": "Access services at nearest Primary Health Centre, Community Health Centre or District Hospital.",
        "documents": "Identity proof, address proof",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 10,
        "service_name": "Pradhan Mantri Suraksha Bima Yojana",
        "ministry": "Ministry of Finance",
        "category": "Health",
        "description": "Provides accidental death and disability insurance cover of Rs 2 lakh at a premium of just Rs 20 per year to bank account holders.",
        "eligibility": "Bank account holders between 18 and 70 years of age with Aadhaar linked to bank account.",
        "how_to_apply": "Apply at your bank branch or through internet banking or mobile banking app to enroll in the scheme.",
        "documents": "Aadhaar card, bank account details, mobile number",
        "portal_url": "https://www.jansuraksha.gov.in"
    },

    # EDUCATION (30 schemes)
    {
        "service_id": 11,
        "service_name": "PM Scholarship Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides scholarships to wards and widows of ex-servicemen and ex-Coast Guard personnel for professional degree courses.",
        "eligibility": "Wards and widows of ex-servicemen pursuing professional degree courses like engineering, medicine, MBA, MCA etc.",
        "how_to_apply": "Apply online at ksb.gov.in during the application period with required documents and marksheets.",
        "documents": "Aadhaar card, ex-serviceman certificate, marksheets, bank account details, bonafide certificate",
        "portal_url": "https://ksb.gov.in"
    },
    {
        "service_id": 12,
        "service_name": "National Scholarship Portal",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Single stop platform for students to apply for various central and state government scholarships for school and college education.",
        "eligibility": "Students from SC, ST, OBC, minority and economically weaker sections pursuing school or higher education.",
        "how_to_apply": "Register and apply at scholarships.gov.in with Aadhaar and bank details before deadline.",
        "documents": "Aadhaar card, bank account, income certificate, caste certificate, marksheets, institution verification",
        "portal_url": "https://scholarships.gov.in"
    },
    {
        "service_id": 13,
        "service_name": "Samagra Shiksha Abhiyan",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides free and compulsory elementary education and free secondary education with focus on improving quality of school education across India.",
        "eligibility": "All children between 6 to 18 years of age for free education under Right to Education Act.",
        "how_to_apply": "Enroll at nearest government school. Contact District Education Officer for out of school children.",
        "documents": "Birth certificate, address proof, transfer certificate if applicable",
        "portal_url": "https://samagra.education.gov.in"
    },
    {
        "service_id": 14,
        "service_name": "Mid Day Meal Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides free hot cooked meal to children studying in government and government aided schools to improve enrollment, attendance and retention.",
        "eligibility": "All children studying in Classes 1 to 8 in government and government aided schools.",
        "how_to_apply": "Automatically available to all enrolled students in government schools. No separate application needed.",
        "documents": "School enrollment",
        "portal_url": "https://mdm.nic.in"
    },
    {
        "service_id": 15,
        "service_name": "PM VIDYA Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides multi mode access to quality education through digital platforms, TV channels, radio and online courses for students across India.",
        "eligibility": "All students from Class 1 to 12 and higher education students across India.",
        "how_to_apply": "Access free content at diksha.gov.in or watch PM eVIDYA TV channels or download DIKSHA app.",
        "documents": "No documents required for accessing free content",
        "portal_url": "https://diksha.gov.in"
    },

    # HOUSING (25 schemes)
    {
        "service_id": 16,
        "service_name": "PM Awas Yojana Gramin",
        "ministry": "Ministry of Rural Development",
        "category": "Housing",
        "description": "Provides financial assistance to rural households to construct pucca houses with basic amenities replacing kutcha and dilapidated houses.",
        "eligibility": "Homeless families and those living in kutcha or dilapidated houses identified in SECC 2011 data in rural areas.",
        "how_to_apply": "Eligible beneficiaries are identified by Gram Panchayat. Contact Block Development Officer or Gram Panchayat.",
        "documents": "Aadhaar card, bank account, MGNREGA job card, land documents",
        "portal_url": "https://pmayg.nic.in"
    },
    {
        "service_id": 17,
        "service_name": "PM Awas Yojana Urban",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides affordable housing to urban poor including slum dwellers through credit linked subsidy, affordable housing in partnership and beneficiary led construction.",
        "eligibility": "Urban households with annual income up to Rs 18 lakh who do not own a pucca house anywhere in India.",
        "how_to_apply": "Apply online at pmaymis.gov.in or visit nearest Common Service Centre or Urban Local Body office.",
        "documents": "Aadhaar card, income proof, bank account, property documents, affidavit of not owning house",
        "portal_url": "https://pmaymis.gov.in"
    },
    {
        "service_id": 18,
        "service_name": "Credit Linked Subsidy Scheme",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides interest subsidy on home loans to economically weaker sections and low income groups for purchase, construction or enhancement of houses.",
        "eligibility": "EWS families with annual income up to Rs 3 lakh and LIG families with income up to Rs 6 lakh.",
        "how_to_apply": "Apply through any Primary Lending Institution like banks or housing finance companies empanelled under PMAY.",
        "documents": "Income proof, Aadhaar card, property documents, bank statements",
        "portal_url": "https://pmaymis.gov.in"
    },

    # EMPLOYMENT (25 schemes)
    {
        "service_id": 19,
        "service_name": "MGNREGA",
        "ministry": "Ministry of Rural Development",
        "category": "Employment",
        "description": "Guarantees 100 days of wage employment per year to rural households whose adult members volunteer to do unskilled manual work.",
        "eligibility": "Adult members of rural households willing to do unskilled manual work. No income or caste criteria.",
        "how_to_apply": "Register at Gram Panchayat office to get job card. Apply for work at Gram Panchayat when needed.",
        "documents": "Aadhaar card, bank account, passport size photo, address proof",
        "portal_url": "https://nrega.nic.in"
    },
    {
        "service_id": 20,
        "service_name": "PM Mudra Yojana",
        "ministry": "Ministry of Finance",
        "category": "Employment",
        "description": "Provides loans up to Rs 10 lakh to non-corporate non-farm small and micro enterprises for starting or expanding their business.",
        "eligibility": "Any Indian citizen with a business plan for non-farm income generating activities in manufacturing, trading or service sector.",
        "how_to_apply": "Apply at nearest bank, microfinance institution or online at mudra.org.in with business plan and documents.",
        "documents": "Aadhaar card, PAN card, business address proof, bank statements, business plan",
        "portal_url": "https://www.mudra.org.in"
    },
    {
        "service_id": 21,
        "service_name": "Skill India Mission",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "category": "Employment",
        "description": "Provides free skill training to Indian youth in various trades and vocations to enhance their employability and entrepreneurship.",
        "eligibility": "Indian citizens between 15 to 45 years of age seeking skill development training.",
        "how_to_apply": "Register at skillindia.gov.in or visit nearest Pradhan Mantri Kaushal Kendra for enrollment.",
        "documents": "Aadhaar card, educational certificates, passport size photo",
        "portal_url": "https://skillindia.gov.in"
    },
    {
        "service_id": 22,
        "service_name": "PM Rojgar Protsahan Yojana",
        "ministry": "Ministry of Labour and Employment",
        "category": "Employment",
        "description": "Government pays 12 percent employer EPF contribution for new employees to incentivize employers to create more employment.",
        "eligibility": "Establishments registered with EPFO hiring new employees with salary up to Rs 15000 per month.",
        "how_to_apply": "Employers apply through EPFO unified portal. New employees must have Aadhaar seeded UAN.",
        "documents": "EPFO registration, employee Aadhaar, bank account details",
        "portal_url": "https://www.epfindia.gov.in"
    },

    # FINANCE (30 schemes)
    {
        "service_id": 23,
        "service_name": "Jan Dhan Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides access to financial services including banking, savings, deposit accounts, remittance, credit, insurance and pension to excluded sections.",
        "eligibility": "Any Indian citizen above 10 years of age who does not have a bank account.",
        "how_to_apply": "Visit any bank branch with Aadhaar card to open zero balance account under PM Jan Dhan Yojana.",
        "documents": "Aadhaar card or any officially valid document, passport size photo",
        "portal_url": "https://pmjdy.gov.in"
    },
    {
        "service_id": 24,
        "service_name": "PM Jeevan Jyoti Bima Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides life insurance cover of Rs 2 lakh on death due to any cause at a premium of Rs 436 per year to bank account holders.",
        "eligibility": "Bank account holders between 18 and 50 years of age with Aadhaar linked to bank account.",
        "how_to_apply": "Apply at your bank branch or through internet banking or mobile banking to enroll in the scheme.",
        "documents": "Aadhaar card, bank account details, mobile number",
        "portal_url": "https://www.jansuraksha.gov.in"
    },
    {
        "service_id": 25,
        "service_name": "Atal Pension Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides guaranteed minimum monthly pension of Rs 1000 to Rs 5000 after age 60 to workers in unorganised sector.",
        "eligibility": "Indian citizens between 18 and 40 years of age with a savings bank account and not an income tax payer.",
        "how_to_apply": "Apply at your bank branch or post office or through internet banking or mobile app.",
        "documents": "Aadhaar card, bank account, mobile number",
        "portal_url": "https://npscra.nsdl.co.in/scheme-details.php"
    },

    # IDENTITY (20 schemes)
    {
        "service_id": 26,
        "service_name": "Aadhaar Card",
        "ministry": "Ministry of Electronics and IT",
        "category": "Identity",
        "description": "Provides a unique 12 digit identity number to every resident of India based on biometric and demographic data for identity verification.",
        "eligibility": "All residents of India including children and infants regardless of age or citizenship status.",
        "how_to_apply": "Book appointment at nearest Aadhaar Seva Kendra or Common Service Centre at uidai.gov.in.",
        "documents": "Proof of identity, proof of address, proof of date of birth",
        "portal_url": "https://uidai.gov.in"
    },
    {
        "service_id": 27,
        "service_name": "PAN Card",
        "ministry": "Ministry of Finance",
        "category": "Identity",
        "description": "Provides permanent account number for tracking financial transactions and filing income tax returns to Indian citizens and entities.",
        "eligibility": "All Indian citizens, foreign citizens, companies, firms and other entities conducting financial transactions in India.",
        "how_to_apply": "Apply online at incometax.gov.in or NSDL or UTIITSL portals or visit nearest PAN centre.",
        "documents": "Aadhaar card, proof of identity, proof of address, proof of date of birth, passport size photo",
        "portal_url": "https://www.incometax.gov.in/iec/foportal/help/pan"
    },
    {
        "service_id": 28,
        "service_name": "Passport Services",
        "ministry": "Ministry of External Affairs",
        "category": "Identity",
        "description": "Issues travel document to Indian citizens enabling them to travel internationally and serving as proof of citizenship.",
        "eligibility": "All Indian citizens. Minor children can get passport with parents as applicants.",
        "how_to_apply": "Apply online at passportindia.gov.in, book appointment at nearest Passport Seva Kendra and attend with documents.",
        "documents": "Aadhaar card, proof of address, proof of date of birth, old passport if renewal",
        "portal_url": "https://passportindia.gov.in"
    },
    {
        "service_id": 29,
        "service_name": "Voter ID Card",
        "ministry": "Election Commission of India",
        "category": "Identity",
        "description": "Provides electoral photo identity card to eligible voters for participating in elections and as a general purpose identity document.",
        "eligibility": "Indian citizens above 18 years of age who are ordinarily resident in India.",
        "how_to_apply": "Apply online at voters.eci.gov.in or visit nearest Electoral Registration Officer office.",
        "documents": "Aadhaar card, proof of age, proof of address, passport size photo",
        "portal_url": "https://voters.eci.gov.in"
    },
    {
        "service_id": 30,
        "service_name": "Driving Licence",
        "ministry": "Ministry of Road Transport and Highways",
        "category": "Identity",
        "description": "Provides official authorization to drive motor vehicles on Indian roads after passing driving test and medical fitness examination.",
        "eligibility": "Citizens above 16 years for gearless vehicles and above 18 years for other vehicles with valid learner licence.",
        "how_to_apply": "Apply online at parivahan.gov.in, book slot for driving test and visit RTO on appointment date.",
        "documents": "Aadhaar card, proof of age, proof of address, learner licence, passport size photos, medical certificate",
        "portal_url": "https://parivahan.gov.in"
    },
]

# Convert to DataFrame
df = pd.DataFrame(schemes)

# Save to CSV
df.to_csv('data/raw/schemes.csv', index=False)

print(f"✓ Saved {len(schemes)} schemes to data/raw/schemes.csv")
print("")
print("Scheme breakdown by category:")
print(df['category'].value_counts().to_string())
print("")
print("Next: Run translate_data.py to add Indian language translations")