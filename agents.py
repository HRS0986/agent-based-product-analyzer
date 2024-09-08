from crewai import Agent


class AnalyzerAgents:
    def manager_agent(self) -> Agent:
        return Agent(
            role="Project Manager",
            goal="Efficiently manage the crew and ensure high-quality task completion",
            backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
            allow_delegation=True,
        )
    
    def review_collector_agent(self) -> Agent:
        return Agent(
            role="Review Collector",
            goal="Collect and analyze feedbacks and reviews from the customers",
            backstory="You're responsible for collecting customer feedback and reviews about the given product from the internet (e-commerce websites, social media, blogs, etc.)",
            allow_delegation=False,
        )
        
    def sentiment_analyzer_agent(self) -> Agent:
        return Agent(
            role="Sentiment Analyzer",
            goal="Analyze the sentiment of the collected reviews and feedbacks",
            backstory="You're an expert in natural language processing and sentiment analysis. Your role is to analyze the sentiment of the reviews and feedback collected by the Review Collector, providing valuable insights to the Project Manager.",
            allow_delegation=False,
        )
        
    def feature_extractor_agent(self) -> Agent:
        return Agent(
            role="Feature Extractor",
            goal="Extract key features of the product",
            backstory="You're skilled in feature extraction. Your role is to extract key features of the product from the internet and reviews/feedback collected by the Review Collector, providing product features to the Project Manager.",
            allow_delegation=False,
        )
    
    def price_checker_agent(self) -> Agent:
        return Agent(
            role="Price Checker",
            goal="Check and compare the prices of the given product in different e-commerce websites",
            backstory="You're responsible for checking and comparing the prices of the product in different e-commerce websites and give the best price and the location to buy to the Project Manager.",
            allow_delegation=False,
        )

    def comparison_analyzer_agent(self) -> Agent:
        return Agent(
            role="Comparison Analyzer",
            goal="Analyze and compare the product with its competitors",
            backstory="You're an expert in market analysis and product comparison. Your role is to analyze and compare the product with its competitors, providing valuable insights to the Project Manager.",
            allow_delegation=False,
        )
    
    def summary_generator_agent(self) -> Agent:
        return Agent(
            role="Summary Generator",
            goal="Generate a summary report of the product analysis",
            backstory="You're skilled in summarization and report generation. Your role is to generate a summary report of the product analysis, highlighting key insights and recommendations for the Project Manager.",
            allow_delegation=False,
        )