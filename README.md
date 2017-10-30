# no-refuge
Scripts from the Bureau Local domestic violence refuge investigation

The Python scripts pull out all the areas receiving DCLG funding and those that are not. This allowed us to calculate that 15% of the adult female population were not in an area covered by the fund.

Read the full story here: https://www.thebureauinvestigates.com/stories/2017-10-16/a-system-at-breaking-point

### Step 1: matches.py
This script goes through every local authority in the UK and find the three best possible matches among DCLG funding recipients using fuzzy matching.

The output was then manually checked to see if one of the three best possible matches the script found was indeed a match. If none of the possible matches identified by the script seemed to accuratly match the local authorities (50 cases) we went back and looked for the authority in the list of recipients to make sure it wasn't here. In every case the script was right and the local authority hadn't receive funding.
