from base_path import Path
from base_query import BaseQuery
from parameter import Parameter

from ..schema.forum_posts_response import ForumPostsResponse
from ..schema.forum_thread_response import ForumThreadResponse


class ForumThreadId(BaseQuery):
    """
    A collection of paths representing `ForumThreadId`.
    """

    thread = Path(
        "/forum/{threadId}/thread",
        ForumThreadResponse,
        threadId=Parameter("threadId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/forum/{threadId}/thread`: Get specific thread details
    Requires public access key. Contains details of a thread including topic content and poll (if any).

    # Parameters
    - threadId : Thread id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    posts = Path(
        "/forum/{threadId}/posts",
        ForumPostsResponse,
        striptags=Parameter("striptags", "query", required=False, deprecated=False),
        offset=Parameter("offset", "query", required=False, deprecated=False),
        sort=Parameter("sort", "query", required=False, deprecated=False),
        from_=Parameter("from", "query", required=False, deprecated=False),
        to=Parameter("to", "query", required=False, deprecated=False),
        threadId=Parameter("threadId", "path", required=True, deprecated=False),
        timestamp=Parameter("timestamp", "query", required=False, deprecated=False),
        comment=Parameter("comment", "query", required=False, deprecated=False),
        key=Parameter("key", "query", required=False, deprecated=False),
    )
    """
    `/forum/{threadId}/posts`: Get specific forum thread posts
    Requires public access key. Returns 20 posts per page for a specific thread. By default, it uses 'offset', but it's possible to filter posts with 'from' & 'to' parameters.

    # Parameters
    - striptags : Determines if fields include HTML or not (&#39;Hospitalized by &lt;a href=...&gt;user&lt;/a&gt;&#39; vs &#39;Hospitalized by user&#39;).
    - offset : N/A
    - sort : Sorted by the greatest timestamps
    - from_ : Timestamp that sets the lower limit for the data returned. Data returned will be after this time
    - to : Timestamp that sets the upper limit for the data returned. Data returned will be up to and including this time
    - threadId : Thread id
    - timestamp : Timestamp to bypass cache
    - comment : Comment for your tool/service/bot/website to be visible in the logs.
    - key : API key (Public). It&#39;s not required to use this parameter when passing the API key via the Authorization header.
    
    """

    def __init__(self):
        super().__init__(base_path="forum/{threadId}")
