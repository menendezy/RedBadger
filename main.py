import traceback
import praw
from redposterwithflair import RedditPosterWithFlair
from redcom import RedCom
from logger import Logger
import os
import sys

# Path to external settings file
external_settings_path = 'newsettings.py'
#print(f"Looking for settings.py at: {os.path.abspath(external_settings_path)}")

# Check if the external settings file exists
if os.path.isfile(external_settings_path):
    sys.path.insert(1, os.path.dirname(external_settings_path))
    import newsettings
    settings = newsettings
    print("newsettings")
else:
    import defaultsettings
    settings = defaultsettings
    print("defaultsettings")

# Set environment variables for PRAW configuration
os.environ['praw_client_id'] = settings.CLIENT_ID
os.environ['praw_client_secret'] = settings.CLIENT_SECRET
os.environ['praw_user_agent'] = settings.USER_AGENT
os.environ['praw_username'] = settings.USERNAME
os.environ['praw_password'] = settings.PASSWORD


log_directory = settings.LOG_DIRECTORY 
logger = Logger(log_directory)


RedComs = [RedCom(name, arg2, arg3 , arg4 ) for name, arg2, arg3, arg4  in settings.RedComs]

RedCom0 = RedCom("bagertester","9d656802-9904-11ee-8b5e-4a285bc43423","Test34")

DebugRedComs = [RedCom0]

try:
    reddit = praw.Reddit(
        client_id=os.environ.get('praw_client_id'),
        client_secret=os.environ.get('praw_client_secret'),
        user_agent=os.environ.get('praw_user_agent'),
        username=os.environ.get('praw_username'),
        password=os.environ.get('praw_password')
    )
    print("PRAW initialized successfully")
except Exception as e:
    print(f"Error initializing PRAW: {e}")


RedPoster = RedditPosterWithFlair(reddit)


#Var-------------------------------------

if settings.UseDebug:
    RedComs = DebugRedComs

title = settings.POST_TITLE

content = settings.POST_CONTEXT

for redCom in RedComs:
    subreddit_name = redCom.name
    flairText = redCom.flairname
    flairId = redCom.flairId
    try:
        #Post with Flair ----------------------------------------
        print(subreddit_name+" Posting with Flair ...") 
        logger.log(subreddit_name+" Posting with Flair ...")

        RedPoster.set_flair_and_post(subreddit_name , flairText , flairId , title , content )
        
        print(subreddit_name+" Posting with Flair done") 
        #--------------------------------------------------
    except Exception as e:
        # Log the exception
        error_message = f"An error occurred: {e}\n"
        error_traceback = traceback.format_exc()
        logger.log(error_message + error_traceback)

    finally:
        logger.log(subreddit_name+" Posting with Flair done")

logger.close