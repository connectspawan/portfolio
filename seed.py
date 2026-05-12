import os
import django

# Apne project ka settings module yahan set karein
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

# Milestone model ko bhi yahan import kar liya hai
from main.models import Project, Profile, Milestone 

def seed_profile():
    print("Seeding profile data...")
    profile_data = {
        "name": "Pawan Kumar",
        "profession": "Computer Engineer | Full Stack Developer | AI Enthusiast",
        "email": "connectspawan@gmail.com",
        "phone": "+91-92342 72087 | +977-98142 00113",
        "location": "Nepal",
        "google_map": "https://maps.google.com/?q=Nepal", 
        "github": "https://github.com/connectspawan",
        "linkedin": "https://www.linkedin.com/in/connectspawan",
        "instagram": "https://www.instagram.com/melomaniac_pawan/",
        "facebook": "https://www.facebook.com/pawankumar.barnawal.501",
        "short_bio": "Building bridges between complex problems and elegant technical solutions.\n\nI'm a Computer Engineering graduate with a passion for transforming ideas into impactful digital solutions.\n\nMy expertise spans full-stack development, machine learning implementations, and cloud-native architectures.\n\nWhat drives me is the intersection of technology and real-world problem solving.",
        "footer_description": "Building bridges between complex problems and elegant technical solutions.",
        "projects_completed": 13,
        "years_experience": 2, 
        "technologies_used": 15, 
    }

    if not Profile.objects.exists():
        Profile.objects.create(**profile_data)
        print("Successfully created your Profile!")
    else:
        Profile.objects.filter(id=1).update(**profile_data)
        print("Profile data already exists. Updated with latest seed data.")

def seed_milestones():
    print("\nSeeding milestones data...")
    milestones_data = [
        {
            "order": 1,
            "date": "March 2025",
            "title": "Code Unnati Finalist",
            "subtitle": "Top 3% among 830 Teams",
            "description": "Presented project at GTU before mentors and judges, gaining valuable experience in innovation and pitching."
        },
        {
            "order": 2,
            "date": "March 2025",
            "title": "EntrepreNaari 3.0",
            "subtitle": "Startup Pitch Competition",
            "description": "Presented startup idea to investors and judges, gaining exposure to entrepreneurship and business pitching."
        },
        {
            "order": 3,
            "date": "April 2025",
            "title": "SSIP Grant Recipient",
            "subtitle": "2 Lakh Innovation Funding",
            "description": "Selected among Gujarat's most promising startups to receive SSIP's prestigious grant."
        },
        {
            "order": 4,
            "date": "September 2025",
            "title": "Best Model Award",
            "subtitle": "Hand Gesture Controlled Rocket Game",
            "description": "Won 1st Prize at University Engineer's Day 2025 for \"Gesture-Controlled Rocket Game\"."
        },
        {
            "order": 5,
            "date": "April 2026",
            "title": "Completed Internship",
            "subtitle": "Intern at Shreeji Fintech Pvt Ltd",
            "description": "Worked at Intern and developed several websites and apps using Django and Flutter framework respectively."
        }
    ]

    for data in milestones_data:
        if not Milestone.objects.filter(title=data['title']).exists():
            Milestone.objects.create(**data)
            print(f"Successfully added Milestone: {data['title']}")
        else:
            print(f"Milestone already exists: {data['title']}")
            
    print("Milestone seeding complete!")

