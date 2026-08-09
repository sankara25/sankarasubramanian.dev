import json

schema = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#website",
      "url": "https://sankara25.github.io/sankarasubramanian.dev/",
      "name": "Sankara Subramanian Portfolio",
      "alternateName": [
        "Sankara Subramanian – Senior Full Stack Developer",
        "sankarasubramanian.dev"
      ],
      "description": "Portfolio of S. Sankara Subramanian, Senior Full Stack Developer & AI Engineer with 10+ years building scalable digital platforms, backend systems, and AI workflows.",
      "publisher": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "inLanguage": "en-US"
    },
    {
      "@type": "ProfilePage",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#webpage",
      "url": "https://sankara25.github.io/sankarasubramanian.dev/",
      "name": "Sankara Subramanian – Senior Full Stack Developer | AI - Powered Full Stack Engineer",
      "isPartOf": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#website"
      },
      "breadcrumb": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#breadcrumb"
      },
      "inLanguage": "en-US",
      "description": "Portfolio of S. Sankara Subramanian, Senior Full Stack Developer with 10+ years building scalable digital experiences, backend APIs, automation workflows, and AI systems.",
      "mainEntity": {
        "@type": "Person",
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person",
        "name": "S. Sankara Subramanian",
        "alternateName": "Sankara Subramanian",
        "givenName": "Sankara",
        "familyName": "Subramanian",
        "url": "https://sankara25.github.io/sankarasubramanian.dev/",
        "image": "https://sankara25.github.io/sankarasubramanian.dev/sankara_subramanian.png",
        "jobTitle": "Senior Full Stack Developer",
        "description": "Senior Full Stack Developer and AI-Powered Engineer with 10+ years of experience designing and scaling backend systems using PHP (Laravel, CodeIgniter) and Python (FastAPI), modern frontend frameworks (React, Next.js), database optimization, cloud architecture (AWS, GCP), and AI/n8n automation workflows.",
        "email": "mailto:sankaranec@gmail.com",
        "telephone": "+919940768586",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Bangalore",
          "addressRegion": "Karnataka",
          "addressCountry": "India"
        },
        "sameAs": [
          "https://github.com/sankara25",
          "https://linkedin.com/in/sankara-subramanian",
          "https://x.com/sankaranec"
        ],
        "worksFor": [
          {
            "@type": "Organization",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#org-nexilra",
            "name": "Nexilra Technology",
            "location": {
              "@type": "PostalAddress",
              "addressLocality": "Bangalore",
              "addressRegion": "Karnataka",
              "addressCountry": "India"
            }
          },
          {
            "@type": "Organization",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#org-bosswallah",
            "name": "Bosswallah Technology Pvt Ltd",
            "alternateName": "Suvision Holdings Pvt Ltd",
            "location": {
              "@type": "PostalAddress",
              "addressLocality": "Bangalore",
              "addressRegion": "Karnataka",
              "addressCountry": "India"
            }
          },
          {
            "@type": "Organization",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#org-annap",
            "name": "Annap Interactive Solutions Pvt Ltd",
            "location": {
              "@type": "PostalAddress",
              "addressCountry": "India"
            }
          }
        ],
        "hasOccupation": [
          {
            "@type": "Occupation",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#occupation-nexilra",
            "name": "AI-Powered Full Stack Engineer",
            "occupationalCategory": "15-1254.00 - Web Developers",
            "description": "Developed and deployed scalable web applications (E-commerce, HRMS) using Laravel, Vue.js, MySQL, and Razorpay integration. Built a high-performance news platform using FastAPI and Next.js, ensuring fast response times and optimized user experience. Designed and implemented AI-powered automation workflows using n8n integrated with OpenAI and Gemini, reducing manual operations. Automated multi-channel communication workflows (Telegram, WhatsApp).",
            "skills": "Laravel, Vue.js, MySQL, Razorpay, FastAPI, Next.js, n8n, OpenAI, Google Gemini, Telegram, WhatsApp, AI Automation, GCP",
            "occupationLocation": {
              "@type": "AdministrativeArea",
              "name": "Bangalore, India"
            },
            "responsibilities": [
              "Developed and deployed scalable web applications (E-commerce, HRMS) using Laravel, Vue.js, MySQL, and Razorpay integration",
              "Built a high-performance news platform using FastAPI and Next.js, ensuring fast response times and optimized user experience",
              "Designed and implemented AI-powered automation workflows using n8n integrated with OpenAI and Gemini, reducing manual operations",
              "Automated multi-channel communication workflows (Telegram, WhatsApp) for intelligent conversational systems",
              "Leveraged AI-assisted development tools to accelerate delivery, improve code quality, and streamline documentation processes"
            ]
          },
          {
            "@type": "Occupation",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#occupation-bosswallah",
            "name": "Full Stack Engineer",
            "occupationalCategory": "15-1254.00 - Web Developers",
            "description": "Developed and scaled REST APIs using Laravel and FastAPI, improving system performance by up to 40%. Led migration of legacy CodeIgniter APIs to FastAPI, reducing response time and improving maintainability. Integrated Razorpay payment gateway and Zoho Sign workflows. Optimized SQL queries and implemented Redis caching. Developed automation workflows using n8n and MageAI, reducing manual operations by 50%+. Rebuilt frontend using React.js.",
            "skills": "Laravel, FastAPI, CodeIgniter, React.js, Razorpay, Zoho Sign, Redis, MySQL, MongoDB, n8n, MageAI, SMS/WhatsApp/Email APIs",
            "occupationLocation": {
              "@type": "AdministrativeArea",
              "name": "Bangalore, India"
            },
            "responsibilities": [
              "Developed and scaled REST APIs using Laravel and FastAPI, improving system performance by up to 40%",
              "Led migration of legacy CodeIgniter APIs to FastAPI, reducing response time and improving maintainability",
              "Integrated Razorpay payment gateway, enabling secure and seamless transactions across platforms",
              "Implemented Zoho Sign workflows, automating document processing and reducing manual effort",
              "Optimized SQL queries and implemented Redis caching, significantly improving performance and load times",
              "Built multi-channel communication systems (SMS, WhatsApp, email, push notifications)",
              "Developed automation workflows using n8n and MageAI, reducing manual operations by 50%+",
              "Rebuilt frontend using React.js, improving UI performance and user experience",
              "Supported applications used by thousands of active users with high availability"
            ]
          },
          {
            "@type": "Occupation",
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#occupation-annap",
            "name": "Senior Software Developer / Team Lead",
            "occupationalCategory": "15-1254.00 - Web Developers",
            "description": "Delivered 15+ enterprise applications (CRM, CMS, HRMS) using PHP, CodeIgniter, Laravel, and Python. Improved system performance by 70% through database optimization, Redis caching, and search indexing. Integrated APIs including Twilio, Exotel, WhatsApp, Mailchimp, Zoho, and Airtable. Led a team of 6 developers, improving delivery speed by 30% through Agile practices and code reviews.",
            "skills": "PHP, CodeIgniter, Laravel, Python, Redis, MySQL, Twilio, Exotel, WhatsApp API, Mailchimp, Zoho, Airtable, Team Leadership, Agile",
            "occupationLocation": {
              "@type": "AdministrativeArea",
              "name": "India"
            },
            "responsibilities": [
              "Delivered 15+ enterprise applications (CRM, CMS, HRMS) using PHP, CodeIgniter, Laravel, and Python",
              "Improved system performance by 70% through database optimization, Redis caching, and search indexing",
              "Integrated APIs including Twilio, Exotel, WhatsApp, Mailchimp, Zoho, and Airtable",
              "Led a team of 6 developers, improving delivery speed by 30% through Agile practices and code reviews",
              "Designed scalable backend systems handling high user traffic and large datasets"
            ]
          }
        ],
        "knowsAbout": [
          "PHP",
          "Laravel",
          "CodeIgniter",
          "Python",
          "FastAPI",
          "JavaScript",
          "TypeScript",
          "React.js",
          "Next.js",
          "Vue.js",
          "REST API Design",
          "System Architecture",
          "MySQL",
          "PostgreSQL",
          "MongoDB",
          "Redis",
          "Query Optimization",
          "Docker",
          "Git",
          "CI/CD",
          "Amazon Web Services (AWS)",
          "Google Cloud Platform (GCP)",
          "n8n Workflow Automation",
          "Mage AI",
          "OpenAI API",
          "Google Gemini AI",
          "Razorpay Payment Gateway",
          "Zoho Sign",
          "Twilio API",
          "WhatsApp Business API",
          "Tailwind CSS",
          "Bootstrap"
        ],
        "workExample": [
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-justfact"
          },
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-houseofkausheya"
          },
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-chatmaxima"
          },
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-expertconnect"
          },
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-subscriptionsystem"
          },
          {
            "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-ffreedom"
          }
        ]
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "About",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/#about"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Skills",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/#skills"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "name": "Experience",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/#experience"
        },
        {
          "@type": "ListItem",
          "position": 5,
          "name": "Projects",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/#projects"
        },
        {
          "@type": "ListItem",
          "position": 6,
          "name": "Contact",
          "item": "https://sankara25.github.io/sankarasubramanian.dev/#contact"
        }
      ]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-justfact",
      "name": "JustFact.net",
      "url": "https://justfact.net",
      "applicationCategory": "NewsApplication",
      "operatingSystem": "All (Web)",
      "description": "News aggregation and publishing platform with JWT-based authentication, Google Gemini AI content summarization and fact-checking, deployed on GCP for high availability.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "Python, FastAPI, MySQL, JWT, Gemini AI, GCP, News Aggregation"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-houseofkausheya",
      "name": "Houseofkausheya.com",
      "url": "https://houseofkausheya.com",
      "applicationCategory": "ShoppingApplication",
      "operatingSystem": "All (Web)",
      "description": "E-commerce platform with automated order management, Razorpay payment gateway integration, automated email notifications, and Tailwind CSS frontend deployed on GCP.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "Laravel, MySQL, Razorpay, Tailwind CSS, GCP, E-commerce"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-chatmaxima",
      "name": "Chatmaxima.com",
      "url": "https://chatmaxima.com",
      "applicationCategory": "CommunicationApplication",
      "operatingSystem": "All (Web)",
      "description": "Unified omnichannel communication platform and drag-and-drop chatbot builder supporting SMS, WhatsApp, Instagram, Facebook, Telegram, and Slack with centralized real-time messaging.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "CodeIgniter 4, MySQL, Redis, Bootstrap, Twilio, WhatsApp API, Meta API, Chatbot"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-expertconnect",
      "name": "Expert Connect Platform",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All (Web)",
      "description": "Secure consultation and expert onboarding platform featuring real-time session tracking, automated earnings calculation, role-based auth, Razorpay payments, and Redis caching.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "FastAPI, CodeIgniter, Laravel, MySQL, MongoDB, Redis, Razorpay"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-subscriptionsystem",
      "name": "Website & Subscription System",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "All (Web)",
      "description": "High-performance subscription management and billing API platform with webhook integrations, Redis session caching, multi-channel notifications, and Firebase real-time data sync.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "FastAPI, MongoDB, Redis, Firebase, Razorpay, Subscription API"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://sankara25.github.io/sankarasubramanian.dev/#project-ffreedom",
      "name": "ffreedom App API",
      "applicationCategory": "EducationalApplication",
      "operatingSystem": "All (Web)",
      "description": "Scalable enterprise API architecture for automated dynamic PDF certificate/invoice generation, Zoho Sign eSignature workflow integration, Redis caching, and AWS/GCP cloud storage.",
      "creator": {
        "@id": "https://sankara25.github.io/sankarasubramanian.dev/#person"
      },
      "keywords": "CodeIgniter, Laravel, Python, Redis, Zoho Sign, AWS, GCP"
    }
  ]
}

formatted = json.dumps(schema, indent=2, ensure_ascii=False)
with open("schema_ld.json", "w", encoding="utf-8") as f:
    f.write(formatted)
print("Updated schema_ld.json with perfected ProfilePage, worksFor Organization array, and hasOccupation array!")
