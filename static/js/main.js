// Portfolio JavaScript Functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initNavigation();
    initAnimations();
    initSkillBars();
    initContactForm();
    initAdminFunctions();
    initLandingPageEffects();
    initAdvancedEffects();
    initLoadingScreen();
    
    console.log('Portfolio JavaScript loaded successfully!');
});

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
    // Typing effect for hero title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle && heroTitle.textContent.includes('Deepak Yadav')) {
        typeWriter(heroTitle);
    }
    
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

// Counter animation for stats
function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-number');
    const observerOptions = {
        threshold: 0.5
    };
    
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    counters.forEach(counter => counterObserver.observe(counter));
}

function animateCounter(element) {
    const target = parseInt(element.textContent.replace(/\D/g, ''));
    const suffix = element.textContent.replace(/[\d]/g, '');
    let current = 0;
    const increment = target / 50;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target + suffix;
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current) + suffix;
        }
    }, 40);
}

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
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.skill-card, .project-card, .stats-item');
    animateElements.forEach(el => observer.observe(el));
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

// Theme toggle functionality
function initThemeToggle() {
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
    
    // Click counter easter egg
    let clickCount = 0;
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.addEventListener('click', () => {
            clickCount++;
            if (clickCount === 7) {
                heroTitle.style.background = 'linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3, #54a0ff)';
                heroTitle.style.backgroundSize = '400% 400%';
                heroTitle.style.animation = 'rainbow 2s ease infinite';
                heroTitle.style.webkitBackgroundClip = 'text';
                heroTitle.style.webkitTextFillColor = 'transparent';
                
                // Add rainbow animation
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes rainbow {
                        0% { background-position: 0% 50%; }
                        50% { background-position: 100% 50%; }
                        100% { background-position: 0% 50%; }
                    }
                `;
                document.head.appendChild(style);
                
                clickCount = 0;
            }
        });
    }
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

// Utility functions
function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('.alert-container') || document.body;
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.insertBefore(alert, alertContainer.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (alert.parentNode) {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }
    }, 5000);
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
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

// Back to top functionality
function createBackToTopButton() {
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.className = 'btn btn-primary position-fixed';
    backToTop.style.cssText = `
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        display: none;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    `;
    
    document.body.appendChild(backToTop);
    
    // Show/hide based on scroll position
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });
    
    // Scroll to top on click
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Initialize back to top button
createBackToTopButton();

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