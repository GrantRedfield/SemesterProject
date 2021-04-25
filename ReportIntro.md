# Introduction
## The Global Terrorism Database

It’s often been said that one should never negotiate with terrorists.  However, in this age of abundant data and documented events, analysts can leverage their expertise along with data to assess how to deal with terrorists and react to attacks.  One of the most comprehensive open-source and unclassified datasets of terrorist attacks is the Global Terrorism Database (GTD).  It is available online so that terrorist violence can be studied and conquered by anyone.  It’s been maintained and steadily grown by a team of researchers as well as technical staff.  As the name suggests, terrorist attacks from all over the world are documented in this database.  It currently holds over 200,000 incidents from 1970 to 2018.  Each entry is meticulously documented with numerical and categorical data, ready for analysis with minimal cleaning needed. 

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
