import requests
website = "https://api.nfl.com/v2/teams/10044900-2014-de93-fafa-be17820d8386?fs={id,season,fullName,nickName,abbr,cityStateRegion,conference{abbr},division{abbr},draftPicks{round,pickInRound,numberOverall,grade,overView,analysis,personal,nflComparison,bottomLine,draftProjection,profileAuthor,proDayResults,year,relatedContent{title,url},person{id,firstName,lastName,player{position}}},draftNeeds}"
response = requests.get(website)
print(response)     
