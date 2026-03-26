# NAAC Configuration - Fixed with 4 metrics per criterion (40 total)
# Based on Dr. Radhakrishnan Committee Report 2023

ORIENTATION_CATEGORIES = {
    "multi_disciplinary_research": "Multi-disciplinary Education and Research-Intensive",
    "research_intensive": "Research-Intensive",
    "teaching_intensive": "Teaching-Intensive",
    "specialized_streams": "Specialised Streams",
    "vocational_skill": "Vocational and Skill-Intensive",
    "community_engagement": "Community Engagement & Service",
    "rural_remote": "Rural & Remote Location"
}

LEGACY_CATEGORIES = {
    "old_established": "Old and Established",
    "new_upcoming": "New and Upcoming"
}

CRITERIA = {
    1: {"name": "Curriculum", "weight": 150, "description": "Curriculum design, development, relevance, and outcomes"},
    2: {"name": "Faculty Resources", "weight": 150, "description": "Faculty recruitment, development, quality, and impact on students"},
    3: {"name": "Learning and Teaching", "weight": 150, "description": "Teaching methodologies, student engagement, learning outcomes"},
    4: {"name": "Research and Innovation", "weight": 200, "description": "Research culture, output, patents, innovation ecosystem"},
    5: {"name": "Co-curricular and Extra-curricular Activities", "weight": 80, "description": "Student development through EC/CC activities"},
    6: {"name": "Community Engagement", "weight": 80, "description": "Social outreach, extension activities, community impact"},
    7: {"name": "Green Initiatives", "weight": 60, "description": "Sustainability, environment, green campus"},
    8: {"name": "Governance and Administration", "weight": 80, "description": "Leadership, transparency, e-governance, grievance redressal"},
    9: {"name": "Infrastructure Development", "weight": 50, "description": "Physical facilities, IT infrastructure, maintenance"},
    10: {"name": "Financial Resources and Management", "weight": 100, "description": "Budgeting, resource mobilization, financial sustainability"}
}

TOTAL_WEIGHTAGE = 1100

BINARY_ACCREDITATION = {
    "accredited": {"min_score": 60, "description": "Meets minimum standards"},
    "awaiting_accreditation": {"min_score": 50, "max_score": 59, "description": "Close to threshold"},
    "not_accredited": {"max_score": 49, "description": "Far below standards"}
}

MATURITY_LEVELS = {
    1: {"name": "Foundational Level", "min_score": 60},
    2: {"name": "Developing Level", "min_score": 70},
    3: {"name": "Advanced Level", "min_score": 80},
    4: {"name": "National Excellence", "min_score": 90},
    5: {"name": "Global Excellence", "min_score": 95}
}

# ============================================================================
# METRICS - Exactly 4 per criterion (40 total)
# ============================================================================

