import pandas as pd

print("Seva Setu — Expanded Dataset Builder")
print("=" * 50)

schemes = [
    # ═══════════════════════════════════
    # AGRICULTURE (15 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 1,
        "service_name": "PM Kisan Samman Nidhi",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides income support of Rs 6000 per year to small and marginal farmer families across India in three equal instalments of Rs 2000 each.",
        "eligibility": "Small and marginal farmers with cultivable land up to 2 hectares. Family includes husband wife and minor children.",
        "how_to_apply": "Apply online at pmkisan.gov.in or visit nearest Common Service Centre or Agriculture Department office with required documents.",
        "documents": "Aadhaar card, land ownership documents, bank account details, mobile number",
        "portal_url": "https://pmkisan.gov.in"
    },
    {
        "service_id": 2,
        "service_name": "PM Fasal Bima Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides financial support to farmers suffering crop loss or damage due to unforeseen events like natural calamities pests and diseases.",
        "eligibility": "All farmers including sharecroppers and tenant farmers growing notified crops in notified areas.",
        "how_to_apply": "Apply through nearest bank branch Common Service Centre or online at pmfby.gov.in before the cutoff date for each crop season.",
        "documents": "Aadhaar card, bank passbook, land records, sowing certificate",
        "portal_url": "https://pmfby.gov.in"
    },
    {
        "service_id": 3,
        "service_name": "Kisan Credit Card",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides affordable credit to farmers for agricultural operations post harvest expenses maintenance of farm assets and allied activities.",
        "eligibility": "All farmers including individual joint borrowers who are owner cultivators tenant farmers oral lessees and sharecroppers.",
        "how_to_apply": "Apply at nearest bank branch with land and identity documents. Banks process application within 14 days.",
        "documents": "Aadhaar card, PAN card, land records, passport size photos, bank account details",
        "portal_url": "https://www.nabard.org"
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
    {
        "service_id": 6,
        "service_name": "National Agriculture Market eNAM",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Online trading platform for agricultural commodities connecting farmers traders and buyers across India for better price discovery.",
        "eligibility": "All farmers traders and buyers of agricultural produce registered with their local APMC mandi.",
        "how_to_apply": "Register at enam.gov.in or visit nearest APMC mandi for registration with Aadhaar and bank details.",
        "documents": "Aadhaar card, bank account details, APMC registration",
        "portal_url": "https://enam.gov.in"
    },
    {
        "service_id": 7,
        "service_name": "PM Kisan Maandhan Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides pension of Rs 3000 per month to small and marginal farmers after attaining age of 60 years for old age security.",
        "eligibility": "Small and marginal farmers between 18 to 40 years of age with cultivable land up to 2 hectares.",
        "how_to_apply": "Enroll at nearest Common Service Centre with Aadhaar card and bank passbook.",
        "documents": "Aadhaar card, bank passbook, land records",
        "portal_url": "https://maandhan.in"
    },
    {
        "service_id": 8,
        "service_name": "Paramparagat Krishi Vikas Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Promotes organic farming through cluster approach by providing financial assistance to farmers for adopting organic farming practices.",
        "eligibility": "Farmers willing to adopt organic farming practices in clusters of 50 acres minimum.",
        "how_to_apply": "Contact District Agriculture Officer to form farmer clusters and apply for organic farming certification and assistance.",
        "documents": "Land records, Aadhaar card, farmer group registration",
        "portal_url": "https://pgsindia-ncof.gov.in"
    },
    {
        "service_id": 9,
        "service_name": "Pradhan Mantri Annadata Aay SanraksHan Abhiyan",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Ensures farmers get remunerative prices for their produce through price support scheme procurement and price deficiency payment.",
        "eligibility": "All farmers growing notified oilseeds pulses and copra in states implementing the scheme.",
        "how_to_apply": "Register on state agriculture department portal before sowing season with land and bank details.",
        "documents": "Land records, Aadhaar card, bank account, sowing declaration",
        "portal_url": "https://agricoop.nic.in"
    },
    {
        "service_id": 10,
        "service_name": "Micro Irrigation Fund",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides subsidized drip and sprinkler irrigation systems to farmers to improve water use efficiency and increase crop productivity.",
        "eligibility": "All categories of farmers especially small and marginal farmers wanting to adopt micro irrigation.",
        "how_to_apply": "Apply through state horticulture or agriculture department with land documents and irrigation plan.",
        "documents": "Land records, Aadhaar card, bank account, irrigation plan",
        "portal_url": "https://pmksy.gov.in"
    },
    {
        "service_id": 11,
        "service_name": "Rashtriya Krishi Vikas Yojana",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides financial assistance to states for strengthening agricultural infrastructure and increasing agricultural productivity through need based projects.",
        "eligibility": "Farmers and agricultural institutions in states submitting approved project proposals.",
        "how_to_apply": "Apply through state agriculture department for project based assistance under RKVY scheme.",
        "documents": "Project proposal, land documents, Aadhaar card",
        "portal_url": "https://rkvy.nic.in"
    },
    {
        "service_id": 12,
        "service_name": "Agriculture Infrastructure Fund",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides medium to long term debt financing for investment in viable projects for post harvest management and community farming assets.",
        "eligibility": "Farmers FPOs PACS agri entrepreneurs and startups for post harvest management infrastructure projects.",
        "how_to_apply": "Apply online at agriinfra.dac.gov.in with project proposal and financial documents.",
        "documents": "Project proposal, financial statements, Aadhaar card, PAN card, bank account",
        "portal_url": "https://agriinfra.dac.gov.in"
    },
    {
        "service_id": 13,
        "service_name": "PM Formalisation of Micro Food Processing Enterprises",
        "ministry": "Ministry of Food Processing Industries",
        "category": "Agriculture",
        "description": "Provides financial technical and business support to existing micro food processing enterprises to enhance their competitiveness.",
        "eligibility": "Existing micro food processing units individual farmers FPOs and self help groups in food processing.",
        "how_to_apply": "Apply online at pmfme.mofpi.gov.in with business details and project proposal.",
        "documents": "Business registration, Aadhaar card, bank account, project report",
        "portal_url": "https://pmfme.mofpi.gov.in"
    },
    {
        "service_id": 14,
        "service_name": "Beekeeping Development Committee",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "description": "Provides training financial assistance and equipment support to farmers for adopting beekeeping as supplementary income activity.",
        "eligibility": "Any farmer or rural youth interested in beekeeping as livelihood activity.",
        "how_to_apply": "Contact nearest Krishi Vigyan Kendra or District Horticulture Officer for training and financial assistance.",
        "documents": "Aadhaar card, bank account, land records",
        "portal_url": "https://nbb.gov.in"
    },
    {
        "service_id": 15,
        "service_name": "Pradhan Mantri Matsya Sampada Yojana",
        "ministry": "Ministry of Fisheries Animal Husbandry and Dairying",
        "category": "Agriculture",
        "description": "Provides financial assistance for development of fisheries sector infrastructure fish production and fishermen welfare.",
        "eligibility": "Fishermen fish farmers fish workers and fish vendors engaged in fisheries and aquaculture activities.",
        "how_to_apply": "Apply through state fisheries department with project proposal and identity documents.",
        "documents": "Aadhaar card, bank account, fishing license, project proposal",
        "portal_url": "https://pmmsy.dof.gov.in"
    },

    # ═══════════════════════════════════
    # HEALTH (15 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 16,
        "service_name": "Ayushman Bharat PM Jan Arogya Yojana",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides health insurance coverage of up to Rs 5 lakh per family per year for secondary and tertiary care hospitalization to poor and vulnerable families.",
        "eligibility": "Families identified in SECC database construction workers ASHA workers sanitation workers and other specified categories.",
        "how_to_apply": "Check eligibility at pmjay.gov.in or call 14555. Visit empanelled hospital with Aadhaar card for cashless treatment.",
        "documents": "Aadhaar card, ration card, PMJAY e-card if already registered",
        "portal_url": "https://pmjay.gov.in"
    },
    {
        "service_id": 17,
        "service_name": "Janani Suraksha Yojana",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Promotes institutional delivery among poor pregnant women by providing cash assistance for delivery in government or accredited private health facilities.",
        "eligibility": "Pregnant women from below poverty line families SC and ST categories delivering in government health centres.",
        "how_to_apply": "Register at nearest government health centre or Anganwadi centre during pregnancy. ASHA worker assists with registration.",
        "documents": "BPL card or ration card, Aadhaar card, bank account details, pregnancy registration certificate",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 18,
        "service_name": "Pradhan Mantri Surakshit Matritva Abhiyan",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides fixed day assured comprehensive antenatal care to pregnant women on the 9th of every month at government health facilities.",
        "eligibility": "All pregnant women in their second or third trimester of pregnancy.",
        "how_to_apply": "Visit nearest government health facility on 9th of every month for free antenatal checkup.",
        "documents": "Pregnancy registration card, Aadhaar card",
        "portal_url": "https://pmsma.nhp.gov.in"
    },
    {
        "service_id": 19,
        "service_name": "Pradhan Mantri Suraksha Bima Yojana",
        "ministry": "Ministry of Finance",
        "category": "Health",
        "description": "Provides accidental death and disability insurance cover of Rs 2 lakh at a premium of just Rs 20 per year to bank account holders.",
        "eligibility": "Bank account holders between 18 and 70 years of age with Aadhaar linked to bank account.",
        "how_to_apply": "Apply at your bank branch or through internet banking or mobile banking app to enroll in the scheme.",
        "documents": "Aadhaar card, bank account details, mobile number",
        "portal_url": "https://www.jansuraksha.gov.in"
    },
    {
        "service_id": 20,
        "service_name": "National Health Mission",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides accessible affordable and quality healthcare to rural and urban population especially vulnerable groups including women children and elderly.",
        "eligibility": "All citizens especially those in rural areas urban slums and vulnerable communities.",
        "how_to_apply": "Access services at nearest Primary Health Centre Community Health Centre or District Hospital.",
        "documents": "Identity proof, address proof",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 21,
        "service_name": "Rashtriya Bal Swasthya Karyakram",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides health screening and early intervention services for children from birth to 18 years for 4Ds — defects at birth diseases deficiencies and developmental delays.",
        "eligibility": "All children from birth to 18 years studying in government and government aided schools and anganwadi centres.",
        "how_to_apply": "Automatic screening through mobile health teams visiting schools and anganwadi centres. No separate application needed.",
        "documents": "Birth certificate, school enrollment",
        "portal_url": "https://nhm.gov.in/index1.php?lang=1&level=2&sublinkid=1228&lid=655"
    },
    {
        "service_id": 22,
        "service_name": "Pradhan Mantri National Dialysis Programme",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides free dialysis services to poor patients suffering from kidney failure at district hospitals across India.",
        "eligibility": "BPL patients suffering from chronic kidney disease requiring regular dialysis.",
        "how_to_apply": "Visit nearest district hospital with BPL card and medical prescription for kidney failure diagnosis.",
        "documents": "BPL card, Aadhaar card, medical reports confirming kidney failure",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 23,
        "service_name": "National Mental Health Programme",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides free mental health services including counselling therapy and medicines at government hospitals and community health centres.",
        "eligibility": "All citizens requiring mental health services. Priority to economically weaker sections.",
        "how_to_apply": "Visit nearest government hospital or community health centre for free mental health consultation and treatment.",
        "documents": "Identity proof, address proof",
        "portal_url": "https://nhp.gov.in/Mental-Health_pg"
    },
    {
        "service_id": 24,
        "service_name": "Ayushman Bharat Health and Wellness Centres",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides comprehensive primary healthcare services including maternal child health non communicable diseases and free essential medicines at upgraded sub centres.",
        "eligibility": "All citizens especially in rural and remote areas.",
        "how_to_apply": "Visit nearest Ayushman Bharat Health and Wellness Centre for free primary healthcare services.",
        "documents": "Aadhaar card or any identity proof",
        "portal_url": "https://ab-hwc.nhp.gov.in"
    },
    {
        "service_id": 25,
        "service_name": "Intensified Mission Indradhanush",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides free vaccination to children up to 2 years and pregnant women against 12 vaccine preventable diseases.",
        "eligibility": "All children up to 2 years of age and pregnant women across India.",
        "how_to_apply": "Visit nearest government health centre or Anganwadi centre on vaccination day. ASHA worker informs about schedule.",
        "documents": "Birth certificate for child, Aadhaar card",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 26,
        "service_name": "Poshan Abhiyaan",
        "ministry": "Ministry of Women and Child Development",
        "category": "Health",
        "description": "Aims to reduce malnutrition among children pregnant women and lactating mothers through improved nutrition practices and services.",
        "eligibility": "Children under 6 years pregnant women and lactating mothers especially in high burden districts.",
        "how_to_apply": "Register at nearest Anganwadi centre. ASHA and AWW workers provide nutrition counselling and supplementary nutrition.",
        "documents": "Aadhaar card, birth certificate for children",
        "portal_url": "https://poshanabhiyaan.gov.in"
    },
    {
        "service_id": 27,
        "service_name": "Janani Shishu Suraksha Karyakram",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides completely free maternity services including normal deliveries caesarean operations and treatment of sick newborns at government health institutions.",
        "eligibility": "All pregnant women and sick newborns up to 30 days of age seeking treatment at government health facilities.",
        "how_to_apply": "Visit any government hospital or health centre for free delivery and newborn care services.",
        "documents": "Aadhaar card, any identity proof",
        "portal_url": "https://nhm.gov.in"
    },
    {
        "service_id": 28,
        "service_name": "National Programme for Control of Blindness",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides free cataract operations spectacles and treatment for eye diseases at government hospitals to reduce avoidable blindness.",
        "eligibility": "All citizens requiring eye care with priority to economically weaker sections and elderly population.",
        "how_to_apply": "Visit nearest government hospital district hospital or eye camp organised by health department for free treatment.",
        "documents": "Aadhaar card, BPL card if applicable",
        "portal_url": "https://npcbvi.gov.in"
    },
    {
        "service_id": 29,
        "service_name": "Nikshay Poshan Yojana",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Provides nutritional support of Rs 500 per month to all tuberculosis patients during their treatment period.",
        "eligibility": "All notified tuberculosis patients undergoing treatment under Revised National TB Control Programme.",
        "how_to_apply": "Automatic enrollment when registered for TB treatment at government health facility. Bank account required for direct benefit transfer.",
        "documents": "Aadhaar card, bank account details, TB registration certificate",
        "portal_url": "https://nikshay.in"
    },
    {
        "service_id": 30,
        "service_name": "PM Ayushman Bharat Health Infrastructure Mission",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "description": "Strengthens health infrastructure at primary secondary and tertiary levels including critical care facilities and disease surveillance network.",
        "eligibility": "All citizens benefit through improved healthcare infrastructure at government hospitals.",
        "how_to_apply": "Access improved healthcare services at government health facilities under this mission.",
        "documents": "Aadhaar card or any identity proof",
        "portal_url": "https://nhm.gov.in"
    },

    # ═══════════════════════════════════
    # EDUCATION (15 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 31,
        "service_name": "National Scholarship Portal",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Single stop platform for students to apply for various central and state government scholarships for school and college education.",
        "eligibility": "Students from SC ST OBC minority and economically weaker sections pursuing school or higher education.",
        "how_to_apply": "Register and apply at scholarships.gov.in with Aadhaar and bank details before deadline.",
        "documents": "Aadhaar card, bank account, income certificate, caste certificate, marksheets, institution verification",
        "portal_url": "https://scholarships.gov.in"
    },
    {
        "service_id": 32,
        "service_name": "PM Scholarship Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides scholarships to wards and widows of ex-servicemen and ex-Coast Guard personnel for professional degree courses.",
        "eligibility": "Wards and widows of ex-servicemen pursuing professional degree courses like engineering medicine MBA MCA.",
        "how_to_apply": "Apply online at ksb.gov.in during the application period with required documents and marksheets.",
        "documents": "Aadhaar card, ex-serviceman certificate, marksheets, bank account details, bonafide certificate",
        "portal_url": "https://ksb.gov.in"
    },
    {
        "service_id": 33,
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
        "service_id": 34,
        "service_name": "Mid Day Meal Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides free hot cooked meal to children studying in government and government aided schools to improve enrollment attendance and retention.",
        "eligibility": "All children studying in Classes 1 to 8 in government and government aided schools.",
        "how_to_apply": "Automatically available to all enrolled students in government schools. No separate application needed.",
        "documents": "School enrollment",
        "portal_url": "https://mdm.nic.in"
    },
    {
        "service_id": 35,
        "service_name": "PM VIDYA Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides multi mode access to quality education through digital platforms TV channels radio and online courses for students across India.",
        "eligibility": "All students from Class 1 to 12 and higher education students across India.",
        "how_to_apply": "Access free content at diksha.gov.in or watch PM eVIDYA TV channels or download DIKSHA app.",
        "documents": "No documents required for accessing free content",
        "portal_url": "https://diksha.gov.in"
    },
    {
        "service_id": 36,
        "service_name": "National Means cum Merit Scholarship",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides scholarships of Rs 12000 per year to meritorious students of economically weaker sections to arrest their dropout at Class 8 and encourage them to continue education.",
        "eligibility": "Students who passed Class 8 examination with 55 percent marks from government schools with family income below Rs 3.5 lakh.",
        "how_to_apply": "Apply through state education department after passing NMMS examination conducted by state governments.",
        "documents": "Mark sheets, income certificate, bank account, Aadhaar card, caste certificate if applicable",
        "portal_url": "https://scholarships.gov.in"
    },
    {
        "service_id": 37,
        "service_name": "Higher Education Loan Subsidy Scheme",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides interest subsidy on education loans for technical and professional courses to students from economically weaker sections during moratorium period.",
        "eligibility": "Students with family income below Rs 4.5 lakh per annum pursuing technical or professional courses with education loan.",
        "how_to_apply": "Apply through Canara Bank nodal agency with education loan documents and income certificate.",
        "documents": "Education loan sanction letter, income certificate, Aadhaar card, admission letter",
        "portal_url": "https://www.canbankmf.com"
    },
    {
        "service_id": 38,
        "service_name": "Kendriya Vidyalaya Admission",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides quality education in Kendriya Vidyalayas to children of central government employees transferable government servants and defence personnel.",
        "eligibility": "Children of central government employees transferable employees defence and paramilitary personnel.",
        "how_to_apply": "Apply online at kvsangathan.nic.in during admission season. Offline application at nearest KV also accepted.",
        "documents": "Service certificate of parent, birth certificate, address proof, Aadhaar card",
        "portal_url": "https://kvsangathan.nic.in"
    },
    {
        "service_id": 39,
        "service_name": "Navodaya Vidyalaya Admission",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides free quality residential education to talented rural children at Jawahar Navodaya Vidyalayas from Class 6 to 12.",
        "eligibility": "Rural children studying in Class 5 for Class 6 admission. 75 percent seats reserved for rural area students.",
        "how_to_apply": "Apply online at navodaya.gov.in for JNVST selection test. Free of cost admission for selected students.",
        "documents": "Birth certificate, Class 5 school certificate, rural area certificate, Aadhaar card",
        "portal_url": "https://navodaya.gov.in"
    },
    {
        "service_id": 40,
        "service_name": "Beti Bachao Beti Padhao",
        "ministry": "Ministry of Women and Child Development",
        "category": "Education",
        "description": "Promotes education of girl children and prevents gender biased sex selective elimination through awareness and educational support.",
        "eligibility": "Girl children especially in districts with low child sex ratio. All families with girl children.",
        "how_to_apply": "Enroll girl child in nearby school. Access Sukanya Samriddhi Yojana at post office or bank for savings.",
        "documents": "Birth certificate of girl child, Aadhaar card, address proof",
        "portal_url": "https://wcd.nic.in/bbbp-schemes"
    },
    {
        "service_id": 41,
        "service_name": "Post Matric Scholarship for SC Students",
        "ministry": "Ministry of Social Justice and Empowerment",
        "category": "Education",
        "description": "Provides financial assistance to SC students pursuing post matriculation or post secondary education to enable them to complete their education.",
        "eligibility": "SC students studying at post matriculation level with family income below Rs 2.5 lakh per annum.",
        "how_to_apply": "Apply at scholarships.gov.in or through state social welfare department before deadline each year.",
        "documents": "Caste certificate, income certificate, Aadhaar card, bank account, marksheets, institution certificate",
        "portal_url": "https://scholarships.gov.in"
    },
    {
        "service_id": 42,
        "service_name": "National Fellowship for SC Students",
        "ministry": "Ministry of Social Justice and Empowerment",
        "category": "Education",
        "description": "Provides fellowship to SC students pursuing MPhil and PhD programmes in universities and institutions recognized by UGC.",
        "eligibility": "SC students admitted to regular full time MPhil or PhD programme in UGC recognized universities.",
        "how_to_apply": "Apply through UGC online portal during notification period with admission letter and caste certificate.",
        "documents": "Caste certificate, admission letter, Aadhaar card, bank account, UGC NET scorecard if applicable",
        "portal_url": "https://ugc.ac.in"
    },
    {
        "service_id": 43,
        "service_name": "Pradhan Mantri Innovative Learning Programme DHRUV",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Identifies and nurtures talented students in science and performing arts through mentorship by eminent personalities.",
        "eligibility": "Talented students from Class 9 to 12 selected through state level screening process.",
        "how_to_apply": "Schools nominate students to state education departments for screening and selection to the programme.",
        "documents": "School nomination, marksheets, identity proof",
        "portal_url": "https://ncert.nic.in"
    },
    {
        "service_id": 44,
        "service_name": "Eklavya Model Residential Schools",
        "ministry": "Ministry of Tribal Affairs",
        "category": "Education",
        "description": "Provides quality residential education to ST students in remote tribal areas from Class 6 to 12 with focus on preserving tribal culture.",
        "eligibility": "ST students in remote tribal areas. Admission through entrance examination conducted by state tribal departments.",
        "how_to_apply": "Apply through district tribal welfare office for entrance examination. Admission based on merit.",
        "documents": "ST certificate, birth certificate, school marksheets, Aadhaar card",
        "portal_url": "https://tribal.nic.in"
    },
    {
        "service_id": 45,
        "service_name": "Ishan Uday Special Scholarship for North East",
        "ministry": "Ministry of Education",
        "category": "Education",
        "description": "Provides scholarships to students from North Eastern states pursuing general degree technical and medical education to increase gross enrollment ratio.",
        "eligibility": "Students domiciled in North Eastern states pursuing undergraduate courses with family income below Rs 4.5 lakh.",
        "how_to_apply": "Apply at scholarships.gov.in during notification period with domicile and income certificates.",
        "documents": "Domicile certificate, income certificate, Aadhaar card, bank account, marksheets",
        "portal_url": "https://scholarships.gov.in"
    },

    # ═══════════════════════════════════
    # EMPLOYMENT (15 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 46,
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
        "service_id": 47,
        "service_name": "PM Mudra Yojana",
        "ministry": "Ministry of Finance",
        "category": "Employment",
        "description": "Provides loans up to Rs 10 lakh to non corporate non farm small and micro enterprises for starting or expanding their business.",
        "eligibility": "Any Indian citizen with a business plan for non farm income generating activities in manufacturing trading or service sector.",
        "how_to_apply": "Apply at nearest bank microfinance institution or online at mudra.org.in with business plan and documents.",
        "documents": "Aadhaar card, PAN card, business address proof, bank statements, business plan",
        "portal_url": "https://www.mudra.org.in"
    },
    {
        "service_id": 48,
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
        "service_id": 49,
        "service_name": "PM Rojgar Protsahan Yojana",
        "ministry": "Ministry of Labour and Employment",
        "category": "Employment",
        "description": "Government pays 12 percent employer EPF contribution for new employees to incentivize employers to create more employment.",
        "eligibility": "Establishments registered with EPFO hiring new employees with salary up to Rs 15000 per month.",
        "how_to_apply": "Employers apply through EPFO unified portal. New employees must have Aadhaar seeded UAN.",
        "documents": "EPFO registration, employee Aadhaar, bank account details",
        "portal_url": "https://www.epfindia.gov.in"
    },
    {
        "service_id": 50,
        "service_name": "Deen Dayal Upadhyaya Grameen Kaushalya Yojana",
        "ministry": "Ministry of Rural Development",
        "category": "Employment",
        "description": "Provides placement linked skill training to rural youth from poor families to enable them to access regular salaried employment.",
        "eligibility": "Rural youth between 15 and 35 years from poor families. Age relaxation up to 45 years for SC ST women and PwD.",
        "how_to_apply": "Contact nearest DDU-GKY training partner or visit kaushal.nic.in for registration and training details.",
        "documents": "Aadhaar card, income certificate, educational certificates, bank account",
        "portal_url": "https://ddugky.gov.in"
    },
    {
        "service_id": 51,
        "service_name": "National Career Service Portal",
        "ministry": "Ministry of Labour and Employment",
        "category": "Employment",
        "description": "Provides online job matching placement services career counselling and vocational guidance to job seekers across India.",
        "eligibility": "All job seekers including freshers experienced professionals and differently abled persons.",
        "how_to_apply": "Register at ncs.gov.in with educational and work experience details to access job listings and career services.",
        "documents": "Aadhaar card, educational certificates, experience certificates if any",
        "portal_url": "https://www.ncs.gov.in"
    },
    {
        "service_id": 52,
        "service_name": "Startup India",
        "ministry": "Ministry of Commerce and Industry",
        "category": "Employment",
        "description": "Provides tax benefits funding support mentorship and simplified regulations to startups to promote entrepreneurship and job creation.",
        "eligibility": "Entities incorporated as private limited company partnership or LLP less than 10 years old with annual turnover below Rs 100 crore.",
        "how_to_apply": "Apply for DPIIT recognition at startupindia.gov.in with incorporation certificate and business details.",
        "documents": "Incorporation certificate, PAN card, business description, innovation certificate",
        "portal_url": "https://www.startupindia.gov.in"
    },
    {
        "service_id": 53,
        "service_name": "Stand Up India",
        "ministry": "Ministry of Finance",
        "category": "Employment",
        "description": "Provides bank loans between Rs 10 lakh and Rs 1 crore to SC ST and women entrepreneurs for setting up greenfield enterprises.",
        "eligibility": "SC ST and women entrepreneurs above 18 years for greenfield projects in manufacturing services or trading sector.",
        "how_to_apply": "Apply at standupmitra.in or visit nearest bank branch with business plan and eligibility documents.",
        "documents": "Aadhaar card, caste certificate if SC ST, business plan, project report, bank statements",
        "portal_url": "https://www.standupmitra.in"
    },
    {
        "service_id": 54,
        "service_name": "PM SVANidhi Scheme",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Employment",
        "description": "Provides affordable working capital loans to street vendors to resume their livelihoods affected by COVID-19 lockdowns.",
        "eligibility": "Street vendors vending in urban areas with certificate of vending or letter of recommendation from ULB.",
        "how_to_apply": "Apply at pmsvanidhi.mohua.gov.in or through nearest bank or MFI with vending certificate.",
        "documents": "Vending certificate or letter of recommendation, Aadhaar card, bank account",
        "portal_url": "https://pmsvanidhi.mohua.gov.in"
    },
    {
        "service_id": 55,
        "service_name": "Pradhan Mantri Kaushal Vikas Yojana",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "category": "Employment",
        "description": "Provides free short term skill training and certification to Indian youth to enhance their employability in various industry sectors.",
        "eligibility": "Indian nationals between 15 to 45 years who have dropped out of school or college or are looking for better employment.",
        "how_to_apply": "Register at pmkvyofficial.org or visit nearest PMKVY training centre for enrollment in relevant skill course.",
        "documents": "Aadhaar card, educational certificates, bank account for stipend",
        "portal_url": "https://pmkvyofficial.org"
    },
    {
        "service_id": 56,
        "service_name": "Mahatma Gandhi National Fellowship",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "category": "Employment",
        "description": "Provides two year fellowship to young graduates to work with district administration on skill development and economic development.",
        "eligibility": "Young graduates below 30 years with strong academic record interested in public policy and development work.",
        "how_to_apply": "Apply through IIM partner institutions during fellowship notification period with academic documents.",
        "documents": "Graduation certificate, marksheets, Aadhaar card, statement of purpose",
        "portal_url": "https://msde.gov.in"
    },
    {
        "service_id": 57,
        "service_name": "National Apprenticeship Promotion Scheme",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "category": "Employment",
        "description": "Promotes apprenticeship training by providing financial support to employers and stipend to apprentices for on the job skill training.",
        "eligibility": "Youth who have passed Class 5 or above seeking practical skill training with employers.",
        "how_to_apply": "Register at apprenticeshipindia.org and find employers offering apprenticeship in your trade.",
        "documents": "Educational certificates, Aadhaar card, bank account",
        "portal_url": "https://apprenticeshipindia.org"
    },
    {
        "service_id": 58,
        "service_name": "Deendayal Antyodaya Yojana National Urban Livelihoods Mission",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Employment",
        "description": "Provides skill training self employment and social mobilization support to urban poor to reduce poverty and vulnerability.",
        "eligibility": "Urban poor especially women homeless persons rag pickers street children and differently abled persons.",
        "how_to_apply": "Contact nearest Urban Local Body or city livelihood centre for enrollment in skill training and self help group.",
        "documents": "Aadhaar card, address proof, income proof",
        "portal_url": "https://nulm.gov.in"
    },
    {
        "service_id": 59,
        "service_name": "PM Vishwakarma Scheme",
        "ministry": "Ministry of Micro Small and Medium Enterprises",
        "category": "Employment",
        "description": "Provides recognition training toolkit and collateral free credit support to traditional artisans and craftsmen working with hands and tools.",
        "eligibility": "Artisans and craftsmen in 18 traditional trades including carpenter blacksmith goldsmith potter tailor etc.",
        "how_to_apply": "Apply at pmvishwakarma.gov.in through Common Service Centre with trade details and Aadhaar.",
        "documents": "Aadhaar card, bank account, trade skill proof, mobile number",
        "portal_url": "https://pmvishwakarma.gov.in"
    },
    {
        "service_id": 60,
        "service_name": "Atmanirbhar Bharat Rozgar Yojana",
        "ministry": "Ministry of Labour and Employment",
        "category": "Employment",
        "description": "Incentivizes employers to create new employment by subsidizing EPF contributions for new employees hired during COVID recovery period.",
        "eligibility": "Establishments registered with EPFO hiring new employees with monthly wages below Rs 15000.",
        "how_to_apply": "Employers register new employees on EPFO unified portal to avail government contribution benefit automatically.",
        "documents": "EPFO registration, new employee Aadhaar, salary details",
        "portal_url": "https://www.epfindia.gov.in"
    },

    # ═══════════════════════════════════
    # FINANCE (15 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 61,
        "service_name": "Jan Dhan Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides access to financial services including banking savings deposit accounts remittance credit insurance and pension to excluded sections.",
        "eligibility": "Any Indian citizen above 10 years of age who does not have a bank account.",
        "how_to_apply": "Visit any bank branch with Aadhaar card to open zero balance account under PM Jan Dhan Yojana.",
        "documents": "Aadhaar card or any officially valid document, passport size photo",
        "portal_url": "https://pmjdy.gov.in"
    },
    {
        "service_id": 62,
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
        "service_id": 63,
        "service_name": "Atal Pension Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides guaranteed minimum monthly pension of Rs 1000 to Rs 5000 after age 60 to workers in unorganised sector.",
        "eligibility": "Indian citizens between 18 and 40 years of age with a savings bank account and not an income tax payer.",
        "how_to_apply": "Apply at your bank branch or post office or through internet banking or mobile app.",
        "documents": "Aadhaar card, bank account, mobile number",
        "portal_url": "https://npscra.nsdl.co.in"
    },
    {
        "service_id": 64,
        "service_name": "PM Vaya Vandana Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides assured pension income to senior citizens above 60 years at guaranteed rate of return through LIC of India.",
        "eligibility": "Senior citizens above 60 years of age. No upper age limit. Investment limit Rs 15 lakh per senior citizen.",
        "how_to_apply": "Apply at nearest LIC branch or online at licindia.in with age proof and investment amount.",
        "documents": "Age proof, Aadhaar card, PAN card, bank account details, passport size photo",
        "portal_url": "https://licindia.in"
    },
    {
        "service_id": 65,
        "service_name": "Sukanya Samriddhi Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides high interest savings scheme for girl children to meet expenses of higher education and marriage with tax benefits.",
        "eligibility": "Girl child below 10 years of age. Account opened by parent or legal guardian. One account per girl child maximum two accounts per family.",
        "how_to_apply": "Open account at nearest post office or authorized bank with girl child birth certificate and guardian Aadhaar.",
        "documents": "Girl child birth certificate, guardian Aadhaar card, guardian PAN card, address proof",
        "portal_url": "https://www.indiapost.gov.in"
    },
    {
        "service_id": 66,
        "service_name": "Kisan Vikas Patra",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides fixed return savings certificate that doubles the investment in a fixed period available at post offices and banks.",
        "eligibility": "Any Indian citizen above 18 years. Minor accounts can be opened by guardian. No maximum investment limit.",
        "how_to_apply": "Purchase at nearest post office or designated bank with KYC documents and investment amount.",
        "documents": "Aadhaar card, PAN card for investments above Rs 50000, address proof",
        "portal_url": "https://www.indiapost.gov.in"
    },
    {
        "service_id": 67,
        "service_name": "National Savings Certificate",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides tax saving fixed income investment with guaranteed returns for 5 years available at post offices across India.",
        "eligibility": "Any Indian citizen above 18 years. Joint accounts allowed. No maximum investment limit.",
        "how_to_apply": "Purchase at nearest post office with KYC documents and investment amount. Available in denominations of Rs 100 and above.",
        "documents": "Aadhaar card, PAN card for investments above Rs 50000, address proof, passport size photo",
        "portal_url": "https://www.indiapost.gov.in"
    },
    {
        "service_id": 68,
        "service_name": "PM Jan Dhan Overdraft Facility",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides overdraft facility up to Rs 10000 to Jan Dhan account holders for emergency credit needs without any collateral.",
        "eligibility": "Jan Dhan account holders who have operated their account satisfactorily for 6 months. Preference to women account holders.",
        "how_to_apply": "Apply at your bank branch where Jan Dhan account is maintained with satisfactory account operation proof.",
        "documents": "Jan Dhan account details, Aadhaar card, 6 months account statement",
        "portal_url": "https://pmjdy.gov.in"
    },
    {
        "service_id": 69,
        "service_name": "Credit Guarantee Fund Trust for Micro and Small Enterprises",
        "ministry": "Ministry of MSME",
        "category": "Finance",
        "description": "Provides collateral free credit guarantee for loans to micro and small enterprises enabling them to access formal credit.",
        "eligibility": "Micro and small enterprises seeking loans up to Rs 2 crore from eligible lending institutions.",
        "how_to_apply": "Apply for business loan at any CGTMSE member lending institution. Guarantee is automatically provided by bank.",
        "documents": "Business registration, Aadhaar card, PAN card, business plan, financial statements",
        "portal_url": "https://www.cgtmse.in"
    },
    {
        "service_id": 70,
        "service_name": "PM Street Vendor AtmaNirbhar Nidhi",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Finance",
        "description": "Provides collateral free working capital loans to street vendors at subsidized interest rate with incentive for digital transactions.",
        "eligibility": "Street vendors vending in urban areas on or before March 24 2020 with vending certificate from Urban Local Body.",
        "how_to_apply": "Apply at pmsvanidhi.mohua.gov.in or through bank MFI or MicroFinance with vending certificate and Aadhaar.",
        "documents": "Vending certificate, Aadhaar card, bank account, mobile number",
        "portal_url": "https://pmsvanidhi.mohua.gov.in"
    },
    {
        "service_id": 71,
        "service_name": "Pradhan Mantri Laghu Vyapari Maandhan Yojana",
        "ministry": "Ministry of Labour and Employment",
        "category": "Finance",
        "description": "Provides pension of Rs 3000 per month to small traders shopkeepers and self employed persons after attaining age of 60 years.",
        "eligibility": "Small traders and shopkeepers between 18 to 40 years with annual turnover below Rs 1.5 crore not covered under NPS ESIC or EPFO.",
        "how_to_apply": "Enroll at nearest Common Service Centre with GST registration or trade license and bank account.",
        "documents": "GST registration or trade license, Aadhaar card, bank account, mobile number",
        "portal_url": "https://maandhan.in"
    },
    {
        "service_id": 72,
        "service_name": "National Pension System",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides voluntary long term retirement savings scheme regulated by PFRDA with tax benefits and choice of investment options.",
        "eligibility": "Indian citizens between 18 and 70 years. Available for both government employees and general public.",
        "how_to_apply": "Open NPS account at nearest Point of Presence bank or online at enps.nsdl.com with KYC documents.",
        "documents": "Aadhaar card, PAN card, bank account, passport size photo, cancelled cheque",
        "portal_url": "https://www.npscra.nsdl.co.in"
    },
    {
        "service_id": 73,
        "service_name": "PM Garib Kalyan Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides free food grains cash transfers and insurance cover to poor and vulnerable population during economic hardships.",
        "eligibility": "NFSA beneficiaries with ration card. Prioritised households identified under Antyodaya Anna Yojana and Priority Household categories.",
        "how_to_apply": "Automatic benefit for NFSA ration card holders. Collect free grains at nearest Fair Price Shop with ration card.",
        "documents": "Ration card, Aadhaar card",
        "portal_url": "https://dfpd.gov.in"
    },
    {
        "service_id": 74,
        "service_name": "Aam Aadmi Bima Yojana",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides life and disability insurance coverage to rural landless households head of family or earning member.",
        "eligibility": "Rural landless households between 18 and 59 years. Member should be head of family or earning member.",
        "how_to_apply": "Apply through state nodal agency or LIC branch with age and landless status proof.",
        "documents": "Age proof, BPL certificate or landless proof, Aadhaar card, bank account, passport size photo",
        "portal_url": "https://licindia.in"
    },
    {
        "service_id": 75,
        "service_name": "Pradhan Mantri Vaya Vandana Yojana Senior Citizen Savings",
        "ministry": "Ministry of Finance",
        "category": "Finance",
        "description": "Provides senior citizens above 60 years a safe investment option with guaranteed quarterly interest income and capital protection.",
        "eligibility": "Senior citizens above 60 years of age. Investment limit up to Rs 30 lakh per individual.",
        "how_to_apply": "Open account at nearest post office or authorized bank with age proof and investment amount.",
        "documents": "Age proof, Aadhaar card, PAN card, address proof, bank account",
        "portal_url": "https://www.indiapost.gov.in"
    },

    # ═══════════════════════════════════
    # HOUSING (10 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 76,
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
        "service_id": 77,
        "service_name": "PM Awas Yojana Urban",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides affordable housing to urban poor including slum dwellers through credit linked subsidy affordable housing in partnership and beneficiary led construction.",
        "eligibility": "Urban households with annual income up to Rs 18 lakh who do not own a pucca house anywhere in India.",
        "how_to_apply": "Apply online at pmaymis.gov.in or visit nearest Common Service Centre or Urban Local Body office.",
        "documents": "Aadhaar card, income proof, bank account, property documents, affidavit of not owning house",
        "portal_url": "https://pmaymis.gov.in"
    },
    {
        "service_id": 78,
        "service_name": "Credit Linked Subsidy Scheme",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides interest subsidy on home loans to economically weaker sections and low income groups for purchase construction or enhancement of houses.",
        "eligibility": "EWS families with annual income up to Rs 3 lakh and LIG families with income up to Rs 6 lakh.",
        "how_to_apply": "Apply through any Primary Lending Institution like banks or housing finance companies empanelled under PMAY.",
        "documents": "Income proof, Aadhaar card, property documents, bank statements",
        "portal_url": "https://pmaymis.gov.in"
    },
    {
        "service_id": 79,
        "service_name": "Rajiv Awas Yojana",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides slum free cities by upgrading slums providing housing to slum dwellers and creating affordable housing for urban poor.",
        "eligibility": "Slum dwellers and urban poor in cities implementing the scheme under state government approval.",
        "how_to_apply": "Contact Urban Local Body or city municipality for registration under slum rehabilitation and affordable housing project.",
        "documents": "Proof of slum residence, Aadhaar card, income proof, bank account",
        "portal_url": "https://mhupa.gov.in"
    },
    {
        "service_id": 80,
        "service_name": "National Urban Livelihood Mission Housing",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides shelter homes with basic amenities for urban homeless persons as part of National Urban Livelihood Mission.",
        "eligibility": "Urban homeless persons identified by Urban Local Bodies.",
        "how_to_apply": "Contact nearest Urban Local Body or city shelter home for accommodation and support services.",
        "documents": "Any available identity proof",
        "portal_url": "https://nulm.gov.in"
    },
    {
        "service_id": 81,
        "service_name": "Indira Awas Yojana",
        "ministry": "Ministry of Rural Development",
        "category": "Housing",
        "description": "Provides financial assistance for construction of houses to below poverty line rural households especially SC ST minorities and freed bonded labourers.",
        "eligibility": "BPL rural households especially SC ST freed bonded labourers widows and next of kin of defence personnel killed in action.",
        "how_to_apply": "Contact Gram Panchayat or Block Development Office for registration and selection under IAY beneficiary list.",
        "documents": "BPL card, Aadhaar card, caste certificate if applicable, bank account",
        "portal_url": "https://rhreporting.nic.in"
    },
    {
        "service_id": 82,
        "service_name": "PM Awas Yojana Urban Light House Projects",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Demonstrates alternate innovative construction technologies for affordable housing through light house projects in six cities.",
        "eligibility": "Urban poor and EWS families in six selected cities where Light House Projects are being constructed.",
        "how_to_apply": "Apply through city level implementing agency in the six selected cities for Light House Project housing.",
        "documents": "Income proof, Aadhaar card, domicile certificate, bank account",
        "portal_url": "https://pmaymis.gov.in"
    },
    {
        "service_id": 83,
        "service_name": "Housing for All Mission Rural",
        "ministry": "Ministry of Rural Development",
        "category": "Housing",
        "description": "Aims to provide pucca house with basic amenities to all homeless and houseless rural families by providing financial and technical assistance.",
        "eligibility": "Rural families without a pucca house or living in dilapidated housing identified through SECC data and Awaas Plus survey.",
        "how_to_apply": "Gram Panchayat identifies and recommends eligible beneficiaries. Contact local panchayat or BDO office.",
        "documents": "Aadhaar card, bank account, land documents, MGNREGA job card",
        "portal_url": "https://pmayg.nic.in"
    },
    {
        "service_id": 84,
        "service_name": "Affordable Rental Housing Complexes",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "description": "Provides affordable rental housing to urban migrants and poor near their workplace in industrial clusters and urban areas.",
        "eligibility": "Urban migrants workers from EWS and LIG categories seeking affordable rental accommodation near workplace.",
        "how_to_apply": "Apply through implementing agency or urban local body in cities where ARHC scheme is operational.",
        "documents": "Identity proof, income proof, Aadhaar card, employment proof",
        "portal_url": "https://mohua.gov.in"
    },
    {
        "service_id": 85,
        "service_name": "National Rurban Mission",
        "ministry": "Ministry of Rural Development",
        "category": "Housing",
        "description": "Develops rural clusters with urban amenities including housing roads water supply sanitation and economic opportunities.",
        "eligibility": "Residents of selected rural clusters under Rurban Mission in states implementing the scheme.",
        "how_to_apply": "Benefit flows automatically through development of selected clusters. Contact District Rural Development Agency for details.",
        "documents": "Aadhaar card, address proof in the Rurban cluster",
        "portal_url": "https://rurban.gov.in"
    },

    # ═══════════════════════════════════
    # IDENTITY (10 schemes)
    # ═══════════════════════════════════
    {
        "service_id": 86,
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
        "service_id": 87,
        "service_name": "PAN Card",
        "ministry": "Ministry of Finance",
        "category": "Identity",
        "description": "Provides permanent account number for tracking financial transactions and filing income tax returns to Indian citizens and entities.",
        "eligibility": "All Indian citizens foreign citizens companies firms and other entities conducting financial transactions in India.",
        "how_to_apply": "Apply online at incometax.gov.in or NSDL or UTIITSL portals or visit nearest PAN centre.",
        "documents": "Aadhaar card, proof of identity, proof of address, proof of date of birth, passport size photo",
        "portal_url": "https://www.incometax.gov.in"
    },
    {
        "service_id": 88,
        "service_name": "Passport Services",
        "ministry": "Ministry of External Affairs",
        "category": "Identity",
        "description": "Issues travel document to Indian citizens enabling them to travel internationally and serving as proof of citizenship.",
        "eligibility": "All Indian citizens. Minor children can get passport with parents as applicants.",
        "how_to_apply": "Apply online at passportindia.gov.in book appointment at nearest Passport Seva Kendra and attend with documents.",
        "documents": "Aadhaar card, proof of address, proof of date of birth, old passport if renewal",
        "portal_url": "https://passportindia.gov.in"
    },
    {
        "service_id": 89,
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
        "service_id": 90,
        "service_name": "Driving Licence",
        "ministry": "Ministry of Road Transport and Highways",
        "category": "Identity",
        "description": "Provides official authorization to drive motor vehicles on Indian roads after passing driving test and medical fitness examination.",
        "eligibility": "Citizens above 16 years for gearless vehicles and above 18 years for other vehicles with valid learner licence.",
        "how_to_apply": "Apply online at parivahan.gov.in book slot for driving test and visit RTO on appointment date.",
        "documents": "Aadhaar card, proof of age, proof of address, learner licence, passport size photos, medical certificate",
        "portal_url": "https://parivahan.gov.in"
    },
    {
        "service_id": 91,
        "service_name": "Birth Certificate",
        "ministry": "Ministry of Home Affairs",
        "category": "Identity",
        "description": "Provides official record of birth registered with government authorities serving as primary proof of age and citizenship.",
        "eligibility": "All births occurring in India must be registered within 21 days. Late registration also possible with affidavit.",
        "how_to_apply": "Register birth at nearest municipal corporation office or gram panchayat within 21 days of birth.",
        "documents": "Hospital discharge summary, parents Aadhaar card, marriage certificate of parents",
        "portal_url": "https://crsorgi.gov.in"
    },
    {
        "service_id": 92,
        "service_name": "Caste Certificate",
        "ministry": "State Government",
        "category": "Identity",
        "description": "Provides official certification of caste status for SC ST OBC communities to enable access to reservations and government benefits.",
        "eligibility": "Citizens belonging to Scheduled Caste Scheduled Tribe or Other Backward Class communities.",
        "how_to_apply": "Apply at nearest tehsil office or SDM office or through state government online portal with required documents.",
        "documents": "Aadhaar card, proof of caste from community, address proof, existing caste certificate of parent if available",
        "portal_url": "https://serviceonline.gov.in"
    },
    {
        "service_id": 93,
        "service_name": "Income Certificate",
        "ministry": "State Government",
        "category": "Identity",
        "description": "Provides official certification of annual family income for accessing income based government benefits scholarships and reservations.",
        "eligibility": "All citizens requiring income proof for accessing government schemes scholarships or benefits.",
        "how_to_apply": "Apply at nearest tehsil office or through state government online portal with income proof documents.",
        "documents": "Aadhaar card, salary slips or income proof, address proof, self declaration of income",
        "portal_url": "https://serviceonline.gov.in"
    },
    {
        "service_id": 94,
        "service_name": "DigiLocker",
        "ministry": "Ministry of Electronics and IT",
        "category": "Identity",
        "description": "Provides secure digital platform for storing sharing and verifying documents and certificates issued by government agencies.",
        "eligibility": "All Indian citizens with Aadhaar number and mobile number.",
        "how_to_apply": "Register at digilocker.gov.in or download DigiLocker app with Aadhaar number and mobile number.",
        "documents": "Aadhaar card, mobile number linked to Aadhaar",
        "portal_url": "https://digilocker.gov.in"
    },
    {
        "service_id": 95,
        "service_name": "Disability Certificate",
        "ministry": "Ministry of Social Justice and Empowerment",
        "category": "Identity",
        "description": "Provides official certification of disability for persons with disabilities to access reservations concessions and government welfare schemes.",
        "eligibility": "Persons with benchmark disabilities as defined under Rights of Persons with Disabilities Act 2016.",
        "how_to_apply": "Apply at nearest government hospital or district disability rehabilitation centre for medical assessment and certificate.",
        "documents": "Aadhaar card, medical reports, address proof, passport size photos",
        "portal_url": "https://swavlambancard.gov.in"
    },
]

# Convert to DataFrame and save
df = pd.DataFrame(schemes)
df.to_csv('data/raw/schemes.csv', index=False)

print(f"✓ Saved {len(schemes)} schemes to data/raw/schemes.csv")
print("")
print("Breakdown by category:")
print(df['category'].value_counts().to_string())