from fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi


mcp = FastMCP()


@mcp.prompt
def prompt_for_notes_generation1():
    """prompt for notes generation from a You tube video link with no additional knowlege from model behalf"""
    return """You are an AI agent that generates notes from a YouTube video. Follow the instructions strictly.

Goal
Convert the content of a YouTube video into detailed, well-structured notes using only the video transcript.

Available Tools

YouTube ID Extractor – extracts the video ID from a YouTube URL.

Transcript Retrieval Tool – retrieves the transcript using the video ID.

Workflow
Step 1: Receive a YouTube video URL.
Step 2: Use the YouTube ID Extractor tool to obtain the video ID.
Step 3: Use the Transcript Retrieval tool with the video ID to get the full transcript.
Step 4: Read the transcript carefully.
Step 5: Convert the transcript into structured notes.

Output Structure
Title
Overview
Main Topics
Subtopics / Explanations
Examples (if present)
Key Points / Takeaways

Rules

Use only information present in the transcript.

Do not add external knowledge.

Do not infer or expand beyond the transcript.

Do not hallucinate missing information.

If something is unclear or missing in the transcript, leave it as is.

Output the notes directly in chat in a clear structured format."""


@mcp.prompt
def prompt_for_notes_generation2():
    """prompt for notes generation from a You tube video link with additional knowlege from model behalf"""
    return """You are an AI agent that generates notes from a YouTube video. Follow the instructions strictly.

Goal
Convert the content of a YouTube video into detailed, well-structured notes using the video transcript. The model may add extra explanations when useful, but those must be clearly marked.

Available Tools

YouTube ID Extractor – extracts the video ID from a YouTube URL.

Transcript Retrieval Tool – retrieves the transcript using the video ID.

Workflow
Step 1: Receive a YouTube video URL.
Step 2: Use the YouTube ID Extractor tool to obtain the video ID.
Step 3: Use the Transcript Retrieval tool with the video ID to get the full transcript.
Step 4: Read the transcript carefully.
Step 5: Convert the transcript into structured notes.

Output Structure
Title
Overview
Main Topics
Subtopics / Explanations
Examples (if present)
Key Points / Takeaways

Additional Knowledge
If you add explanations, clarifications, or background knowledge not present in the transcript, place them under clearly labeled sections like:

[Added Explanation]
[Added Context]

Rules

Base the notes primarily on the transcript.

Any information not present in the transcript must be clearly marked as [Added].

Do not mix added knowledge with transcript content without labeling it.

Do not hallucinate missing transcript content.

Output the notes directly in chat in a clear structured format."""


@mcp.tool()
def extract_video_id_from_url(url: str):
    """this function takes youtube video url as input and returns its video id"""
    try:
        video_id = url.replace("https://www.youtube.com/watch?v=", "").split("&")[0]
        return {"status": "ok", "response": video_id}
    except Exception as E:
        return {"status": "error", "response": E}


ytt_api = YouTubeTranscriptApi()

@mcp.tool()
def extract_video_transcript(video_id: str,video_language:str):
    """this function takes youtube video id and video_language as input and returns it's transcript. Video language should be shorhand for orignal language for example hi for hindi and en for english etc"""
    try:
        trans = ytt_api.fetch(video_id, languages=["hi"])
        trans = " ".join([i.text for i in trans.snippets])
        return {"status": "ok", "response": trans}
    
    except Exception as E:
        return {"status": "error", "response": E}

if __name__ == "__main__":
    mcp.run(transport="http", port=8000,host="0.0.0.0")
