# Taste Tracker

## Inspiration
We are all big fans of Spotify and use it in our daily lives. Everyone's favorite time of year is when Spotify Wrapped comes around, a summary of your past year of listening. Many web apps exist to analyze stats, but we decided to have a little fun with it. 

## What it does
The user signs into their Spotify, allowing our app to read their top 50 songs. These songs are sent to four different LLM "personalities" using Hugging Face, which returns their judgment of the user's songs. 

## How we built it
Spotify API is language agnostic, but we used Spotipy for seamless Python integration. Once the Spotify end was handled, we also created a function and prompts for the Hugging Face LLM calls. To put it all together, we used HTML/CSS and Flask to create a web app. We also used Aesprite to create original sprites for all of the judges.

## Challenges we ran into
One big hurdle was deciding how we would make this a web app. The first few hours of development were spent trying to figure out what tech stack to use, making sure we didn't develop in a way that would bite us later. Interfacing with Spotify and Hugging Face proved to be a bit of a struggle. The returned datatypes were a bit obtuse looking from the outside in, but once we dug into a debug, we were able to extract all relevant data. 

## Accomplishments that we're proud of
We really love the responses that our judges give. We find them to be quite humorous, and we hope you will, too :)

## What we learned
Our big takeaway is basic web development skills, from the basic skeleton of a program to HTML/CSS work. Much of the work was split up between team members, but all of us learned a little about what the others were working on as we went. Many of us were familiar with API usage, so most of our problem-solving occurred on the front end.

## What's next for TasteTracker
We would like to have our app hosted so it does not have to be run locally and can be used by anyone, anywhere.
