# no-refuge
Scripts from the Bureau Local domestic violence refuge investigation

The Python scripts pull out all the areas receiving DCLG funding and those that are not. This allowed us to calculate that 15% of the adult female population were not in an area covered by the fund.

Read the full story here: https://www.thebureauinvestigates.com/stories/2017-10-16/a-system-at-breaking-point

### Step 1: matches.py
This script goes through every local authority in the UK and find the three best possible matches among DCLG funding recipients using fuzzy matching.

### Step 2: manual clean up
The output was then manually checked to see if one of the three best possible matches the script found was indeed a match. If none of the possible matches identified by the script seemed to accuratly match the local authorities we went back and looked for the authority in the list of recipients to make sure it wasn't here. In every case the script was right and the local authority hadn't receive funding.

### Step 3: verif-match.py
This script verifies if the districts with no matchs, might have received funding through their county. So we go through each local authority and ask (a) did the local authority received funding directly, (b) if not is it a district, (c) if yes did it's county received funding, (d) if yes indicate a match as "via [name of county]". By now we should have a definite number of authority that didn't received DCLG funding.

### Step 4: add-pop-maj.py
We also want to know how many adult women live in those areas, so this script matches the local authorities with their adult women population from the ONS.
