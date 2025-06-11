// Portfolio JavaScript Functionality - Modern Enhancement

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Portfolio JavaScript starting...');
    
    // Initialize theme toggle first (most important)
    initThemeToggle();
    
    // Initialize other functionality    initNavigation();
    initAnimations();
    initSkillBars();
    initContactForm();
    initAdminFunctions();
    initLandingPageEffects();
    initAdvancedEffects();
    initLoadingScreen();
    initModernEffects();
    initParticleBackground();
    initTypingAnimation(); // REACTIVATED: For hero subtitle typing effect only
    initCounterAnimation();
    initMouseTrail();
    initFAB();
    initProgressiveLoading();
    
    console.log('✅ Portfolio JavaScript loaded successfully!');
});

// Modern Theme Toggle System
function initThemeToggle() {
    console.log('🎨 Initializing theme toggle...');
    const html = document.documentElement;
    
    // Check for saved theme or default to light
    const savedTheme = localStorage.getItem('portfolio-theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    console.log('💾 Loaded theme:', savedTheme);
    
    // Update button icon to match current theme
    updateThemeToggleIcon(savedTheme);
    
    // The onclick handler in HTML will handle the clicking
    // This function just ensures the initial theme is set correctly
    console.log('✅ Theme toggle initialized with', savedTheme, 'theme');
}

// Theme toggle function called by the button onclick
function toggleTheme() {
    console.log('🎨 Toggling theme...');
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    // Add transition class for smooth animation
    html.classList.add('theme-transitioning');
    
    // Change theme
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('portfolio-theme', newTheme);
    
    console.log('🔄 Theme changed from', currentTheme, 'to', newTheme);
    
    // Remove transition class after animation completes
    setTimeout(() => {
        html.classList.remove('theme-transitioning');
    }, 300);
    
    // Update button icon
    updateThemeToggleIcon(newTheme);
}

// Update theme toggle button icon
function updateThemeToggleIcon(theme) {
    const toggleButton = document.querySelector('.theme-toggle-btn');
    if (toggleButton) {
        const icon = toggleButton.querySelector('i');
        if (icon) {
            icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }
    }
}

// Modern Intersection Observer for Animations
function initModernEffects() {
    // Animated skill bars
    const skillBars = document.querySelectorAll('.skill-progress-bar');
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const width = bar.getAttribute('data-width') || '0%';
                bar.style.width = width;
            }
        });
    }, { threshold: 0.1 });
    
    skillBars.forEach(bar => skillObserver.observe(bar));
    
    // Stagger animation for cards
    const cards = document.querySelectorAll('.card-modern, .skill-card, .project-card');
    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
            }
        });
    }, { threshold: 0.1 });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        cardObserver.observe(card);
    });
      // Parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallax = scrolled * 0.5;
            heroSection.style.transform = `translateY(${parallax}px)`;
        });
    }
      // DISABLED: Typing effect for hero title to make heading static
    // const heroTitle = document.querySelector('.hero-title');
    // if (heroTitle && !heroTitle.dataset.typed) {
    //     const originalText = heroTitle.textContent;
    //     heroTitle.textContent = '';
    //     heroTitle.dataset.typed = 'true';
    //     
    //     let i = 0;
    //     const typeWriter = () => {
    //         if (i < originalText.length) {
    //             heroTitle.textContent += originalText.charAt(i);
    //             i++;
    //             setTimeout(typeWriter, 100);
    //         }
    //     };
    //     
    //     setTimeout(typeWriter, 1000);
    // }
    
    // Scroll progress indicator
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            scrollProgress.style.width = scrollPercent + '%';
        });
    }
    
    // Animated counters for stats
    const counters = document.querySelectorAll('.stat-counter');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-target') || counter.textContent);
                const increment = target / 50;
                let current = 0;
                
                const updateCounter = () => {
                    if (current < target) {
                        current += increment;
                        counter.textContent = Math.ceil(current);
                        setTimeout(updateCounter, 20);
                    } else {
                        counter.textContent = target;
                    }
                };
                
                updateCounter();
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.1 });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

