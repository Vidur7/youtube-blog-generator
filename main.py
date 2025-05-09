from workflow import graph
import os
from datetime import datetime

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=8jLOx1hD3_o"  # A TED talk about AI
    result = graph.invoke({"video_url": video_url})

    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/blog_post_{timestamp}.md"

    # Save the blog post to a file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result["blog_post"])

    print(f"\nBlog post has been saved to: {filename}")
    print("\nPreview of the blog post:")
    print("\n==== FINAL BLOG POST ====\n")
    print(result["blog_post"])
