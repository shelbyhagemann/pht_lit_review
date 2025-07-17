Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland

# **HoloLearn: Wearable Mixed Reality for People with** **Neurodevelopmental Disorders (NDD)**


**Beatrice Aruanno** **[(1)]** **Franca Garzotto** **[(2)]** **Emanuele Torelli** **[(2)]** **Francesco Vona** **[(2)]**



(1) Department of Mechanical Engineering - Politecnico di Milano - Milano - Italy
beatrice.aruanno@polimi.it

(2) i3lab - Department of Electronics, Information, and Bioengineering - Politecnico di Milano - Milano - Italy
franca.garzotto@polimi.it; emanuele1.torelli@mail.polimi.it; francesco.vona@mail.polimi.it

**ABSTRACT** **INTRODUCTION**
Our research explores the potential of wearable Mixed The goal of our research is to investigate the potential of
Reality (MR) for people with Neuro-Developmental _wearable Mixed Reality_
Disorders (NDD). The paper presents HoloLearn, a MR those based on HoloLens technology, to offer new forms of
application designed in cooperation with NDD experts and interventions for people with
implemented using HoloLens technology. The goal of _Disorders_ .
HoloLearn is to help people with NDD learn how to perform

Neurodevelopmental Disorders (NDD) is an umbrella term

simple everyday tasks in domestic environments and

that comprises various forms of disability ascribed primarily

improve autonomy. An original feature of the system is the

to the functioning of the neurological system and the brain.

presence of a virtual assistant devoted to capture the user’s

Included in NDD we find for example Attention
attention and to give her/him hints during task execution in

Deficit/Hyperactivity Disorder (ADHD), Autism, Learning

the MR environment. We performed an exploratory study

Disabilities, and Intellectual Disability. Most individuals

involving 20 subjects with NDD to investigate the

with NDD experience various and often co-occurring

acceptability and usability of HoloLearn and its potential as

difficulties in different areas, such as language and speech,

a therapeutic tool. HoloLearn was well-accepted by the

memory, learning, social behavior, and motor skills [42]. The

participants and the activities in the MR space were

occurrence of some disorders in the NDD spectrum,

perceived as enjoyable, despite some usability problems

specifically Autism and ADHD, has been increasing over the

associated to HoloLens interaction mechanism. More

last four decades [42]. The treatment of NDD involves a

extensive and long term empirical research is needed to

combination of professional therapy, pharmaceuticals,

validate these early results, but our study suggests that

home-based and school-based programs. Better results are

HoloLearn could be adopted as a complement to more

achieved when interventions start in

traditional interventions. Our work, and the lessons we

studies show that therapies can also be beneficial to adults

learned, may help designers and developers of future MR

[14].

applications devoted to people with NDD and to other people
with similar needs.



**INTRODUCTION**
The goal of our research is to investigate the potential of
_wearable Mixed Reality_ (MR) applications, particularly
those based on HoloLens technology, to offer new forms of
interventions for people with _Neuro-Developmental_
_Disorders_ .



**AUTHOR KEYWORDS**
Augmented Reality; Mixed Reality; HoloLens; Holograms;
Neuro-developmental Disorders; Virtual assistant.


Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for profit or commercial advantage and that copies
bear this notice and the full citation on the first page. Copyrights for
components of this work owned by others than ACM must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to
post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from Permissions@acm.org.

_ASSETS '18,_ October 22–24, 2018, Galway, Ireland
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-5650-3/18/10…$15.00
https://doi.org/10.1145/3234695.3236351



Neurodevelopmental Disorders (NDD) is an umbrella term
that comprises various forms of disability ascribed primarily
to the functioning of the neurological system and the brain.
Included in NDD we find for example AttentionDeficit/Hyperactivity Disorder (ADHD), Autism, Learning
Disabilities, and Intellectual Disability. Most individuals
with NDD experience various and often co-occurring
difficulties in different areas, such as language and speech,
memory, learning, social behavior, and motor skills [42]. The
occurrence of some disorders in the NDD spectrum,
specifically Autism and ADHD, has been increasing over the
last four decades [42]. The treatment of NDD involves a
combination of professional therapy, pharmaceuticals,
home-based and school-based programs. Better results are
achieved when interventions start in childhood, but some
studies show that therapies can also be beneficial to adults

[14].


Mixed Reality (MR) is the richest form of Augmented
Reality (AR). AR experiences take place in a real-world
environment whose elements are “augmented” by computergenerated overlaid information (e.g. visual and auditory). In
AR, the user sees what is in front of him but with an added
virtual layer on top of it, which adds new elements to the
natural environment or masks portions of it. MR provides a
stronger merging of real and virtual reality. Instead of just
seeing a set of digital elements overlaid on the view of the
physical world, in MR the user can interact with an artificial
environment where the surrounding physical space, realistic
renderings of physical materials, and digital objects, all coexist and communicate in real time [13]. In _wearable_ Mixed
Reality, the real-virtual environment is experienced through
a head mounted display (Figure 1).


This paper presents _HoloLearn_, an application for Microsoft
HoloLens [27] - the most recent and advanced example of
commercial wearable MR technology. HoloLearn addresses
young adults with NDD and has been designed in
cooperation with psychologists and therapists. The goal of
HoloLearn is to promote the understanding of some basic



40


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



tasks that are typical of domestic routines (e.g. table setting
and garbage collection) and to help these people improve
autonomy in everyday life.


The paper describes the design rationale of HoloLearn and
its technical implementation. We then report an exploratory
empirical study that involved 20 people with various forms
of NDD, who used HoloLearn at a care center under the
supervision of their caregivers. The study results highlight
the limitations as well as the potential of HoloLens
technology for this target group. We also discuss the main
lessons learned during this project, which could benefit
designers and developers of future wearable Mixed Reality
applications for people with NDD and similar target groups.


**Figure 1: Example of Mixed Reality with Microsoft HoloLens;**
**on the background, what the user sees on the head-mounted**
**device.**


**STATE OF THE ART**


**Virtual, Augmented, and Mixed Reality for People with**
**NDD**
Several studies explore the use of virtual worlds in
interventions for people with NDD, particularly those with
Autism [4, 6, 7, 8, 10, 11, 43]. Compared to traditional
therapeutic or educational materials, VR contents offer safe
environments for learning that can be customized to the
specific needs of each individual [37, 38]. VR has the
potential of stimulating the imagination and promoting
generalization [23, 24]; several studies report successful
transfer from the skills learned in VR to real life situations

[25]. When the virtual world is displayed on a wearable
device, the entire user’s field of view is “embedded” in the
artificial environment; this immersion effect removes the
distractions from the external world and helps individuals to
remain focused on the assigned task [15, 38].