// Enhanced Navigation functionality
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add active class to current page
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
    
    // Enhanced navbar scroll effect
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled', 'scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled', 'scrolled');
            }
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Landing page specific effects
function initLandingPageEffects() {
    // DISABLED: Typing effect for hero title to make heading static
    // const heroTitle = document.querySelector('.hero-title');
    // if (heroTitle && heroTitle.textContent.includes('Deepak Yadav')) {
    //     typeWriter(heroTitle);
    // }
    
    // Parallax effect for floating shapes
    initParallaxShapes();
    
    // Counter animation for stats
    initCounterAnimation();
    
    // Tilt effect for feature cards
    initTiltEffect();
}

// Typewriter effect
function typeWriter(element) {
    const text = element.textContent;
    element.textContent = '';
    element.style.opacity = '1';
    
    let i = 0;
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, 50);
        }
    }
    type();
}

// Parallax shapes effect
function initParallaxShapes() {
    document.addEventListener('mousemove', function(e) {
        const shapes = document.querySelectorAll('.shape');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        
        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 0.03;
            const x = (mouseX - 0.5) * speed * 30;
            const y = (mouseY - 0.5) * speed * 30;
            shape.style.transform = `translate(${x}px, ${y}px)`;
        });
    });
}

// Counter animation for stats - see complete implementation below

// Tilt effect for cards
function initTiltEffect() {
    const cards = document.querySelectorAll('.feature-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function(e) {
            card.style.transition = 'transform 0.1s';
        });
        
        card.addEventListener('mousemove', function(e) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
        });
        
        card.addEventListener('mouseleave', function(e) {
            card.style.transition = 'transform 0.3s';
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
        });
    });
}

// Animation functionality
function initAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all fade-in elements including CTA section
    const animateElements = document.querySelectorAll('.fade-in, .skill-card, .project-card, .stats-item');
    animateElements.forEach(el => observer.observe(el));
    
    console.log('✅ Animation observer initialized for', animateElements.length, 'elements');
}

// Skill progress bars
function initSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress-bar');
    
    if (skillBars.length > 0) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const percentage = bar.getAttribute('data-percentage') || '0';
                    
                    // Animate the progress bar
                    setTimeout(() => {
                        bar.style.width = percentage + '%';
                    }, 300);
                    
                    observer.unobserve(bar);
                }
            });
        }, { threshold: 0.5 });
        
        skillBars.forEach(bar => observer.observe(bar));
    }
}

// Contact form functionality
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const submitButton = contactForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            // Show loading state
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner"></span> Sending...';
            
            // Submit form
            fetch('/contact', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('Thank you! Your message has been sent successfully.', 'success');
                    contactForm.reset();
                } else {
                    showAlert('Sorry, there was an error sending your message. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('Sorry, there was an error sending your message. Please try again.', 'error');
            })
            .finally(() => {
                // Reset button
                submitButton.disabled = false;
                submitButton.textContent = originalText;
            });
        });
    }
}

// Admin panel functionality
function initAdminFunctions() {
    // Auto-hide alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert.parentNode) {
                alert.style.opacity = '0';
                setTimeout(() => {
                    alert.remove();
                }, 300);
            }
        }, 5000);
    });
    
    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete, .delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
                e.preventDefault();
            }
        });
    });
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    
                    // Remove invalid class on input
                    field.addEventListener('input', function() {
                        if (this.value.trim()) {
                            this.classList.remove('is-invalid');
                        }
                    });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showAlert('Please fill in all required fields.', 'error');
            }
        });
    });
}

// Additional interactive features for landing page
function initAdvancedEffects() {
    // Particle system for hero background
    createParticleSystem();
    
    // Progressive loading of sections
    initProgressiveLoading();
    
    // Dynamic color themes
    initThemeToggle();
    
    // Performance monitoring
    monitorPerformance();
    
    // Easter eggs and hidden features
    initEasterEggs();
}

