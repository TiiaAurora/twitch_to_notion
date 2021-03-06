# twitch_to_notion 
Changes the export data that Twitch provides into a readable format for Notion

1. Create a folder named "data_raw" and a folder named "data_notion" in the same folder as main.py
2. When you run main.py all files will be formatted into a notion-friendly version. 
3. Create a new notion-database and rename the Tags column into "Game"
4. Chose the option "Merge with csv" and chose your file in data_notion.
5. Filter and hide columns or days as you please. I suggest filtering for stream days only and hiding all properties that are not of interest.

With a notion patch happening between September 2021 and January 2022, you cannot simply merge csv files that contain partially identical data anymore. So when extracting your statistics from twitch, make sure to not include the same data twice or you will have duplicates in your database. We hope this will change in the future.

Unfortunately Twitch does not export the played games with it's files, so this is the only manual work you have to do. Create tags for each game or each category you stream in and it's 2 clicks for every stream day. 
