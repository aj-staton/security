# Venemy -- An Intelligence Tool for Venmo

Venmo's (40 mil users) transactions are public by default. This creates many opportunites for intelligence gathering. Venmo provided one of the first opportunities to publicly view financial transactions. Sadly, there is no publicly documented API; however, every user is issuded an API key.

Information people make public on Venmo:
* Travel -- easy to tell if someone leaves for vacation (burglary potential)
* Marriage Plans
* Roommates
* Gambling -- can affect your Security Clearance
* Drug Purchases -- In a small survey of drug users, ~40% of millenial drug users admitted to purchasing drugs through Venmo.

[Neo4j](https://www.neo4j.com) Graph Database, using Cyber Query Language, can be used to create people as nodes, and link them to other friends/transactions. Venemy uses Neo4j to correlate data between users.

#### Venmo's Privacy Policy
In Venmo's privacy policy, when you import your contacts, it allows Venmo to create profiles and data for all persons in that list:
* _"Venmo will use the names, phone numbers and email addresses of your contacts to friend those that use Venmo, help you invite those that don't, improve your search results and as noted in our Privacy Policy"_

Meaning, if a person with a lesser online footprint, or _no_ online footprint is in the contact list, they will be tied to the public friends of the user. 

Expanding on your OSINT:
* When you link accounts to facebook (as you can with Venmo), you are given a unique account identifier for the various accounts ties to your facaebook.com social account. This identifier can be used to link you to all of the other accounts that you have connected to Facebook.

## Credits
* This presentation was given by Michael Portera on November 9th, 2019 at B-Sides Charleston.
* Recommendation from the speaker: do the TraceLabs MissingPersonsCTF, where flags are given for information on missing people.
* [SRC Repo](https://github.com/mportatoes/venemy)