// Particle system for visual appeal
function createParticleSystem() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;
    
    const particleContainer = document.createElement('div');
    particleContainer.className = 'particle-container';
    particleContainer.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 1;
    `;
    
    heroSection.appendChild(particleContainer);
    
    // Create floating particles
    for (let i = 0; i < 20; i++) {
        createParticle(particleContainer);
    }
}

function createParticle(container) {
    const particle = document.createElement('div');
    const size = Math.random() * 4 + 2;
    const animationDuration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;
    
    particle.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        left: ${Math.random() * 100}%;
        top: ${Math.random() * 100}%;
        animation: floatParticle ${animationDuration}s infinite linear;
        animation-delay: ${delay}s;
    `;
    
    container.appendChild(particle);
    
    // Add CSS animation for particles
    if (!document.getElementById('particle-styles')) {
        const style = document.createElement('style');
        style.id = 'particle-styles';
        style.textContent = `
            @keyframes floatParticle {
                0% {
                    transform: translateY(100vh) rotate(0deg);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-10vh) rotate(360deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

// Progressive section loading for performance
function initProgressiveLoading() {
    const sections = document.querySelectorAll('section');
    const loadingObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-loaded');
                // Trigger any section-specific animations
                triggerSectionAnimations(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    sections.forEach(section => {
        section.classList.add('section-loading');
        loadingObserver.observe(section);
    });
}

function triggerSectionAnimations(section) {
    const cards = section.querySelectorAll('.feature-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.animation = `fadeInUp 0.6s ease-out forwards`;
        }, index * 100);
    });
}

// Enhanced theme detection and monitoring
function initSystemThemeDetection() {
    // Auto-detect system theme preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Listen for theme changes
    prefersDark.addEventListener('change', (e) => {
        updateTheme(e.matches ? 'dark' : 'light');
    });
    
    // Initialize theme
    updateTheme(prefersDark.matches ? 'dark' : 'light');
}

function updateTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // Update hero gradient for dark theme
    const heroSection = document.querySelector('.hero-section');
    if (heroSection && theme === 'dark') {
        heroSection.style.background = 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)';
    }
}

// Performance monitoring
function monitorPerformance() {
    // Monitor page load performance
    window.addEventListener('load', () => {
        const perfData = performance.getEntriesByType('navigation')[0];
        if (perfData.loadEventEnd - perfData.loadEventStart > 3000) {
            console.warn('Page loading slower than expected');
            // Could implement performance optimizations here
        }
    });
    
    // Monitor scroll performance
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            // Optimize animations based on scroll performance
            optimizeScrollAnimations();
        }, 150);
    });
}

function optimizeScrollAnimations() {
    const isSlowDevice = navigator.hardwareConcurrency < 4;
    if (isSlowDevice) {
        document.documentElement.style.setProperty('--animation-duration', '0.2s');
    }
}

// Easter eggs and hidden features
function initEasterEggs() {
    // Konami code easter egg
    let konamiCode = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
    let konamiIndex = 0;
    
    document.addEventListener('keydown', (e) => {
        if (e.keyCode === konamiCode[konamiIndex]) {
            konamiIndex++;
            if (konamiIndex === konamiCode.length) {
                activateEasterEgg();
                konamiIndex = 0;
            }
        } else {
            konamiIndex = 0;
        }
    });
    
    // DISABLED: Click counter easter egg to prevent dynamic title changes
    // let clickCount = 0;
    // const heroTitle = document.querySelector('.hero-title');
    // if (heroTitle) {
    //     heroTitle.addEventListener('click', () => {
    //         clickCount++;
    //         if (clickCount === 7) {
    //             heroTitle.style.background = 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3, #54a0ff)';
    //             heroTitle.style.backgroundSize = '400% 400%';
    //             heroTitle.style.animation = 'rainbow 2s ease infinite';
    //             heroTitle.style.webkitBackgroundClip = 'text';
    //             heroTitle.style.webkitTextFillColor = 'transparent';
    //             
    //             // Add rainbow animation
    //             const style = document.createElement('style');
    //             style.textContent = `
    //                 @keyframes rainbow {
    //                     0% { background-position: 0% 50%; }
    //                     50% { background-position: 100% 50%; }
    //                     100% { background-position: 0% 50%; }
    //                 }
    //             `;
    //             document.head.appendChild(style);
    //             
    //             clickCount = 0;
    //         }
    //     });
    // }
}

