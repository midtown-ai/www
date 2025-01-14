import logging, re
import mkdocs.plugins

log = logging.getLogger('mkdocs')

# https://www.youtube.com/watch?v=zU6eovES53M
# https://www.youtube.com/watch?v=zU6eovES53M&t=420s
# https://youtu.be/zU6eovES53M?t=420
YOUTUBE_RE = r'\{\%[\s]*youtube[\s]*https:\/\/www.youtube.com\/watch?v=([_a-zA-0-9]{2,15})[\s]*\%\}'

def on_page_markdown(markdown, page, **kwargs):
    path = page.file.src_uri
    for m in re.finditer(YOUTUBE_RE, markdown):
        log.warning(f"Documentation file '{path}' contains a youtube link: {m[0]}")
