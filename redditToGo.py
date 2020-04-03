import praw
import numpy as np
import pandas as pd

#Initiate Read-Only Reddit Instance
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

i = 1
userSubreddit = input('Enter Subreddit to search top 10 submissions: ')
print(userSubreddit)

txt_file = open("preCvs.txt", "w+")

txt_file.write('index, ' + 'Headline, ' + 'SubmissionText ' + 'SubmissionID ' + 'submissionURL ')
for submission in reddit.subreddit(userSubreddit).hot(limit=10):

        #Write 10 Submission into preCVS.txt
        txt_file.write(str(i) + ', ' + submission.title + ', ' + submission.selftext + ', ' + submission.id + ', ' + submission.url + '\n')

        #Write to out.txt in cvs sytle
        df = pd.DataFrame({'Index': [str(i)],
                           'Headline': [submission.title],
                           'submissionText': [submission.selftext],
                           'submisssionID': [submission.id],
                           'submissonURL': [submission.url]})
        df.to_csv('out.txt', index=False)
        i += 1
txt_file.close()

#df.to_csv('out.txt', mode="a", index=False)

#submission = reddit.submission(id='')
#for top_level_comment in submission.comments:
    #print(top_level_comment.body)

#filename = 'preCvs.txt'
#df = pd.read_csv(filename)
#print(df)