function activateEasterEgg() {
    // Create confetti effect
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57'];
    for (let i = 0; i < 50; i++) {
        createConfetti(colors[Math.floor(Math.random() * colors.length)]);
    }
    
    // Show secret message
    const message = document.createElement('div');
    message.innerHTML = '🎉 You found the secret! 🎉<br>Thanks for exploring!';
    message.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 20px 40px;
        border-radius: 15px;
        font-size: 1.2rem;
        text-align: center;
        z-index: 10000;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        animation: pulse 0.5s ease-in-out;
    `;
    
    document.body.appendChild(message);
    
    setTimeout(() => {
        message.remove();
    }, 3000);
}

function createConfetti(color) {
    const confetti = document.createElement('div');
    confetti.style.cssText = `
        position: fixed;
        width: 10px;
        height: 10px;
        background: ${color};
        left: ${Math.random() * window.innerWidth}px;
        top: -10px;
        z-index: 9999;
        animation: confettiFall ${Math.random() * 2 + 2}s linear forwards;
        transform: rotate(${Math.random() * 360}deg);
    `;
    
    document.body.appendChild(confetti);
    
    // Add confetti animation
    if (!document.getElementById('confetti-styles')) {
        const style = document.createElement('style');
        style.id = 'confetti-styles';
        style.textContent = `
            @keyframes confettiFall {
                to {
                    transform: translateY(${window.innerHeight + 10}px) rotate(720deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    setTimeout(() => confetti.remove(), 4000);
}

// Loading screen management
function initLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    
    // Hide loading screen when page is fully loaded
    window.addEventListener('load', () => {
        setTimeout(() => {
            if (loadingScreen) {
                loadingScreen.classList.add('loading-hidden');
                setTimeout(() => {
                    loadingScreen.remove();
                }, 500);
            }
            
            // Trigger entrance animations
            triggerEntranceAnimations();
        }, 1000); // Show loading for at least 1 second for better UX
    });
    
    // Fallback: hide loading screen after 5 seconds maximum
    setTimeout(() => {
        if (loadingScreen) {
            loadingScreen.classList.add('loading-hidden');
            setTimeout(() => {
                loadingScreen.remove();
            }, 500);
        }
    }, 5000);
}

function triggerEntranceAnimations() {
    // Animate hero elements
    const heroElements = document.querySelectorAll('.hero-content > *');
    heroElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        setTimeout(() => {
            element.style.transition = 'all 0.8s cubic-bezier(0.25, 0.8, 0.25, 1)';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200);
    });
    
    // Animate hero image
    const heroImage = document.querySelector('.hero-image');
    if (heroImage) {
        heroImage.style.opacity = '0';
        heroImage.style.transform = 'scale(0.8) rotateY(180deg)';
        setTimeout(() => {
            heroImage.style.transition = 'all 1s cubic-bezier(0.25, 0.8, 0.25, 1)';
            heroImage.style.opacity = '1';
            heroImage.style.transform = 'scale(1) rotateY(0deg)';
        }, 800);
    }
}

// Modern Particle Background Effect
function initParticleBackground() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;
    
    // Create particle container
    const particleContainer = document.createElement('div');
    particleContainer.className = 'particle-container';
    particleContainer.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    `;
    heroSection.appendChild(particleContainer);
    
    // Create floating particles
    for (let i = 0; i < 50; i++) {
        createParticle(particleContainer);
    }
    
    function createParticle(container) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        const size = Math.random() * 4 + 1;
        const x = Math.random() * 100;
        const duration = Math.random() * 20 + 10;
        const delay = Math.random() * 20;
        
        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: rgba(255, 255, 255, ${Math.random() * 0.5 + 0.2});
            border-radius: 50%;
            left: ${x}%;
            animation: floatUp ${duration}s linear infinite;
            animation-delay: ${delay}s;
        `;
        
        container.appendChild(particle);
        
        // Remove and recreate particle when animation ends
        setTimeout(() => {
            particle.remove();
            createParticle(container);
        }, (duration + delay) * 1000);
    }
}

// Enhanced Typing Animation
function initTypingAnimation() {
    const typingElement = document.querySelector('.typing-text');
    if (!typingElement) return;
    
    const phrases = [
        'Full Stack Developer',
        'Software Engineer',
        'Problem Solver',
        'Tech Enthusiast'
    ];
    
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    
    function type() {
        const currentPhrase = phrases[phraseIndex];
        
        if (isDeleting) {
            typingElement.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingElement.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
        }
        
        let typeSpeed = isDeleting ? 50 : 100;
        
        if (!isDeleting && charIndex === currentPhrase.length) {
            typeSpeed = 2000; // Pause at end
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            typeSpeed = 500; // Pause before next phrase
        }
        
        setTimeout(type, typeSpeed);
    }
    
    type();
}