The first generation of VR headsets had some technological
weaknesses, e.g. poor viewing angles, high latency, and
weight [38]. Current Head-Mounted Displays (HMDs) are
much more comfortable [36], and wearable VR experiences
are starting to be experimented in the treatment of NDD [16,
17, 20, 39], especially for children. The _Wilcard_ project [21],
for example, transforms the stories of some children’s books
that are used in NDD therapy into immersive VR contents
enriched with interactive affordances and simple
gamification features. These VR experiences require only a
smartphone mounted on a low-cost VR viewer (Google
cardboard). In [22], the authors exploit a similar approach,



using contents inspired by “Social Stories”, i.e. short
narratives describing everyday life situations that are widely
used as a therapeutic method among people with Autism.


The benefits of AR among subjects with NDD have been
much less explored than VR ones. AR is thought to have the
advantage of maintaining a real, familiar environment during
the virtual experience. Some AR applications (e.g. _Empower_
_Me_ [9] by Brain Power) use Google Glass and aim to teach
practical life skills to children and adults with Autism, such
as language, emotional understanding, eye contact,
conversational skills, and behavior control [5, 26].


Some AR technologies for NDD enable the user to interact
with VR contents using body movements [19]. This
interaction paradigm is thought to promote embodied
learning and to enhance engagement. Examples are
_Pictogram Room_ [12] and _Shape Game_ [19]. These systems
provide different game-based activities but share the goal of
helping people with Autism to develop their body schema
and imitation skills by performing playful tasks based on
body postures and movements of legs or arms.


Very little is known on how to exploit MR in general, and
HoloLens technology in particular, for people with NDD. To
our knowledge, the only HoloLens application that addresses
people with cognitive disability is the one reported in [3].
This system addresses people suffering from Alzheimer's
disease, it was designed in cooperation with neurologists and
geriatric doctors and consists of a set of tasks that aims to
improve short-term memory and spatial memory, in an
attempt to slow down mental decline.


**Microsoft HoloLens**
HoloLens - the Microsoft flagship device for wearable MR

[27] - is a self-contained, holographic computer mounted on
a headset (Figure 2) and is equipped with specialized
components, like multiple sensors, advanced optics, and a
custom holographic processing unit. HoloLens enables the
user to interact with digital contents rendered by holograms
that are placed in the real environment where the user is
located. Using spatial mapping techniques, the device
captures the information about the physical space, identifies
planes such as tables, floor, walls, and ceiling [31], and
generates a fully realistic rendering of the surrounding
environment where interactive holograms representing real
objects or other kinds of interactive digital contents can be
placed.


HoloLens supports various interaction modes, and visual or
audio effects can be associated with interactive items (e.g.
hologram animations) and also with the environment as a
whole (e.g. spatial sound [32]) as responses to the
interaction.


- _Gaze_ . By changing gaze direction, the user updates
his/her view of the environment. A cursor appears on the
gaze focus and follows the gaze movement [28].
Technically, the built-in sensors track only head
orientation and movements (i.e. there is no eye



41


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



tracking). The user’s gaze focus is determined by head
orientation, the changes of the pointer position and the
space view correspond to head movements.

- _Gestures_ . Hand gestures are used to interact with
holograms in the surrounding physical space. The main
gesture is _air-tap_ of _thumb and index_ . “Instantaneous”
air-tap selects and activates the gazed interactive
hologram on which the cursor is placed, triggering the
associated feedback. “Sustained” air-tap performs
drag&drop. In this case, after the initial air-tap on the
gazed hologram (“selection”), fingers must be kept close
to move the selected item to the desired position and
must be opened to “drop” the element there [29].

- _Voice_ . Voice commands can be defined to give
instructions to the application and interact with
interactive items [30].

- _Clicker._ A physical button-shaped controller connected
to the headset via Bluetooth can be used in place of airtap to select and move interactive elements [34].


**Figure 2: HoloLens device [27]**


**HOLOLEARN DESIGN**


**User Needs and Requirements**
The design process of HoloLearn involved two therapists
(psychologists) who work at “ _Fraternità e Amicizia”_, a care
center in Milan that serves over 80 individuals with NDD.
Three preliminary focus groups with these specialists were
devoted to understand how MR could help these people. The
therapists pinpointed that many education activities
performed at the center attempt to make these people more
autonomous (or at least less dependent on caregivers) and
highlighted the need to help these people learn how to
perform the basic everyday life tasks.


These considerations informed the definition of the general
goals of HoloLearn: to use MR in order to provide virtual
environments for people with NDD which are the same as
real-life ones and enable them to practice tasks associated
with their domestic activities.


As a starting point for the design of HoloLearn, we focused
on two activities: _Laying the table_ and _garbage collection_ .


These activities involve movements in the physical space and
the actions of grasping/moving/placing objects and can be
simulated using the built-in features of HoloLens



technology. The physical space where the MR experience
takes place - the one sensed and digitally rendered by the
device - should contain the physical elements functional to
the designed tasks, for example a table for the “Laying the
table” activity. The space view is then enhanced with
holograms which represent the other elements needed for the
tasks, for example objects that need to be “grasped” and
placed in the proper position using gaze focus, gaze
movement, and air-tap.


Another requirement indicated by the therapists was to offer
additional elements in the MR space that attract the user’s
attention to objects and target locations, help the user
complete the task by providing step-by-step instructions, and
promote engagement and fun. To this end, we decided to
introduce an animated holographic character into the MR
experience which plays the role of a cheerful virtual
assistant. According to the therapists, the virtual assistant
should evoke something familiar to users, such as a cartoon
character. We considered a number of options, and asked the
people attending the center to vote their favorite one. The
“most popular” turned out to be a _Minion_ (from the movie
_Despicable Me_ ); therefore, we decided to model the shape of
the virtual assistant on this.


Finally, the therapists pinpointed the importance of making
the application as customizable as possible, to enable them
to address the different and evolving needs of each person
with NDD. For each activity, we designed different
configurations corresponding to different levels of task
complexity which the therapist can choose before a session
by setting some features of the activity, such as the presence
or absence of the virtual assistant, the number of interactive
digital objects in the MR space, and their visual
characteristics.


**“Laying the table” activity**
The purpose of this activity is to teach the user to lay a real
table by placing various objects (e.g. virtual glasses, plates,
cutlery, or bottles) on it, in the proper position.


**Figure 3: “Laying the table” activity**


The MR environment consists of the space surrounding the
user (which must include a table) and some holographic
objects, which appear at one edge of the table (of course
holograms should not “float” in the air), while some areas are



42


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



highlighted on the other edges (Figure 3). To complete the
task, the user must move all the holograms to the correct
positions, which correspond to the highlighted areas, by
gazing each holographic object to move the cursor on it, and
then dragging and dropping the grasped element using
“sustained” air-tap.


Using a simple menu (Figure 4), the therapist can configure
the level of complexity of the activity, setting the number of
people for whom the table must be prepared (up to three
people, to avoid having too many elements on the table,
which could be confusing) and choosing the types of objects
to be placed. For instance, in the “easy” configuration, the
participant should set the table using basic objects such as
glasses, cutlery, plates and one bottle of water. In a more
complex configuration, there are additional objects such as
cans of beverages, or more glasses of different shapes. In the
most advanced configuration, the number of objects is larger,
and their shape and color are more complex.


