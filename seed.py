import os
import django

# Apne project ka settings module yahan set karein (agar aapke project ka naam 'portfolio' nahi hai, to ise change kar lein)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project  # 'main' ko apne app ke naam se replace karein agar alag hai

def seed_projects():
    projects_data = [
        {
            "order": 7,
            "title": "Gesture-Controlled Rocket Game",
            "project_type": "AI/ML Project",
            "description": "Built an interactive space-shooter game controlled entirely by hand gestures using a webcam. Integrated MediaPipe Hands and OpenCV for real-time gesture recognition, and Pygame for rendering gameplay. [cite: 69, 70]",
            "technologies": "Python Streamlit MediaPipe OpenCV Pygame",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 8,
            "title": "Shreeji FinTech",
            "project_type": "Website",
            "description": "Designed and developed the official corporate website for Shreeji FinTech to establish the company's professional digital presence. Built using Django for backend and integrated responsive front-end design. [cite: 61, 62]",
            "technologies": "Django Python HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://www.shreejifintech.com/",
        },
        {
            "order": 9,
            "title": "Government Job Portal",
            "project_type": "Website",
            "description": "Developed a full-stack Government Job Portal enabling users to search jobs based on state, qualification, and eligibility criteria. Built the web platform using Django and the mobile application using Flutter. [cite: 51, 52, 53]",
            "technologies": "Django Python Flutter SQLite",
            "source_code": "",
            "live_demo": "https://www.jobportal.shreejifintech.com/",
        },
        {
            "order": 10,
            "title": "Wish2Chat",
            "project_type": "App",
            "description": "Built a festival-based content sharing application that provides Images, GIFs, Stickers, and Quotes. Developed backend services using Django and implemented REST APIs to fetch dynamic content into the mobile application. [cite: 47]",
            "technologies": "Django Python Flutter SQLite",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 11,
            "title": "GyanSetu",
            "project_type": "App",
            "description": "Developed a full-stack learning platform consisting of a web application and mobile app for structured educational content delivery. Built Django backend APIs integrated with Flutter frontend for seamless user experience. [cite: 41, 42]",
            "technologies": "Flutter Django PostgreSQL REST-API",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 12,
            "title": "Toon Quiz App",
            "project_type": "App",
            "description": "Developed an interactive cartoon-themed quiz application inspired by KBC for children. Implemented features including user authentication, dynamic question management, lifelines, and score tracking. [cite: 35, 36]",
            "technologies": "Flutter Django PostgreSQL REST-API",
            "source_code": "",
            "live_demo": "",
        },
        {
            "order": 13,
            "title": "Elite Digitals",
            "project_type": "Website",
            "description": "Developed a premium digital agency website showcasing services including app development, website development, graphic design, and content creation. Built using Django backend with responsive premium UI/UX. [cite: 27, 28, 29]",
            "technologies": "Django Python HTML CSS JavaScript",
            "source_code": "",
            "live_demo": "https://elite-digitals.onrender.com/",
        }
    ]

    print("Seeding new projects...")
    for data in projects_data:
        # Check if project already exists to avoid duplicates
        if not Project.objects.filter(title=data['title']).exists():
            Project.objects.create(
                order=data['order'],
                title=data['title'],
                project_type=data['project_type'],
                description=data['description'],
                technologies=data['technologies'],
                source_code=data['source_code'],
                live_demo=data['live_demo'],
                # Image blank chhod rahe hain, admin se upload karni padegi
            )
            print(f"Successfully added: {data['title']}")
        else:
            print(f"Already exists: {data['title']}")
            
    print("Seeding complete!")

if __name__ == '__main__':
    seed_projects()