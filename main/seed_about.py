from main.models import Profile, Skill, Milestone


# PROFILE
Profile.objects.create(

    name="Pawan Kumar",

    profession="Computer Engineer | Full Stack Developer | AI Enthusiast",

    short_bio="""
I'm a Computer Engineering graduate with a passion for transforming ideas into impactful digital solutions.

My expertise spans full-stack development, machine learning implementations, and cloud-native architectures.

What drives me is the intersection of technology and real-world problem solving.
""",

    hero_image="profile/default.png",

    resume="resume/default.pdf",

    github="https://github.com/connectspawan",

    linkedin="https://www.linkedin.com/in/connectspawan",

    instagram="https://www.instagram.com/melomaniac_pawan/",

    facebook="https://www.facebook.com/pawankumar.barnawal.501",

    email="connectspawan@gmail.com",

    footer_description="Building bridges between complex problems and elegant technical solutions",

    projects_completed=5,

    years_experience=1,

    technologies_used=10
)


# SKILLS
skills = [

    {
        "order": 1,
        "name": "Python",
        "percentage": 70
    },

    {
        "order": 2,
        "name": "JavaScript/Web Technology",
        "percentage": 80
    },

    {
        "order": 3,
        "name": "Machine Learning & AI",
        "percentage": 50
    },

    {
        "order": 4,
        "name": "Java",
        "percentage": 70
    }

]

for skill in skills:

    Skill.objects.create(
        order=skill["order"],
        name=skill["name"],
        percentage=skill["percentage"]
    )


# MILESTONES
milestones = [

    {
        "order": 1,

        "date": "April 2025",

        "title": "SSIP Grant Recipient",

        "subtitle": "₹2 Lakh Innovation Funding",

        "description":
        "Selected among Gujarat's most promising startups to receive SSIP's prestigious grant."
    },

    {
        "order": 2,

        "date": "March 2025",

        "title": "Code Unnati Finalist",

        "subtitle": "Top 3% among 830 Teams",

        "description":
        "Presented project at GTU before mentors and judges, gaining valuable experience in innovation and pitching."
    },

    {
        "order": 3,

        "date": "March 2025",

        "title": "EntrepreNaari 3.0",

        "subtitle": "Startup Pitch Competition",

        "description":
        "Presented startup idea to investors and judges, gaining exposure to entrepreneurship and business pitching."
    }

]

for milestone in milestones:

    Milestone.objects.create(
        order=milestone["order"],
        date=milestone["date"],
        title=milestone["title"],
        subtitle=milestone["subtitle"],
        description=milestone["description"]
    )


print("About Data Added Successfully")