// Smooth Number Counting Animation
function initCounterAnimation() {
    const counters = document.querySelectorAll('[data-count]');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-count'));
                let current = 0;
                const increment = target / 100;
                const duration = 2000;
                const stepTime = duration / 100;
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    counter.textContent = Math.floor(current);
                }, stepTime);
                
                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => counterObserver.observe(counter));
}

// Mouse Trail Effect
function initMouseTrail() {
    const trail = [];
    const trailLength = 20;
    
    for (let i = 0; i < trailLength; i++) {
        const dot = document.createElement('div');
        dot.className = 'trail-dot';
        dot.style.cssText = `
            position: fixed;
            width: 4px;
            height: 4px;
            background: var(--primary-color);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            opacity: ${1 - i / trailLength};
            transition: all 0.1s ease;
        `;
        document.body.appendChild(dot);
        trail.push(dot);
    }
    
    let mouseX = 0, mouseY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });
    
    function updateTrail() {
        for (let i = trail.length - 1; i > 0; i--) {
            trail[i].style.left = trail[i - 1].style.left;
            trail[i].style.top = trail[i - 1].style.top;
        }
        trail[0].style.left = mouseX + 'px';
        trail[0].style.top = mouseY + 'px';
        
        requestAnimationFrame(updateTrail);
    }
    
    updateTrail();
}

// Floating Action Button functionality
function initFAB() {
    const fabMain = document.getElementById('fabMain');
    const backToTop = document.getElementById('backToTop');
    
    if (fabMain) {
        fabMain.addEventListener('click', function() {
            // Create quick action menu
            showQuickActionMenu();
        });
    }
    
    // Back to top functionality
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.style.display = 'flex';
                backToTop.style.alignItems = 'center';
                backToTop.style.justifyContent = 'center';
            } else {
                backToTop.style.display = 'none';
            }
        });
        
        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
}

function showQuickActionMenu() {
    const menu = document.createElement('div');
    menu.className = 'quick-action-menu';
    menu.style.cssText = `
        position: fixed;
        bottom: 100px;
        right: 30px;
        background: var(--bg-primary);
        border: 1px solid var(--border-color, rgba(0, 0, 0, 0.1));
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        padding: 16px;
        z-index: 1001;
        min-width: 200px;
        animation: slideInUp 0.3s ease-out;
        color: var(--text-primary);
    `;
    
    const actions = [
        { icon: 'fas fa-envelope', text: 'Contact Me', action: () => window.location.href = '/contact' },
        { icon: 'fas fa-download', text: 'Download CV', action: () => showToast('CV download will be available soon!') },
        { icon: 'fas fa-share', text: 'Share Portfolio', action: () => sharePortfolio() },
        { icon: 'fas fa-moon', text: 'Toggle Theme', action: () => document.getElementById('themeToggle').click() }
    ];
    
    actions.forEach(action => {
        const item = document.createElement('div');
        item.style.cssText = `
            display: flex;
            align-items: center;
            padding: 12px;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.2s ease;
            margin-bottom: 4px;
        `;
        item.innerHTML = `
            <i class="${action.icon}" style="margin-right: 12px; width: 20px;"></i>
            <span>${action.text}</span>
        `;
          item.addEventListener('mouseenter', () => {
            // Use theme-aware hover color
            const isDark = document.body.classList.contains('dark-theme') || 
                          document.documentElement.classList.contains('dark-theme');
            item.style.backgroundColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.05)';
        });
        item.addEventListener('mouseleave', () => {
            item.style.backgroundColor = 'transparent';
        });
        item.addEventListener('click', () => {
            action.action();
            menu.remove();
        });
        
        menu.appendChild(item);
    });
    
    // Close menu when clicking outside
    setTimeout(() => {
        document.addEventListener('click', function closeMenu(e) {
            if (!menu.contains(e.target) && e.target.id !== 'fabMain') {
                menu.remove();
                document.removeEventListener('click', closeMenu);
            }
        });
    }, 100);
    
    document.body.appendChild(menu);
}

