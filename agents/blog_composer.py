def blog_composer_agent(state):
    return {
        "blog_post": f"""
## {state["title"]}

{state["description"]}

---

### Summary

{state["summary"]}

---

**Transcript Snippet:**  
> {state["transcript"][:1000]}...
"""
    }
