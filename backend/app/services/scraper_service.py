from trafilatura import fetch_url, extract

def fetch_and_extract_text(url: str) -> str | None:
    """
    Fetches a URL and extracts the main article text.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        The extracted main text as a string, or None if extraction fails.
    """
    # 1. Download the webpage
    downloaded = fetch_url(url)
    
    if downloaded is None:
        # Failed to download
        return None

    # 2. Extract the main content
    main_text = extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        no_fallback=True
    )
    
    return main_text