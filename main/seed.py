from main.models import Project


projects = [

     # EmpowerAbility
    {
        "title": "EmpowerAbility",

        "description":
        "An assistive technology platform combining computer vision and IoT to detect mobility impairments and automatically adjust environments.",

        "technologies":
        "Python ML ComputerVision Mediapipe YOLO Torch Streamlit",

        "source_code":
        "https://github.com/connectspawan/EmpowerAbility",

        "live_demo":
        "https://drive.google.com/file/d/1u5Gn2UtXT-O85qaScmxrrBcZw_0SHTFm/view"
    },

    # Crook Catcher
    {
        "title": "Crook Catcher",

        "description":
        "An IoT-based security system that analyzes movement patterns using onboard sensors and machine learning algorithms.",

        "technologies":
        "Python OpenCV YOLO EdgeAI",

        "source_code":
        "https://github.com/connectspawan/crookCatcher",

        "live_demo":
        ""
    },

    # Portfolio Website
    {
        "title": "Portfolio",

        "description":
        "A glimpse into my learning journey and the projects I’ve built along the way.",

        "technologies":
        "HTML CSS JavaScript Django",

        "source_code":
        "",

        "live_demo":
        "https://connectspawan.netlify.app/"
    },

    # Quick BMI
    {
        "title": "Quick BMI",

        "description":
        "Platform to calculate Body Mass Index accurately and understand health status.",

        "technologies":
        "HTML CSS JavaScript",

        "source_code":
        "",

        "live_demo":
        "https://quickbmi.netlify.app/"
    },

    # COCRewards
    {
        "title": "COCRewards",

        "description":
        "Clash Rewards Central, your ultimate hub for unlocking exclusive rewards in Clash of Clans.",

        "technologies":
        "HTML CSS JavaScript",

        "source_code":
        "",

        "live_demo":
        "https://cocrewards.netlify.app/"
    },

]


for item in projects:

    Project.objects.create(
        title=item["title"],
        description=item["description"],
        technologies=item["technologies"],
        source_code=item["source_code"],
        live_demo=item["live_demo"],
        image="projects/default.png"
    )


print("All Projects Added Successfully")