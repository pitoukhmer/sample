"""Script format shared by the writer (Claude) and the renderer."""
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class Card(BaseModel):
    """The on-screen visual for one scene (the middle of the frame)."""
    type: Literal["none", "github", "bullets", "terminal", "number", "badges", "cta"]
    title: Optional[str] = None          # github: repo slug; bullets/terminal: heading; cta: keyword
    subtitle: Optional[str] = None       # github: one-line description; number: label; cta: sub line
    items: List[str] = Field(default_factory=list)  # bullets / terminal lines / badges
    active: int = -1                     # bullets: index to highlight (-1 = none)
    value: Optional[str] = None          # number: the big number, e.g. "94/100"


class Scene(BaseModel):
    speaker: Literal["you", "host"]      # "you" = the viewer stand-in, "host" = the AI mascot
    line: str                            # spoken text (voiceover language)
    subtitle: Optional[str] = None       # on-screen text if different from line (e.g. English subs under Khmer voice)
    card: Card


class VideoScript(BaseModel):
    slug: str                            # kebab-case id used for the output folder
    hook_title: str                      # 2-line title pinned at the top for the whole video
    hook_highlight: str                  # the part of hook_title shown in yellow (2nd line)
    scenes: List[Scene]
    cta_keyword: str                     # one word viewers comment, e.g. "CLIPS"
    post_caption: str                    # caption for TikTok / Reels / Shorts
    hashtags: List[str]
    sources: List[str]                   # URLs every factual claim came from
    claims_to_verify: List[str]          # anything a human must check before posting
