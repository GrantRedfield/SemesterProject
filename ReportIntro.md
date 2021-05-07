# An Analysis of the Global Terrorism Database
## Introduction

It’s often been said that one should never negotiate with terrorists.  However, in this age of abundant data and documented events, analysts can leverage their expertise along with data to assess how to deal with terrorists and react to attacks.  One of the most comprehensive open-source and unclassified datasets of terrorist attacks is the Global Terrorism Database (GTD).  It is available online so that terrorist violence can be studied and conquered by anyone.  It has been maintained and has steadily grown by a team of researchers as well as technical staff.  As the name suggests, terrorist attacks from all over the world are documented in this database.  It currently holds over 200,000 incidents from 1970 to 2019.  Each entry is meticulously documented with numerical and categorical data, ready for analysis with minimal cleaning needed.  This database defines a terrorist attack as the threat or actual use of illegal force and violence by a non-state actor to attain political, economic, religious, or social goal through fear, coercion, or intimidation.

## Objective

The research team had one objective, which was to find scenarios that are more likely to have an event. The research completed can help drive future actions to mitigate, prepare for, or prevent terrorist like events from happening in the future. There were three areas we focused on in order to complete our objective. For purposes of this analysis, we limited our analysis to events that occurred from 2000 to 2019. The GTD researchers/data collectors noted that there were some [data quality issues] (https://www.start.umd.edu/gtd/downloads/Codebook.pdf) prior to 2000 as data collection methods have changed over the decades.

1. Time: The number of events have fluctuated over 50 years. We aggregated events over years all the way down to specific days of the week to discover patterns and trends.
2. Location: Certain areas of the world have experienced more events than others. We focus on event location to find hotspots in the world.
3. Motive: All terrorist-like events have a motive. We focused on common words found in the motive column for any patterns.
4. Attack Type and Impact: Every terrorist-like event has a means of getting it done. We focused on the most prevalent types of terrorist attack and the types that caused the most fatalities.

## The Dataset

Below is a table of the variables that were found in the Global Terrorism Database (GTD).  The variables highlighted in blue were removed prior to analysis.




[GTD Codebook](https://www.start.umd.edu/gtd/downloads/Codebook.pdf)

The National Counterterrorism Center Mission:

> We lead and integrate the national counterterrorism (CT) effort by fusing foreign and domestic CT information, 
> providing terrorism analysis, sharing information with partners across the CT enterprise, and driving whole-of-government 
> action to secure our national CT objectives.

![September 11, 2001. NYC, NY](https://user-images.githubusercontent.com/47093852/116001333-f99cb500-a5c1-11eb-9331-13f8cdf12ed1.jpg)


Code to create bar chart of attack types: 

`attack = df['attacktype1_txt'].value_counts()`

`attack = attack.to_dict()`   

`fig = plt.figure(figsize=(24, 6))`

`plt.bar(x = attack.keys(), height = attack.values(), )`

`plt.title('Frequency of Attack Types')`

`plt.xlabel("Attack Type")`

`plt.ylabel("Count")`
