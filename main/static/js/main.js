// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (window.innerWidth <= 768) {
                    navLinks.classList.remove('active');
                    menuToggle.classList.remove('active');
                }
            }
        });
    });
    
    // Header scroll effect
    window.addEventListener('scroll', function() {
        const header = document.querySelector('.header');
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Here you would typically send the form data to a server
            console.log('Form submitted:', { name, email, subject, message });
            
            // Show success message
            alert('Thank you for your message! I will get back to you soon.');
            
            // Reset form
            contactForm.reset();
        });
    }
});

// Contact form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Submit to Formspree
        const formData = new FormData(contactForm);
        try {
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (response.ok) {
                // Show success message
                showSuccessMessage("Thank you for your message! I will get back to you soon.");
                contactForm.reset();
            } else {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Form submission failed');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('There was a problem submitting your form. Please try again later.');
        }
    });
}

// Function to show success message
function showSuccessMessage(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'form-alert';
    alertDiv.textContent = message;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// Dark/Light Mode Toggle
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const icon = themeToggle.querySelector('i');
    
    // Check for saved user preference or use system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        document.body.classList.add('dark-mode');
        icon.classList.replace('fa-moon', 'fa-sun');
    }
    
    // Toggle theme on button click
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        
        if (document.body.classList.contains('dark-mode')) {
            icon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('theme', 'dark');
        } else {
            icon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('theme', 'light');
        }
    });
});


// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Function to animate counters
    function animateCounters() {
        const counters = document.querySelectorAll('.counter');
        const options = {
            threshold: 0.5,
            rootMargin: '0px 0px -100px 0px'
        };

        // Create Intersection Observer
        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = +counter.getAttribute('data-target');
                    const speed = +counter.getAttribute('data-speed') || 200;
                    const count = +counter.innerText.replace('+', '');
                    const increment = target / speed;

                    // Only animate if not already at target
                    if (count < target) {
                        const updateCounter = () => {
                            const currentCount = +counter.innerText.replace('+', '');
                            if (currentCount < target) {
                                counter.innerText = Math.ceil(currentCount + increment) + '+';
                                setTimeout(updateCounter, 1);
                            } else {
                                counter.innerText = target + '+';
                                counter.classList.add('animated');
                                setTimeout(() => {
                                    counter.classList.remove('animated');
                                }, 500);
                            }
                        };
                        updateCounter();
                    }
                    observer.unobserve(counter);
                }
            });
        }, options);

        // Observe all counters
        counters.forEach(counter => {
            observer.observe(counter);
        });
    }

    // Initialize counter animation
    animateCounters();
});

document.addEventListener('DOMContentLoaded', function() {
    const statItems = document.querySelectorAll('.hover-trigger');
    
    statItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            const counter = this.querySelector('.counter');
            if (counter.getAttribute('data-animated') === 'true') return;
            
            const target = +counter.getAttribute('data-target');
            const duration = 1000; // Animation duration in ms
            const startTime = Date.now();
            
            const updateCounter = () => {
                const elapsed = Date.now() - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const currentValue = Math.floor(progress * target);
                
                counter.textContent = currentValue + '+';
                
                if (progress < 1) {
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.setAttribute('data-animated', 'true');
                    counter.classList.add('animated');
                    setTimeout(() => {
                        counter.classList.remove('animated');
                    }, 500);
                }
            };
            
            updateCounter();
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const skills = document.querySelectorAll(".skill-progress");

    skills.forEach(skill => {
        const width = skill.getAttribute("data-width");
        skill.style.width = width;

        // Set percentage value to corresponding span
        const info = skill.closest(".skill-item").querySelector(".skill-info span:last-child");
        if (info) info.textContent = width;
    });
});