We exploited the spatial mapping function of HoloLens to
create the MR space at the beginning of each session. The
first operation performed by the application before the user
can start the activity is to scan the surrounding environment,
until a sufficiently large table is detected (with an area of at
least one square meter), to place the holograms on it, and to
highlight the destination areas on the table surface.


**Figure 4: “Laying the table” settings menu**


**“Garbage collection” activity**
The purpose of this activity is to help the user learn how to
perform garbage collection properly.


The MR environment consists of the room where the user is
located, different holographic bins placed on the floor - a
paper bin, a glass bin and a plastic bin (Figure 5), and some
pieces of trash located nearby. The goal of the activity is to
move each holographic trash object inside the correct bin.


As in the “Laying the table” activity, the application uses the
spatial mapping feature of HoloLens to scan the surrounding
environment, to identify the floor and to place the objects in
a meaningful way.



To ensure also in this activity a high level of customization,
the therapist can choose the number of bins and the number
of trash items that the user must throw into them.


**Figure 5: “Garbage collection” activity**


**Virtual assistant**
The virtual assistant is animated (to attract attention and
promote engagement) and has various behaviors, depending
on the difficulty the therapist wants to set in the activity.


We have currently implemented three configurations for the
virtual assistant.


In the _static_ one, the character stays idle, giving feedbacks
only after the user places an object in a target position: if the
position is correct it looks happy, otherwise it expresses
disappointment.


In the _dynamic_ configuration, the virtual assistant waits for a
while, then it walks to the nearest object and moves its arms
to point at it, in order to encourage the user to grasp and drag
it (Figure 6). If the user is dragging an object but doesn’t
know where to put it (e.g. because he/she is moving it in the
wrong direction, the assistant walks towards the position in
which the item should be placed, and points at it.


In the _reactive_ mode, the virtual assistant remains idle until
the user says something like “help me”, and then walks either
to the nearest object or to the nearest target position.


**Figure 6: Virtual assistant in action**


**IMPLEMENTATION OF HOLOLEARN**
The main software tools we used in the implementation of
HoloLearn are Unity [40] and Visual Studio [35]. HoloLearn
scripts were coded in C#, which is more supported than other



43


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



programming languages by both Microsoft and Unity
technical documentation.


The application source consists of Unity assets and C#
scripts. Unity assets are managed by the Unity engine and
include the 3D models used for the holograms, the UI
elements, and the Mixed Reality Toolkit [33]. The Mixed
Reality Toolkit is a collection of components provided by
Microsoft which accelerate the development of applications
for Microsoft HoloLens and other Windows Mixed Reality
headsets. The Toolkit is organized in different modules, each
of them containing scripts and Unity prefabs that facilitate
the implementation of the interaction paradigm of HoloLens
and provide other useful features. For instance, the input
module contains scripts that interpret inputs such as gaze,
gesture, and voice. The spatial mapping component is used
by HoloLearn to map the real world into the MR
environment (Figure 7). We also exploited some of the UX
controls provided by the Toolkit (for instance sliders,
buttons, checkboxes, etc.) to implement the HoloLearn

menu.


**Figure 7: Spatial mapping**


To develop the virtual assistant, we found some useful
animations on Mixamo.com service by Adobe [1] and
applied them to the 3D model of the virtual character. We
managed model animations by means of the Unity animation
management tool [41]. The behavioral rules of the assistant
are defined by a state machine implemented in C#. To
provide the proper hints, assistant animation changes
according to what the user is doing. For example, if the user
drags an object, the assistant state becomes “walk”, and the
character walks towards the nearest target position.


Visual Studio is used to load and compile the code from the
PC where the application is developed into the HoloLens
device.


HoloLearn is currently executed as a client-side application,
and all the data are managed by the application itself. For
instance, it is possible to save the configuration parameters
set for each activity performed as persistent data and re-use
them in following application executions.



HoloLens supports UWP (Universal Windows Platform)
applications, so our final product can be deployed on the
Microsoft Store.


**EXPLORATORY STUDY**
We performed an exploratory study on HoloLearn at the
“ _Fraternità e Amicizia_ ” center involving _20_ subjects with
different disorders in the NDD spectrum, and their 3
caregivers.


**Goal of the study and research questions**
To our knowledge, no published research explores the use of
HoloLens technology among people with NDD; little is
known on how these people behave when they are exposed
to HoloLens devices and applications.


The first goal of our study was therefore to investigate _device_
_acceptability_, i.e. if subjects with NDD (hereinafter referred
to as “ _users_ ”) would accept to wear the HoloLens headset,
and _usability_, i.e. if they would have difficulty in
understanding and using the main interaction mechanism
(air-tap gesture coordinated with gaze).


In addition, we wanted to explore some HoloLearn-specific
aspects, e.g. the degree of _complexity of the user tasks and_
_the role of the virtual assistant_ . Finally, we investigated how
users would perceive the overall experience with HoloLearn
( _likeability_ and _satisfaction_ ).


We organized our main _research questions_ along the above
lines:


_Device Acceptability_ :

- Q1: Do users accept to wear and use the HoloLens
device?


_Usability of the interaction mode_ :

- Q2: Do users understand the air-tap gesture, and can
they perform it?

- Q3: Do users understand how to stare at holograms with
their gaze?

- Q4: Are users able to coordinate gaze and air-tapping?


_Task complexity:_

- Q5: Do users understand the goal of the tasks?

- Q6: Were users able to contextualize the tasks in the MR
space, i.e. to understand that they are performing the
tasks in a virtual environment and not in a real space?


_Virtual assistant role_ :

- Q7: Do users try to interact with the virtual assistant?

- Q8: Do users understand the role of this character?


_Likeability and satisfaction_ .

- Q9: Do users have fun using HoloLearn?

- Q10: Are users satisfied with this experience?


**Participants**
The study involved two groups of people who attend the care
center on a regular basis, are aged 16-43 and have different
disorders in the NDD spectrum. The _severity_ level was



44


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



homogeneous within each group: _severe_ for Group 1 and
_moderate_ for Group 2.


“Severity” is a clinical measure designed to be used at initial
evaluation to inform treatment planning, to establish a
baseline for comparison, and to monitor changes. Severity
takes into account various aspects, such as the intensity,
frequency and the duration of symptoms associated with a
specific disorder in the NDD spectrum.


Criteria and guidance to rate severity are provided in the
DMS-5 [2]. In intellectual disability, the “severe” level for
people in the age range of the participants in our study is
characterized by little understanding of written language and
concepts involving numbers, quantity, time and money,
limited spoken language, and the need for supervision at all
time for all daily-living activities including meals, dressing,
personal hygiene.


The “moderate” level is associated with limited academic
skills (reading, writing, maths), assistance required to
complete conceptual day-by-day living tasks, difficulty in
perceiving and interpreting social cues accurately, and the
need of reminders and instruction in practical tasks involving
eating, dressing and hygiene.


Group 1 (n=11, average age = 27,27, SD=5,04) is described
in Table 1 _._ Group 2 (n=9; average = _31,33_, SD=5,67) is
described in Table 2.


|ID|Gender|Age|Disorder|Sessions<br>attended|
|---|---|---|---|---|
|M1<br>M2<br>M3<br>M4<br>M5<br>M6<br>M7<br>M8<br>M9|F <br>M <br>M <br>F <br>M <br>F <br>M <br>F <br>F|35<br>25<br>31<br>36<br>29<br>28<br>28<br>43<br>27|Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Intellectual disability|1 <br>1 <br>1 <br>1 <br>1 <br>1 <br>1 <br>1 <br>1|












|ID|Gender|Age|Disorder|Sessions<br>attended|
|---|---|---|---|---|
|S1<br>S2<br>S3<br>S4<br>S5<br>S6<br>S7<br>S8<br>S9<br>S10<br>S11|M <br>M <br>F <br>M <br>M <br>F <br>M <br>F <br>F <br>F <br>M|25<br>34<br>24<br>27<br>28<br>28<br>16<br>33<br>24<br>31<br>30|Intellectual disability<br>Intellectual disability<br>Intellectual disability<br>Asperger syndrome<br>Intellectual disability and<br>psychosis<br>Intellectual disability<br>Prader-Willi syndrome<br>Intellectual disability<br>Pervasive developmental<br>disorder<br>Intellectual disability<br>Down syndrome|1 <br>1 <br>1 <br>1 <br>1 <br>2 <br>2 <br>2 <br>2 <br>2 <br>2|


**Table 1: Study Participants - Group 1 (severity level = severe)**



**Table 2: Study Participants - Group 2 (severity level =**

**moderate**


**Procedure**
Each session took place at the therapeutic center in a room
that was familiar to all participants (Figure 8). The activity
selected for the study was _Garbage collection_, which the
therapists considered easier than _Laying the table_ since it
involves simpler movements. During a session, the person
with NDD used HoloLearn for approximately 10 minutes
with the assistance of his/her caregiver; an additional
therapist while two members of the university team
participated as observers and took notes.


**Figure 8. Using HoloLearn during the exploratory study**


We connected HoloLens to a PC and a large display screen,
so that all the people in the room could see what the current
user was seeing inside the device, and the caregiver could
provide more contextualized help when needed.


Before starting the activity, the therapist explained its goal
and told the user what he/she had to do and how to interact
with the application. He/she gave instructions during the



45


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



session when explicitly asked by the user, or when he/she
needed help.


In some cases, it was enough to give suggestions by voice.
In other cases, the caregiver had to interact physically with
the user, in two ways: i) The caregiver manipulated the user’s
head to help him/her focus the gaze on the cursor, to move
the cursor toward the hologram, and to drag the hologram to
the proper position; ii) The caregiver moved the user’s
fingers to explain how to perform air-tap.


