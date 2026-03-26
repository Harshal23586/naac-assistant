# Complete Metric Guidance System for NAAC Accreditation
# All 40 metrics with detailed hints, examples, and references

METRIC_GUIDANCE = {
    # =========================================================================
    # CRITERION 1: CURRICULUM (4 metrics)
    # =========================================================================
    "1.1.1": {
        "name": "Curriculum Relevance",
        "weight": 40,
        "ipo": "Input",
        "description": "Curriculum developed and implemented have relevance to local, national, regional and global developmental needs",
        "what_is_needed": """
        You need to demonstrate that your curriculum addresses:
        
        1. LOCAL NEEDS: Community requirements, regional industry, local culture, nearby geography
        2. NATIONAL PRIORITIES: NEP 2020, Skill India, Digital India, Make in India, SDGs
        3. REGIONAL REQUIREMENTS: State-specific industries, local employment needs, regional languages
        4. GLOBAL TRENDS: International standards, emerging technologies, cross-border collaborations
        """,
        "how_to_calculate": """
        Not a numerical metric. Provide qualitative description with evidence.
        
        Scoring Criteria:
        - 4.0 (Excellent): Explicitly mapped to all four areas with documented evidence
        - 3.0 (Good): Addresses all four areas but lacks documentation
        - 2.0 (Satisfactory): Addresses 2-3 areas
        - 1.0 (Poor): Addresses only 1 area
        - 0.0 (None): No evidence of relevance
        """,
        "hints": """
        💡 HINTS:
        • Create a mapping table showing how each course addresses local/global needs
        • Include stakeholder feedback (industry, alumni, community) in curriculum design
        • Show evidence of curriculum committee discussions on national priorities
        • Provide examples of courses specifically designed for local context
        • Include international collaborations that influenced curriculum
        """,
        "example_response": """
        **Example Response:**
        
        Our curriculum addresses:
        
        **Local Needs:** We have introduced courses on 'Local Agricultural Practices in Maharashtra' and 'Marathi Literature and Culture' to serve our community. We have 15 MOUs with local industries (Pune IT Park) that inform our skill-based courses.
        
        **National Priorities:** Aligned with NEP 2020, we have implemented CBCS, introduced 8 multidisciplinary courses, and established an incubation center. Our curriculum includes 'Digital India' initiatives with 100% ICT-enabled courses.
        
        **Regional Requirements:** We offer specialized courses on 'Western Ghats Biodiversity' and 'Marathi Business Communication' addressing state-specific needs. Our programs meet the requirements of Pune's IT and manufacturing industries.
        
        **Global Trends:** We have integrated 17 SDGs into our curriculum, offer courses on 'Climate Change', 'Artificial Intelligence', and have collaborations with 5 international universities for curriculum development.
        
        **Evidence:** All POs, PSOs, and COs are published at: [website URL]. Minutes of curriculum review meetings (attached) show industry participation.
        """,
        "required_documents": [
            {"name": "Programme Outcomes (POs)", "description": "List of POs for each programme", "format": "PDF/DOCX"},
            {"name": "Programme Specific Outcomes (PSOs)", "description": "List of PSOs for each programme", "format": "PDF/DOCX"},
            {"name": "Course Outcomes (COs)", "description": "List of COs for all courses", "format": "PDF/DOCX/Excel"},
            {"name": "Website URL", "description": "Link where POs/PSOs/COs are published", "format": "URL"}
        ]
    },
    
    "1.1.2": {
        "name": "Syllabus Revision",
        "weight": 40,
        "ipo": "Input",
        "description": "Percentage of Programmes where syllabus revision was carried out during the last five years",
        "what_is_needed": """
        Calculate the percentage of programmes that have undergone syllabus revision in the last 5 years.
        
        Definition: A programme is considered 'revised' if at least 20% of its courses' content has been updated.
        
        Count a programme only once even if revised multiple times in the 5-year period.
        """,
        "how_to_calculate": """
        Formula: (Number of programmes with syllabus revision ÷ Total number of programmes) × 100
        
        Example: 24 revised ÷ 30 total = 80%
        
        Scoring Criteria:
        - 4.0 (Excellent): ≥ 90%
        - 3.0 (Good): 70-89%
        - 2.0 (Satisfactory): 50-69%
        - 1.0 (Poor): 30-49%
        - 0.0 (None): < 30%
        """,
        "hints": """
        💡 HINTS:
        • Include all programmes (UG, PG, Diploma, Ph.D.) in your count
        • "Revision" includes content update, new courses added, obsolete content removed
        • Keep a Programme Revision Register with dates and details
        • BOS minutes should explicitly mention "syllabus revision approved"
        • Calculate year-wise for better tracking
        """,
        "example_response": """
        **Example Response:**
        
        **Total Programmes:** 45 (25 UG, 15 PG, 5 Ph.D.)
        
        **Programmes Revised (2019-2024):** 38
        
        **Calculation:** (38/45) × 100 = 84.4%
        
        **Breakdown:**
        - UG Programmes: 22/25 revised (88%)
        - PG Programmes: 12/15 revised (80%)
        - Ph.D. Programmes: 4/5 revised (80%)
        
        **Recent Revisions:**
        - B.Tech Computer Science: 2023 (AI/ML integration)
        - MBA: 2022 (Entrepreneurship focus added)
        - M.Sc. Biotechnology: 2024 (CRISPR technology added)
        
        **Documentation:** Attached BOS minutes for all 38 revisions and Academic Council approval letters.
        """,
        "required_documents": [
            {"name": "Programme List", "description": "List of all programmes with revision status", "format": "Excel"},
            {"name": "BOS Minutes", "description": "Minutes of Board of Studies meetings approving revisions", "format": "PDF"},
            {"name": "Academic Council Minutes", "description": "Minutes of Academic Council meetings approving revisions", "format": "PDF"}
        ],
        "calculation_fields": [
            {"field": "total_programmes", "label": "Total Programmes", "type": "number", "min": 0},
            {"field": "revised_programmes", "label": "Programmes Revised (last 5 years)", "type": "number", "min": 0}
        ]
    },
    
    "1.1.3": {
        "name": "Employability Courses",
        "weight": 35,
        "ipo": "Outcome",
        "description": "Average percentage of courses having focus on employability/entrepreneurship/skill development",
        "what_is_needed": """
        Identify courses that develop:
        1. Employability skills (communication, teamwork, problem-solving, leadership)
        2. Entrepreneurship skills (business planning, innovation, risk-taking, startup creation)
        3. Skill development (technical skills, vocational training, certifications)
        """,
        "how_to_calculate": """
        Step 1: Identify all courses with employability/entrepreneurship/skill focus
        Step 2: Per year: (Focus courses ÷ Total courses) × 100
        Step 3: Average across 5 years
        
        Example:
        Year 1: 15 focus ÷ 100 total = 15%
        Year 2: 18 focus ÷ 105 total = 17.1%
        Year 3: 22 focus ÷ 108 total = 20.4%
        Year 4: 25 focus ÷ 110 total = 22.7%
        Year 5: 28 focus ÷ 112 total = 25%
        Average = (15 + 17.1 + 20.4 + 22.7 + 25) ÷ 5 = 20.04%
        
        Scoring Criteria:
        - 4.0: ≥ 30%
        - 3.0: 20-29%
        - 2.0: 10-19%
        - 1.0: 5-9%
        - 0.0: < 5%
        """,
        "hints": """
        💡 HINTS:
        • Include courses with embedded skill components (communication labs, soft skills)
        • Entrepreneurship courses should have practical components (business plan development)
        • Skill courses should lead to industry-recognized certifications
        • Map each course to specific employability outcomes
        • Consider including internships that have academic credit
        """,
        "example_response": """
        **Example Response:**
        
        **Year-wise Data:**
        | Year | Total Courses | Employability Focus | Entrepreneurship | Skill Focus | Total Focus |
        |------|---------------|---------------------|------------------|-------------|-------------|
        | 2019-20 | 450 | 65 | 12 | 48 | 125 (27.8%) |
        | 2020-21 | 465 | 72 | 15 | 52 | 139 (29.9%) |
        | 2021-22 | 480 | 85 | 18 | 60 | 163 (34.0%) |
        | 2022-23 | 495 | 95 | 22 | 68 | 185 (37.4%) |
        | 2023-24 | 510 | 110 | 28 | 75 | 213 (41.8%) |
        
        **Average (5 years):** (27.8 + 29.9 + 34.0 + 37.4 + 41.8) ÷ 5 = 34.2%
        
        **Examples:**
        - Employability: 'Professional Communication', 'Team Dynamics', 'Critical Thinking'
        - Entrepreneurship: 'Startup Fundamentals', 'Business Model Canvas', 'Innovation Lab'
        - Skill: 'Python Programming', 'Data Analytics', 'Digital Marketing'
        
        **Outcomes:** 85% of students report improved employability skills; 12 student startups launched in last 3 years.
        """,
        "required_documents": [
            {"name": "Course List", "description": "All courses with focus areas", "format": "Excel"},
            {"name": "Syllabus Copies", "description": "Syllabus highlighting focus", "format": "PDF"},
            {"name": "Course Outcomes", "description": "COs showing skill development", "format": "PDF"}
        ],
        "calculation_fields": [
            {"field": "year_1_focus", "label": "Year 1 - Courses with Focus", "type": "number"},
            {"field": "year_1_total", "label": "Year 1 - Total Courses", "type": "number"},
            {"field": "year_2_focus", "label": "Year 2 - Courses with Focus", "type": "number"},
            {"field": "year_2_total", "label": "Year 2 - Total Courses", "type": "number"},
            {"field": "year_3_focus", "label": "Year 3 - Courses with Focus", "type": "number"},
            {"field": "year_3_total", "label": "Year 3 - Total Courses", "type": "number"},
            {"field": "year_4_focus", "label": "Year 4 - Courses with Focus", "type": "number"},
            {"field": "year_4_total", "label": "Year 4 - Total Courses", "type": "number"},
            {"field": "year_5_focus", "label": "Year 5 - Courses with Focus", "type": "number"},
            {"field": "year_5_total", "label": "Year 5 - Total Courses", "type": "number"}
        ]
    },
    
    "1.1.4": {
        "name": "Curriculum Impact",
        "weight": 35,
        "ipo": "Impact",
        "description": "Progression, employability, entrepreneurship outcomes",
        "what_is_needed": """
        Demonstrate the long-term impact of your curriculum on:
        1. Student progression to higher education (PG, Ph.D., professional courses)
        2. Employability and placement rates (campus placements, off-campus jobs)
        3. Entrepreneurship and startup creation (student-led startups, incubated ventures)
        """,
        "how_to_calculate": """
        Provide quantitative data and qualitative evidence.
        
        Key Metrics to Track:
        - % of students pursuing higher education within 1 year of graduation
        - % of students placed in jobs within 1 year
        - Number of student startups registered
        - Average starting salary
        
        Scoring Criteria:
        - 4.0: Excellent outcomes (>80% placement, >30% higher education, >10 startups)
        - 3.0: Good outcomes (>70% placement, >20% higher education)
        - 2.0: Satisfactory outcomes (>60% placement)
        - 1.0: Poor outcomes (>50% placement)
        - 0.0: No evidence of impact
        """,
        "hints": """
        💡 HINTS:
        • Track alumni data systematically through a dedicated portal
        • Conduct annual alumni surveys to capture progression data
        • Maintain a database of student startups with registration details
        • Collect offer letters from placed students as evidence
        • Track higher education admissions with proof of enrollment
        """,
        "example_response": """
        **Example Response:**
        
        **Impact Data (Last 5 Years):**
        
        | Year | Graduates | Higher Education | Placed | Startups | Avg Salary |
        |------|-----------|------------------|--------|----------|------------|
        | 2020 | 850 | 289 (34%) | 510 (60%) | 4 | ₹4.2 LPA |
        | 2021 | 875 | 306 (35%) | 542 (62%) | 6 | ₹4.5 LPA |
        | 2022 | 900 | 333 (37%) | 585 (65%) | 8 | ₹4.8 LPA |
        | 2023 | 925 | 351 (38%) | 620 (67%) | 10 | ₹5.1 LPA |
        | 2024 | 950 | 380 (40%) | 665 (70%) | 12 | ₹5.5 LPA |
        
        **Key Achievements:**
        - 40% of graduates pursuing higher education (IITs, IISc, Foreign Universities)
        - 70% placement rate with top recruiters (TCS, Infosys, Microsoft, Amazon)
        - 12 student startups registered in 2023-24, 3 receiving incubation funding
        - Alumni network of 15,000+ with 200+ entrepreneurs
        
        **Evidence:** Attached placement reports, startup registration certificates, alumni progression data.
        """,
        "required_documents": [
            {"name": "Alumni Progression Data", "description": "Higher education enrollment data", "format": "Excel"},
            {"name": "Placement Records", "description": "Placement statistics", "format": "Excel/PDF"},
            {"name": "Startup Registrations", "description": "Student startups", "format": "PDF"}
        ]
    },
    
    # =========================================================================
    # CRITERION 2: FACULTY RESOURCES (4 metrics)
    # =========================================================================
    "2.1.1": {
        "name": "Faculty Recruitment",
        "weight": 35,
        "ipo": "Input",
        "description": "Applications received, recruitment process, selection committee",
        "what_is_needed": """
        Document your faculty recruitment process including:
        1. Number of applications received vs positions filled
        2. Selection process and criteria (written test, interview, demo lecture)
        3. Selection committee composition (external experts, internal members)
        4. Transparency measures (advertisement, notification, selection list publication)
        """,
        "how_to_calculate": """
        Provide data on applications vs selections.
        
        Formula: Application-to-Selection Ratio = Total Applications ÷ Positions Filled
        
        Example: 500 applications ÷ 20 positions = 25:1 ratio
        
        Scoring Criteria:
        - 4.0: Excellent (>20:1 ratio, transparent process)
        - 3.0: Good (10-20:1 ratio)
        - 2.0: Adequate (5-9:1 ratio)
        - 1.0: Poor (1-4:1 ratio)
        - 0.0: No documented process
        """,
        "hints": """
        💡 HINTS:
        • Maintain records of all advertisements (newspaper clippings, website screenshots)
        • Keep minutes of selection committee meetings
        • Document the evaluation criteria used (weightage for each component)
        • Show how SC/ST/OBC/PWD reservations were implemented
        • Include details of guest faculty/adjunct faculty recruitment if applicable
        """,
        "example_response": """
        **Example Response:**
        
        **Recruitment Data (Last 5 Years):**
        
        | Year | Positions | Applications | Selected | Ratio | SC/ST/OBC |
        |------|-----------|--------------|----------|-------|-----------|
        | 2019-20 | 15 | 425 | 15 | 28:1 | 8 (53%) |
        | 2020-21 | 12 | 380 | 12 | 32:1 | 7 (58%) |
        | 2021-22 | 18 | 550 | 18 | 31:1 | 10 (56%) |
        | 2022-23 | 20 | 620 | 20 | 31:1 | 11 (55%) |
        | 2023-24 | 25 | 780 | 25 | 31:1 | 14 (56%) |
        
        **Total:** 90 positions filled from 2,755 applications (Average ratio 31:1)
        
        **Selection Process:**
        1. Advertisement in leading newspapers and UGC portal
        2. Screening based on API score (minimum 70)
        3. Written test (30% weightage)
        4. Seminar/Demo lecture (30% weightage)
        5. Interview with selection committee (40% weightage)
        
        **Committee Composition:** 3 external experts (IIT/IISc), 2 internal members, 1 subject expert, 1 SC/ST representative
        """,
        "required_documents": [
            {"name": "Recruitment Applications", "description": "Number of applications received", "format": "Excel"},
            {"name": "Selection Committee Minutes", "description": "Minutes of selection meetings", "format": "PDF"}
        ],
        "calculation_fields": [
            {"field": "applications", "label": "Total Applications Received (last 5 years)", "type": "number"},
            {"field": "selected", "label": "Teachers Selected (last 5 years)", "type": "number"}
        ]
    },
    
    "2.1.2": {
        "name": "Faculty Development",
        "weight": 40,
        "ipo": "Process",
        "description": "FDP programs, professional development, training",
        "what_is_needed": """
        Document faculty development initiatives:
        1. FDP programs conducted (by your institution)
        2. FDP programs attended by faculty (externally organized)
        3. Training workshops, seminars, conferences
        4. Professional development activities (online courses, certifications)
        """,
        "how_to_calculate": """
        Calculate percentage of faculty participating in development programs.
        
        Formula: (Faculty who participated in ≥1 FDP/Training ÷ Total Faculty) × 100
        
        Example: 180 faculty participated ÷ 200 total = 90%
        
        Scoring Criteria:
        - 4.0: ≥ 80% faculty participated
        - 3.0: 60-79%
        - 2.0: 40-59%
        - 1.0: 20-39%
        - 0.0: < 20%
        """,
        "hints": """
        💡 HINTS:
        • Include both in-house and external programs
        • FDPs should be of at least 5 days duration (UGC norms)
        • Document participation certificates as evidence
        • Include programs from UGC-HRDC, Malviya Mission, AICTE, NPTEL, SWAYAM
        • Count online courses with certificates (Coursera, NPTEL, etc.)
        """,
        "example_response": """
        **Example Response:**
        
        **Faculty Development Programs (Last 5 Years):**
        
        | Year | Programs Conducted | Programs Attended | Faculty Participated | Total Faculty |
        |------|-------------------|-------------------|---------------------|---------------|
        | 2019-20 | 8 | 45 | 165 | 185 (89%) |
        | 2020-21 | 12 | 68 | 175 | 192 (91%) |
        | 2021-22 | 15 | 82 | 185 | 198 (93%) |
        | 2022-23 | 18 | 95 | 192 | 205 (94%) |
        | 2023-24 | 22 | 110 | 200 | 212 (94%) |
        
        **Key Programs Conducted:**
        - "Research Methodology" (5-day, 45 participants)
        - "ICT in Teaching" (7-day, 60 participants)
        - "NEP 2020 Implementation" (3-day, 85 participants)
        - "AI in Education" (5-day, 50 participants)
        
        **External Programs Attended:**
        - UGC-HRDC Orientation/Refresher Courses: 85 faculty
        - AICTE-ATAL FDPs: 42 faculty
        - NPTEL Online Certifications: 65 faculty
        - International Conferences: 28 faculty
        
        **Impact:** 92% faculty report improved teaching effectiveness; 45 new courses introduced post-FDPs.
        """,
        "required_documents": [
            {"name": "FDP Attendance Records", "description": "Faculty participation records", "format": "Excel"},
            {"name": "Training Certificates", "description": "Sample certificates", "format": "PDF"}
        ],
        "calculation_fields": [
            {"field": "faculty_participated", "label": "Faculty Participated in FDPs (last 5 years)", "type": "number"},
            {"field": "total_faculty_fdp", "label": "Total Full-time Teachers", "type": "number"}
        ]
    },
    
    "2.1.3": {
        "name": "Faculty Qualifications",
        "weight": 35,
        "ipo": "Outcome",
        "description": "Ph.D. percentage, awards, recognitions",
        "what_is_needed": """
        Document faculty qualifications:
        1. Percentage with Ph.D. (highest degree in their discipline)
        2. National/international awards received (Ramanujan, Shanti Swarup Bhatnagar, etc.)
        3. Recognitions from professional bodies (Fellow of academies, editorial boards)
        """,
        "how_to_calculate": """
        Formula: (Ph.D. teachers ÷ Total teachers) × 100
        
        Example: 200 Ph.D. teachers ÷ 250 total = 80%
        
        Scoring Criteria:
        - 4.0: ≥ 80% Ph.D.
        - 3.0: 60-79%
        - 2.0: 40-59%
        - 1.0: 20-39%
        - 0.0: < 20%
        """,
        "hints": """
        💡 HINTS:
        • Ph.D. should be from UGC-recognized universities
        • Count faculty with Ph.D. at the time of joining (not pursuing)
        • Include M.Ch./D.M. for medical faculty, D.Sc. for senior faculty
        • Awards should be from Government/recognized bodies (not self-awarded)
        • Include fellowships like FNA, FASc, FNAE, FNASc
        """,
        "example_response": """
        **Example Response:**
        
        **Faculty Qualification Profile (2023-24):**
        
        | Department | Total | Ph.D. | % Ph.D. | Awards/Recognitions |
        |------------|-------|-------|---------|---------------------|
        | Engineering | 85 | 72 | 85% | 3 Fellows, 8 National Awards |
        | Sciences | 52 | 48 | 92% | 2 Fellows, 6 National Awards |
        | Humanities | 38 | 30 | 79% | 1 Fellow, 4 National Awards |
        | Commerce | 25 | 20 | 80% | 1 Fellow, 3 National Awards |
        | Management | 22 | 18 | 82% | 2 Fellows, 5 National Awards |
        | **Total** | **222** | **188** | **84.7%** | **9 Fellows, 26 Awards** |
        
        **Notable Awards:**
        - Prof. A. Sharma: Shanti Swarup Bhatnagar Award (2022)
        - Dr. B. Patel: Ramanujan Fellowship (2021)
        - 3 Faculty: INSA Young Scientist Award
        - 5 Faculty: Fellow of Indian National Science Academy
        - 8 Faculty: Best Teacher Awards from Government of India
        
        **Ph.D. Distribution by Source:**
        - IITs/IISc: 45%
        - Central Universities: 30%
        - State Universities: 15%
        - Foreign Universities: 10%
        """,
        "required_documents": [
            {"name": "Faculty Qualification List", "description": "Teachers with degrees", "format": "Excel"},
            {"name": "Award Letters", "description": "Award certificates", "format": "PDF"}
        ],
        "calculation_fields": [
            {"field": "phd_teachers", "label": "Teachers with Ph.D.", "type": "number"},
            {"field": "total_teachers_phd", "label": "Total Full-time Teachers", "type": "number"}
        ]
    },
    
    "2.1.4": {
        "name": "Faculty Impact",
        "weight": 40,
        "ipo": "Impact",
        "description": "Student outcomes, alumni success, mentorship impact",
        "what_is_needed": """
        Demonstrate faculty impact through:
        1. Student success stories (toppers, research scholars)
        2. Alumni achievements (leadership positions, entrepreneurial success)
        3. Mentorship outcomes (students who excelled under guidance)
        """,
        "how_to_calculate": """
        Provide qualitative and quantitative evidence.
        
        Key Metrics:
        - Number of students mentored who got PhD admissions
        - Students who published papers under faculty guidance
        - Alumni in leadership positions
        
        Scoring Criteria:
        - 4.0: Excellent documented impact with >20 success stories
        - 3.0: Good impact with 10-20 stories
        - 2.0: Satisfactory impact with 5-9 stories
        - 1.0: Limited impact with 1-4 stories
        - 0.0: No evidence
        """,
        "hints": """
        💡 HINTS:
        • Collect success stories systematically through department reports
        • Track alumni achievements through LinkedIn and alumni portals
        • Document student research publications with faculty co-authors
        • Include testimonials from successful alumni
        • Show progression of mentored students (UG→PG→Ph.D.→Post-doc)
        """,
        "example_response": """
        **Example Response:**
        
        **Faculty Impact Highlights (Last 5 Years):**
        
        **Student Success:**
        - 45 students mentored who secured Ph.D. admissions in IITs/IISc (2020-24)
        - 12 students published research papers in SCI journals with faculty co-authors
        - 8 students received INSPIRE Fellowships
        - 5 students selected for Rhodes Scholarship (1), Fulbright (2), DAAD (2)
        
        **Alumni Achievements:**
        | Alumni Name | Batch | Current Position | Faculty Mentor |
        |-------------|-------|------------------|----------------|
        | Dr. S. Kumar | 2015 | Associate Professor, IIT Delhi | Prof. A. Sharma |
        | Ms. R. Singh | 2016 | Senior Data Scientist, Google | Dr. B. Patel |
        | Mr. A. Mehta | 2017 | Founder, Startup Unicorn (₹500 Cr) | Prof. C. Desai |
        | Dr. P. Joshi | 2018 | Postdoc, MIT, USA | Dr. D. Kulkarni |
        
        **Mentorship Program:**
        - 22 faculty mentors assigned to 200+ students annually
        - 85% of mentored students reported improved academic performance
        - 15 mentored students received university medals
        
        **Evidence:** Attached alumni success stories (20 pages), mentoring reports, student publication list.
        """,
        "required_documents": [
            {"name": "Student Success Stories", "description": "Student achievements", "format": "PDF"},
            {"name": "Alumni Feedback", "description": "Alumni testimonials", "format": "PDF"}
        ]
    },
    
    # =========================================================================
    # CRITERION 3: LEARNING AND TEACHING (4 metrics)
    # =========================================================================
    "3.1.1": {
        "name": "Teaching Resources",
        "weight": 30,
        "ipo": "Input",
        "description": "Diversity of content, contemporary issues, digital tools",
        "what_is_needed": """
        Document teaching resources available:
        1. Updated syllabus and course materials (last 5 years)
        2. Digital tools and Learning Management System (LMS)
        3. Contemporary content (current affairs, latest developments)
        """,
        "how_to_calculate": """
        Assess based on availability and currency of resources.
        
        Scoring Criteria:
        - 4.0: Excellent resources with LMS, updated syllabi, and digital content
        - 3.0: Good resources with LMS and updated syllabi
        - 2.0: Adequate resources with mostly updated syllabi
        - 1.0: Limited resources, outdated materials
        - 0.0: No resources documented
        """,
        "hints": """
        💡 HINTS:
        • List all LMS platforms used (Moodle, Canvas, Google Classroom, etc.)
        • Include e-resources like NPTEL, SWAYAM, e-PG Pathshala
        • Show how faculty create digital content (videos, presentations)
        • Document integration of current events into curriculum
        • Include open educational resources (OER) used
        """,
        "example_response": """
        **Example Response:**
        
        **Teaching Resources Overview:**
        
        **1. Learning Management System (LMS):**
        - Moodle platform (customized) hosting 450+ courses
        - 12,000+ registered student accounts
        - 2,500+ hours of video content uploaded
        - Usage: 95% of courses have weekly content updates
        
        **2. Digital Resources:**
        - NPTEL Local Chapter: 35 courses accessed by 2,000+ students
        - SWAYAM: 40 MOOCs integrated into curriculum
        - e-PG Pathshala: Used for 25 PG courses
        - Coursera for Campus: 5,000+ licenses for students
        
        **3. Faculty-Generated Content:**
        - 150+ e-content modules developed (e-PG Pathshala, SWAYAM)
        - 8 faculty recognized as NPTEL/SWAYAM content creators
        - 200+ recorded lectures on institutional YouTube channel
        
        **4. Contemporary Content:**
        - Weekly current affairs integration in 80% of courses
        - Industry guest lectures: 45 sessions/year
        - Case studies: 120+ industry-specific cases developed
        
        **Evidence:** LMS access screenshots, e-content links, course material samples attached.
        """,
        "required_documents": [
            {"name": "Syllabus", "description": "Current syllabus", "format": "PDF"},
            {"name": "Course Materials", "description": "Learning materials", "format": "PDF"},
            {"name": "Digital Tools List", "description": "Tools and LMS used", "format": "Excel"}
        ]
    },
    
    "3.1.2": {
        "name": "Teaching Methodologies",
        "weight": 50,
        "ipo": "Process",
        "description": "Interactive methods, experiential learning, digital integration",
        "what_is_needed": """
        Document teaching methodologies:
        1. Interactive and participatory methods (flipped classroom, case studies, debates)
        2. Experiential learning activities (projects, field visits, internships)
        3. ICT integration in teaching (smart classrooms, online resources)
        """,
        "how_to_calculate": """
        Assess based on variety and effectiveness.
        
        Scoring Criteria:
        - 4.0: Innovative methods with proven effectiveness (5+ methods documented)
        - 3.0: Good variety of methods (3-4 methods)
        - 2.0: Adequate methods (2 methods)
        - 1.0: Traditional methods only (lecture-based)
        - 0.0: No documented methods
        """,
        "hints": """
        💡 HINTS:
        • List specific methodologies used in each department
        • Show evidence of effectiveness (student feedback, learning outcomes)
        • Include examples of innovative practices
        • Document use of simulations, role-play, case method
        • Show integration of research into teaching
        """,
        "example_response": """
        **Example Response:**
        
        **Teaching Methodologies by Department:**
        
        **1. Flipped Classroom (All Departments):**
        - Pre-class video lectures (80% courses)
        - In-class problem-solving and discussions
        - Student engagement: 85% participation
        - Improved exam scores: 15% increase over traditional method
        
        **2. Case Study Method (Management/Law):**
        - 120 Harvard Business School cases used
        - 25 indigenous cases developed
        - Students present case analyses weekly
        
        **3. Project-Based Learning (Engineering/Sciences):**
        - 45 interdisciplinary projects/year
        - Industry-sponsored projects: 12/year
        - Students present at national conferences
        
        **4. Experiential Learning:**
        - Field visits: 30/year (industry, research labs)
        - Rural immersion program: 7 days for all UG students
        - Internships: 95% students complete industry internships
        
        **5. ICT Integration:**
        - 90 smart classrooms with recording facility
        - Interactive whiteboards in 45 classrooms
        - Online quizzes and assignments (Moodle)
        - Virtual labs for 15 science courses
        
        **Student Feedback:**
        - 92% students rate teaching methodologies as 'effective'
        - 88% report improved understanding
        """,
        "required_documents": [
            {"name": "Teaching Plans", "description": "Lesson plans", "format": "PDF"},
            {"name": "Activity Reports", "description": "Activity documentation", "format": "PDF"},
            {"name": "LMS Usage Data", "description": "LMS analytics", "format": "Excel"}
        ]
    },
    
    "3.1.3": {
        "name": "Learning Outcomes",
        "weight": 35,
        "ipo": "Outcome",
        "description": "Holistic understanding, research aptitude, skill development",
        "what_is_needed": """
        Document learning outcomes:
        1. Student assessment results (pass percentages, grade distribution)
        2. Research projects and publications (student publications)
        3. Skill development certifications (industry certifications)
        """,
        "how_to_calculate": """
        Use pass percentages, project completion rates, certification data.
        
        Scoring Criteria:
        - 4.0: Excellent outcomes (>85% pass, >30% publications, >40% certifications)
        - 3.0: Good outcomes (70-84% pass)
        - 2.0: Satisfactory (60-69% pass)
        - 1.0: Poor (50-59% pass)
        - 0.0: Very poor (<50% pass)
        """,
        "hints": """
        💡 HINTS:
        • Show pass percentage trends over 5 years
        • Include number of student publications in peer-reviewed journals
        • List industry certifications earned by students
        • Show student participation in research projects
        • Include awards won by students in competitions
        """,
        "example_response": """
        **Example Response:**
        
        **Learning Outcome Metrics (2023-24):**
        
        **1. Pass Percentage:**
        | Programme | Appeared | Passed | Percentage |
        |-----------|----------|--------|------------|
        | B.Tech | 450 | 423 | 94% |
        | M.Tech | 85 | 81 | 95% |
        | B.Sc. | 320 | 298 | 93% |
        | M.Sc. | 95 | 90 | 95% |
        | B.A. | 280 | 259 | 92.5% |
        | **Overall** | **1,230** | **1,151** | **93.6%** |
        
        **2. Student Research Output (Last 3 Years):**
        - Publications: 45 (SCI journals: 18, Scopus: 22, Conference: 5)
        - Student co-authored papers with faculty: 28
        - Student-led research projects funded: 8 (₹45 Lakhs)
        
        **3. Skill Development Certifications:**
        | Certification | Provider | Students |
        |---------------|----------|----------|
        | Python | NPTEL | 320 |
        | Data Science | Coursera | 185 |
        | AWS Cloud | Amazon | 95 |
        | Digital Marketing | Google | 120 |
        | **Total Certifications** | | **720** |
        
        **4. Awards & Recognition:**
        - 12 students won national-level paper presentations
        - 5 students selected for MITACS Globalink
        - 3 students received DAAD scholarships
        """,
        "required_documents": [
            {"name": "Student Assessment Records", "description": "Results data", "format": "Excel"},
            {"name": "Project Reports", "description": "Student projects", "format": "PDF"}
        ]
    },
    
    "3.1.4": {
        "name": "Student Success",
        "weight": 35,
        "ipo": "Impact",
        "description": "Graduate success, life-long learning, career progression",
        "what_is_needed": """
        Demonstrate student success:
        1. Graduate placement and higher education
        2. Alumni career progression (leadership positions)
        3. Life-long learning engagement (continuing education)
        """,
        "how_to_calculate": """
        Provide placement data, alumni surveys, and success stories.
        
        Scoring Criteria:
        - 4.0: Excellent success metrics (>90% placement, >30% higher education)
        - 3.0: Good success rates (>80% placement)
        - 2.0: Satisfactory success (>70% placement)
        - 1.0: Limited success (>60% placement)
        - 0.0: No success data
        """,
        "hints": """
        💡 HINTS:
        • Track alumni for 5 years after graduation
        • Conduct annual alumni surveys
        • Maintain LinkedIn alumni group for tracking
        • Document alumni who started businesses
        • Show career progression (entry-level to leadership)
        """,
        "example_response": """
        **Example Response:**
        
        **Graduate Success Data (Class of 2019-2024):**
        
        **Placement Statistics (5-Year Trend):**
        | Year | Graduates | Placed | Higher Education | Average Salary |
        |------|-----------|--------|------------------|----------------|
        | 2020 | 850 | 595 (70%) | 212 (25%) | ₹4.5 LPA |
        | 2021 | 875 | 613 (70%) | 228 (26%) | ₹4.8 LPA |
        | 2022 | 900 | 648 (72%) | 243 (27%) | ₹5.1 LPA |
        | 2023 | 925 | 703 (76%) | 259 (28%) | ₹5.5 LPA |
        | 2024 | 950 | 760 (80%) | 276 (29%) | ₹6.0 LPA |
        
        **Alumni Career Progression:**
        - 45 alumni in CEO/MD positions (Fortune 500 companies)
        - 120 alumni as Professors in IITs/IISc
        - 85 alumni as Entrepreneurs (30 startups funded)
        - 200+ alumni in leadership roles (VP, Director)
        
        **Life-long Learning:**
        - 3,500 alumni enrolled in continuing education programs
        - 850 alumni completed professional certifications
        - 120 alumni pursued Ph.D. after 5+ years of work experience
        
        **Alumni Engagement:**
        - 15,000+ alumni on LinkedIn group
        - 8 alumni chapters worldwide (USA, UK, Singapore, UAE, etc.)
        - Annual alumni meet: 500+ attendees
        
        **Evidence:** Alumni success stories (50+), placement reports, LinkedIn profiles attached.
        """,
        "required_documents": [
            {"name": "Alumni Surveys", "description": "Alumni feedback", "format": "Excel"},
            {"name": "Career Progression Data", "description": "Alumni careers", "format": "Excel"}
        ]
    },
    
    # =========================================================================
    # CRITERION 4: RESEARCH AND INNOVATION (4 metrics)
    # =========================================================================
    "4.1.1": {
        "name": "Research Policy",
        "weight": 30,
        "ipo": "Input",
        "description": "Research promotion policy, research facilitation, seed money",
        "what_is_needed": """
        Document research policies:
        1. Research promotion policy (with approval date)
        2. Seed money provisions (amount, eligibility, process)
        3. Research facilitation mechanisms (lab access, research assistants, travel grants)
        """,
        "how_to_calculate": """
        Assess policy comprehensiveness and implementation.
        
        Scoring Criteria:
        - 4.0: Comprehensive policy with seed money (≥ ₹10 Lakhs/year)
        - 3.0: Good policy with seed money (₹5-10 Lakhs/year)
        - 2.0: Adequate policy with seed money (₹2-5 Lakhs/year)
        - 1.0: Limited policy (₹<2 Lakhs/year)
        - 0.0: No policy
        """,
        "hints": """
        💡 HINTS:
        • Research policy should be approved by competent authority (BoG/Syndicate)
        • Seed money should be at least ₹50,000 per project
        • Include provisions for conference travel, publication fees
        • Document research incentives (cash awards, workload reduction)
        • Include mentorship program for new researchers
        """,
        "example_response": """
        **Example Response:**
        
        **Research Promotion Policy (Approved: 15 March 2020, BoG Resolution No. 45)**
        
        **Key Provisions:**
        
        **1. Seed Money Grants:**
        - Amount: Up to ₹5 Lakhs per project
        - Eligibility: All full-time faculty with <10 years of experience
        - Selection: Research Committee evaluation
        - Disbursement: ₹2.5 Lakhs initial, ₹2.5 Lakhs after progress review
        
        **2. Research Incentives:**
        - Publication Incentive: ₹20,000 per SCI paper, ₹10,000 per Scopus paper
        - Patent Filing: Full reimbursement (₹50,000 max)
        - Conference Travel: ₹1 Lakh per year (international), ₹25,000 (national)
        
        **3. Research Facilitation:**
        - Central Instrumentation Facility: 24x7 access
        - Research Assistants: 10 allocated annually
        - Research Support Staff: 5 technicians
        - Publication Support: Up to ₹25,000 per paper
        
        **Implementation (Last 3 Years):**
        - Seed Money Awarded: ₹45 Lakhs to 22 faculty
        - Publication Incentives: ₹12 Lakhs paid (60 papers)
        - Conference Travel Support: ₹28 Lakhs (45 faculty)
        - Patent Filing Support: ₹5 Lakhs (10 patents)
        
        **Evidence:** Policy document (attached), BoG minutes, disbursement records.
        """,
        "required_documents": [
            {"name": "Research Policy Document", "description": "Approved policy", "format": "PDF"},
            {"name": "Seed Money Records", "description": "Grant details", "format": "Excel"}
        ]
    },
    
    "4.1.2": {
        "name": "Research Process",
        "weight": 50,
        "ipo": "Process",
        "description": "Interdisciplinary collaboration, societal issue focus",
        "what_is_needed": """
        Document research processes:
        1. Interdisciplinary research projects (collaboration across departments)
        2. Collaborations with industry/institutions (national/international)
        3. Research addressing societal issues (local/global challenges)
        """,
        "how_to_calculate": """
        Count collaborative projects and interdisciplinary initiatives.
        
        Scoring Criteria:
        - 4.0: Excellent collaboration (>10 active projects, >5 interdisciplinary)
        - 3.0: Good collaboration (5-9 projects)
        - 2.0: Some collaboration (2-4 projects)
        - 1.0: Limited collaboration (1 project)
        - 0.0: No collaboration
        """,
        "hints": """
        💡 HINTS:
        • List all MoUs with research collaborations
        • Show evidence of interdisciplinary centers/institutes
        • Include projects addressing SDGs, government priorities
        • Document industry-funded research projects
        • Include joint supervision of Ph.D. students
        """,
        "example_response": """
        **Example Response:**
        
        **Research Collaborations (Active Projects):**
        
        **Interdisciplinary Projects:**
        | Project Title | Departments Involved | Funding | Duration |
        |---------------|---------------------|---------|----------|
        | AI for Healthcare | CSE, BioTech, Medicine | DST | 2022-25 |
        | Sustainable Materials | Chemistry, Civil, Mech | SERB | 2023-26 |
        | Water Conservation | Environmental Sci, Civil | ICSSR | 2022-24 |
        | Smart Agriculture | Electronics, Agriculture | MeitY | 2023-26 |
        
        **Industry Collaborations:**
        - TCS Research: 3 joint projects (AI, Cloud, Data Science)
        - Microsoft Research: 2 projects (Computer Vision, NLP)
        - IBM Research: 1 project (Quantum Computing)
        - Local Industry: 8 projects with Pune-based companies
        
        **International Collaborations:**
        - University of Cambridge: Joint research on Climate Change
        - MIT, USA: Faculty exchange program (5 faculty/year)
        - National University of Singapore: Joint Ph.D. program
        - University of Melbourne: Research partnership agreement
        
        **Societal Impact Projects:**
        1. "Clean Ganga" Initiative: Water quality monitoring
        2. "Digital India" Project: Rural internet connectivity
        3. "Swachh Bharat" Research: Solid waste management
        4. "Women Empowerment" Study: Gender equality in STEM
        
        **Evidence:** MoUs (12), project reports, joint publications list attached.
        """,
        "required_documents": [
            {"name": "Research Project List", "description": "Projects with details", "format": "Excel"},
            {"name": "Collaboration MoUs", "description": "MoU documents", "format": "PDF"}
        ]
    },
    
    "4.1.3": {
        "name": "Research Output",
        "weight": 70,
        "ipo": "Outcome",
        "description": "Publications, patents, Ph.D.s awarded",
        "what_is_needed": """
        Document research outputs:
        1. Publications in journals (SCI/Scopus/UGC-CARE)
        2. Patents filed/granted (Indian/International)
        3. Ph.D. degrees awarded (full-time/part-time)
        """,
        "how_to_calculate": """
        Papers per faculty, patents, Ph.D. per faculty.
        
        Scoring Criteria:
        - 4.0: ≥3 papers/faculty/year, ≥1 patent, ≥0.5 Ph.D./faculty/year
        - 3.0: 2 papers/faculty/year
        - 2.0: 1 paper/faculty/year
        - 1.0: 0.5 paper/faculty/year
        - 0.0: No output
        """,
        "hints": """
        💡 HINTS:
        • Include only UGC-CARE listed journals
        • Count patents published/granted (not just filed)
        • Ph.D.s awarded should have thesis submission date in last 5 years
        • Include book chapters, conference proceedings with ISBN/ISSN
        • Show citation metrics for publications
        """,
        "example_response": """
        **Example Response:**
        
        **Research Output (Last 5 Years):**
        
        **Publications:**
        | Year | SCI | Scopus | UGC-CARE | Total | Impact Factor |
        |------|-----|--------|----------|-------|---------------|
        | 2020 | 85 | 120 | 45 | 250 | 3.2 |
        | 2021 | 95 | 135 | 52 | 282 | 3.5 |
        | 2022 | 110 | 150 | 58 | 318 | 3.8 |
        | 2023 | 125 | 168 | 65 | 358 | 4.1 |
        | 2024 | 140 | 185 | 72 | 397 | 4.4 |
        | **Total** | **555** | **758** | **292** | **1,605** | |
        
        **Papers per Faculty:** 1,605 ÷ 222 = 7.2 papers/faculty (5 years) = 1.44 papers/faculty/year
        
        **Patents:**
        - Filed: 45 patents (India: 38, PCT: 7)
        - Granted: 12 patents (India: 10, US: 2)
        - Licensed: 3 patents to industry
        
        **Ph.D. Awards:**
        | Year | Full-time | Part-time | Total |
        |------|-----------|-----------|-------|
        | 2020 | 18 | 12 | 30 |
        | 2021 | 22 | 14 | 36 |
        | 2022 | 25 | 16 | 41 |
        | 2023 | 28 | 18 | 46 |
        | 2024 | 32 | 20 | 52 |
        | **Total** | **125** | **80** | **205** |
        
        **Ph.D. per Faculty:** 205 ÷ 222 = 0.92 Ph.D./faculty (5 years)
        
        **Publications by Faculty Category:**
        - Professors: 2.8 papers/year
        - Associate Professors: 1.6 papers/year
        - Assistant Professors: 1.2 papers/year
        
        **Evidence:** Publication list, patent certificates, Ph.D. award letters attached.
        """,
        "required_documents": [
            {"name": "Publication List", "description": "Papers with journal details", "format": "Excel"},
            {"name": "Patent Certificates", "description": "Patent documents", "format": "PDF"},
            {"name": "Ph.D. Award Letters", "description": "Ph.D. certificates", "format": "PDF"}
        ]
    },
    
    "4.1.4": {
        "name": "Research Impact",
        "weight": 50,
        "ipo": "Impact",
        "description": "Citations, peer recognition, industry funding",
        "what_is_needed": """
        Demonstrate research impact:
        1. Citation metrics (total citations, h-index)
        2. Awards and recognition (national/international)
        3. Industry funding for research (sponsored projects)
        """,
        "how_to_calculate": """
        Calculate citations, h-index, funding amounts.
        
        Scoring Criteria:
        - 4.0: High citations (h-index >50), external funding >₹10 Cr
        - 3.0: Good citations (h-index >30), funding >₹5 Cr
        - 2.0: Some citations (h-index >15), funding >₹2 Cr
        - 1.0: Limited citations, funding <₹1 Cr
        - 0.0: No impact
        """,
        "hints": """
        💡 HINTS:
        • Use Scopus/Web of Science for citation metrics
        • Include h-index of top researchers
        • List prestigious awards (INSA, NASI, Shanti Swarup Bhatnagar)
        • Show industry funding from private sector
        • Include technology transfer/commercialization examples
        """,
        "example_response": """
        **Example Response:**
        
        **Citation Metrics (Scopus Data):**
        
        **Institutional Metrics:**
        - Total Citations: 45,280
        - h-index: 82
        - i10-index: 1,250
        - Top 1% Papers: 28
        - Top 10% Papers: 245
        
        **Top Researchers (by h-index):**
        | Name | Department | h-index | Citations | Papers |
        |------|------------|---------|-----------|--------|
        | Prof. A. Sharma | Physics | 45 | 12,500 | 180 |
        | Prof. B. Patel | Chemistry | 42 | 10,200 | 150 |
        | Prof. C. Desai | CSE | 38 | 8,500 | 120 |
        | Dr. D. Kulkarni | Biotech | 35 | 7,200 | 95 |
        
        **Awards & Recognition (Last 5 Years):**
        - Shanti Swarup Bhatnagar Award: 2 faculty
        - INSA Young Scientist Award: 5 faculty
        - National Academy Fellowship: 8 faculty
        - Highly Cited Researcher (Clarivate): 3 faculty
        - Distinguished Alumnus Awards: 4 faculty
        
        **Research Funding (Last 5 Years):**
        | Source | Projects | Amount (₹ Cr) |
        |--------|----------|---------------|
        | DST | 45 | 32.5 |
        | SERB | 38 | 28.2 |
        | DBT | 22 | 18.5 |
        | Industry | 28 | 15.8 |
        | International | 12 | 12.5 |
        | **Total** | **145** | **107.5** |
        
        **Technology Transfer:**
        - 5 patents licensed to industry
        - 2 startups spun-off from research
        - 3 technologies commercialized (revenue ₹2.5 Cr)
        
        **Evidence:** Scopus profile, award certificates, funding letters attached.
        """,
        "required_documents": [
            {"name": "Citation Metrics", "description": "Citation data", "format": "Excel"},
            {"name": "Funding Agency Letters", "description": "Grant letters", "format": "PDF"}
        ]
    },
    
    # =========================================================================
    # CRITERION 5: CO-CURRICULAR & EXTRA-CURRICULAR (4 metrics)
    # =========================================================================
    "5.1.1": {
        "name": "EC/CC Policies",
        "weight": 15,
        "ipo": "Input",
        "description": "Credit for EC/CC activities, policies and framework",
        "what_is_needed": """
        Document EC/CC policies:
        1. Credit system for EC/CC activities (how many credits)
        2. Activity framework (types of activities recognized)
        3. Incentive structure (awards, certificates)
        """,
        "hints": """
        💡 HINTS:
        • Show how EC/CC activities are integrated into curriculum
        • List types of activities recognized (sports, cultural, NSS, NCC)
        • Document credit allocation (e.g., 2 credits for NSS)
        • Include assessment criteria for EC/CC credits
        """,
        "required_documents": [
            {"name": "Academic Policy Documents", "description": "Credit policy", "format": "PDF"}
        ]
    },
    
    "5.1.2": {
        "name": "Activity Process",
        "weight": 25,
        "ipo": "Process",
        "description": "Incentivization, logistics, syllabus connection",
        "what_is_needed": """
        Document EC/CC processes:
        1. Activity organization (frequency, structure)
        2. Student participation (enrollment, attendance)
        3. Integration with curriculum (mapped to courses)
        """,
        "hints": """
        💡 HINTS:
        • List all EC/CC activities conducted annually
        • Show student participation statistics
        • Document how activities connect to learning outcomes
        • Include budget allocation for activities
        """,
        "required_documents": [
            {"name": "Activity Reports", "description": "Activity documentation", "format": "PDF"},
            {"name": "Budget Allocations", "description": "Funding details", "format": "Excel"}
        ]
    },
    
    "5.1.3": {
        "name": "Student Achievements",
        "weight": 20,
        "ipo": "Outcome",
        "description": "Awards, recognition, talent discovery",
        "what_is_needed": """
        Document student achievements:
        1. Awards won at state/national/international level
        2. Recognition in sports, cultural, technical events
        3. Talent discovery outcomes (students who excelled)
        """,
        "hints": """
        💡 HINTS:
        • List all awards with details (event, level, category)
        • Include team awards (count as one)
        • Show year-wise trend of achievements
        • Document students who represented institution at higher levels
        """,
        "required_documents": [
            {"name": "Awards Won", "description": "Award certificates", "format": "PDF"},
            {"name": "Student Achievements List", "description": "Achievement list", "format": "Excel"}
        ]
    },
    
    "5.1.4": {
        "name": "Holistic Development",
        "weight": 20,
        "ipo": "Impact",
        "description": "Student representation, confidence, leadership",
        "what_is_needed": """
        Demonstrate holistic development:
        1. Student leadership roles (student council, club heads)
        2. Confidence and soft skills (assessments)
        3. Satisfaction surveys (feedback on activities)
        """,
        "hints": """
        💡 HINTS:
        • Show leadership positions held by students
        • Include soft skills assessment results
        • Present satisfaction survey data
        • Document student feedback on EC/CC programs
        """,
        "required_documents": [
            {"name": "Student Leadership Records", "description": "Leadership positions", "format": "Excel"},
            {"name": "Satisfaction Surveys", "description": "Survey results", "format": "Excel"}
        ]
    },
    
    # =========================================================================
    # CRITERION 6: COMMUNITY ENGAGEMENT (4 metrics)
    # =========================================================================
    "6.1.1": {
        "name": "Outreach Policies",
        "weight": 15,
        "ipo": "Input",
        "description": "Curriculum-community linkage, NSS/NCC policies",
        "hints": """
        💡 HINTS:
        • Document NSS/NCC unit structure
        • Show community engagement policy
        • Include extension activity guidelines
        """,
        "required_documents": [
            {"name": "Outreach Policy", "description": "Policy document", "format": "PDF"},
            {"name": "NSS/NCC Records", "description": "Activity records", "format": "PDF"}
        ]
    },
    
    "6.1.2": {
        "name": "Engagement Process",
        "weight": 25,
        "ipo": "Process",
        "description": "Social outreach, village adoption, extension activities",
        "hints": """
        💡 HINTS:
        • List all outreach activities conducted
        • Show villages/institutions adopted
        • Document number of beneficiaries
        • Include collaboration with NGOs/Government
        """,
        "required_documents": [
            {"name": "Activity Reports", "description": "Activity documentation", "format": "PDF"},
            {"name": "Village Adoption Letters", "description": "Adoption documents", "format": "PDF"}
        ]
    },
    
    "6.1.3": {
        "name": "Community Outcomes",
        "weight": 20,
        "ipo": "Outcome",
        "description": "Student social responsibility, community feedback",
        "hints": """
        💡 HINTS:
        • Track student volunteer hours
        • Collect community feedback on activities
        • Document social impact metrics
        """,
        "required_documents": [
            {"name": "Volunteer Hours", "description": "Hour logs", "format": "Excel"},
            {"name": "Community Feedback", "description": "Feedback forms", "format": "PDF"}
        ]
    },
    
    "6.1.4": {
        "name": "Community Impact",
        "weight": 20,
        "ipo": "Impact",
        "description": "Health, education, economic improvement",
        "hints": """
        💡 HINTS:
        • Show measurable community improvements
        • Document before-after impact
        • Include case studies of community transformation
        """,
        "required_documents": [
            {"name": "Impact Assessment Reports", "description": "Impact studies", "format": "PDF"}
        ]
    },
    
    # =========================================================================
    # CRITERION 7: GREEN INITIATIVES (4 metrics)
    # =========================================================================
    "7.1.1": {
        "name": "Sustainability Policies",
        "weight": 10,
        "ipo": "Input",
        "description": "Green initiatives credit, sustainability policies",
        "hints": """
        💡 HINTS:
        • Document green campus policy
        • Show sustainability guidelines
        • Include environmental commitments
        """,
        "required_documents": [
            {"name": "Sustainability Policy", "description": "Policy document", "format": "PDF"}
        ]
    },
    
    "7.1.2": {
        "name": "Green Processes",
        "weight": 20,
        "ipo": "Process",
        "description": "Renewable energy, waste management, green buildings",
        "hints": """
        💡 HINTS:
        • List all green measures implemented
        • Show solar panel capacity (kW)
        • Document waste segregation and recycling
        • Include water harvesting systems
        • Show energy audit reports
        """,
        "required_documents": [
            {"name": "Energy Bills", "description": "Energy consumption", "format": "PDF"},
            {"name": "Waste Reports", "description": "Waste management", "format": "PDF"},
            {"name": "Green Audit", "description": "Audit reports", "format": "PDF"}
        ]
    },
    
    "7.1.3": {
        "name": "Environmental Outcomes",
        "weight": 15,
        "ipo": "Outcome",
        "description": "Environmental orientation, awareness",
        "hints": """
        💡 HINTS:
        • Conduct awareness surveys
        • Document environmental programs
        • Show green practices adoption rates
        """,
        "required_documents": [
            {"name": "Student Awareness Surveys", "description": "Survey results", "format": "Excel"}
        ]
    },
    
    "7.1.4": {
        "name": "Environmental Impact",
        "weight": 15,
        "ipo": "Impact",
        "description": "Carbon footprint reduction",
        "hints": """
        💡 HINTS:
        • Calculate carbon footprint reduction
        • Show energy savings data
        • Document waste reduction metrics
        """,
        "required_documents": [
            {"name": "Carbon Footprint Metrics", "description": "Footprint data", "format": "Excel"}
        ]
    },
    
    # =========================================================================
    # CRITERION 8: GOVERNANCE AND ADMINISTRATION (4 metrics)
    # =========================================================================
    "8.1.1": {
        "name": "Governance Framework",
        "weight": 15,
        "ipo": "Input",
        "description": "Act, Statutes, Regulations, Policies",
        "hints": """
        💡 HINTS:
        • Upload Institutional Act
        • Include approved Statutes
        • Document all governance policies
        """,
        "required_documents": [
            {"name": "Institutional Act", "description": "Act document", "format": "PDF"},
            {"name": "Statutes", "description": "Statute documents", "format": "PDF"},
            {"name": "Policy Documents", "description": "Governance policies", "format": "PDF"}
        ]
    },
    
    "8.1.2": {
        "name": "Governance Process",
        "weight": 25,
        "ipo": "Process",
        "description": "Implementation, e-Governance, grievance redressal",
        "hints": """
        💡 HINTS:
        • Show policy implementation records
        • Document e-Governance systems
        • Include grievance redressal mechanism
        • Show complaint resolution statistics
        """,
        "required_documents": [
            {"name": "Compliance Reports", "description": "Compliance documentation", "format": "PDF"},
            {"name": "e-Governance Records", "description": "System usage", "format": "PDF"},
            {"name": "Grievance Data", "description": "Grievance records", "format": "Excel"}
        ]
    },
    
    "8.1.3": {
        "name": "Governance Outcomes",
        "weight": 20,
        "ipo": "Outcome",
        "description": "Transparency, mission achievement",
        "hints": """
        💡 HINTS:
        • Show transparency metrics (website updates, RTI compliance)
        • Document mission achievement indicators
        • Include stakeholder satisfaction surveys
        """,
        "required_documents": [
            {"name": "Governance Audit Reports", "description": "Audit findings", "format": "PDF"}
        ]
    },
    
    "8.1.4": {
        "name": "Governance Impact",
        "weight": 20,
        "ipo": "Impact",
        "description": "Increased GER, institutional reputation",
        "hints": """
        💡 HINTS:
        • Show enrollment growth trends
        • Document ranking improvements (NIRF, QS)
        • Include stakeholder trust metrics
        """,
        "required_documents": [
            {"name": "Enrollment Statistics", "description": "Student numbers", "format": "Excel"},
            {"name": "NIRF Rankings", "description": "Ranking data", "format": "PDF"}
        ]
    },
    
    # =========================================================================
    # CRITERION 9: INFRASTRUCTURE (4 metrics)
    # =========================================================================
    "9.1.1": {
        "name": "Facility Inventory",
        "weight": 10,
        "ipo": "Input",
        "description": "Land, buildings, labs, library, sports facilities",
        "hints": """
        💡 HINTS:
        • Provide complete inventory of all facilities
        • Include area in sq. meters
        • Upload geo-tagged photos of facilities
        """,
        "required_documents": [
            {"name": "Facility Inventory", "description": "Complete list", "format": "Excel"},
            {"name": "Geo-tagged Photos", "description": "Photos with location", "format": "JPG/PNG"}
        ]
    },
    
    "9.1.2": {
        "name": "Infrastructure Utilization",
        "weight": 15,
        "ipo": "Process",
        "description": "Maintenance, usage, accessibility",
        "hints": """
        💡 HINTS:
        • Show utilization rates of facilities
        • Document maintenance schedule
        • Include accessibility features
        """,
        "required_documents": [
            {"name": "Utilization Reports", "description": "Usage data", "format": "Excel"},
            {"name": "Maintenance Records", "description": "Maintenance logs", "format": "PDF"}
        ]
    },
    
    "9.1.3": {
        "name": "Infrastructure Availability",
        "weight": 10,
        "ipo": "Outcome",
        "description": "Student-facility ratios",
        "hints": """
        💡 HINTS:
        • Calculate students per classroom
        • Show students per computer ratio
        • Include students per library seat
        """,
        "required_documents": [
            {"name": "Facility Availability Metrics", "description": "Ratio data", "format": "Excel"}
        ]
    },
    
    "9.1.4": {
        "name": "Infrastructure Impact",
        "weight": 15,
        "ipo": "Impact",
        "description": "Student/faculty satisfaction",
        "hints": """
        💡 HINTS:
        • Conduct satisfaction surveys
        • Show survey results by category
        • Include feedback on infrastructure
        """,
        "required_documents": [
            {"name": "Satisfaction Surveys", "description": "Survey results", "format": "Excel"}
        ]
    },
    
    # =========================================================================
    # CRITERION 10: FINANCIAL RESOURCES (4 metrics)
    # =========================================================================
    "10.1.1": {
        "name": "Financial Resources",
        "weight": 20,
        "ipo": "Input",
        "description": "Budget allocation, grants, CSR funds",
        "hints": """
        💡 HINTS:
        • Show annual budget allocation
        • Document all grants received
        • Include CSR funds and donations
        """,
        "required_documents": [
            {"name": "Budget Documents", "description": "Budget allocations", "format": "PDF"},
            {"name": "Grant Letters", "description": "Funding letters", "format": "PDF"}
        ]
    },
    
    "10.1.2": {
        "name": "Financial Management",
        "weight": 25,
        "ipo": "Process",
        "description": "Resource mobilization, financial systems",
        "hints": """
        💡 HINTS:
        • Document resource mobilization strategies
        • Show financial systems and controls
        • Include audit process documentation
        """,
        "required_documents": [
            {"name": "Audited Statements", "description": "Audit reports", "format": "PDF"},
            {"name": "Financial Reports", "description": "Financial statements", "format": "PDF"}
        ]
    },
    
    "10.1.3": {
        "name": "Financial Health",
        "weight": 25,
        "ipo": "Outcome",
        "description": "Income-expenditure balance, financial ratios",
        "hints": """
        💡 HINTS:
        • Show income-expenditure balance
        • Calculate key financial ratios
        • Document surplus/deficit trends
        """,
        "required_documents": [
            {"name": "Financial Ratios", "description": "Ratio analysis", "format": "Excel"}
        ]
    },
    
    "10.1.4": {
        "name": "Financial Impact",
        "weight": 30,
        "ipo": "Impact",
        "description": "Correlation with outcomes, sustainability",
        "hints": """
        💡 HINTS:
        • Show correlation between funding and outcomes
        • Document sustainability metrics
        • Include long-term financial planning
        """,
        "required_documents": [
            {"name": "Financial-Outcome Analysis", "description": "Correlation data", "format": "Excel"}
        ]
    }
}

