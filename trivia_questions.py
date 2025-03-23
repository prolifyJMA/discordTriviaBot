"""
Database of computer science trivia questions with hints.
Each question is a dictionary containing:
- question: The trivia question
- correct_answer: The correct answer
- incorrect_answers: List of incorrect answers
- hint: A helpful hint for the question
"""

TRIVIA_QUESTIONS = [
    # Programming Languages
    {
        "question": "What does CPU stand for?",
        "correct_answer": "Central Processing Unit",
        "incorrect_answers": [
            "Computer Processing Unit",
            "Central Program Unit",
            "Computer Program Unit"
        ],
        "hint": "This is the main component that processes instructions in a computer"
    },
    {
        "question": "Which programming language is known as the 'mother of all programming languages'?",
        "correct_answer": "FORTRAN",
        "incorrect_answers": [
            "COBOL",
            "BASIC",
            "Pascal"
        ],
        "hint": "This language was developed in the 1950s and is still used in scientific computing"
    },
    {
        "question": "What does HTML stand for?",
        "correct_answer": "HyperText Markup Language",
        "incorrect_answers": [
            "High Text Markup Language",
            "HyperText Making Language",
            "High Text Making Language"
        ],
        "hint": "This language is used to structure content on the web"
    },
    {
        "question": "Which company developed Python?",
        "correct_answer": "Guido van Rossum",
        "incorrect_answers": [
            "Microsoft",
            "Google",
            "Apple"
        ],
        "hint": "This is the name of the individual who created Python, not a company"
    },
    {
        "question": "What is the smallest unit of digital information?",
        "correct_answer": "Bit",
        "incorrect_answers": [
            "Byte",
            "Nibble",
            "Word"
        ],
        "hint": "This is a single binary digit, either 0 or 1"
    },
    {
        "question": "Which of these is NOT a programming paradigm?",
        "correct_answer": "Binary Programming",
        "incorrect_answers": [
            "Object-Oriented Programming",
            "Functional Programming",
            "Procedural Programming"
        ],
        "hint": "This term refers to a way of organizing and structuring code"
    },
    {
        "question": "What does RAM stand for?",
        "correct_answer": "Random Access Memory",
        "incorrect_answers": [
            "Read Access Memory",
            "Random Available Memory",
            "Read Available Memory"
        ],
        "hint": "This is the temporary memory that your computer uses while running programs"
    },
    {
        "question": "Which of these is a type of computer virus?",
        "correct_answer": "Trojan Horse",
        "incorrect_answers": [
            "Greek Horse",
            "Roman Horse",
            "Persian Horse"
        ],
        "hint": "This type of malware disguises itself as legitimate software"
    },
    {
        "question": "What is the process of finding and fixing errors in code called?",
        "correct_answer": "Debugging",
        "incorrect_answers": [
            "Error fixing",
            "Code cleaning",
            "Problem solving"
        ],
        "hint": "This term comes from removing actual bugs from early computers"
    },
    {
        "question": "Which of these is NOT a web browser?",
        "correct_answer": "Microsoft Word",
        "incorrect_answers": [
            "Chrome",
            "Firefox",
            "Safari"
        ],
        "hint": "This is a word processing application, not a web browser"
    },
    {
        "question": "What does URL stand for?",
        "correct_answer": "Uniform Resource Locator",
        "incorrect_answers": [
            "Universal Resource Link",
            "Uniform Resource Link",
            "Universal Resource Locator"
        ],
        "hint": "This is the address you type to visit a website"
    },
    {
        "question": "Which of these is a type of computer network?",
        "correct_answer": "LAN",
        "incorrect_answers": [
            "LAP",
            "LAM",
            "LAR"
        ],
        "hint": "This stands for Local Area Network"
    },
    {
        "question": "What is the process of converting source code into machine code called?",
        "correct_answer": "Compilation",
        "incorrect_answers": [
            "Translation",
            "Conversion",
            "Transformation"
        ],
        "hint": "This process creates an executable program from your code"
    },
    {
        "question": "Which of these is NOT a data structure?",
        "correct_answer": "Computer",
        "incorrect_answers": [
            "Array",
            "Stack",
            "Queue"
        ],
        "hint": "This is a physical device, not a way to organize data"
    },
    {
        "question": "What does SQL stand for?",
        "correct_answer": "Structured Query Language",
        "incorrect_answers": [
            "Simple Query Language",
            "Structured Question Language",
            "Simple Question Language"
        ],
        "hint": "This language is used to interact with databases"
    },
    # Additional Programming Languages
    {
        "question": "Which programming language was created by James Gosling?",
        "correct_answer": "Java",
        "incorrect_answers": [
            "Python",
            "C++",
            "Ruby"
        ],
        "hint": "This language's mascot is a coffee cup"
    },
    {
        "question": "What does PHP stand for?",
        "correct_answer": "PHP: Hypertext Preprocessor",
        "incorrect_answers": [
            "Personal Home Page",
            "Programmed Hypertext Processor",
            "Public Home Page"
        ],
        "hint": "This is a server-side scripting language commonly used for web development"
    },
    {
        "question": "Which language is known as the 'mother of all modern programming languages'?",
        "correct_answer": "C",
        "incorrect_answers": [
            "FORTRAN",
            "COBOL",
            "BASIC"
        ],
        "hint": "Many modern languages like C++, Java, and Python were influenced by this language"
    },
    {
        "question": "What does CSS stand for?",
        "correct_answer": "Cascading Style Sheets",
        "incorrect_answers": [
            "Computer Style Sheets",
            "Cascading System Sheets",
            "Computer System Sheets"
        ],
        "hint": "This language is used to style web pages"
    },
    {
        "question": "Which programming language is named after a snake?",
        "correct_answer": "Python",
        "incorrect_answers": [
            "Java",
            "Ruby",
            "Perl"
        ],
        "hint": "This language's logo features a coiled snake"
    },
    # Computer Hardware
    {
        "question": "What does GPU stand for?",
        "correct_answer": "Graphics Processing Unit",
        "incorrect_answers": [
            "Graphics Program Unit",
            "General Processing Unit",
            "General Program Unit"
        ],
        "hint": "This component is specialized for handling graphics and parallel processing"
    },
    {
        "question": "Which of these is NOT a type of computer port?",
        "correct_answer": "USB-C",
        "incorrect_answers": [
            "HDMI",
            "VGA",
            "DVI"
        ],
        "hint": "This is a newer type of connection that can handle both data and power"
    },
    {
        "question": "What is the main function of a motherboard?",
        "correct_answer": "Connect all computer components",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This component is the main circuit board of a computer"
    },
    {
        "question": "Which of these is a type of computer storage?",
        "correct_answer": "SSD",
        "incorrect_answers": [
            "CPU",
            "GPU",
            "RAM"
        ],
        "hint": "This is a solid-state storage device that's faster than traditional hard drives"
    },
    {
        "question": "What does HDD stand for?",
        "correct_answer": "Hard Disk Drive",
        "incorrect_answers": [
            "Hard Drive Disk",
            "High Density Drive",
            "High Definition Drive"
        ],
        "hint": "This is a traditional type of storage device that uses spinning disks"
    },
    # Computer Networks
    {
        "question": "What does DNS stand for?",
        "correct_answer": "Domain Name System",
        "incorrect_answers": [
            "Domain Network System",
            "Digital Name System",
            "Digital Network System"
        ],
        "hint": "This system converts human-readable domain names into IP addresses"
    },
    {
        "question": "Which of these is NOT a network topology?",
        "correct_answer": "Square",
        "incorrect_answers": [
            "Star",
            "Ring",
            "Bus"
        ],
        "hint": "This is a shape, not a way to arrange network devices"
    },
    {
        "question": "What is the maximum speed of a standard Ethernet connection?",
        "correct_answer": "1000 Mbps",
        "incorrect_answers": [
            "100 Mbps",
            "500 Mbps",
            "2000 Mbps"
        ],
        "hint": "This is also known as Gigabit Ethernet"
    },
    {
        "question": "Which protocol is used to send email?",
        "correct_answer": "SMTP",
        "incorrect_answers": [
            "HTTP",
            "FTP",
            "SSH"
        ],
        "hint": "This stands for Simple Mail Transfer Protocol"
    },
    {
        "question": "What does VPN stand for?",
        "correct_answer": "Virtual Private Network",
        "incorrect_answers": [
            "Virtual Public Network",
            "Visual Private Network",
            "Visual Public Network"
        ],
        "hint": "This creates a secure connection over the internet"
    },
    # Computer Security
    {
        "question": "What is the most common type of computer virus?",
        "correct_answer": "Trojan Horse",
        "incorrect_answers": [
            "Worm",
            "Spyware",
            "Adware"
        ],
        "hint": "This type of malware disguises itself as legitimate software"
    },
    {
        "question": "Which of these is NOT a type of encryption?",
        "correct_answer": "Binary",
        "incorrect_answers": [
            "AES",
            "RSA",
            "DES"
        ],
        "hint": "This is a number system, not a security method"
    },
    {
        "question": "What is the purpose of a firewall?",
        "correct_answer": "Block unauthorized access",
        "incorrect_answers": [
            "Speed up internet",
            "Store data",
            "Process information"
        ],
        "hint": "This is a security system that monitors and controls network traffic"
    },
    {
        "question": "Which of these is a type of password attack?",
        "correct_answer": "Brute Force",
        "incorrect_answers": [
            "Soft Force",
            "Light Force",
            "Easy Force"
        ],
        "hint": "This method tries every possible combination until it finds the right password"
    },
    {
        "question": "What does SSL stand for?",
        "correct_answer": "Secure Sockets Layer",
        "incorrect_answers": [
            "Secure System Layer",
            "Safe Sockets Layer",
            "Safe System Layer"
        ],
        "hint": "This protocol provides secure communication over the internet"
    },
    # Computer History
    {
        "question": "Who is known as the 'father of the computer'?",
        "correct_answer": "Charles Babbage",
        "incorrect_answers": [
            "Alan Turing",
            "John von Neumann",
            "Ada Lovelace"
        ],
        "hint": "This person designed the first mechanical computer in the 1830s"
    },
    {
        "question": "Which company created the first personal computer?",
        "correct_answer": "IBM",
        "incorrect_answers": [
            "Apple",
            "Microsoft",
            "Intel"
        ],
        "hint": "This company released the IBM PC in 1981"
    },
    {
        "question": "What was the first computer mouse made of?",
        "correct_answer": "Wood",
        "incorrect_answers": [
            "Plastic",
            "Metal",
            "Glass"
        ],
        "hint": "This was created by Douglas Engelbart in the 1960s"
    },
    {
        "question": "Which was the first computer to use a graphical user interface?",
        "correct_answer": "Xerox Alto",
        "incorrect_answers": [
            "Apple Macintosh",
            "IBM PC",
            "Commodore 64"
        ],
        "hint": "This computer was developed in the 1970s and inspired the Macintosh"
    },
    {
        "question": "What was the first computer virus called?",
        "correct_answer": "Creeper",
        "incorrect_answers": [
            "Worm",
            "Bug",
            "Spider"
        ],
        "hint": "This virus was created in 1971 and displayed the message 'I'm the creeper, catch me if you can!'"
    },
    # Computer Science Concepts
    {
        "question": "What is the time complexity of binary search?",
        "correct_answer": "O(log n)",
        "incorrect_answers": [
            "O(n)",
            "O(n²)",
            "O(1)"
        ],
        "hint": "This algorithm divides the search space in half with each step"
    },
    {
        "question": "Which of these is NOT a sorting algorithm?",
        "correct_answer": "Binary",
        "incorrect_answers": [
            "Bubble Sort",
            "Quick Sort",
            "Merge Sort"
        ],
        "hint": "This is a number system, not a way to organize data"
    },
    {
        "question": "What is the purpose of a stack in programming?",
        "correct_answer": "Store data in LIFO order",
        "incorrect_answers": [
            "Store data in FIFO order",
            "Store data randomly",
            "Store data in sorted order"
        ],
        "hint": "This data structure follows the Last In, First Out principle"
    },
    {
        "question": "Which of these is a type of computer memory?",
        "correct_answer": "Cache",
        "incorrect_answers": [
            "CPU",
            "GPU",
            "PSU"
        ],
        "hint": "This is a small, fast memory that stores frequently accessed data"
    },
    {
        "question": "What is the purpose of an operating system?",
        "correct_answer": "Manage computer resources",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This software controls hardware and provides services to applications"
    },
    # Additional Computer Science Concepts
    {
        "question": "What is the time complexity of bubble sort?",
        "correct_answer": "O(n²)",
        "incorrect_answers": [
            "O(n)",
            "O(log n)",
            "O(1)"
        ],
        "hint": "This sorting algorithm repeatedly steps through the list and swaps adjacent elements"
    },
    {
        "question": "Which of these is NOT a type of computer network?",
        "correct_answer": "WAN",
        "incorrect_answers": [
            "LAN",
            "MAN",
            "PAN"
        ],
        "hint": "This is a type of network that covers a large geographic area"
    },
    {
        "question": "What is the purpose of a compiler?",
        "correct_answer": "Convert source code to machine code",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This program translates high-level programming language into low-level machine code"
    },
    {
        "question": "Which of these is a type of computer memory?",
        "correct_answer": "ROM",
        "incorrect_answers": [
            "CPU",
            "GPU",
            "PSU"
        ],
        "hint": "This is Read-Only Memory that stores permanent data"
    },
    {
        "question": "What is the purpose of an algorithm?",
        "correct_answer": "Solve a problem step by step",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This is a set of instructions to accomplish a specific task"
    },
    # Web Development
    {
        "question": "What does JavaScript primarily run on?",
        "correct_answer": "Web browser",
        "incorrect_answers": [
            "Server",
            "Database",
            "Operating system"
        ],
        "hint": "This programming language is commonly used to make web pages interactive"
    },
    {
        "question": "Which of these is NOT a web development framework?",
        "correct_answer": "Java",
        "incorrect_answers": [
            "React",
            "Angular",
            "Vue"
        ],
        "hint": "This is a programming language, not a framework"
    },
    {
        "question": "What is the purpose of CSS?",
        "correct_answer": "Style web pages",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This language controls the appearance and layout of web pages"
    },
    {
        "question": "Which of these is a type of web server?",
        "correct_answer": "Apache",
        "incorrect_answers": [
            "MySQL",
            "MongoDB",
            "Redis"
        ],
        "hint": "This is one of the most popular web server software"
    },
    {
        "question": "What is the purpose of a cookie in web development?",
        "correct_answer": "Store user data",
        "incorrect_answers": [
            "Process information",
            "Display graphics",
            "Connect to database"
        ],
        "hint": "This is a small piece of data stored on the user's computer"
    },
    # Database Systems
    {
        "question": "Which of these is NOT a type of database?",
        "correct_answer": "HTML",
        "incorrect_answers": [
            "MySQL",
            "PostgreSQL",
            "MongoDB"
        ],
        "hint": "This is a markup language, not a database system"
    },
    {
        "question": "What is the purpose of a database index?",
        "correct_answer": "Speed up data retrieval",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This structure helps quickly locate data in a database"
    },
    {
        "question": "Which of these is a NoSQL database?",
        "correct_answer": "MongoDB",
        "incorrect_answers": [
            "MySQL",
            "PostgreSQL",
            "SQLite"
        ],
        "hint": "This database stores data in a document-based format"
    },
    {
        "question": "What is the purpose of a database transaction?",
        "correct_answer": "Ensure data consistency",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This ensures that database operations are atomic and reliable"
    },
    {
        "question": "Which of these is NOT a database operation?",
        "correct_answer": "RENDER",
        "incorrect_answers": [
            "SELECT",
            "INSERT",
            "UPDATE"
        ],
        "hint": "This is not a standard SQL command"
    },
    # Artificial Intelligence
    {
        "question": "What is machine learning?",
        "correct_answer": "Training computers to learn from data",
        "incorrect_answers": [
            "Storing data",
            "Processing information",
            "Displaying graphics"
        ],
        "hint": "This field focuses on creating systems that can learn and improve from experience"
    },
    {
        "question": "Which of these is NOT a type of machine learning?",
        "correct_answer": "Binary Learning",
        "incorrect_answers": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Reinforcement Learning"
        ],
        "hint": "This is not a recognized category of machine learning"
    },
    {
        "question": "What is the purpose of a neural network?",
        "correct_answer": "Process information like the human brain",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This is inspired by the structure of biological neural networks"
    },
    {
        "question": "Which of these is a type of AI application?",
        "correct_answer": "Computer Vision",
        "incorrect_answers": [
            "Database",
            "Web server",
            "Operating system"
        ],
        "hint": "This field focuses on enabling computers to understand visual information"
    },
    {
        "question": "What is the purpose of natural language processing?",
        "correct_answer": "Understand human language",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This field focuses on enabling computers to understand and process human language"
    },
    # Mobile Development
    {
        "question": "Which of these is NOT a mobile operating system?",
        "correct_answer": "Windows XP",
        "incorrect_answers": [
            "Android",
            "iOS",
            "Windows Mobile"
        ],
        "hint": "This is a desktop operating system"
    },
    {
        "question": "What is the purpose of a mobile app?",
        "correct_answer": "Provide functionality on mobile devices",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This is software designed to run on mobile devices"
    },
    {
        "question": "Which of these is a mobile development framework?",
        "correct_answer": "React Native",
        "incorrect_answers": [
            "MySQL",
            "Apache",
            "MongoDB"
        ],
        "hint": "This framework allows you to build mobile apps using JavaScript"
    },
    {
        "question": "What is the purpose of mobile responsive design?",
        "correct_answer": "Make websites work on mobile devices",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This ensures websites look good on all screen sizes"
    },
    {
        "question": "Which of these is NOT a mobile app store?",
        "correct_answer": "Amazon",
        "incorrect_answers": [
            "App Store",
            "Google Play",
            "Microsoft Store"
        ],
        "hint": "This is an e-commerce platform, not primarily an app store"
    },
    # Cloud Computing
    {
        "question": "What is cloud computing?",
        "correct_answer": "Using remote servers over the internet",
        "incorrect_answers": [
            "Storing data locally",
            "Processing information",
            "Displaying graphics"
        ],
        "hint": "This allows you to access computing resources over the internet"
    },
    {
        "question": "Which of these is NOT a cloud service provider?",
        "correct_answer": "Oracle",
        "incorrect_answers": [
            "AWS",
            "Azure",
            "Google Cloud"
        ],
        "hint": "This company is primarily known for databases, not cloud services"
    },
    {
        "question": "What is the purpose of cloud storage?",
        "correct_answer": "Store data on remote servers",
        "incorrect_answers": [
            "Process information",
            "Display graphics",
            "Connect to database"
        ],
        "hint": "This allows you to store and access data over the internet"
    },
    {
        "question": "Which of these is a type of cloud service?",
        "correct_answer": "SaaS",
        "incorrect_answers": [
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "hint": "This stands for Software as a Service"
    },
    {
        "question": "What is the purpose of cloud computing?",
        "correct_answer": "Access computing resources remotely",
        "incorrect_answers": [
            "Store data locally",
            "Process information",
            "Display graphics"
        ],
        "hint": "This allows you to use computing resources without owning them"
    },
    # Cybersecurity
    {
        "question": "What is a 'zero-day' vulnerability?",
        "correct_answer": "A security flaw unknown to the vendor",
        "incorrect_answers": [
            "A virus that lasts only one day",
            "A password that expires in 24 hours",
            "A temporary security patch"
        ],
        "hint": "This type of vulnerability is called 'zero-day' because developers have zero days to fix it before it's exploited"
    },
    {
        "question": "Which of these is NOT a type of cyber attack?",
        "correct_answer": "Data Mining",
        "incorrect_answers": [
            "Phishing",
            "Ransomware",
            "DDoS"
        ],
        "hint": "This is a legitimate data analysis technique, not a malicious attack"
    },
    {
        "question": "What is the purpose of two-factor authentication?",
        "correct_answer": "Add an extra layer of security",
        "incorrect_answers": [
            "Speed up login process",
            "Store more passwords",
            "Share accounts"
        ],
        "hint": "This requires both something you know and something you have to verify your identity"
    },
    {
        "question": "Which of these is a type of encryption key?",
        "correct_answer": "Public Key",
        "incorrect_answers": [
            "Open Key",
            "Shared Key",
            "Common Key"
        ],
        "hint": "This key can be freely shared and is used to encrypt messages"
    },
    {
        "question": "What is the purpose of a honeypot?",
        "correct_answer": "Trap cyber attackers",
        "incorrect_answers": [
            "Store honey",
            "Speed up internet",
            "Process data"
        ],
        "hint": "This is a decoy system designed to lure and study cyber attackers"
    },
    # Game Development
    {
        "question": "What is a game engine?",
        "correct_answer": "Software framework for game development",
        "incorrect_answers": [
            "A type of computer",
            "A gaming console",
            "A video game"
        ],
        "hint": "This provides the core functionality needed to create video games"
    },
    {
        "question": "Which of these is NOT a game development concept?",
        "correct_answer": "Data Mining",
        "incorrect_answers": [
            "Physics Engine",
            "Game Loop",
            "Collision Detection"
        ],
        "hint": "This is a data analysis technique, not a game development concept"
    },
    {
        "question": "What is the purpose of a sprite in game development?",
        "correct_answer": "Represent game objects visually",
        "incorrect_answers": [
            "Store game data",
            "Process game logic",
            "Handle user input"
        ],
        "hint": "This is a 2D image or animation used in games"
    },
    {
        "question": "Which of these is a popular game engine?",
        "correct_answer": "Unity",
        "incorrect_answers": [
            "MySQL",
            "Apache",
            "MongoDB"
        ],
        "hint": "This engine is known for its cross-platform capabilities"
    },
    {
        "question": "What is the purpose of game physics?",
        "correct_answer": "Simulate realistic movement",
        "incorrect_answers": [
            "Store game data",
            "Process game logic",
            "Handle user input"
        ],
        "hint": "This handles gravity, collisions, and other physical interactions"
    },
    # Software Engineering
    {
        "question": "What is the purpose of version control?",
        "correct_answer": "Track changes in code",
        "incorrect_answers": [
            "Speed up coding",
            "Store data",
            "Process information"
        ],
        "hint": "This system helps manage different versions of software"
    },
    {
        "question": "Which of these is NOT a software development methodology?",
        "correct_answer": "Data Mining",
        "incorrect_answers": [
            "Agile",
            "Waterfall",
            "Scrum"
        ],
        "hint": "This is a data analysis technique, not a development methodology"
    },
    {
        "question": "What is the purpose of unit testing?",
        "correct_answer": "Test individual components",
        "incorrect_answers": [
            "Speed up development",
            "Store data",
            "Process information"
        ],
        "hint": "This tests small, isolated parts of the code"
    },
    {
        "question": "Which of these is a type of software architecture?",
        "correct_answer": "Microservices",
        "incorrect_answers": [
            "Data Mining",
            "Web Server",
            "Database"
        ],
        "hint": "This architecture breaks down applications into small, independent services"
    },
    {
        "question": "What is the purpose of continuous integration?",
        "correct_answer": "Automate code integration",
        "incorrect_answers": [
            "Speed up coding",
            "Store data",
            "Process information"
        ],
        "hint": "This practice automatically merges code changes into a shared repository"
    },
    # Computer Graphics
    {
        "question": "What is ray tracing?",
        "correct_answer": "Simulate light behavior in graphics",
        "incorrect_answers": [
            "Store graphics",
            "Process images",
            "Display text"
        ],
        "hint": "This technique creates realistic lighting effects in computer graphics"
    },
    {
        "question": "Which of these is NOT a graphics format?",
        "correct_answer": "TXT",
        "incorrect_answers": [
            "PNG",
            "JPEG",
            "SVG"
        ],
        "hint": "This is a text file format, not an image format"
    },
    {
        "question": "What is the purpose of texture mapping?",
        "correct_answer": "Add surface detail to 3D models",
        "incorrect_answers": [
            "Store images",
            "Process text",
            "Display video"
        ],
        "hint": "This technique applies 2D images to 3D surfaces"
    },
    {
        "question": "Which of these is a 3D modeling software?",
        "correct_answer": "Blender",
        "incorrect_answers": [
            "MySQL",
            "Apache",
            "MongoDB"
        ],
        "hint": "This is a free and open-source 3D creation suite"
    },
    {
        "question": "What is the purpose of anti-aliasing?",
        "correct_answer": "Smooth jagged edges in graphics",
        "incorrect_answers": [
            "Speed up rendering",
            "Store images",
            "Process text"
        ],
        "hint": "This technique reduces the appearance of jagged edges in computer graphics"
    },
    # Computer Vision
    {
        "question": "What is image recognition?",
        "correct_answer": "Identify objects in images",
        "incorrect_answers": [
            "Store images",
            "Process text",
            "Display video"
        ],
        "hint": "This technology allows computers to understand and identify objects in images"
    },
    {
        "question": "Which of these is NOT a computer vision task?",
        "correct_answer": "Data Mining",
        "incorrect_answers": [
            "Object Detection",
            "Face Recognition",
            "Motion Tracking"
        ],
        "hint": "This is a data analysis technique, not a computer vision task"
    },
    {
        "question": "What is the purpose of edge detection?",
        "correct_answer": "Find boundaries in images",
        "incorrect_answers": [
            "Store images",
            "Process text",
            "Display video"
        ],
        "hint": "This technique identifies significant changes in image brightness"
    },
    {
        "question": "Which of these is a computer vision library?",
        "correct_answer": "OpenCV",
        "incorrect_answers": [
            "MySQL",
            "Apache",
            "MongoDB"
        ],
        "hint": "This is a popular library for computer vision and image processing"
    },
    {
        "question": "What is the purpose of facial recognition?",
        "correct_answer": "Identify people from images",
        "incorrect_answers": [
            "Store images",
            "Process text",
            "Display video"
        ],
        "hint": "This technology analyzes facial features to identify individuals"
    },
    # Additional Programming Languages Questions
    {
        "question": "Which programming language is known for its 'write once, run anywhere' slogan?",
        "correct_answer": "Java",
        "incorrect_answers": [
            "Python",
            "C++",
            "Ruby"
        ],
        "hint": "This language runs on a virtual machine"
    },
    {
        "question": "What does IDE stand for?",
        "correct_answer": "Integrated Development Environment",
        "incorrect_answers": [
            "Internet Development Environment",
            "Integrated Design Environment",
            "Internet Design Environment"
        ],
        "hint": "This is a software application that provides comprehensive tools for development"
    },
    {
        "question": "Which language is commonly used for system programming?",
        "correct_answer": "C",
        "incorrect_answers": [
            "Python",
            "Java",
            "Ruby"
        ],
        "hint": "This language provides low-level access to memory and hardware"
    },
    {
        "question": "What is the purpose of garbage collection?",
        "correct_answer": "Automatically manage memory",
        "incorrect_answers": [
            "Speed up programs",
            "Store data",
            "Process information"
        ],
        "hint": "This feature automatically frees memory that's no longer needed"
    },
    {
        "question": "Which language is known for its extensive use in data science?",
        "correct_answer": "Python",
        "incorrect_answers": [
            "Java",
            "C++",
            "Ruby"
        ],
        "hint": "This language has libraries like NumPy and Pandas"
    },
    # Additional Computer Hardware Questions
    {
        "question": "What is the purpose of a heatsink?",
        "correct_answer": "Cool computer components",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This component helps prevent overheating by dissipating heat"
    },
    {
        "question": "What is the purpose of a power supply unit?",
        "correct_answer": "Convert power for computer components",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This component converts AC power to DC power for the computer"
    },
    {
        "question": "Which of these is a type of computer cooling system?",
        "correct_answer": "Liquid Cooling",
        "incorrect_answers": [
            "Data Cooling",
            "Process Cooling",
            "Display Cooling"
        ],
        "hint": "This system uses liquid to transfer heat away from components"
    },
    {
        "question": "What is the purpose of a sound card?",
        "correct_answer": "Process audio signals",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This component handles audio input and output"
    },
    # Additional Computer Networks Questions
    {
        "question": "What is the purpose of a router?",
        "correct_answer": "Direct network traffic",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This device forwards data packets between computer networks"
    },
    {
        "question": "Which protocol is used for secure web browsing?",
        "correct_answer": "HTTPS",
        "incorrect_answers": [
            "HTTP",
            "FTP",
            "SSH"
        ],
        "hint": "This protocol adds encryption to standard web traffic"
    },
    {
        "question": "What is the purpose of a firewall?",
        "correct_answer": "Control network access",
        "incorrect_answers": [
            "Speed up internet",
            "Store data",
            "Process information"
        ],
        "hint": "This security system monitors and controls incoming and outgoing network traffic"
    },
    {
        "question": "Which of these is a type of wireless network?",
        "correct_answer": "Wi-Fi",
        "incorrect_answers": [
            "Ethernet",
            "Fiber",
            "Coaxial"
        ],
        "hint": "This technology allows devices to connect to the internet without cables"
    },
    {
        "question": "What is the purpose of a network switch?",
        "correct_answer": "Connect network devices",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This device connects multiple devices on a local network"
    },
    # Additional Computer Security Questions
    {
        "question": "What is the purpose of encryption?",
        "correct_answer": "Protect data privacy",
        "incorrect_answers": [
            "Speed up data transfer",
            "Store data",
            "Process information"
        ],
        "hint": "This process converts data into a secure format"
    },
    {
        "question": "Which of these is a type of malware?",
        "correct_answer": "Ransomware",
        "incorrect_answers": [
            "Dataware",
            "Processware",
            "Displayware"
        ],
        "hint": "This malicious software encrypts files and demands payment"
    },
    {
        "question": "What is the purpose of a VPN?",
        "correct_answer": "Create secure connections",
        "incorrect_answers": [
            "Speed up internet",
            "Store data",
            "Process information"
        ],
        "hint": "This creates an encrypted tunnel for data transmission"
    },
    {
        "question": "Which of these is a security best practice?",
        "correct_answer": "Regular password updates",
        "incorrect_answers": [
            "Using simple passwords",
            "Sharing passwords",
            "Writing passwords down"
        ],
        "hint": "This helps maintain account security over time"
    },
    {
        "question": "What is the purpose of biometric authentication?",
        "correct_answer": "Verify identity using unique features",
        "incorrect_answers": [
            "Speed up login",
            "Store data",
            "Process information"
        ],
        "hint": "This uses physical characteristics like fingerprints or facial features"
    },
    # Additional Computer History Questions
    {
        "question": "Who is known as the 'mother of programming'?",
        "correct_answer": "Ada Lovelace",
        "incorrect_answers": [
            "Grace Hopper",
            "Margaret Hamilton",
            "Jean Bartik"
        ],
        "hint": "This person wrote the first algorithm intended for machine processing"
    },
    {
        "question": "Which was the first commercial microprocessor?",
        "correct_answer": "Intel 4004",
        "incorrect_answers": [
            "Intel 8080",
            "Zilog Z80",
            "MOS 6502"
        ],
        "hint": "This processor was released by Intel in 1971"
    },
    {
        "question": "What was the first computer to use a mouse?",
        "correct_answer": "Xerox Alto",
        "incorrect_answers": [
            "Apple Macintosh",
            "IBM PC",
            "Commodore 64"
        ],
        "hint": "This computer was developed in the 1970s"
    },
    {
        "question": "Which company created the first personal computer?",
        "correct_answer": "IBM",
        "incorrect_answers": [
            "Apple",
            "Microsoft",
            "Intel"
        ],
        "hint": "This company released the IBM PC in 1981"
    },
    {
        "question": "What was the first computer virus called?",
        "correct_answer": "Creeper",
        "incorrect_answers": [
            "Worm",
            "Bug",
            "Spider"
        ],
        "hint": "This virus was created in 1971"
    },
    # Additional Computer Science Concepts Questions
    {
        "question": "What is the purpose of a binary tree?",
        "correct_answer": "Organize hierarchical data",
        "incorrect_answers": [
            "Store data",
            "Process information",
            "Display graphics"
        ],
        "hint": "This data structure has at most two children per node"
    },
    {
        "question": "Which of these is a type of algorithm?",
        "correct_answer": "Binary Search",
        "incorrect_answers": [
            "Data Search",
            "Process Search",
            "Display Search"
        ],
        "hint": "This algorithm divides the search space in half with each step"
    },
    {
        "question": "What is the purpose of recursion?",
        "correct_answer": "Solve problems by breaking them down",
        "incorrect_answers": [
            "Speed up programs",
            "Store data",
            "Process information"
        ],
        "hint": "This technique involves a function calling itself"
    },
    {
        "question": "Which of these is a type of data structure?",
        "correct_answer": "Hash Table",
        "incorrect_answers": [
            "Data Table",
            "Process Table",
            "Display Table"
        ],
        "hint": "This structure provides fast access to data using key-value pairs"
    },
    {
        "question": "What is the purpose of object-oriented programming?",
        "correct_answer": "Organize code into reusable objects",
        "incorrect_answers": [
            "Speed up programs",
            "Store data",
            "Process information"
        ],
        "hint": "This programming paradigm uses objects to model real-world entities"
    }
] 