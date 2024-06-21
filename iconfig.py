DEVELOPER_ROLE = "Full Stack Developer"
DEVELOPER_PASSION = "I design and code beautifully simple things, and I love what I do."
DEVELOPER_NAME = "Ahmed Ezzat"
DEVELOPER_ADDRESS = "Egypt"
DEVELOPER_GREETINGS = f"Hi, I’m {DEVELOPER_NAME}. Nice to meet you."
DEVELOPER_INTRODUCTION = "Since beginning my journey as a full stack developer 7 years ago, I've done remote work for agencies, consulted for startups, and collaborated with talented people to create digital products for both business and consumer use. I'm quietly confident, naturally curious, and perpetually working on improving my chops."
DEVELOPER_SKILLS = [
    [
        "Full Stack Developer",
        "I like to code things from scratch, and enjoy bringing ideas to life in the browser.",
        "Languages I speak:",
        "javascript, Typescript, HTML, CSS, Sass, Git, PHP",
        "Dev Tools:",
        [
            "Laravel",
            "React",
            "Nextjs",
            "Tailwind CSS",
            "Github",
            "VS Code",
        ],
    ],
    [
        "Python Developer",
        "I genuinely care about crafting user-friendly experiences, reducing complexity while maximizing effectiveness.",
        "Things I help with:",
        "Scraping, Crawling, Recommendation System, AI Bot",
        "Dev Frameworks",
        [
            "Selenium",
            "Langchain",
            "Hugging Face",
            "Pytorch",
            "Deepgram",
            "Bubble.io",
            "openai",
        ],
    ],
]
DEVELOPER_EXPERIENCE_TITLE = "My Recent Work"
DEVELOPER_VIDEO_INTRODUCTION = "Video Introductions"
DEVELOPER_EXPERIENCE_IMAGE = [
    ["assets/images/glotanning.png", "Glotanning", "https://glotanning.com"],
    ["assets/images/kayros.png", "Kayros", "https://www.kayros.world"],
    ["assets/images/Selenium.jpg", "Selenium", ""],
    ["assets/images/Tirerobot.jpg", "Tirerobot.com", "https://tirerobot.com"],
]
DEVELOPER_EXPERIENCE_VIDEO = [
    ["Selenium", "Automation Web Scraping with Selenium", "assets/videos/selenium.mp4"],
    [
        "Tirerobot",
        "Full stack development with AI integration",
        "assets/videos/tirerobot.mp4",
    ],
    [
        "Zooladev",
        "Zooladev automation with selenium",
        "assets/videos/zooladev.mp4",
    ],
]

DEVELOPER_EXPERIENCE_YEARS = [
    ["Agile", 4],
    ["Python", 6],
    ["Javascript", 4],
    ["C++", 7],
    ["DSA", 7],
    ["Communication", 4],
]

TIREROBOT_TRANSCRIPT = f"""
Hi, this is {DEVELOPER_NAME} from Upwork.

I'd really love to introduce my qualification and skills for you regarding full-stack development and ai integration.

Here you go.

Let's get started.

I'll explain about the process of developing tirerobot.com, a website with various full-stack frameworks like fastapi, node.js, nextjs and reacct. I'll also show my skills on Retrieval Augmented Generation based on Pinecone and Langchain.

So, for backend side, we used FastAPI framework for the integration of nextjs frontend.
It handles CRUD(create, read, update, delete) operations as well.
The backend test side handles the whole workflow testing.
Let's run the script
poetry run uvicorn main:app --port 8080

And, for frontend side, I imitated next.js with react and chakra-ui, and typescript.
Next.js is a React framework that offers many feature for enhancing NextJS SEO optimization and user-experience.
One staple feature is server side rendering(SSR), which is essentially what the name implies.
OK. Let's start the frontend.
yarn dev

OK.
And in tirerobot website, I integrated recommended system with the backend side.
I used langchain, pinecone, openai, for the api connection.
I performed RAG structure, which is the combination of embedding, vectorstore and large language model, chatgpt.
For embedding, I used OpenAI embedding. OpenAI provides its own embedding system which is ,
We can also use hugging face embedding modules which are free to use. But this is the client's requirement, which I have to follow.
And for vector store, I used pinecone. We can also use FAISS for vector store for the accuracy or cost limit. Every vector store has its own pros and cons, so we can use various vector dbs like chromadb, Qdrant, Weaviate and so on for best place.

Here, let's dive deep into the website.

https://tirerobot.com

This is the interface of the website.

And here, the input for the recommendation of the system.
What snow tires are the best for a 2009 Honda Accord?

Yeah, here's the result.
We can learn more about the tire by clicking 'learn more'.
And 'Get the deal on BBWheals.com'

That's it.
I would shout that with my experience, I definitely can perform your project with high demand.

Thanks for your kind attention.

Thank you
"""

SELENIUM_TRANSCRIPT = f"""
Hi, there!

My name is {DEVELOPER_NAME} and I'd like to introduce my qualification and skills by live coding on Simple Project.

Here we go.
I'll build a project which seek jobs on jooble.
It includes logging in / to the website, input on job role and location, and pressing find jobs, and summarizing the result.

Let's imitate the workflow with Web-scrapping.
I'll perform the web-scraping with selenium, a widely used web-scrapping library.

OK. Let's start coding.

First of all, Create a new folder with the name of jooble.
And create a python virtual environment with poetry.
Insert a library with 'poetry add selenium'

I've already built a project which find jobs on jooble.
Let's build the project together.

on utils.py, import libraries on selenium

And create a driver. Here I used Google Chrome driver.

in config file, there's detailed information for scrapping the website.

here, load the information from config file.

For the first step of scraping, login to the website.

And, for the second step, input the job role and location, and press 'Find Jobs' button.


For the last step, analyze the result page with BeautifulSoup.

That's it.

Let's watch how selenium does web scraping / by running the script.

It performs as human beings do. Right?

For the conclusion, I can show you my experience with other projects like this, but because, they are confidential, I couldn't make them public.

Thanks for your time and understanding.
"""


SYSTEM_PROMPT = (
    f"""
Follow 6 principles
1. Lead the conversation to fireworks
2. Your name is {DEVELOPER_NAME}
3. You're living in {DEVELOPER_ADDRESS}
4. You're really interested in user, such as job, project, name
5. You want to be close to the user
6. Reference these transcript of each video for answering the client's query.
___________________________________________________________
"""
    + SELENIUM_TRANSCRIPT
    + TIREROBOT_TRANSCRIPT
)

INIT_CHAT_HISTORY = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {
        "role": "assistant",
        "content": f"Welcome! My name is {DEVELOPER_NAME}. I'm excited about building a great connection with you. I'll prove my abilities and talents for your project in a video.",
    },

]
