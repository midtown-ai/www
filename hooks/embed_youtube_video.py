import logging, re
import mkdocs.plugins

log = logging.getLogger('mkdocs')

YOUTUBE_REGEX_STR = r"{%\s*youtube\s+\"(https?://www\.youtube\.com/watch\?v=([\w-]+)(?:&t=(\d+))?.*?)\"\s*(.*?)\s*%}"

DEBUG = False
DEBUG_PAGE_URL_FILTER = re.compile(r"blog/[1-9].*")
DEBUG_PAGE_URL_FILTER = re.compile(r"tests/youtube_hook/")

def youtube_url_to_iframe(markdown):
    """
    Parses a Markdown string and replaces all occurrences of
    {% youtube URL %} with the corresponding YouTube iframe embed code.

    Supports Markdown attr_list to customize iframe attributes.

    Parameters:
        markdown (str): The Markdown content containing {% youtube ... %}.

    Returns:
        str: The updated Markdown content with embedded YouTube videos.
    """
    YOUTUBE_REGEX = re.compile(YOUTUBE_REGEX_STR)

    def replace_with_iframe(match):
        video_url = match.group(1)
        video_id = match.group(2)
        start_time = match.group(3)  # Time parameter (t)
        attributes = match.group(4).strip()   # Attribute passed in the markdown element

        default_attrs = {
            "width": "560",
            "height": "315",
            "frameborder": "0",
            "allow": "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
            "referrerpolicy": "strict-origin-when-cross-origin",
            "allowfullscreen": "allowfullscreen"
        }

        # Parse additional attributes from attr_list if provided
        if attributes:
            for attr in attributes.split():
                if "=" in attr:
                    key, value = attr.split("=", 1)
                    default_attrs[key] = value.strip('"')

        # Add start time to the embed URL if present
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        if start_time:
            embed_url += f"?start={start_time}"

        # Build the iframe tag with custom and default attributes
        iframe_attrs = " ".join([f'{key}="{value}"' for key, value in default_attrs.items()])

        return f'<iframe src="{embed_url}" {iframe_attrs}></iframe>'

    return YOUTUBE_REGEX.sub(replace_with_iframe, markdown)


def on_page_markdown(markdown, **kwargs):
    """
    markdown is the complete markdown for the page being processed

    on_page_markdown is executed only once per <page>.md
    """
    page = kwargs['page']
    config = kwargs['config']

    if DEBUG:

        # Process only selected pages when debugging
        if not DEBUG_PAGE_URL_FILTER.match(page.url):
            return markdown

        path = page.file.src_uri                            # e.g. tests/youtube_hook.md
        matches = re.finditer(YOUTUBE_REGEX_STR, markdown)
        for match in matches:
            youtube_markdown = match.group(0)               # entire matched pattern
            youtube_url = match.group(1)
            video_id = match.group(2)
            log.warning(f"Documentation file '{path}' found an instance of a youtube markdown: {youtube_markdown}")
            log.warning(f"- youtube link: {youtube_url}")
            log.warning(f"- video_id: {video_id}")

    updated_markdown = youtube_url_to_iframe(markdown)

    if DEBUG:
        log.warning(updated_markdown)

    # Has markdown changed? If so, return it!
    return updated_markdown