def seed_projects():
    print("\nSeeding projects data...")
    projects_data = [
        {
            "order": 1,
            "title": "Portfolio",
            "project_type": "Website",
            "description": "A glimpse into my learning journey and the projects I have built along the way.",
            "technologies": "HTML CSS JavaScript Django",
            "source_code": "",
            "live_demo": "https://connectspawan.netlify.app/",
        },
        {
            "order": 2,
            "title": "Photo Enhancer",
            "project_type": "AI/ML Project",
            "description": "An advanced image processing platform that uses convolutional neural networks (CNNs) to upscale low - resolution images while preserving critical details. The system achieves 40% better clarity than traditional methods.",
            "technologies": "Python ML ComputerVision EdgeAI Torch Streamlit",
            "source_code": "https://github.com/connectspawan/photo-enhancer",
            "live_demo": "https://github.com/connectspawan/photo-enhancer",
        },
        {
            "order": 3,
            "title": "Toon Quiz App",
            "project_type": "App",
            "description": "Developed an interactive cartoon-themed quiz application inspired by KBC for children. Implemented features including user authentication, dynamic question management, lifelines, and score tracking.",
            "technologies": "Flutter Django PostgreSQL REST-API",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 4,
            "title": "GyanSetu",
            "project_type": "App",
            "description": "Developed a full-stack learning platform consisting of a web application and mobile app for structured educational content delivery. Built Django backend APIs integrated with Flutter frontend for seamless user experience.",
            "technologies": "Flutter Django PostgreSQL REST-API",
            "source_code": "",
            "live_demo": "https://www.gyansetu.shreejifintech.com/",
        },
        {
            "order": 5,
            "title": "Wish2Chat",
            "project_type": "App",
            "description": "Built a festival-based content sharing application that provides Images, GIFs, Stickers, and Quotes. Developed backend services using Django and implemented REST APIs to fetch dynamic content into the mobile application.",
            "technologies": "Django Python Flutter SQLite",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 6,
            "title": "Government Job Portal",
            "project_type": "Website",
            "description": "Developed a full-stack Government Job Portal enabling users to search jobs based on state, qualification, and eligibility criteria. Built the web platform using Django and the mobile application using Flutter.",
            "technologies": "Django Python Flutter SQLite",
            "source_code": "",
            "live_demo": "https://www.jobportal.shreejifintech.com/",
        },
        {
            "order": 7,
            "title": "Shreeji FinTech",
            "project_type": "Website",
            "description": "Designed and developed the official corporate website for Shreeji FinTech to establish the company's professional digital presence. Built using Django for backend and integrated responsive front-end design.",
            "technologies": "Django Python HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://www.shreejifintech.com/",
        },
        {
            "order": 8,
            "title": "Gesture-Controlled Rocket Game",
            "project_type": "AI/ML Project",
            "description": "Built an interactive space-shooter game controlled entirely by hand gestures using a webcam. Integrated MediaPipe Hands and OpenCV for real-time gesture recognition, and Pygame for rendering gameplay.",
            "technologies": "Python Streamlit MediaPipe OpenCV Pygame",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 9,
            "title": "Quick BMI",
            "project_type": "Website",
            "description": "Platform to calculate Body Mass Index accurately and understand health status.",
            "technologies": "HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://quickbmi.netlify.app/",
        },
        {
            "order": 10,
            "title": "COCRewards",
            "project_type": "Website",
            "description": "Clash Rewards Central, your ultimate hub for unlocking exclusive rewards in Clash of Clans.",
            "technologies": "HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://cocrewards.netlify.app/",
        },
        {
            "order": 11,
            "title": "Crook Catcher",
            "project_type": "AI/ML Project",
            "description": "An IoT-based security system that analyzes movement patterns using onboard sensors and machine learning algorithms.",
            "technologies": "Python OpenCV YOLO EdgeAI",
            "source_code": "https://github.com/connectspawan/crookCatcher",
            "live_demo": "",
        },
        {
            "order": 12,
            "title": "EmpowerAbility",
            "project_type": "AI/ML Project",
            "description": "An assistive technology platform combining computer vision and IoT to detect mobility impairments and automatically adjust environments.",
            "technologies": "Python ML ComputerVision Mediapipe YOLO Torch Streamlit",
            "source_code": "https://github.com/connectspawan/EmpowerAbility",
            "live_demo": "https://drive.google.com/file/d/1u5Gn2UtXT-O85qaScmxrrBcZw_0SHTFm/view",
        },
        {
            "order": 13,
            "title": "Elite Digitals",
            "project_type": "Website",
            "description": "Developed a premium digital agency website showcasing services including app development, website development, graphic design, and content creation. Built using Django backend with responsive premium UI/UX.",
            "technologies": "Django Python HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://elite-digitals.onrender.com/",
        }
    ]

    for data in projects_data:
        if not Project.objects.filter(title=data['title']).exists():
            Project.objects.create(
                order=data['order'],
                title=data['title'],
                project_type=data['project_type'],
                description=data['description'],
                technologies=data['technologies'],
                source_code=data['source_code'],
                live_demo=data['live_demo'],
                # Image blank hai abhi
            )
            print(f"Successfully added: {data['title']}")
        else:
            print(f"Already exists: {data['title']}")
            
    print("Project seeding complete!")

if __name__ == '__main__':
    # Teeno cheezein ek saath chalengi: Profile -> Milestones -> Projects
    seed_profile()
    seed_milestones()
    seed_projects()