The caregivers and the users answered a set of questions at
the end of each session. Caregivers filled in a questionnaire
based on research questions Q1-Q8 on a 3-value response
scale: _1 = yes, with no or only initial support; 2 = with_
_evident difficulty and frequent support; 3 = not at all._


Users provided voice answers to two questions - based on
research questions Q9 and Q10 (about fun and satisfaction
respectively) which were asked by the caregiver.


**RESULTS AND DISCUSSION**
We initially planned to perform one session per user in both
groups. Six users in Group 1 (S6, S7, S8 S9, S10, and S11)
who have the strongest disability were also involved in a
second session (after one week) since they had enormous
difficulties in the first session and we wanted to find out if,
after some familiarization, they could achieve some
improvement.


In the rest of this section, we report the main numerical
results for each group, and then also discuss the findings in
light of the notes taken by the observers.


**Main Results - Group 1 (severity level = severe)**
The first set of the following tables (Table 3, Table 4, and
Table 5) reports the results of the caregivers’ survey about
device acceptability and usability, which was filled-out for
the entire Group 1 (n=11) after the _first_ session of use of
HoloLearn.


Table 6A and Table 6B presents the results of the caregivers’
questions on usability for the 6 participants in Group 1 who
attended two sessions with HoloLearn and allow us to
compare the results for these subjects in the first and second
session.

|Col1|1|2|3|
|---|---|---|---|
|~~**Q1**~~<br>**Q2**<br>**Q3**<br>**Q4**|~~90.9%~~<br>18.2%<br>27.2%<br>18.2%|~~9.1%~~<br>27.3%<br>36.4%<br>45.5%|~~0.0%~~<br>54.5%<br>36.4%<br>33.3%|



**Table 3: Caregivers’ survey: device acceptability (Q1) and**
**usability of the interaction paradigm. Group 1; n=11; first use**



|Col1|1|2|3|
|---|---|---|---|
|~~**Q5**~~<br>**Q6**|~~36.4%~~<br>18.2%|~~45.5%~~<br>63.6%|~~18.1%~~<br>18.2%|


**Table 4: Caregivers’ survey: task complexity. Group 1; n=11;**

**first use**

|Col1|1|2|3|
|---|---|---|---|
|~~**Q7 **~~<br>**Q8 **|~~90.9%~~<br>90.9%|~~9.1%~~<br>9.1%|~~0.0%~~<br>0.0%|



**Table 5: Caregivers’ survey: virtual assistant’s role. Group 1;**

**n=11; first use**

|Col1|1|2|3|
|---|---|---|---|
|~~**Q2**~~<br>**Q3**<br>**Q4**|~~0.0%~~<br>0.0%<br>0.0%|~~0.0%~~<br>33.3%<br>33.3%|~~100%~~<br>66.7%<br>66.7%|



**Table 6A: Caregivers’ survey: usability of the interaction**
**paradigm. Group 1- participants who attended 2 sessions;**

**n=6; FIRST session**

|Col1|1|2|3|
|---|---|---|---|
|~~**Q2**~~<br>**Q3**<br>**Q4**|~~0.0%~~<br>0.0%<br>0.0%|~~16.7%~~<br>66.7 %<br>50%|~~83.3%~~<br>33.3%<br>50%|



**Table 6B: Caregivers’ survey: usability of the interaction**
**paradigm. Group 1- participants who attended 2 sessions;**

**n=6; SECOND session**


**Discussion of Results for Group 1**
The data in Table 3-Q1 show positive results, i.e. the high
level of acceptability of the HoloLens device, despite the
strong disabilities of the people in Group 1. In most cases
however it was difficult to capture their attention and help
them understand what to do and how. According to our
observations, only two people successfully completed the
task while six more managed to move the objects around,
placing only some of them in the proper bin.


The main problem that users encountered was to perform the
interaction, and use gaze, air-tap gestures, and their
combination correctly (Table 3 - Q2, Q3, Q4).


