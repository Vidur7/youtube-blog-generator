from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id: str):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([segment["text"] for segment in transcript_list])


def transcript_agent(state):
    video_url = state["video_url"]
    video_id = video_url.split("v=")[-1].split("&")[0]
    transcript = get_transcript(video_id)
    return {"transcript": transcript}
