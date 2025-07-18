# **Auditory Displays for Accessible Fantasy Sports**

Jared M. Batterman, Jonathan H. Schuett, and Bruce N. Walker
Georgia Institute of Technology
School of Psychology
+1 (404) 894-8265
jmbatterman@gatech.edu, jschuett6@gatech.edu, bruce.walker@psych.gatech.edu



**ABSTRACT**

for visually impaired users and discuss the accessible fantasy
sports system that we have designed using auditory displays.
Fantasy sports are a fun and social activity requiring users to
make decisions about their fantasy teams, which use real athletes'
weekly performance to gain points and compete against other
users' fantasy teams. Fantasy players manage their teams by
making informed decisions using statistics about real sports
related data. These statistics are usually presented online in a
spreadsheet layout, however online fantasy sports are usually
inaccessible to screen readers due to the use of Flash on most
sites. Our current system, described in this paper, utilizes auditory
display techniques such as auditory alerts, earcons, spearcons,
general text-to-speech, and auditory graphs to present sports
statistics to visually impaired fantasy users. The current version of
our system was designed based on feedback from current fantasy
sports users during a series of think-aloud walkthroughs.


**Categories and Subject Descriptors**
H.1.2 [ **Models and Principles** ]: User/Machine Systems—
_Human_ _factors;_ _human_ _information_ _processing_ ; H.5.1

[ **Information** **Interfaces** **and** **Presentation** ]: Multimedia
Information Systems— _Audio input/output_ ; H.5.2 [ **Information**
**Interfaces** **and** **Presentation** ]: User Interfaces— _Auditory_
_(nonspeech) feedback; user-centered design_ ; J.4 [ **Computer**
**Application** ]: Social and Behavioral Sciences— _Psychology_


**General Terms**

Measurement, Performance, Design, Experimentation, Human
Factors.


**Keywords**
Accessibility, Sports Data, Auditory Displays, Sonification,
Fantasy Football.


**1. INTRODUCTION**

Sports are a cross-cultural phenomenon. Across the world people
clamor into stadiums and living rooms to catch the latest on their
favorite athletes and teams. This worldwide obsession has led to
fans wanting to be more involved. Couple that with elements of
friendly competition and you have the genesis of fantasy sports.
Though it can trace its beginnings to golf aficionados in the postWorld War II era, its modern form began in the 1960s [1]. This
consists of players acting as de facto team managers selecting
players at various positions and being scored based on their
collective team’s performance (positions and scoring vary
depending on the sport) [2]. Despite its humble beginnings as a


Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that
copies bear this notice and the full citation on the first page. To copy
otherwise, or republish, to post on servers or to redistribute to lists,
requires prior specific permission and/or a fee.
ASSETS '13, October 21 - 23 2013, Bellevue, WA, USA
Copyright 2013 ACM 978-1-4503-2405-2/13/10…$15.00.



pen and paper hobby of a select few diehard fans, the advent of
the internet has caused fantasy sports to explode in popularity,
creating a massive industry with over 32 million players in the
United States and Canada alone, and $3-$4 billion dollars of
worldwide economic impact [3]. However, despite its enormous
popularity, online fantasy sports remain inaccessible to blind and
visually impaired users due to the way these sites use CSS image
replacement instead of text, pop-over windows, and inaccessible
tabs to name a few issues. To remedy this, we designed the first
version of an accessible fantasy sports interface, which utilizes an
auditory display of different alerts, text-to-speech, spearcons, and
auditory graphs. The current system focuses on American football
because it is the most popular fantasy sport, but future systems
would incorporate other sports as well.


**2. SYSTEM DESIGN**

Our current system was designed by adding various auditory
display features to a spreadsheet layout that is organized in a way
similar to most online fantasy sports layouts. The difference from
current fantasy sports systems is that ours features auditory
displays that present information using sounds that can be as basic
as a brief alert when a player on your lineup is injured or as
complex as comparing statistics from last season between players.
This use of auditory displays allows for a dynamic and interactive
system that is accessible to visually impaired users.
Our design was informed by think-aloud walkthroughs, which
indicated that individual players’ statuses are of the utmost
importance to users so they know if players need to be changed.
In our system, an alert in the form of an auditory earcon (in this
case a referee’s whistle) [4] was used to convey this information.
Users hear this earcon alert when first opening the page, letting
them know that they should be listening for a more specific alert
as they navigate through their lineup.
For navigating the user’s team lineup page we chose to use
spearcons (algorithmically compressed speech). The use of
spearcons has been found to increase both speed and accuracy
when locating items [5], as well as increase the learning rates
compared to other auditory display techniques like earcons [6]. In
addition, when navigating two-dimensional menus (such as the
spreadsheet layout used by most fantasy leagues for their team
lineup pages) auditory menus with spearcons have been found to
be much more efficient [7]. When the user gets to a specific
player with an alert about him, another earcon notification plays.
The use of different player statistics such as predicted scores
and position rank allow users to make informed decisions about
whom they will keep in play and who they will keep on the bench
in a given week. During the think-aloud walkthroughs we found
that users were interested in different player statistics based on the
types of strategies each user employed. Often users would pull up
graphs within the user interface that allowed them to view trends
in players’ performance over time. In many online leagues users