Concerning gaze, we observed that it was very difficult for
the users to find the cursor. Several people also showed some
difficulty in understanding the concept of moving the pointer
over a hologram using sustained air-tap gesture.



46


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



These problems might be ascribed to a design weakness. We
used the default cursor provided by HoloLens, which is
white. On several occasions its visualization was confused
because it resulted mixed up with the reflection of the light
on the floor. For this reason, after the first session with Group
1 we decided to replace the default white arrowed cursor with
a bigger, hand-shaped, purple-colored cursor, in order to
make it more easily recognizable by the participant. We also
generated a visual and sound feedback when the
instantaneous air-tap gesture (“select”) was performed
correctly.


As for the air-tap action in itself, the users found it very
difficult to learn the movement of the fingers. This is not
surprising, considering the NDD is often associated with fine
motor skills impairment. The users tended to open and close
the whole hand, instead of using only thumb and index, or
could not keep the two fingers closed while dragging the
holograms around.


It is likely that these difficulties influenced task completion.
Only one participant completed the task successfully, and six
users managed to move the objects but without placing any
of them in the corresponding bin.


Table 5 shows that the users were attracted by the virtual
assistant: according to our observations, it was the first thing
they noticed, and they easily recognized that it was a _Minion_ .
Still, no user was able to understand the instructions of the
virtual character, and to use the application without the
constant help of their caregivers.


The comparisons of Table 6A and Table 6B for the 6 users
who attended two sessions shows an improvement in terms
of usability in the second session, which means that the
second time, the use of HoloLearn was simpler, even if
observations show that the coordination of gaze and air-tap
gesture remained very difficult to perform. The better
usability might be ascribed to the improvement we
introduced in the HoloLearn version for the second session:
the purple cursor with feedback and its effect was probably
more evident. But the usability result might also mean that in
the first session the people learned something about the
system that they did not forget after one week (when the
second session was performed) and which they could exploit
during the second experience. This would be surprising,
considering the severity of the disability of these people and
their memory impairments which normally affect the
capability of remembering previous experiences and
capitalizing on them.


**Main Results - Group 2 (severity level = moderate)**
Table 7 and Table 8 report the results of the caregivers’
surveys for Group 2, i.e. the people with a moderate severity
level of disability.



|Col1|1|2|3|
|---|---|---|---|
|~~**Q1**~~<br>**Q2**<br>**Q3**<br>**Q4**|~~100%~~<br>55.6%<br>66.7%<br>44.4%|~~0%~~<br>22.2%<br>11.1%<br>22.2%|~~0%~~<br>22.2%<br>22.2%<br>33.3%|


**Table 7: Caregivers’ survey: device acceptability (Q1) and**

**usability of the interaction paradigm. Group 2; n=9**

|Col1|1|2|3|
|---|---|---|---|
|~~**Q5**~~<br>**Q6**|~~44.4%~~<br>22.2%|~~55.6%~~<br>77.8%|~~0.0%~~<br>0.0%|



**Table 8: Caregivers’ survey: task complexity. Group 2; n=9**


**Discussion of Results for Group 2**
The people in this group had less and weaker impairments
than Group 1. In addition, they used the improved versions
of HoloLearn in which we provided the purple cursor with
feedback.


For these reasons, the caregivers were able to explain to them
the interaction method and the actions to be performed to
complete the activity and invite them to use the application
autonomously.


According to our observations, all users in Group 2
understood what holograms meant and the purpose of the
activity (Table 8).


After a few attempts and without too much difficulty, most
of them were able to coordinate gaze with air-tap gesture
(Table 7). Six of them completed the task successfully. The
other three could not reach completion but managed to move
the objects around and place some of them in the proper
position.


Like Group 1, everyone in Group 2 liked the _Minion._ In this
group many people also tried to interact with it, for example
by saying “hello” or talking to it. Compared to Group 1,
Group 2 also made better use of the virtual assistant: all users
were able to understand what the _Minion_ was trying to
communicate, and caregivers were able to provide them with
much less assistance.


**Results and discussion on users’ survey**
Table 9 highlights a good degree of fun and satisfaction.

|Col1|1|2|3|
|---|---|---|---|
|~~**Q9**~~<br>**Q10**|~~82.1%~~<br>85.7%|~~17.9%~~<br>10.7%|~~0%~~<br>3.6%|



**Table 9: Participants’ survey**



47


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



According to the observers’ note, most people enjoyed using
HoloLearn and were satisfied with their experience (only one
person showed disappointment), regardless of their
performance and degree of task completion.


**FINAL DISCUSSION AND LESSONS LEARNED**


The findings of the exploratory study are very tentative
because of the heterogeneity of the participants in terms of
age and impairments and the very limited exposure to
HoloLearn. In addition, our study does not offer any rigorous
evidence of the benefits that performing tasks in Mixed
Reality could bring to people with NDD. Nevertheless, the
specialists had a very positive opinion on the potential of this
technology to improve autonomy and to motivate the
learning of day-by-day routines.


At the end of the exploratory study, we organized a focus
group involving the entire working team, including the
caregivers involved in the empirical study, to discuss the
outcomes of the project. Together we analyzed what worked
well and what did not work, and how it should be improved,
and distilled the main lessons we learned.


**Lesson 1: Target Group**
The results of the exploratory study indicate that the
participants in Group 1 required much more support from the
caregivers during the experience than the people in Group 2.
This suggests that HoloLens applications might be more
appropriate for people with moderate severity level of NDD,
since they can better master the intrinsic complexity of the
interaction mechanisms of this device (see also Lesson 2). In
addition, as suggested by one therapist, these subjects might
be able to perceive a stronger sense of presence in MR
environments. Our findings confirm what we also
experienced in other projects [16, 17, 18, 20, 21, 22], i.e. that
creating innovative technologies for the strongest forms of
disability could be much more challenging than for mild
disabilities.


**Lesson 2: Facilitating HoloLens Interaction**
The built-in, most characterizing interaction paradigm of
HoloLens - coordinating gaze and air-tap - might totally
prevent the autonomous use of this technology for people
with the most severe forms of disability in the NDD spectrum
and seems to be complex - but affordable - for people with
moderate severity level. The air-tap gesture is not a natural
movement; coordinating it with gaze can be very hard, if not
impossible, to learn. To mitigate these difficulties, several
strategies could be adopted. One is to envision a possibly
long period of familiarization and training focused only on
learning the interaction mechanism. Other strategies can be
adopted at technological level. For example, we
implemented a technical improvement, replacing the white
default cursor with a purple, hand-shaped one associated
with feedback. This pointer was more visible and intuitive,
and the participants who used it achieved better results. A
complementary solution to alleviate interaction problems
could be to use the HoloLens “clicker” (a physical button


shaped controller) for selection, in place of air-tap. We
integrated this device in the latest version of HoloLearn and
performed a short laboratory test with 8 people with NDD
and moderate severity level. The use of the clicker facilitated
the interaction: After an initial explanation, all participants
understood how to use this device, and the coordination with
gaze was immediate.