function sharePortfolio() {
    if (navigator.share) {
        navigator.share({
            title: 'Deepak Yadav - Portfolio',
            text: 'Check out my portfolio showcasing modern web development skills!',
            url: window.location.href
        });
    } else {
        // Fallback for browsers that don't support Web Share API
        navigator.clipboard.writeText(window.location.href).then(() => {
            showToast('Portfolio link copied to clipboard!', 'success');
        });
    }
}

// Modern toast notification system
function showToast(message, type = 'info', duration = 5000) {
    const toastContainer = document.getElementById('toastContainer') || document.body;
    
    const toast = document.createElement('div');
    toast.className = 'toast-modern';
    
    const iconMap = {
        success: 'fas fa-check-circle',
        error: 'fas fa-exclamation-circle',
        warning: 'fas fa-exclamation-triangle',
        info: 'fas fa-info-circle'
    };
    
    const colorMap = {
        success: '#10b981',
        error: '#ef4444',
        warning: '#f59e0b',
        info: '#3b82f6'
    };
    
    toast.style.borderLeft = `4px solid ${colorMap[type]}`;
    toast.innerHTML = `
        <div style="display: flex; align-items: center;">
            <i class="${iconMap[type]}" style="color: ${colorMap[type]}; margin-right: 12px;"></i>
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" style="
                background: none;
                border: none;
                font-size: 18px;
                margin-left: auto;
                padding-left: 12px;
                cursor: pointer;
                opacity: 0.7;
            ">&times;</button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    
    // Auto remove after duration
    setTimeout(() => {
        if (toast.parentElement) {
            toast.style.animation = 'slideOutRight 0.3s ease-in';
            setTimeout(() => toast.remove(), 300);
        }
    }, duration);
}

// Enhanced scroll animations
function initEnhancedScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                
                // Add different animation classes based on element type
                if (element.classList.contains('stat-number')) {
                    element.style.animation = 'countUp 2s ease-out';
                } else if (element.classList.contains('skill-bar')) {
                    const width = element.getAttribute('data-width') || '0%';
                    element.style.width = width;
                } else {
                    element.style.animation = 'fadeInUp 0.8s ease-out forwards';
                }
                
                observer.unobserve(element);
            }
        });
    }, observerOptions);
    
    // Observe all animatable elements
    const animatableElements = document.querySelectorAll('.fade-in, .stat-number, .skill-bar, .card-modern');
    animatableElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        observer.observe(el);
    });
}

// Smooth page transitions
function initPageTransitions() {
    const links = document.querySelectorAll('a[href^="/"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.hostname === window.location.hostname) {
                e.preventDefault();
                
                // Add page transition effect
                document.body.style.opacity = '0.8';
                document.body.style.transform = 'scale(0.98)';
                document.body.style.transition = 'all 0.3s ease';
                
                setTimeout(() => {
                    window.location.href = this.href;
                }, 300);
            }
        });
    });
}

// Enhanced performance monitoring
function initPerformanceOptimizations() {
    // Lazy load images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Preload critical resources
    const criticalResources = [
        '/static/css/style.css',
        '/static/js/main.js'
    ];
    
    criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = resource;
        link.as = resource.endsWith('.css') ? 'style' : 'script';
        document.head.appendChild(link);
    });
}

// Analytics and tracking (placeholder for future implementation)
function initAnalytics() {
    // Track page views
    if (typeof gtag === 'function') {
        gtag('config', 'GA_MEASUREMENT_ID', {
            page_title: document.title,
            page_location: window.location.href
        });
    }
    
    // Track button clicks
    document.querySelectorAll('a, button').forEach(element => {
        element.addEventListener('click', function() {
            const text = this.textContent.trim();
            const href = this.href || '';
            
            if (typeof gtag === 'function' && text) {
                gtag('event', 'click', {
                    event_category: 'engagement',
                    event_label: text,
                    value: href
                });
            }
        });
    });
}

// Error handling
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    
    // Optional: Send error to logging service
    // sendErrorToLoggingService(e.error);
});

// Service Worker registration (for future PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('ServiceWorker registration successful');
            })
            .catch(error => {
                console.log('ServiceWorker registration failed');
            });
    });
}