import os
from pathlib import Path
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

def load_env_file(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


# Setup
load_env_file()
if os.environ.get("SERPER_API_KEY"):
    search_tool = SerperDevTool()
    tools = [search_tool]
else:
    tools = []

llm = LLM(
    model="watsonx/meta-llama/llama-3-3-70b-instruct",
    base_url="https://us-south.ml.cloud.ibm.com",
    project_id="skills-network",
    max_tokens=2000,
)

research_agent = Agent(
    role='Senior Research Analyst',
    goal = 'Uncover cutting-edge information and insights on any subject',
    backstory = "Expert researcher with extensive in gathering and analyzing information",
    llm = llm,
    tools = tools
)

writer_agent = Agent(
    role = 'Tech Content Strategist',
    goal = 'Craft well-structured and engaging content on research findings',
    backstory = "Skilled content strategist who translates complex topics into clear narratives",
    llm = llm

)

research_task = Task(
    description="Analyze the major {topics}, identifying key trends and technologies",
    agent = research_agent,
    expected_output = "A detailed report on {topics} including trends and impact"
)

writer_task = Task(
    description="Create an engaging blog post based on research findings about {topics}",
    agent=writer_agent,
    expected_output = "A well-structured blog post that effectively communicates the research insights on the topic",
)

crew = Crew(
    agents = [research_agent, writer_agent],
    tasks = [research_task, writer_task],
    process = Process.sequential,
)

#Run
if __name__ == "__main__":
    topic = "Latest Generative AI breakthroughs"
    result = crew.kickoff(input={"topics": topic})
    print(result)
