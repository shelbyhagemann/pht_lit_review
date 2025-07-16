# **Rehabilitation through Accessible Mobile Gaming and Wearable** **Sensors**



Dragan Ahmetovic

Antonio Pugliese

Sergio Mascetti
[dragan.ahmetovic@unimi.it](mailto:dragan.ahmetovic@unimi.it)
[antonio.pugliese@studenti.unimi.it](mailto:antonio.pugliese@studenti.unimi.it)

[sergio.mascetti@unimi.it](mailto:sergio.mascetti@unimi.it)
Università degli Studi di Milano, Italy


**ABSTRACT**



Valentina Begnozzi

Elena Boccalandro

[valentinabegnozzi@gmail.com](mailto:valentinabegnozzi@gmail.com)

[boccalandro.elena@gmail.com](mailto:boccalandro.elena@gmail.com)
Centro Emofilia e Trombosi Angelo
Bianchi Bonomi, Fondazione IRCCS

Ca’ Granda, Ospedale Maggiore

Policlinico di Milano, Italy



Roberta Gualtierotti

Flora Peyvandi
[roberta.gualtierotti@unimi.it](mailto:roberta.gualtierotti@unimi.it)

[flora.peyvandi@unimi.it](mailto:flora.peyvandi@unimi.it)
Università degli Studi di Milano, Italy

Centro Emofilia e Trombosi Angelo
Bianchi Bonomi, Fondazione IRCCS

Ca’ Granda, Ospedale Maggiore

Policlinico di Milano, Italy



Play Access is an Android assistive technology that replaces touch­
screen interaction with alternative interfaces, enabling people with
upper extremity impairments to access mobile games, and providing
alternative means of playing mobile games for all. We demonstrate
the use of Play Access to support physical therapy for children
with haemophilia, with the goal of preventing long-term mobility
impairments. To achieve this, we modified Play Access to enable
the use of body movements, recognized using wearable sensors,
as an alternative interface for playing games. This way, Play Ac­
cess makes it possible to use existing Android games as exergames,
hence better targeting patients’ interest.


**CCS** **CONCEPTS**


- **Applied** **computing** → _Health_ _informatics_ ; - **Human-centered**
**computing** → _Accessibility_ _systems_ _and_ _tools_ ; _Mobile_ _devices_ .


**KEYWORDS**


Rehabilitation; Physical therapy; Interaction substitution.


**ACM** **Reference** **Format:**