**Figure 1: This screenshot of our accessible fantasy sports system shows**
**captions that indicate what kind of sonification is being used for each data**
**type.**



have the option to compare players by selecting them and
graphing them together. The accessible auditory display
equivalent to this is the use of auditory graphs. Auditory graphs
are a type of sonification, in that they represent data with nonspeech sounds, usually on the dimensions of pitch and time. In
comparison to visual graphs, auditory graphs usually map data
values (y-axis) onto pitch, and x-axis values onto time.
Auditory graphs have been shown to be powerful tools for
identifying trends and comparing data, but the type of data being
represented has a large impact on how they should be designed
and how effective they end up being. Furthermore, different
populations have been shown to have different representations of
the same concept [8].
In addition to displaying information through sonifications,
additional features have been added to aid accessibility (see
Figure 1). For instance, the _Move Player_ button, common to many
current systems, usually becomes selectable and highlighted in the
rows for positions available for the player being moved. Rather
than require visually impaired users to tab through the entire
lineup listening for eligible players to move, we have included an
auditory drop down menu, which presents only the
players eligible to fill that position. Additionally, navigating team
rosters by column and row should be much easier now, as we
have added the ability to navigate via arrow keys rather than only
being able to scroll from left to right through all cells one at a time
with the tab key.


**3. EVALUATION & FUTURE WORK**

Our current plan is to host our own accessible fantasy football
league this coming season with both visually impaired and sighted
users, in order to fully test our system. This will allow us to
analyze our system in real time and gauge participant feedback.
Although the creation of a system for accessible fantasy sports
fills a desire for providing a fun example of how we can leverage
auditory displays to create an accessible system that properly
displays statistical data, we also see it as a platform for exploring
the perceptual and cognitive ways in which users consume the
information provided. For example, when a user wants to compare
trends in performance between two athletes, understanding how
the user cognitively processes the information will directly affect
how that information display is designed. For example, though
much data has positive valence (i.e. more is better) such as
rushing yards, passing yards, etc.; there is also important and
highly relevant data with negative valence (i.e. less is better), such
as interceptions thrown or number of fumbles. Should these data
be represented differently? Should higher pitches be used for both



higher numbers of rushing yards and interceptions thrown?
Furthermore, what if, given a different context, interceptions are a
good thing (i.e. when looking at defenses)? These issues need to
be researched in order to develop the best possible system for
displaying and comparing statistics using auditory information in
a way that not only makes them accessible to visually impaired
users, but also exciting and useful for sighted users.


**REFERENCES**

[1] Schwarz, A. (2005). _The numbers game: Baseball's lifelong_
_fascination with statistics_ . (p. 175). New York, NY: St.
Martin's Press.


[2] Tozzi, L. (1999, July 5). The great pretenders: Fans find joy
and justice in fantasy sports leagues. _The Austin Chronicle_ .
Retrieved from www.weeklywire.com/ww/07-0599/austin_xtra_feature2.html


[3] Fantasy Sports Trade Association. (2011, June 10). _Fantasy_
_sports participation sets all-time record, grows past 35_
_million players_ . Retrieved from www.fsta.org/blog/fstapress-release/fantasy-sports-participation-sets-all-timerecord-grows-past-35-million-players


[4] McGookin, D. and Brewster S. _Chapter 14: Earcons._ The
Sonification Handbook (Hermann, T., Hunt, A. Neuhoff, J.
eds.), Logos Verlag, Berlin.


[5] Walker, B. N., Nance, A., & Lindsay, J. (2006). Spearcons:
Speech-based earcons Improve navigation performance in
auditory menus. _Proceedings of the International Conference_
_on Auditory Display (ICAD 2006)_, London, England (20-24
June). pp. 63-68.


[6] Palladino, D., & Walker, B. N. (2007). Learning rates for
auditory menus enhanced with spearcons versus earcons.
_Proceedings of the International Conference on Auditory_
_Display (ICAD 2007)_, Montreal, Canada (26-29 June). pp.
274-279.


[7] Palladino, D., & Walker, B. N. (2008). Navigation efficiency
of two dimensional auditory menus using spearcon
enhancements. _Proceedings of the Annual Meeting of the_
_Human Factors and Ergonomics Society (HFES2008)_, New
York, NY (22-26 September). pp. 1262-1266.


[8] Walker, B. N., & Lane, D. M. (2001). Psychophysical
scaling of sonification mappings: A comparison of visually
impaired and sighted listeners. _Proceedings of the Seventh_
_International Conference on Auditory Display ICAD2001_,
Espoo, Finland (28 July-01 August) pp 90-94.


