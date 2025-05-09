import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from agents.transcript_agent import transcript_agent
from agents.title_agent import title_agent
from agents.description_agent import description_agent
from agents.summary_agent import summary_agent
from agents.blog_composer import blog_composer_agent


# Define the state schema
class BlogState(TypedDict):
    video_url: str
    transcript: Optional[str]
    title: Optional[str]
    description: Optional[str]
    summary: Optional[str]
    blog_post: Optional[str]


# Build the workflow
workflow = StateGraph(BlogState)

workflow.add_node("transcript_node", transcript_agent)
workflow.add_node("title_node", title_agent)
workflow.add_node("description_node", description_agent)
workflow.add_node("summary_node", summary_agent)
workflow.add_node("composer_node", blog_composer_agent)

workflow.set_entry_point("transcript_node")
workflow.add_edge("transcript_node", "title_node")
workflow.add_edge("title_node", "description_node")
workflow.add_edge("description_node", "summary_node")
workflow.add_edge("summary_node", "composer_node")
workflow.add_edge("composer_node", END)

graph = workflow.compile()