Dragan Ahmetovic, Antonio Pugliese, Sergio Mascetti, Valentina Begnozzi,
Elena Boccalandro, Roberta Gualtierotti, and Flora Peyvandi. 2021. Rehabili­
tation through Accessible Mobile Gaming and Wearable Sensors. In _The_ _23rd_
_International_ _ACM_ _SIGACCESS_ _Conference_ _on_ _Computers_ _and_ _Accessibility_
_(ASSETS_ _’21),_ _October_ _18–22,_ _2021,_ _Virtual_ _Event,_ _USA._ ACM, New York, NY,
USA, 4 pages. [https://doi.org/10.1145/3441852.3476544](https://doi.org/10.1145/3441852.3476544)


**1** **INTRODUCTION**


For people with haemophilia, hemarthrosis ( _i.e._, bleeding into joints)
is a common condition [ 12 ], and one of the major causes of mobility
impairment and disability [ 18 ]. Prior works highlight that physical
exercise strengthens muscles, ligaments and tendons, improving the
motion range of joints and preventing further articular damage due
to recurrent hemarthrosis [ 9 ]. However, people with haemophilia


Permission to make digital or hard copies of part or all of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
_ASSETS_ _’21,_ _October_ _18–22,_ _2021,_ _Virtual_ _Event,_ _USA_
© 2021 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-8306-6/21/10.
[https://doi.org/10.1145/3441852.3476544](https://doi.org/10.1145/3441852.3476544)



are less physically active in comparison to their peers [ 17 ], and the
COVID-19 pandemic has further reduced their exercise routine [ 8,
13 ]. In particular, maintaining adherence to training regimen was
shown to be difficult for children [7, 10, 16].

As a means of promoting at-home exercises, prior works pro­
pose telerehabilitation [ 5 ] through exergames [ 4, 6 ]. However, de­
signing effective exergames for children with haemophilia is chal­
lenging. The exercises need to be suitable for different patients’
conditions [ 14 ], and the games need to be age-appropriate, engag­
ing [ 11 ], and sufficiently numerous, so that, when a patient gets
bored with a game, a different one can be used. It is also important
to verify that the exercises are performed correctly, in particular
during autonomous usage without a clinical supervisor [15].

To address these challenges, we propose to use existing popular
mobile games as exergames, played using body movements suitable
for physical therapy by children with haemophilia. To achieve this,
we extended _Play_ _Access_ [ 3 ], a system designed to replace touch­
screen interaction with different interfaces, to enable interaction
with the games through body movements, detected with wearable
sensors. For example, extending a leg (Figure 1) can be configured
to trigger a tap on the screen at a given position, making Mario
jump in the Super Mario Run [1] game (Figure 2(e)).


(a) Position 1                  - Kneeling


(b) Position 1                - Leg extension


**Figure** **1:** **Leg** **exercise** **detected** **using** **a** **wearable** **sensor**


ASSETS ’21, October 18–22, 2021, Virtual Event, USA Ahmetovic, et al.


(a) Game configurations (b) Triggering actions (c) Pairing Device and Sensor (d) Gesture selection (e) Event configuration


**Figure** **2:** _**Play**_ _**Access**_ **configuration** **screens**



Input body movements are defined separately for every patient,
in agreement with physical therapists, thus ensuring their appro­
priateness for the rehabilitation goals of each patient. Correct body
movements need to be performed in order to play. Thus, the patient
is stimulated to exercise appropriately. It is also possible to remotely
collect interaction data between the patient and the games [ 2 ], en­
abling clinicians to analyze their adherence to the exercise regimen
and their performance. The _Play_ _Access_ system will be tested by
participants (children with haemophilia) enrolled at the “Angelo
Bianchi Bonomi” Hemophilia and Thrombosis center in Milan, Italy.


**2** **PHYSICAL** **THERAPY** **WITH** _**PLAY**_ _**ACCESS**_


_Play_ _Access_ is an _interaction_ _substitution_ _method_ for replacing touch­
screen interaction with different interfaces. It is implemented on
Android as an Accessibility Service (Figure 2), running in the back­
ground and simulating touchscreen events when specific triggering
actions are entered on alternative interfaces. It is published on
Google Play Store [1], and its source code is available online [2] .

_Play_ _Access_ was first designed for people with upper extremity
impairments [ 3 ], to access mobile games through personalizable
interaction configurations, also adapting to changes in user abilities.
In a new prototype, the system was modified to recognize body
movements through wearable sensors and use them as input for
playing games. Thus, any mobile game can be used as an exergame,
supporting physical therapy in children with haemophilia. _Play_
_Access_ presents three features fundamental for this goal.


**2.1** **Ability** **to** **Interact** **with** **Popular** **Games**


Play Access allows to play existing Android games, including pop­
ular ones (Figure 2(a)), by simulating touchscreen interactions any­
where on the screen. Configured games can be easily replaced with


1 [https://play.google.com/store/apps/details?id=com.carlo.a_cube](https://play.google.com/store/apps/details?id=com.carlo.a_cube)
2 [https://github.com/A-CubeTest/A-Cube](https://github.com/A-CubeTest/A-Cube)



new ones if children get bored. This way, it is easier to stimulate
children to do exercises and stick to the training regimen.

_Play_ _Access_ relies on the user to manually label interface elements
used to play on a screenshot of the game (Figure 2(e)). For the labeled
elements the user can then specify the touchscreen _interaction_ _events_
to perform ( _e.g._, a tap), and the _triggering_ _actions_ required to activate
them ( _e.g._, leg extension).


**2.2** **Custom** **Exercises** **for** **Each** **Patient**


Triggering actions used to replace default touchscreen interactions
are specific to each user. They are defined for every target game and
each game allows multiple configurations, adapting to user abilities,
context and preferences. External switches and voice input were
already available as alternative interfaces and body gestures were
added in the new prototype (Figure 2(b)). Body gestures (Figure 1)
are detected using wearable Bluetooth inertial sensors (Figure 3).
Connected sensors can be selected in the app (Figure 2(c)), and
set to recognize specific body movements. These movements, used
as triggering actions, are decided by clinicians, based on patients’
physical conditions and the rehabilitation goal. In the current ver­
sion of the system, physical therapists, who are also authors of this
paper, have defined a number of different body movements suitable
to be used for exercises, which can be selected as triggering actions
(Figure 2(d)). In future, we will integrate a recording functionality
to enable customization for every body gesture.


**2.3** **Telerehabilitation** **&** **Remote** **Data** **Logging**


_Play_ _Access_ records user interactions and triggering actions, which
are transmitted to a remote server [ 2 ]. In particular, considering
body gesture input, we are able to collect inertial data recorded by
the wearable Bluetooth sensors (Figure 3(c)). This allows clinicians
to assess whether the patients are actually doing rehabilitation and
whether they are performing the movements correctly.


Rehabilitation through Accessible Mobile Gaming and Wearable Sensors ASSETS ’21, October 18–22, 2021, Virtual Event, USA


(a) Sensor on hand (b) Sensor on leg (c) Sensor data


**Figure** **3:** **Wearable** **sensors** **and** **sensor** **data**



It is also possible to assess which games are commonly played,
which replacement interfaces are most frequently used, and to
verify whether different triggering actions are recognized correctly.
For example we can check if the system is able to recognize body
movements confidently or if there is possible confusion between
different recorded inputs.


**3** **PRELIMINARY** **EXPERIMENT** **&** **RESULTS**


We deployed _Play_ _Access_, adapted for use with body gestures, at
the Hemophilia and Thrombosis center “Angelo Bianchi Bonomi”
in Milan, Italy. The system is ready to be tested by physical thera­
pists with children with haemophilia to assess its acceptance and
appreciation by the users, to understand which games are more
appropriate for the rehabilitation goal, and which body gestures
are most suitable and can be efficiently applied for mobile games.

Preliminary results of an initial informal trial with one partici­
pant suggest that the choice of the games, gestures and their com­
binations is critical for the successful use of the system for telerehabilitation. Specifically, it is important to identify games having
compatible interactions with the exercised body movements, in
terms of interaction speed and required reaction time. Erroneous
combinations of games and gestures can make the game too easy
or too hard to play, and the inability to play successfully could
demotivate the user, leading to the abandonment of the training
regimen.


**4** **CONCLUSIONS** **&** **FUTURE** **WORK**


We demonstrate the use of _Play_ _Access_ system as a support for
telerehabilitation of children with haemophilia. Our approach, im­
plemented as an Android Accessibility Service, allows to replace
touchscreen interactions with different interfaces, including per­
sonalized body movements, detected through wearable Bluetooth
inertial sensors. Thus, _Play_ _Access_ can transform existing mobile
games into full-fledged exergames. The usage of popular mobile
games is meant to engage children, improving adherence to the
training regimen and discouraging abandonment. At the same time,
remote data collection can help clinicians to support patients re­
motely, verifying if the exercises are performed correctly.



As future work, we will define a methodology to drive the se­
lection of games suitable for the body movements to exercise. We
will also investigate whether wearable sensors can be replaced by
computer vision body pose detection, as a means of recognizing
body movements. This way, it will be possible to recognize a wider
range of movements, that would otherwise require multiple sensors
to be detected, and the users will just need their mobile phone in
order to exercise. Furthermore, we intend to apply the same gamification approach to other applicative domains, including speech
rehabilitation, for example by defining specific vocal exercises and
use them to control mobile games.


**REFERENCES**


[1] 2021. Super Mario Run on Android Play Store. [https://play.google.com/store/](https://play.google.com/store/apps/details?id=com.nintendo.zara)
[apps/details?id=com.nintendo.zara](https://play.google.com/store/apps/details?id=com.nintendo.zara)

[2] Dragan Ahmetovic, Cristian Bernareggi, Mattia Ducci, Andrea Gerino, and Sergio
Mascetti. 2021. Remote Usage Data Collection and Analysis for Mobile Acces­
sibility Applications. In _International_ _Conference_ _on_ _Pervasive_ _Computing_ _and_
_Communications_ _(PerCom)_ _- Mobile_ _and_ _Pervasive_ _Assistive_ _Technologies_ _Workshop_
_(MPAT)_ . IEEE.

[3] Dragan Ahmetovic, Daniele Riboli, Cristian Bernareggi, and Sergio Mascetti. 2021.
RePlay: Touchscreen Interaction Substitution Method for Accessible Gaming. In
_International_ _Conference_ _on_ _Human_ _Computer_ _Interaction_ _with_ _Mobile_ _Devices_ _and_
_Services_ . ACM.

[4] Elena Anna Boccalandro, Valentina Begnozzi, and Pier Mannuccio Mannucci.
2020. Intelligent game engines for home exercises (exergames) in boys with
haemophilia. _Haemophilia_ (2020).

[5] Elena A Boccalandro, Giuseppe Dallari, and Pier Mannuccio Mannucci. 2019.
Telemedicine and telerehabilitation: current and forthcoming applications in
haemophilia. _Blood_ _Transfusion_ (2019).

[6] Nunzio Alberto Borghese. 2017. Exergaming for Autonomous Rehabilitation. In
_Mathematical_ _and_ _Theoretical_ _Neuroscience_ . Springer.

[7] Nailah Coleman, Blaise A Nemeth, and Claire MA LeBlanc. 2018. Increasing
wellness through physical activity in children with chronic disease and disability.
_Current_ _sports_ _medicine_ _reports_ (2018).

[8] Hortensia De la Corte-Rodriguez, M Teresa Alvarez-Roman, E Carlos RodriguezMerchan, and Víctor Jimenez-Yuste. 2020. What COVID-19 can mean for people
with hemophilia beyond the infection risk. _Expert_ _Review_ _of_ _Hematology_ (2020).

[9] S Harris and LN Boggio. 2006. Exercise may decrease further destruction in the
adult haemophilic joint. _Haemophilia_ (2006).

[10] Christopher J Holt, Carly D McKay, Linda K Truong, Christina Y Le, Douglas P
Gross, and Jackie L Whittaker. 2020. Sticking to It: A Scoping Review of Ad­
herence to Exercise Therapy Interventions in Children and Adolescents With
Musculoskeletal Conditions. _Journal_ _of_ _orthopaedic_ _&_ _sports_ _physical_ _therapy_
(2020).

[11] Seungmin Lee, Wonkyung Kim, Taiwoo Park, and Wei Peng. 2017. The psy­

chological effects of playing exergames: A systematic review. _Cyberpsychology,_
_Behavior,_ _and_ _Social_ _Networking_ (2017).


ASSETS ’21, October 18–22, 2021, Virtual Event, USA Ahmetovic, et al.




[12] Matthew Lombardi and Alfonso C Cardenas. 2018. Hemarthrosis. (2018).

[13] Álvarez Román MT, I de la Plaza Collazo, H De la Corte Rodríguez, Romero Garrido JA, Rivas Pollmar MI, T Cebanu, E González-Zorrilla, P Acuña, EC Merchán,
Blanco Bañares MJ, et al . 2020. Registry of patients with congenital bleeding and
COVID-19 in madrid. _Haemophilia_ (2020).

[14] Claude Negrier, Axel Seuser, Angela Forsyth, Sébastien Lobet, Adolfo Llinas,
M Rosas, and Lily Heijnen. 2013. The benefits of exercise for patients with
haemophilia and recommendations for safe and effective physical activity.
_Haemophilia_ (2013).

[15] Ana Pereira, Duarte Folgado, Francisco Nunes, João Almeida, and Inês Sousa. 2019.
Using Inertial Sensors to Evaluate Exercise Correctness in Electromyographybased Home Rehabilitation Systems. In _International_ _Symposium_ _on_ _Medical_



_Measurements_ _and_ _Applications_ . IEEE.

[16] P Petrini and A Seuser. 2009. Haemophilia care in adolescents–compliance and
lifestyle issues. _Haemophilia_ (2009).

[17] Ana Jéssica Pinto, David W Dunstan, Neville Owen, Eloisa Bonfá, and Bruno
Gualano. 2020. Combating physical inactivity during the COVID-19 pandemic.
_Nature_ _Reviews_ _Rheumatology_ (2020).

[18] E Carlos Rodríguez-Merchán. 1997. Pathogenesis, early diagnosis, and prophy­

laxis for chronic hemophilic synovitis. _Clinical_ _orthopaedics_ _and_ _related_ _research_
(1997).


