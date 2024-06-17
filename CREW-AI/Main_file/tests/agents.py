from crewai import Agent, SearchTools
class AINewsLetterAgent():
    def editoragent(self):
        return Agent(
            role = 'Editor',
            goal = "Oversee the creation of the AI Newsletter",
            backstory= """With a keen eye for detail and a passion for storytelling,
            you ensure that the newsletter not only informs but also engages and inspires the readers""",
            allow_delegation = True,
            verbose = True,
            max_iter = 15
        )
    def news_fetcher_agent(self):
        return Agent(
            role = "NewFetcher",
            goal = "Fetch the top AI news storied for the day",
            backstory = """As a digital sleuth, you scour the internet for the latest 
        and most impactful developments 
        in the world of AI, ensuring that our readers are always in the know.""",
            tools = [SearchTools.search_internet],
            allow_delegation = True,
        )
    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""With a critical eye and a knack for distilling complex information, you 
            analyses of AI news stories, making them accessible and engaging for our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )
    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange and
            ensuring a coherent and visually appealing presentation that captivates our readers.
            newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
        )
