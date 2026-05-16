from crewai import Agent, Task, Crew, Process

# 1. وكيل التحليل الاستراتيجي (SIMAS)
strategic_analyst = Agent(
    role='Strategic Intelligence Analyst',
    goal='Transform business insights into technical roadmaps aligned with Vision 2030',
    backstory='Expert in Saudi tech market and AI localization strategies.',
    verbose=True,
    allow_delegation=False
)

# 2. وكيل هندسة المعرفة (Distiller)
knowledge_distiller = Agent(
    role='Knowledge Distillation Engineer',
    goal='Extract actionable intelligence from unstructured data',
    backstory='Specialized in NLP and data mining to find hidden patterns.',
    verbose=True
)

# 3. وكيل الأتمتة (Automator)
workflow_automator = Agent(
    role='Technical Solutions Architect',
    goal='Automate technical workflows and suggest the best tech stack',
    backstory='Expert in Python, FastAPI, and Agentic frameworks.',
    verbose=True
)