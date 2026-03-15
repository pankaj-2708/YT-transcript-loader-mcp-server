# YT Transcript Loader MCP Server

An MCP server that allows an LLM to load YouTube video transcripts
directly from a video URL.

------------------------------------------------------------------------

## Features

### Tools

-   **extract_video_id_from_url**\
    Extracts the YouTube video ID from a given video URL.

-   **extract_video_transcript**\
    Retrieves the transcript using the extracted video ID.

------------------------------------------------------------------------

### Prompts

-   **prompt_for_notes_generation1**\
    Generates structured notes from a YouTube video link using only the
    transcript.\
    The model must **not add any external knowledge**.

-   **prompt_for_notes_generation2**\
    Generates structured notes from a YouTube video link using the
    transcript.\
    The model **may add additional knowledge**, but those sections must
    be clearly marked.

------------------------------------------------------------------------

## Tech Stack

-   Python
-   FastMCP

------------------------------------------------------------------------

# Setup (Claude Desktop)

## Step 1 --- Clone the repository

``` bash
git clone https://github.com/pankaj-2708/YT-transcript-loader-mcp-server
```

------------------------------------------------------------------------

## Step 2 --- Install dependencies

``` bash
pip install youtube_transcript_api
```

------------------------------------------------------------------------

## Step 3 --- Configure Claude Desktop

Add the following configuration to `claude_desktop_config.json`:

``` json
{
  "YT_transcript_retriever": {
    "command": "uv",
    "args": [
      "run",
      "--active",
      "fastmcp",
      "run",
      "absolute path to main.py inside cloned folder"
    ]
  }
}
```