**Lesson 3: Virtual Assistant**
An animated virtual assistant, whose visual characteristics
evoke a familiar character, seems to be effective to attract the
user’s attention and to promote engagement and fun regardless of the disorder and the severity level of the
disability. To increase the engagement potential of this
element, and to reduce the risk of boredom during prolonged
use of the system, the therapists suggested providing a
variety of different characters among which the users could
select their favorite one. In contrast, the role of the virtual
assistant to improve autonomy in task performance seems to
depend on the characteristics of the disorder. When the
disability severity level is high, the virtual assistant might
bring no functional benefits, because of the user’s limited
understanding of character behavior, the weakness of
imitation skills, and the frequent habit of constantly asking
therapists what to do. Caregivers suggested that in all cases,
when the virtual assistant is present, they should refrain from
giving task-related instructions, at least for a while, and
rather try to explain what the virtual assistant is
communicating through visual behavior. They also
suggested extending the communication capability of the
virtual assistant and enabling it to offer aural instructions to
complement visual cues.


**Lesson 4: Customization**
Because each individual with disabilities has unique
characteristics, the educational value of a technology for this
target is strongly related to its ability to be personalized to
each users’ evolving needs. HoloLens experiences should be
conceived from the very start with this requirement in mind,
as occurred in HoloLearn. Tasks and holographic elements
should be designed so that multiple configurations, along
multiple dimensions, are possible, and should be integrated
with a simple tool for therapists that enables them to
personalize the application autonomously.


**Lesson 5: Shared Experience**
The sessions of use of HoloLearn were performed
individually, visualizing on an external display screen what
the user was seeing during the experience. This setting
enabled the caregiver to provide the proper guidance at the
proper time. The therapists suggested that we should
capitalize on the possibility of sharing the experience not
only between the user and the caregiver, but also among the
user’s peers, i.e. other individuals with NDD. These people
could enjoy what happens in the MR environment even if
they do not wear the device; they could feel engaged in a
shared experience, offer instructions, and ultimately learn
from the current user’s interactions. The physical presence
of people other than the caregiver might also bring benefits



48


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



to the HoloLearn user. It could reduce the risk of selfisolation which is a drawback of immersive technologies,
helping the user to better feel the difference between the
“real” environment and the digital one, to maintain the
perception of the surrounding physical space, and to mitigate
the potential stress associated with leaving the MR world and
re-entering “real” reality.


**CONCLUSIONS AND FUTURE WORK**
To the best of our knowledge, HoloLearn is the first
HoloLens application designed for people with NDD and
empirically tested in a real setting. During our work, we
faced several technical and methodological challenges, also
because of the limited number of documented examples of
HoloLens applications and their underlying design solutions,
as well as the absence of publications concerning the use of
HoloLens (and MR in general) among people with NDD and
similar disabilities.


Our research is still in an early stage, and many issues need
to be further explored. Nevertheless, some of our design
solutions, the problems we encountered, and the lessons we
learned, could be inspirational for the designers of wearable
Mixed Reality applications devoted to people with NDD as
well as other target groups with similar needs.


There are many points in our research agenda. From a design
and technological perspective, we will include more options
for the current activities and new types of tasks. We are
currently developing new features for the “Laying the table”
activity, to include new items that depend on food type. With
the therapists in our team we have designed new activities
(e.g. “Tidying up the room”) based on a similar pattern of
tasks (i.e. selecting holographic objects and placing them in
different positions). We are creating new characters for the
virtual assistant, inspired by stories and cartoons used during
regular therapeutic activities. We will also integrate the
clicker-based interaction mode in a more robust way, to
complement, or replace, gaze and air-tap. The
implementation of these extensions does not require an
enormous programming effort due to the modularity of the
system, the online availability of 3D models, and the power
of Unity.


A more challenging and long-term future work is related to
the need of both a stronger assessment of the features already
tested in the exploratory study, and the evaluation of the
benefits of HoloLearn for people with NDD to improve
autonomy. The latter issue will require an articulated
controlled study, for a period of at least six months, in order
to compare the effects of interventions based on HoloLearn
with more traditional forms of treatment. Rigorously
controlled studies in the NDD arena are enormously complex
because of the heterogeneity of the impairments associated
with NDD, the difficulty of recruiting a sufficiently large
sample of “homogeneous” subjects, and the need to control
many confounding variables. We are now working with three
large therapeutic centers in Milan - serving in total
approximately 800 people with NDD. They will enable us to



recruit sufficiently wide control and experimental groups and
will help us to address the challenge of a rigorous empirical
study.


**ACKNOWLEDGEMENTS**
We wish to thank all the people at the “Fraternità e Amicizia”
center who participated in our research, and in particular
their coordinator Dr. Eleonora Beccaluva, for her strong
support during the entire project.


**REFERENCES**
1. Adobe. 2018. Mixamo. Retrieved March 20, 2018