# Helper function to calculate scores automatically
def calculate_auto_score(metric_code, fields):
    """Auto-calculate score based on entered data"""
    if metric_code == "1.1.2":
        total = fields.get('total_programmes', 0)
        revised = fields.get('revised_programmes', 0)
        if total > 0:
            pct = (revised / total) * 100
            if pct >= 90:
                return 4.0, f"Excellent: {pct:.1f}% programmes revised"
            elif pct >= 70:
                return 3.0, f"Good: {pct:.1f}% programmes revised"
            elif pct >= 50:
                return 2.0, f"Satisfactory: {pct:.1f}% programmes revised"
            elif pct >= 30:
                return 1.0, f"Poor: {pct:.1f}% programmes revised"
            return 0.0, f"Very Poor: {pct:.1f}% programmes revised"
    
    elif metric_code == "1.1.3":
        years = []
        for i in range(1, 6):
            focus = fields.get(f'year_{i}_focus', 0)
            total = fields.get(f'year_{i}_total', 1)
            if total > 0:
                years.append((focus / total) * 100)
        if years:
            avg = sum(years) / len(years)
            if avg >= 30:
                return 4.0, f"Excellent: {avg:.1f}% average"
            elif avg >= 20:
                return 3.0, f"Good: {avg:.1f}% average"
            elif avg >= 10:
                return 2.0, f"Satisfactory: {avg:.1f}% average"
            elif avg >= 5:
                return 1.0, f"Poor: {avg:.1f}% average"
            return 0.0, f"Very Poor: {avg:.1f}% average"
    
    elif metric_code == "2.1.1":
        apps = fields.get('applications', 0)
        selected = fields.get('selected', 1)
        ratio = apps / selected if selected > 0 else 0
        if ratio >= 20:
            return 4.0, f"Excellent: {ratio:.1f}:1 selection ratio"
        elif ratio >= 10:
            return 3.0, f"Good: {ratio:.1f}:1 selection ratio"
        elif ratio >= 5:
            return 2.0, f"Satisfactory: {ratio:.1f}:1 selection ratio"
        elif ratio >= 1:
            return 1.0, f"Poor: {ratio:.1f}:1 selection ratio"
        return 0.0, "No applications received"
    
    elif metric_code == "2.1.2":
        participated = fields.get('faculty_participated', 0)
        total = fields.get('total_faculty_fdp', 1)
        pct = (participated / total) * 100 if total > 0 else 0
        if pct >= 80:
            return 4.0, f"Excellent: {pct:.1f}% faculty participated"
        elif pct >= 60:
            return 3.0, f"Good: {pct:.1f}% faculty participated"
        elif pct >= 40:
            return 2.0, f"Satisfactory: {pct:.1f}% faculty participated"
        elif pct >= 20:
            return 1.0, f"Poor: {pct:.1f}% faculty participated"
        return 0.0, f"Very Poor: {pct:.1f}% faculty participated"
    
    elif metric_code == "2.1.3":
        phd = fields.get('phd_teachers', 0)
        total = fields.get('total_teachers_phd', 1)
        pct = (phd / total) * 100 if total > 0 else 0
        if pct >= 80:
            return 4.0, f"Excellent: {pct:.1f}% Ph.D. teachers"
        elif pct >= 60:
            return 3.0, f"Good: {pct:.1f}% Ph.D. teachers"
        elif pct >= 40:
            return 2.0, f"Satisfactory: {pct:.1f}% Ph.D. teachers"
        elif pct >= 20:
            return 1.0, f"Poor: {pct:.1f}% Ph.D. teachers"
        return 0.0, f"Very Poor: {pct:.1f}% Ph.D. teachers"
    
    elif metric_code == "3.4.5":
        papers = fields.get('total_papers', 0)
        teachers = fields.get('total_teachers_papers', 1)
        per_teacher = papers / teachers if teachers > 0 else 0
        if per_teacher >= 3:
            return 4.0, f"Excellent: {per_teacher:.1f} papers per teacher"
        elif per_teacher >= 2:
            return 3.0, f"Good: {per_teacher:.1f} papers per teacher"
        elif per_teacher >= 1:
            return 2.0, f"Satisfactory: {per_teacher:.1f} papers per teacher"
        elif per_teacher >= 0.5:
            return 1.0, f"Poor: {per_teacher:.1f} papers per teacher"
        return 0.0, f"Very Poor: {per_teacher:.1f} papers per teacher"
    
    elif metric_code == "7.1.2":
        count = sum(1 for k, v in fields.items() if v)
        if count >= 5:
            return 4.0, f"Excellent: {count} energy conservation measures"
        elif count >= 4:
            return 3.0, f"Good: {count} energy conservation measures"
        elif count >= 3:
            return 2.0, f"Satisfactory: {count} energy conservation measures"
        elif count >= 1:
            return 1.0, f"Poor: {count} energy conservation measures"
        return 0.0, "No energy conservation measures"
    
    return None, "Auto-calculation not available for this metric"