METRICS = {
    # CRITERION 1: CURRICULUM (4 metrics)
    "1.1.1": {"name": "Curriculum Relevance", "weight": 40, "ipo": "Input", 
              "description": "Curriculum addresses local, national, regional, global needs",
              "documents": ["POs", "PSOs", "COs", "Website URL"]},
    "1.1.2": {"name": "Syllabus Revision", "weight": 40, "ipo": "Input", 
              "description": "Percentage of programmes with syllabus revision in last 5 years",
              "documents": ["Programme List", "BOS Minutes", "Academic Council Minutes"]},
    "1.1.3": {"name": "Employability Courses", "weight": 35, "ipo": "Outcome", 
              "description": "Courses with employability/entrepreneurship/skill focus",
              "documents": ["Course List", "Syllabus Copies", "Course Outcomes"]},
    "1.1.4": {"name": "Curriculum Impact", "weight": 35, "ipo": "Impact", 
              "description": "Progression, employability, entrepreneurship outcomes",
              "documents": ["Alumni Progression Data", "Placement Records", "Startup Registrations"]},
    
    # CRITERION 2: FACULTY RESOURCES (4 metrics)
    "2.1.1": {"name": "Faculty Recruitment", "weight": 35, "ipo": "Input", 
              "description": "Applications received, recruitment process",
              "documents": ["Recruitment Applications", "Selection Committee Minutes"]},
    "2.1.2": {"name": "Faculty Development", "weight": 40, "ipo": "Process", 
              "description": "FDP programs, professional development",
              "documents": ["FDP Attendance Records", "Training Certificates"]},
    "2.1.3": {"name": "Faculty Qualifications", "weight": 35, "ipo": "Outcome", 
              "description": "Ph.D. percentage, awards, recognitions",
              "documents": ["Faculty Qualification List", "Award Letters"]},
    "2.1.4": {"name": "Faculty Impact", "weight": 40, "ipo": "Impact", 
              "description": "Student outcomes, alumni success",
              "documents": ["Student Success Stories", "Alumni Feedback"]},
    
    # CRITERION 3: LEARNING AND TEACHING (4 metrics)
    "3.1.1": {"name": "Teaching Resources", "weight": 30, "ipo": "Input", 
              "description": "Diversity of content, contemporary issues",
              "documents": ["Syllabus", "Course Materials", "Digital Tools"]},
    "3.1.2": {"name": "Teaching Methodologies", "weight": 50, "ipo": "Process", 
              "description": "Interactive methods, experiential learning",
              "documents": ["Teaching Plans", "Activity Reports", "LMS Usage"]},
    "3.1.3": {"name": "Learning Outcomes", "weight": 35, "ipo": "Outcome", 
              "description": "Holistic understanding, research aptitude",
              "documents": ["Student Assessment Records", "Project Reports"]},
    "3.1.4": {"name": "Student Success", "weight": 35, "ipo": "Impact", 
              "description": "Graduate success, life-long learning",
              "documents": ["Alumni Surveys", "Career Progression Data"]},
    
    # CRITERION 4: RESEARCH AND INNOVATION (4 metrics)
    "4.1.1": {"name": "Research Policy", "weight": 30, "ipo": "Input", 
              "description": "Research promotion policy, research facilitation",
              "documents": ["Research Policy Document", "Seed Money Records"]},
    "4.1.2": {"name": "Research Process", "weight": 50, "ipo": "Process", 
              "description": "Interdisciplinary collaboration, societal focus",
              "documents": ["Research Project List", "Collaboration MoUs"]},
    "4.1.3": {"name": "Research Output", "weight": 70, "ipo": "Outcome", 
              "description": "Publications, patents, Ph.D.s awarded",
              "documents": ["Publication List", "Patent Certificates", "Ph.D. Award Letters"]},
    "4.1.4": {"name": "Research Impact", "weight": 50, "ipo": "Impact", 
              "description": "Citations, peer recognition, industry funding",
              "documents": ["Citation Metrics", "Funding Agency Letters"]},
    
    # CRITERION 5: CO-CURRICULAR & EXTRA-CURRICULAR (4 metrics)
    "5.1.1": {"name": "EC/CC Policies", "weight": 15, "ipo": "Input", 
              "description": "Credit for EC/CC activities",
              "documents": ["Academic Policy Documents"]},
    "5.1.2": {"name": "Activity Process", "weight": 25, "ipo": "Process", 
              "description": "Incentivization, logistics, syllabus connection",
              "documents": ["Activity Reports", "Budget Allocations"]},
    "5.1.3": {"name": "Student Achievements", "weight": 20, "ipo": "Outcome", 
              "description": "Awards, recognition, talent discovery",
              "documents": ["Awards Won", "Student Achievements List"]},
    "5.1.4": {"name": "Holistic Development", "weight": 20, "ipo": "Impact", 
              "description": "Student representation, leadership",
              "documents": ["Student Leadership Records", "Satisfaction Surveys"]},
    
    # CRITERION 6: COMMUNITY ENGAGEMENT (4 metrics)
    "6.1.1": {"name": "Outreach Policies", "weight": 15, "ipo": "Input", 
              "description": "Curriculum-community linkage, NSS/NCC",
              "documents": ["Outreach Policy", "NSS/NCC Records"]},
    "6.1.2": {"name": "Engagement Process", "weight": 25, "ipo": "Process", 
              "description": "Social outreach, village adoption",
              "documents": ["Activity Reports", "Village Adoption Letters"]},
    "6.1.3": {"name": "Community Outcomes", "weight": 20, "ipo": "Outcome", 
              "description": "Student social responsibility",
              "documents": ["Volunteer Hours", "Community Feedback"]},
    "6.1.4": {"name": "Community Impact", "weight": 20, "ipo": "Impact", 
              "description": "Health, education, economic improvement",
              "documents": ["Impact Assessment Reports"]},
    
    # CRITERION 7: GREEN INITIATIVES (4 metrics)
    "7.1.1": {"name": "Sustainability Policies", "weight": 10, "ipo": "Input", 
              "description": "Green initiatives credit",
              "documents": ["Sustainability Policy"]},
    "7.1.2": {"name": "Green Processes", "weight": 20, "ipo": "Process", 
              "description": "Renewable energy, waste management",
              "documents": ["Energy Bills", "Waste Reports", "Green Audit"]},
    "7.1.3": {"name": "Environmental Outcomes", "weight": 15, "ipo": "Outcome", 
              "description": "Environmental orientation",
              "documents": ["Student Awareness Surveys"]},
    "7.1.4": {"name": "Environmental Impact", "weight": 15, "ipo": "Impact", 
              "description": "Carbon footprint reduction",
              "documents": ["Carbon Footprint Metrics"]},
    
    # CRITERION 8: GOVERNANCE AND ADMINISTRATION (4 metrics)
    "8.1.1": {"name": "Governance Framework", "weight": 15, "ipo": "Input", 
              "description": "Act, Statutes, Regulations, Policies",
              "documents": ["Institutional Act", "Statutes", "Policy Documents"]},
    "8.1.2": {"name": "Governance Process", "weight": 25, "ipo": "Process", 
              "description": "Implementation, e-Governance, grievance redressal",
              "documents": ["Compliance Reports", "e-Governance Records", "Grievance Data"]},
    "8.1.3": {"name": "Governance Outcomes", "weight": 20, "ipo": "Outcome", 
              "description": "Transparency, mission achievement",
              "documents": ["Governance Audit Reports"]},
    "8.1.4": {"name": "Governance Impact", "weight": 20, "ipo": "Impact", 
              "description": "Increased GER, institutional reputation",
              "documents": ["Enrollment Statistics", "NIRF Rankings"]},
    
    # CRITERION 9: INFRASTRUCTURE (4 metrics)
    "9.1.1": {"name": "Facility Inventory", "weight": 10, "ipo": "Input", 
              "description": "Land, buildings, labs, library, sports",
              "documents": ["Facility Inventory", "Geo-tagged Photos"]},
    "9.1.2": {"name": "Infrastructure Utilization", "weight": 15, "ipo": "Process", 
              "description": "Maintenance, usage, accessibility",
              "documents": ["Utilization Reports", "Maintenance Records"]},
    "9.1.3": {"name": "Infrastructure Availability", "weight": 10, "ipo": "Outcome", 
              "description": "Student-facility ratios",
              "documents": ["Facility Availability Metrics"]},
    "9.1.4": {"name": "Infrastructure Impact", "weight": 15, "ipo": "Impact", 
              "description": "Student/faculty satisfaction",
              "documents": ["Satisfaction Surveys"]},
    
    # CRITERION 10: FINANCIAL RESOURCES (4 metrics)
    "10.1.1": {"name": "Financial Resources", "weight": 20, "ipo": "Input", 
               "description": "Budget allocation, grants, CSR funds",
               "documents": ["Budget Documents", "Grant Letters"]},
    "10.1.2": {"name": "Financial Management", "weight": 25, "ipo": "Process", 
               "description": "Resource mobilization, financial systems",
               "documents": ["Audited Statements", "Financial Reports"]},
    "10.1.3": {"name": "Financial Health", "weight": 25, "ipo": "Outcome", 
               "description": "Income-expenditure balance",
               "documents": ["Financial Ratios"]},
    "10.1.4": {"name": "Financial Impact", "weight": 30, "ipo": "Impact", 
               "description": "Correlation with outcomes",
               "documents": ["Financial-Outcome Analysis"]}
}

GRADE_THRESHOLDS = {
    'A++': (95, 100), 'A+': (90, 94), 'A': (85, 89),
    'B++': (80, 84), 'B+': (75, 79), 'B': (70, 74),
    'C': (60, 69), 'D': (0, 59)
}