[from: https://www.mixamo.com/](https://www.mixamo.com/)


2. American Psychiatric Association. 2013. _Diagnostic_

_and statistical manual of mental disorders_ _(DSM-5®)._
American Psychiatric Pub. 33-41.


3. Beatrice Aruanno, Franca Garzotto, and Mario

Covarrubias Rodriguez. 2017. HoloLens-based Mixed
Reality Experiences for Subjects with Alzheimer's
Disease. _In Proceedings of the 12th Biannual_
_Conference on Italian SIGCHI Chapter (CHItaly '17)_,
Article 15, 9 pages. DOI:
[https://doi.org/10.1145/3125571.3125589](https://doi.org/10.1145/3125571.3125589)


4. Miguel Bernardes, Fernando Barros, Marco Simoes,

and Miguel Castelo-Branco. 2015. A serious game with
virtual reality for travel training with Autism Spectrum
Disorder. In _2015 International Conference on Virtual_
_Rehabilitation (ICVR),_ 127-128. DOI:
[https://doi.org/10.1109/ICVR.2015.7358609](https://doi.org/10.1109/ICVR.2015.7358609)


5. LouAnne E. Boyd, Alejandro Rangel, Helen

Tomimbang, Andrea Conejo-Toledo, Kanika Patel,
Monica Tentori, and Gillian R. Hayes. 2016. SayWAT:
Augmenting Face-to-Face Conversations for Adults
with Autism. In _Proceedings of the 2016 CHI_
_Conference on Human Factors in Computing Systems_
_(CHI '16)_, 4872-4883. DOI:
[https://doi.org/10.1145/2858036.2858215](https://doi.org/10.1145/2858036.2858215)


6. Evren Bozgeyikli, Andrew Raij, Srinivas Katkoori, and

Rajiv Dubey. 2016. Locomotion in Virtual Reality for
Individuals with Autism Spectrum Disorder. In
_Proceedings of the 2016 Symposium on Spatial User_
_Interaction (SUI '16)_, 33-42. DOI:
[https://doi.org/10.1145/2983310.2985763](https://doi.org/10.1145/2983310.2985763)


7. Lal Bozgeyikli, Evren Bozgeyikli, Andrew Raij,

Redwan Alqasemi, Srinivas Katkoori, and Rajiv
Dubey. 2017. Vocational Rehabilitation of Individuals
with Autism Spectrum Disorder with Virtual Reality.
_ACM Transactions on Accessible Computing_
_(TACCESS)_ . 10, 2 (April 2017), Article 5, 25 pages.
[DOI: https://doi.org/10.1145/3046786](https://doi.org/10.1145/3046786)


8. Lal Bozgeyikli, Andrew Raij, Srinivas Katkoori, and

Redwan Alqasemi. 2017. A Survey on Virtual Reality
for Training Individuals with Autism Spectrum
Disorder: Design Considerations. _IEEE Transactions_
_on Learning Technologies_ . 11, 2 (April-June 2018),



49


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



133-151. DOI:
[https://doi.org/10.1109/TLT.2017.2739747](https://doi.org/10.1109/TLT.2017.2739747)


9. Brain Power. 2018. “Empower Me” by Brain Power,

[Retrieved February 16, 2018 from: http://www.brain-](http://www.brain-power.com/autism/)
[power.com/autism/](http://www.brain-power.com/autism/)


10. Ross Brown, Laurianne Sitbon, Lauren Fell, Stewart

Koplick, Chris Beaumont, and Margot Brereton. 2016.
Design insights into embedding virtual reality content
into life skills training for people with intellectual
disability. In _Proceedings of the 28th Australian_
_Conference on Computer-Human Interaction (OzCHI_
_'16)_ . ACM, New York, NY, USA, 581-585. DOI:
[https://doi.org/10.1145/3010915.3010956](https://doi.org/10.1145/3010915.3010956)


11. Vanessa Camilleri, Matthew Montebello, and Alexiei

Dingli. 2017. Walking in small shoes: Investigating the
power of VR on empathising with children's
difficulties. In _2017 23rd International Conference on_
_Virtual System & Multimedia (VSMM)_, 1-6. DOI:
[https://doi.org/10.1109/VSMM.2017.8346253](https://doi.org/10.1109/VSMM.2017.8346253)


12. Xavier Casas, Gerardo Herrera, Inmaculada Coma,

Marcos Fernández. 2012. A Kinect-based Augmented
Reality System for Individuals with Autism Spectrum
Disorders. In _GRAPP/IVAPP._ 440-446.


13. Adam Dachis. 2017. What's the Difference Between

AR, VR, and MR? (11 September 2017). Retrieved
February 18, 2018 from:
[https://next.reality.news/news/whats-difference-](https://next.reality.news/news/whats-difference-between-ar-vr-and-mr-0171163/)
[between-ar-vr-and-mr-0171163/](https://next.reality.news/news/whats-difference-between-ar-vr-and-mr-0171163/)


14. Dan Ehninger, Weidong Li, Kevin Fox, Michael P.

Stryker, & Alcino J. Silva. 2008. Reversing
neurodevelopmental disorders in adults. _Neuron_, 60, 6
(December 2008), 950-960. DOI:
[https://doi.org/10.1016/j.neuron.2008.12.007](https://doi.org/10.1016/j.neuron.2008.12.007)


15. Mariano Etchart and Alessandro Caprarelli. 2018. A

wearable immersive web-virtual reality approach to
remote neurodevelopmental disorder therapy. In
_Proceedings of the 2018 International Conference on_
_Advanced Visual Interfaces (AVI '18)_, Article 61, 3
[pages. DOI: https://doi.org/10.1145/3206505.3206595](https://doi.org/10.1145/3206505.3206595)


16. Franca Garzotto and Matteo Forfori. 2006. FaTe2:

storytelling edutainment experiences in 2D and 3D
collaborative spaces. In _Proceedings of the 2006_
_conference on Interaction design and children (IDC_
_'06)_, 113-116. DOI:
[https://doi.org/10.1145/1139073.1139102](https://doi.org/10.1145/1139073.1139102)


17. Franca Garzotto, Mirko Gelsomini, Daniele Occhiuto,

Vito Matarazzo, and Nicolò Messina. 2017. Wearable
Immersive Virtual Reality for Children with Disability:
a Case Study. In _Proceedings of the 2017 Conference_
_on Interaction Design and Children (IDC '17)_, 478[483. DOI: https://doi.org/10.1145/3078072.3084312](https://doi.org/10.1145/3078072.3084312)


18. Franca Garzotto, Nicolò Messina, Vito Matarazzo,

Lukasz Moskwa, Gianluigi Oliva, and Riccardo



Facchini. 2018. Empowering Interventions for Persons
with Neurodevelopmental Disorders through Wearable
Virtual Reality and Bio-sensors. In _Extended Abstracts_
_of the 2018 CHI Conference on Human Factors in_
_Computing Systems (CHI EA '18)_, Paper LBW618, 6
[pages. DOI: https://doi.org/10.1145/3170427.3188636](https://doi.org/10.1145/3170427.3188636)


19. Franca Garzotto, Matteo Valoriani, and Laura Bartoli.

(2014). Touchless motion-based interaction for therapy
of autistic children. In _Virtual, Augmented Reality and_
_Serious Games for Healthcare 1_ . Intelligent Systems
Reference Library, Vol 68. Springer, Berlin,
Heidelberg. 471-494. DOI:
[https://doi.org/10.1007/978-3-642-54816-1_23](https://doi.org/10.1007/978-3-642-54816-1_23)


20. Franca Garzotto, Mirko Gelsomini, Francesco

Clasadonte, Daniele Montesano, and Daniele Occhiuto.
2016. Wearable Immersive Storytelling for Disabled
Children. In _Proceedings of the International Working_
_Conference on Advanced Visual Interfaces (AVI '16)_,
196-203. DOI:
[https://doi.org/10.1145/2909132.2909256](https://doi.org/10.1145/2909132.2909256)


21. Mirko Gelsomini, Franca Garzotto, Daniele

Montesano, Daniele Occhiuto. 2016. Wildcard: A
wearable virtual reality storytelling tool for children
with intellectual developmental disability. In _2016 38th_
_Annual International Conference of the IEEE_
_Engineering in Medicine and Biology Society (EMBC)_,
5188-5191. DOI:
[https://doi.org/10.1109/EMBC.2016.7591896](https://doi.org/10.1109/EMBC.2016.7591896)


22. Mirko Gelsomini, Franca Garzotto, Vito Matarazzo,

Nicolò Messina, and Daniele Occhiuto. 2017. Creating
Social Stories as Wearable Hyper-Immersive Virtual
Reality Experiences for Children with
Neurodevelopmental Disorders. In _Proceedings of the_
_2017 Conference on Interaction Design and Children_
_(IDC '17)_, 431-437. DOI:
[https://doi.org/10.1145/3078072.3084305](https://doi.org/10.1145/3078072.3084305)


23. Gerardo Herrera, Rita Jordan, and Lucia Vera. 2006.

Abstract concept and imagination teaching through
virtual reality in people with autism spectrum
disorders. _Technology and Disability_, 18, 4 (December
2006), 173-180.


24. Gerardo Herrera, Francisco Alcantud, Rita Jordan,

Amparo Blanquer, Gabriel Labajo, Cristina De Pablo.
2008. Development of symbolic play through the use
of virtual reality tools in children with autistic spectrum
disorders: Two case studies. _Autism_, 12, 2 (March
2008), 143-157. DOI:
[https://doi.org/10.1177/1362361307086657](https://doi.org/10.1177/1362361307086657)


25. Naomi Josman, Hadass Milika Ben-Chaim, Shula

Friedrich, and Patrice L. Weiss. (2008). Effectiveness
of virtual reality for teaching street-crossing skills to
children and adolescents with autism. _International_
_Journal on Disability and Human Development_, 7, 1



50


Session 1: Interacting with the Real World ASSETS’18, October 22–24, 2018, Galway, Ireland



(May 2011), 49-56. DOI:
[https://doi.org/10.1515/IJDHD.2008.7.1.49](https://doi.org/10.1515/IJDHD.2008.7.1.49)


26. Runpeng Liu, Joseph P. Salisbury, Arysha

Vahabzadeh, & Ned T. Sahin. 2017. Feasibility of an
autism-focused augmented reality smartglasses system
for social communication and behavioral coaching.
_Frontiers in pediatrics_, 5, (June 2017). DOI:
[https://doi.org/10.3389/fped.2017.00145](https://doi.org/10.3389/fped.2017.00145)


27. Microsoft. 2017. Microsoft HoloLens. Retrieved March

[20, 2018 from: https://www.microsoft.com/en-](https://www.microsoft.com/en-us/hololens/)
[us/hololens/](https://www.microsoft.com/en-us/hololens/)


28. Microsoft. 2018. Microsoft Holographic Gaze.

Retrieved April 11, 2018 from:
[https://docs.microsoft.com/en-us/windows/mixed-](https://docs.microsoft.com/en-us/windows/mixed-reality/gaze)
[reality/gaze](https://docs.microsoft.com/en-us/windows/mixed-reality/gaze)


29. Microsoft. 2018. Microsoft Holographic Gestures.

Retrieved April 11, 2018 from:
[https://docs.microsoft.com/en-us/windows/mixed-](https://docs.microsoft.com/en-us/windows/mixed-reality/gestures)
[reality/gestures](https://docs.microsoft.com/en-us/windows/mixed-reality/gestures)


30. Microsoft. 2018. Microsoft Holographic Voice Input.

Retrieved April 11, 2018 from:
[https://docs.microsoft.com/en-us/windows/mixed-](https://docs.microsoft.com/en-us/windows/mixed-reality/voice_input)
[reality/voice_input](https://docs.microsoft.com/en-us/windows/mixed-reality/voice_input)


31. Microsoft. 2018. Microsoft Holographic Spatial

Mapping. Retrieved April 11, 2018 from:
[https://docs.microsoft.com/en-us/windows/mixed-](https://docs.microsoft.com/en-us/windows/mixed-reality/spatial-mapping)
[reality/spatial-mapping](https://docs.microsoft.com/en-us/windows/mixed-reality/spatial-mapping)


32. Microsoft. 2018. Microsoft Holographic Spatial Sound.

Retrieved April 11, 2018 from:
[https://docs.microsoft.com/en-us/windows/mixed-](https://docs.microsoft.com/en-us/windows/mixed-reality/holograms-220)
[reality/holograms-220](https://docs.microsoft.com/en-us/windows/mixed-reality/holograms-220)


33. Microsoft. 2017. MixedRealityToolkit-Unity.

Retrieved April 7, 2018 from:
[https://github.com/Microsoft/MixedRealityToolkit-](https://github.com/Microsoft/MixedRealityToolkit-Unity)
[Unity](https://github.com/Microsoft/MixedRealityToolkit-Unity)


34. Microsoft. 2017. Use the HoloLens clicker. Retrieved

[April 12, 2018 from: https://support.microsoft.com/it-](https://support.microsoft.com/it-it/help/12646/hololens-use-the-hololens-clicker)
[it/help/12646/hololens-use-the-hololens-clicker](https://support.microsoft.com/it-it/help/12646/hololens-use-the-hololens-clicker)



35. Microsoft. 2018. Visual Studio. Retrieved April 2,

[2018 from: https://www.visualstudio.com/](https://www.visualstudio.com/)


36. Nigel Newbutt, Connie Sung, Hung Jen Kuo, Michael

J. Leahy and Boyang Tong. 2016. Brief Report: A Pilot
Study of the Use of a Virtual Reality Headset in
Autism Populations. _Journal of Autism and_
_Developmental Disorders_, 46, 6 (September 2016),
[3166–3176. DOI: https://doi.org/10.1007/s10803-016-](https://doi.org/10.1007/s10803-016-2830-5)
[2830-5](https://doi.org/10.1007/s10803-016-2830-5)


37. Sarah Parsons & Peter Mitchell. 2002. The potential of

virtual reality in social skills training for people with
autistic spectrum disorders. _Journal of Intellectual_
_Disability Research_, 46, 5 (April 2014), 430-443. DOI:
[https://doi.org/10.1046/j.1365-2788.2002.00425.x](https://doi.org/10.1046/j.1365-2788.2002.00425.x)


38. Dorothy Strickland. 1997. Virtual reality for the

treatment of autism. _Studies in health technology and_
_informatics_ . 81-86.


39. Andrea Tartaro. 2006. Storytelling with a virtual peer

as an intervention for children with autism.
SIGACCESS Access. Comput. 84 (January 2006), 42[44. DOI: http://dx.doi.org/10.1145/1127564.1127573](http://dx.doi.org/10.1145/1127564.1127573)


40. Unity. 2018. Retrieved April 3, 2018 from:

[https://unity3d.com/](https://unity3d.com/)


41. Unity. 2018. Unity User Manual. Retrieved April 3,

2018 from:
https://docs.unity3d.com/Manual/index.html
42. U.S. Environmental Protection Agency. 2013.

America's Children and the Environment, Third
Edition. (January 2013). 233-253. Retrieved February
25, 2018 from:
https://www.epa.gov/sites/production/files/201506/documents/ace3_2013.pdf
43. Simon Wallace, Sarah Parsons, Alice Westbury, Katie

White, Kathy White, and Anthony Bailey. 2010. Sense
of presence and atypical social judgments in immersive
virtual environments Responses of adolescents with
Autism Spectrum Disorders. Autism, 14, 3 (May
2010), 199-213. DOI:
https://doi.org/10.1177/1362361310363283



51


