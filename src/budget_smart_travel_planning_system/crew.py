import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	StagehandTool,
	SerpApiGoogleSearchTool,
	FirecrawlScrapeWebsiteTool,
	BrowserbaseLoadTool,
	SerplyWebSearchTool,
	JinaScrapeWebsiteTool,
	ScrapeWebsiteTool
)






@CrewBase
class BudgetSmartTravelPlanningSystemCrew:
    """BudgetSmartTravelPlanningSystemCrew crew"""

    
    @agent
    def travel_research_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["travel_research_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    
    @agent
    def flight_search_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["flight_search_specialist"],
            
            
            tools=[				StagehandTool(),
				SerpApiGoogleSearchTool(),
				FirecrawlScrapeWebsiteTool(),
				BrowserbaseLoadTool(),
				SerperDevTool(),
				SerplyWebSearchTool(),
				JinaScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    
    @agent
    def accommodation_expert(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["accommodation_expert"],
            
            
            tools=[				ScrapeWebsiteTool(),
				FirecrawlScrapeWebsiteTool(),
				SerpApiGoogleSearchTool(),
				JinaScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    
    @agent
    def strategic_itinerary_planner(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["strategic_itinerary_planner"],
            
            
            tools=[],
            reasoning=True,
            max_reasoning_attempts=3,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    
    @agent
    def budget_auditor(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["budget_auditor"],
            
            
            tools=[],
            reasoning=True,
            max_reasoning_attempts=3,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    
    @agent
    def travel_plan_consolidator(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["travel_plan_consolidator"],
            
            
            tools=[],
            reasoning=True,
            max_reasoning_attempts=3,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            
        )
        
    

    
    @task
    def research_destination_information(self) -> Task:
        return Task(
            config=self.tasks_config["research_destination_information"],
            markdown=False,
            
            
        )
    
    @task
    def research_flight_options(self) -> Task:
        return Task(
            config=self.tasks_config["research_flight_options"],
            markdown=False,
            
            
        )
    
    @task
    def find_accommodation_options(self) -> Task:
        return Task(
            config=self.tasks_config["find_accommodation_options"],
            markdown=False,
            
            
        )
    
    @task
    def create_comprehensive_travel_itinerary(self) -> Task:
        return Task(
            config=self.tasks_config["create_comprehensive_travel_itinerary"],
            markdown=False,
            
            
        )
    
    @task
    def validate_and_optimize_travel_budget(self) -> Task:
        return Task(
            config=self.tasks_config["validate_and_optimize_travel_budget"],
            markdown=False,
            
            
        )
    
    @task
    def create_final_comprehensive_travel_plan(self) -> Task:
        return Task(
            config=self.tasks_config["create_final_comprehensive_travel_plan"],
            markdown=True,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the BudgetSmartTravelPlanningSystemCrew crew"""

        # Custom manager agent for hierarchical process
        manager_agent = Agent(
            role="Crew Manager",
            goal="Coordinate specialized travel planning agents to produce the most feasible, optimized, and budget-consistent travel plan.",
            backstory="You are an expert travel operations coordinator responsible for managing multiple specialist teams. You analyze user requirements, delegate subtasks intelligently, resolve inconsistencies, and ensure all outputs are cohesive, realistic, and financially optimized.",
            llm=LLM(
                    model="openrouter/openai/gpt-oss-120b:free"
                ),
            allow_delegation=True,
        )

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,


            manager_agent=manager_agent,


            chat_llm=LLM(model="gemini/gemini-2.5-flash"),
        )


