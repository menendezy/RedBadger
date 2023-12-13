
class RedditPosterWithFlair:
    def __init__(self, reddit):
        """ Initialize the RedditPosterWithFlair with a praw.Reddit object """
        self.reddit = reddit

    def submit_text_post(self, subreddit_name, title, content):
        """ Submit a text post to a specified subreddit """
        subreddit = self.reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=content)
        return submission
    
    def fet_flairs(self , subreddit_name):
        flairs = self.reddit.post("r/"+subreddit_name+"/api/flairselector/", data={"is_newlink": True})["choices"]
        return flairs

    def set_flair_and_post(self, subreddit_name, FlairText, FlairId , title , content , linkTitle , linkUrl, useLinkPost):

        # Select a subreddit
        subreddit = self.reddit.subreddit(subreddit_name)

        # Get the flair template ID
        # For example, you can iterate over subreddit.flair.templates
        # and select the appropriate flair based on your criteria

        flair_template_id = FlairId

        # Create a post with flair
        title = title
        selftext = content
        if useLinkPost:
            submission = subreddit.submit(linkTitle, url=linkUrl, flair_id=flair_template_id)
        else:
            submission = subreddit.submit(title, selftext=selftext, flair_id=flair_template_id)
      

        
        