# **Designing a Customizable Picture-Based Augmented Reality** **Application For Therapists and Educational Professionals** **Working in Autistic Contexts**

Tooba Ahsen [Christina](https://orcid.org/0000-0003-2866-4637) Yu [Amanda](https://orcid.org/0000-0001-5350-5457 ) O’Brien

tooba.ahsen@tufts.edu christina.yu@childrens.harvard.edu amanda_obrien@g.harvard.edu
Computer Science Autism Language Program & Speech and Hearing Biosciences and
Tufts University Augmentative Communication Technology
Medford, MA, USA Program Harvard University
Boston Children’s Hospital Cambridge, Massachusetts, USA
Boston, Massachusetts, USA


Ralf W [Schlosser](https://orcid.org/0000-0002-2069-3911) Howard C Shane Dylan Oesch-Emmel
Ralf.Schlosser@Northeastern.edu howard.shane@childrens.harvard.edu dylan.oesch_emmel@tufts.edu
Communication Sciences and Boston Children’s Hospital Computer Science
Disorders Boston, Massachusetts, USA Tufts University
Northeastern University Harvard Medical School Medford, Massachusetts, USA
Boston, Massachusetts, USA Boston, Massachusetts, USA


Eileen [T.](https://orcid.org/0000-0002-1744-7621) Crehan Fahad Dogar
[eileen.crehan@tufts.edu](mailto:eileen.crehan@tufts.edu) [fahad@cs.tufts.edu](mailto:fahad@cs.tufts.edu)
Eliot-Pearson Department of Child Computer Science
Study & Human Development Tufts University
Tufts University Medford, Massachusetts, USA
Medford, Massachusetts, USA
Department of Psychiatry
Rush University Medical Center
Chicago, Illinois, USA



**ABSTRACT**


This paper presents the design and evaluation of CustomAR – a
customizable Augmented Reality (AR) application, designed in col­
laboration with therapists, that allows them to create and customize
picture-based AR experiences for use in an autistic context. Using a
2-week diary study, we gauge whether the application’s customiza­
tion options and features are sufcient to allow therapists and
educational professionals to create AR experiences for the various
learning activities they conduct with autistic children, and what
challenges they face in this regard. We fnd that participants think
the application would be suitable for creating AR experiences for a
wide range of learning activities, such as choice-making and teach­
ing daily living skills, and think that the application’s freeze feature
can be helpful when working with children with limited attention.
Towards the end of the paper we discuss the challenges users face


This work is licensed under a Creative Commons [Attribution](https://creativecommons.org/licenses/by/4.0/) International

4.0 [License.](https://creativecommons.org/licenses/by/4.0/)


_ASSETS_ _’22,_ _October_ _23–26,_ _2022,_ _Athens,_ _Greece_
© 2022 Copyright held by the owner/author(s).
ACM ISBN 978-1-4503-9258-7/22/10.
[https://doi.org/10.1145/3517428.3544884](https://doi.org/10.1145/3517428.3544884)



when trying to incorporate picture-based AR in practical therapy
exercises, and how they can be addressed.


**CCS** **CONCEPTS**


- **Human-centered** **computing** → **Mixed** **/** **augmented** **reality** ;
**User** **studies** ; - **Social** **and** **professional** **topics** → **People** **with**
**disabilities** .


**KEYWORDS**


Augmented Reality; Picture-Based; Marker-Based; Autism Spec­
trum Condition; Education; Therapy; Customization;


**ACM** **Reference** **Format:**

Tooba Ahsen, Christina Yu, Amanda O’Brien, Ralf W Schlosser, Howard
C Shane, Dylan Oesch-Emmel, Eileen T. Crehan, and Fahad Dogar. 2022.
Designing a Customizable Picture-Based Augmented Reality Application
For Therapists and Educational Professionals Working in Autistic Contexts.
In _The_ _24th_ _International_ _ACM_ _SIGACCESS_ _Conference_ _on_ _Computers_ _and_
_Accessibility_ _(ASSETS_ _’22),_ _October_ _23–26,_ _2022,_ _Athens,_ _Greece._ ACM, New
York, NY, USA, 16 pages. [https://doi.org/10.1145/3517428.3544884](https://doi.org/10.1145/3517428.3544884)


**1** **INTRODUCTION**


Autism Spectrum Condition (ASC) is a neurodevelopmental con­
dition that is often characterized by difculty in communication,


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.


in particular, has helped autistic individuals complete daily living
tasks more independently [ 22 ] and has helped them improve their
communication [40] and emotion recognition skills [19].



**(a)** **The** **CustomAR** **Application.** **The** **fgure** **shows** **the**
**creation** **window.** **Users** **can** **associate** **audio,** **videos,** **or**
**3D** **models** **with** **a** **target** **image** **to** **create** **an** **AR** **experi-**
**ence.** **The** **white** **plane** **to** **the** **center-left** **of** **the** **screen**
**shows** **the** **image** **the** **user** **has** **uploaded.** **The** **user** **has**
**added** **a** **Lego** **block** **3D** **model** **to** **this** **AR** **experience** **and**
**is** **customizing** **its** **position.**


**(b)** **The** **AR-View** **window.** **Users** **can** **view** **their** **AR** **ex-**
**perience** **by** **going** **to** **the** **AR-View** **window.** **The** **user**
**has** **printed** **the** **target** **image** **onto** **a** **piece** **of** **paper,** **and**
**is** **holding** **up** **their** **device** **camera** **to** **the** **target** **image** **to**
**elicit** **the** **associated** **AR** **experience.** **The** **3D** **Lego** **block**
**has** **appeared** **on** **their** **screen.**


**Figure** **1**


social-emotional reciprocity, and repetitive behavior [ 34 ]. Autis­
tic children [1] often have varied learning and behavioral profles –
some may have more difculty with expressive and/or receptive
language, others may have difculty understanding and regulat­
ing emotions and behaviors, and many demonstrate very specifc
interests [34, 52].

While there is no one-size fts all approach to teaching, therapists
and teachers on an autistic child’s support team often adopt learning
strategies that utilize _visual_ _supports_ (pictures, icons, photographs
etc.), as they have been shown to be efective in autistic contexts

[ 50, 56 ]. Picture-based Augmented Reality (AR) is a logical extension
to learning activities that rely on visual supports as it allows pictures
to be superimposed with additional information or virtual content
(audio, videos, 3D models etc.) - the virtual content appears on
the screen when the picture comes into view of the user’s device
camera. Augmented Reality, in general, has shown to increase focus
and engagement in children with autism [ 30 ] and Picture-based AR,


1 A note on language: Adolescent and adult self-advocates in our studies and our
advisory board have shared that they strongly prefer identity-frst language (e.g.,
autistic person) [15, 46]



However, practical use of these previously designed AR appli­
cations may be limited in therapeutic or learning environments
because they lack support for _customization_ . Therapists and edu­
cational professionals often need to customize learning exercises
and content according to an autistic child’s interests [ 37, 41 ], to
keep them engaged and encourage positive behaviors [ 16, 57 ]. Cus­
tomization is key, and the lack of support for customization could
make it difcult for therapists and educational professionals to inte­
grate picture-based AR into the day-to-day learning activities they
conduct. Therefore, there is a gap between _research_ _into_ AR appli­
cations and the _practical_ _use_ _of_ those applications, and a scarcity
of work that bridges this gap.

Therapists and educational professionals are also key players
in the adoption of assistive or learning technology. Prior to intro­
ducing new technology into an autistic child’s educational plan,
they must use their clinical and educational experience to evaluate
the technology and determine how to efectively utilize it in an
intervention [ 27 ]. Therefore, to design AR applications that are
useful in practical autistic contexts, it is important for the research
community to understand the customization needs of therapists
and educational professionals, how they envision using AR in the
learning activities they conduct with autistic children, and what
features will be most useful in this regard.

Our contribution is as follows; We frst highlight the design and
implementation of CustomAR; a mobile AR application, created
in collaboration with therapists, that allows them to create and
customize picture-based AR experiences from scratch (refer to fg­
ure 1). We highlight key lessons from each of the two phases of
the design process - from engaging in _participatory_ _design_ with
therapists to create the frst version of the application for a specifc
symbolic development use-case, to modifying the application into
a customizable authoring tool. The latter could potentially allow
therapists and educational professionals to create AR experiences
for a variety of learning contexts, and for a diverse population of
autistic children.


Secondly, we conduct a 2-week diary study and follow-up semi­
structured interviews with special education teachers, occupational
therapists, and speech language pathologists, to gauge whether they
think the application’s customization options and other features are
suitable for use in autism-related learning contexts. Moreover, we
shed light on the challenges that could hamper the use of picturebased AR in practical therapeutic or educational settings. Our study
reveals the following:


  - Therapists/teachers fnd the application’s customization op­

tions sufcient to create AR experiences for a myriad of
learning activities, ranging from choice-making and teach­
ing daily living skills, to teaching lessons on emotion recog­
nition and for collaboration and group-work. Details of these
learning activities and the customization options that sup­
ported their development are provided in section 6.2 and

6.3.

  - Therapists/teachers appreciate the ability to ‘freeze’ AR expe­

riences on the screen and think that it would be useful when


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



working with children with limited focus, or when show­
ing AR experiences to children in groups. This is discussed
further in section 6.4.

  - Therapists/teachers are concerned about generalizing AR
experiences or creating them ‘just-in-time’ during therapy
sessions (section 6.5). Allowing users to share AR experiences
with others, and recommending AR content to users may
alleviate these concerns. This is discussed further in sections

7 and 9.1 respectively.

Our work provides valuable insight into the features and cus­
tomization options that will help therapists and educational pro­
fessionals introduce AR into the learning activities they conduct.
Although autistic individuals did not take part in this study, our
fndings may be useful for future studies that position autistic
children as content creators and investigate which features/UI are
suitable to allow them to independently create AR experiences. In
the subsequent sections of this paper, we summarize related work,
provide details about the two-phased design process and the user
study, present and discuss our qualitative fndings, and highlight
limitations and future directions for this research.


**2** **RELATED** **WORK**


This section leverages prior work to highlight how therapists and
educational professionals use visual supports in learning exercises,
how picture-based AR can extend them, and the signifcance of
customization and interest-based learning in autistic contexts.


**2.1** **Using** **Visual** **Supports** **in** **Learning**
**Exercises** **&** **How** **Picture-Based** **AR** **Can**

**Extend** **Them**


Therapists and teachers frequently use visual supports, such as
pictures, symbols or photographs in learning activities involving
autistic children as they often exhibit strong visual processing abil­
ities [ 50 ]. For example, teachers or therapists may tape pictures
that represent the day’s activities (visual schedules) to the walls
of a classroom to make it easier for autistic children to transition

from one activity to another [ 5, 25 ]. Similarly, they may print pic­
tures depicting the steps involved in a daily living task, and tape
them somewhere in the environment as reminders [ 1, 50 ]. Visual
supports are also used during choice-making activities, reinforcer
assessment activities, or activities involving speech and language

[3]

Picture-based AR is a logical extension to some of these learn­
ing activities that rely on pictures/symbols, and can add layers of
information and helpful hints on top of them. When users hold
their devices over a picture to elicit the associated AR content, the
_context_ _of_ _the_ _activity_ (the picture/photograph, the tabletop etc.)
is preserved, and users can view _additional_ _information_ without
shifting their focus away from the task at hand. For example, Cihak
et al. took a traditional tooth-brushing exercise in which a picture
of the steps in the task was taped to the bathroom mirror, and
superimposed the picture with a video clip depicting how each step
was performed. Autistic children accessed this additional informa­
tion by holding their device cameras up to the picture and could
replicate the steps using the toothbrush, toothpaste, and paper cups
in front of them. The study found that autistic children performed



the tooth-brushing task more independently when AR was used

[ 22 ]. Prior studies have also used picture-based AR to enhance the
learning efects of social stories, [ 20 ], to teach emotion recogni­
tion [ 17, 19 ], and to improve children’s communication abilities by
reinforcing the meaning of pictures/symbols found in the Picture
Exchange Communication System (PECS) [ 40, 47 ]. Picture-based
AR, therefore, can be an efective teaching tool in an autistic context
and as such it is important to understand what tools and features
could facilitate therapists and teachers in using picture-based AR
during the learning exercises they conduct.


**2.2** **Autism,** **Interest-Based** **Learning** **&**
**Customizable** **AR**


Studies have shown that customizing learning exercises accord­
ing to the unique learning needs and interests of autistic children

[ 33, 35 ] leads to positive behaviors [ 16, 28, 57 ]. The ability to cus­
tomize, therefore, may be invaluable to therapists and educational
professionals working with autistic individuals. However, a recent
survey study revealed that current computer-based technologies de­
signed for autistic individuals lack robust support for customization

[ 44 ]. This includes studies under the umbrella of ‘augmented and
virtual reality’ - although AR interventions have shown to support
autistic individuals in various domains [ 38, 39, 45 ] including com­
munication [ 40, 58, 59 ], daily-living [ 22 ], pretend play [ 12, 13, 26 ],
and social and emotional learning [ 29, 43, 54 ], research into _cus­_
_tomizable_ _AR_ is lacking [44].

Very few studies have provided users with the ability to cus­
tomize picture-based AR experiences [ 24, 47 ], and even then users
can only customize within the confnes of an activity, e.g., being
able to change the virtual content associated with predefned PECS
symbols, but being unable to create an experience around new sym­
bols [ 47 ]. Moreover, there is only one AR application on the Google
play store (for android devices) that allows users to create their own
picture-based AR experiences [ 2 ], and this application has not been
created with the needs of therapists/teachers and autistic children
in mind.


In contrast, we involved therapists in the design process and
drew on their clinical experience in working with autistic children.
Subsequently, we created an application that not only gives them
the agency to create and customize picture-based AR experiences
from scratch using their own images and virtual content, for learn­
ing activities that they themselves have conceptualized, but that
also contains features that could potentially facilitate the use of
AR in autistic contexts. Moreover, we investigate the practical chal­
lenges they could encounter when trying to inculcate picture-based
AR in autism-related learning activities - something that no prior
work has looked into thus far.


**3** **RESEARCH** **GOALS** **&** **HIGHER** **LEVEL**

**RESEARCH** **QUESTIONS**


Our frst goal is to provide therapists and educational profession­
als with an application that allows them to create and customize
picture-based AR experiences from scratch. Section 4 describes
the two design phases that culminated in the development of our
customizable AR application.


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.



Our second goal is to evaluate this application by conducting user
studies with therapists and educational professionals. We aim to
understand; (1) whether therapists can sufciently use the applica­
tion’s creation and customization features to create AR experiences
for their autistic students; (2) whether the freeze feature – a feature
that was developed based on feedback from therapists during the
design phase (section 4.2.3), and which allows them to freeze AR
experiences on the screen while keeping the experiences interactive
– is useful in the context of autism; (3) what challenges therapists
face when trying to integrate picture-based AR in the learning
activities they conduct.

The specifc research questions (RQ) are listed below:


  - **RQ** **1:** **Are** **the** **application’s** **customization** **options** **suf-**
**fcient** **to** **allow** **therapists/educational** **professionals** **to**
**create** **AR** **experiences** **to** **meet** **the** **varied** **interests** **and**
**learning** **needs** **of** **the** **autistic** **population** **they** **work**
**with?**

  - **RQ** **2:** **How** **does** **the** **application’s** **freeze** **feature** **facili-**
**tate** **the** **use** **of** **AR** **in** **the** **context** **of** **autism?**

  - **RQ** **3:** **What** **are** **the** **challenges** **in** **using** **picture-based**
**AR** **in** **practical** **therapy/learning** **settings?**

Section 5 highlights the results of the user study we conducted
to answer these research questions.


**4** **APPLICATION** **DESIGN**


We designed and developed our application in two phases. In phase
I (section 4.2), we designed the application in collaboration with 4
researchers/Speech Language Pathologists (SLPs) from the Boston
Children’s Hospital’s outpatient clinic in Waltham, Massachusetts.
The goal was to use AR to enhance the symbolic knowledge for the
moderate to severely autistic children that visited the clinic. Our
collaborating SLPs informally tested the application and realized
that the lack of customization options was hindering its use. We
then re-designed the application in phase II (section 4.3), to allow
users to create/customize picture-based AR experiences for a variety
of learning contexts and autistic individuals, not just those specifc
to the clinic. In this section, we highlight our design journey; We
describe our initial symbolic development use-case, features of the
frst prototype, and the lessons we learnt that spurred the redesign
of the application into a more customizable tool. We then describe
the features of the latest version of the application.


**4.1** **The** **Design** **Team** **&** **Participatory** **Design**
**Process**


Our multi-disciplinary design team comprised of computer scien­
tists and 4 researchers/SLPs from the Boston Children’s Hospi­
tal’s outpatient clinic in Waltham, Massachusetts. These clinicians
primarily work with minimally verbal children with moderate to
severe autism and provide diagnostic, and speech and language
evaluations and treatments. At the time of introduction the SLPs

were exploring AR in play contexts, but had no prior experience
with picture-based AR.

The design process was as follows; the frst author visited the
clinic weekly for a month, and then bi-weekly over the next 3
months for design meetings. The frst month was dedicated to
outlining the features of the application, and the content of the AR



experiences (e.g., the target images and 3D models used, the audio
and animations to create for each model etc.). Over the remaining
months, the frst author coded the application’s features and UI.
When a feature was coded, the frst author would demonstrate
the feature during the bi-weekly in-person meetings. The SLPs
would provide feedback and suggestions for improvement or re­
design, and modifcations would be made accordingly. The SLPs
also informally tested the application amongst themselves (at the
end of Phase I) and provided feedback that spurred the redesign of
the application into a more cutomizable tool (Phase II).


**4.2** **Phase** **I** **- Designing** **an** **AR** **Application** **for** **a**
**Specifc** **Clinical** **Context**


_4.2.1_ **Symbolic** **Development** **Use-case:** In phase I, the goal
was to design an application that could enhance symbolic knowledge for the minimally verbal children with moderate to severe
autism, that visited the clinic. The SLPs often centered therapy
around play, and these children were familiar with numerous toys
present at the clinic.
Let’s consider a common scenario at the clinic; Sam is a 7 year
old male who regularly visits the clinic. He has moderate-severe
autism and very little functional speech (a few intelligible spoken
words). Therapists at the clinic want to teach Sam how to requests
for objects (toys, food etc) by pointing towards pictures of those
objects, instead of trying to grab the objects themselves, physically
dragging an adult towards where the objects are being kept, or
showing disruptive behavior. When the therapist presents Sam
with two objects that he likes, a toy (a Lego block) and a snack
(goldfsh crackers), he consciously points towards the object he
wants. The therapist then puts the objects out of sight, and presents
Sam with a _picture_ of the Lego block and goldfsh crackers instead.
Sam is unable to point towards the picture of the object he wants. He
does not understand that the 2D pictures are _symbols_ that represent
the 3D objects.
Since pictures and symbols are key to numerous alternate communication strategies [ 14, 31, 32, 49 ], it is important for these children to understand the symbolic relationship between 2D pictures
and their 3D referents. In our example, Sam does not have a clear
understanding of this relationship. We hypothesized that if we
could momentarily convert the 2D into 3D, that is, superimpose
the 2D pictures of the objects with highly similar 3D models of the
objects, Sam may understand the 2D-3D symbolic relationship and
be able to make a conscious choice between the available options.


_4.2.2_ **Content** **&** **Features** **of** **the** **Application:**


_**Basic**_ _**AR**_ _**Experiences:**_ _The_ _fst_ _version_ _of_ _the_ _application_ _was_
_very_ _simple._ _We_ _pre-programmed_ _a_ _few_ _images_ _and_ _corresponding_ _3D_
_models_ _into_ _the_ _application_ _(details_ _present_ _in_ _the_ _next_ _bullet_ _point)._
_Therapists_ _would_ _open_ _the_ _application_ _on_ _an_ _iPad_ _and_ _hold_ _the_ _device_
_camera_ _over_ _a_ _print-out_ _of_ _one_ _of_ _the_ _pre-programmed_ _images._ _The_
_associated_ _3D_ _models_ _would_ _then_ _appear_ _on_ _the_ _screen._ _Figure_ _2_ _shows_
_a_ _picture_ _of_ _Lego_ _blocks_ _and_ _goldfsh_ _crackers_ _superimposed_ _with_
_3D_ _models_ _of_ _the_ _same_ _objects._ _Names_ _of_ _the_ _objects_ _would_ _appear_
_on_ _small_ _banners_ _beside_ _the_ _3D_ _models._ _When_ _the_ _3D_ _models_ _were_

_tapped,_ _an_ _audio_ _recording_ _of_ _the_ _object’s_ _name_ _would_ _play_ _out._ _It_
_is_ _important_ _to_ _note_ _that_ _these_ _AR_ _experiences_ _were_ _built_ _into_ _the_


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



**(a)** **Target** **image** **of** **Lego** **block** **and**
**Goldfsh** **crackers**


**(b)** **3D** **models** **of** **the** **Lego** **block** **and**
**goldfsh** **crackers** **appearing** **over** **the**
**target** **image**


**Figure** **2:** **Basic** **AR** **Experience**


_application._ _The_ _therapists_ _could_ _not_ _alter_ _the_ _target_ _images_ _or_ _the_ _3D_
_models_ _associated_ _with_ _them._


_**3D**_ _**Objects**_ _**and**_ _**Target**_ _**Images:**_ _The_ _initial_ _application_ _was_
_designed_ _while_ _keeping_ _in_ _mind_ _the_ _objects_ _(e.g.,_ _toys)_ _that_ _the_ _children_
_at_ _the_ _clinic_ _interacted_ _with_ _the_ _most._ _The_ _design_ _team_ _picked_ _6_ _objects_

_- a_ _bubble_ _wand,_ _a_ _‘Thomas_ _the_ _train’_ _toy,_ _a_ _large_ _Lego_ _block,_ _a_ _packet_
_of_ _goldfsh_ _crackers,_ _a_ _soccer_ _ball_ _and_ _a_ _pair_ _of_ _socks._ _Since_ _the_ _children_
_were_ _prompted_ _to_ _make_ _a_ _choice_ _between_ _2_ _objects_ _at_ _a_ _time,_ _we_ _took_
_images_ _of_ _pairs_ _of_ _objects._ _These_ _served_ _as_ _the_ _2D_ _images_ _the_ _children_
_would_ _be_ _presented_ _with_ _and_ _the_ _target_ _images_ _that_ _the_ _application_
_would_ _recognize._ _Examples_ _of_ _diferent_ _pairs_ _are_ _shown_ _in_ _Figure_ _3._


_**Animations:**_ _Based_ _on_ _discussions_ _with_ _the_ _therapists,_ _we_ _cre­_
_ated_ _an_ _animation_ _for_ _each_ _3D_ _model_ _to_ _promote_ _engagement._ _For_
_example,_ _bubbles_ _would_ _appear_ _in_ _front_ _of_ _the_ _bubble_ _wand,_ _the_ _Lego_
_blocks_ _would_ _start_ _stacking_ _on_ _top_ _of_ _each_ _other,_ _and_ _a_ _few_ _pieces_ _of_
_goldfsh_ _crackers_ _would_ _appear_ _outside_ _their_ _packet._ _(Figure_ _4a)._ _Each_
_animation_ _was_ _paired_ _with_ _relevant_ _audio,_ _such_ _as_ _a_ _popping_ _sound_
_for_ _the_ _bubble_ _wand,_ _a_ _stacking_ _sound_ _for_ _the_ _Lego_ _blocks_ _and_ _the_
_sound_ _of_ _a_ _packet_ _opening_ _for_ _the_ _goldfsh_ _crackers._



**(a)** **Bubble** **wand** **and** **‘Thomas’**


**(b)** **Socks** **and** **soccer** **ball**


**Figure** **3:** **Target** **Images**


_**Hiding**_ _**Target**_ _**Images:**_ _Sometimes_ _when_ _3D_ _models_ _were_ _super­_
_imposed_ _over_ _target_ _images,_ _there_ _would_ _be_ _too_ _many_ _elements_ _on_ _the_
_screen._ _Some_ _individuals_ _on_ _the_ _spectrum_ _could_ _perceive_ _this_ _as_ _visual_
_clutter_ _or_ _sensory_ _overload_ _[_ _21_ _]._ _To_ _minimize_ _this,_ _we_ _added_ _a_ _‘hide’_
_feature_ _to_ _the_ _application._ _A_ _white_ _plane_ _would_ _appear_ _over_ _the_ _target_
_image_ _(Figure_ _4b),_ _temporarily_ _hiding_ _the_ _target_ _image_ _and_ _drawing_
_focus_ _to_ _the_ _3D_ _models_ _on_ _top._


_4.2.3_ **Informal** **Testing** **&** **Design** **Considerations** **Moving** **For­**
**ward:** Our collaborating SLPs informally tested the application
amongst themselves and provided feedback. They were given a
hi-fdelity prototype of the application and instructed to trigger the
various in-built AR experiences, try out the animations for each 3D
model, and comment on the strengths and weaknesses of the appli­
cation. After using the application for several months, and due to
the overnight shift to remote learning practices due to the Covid-19
pandemic [ 53 ], the SLPs faced various challenges. These challenges,
and their implications on application design, are outlined below.


_**Predefned**_ _**Content**_ _**and**_ _**Varied**_ _**Interests**_ _**- The**_ _**Need**_ _**for**_
_**Customization**_ _**Options:**_ _We_ _tried_ _to_ _ensure_ _that_ _the_ _target_ _im­_
_ages_ _and_ _3D_ _models_ _found_ _within_ _the_ _application_ _were_ _representative_
_of_ _(and_ _highly_ _similar_ _to)_ _the_ _objects_ _found_ _at_ _the_ _clinic_ _that_ _were_
_interesting_ _to_ _the_ _clinic’s_ _autistic_ _population._ _However,_ _the_ _move_ _to_


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.



**(a)** **Animations** **- Lego** **blocks** **stack** **and** **gold-**
**fsh** **crackers** **appear**


**(b)** **Target** **image** **hidden** **by** **creating** **a** **white**
**plane** **over** **the** **image**


**Figure** **4:** **Animations** **and** **‘Hide** **target** **Image’** **Feature**


_online_ _therapy_ _due_ _to_ _the_ _Covid-19_ _pandemic_ _presented_ _a_ _challenge._
_If_ _a_ _child_ _did_ _not_ _have_ _these_ _specifc_ _objects_ _at_ _home_ _or_ _did_ _not_ _fnd_
_them_ _interesting,_ _the_ _application_ _would_ _not_ _be_ _engaging/useful_ _for_
_them_ _[_ _41_ _]._ _This_ _feedback_ _made_ _it_ _clear_ _that_ _our_ _AR_ _application_ _had_ _to_
_be_ _more_ _customizable,_ _in_ _order_ _to_ _be_ _usable_ _outside_ _the_ _clinic_ _and_ _to_

_cater_ _to_ _children’s_ _diverse_ _interests._


_**Dynamic**_ _**Therapy**_ _**Environments**_ _**and**_ _**Children’s**_ _**Limited**_
_**Focus**_ _**- The**_ _**Need**_ _**to**_ _**Freeze**_ _**Content:**_ _Owing_ _to_ _the_ _nature_ _of_ _AR_
_technology,_ _the_ _AR_ _experience_ _is_ _only_ _visible_ _on_ _the_ _screen_ _when_ _the_
_device_ _camera_ _has_ _the_ _target_ _image_ _in_ _its_ _sight._ _However,_ _constantly_
_holding_ _the_ _iPad_ _over_ _the_ _target_ _image_ _proved_ _to_ _be_ _difcult_ _for_ _the_
_SLPs,_ _as_ _therapy_ _environments_ _are_ _dynamic;_ _the_ _child_ _may_ _be_ _unable_
_to_ _sit_ _at_ _a_ _table_ _(and_ _therefore_ _near_ _the_ _target_ _image)_ _for_ _long_ _periods_
_of_ _time,_ _or_ _they_ _may_ _get_ _distracted_ _by_ _another_ _item_ _in_ _the_ _room_ _and_
_wander_ _of._ _The_ _therapist_ _may_ _have_ _to_ _abandon_ _the_ _iPad_ _to_ _follow_
_after_ _the_ _child_ _and_ _may_ _fnd_ _it_ _difcult_ _to_ _make_ _the_ _child_ _sit_ _still_
_long_ _enough_ _to_ _trigger_ _the_ _AR_ _experience_ _again._ _We_ _therefore_ _needed_
_to_ _‘freeze’_ _the_ _AR_ _experience_ _on_ _the_ _screen,_ _that_ _is,_ _retain_ _the_ _AR_
_experience_ _on_ _the_ _screen_ _even_ _after_ _the_ _target_ _image_ _was_ _no_ _longer_ _in_
_view_ _of_ _the_ _device_ _camera._


**4.3** **Phase** **II** **- Re-designing** **the** **Application** **to**
**Make** **it** **More** **Customizable**


In Phase II of the design process, we added various customization
options to the application to give therapists and educational pro­
fessionals the ability to create and customize picture-based AR



**(a)** **Creation** **window**


**(b)** **Users** **can** **use** **the** **slide-in** **menu** **to** **add** **content** **to** **an** **AR**
**experience**


**(c)** **The** **selected** **target** **image** **appears** **in** **the** **middle** **of** **the**
**workspace**


**Figure** **5**


experiences according to the needs of the autistic population they
work with. We also added the _freeze_ _feature_ to make it easier to
view a completed AR experience. In this section, we provide details
about these features and the UI of the application.


_4.3.1_ **Customization** **Options:**
Users can avail the following customization options:

  - **Custom** **Target** **Images**   - Users can select custom images
to serve as targets for an AR experience by either taking
an image in real time, or uploading an image from their
device gallery. This gives each user the fexibility to create


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



AR experiences around the specifc visual supports they use
during learning/therapy exercises.

  - **Audio** **Prompts**   - Users can record an audio prompt for
an AR experience. The audio prompt plays automatically
when the target image is recognized by the application. Since
users will decide on the contents of the audio recording
themselves, they may choose to record short hints or longer,
more detailed prompts, depending on the activity they have
in mind.

  - **Videos**   - Users can associate videos with an AR experience
by either recording them in real time, or uploading videos
from their device gallery. We posit that this may be an im­
portant customization option as video modelling is widely
used as an instructional method when working with autistic
children [11, 23, 51].

  - **3D** **Models** **&** **animations**   - Users can add one or more

3D models to their AR experience from an in-built library
of 3D models that contains 40 models spanning the cate­
gories of food, hygiene, toys, etc. Each model has a default
audio prompt (the model’s name) and at least one default
animation associated with it. Users can record their own

audio prompts for a model, and choose between animations
if more than one is available for a particular model. Although
we initially added 3D models because they were essential
for the symbolic development use-case described in section
4.2.1, we were interested to know how users utilize them in
other use-cases or learning activities.


To simplify the process of creating and viewing an AR experience,
we decoupled the creation and viewing windows. The customization options described above can be accessed through the creation
window. The two windows are described below.


_4.3.2_ **Creation** **Window** **(Authoring** **Tool):**
The creation window (Figure 5a) allows users to create their own
picture-based AR experiences from scratch. The user must frst
upload a target image, which appears in the middle of the workspace (Figure 5c). Users can use the slide-in menu to add either
audio, video, 3D models, or a combination of the three, to any AR
experience (Figure 5b). The creation window shows what the target
image and virtual content would look like if users were viewing
them head-on, instead of from above. This is similar to how the AR
experience will appear in the AR-view and helps users adjust the
position of the virtual content in relation to the target image.


_**Miscellaneous**_ _**options:**_ _Users_ _can_ _change_ _an_ _animation_ _asso-_
_ciated_ _with_ _a_ _3D_ _model_ _(Figure_ _6b),_ _and_ _can_ _re-position,_ _resize,_ _and_
_rotate_ _video_ _objects_ _or_ _3D_ _models_ _within_ _their_ _AR_ _experience_ _(Figure_
_6c)._ _They_ _can_ _also_ _clear_ _the_ _work-space,_ _load/edit_ _previously_ _created_
_AR_ _experiences,_ _and_ _shift_ _the_ _camera_ _to_ _look_ _at_ _the_ _work-space_ _from_
_above._ _Moreover,_ _they_ _can_ _temporarily_ _hide_ _content_ _that_ _is_ _present_
_within_ _their_ _AR_ _experience_ _to_ _facilitate_ _adding_ _and_ _customizing_ _more_
_content._ _Users_ _can_ _also_ _access_ _video-based_ _tutorials_ _that_ _explain_ _how_
_to_ _create_ _AR_ _experiences_ _and_ _how_ _to_ _use_ _all_ _the_ _miscellaneous_ _fea-_
_tures/options_ _just_ _described._


_4.3.3_ **AR-View:** The AR-View is where users can view their AR

experiences by bringing their target images in front of their device



**(a)** **Users** **can** **upload** **existing** **videos** **or** **take** **them** **in** **real**
**time.** **Tapping** **on** **the** **video** **object** **(shown** **in** **the** **center** **of**
**the** **screen),** **plays** **or** **pauses** **the** **video.**


**(b)** **Users** **can** **select** **one** **of** **the** **two** **animations** **(stacking** **or**
**lining** **up** **the** **Lego** **blocks),** **using** **the** **animation** **window**
**shown** **on** **the** **right.**


**(c)** **Users** **can** **re-position,** **re-size** **and** **rotate** **3D** **models** **and**
**videos,** **using** **the** **window** **on** **the** **right.**


**Figure** **6**


cameras (Figure 7). This window contains features that facilitate
the use of AR within therapeutic/learning contexts.


_**Freeze**_ _**Feature:**_ _The_ _freeze_ _button_ _allows_ _users_ _to_ _freeze_ _the_ _video_
_background_ _on_ _the_ _screen_ _(Figure_ _7a),_ _while_ _keeping_ _the_ _AR_ _content_
_interactive._ _This_ _allows_ _them_ _to_ _retain_ _the_ _context_ _of_ _the_ _AR_ _experience_
_(the_ _video_ _background_ _and_ _the_ _target_ _image),_ _and_ _move_ _the_ _device_
_away_ _from_ _the_ _target_ _image_ _without_ _the_ _AR_ _experience_ _disappearing._
_This_ _could_ _be_ _useful_ _in_ _dynamic_ _therapy/learning_ _environments_ _where_


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.


_a_ _child_ _is_ _unable_ _to_ _stay_ _near_ _the_ _tabletop._ _The_ _therapist_ _could_ _activate_
_the_ _AR_ _experience,_ _freeze_ _it,_ _and_ _then_ _bring_ _the_ _iPad/device_ _closer_ _to_
_the_ _child_ _for_ _better_ _viewing._ _Prior_ _work_ _has_ _also_ _shown_ _the_ _efectiveness_
_of_ _such_ _a_ _feature_ _in_ _mobile-AR_ _contexts_ _[42]._



_**Setings**_ _**Menu**_ _**&**_ _**On-screen**_ _**Butons:**_ _The_ _settings_ _menu_ _allows_
_users_ _to_ _change_ _the_ _speed_ _of_ _animations_ _and_ _the_ _light_ _intensity,_ _hide_
_target_ _images_ _and_ _switch_ _between_ _‘sound_ _mode’_ _and_ _‘animation_ _mode’_
_for_ _the_ _3D_ _models_ _(Figure_ _7c)._ _The_ _latter_ _determines_ _what_ _happens_
_when_ _a_ _user_ _taps_ _a_ _3D_ _model_ _in_ _an_ _AR_ _experience_ _- either_ _the_ _associated_
_audio_ _or_ _the_ _chosen_ _animation_ _plays_ _out._ _In_ _situations_ _where_ _a_ _user_
_has_ _added_ _more_ _than_ _one_ _type_ _of_ _content_ _(audio,_ _video,_ _3D_ _models)_
_to_ _an_ _AR_ _experience,_ _they_ _can_ _toggle_ _through_ _the_ _content_ _using_ _the_
_‘Next’_ _and_ _‘Prev’_ _prompt_ _buttons_ _present_ _on_ _the_ _bottom_ _of_ _the_ _main_
_screen_ _(Figure_ _7a)._ _By_ _default,_ _the_ _3D_ _model_ _appears_ _frst,_ _then_ _video,_
_and_ _then_ _audio._ _Users_ _can_ _reverse_ _this_ _order_ _using_ _the_ _settings_ _menu._


_This_ _version_ _of_ _the_ _application,_ _at_ _the_ _end_ _of_ _phase_ _II,_ _was_ _used_
_when_ _conducting_ _formal_ _user_ _studies_ _with_ _therapists_ _and_ _educational_
_professionals_ _(section_ _5)._ .


**4.4** **Implementation** **Details**


The application was created using Unity [ 55 ] and C# scripting. We
used the ARCore [ 8 ] and ARKit [ 36 ] XR plugins to provide the
necessary AR functionality for both the android and iOS version
of application respectively. We used the interface provided by AR
Foundation [ 6 ], within Unity, to communicate with these two plu­
gins. This allowed us to use the same code-base to build both an
Android and an iOS version of the application.


**5** **USER** **STUDY**


To answer our research questions (section 3), we conducted a user
study that was approved by our university’s Institutional Review
Board. Recruitment was done over the course of fve months, from
June 2021 to October 2021. The details are as follows:


**5.1** **Participants**


We recruited participants using word-of-mouth and snowball sam­
pling. All our participants were therapists or educational profes­
sionals who had prior experience working with autistic individuals.
We recruited a total of 10 participants in the study; 7 participants
completed the study, 1 participant withdrew because she was not
comfortable with downloading the application on her personal
device, and 2 of them did not complete the study.

For simplicity, we refer to participants using ID numbers P1 to
P7. P1 and P2 belonged to the same clinic as the SLPs that helped
design the frst version of the application (Phase I). However, these
participants were not present during the design discussion in phase
I and did not have access to the application prior to their enrollment
in the study. Since the frst version of the application was created
for a specifc use-case for the clinic, we wanted to see how the latest,
more customizable version could be useful for the same use-case.

Recruiting therapists who had negligible involvement in the design
and creation of the application, but were familiar with the use-case,
allowed us to get an unbiased opinion.



**(a)** **The** **3D** **Lego** **block** **is** **superimposed** **over** **the** **target** **im-**
**age.** **The** **Freeze** **and** **Next** **and** **Prev** **prompt** **buttons** **are**
**present** **at** **the** **bottom** **of** **the** **screen**


**(b)** **A** **video** **object** **superimposed** **over** **the** **target** **image**


**(c)** **The** **diferent** **settings** **options**


**Figure** **7**


Please note, no autistic children participated in this study. Our
goal was to get feedback from therapists and educational profes­
sionals frst and refne the application, before testing it with autistic
children in future studies.


**5.2** **Study** **Method**


Each participant was enrolled in a diary study spanning 2 weeks.
Participants frst took part in a one-on-one information session
via Zoom [ 9 ], where they were introduced to the application and
downloaded it on their preferred devices. They were instructed to


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



use the application over the next 2 weeks to create their own AR
experiences, and provide feedback about its strengths/weaknesses
and what learning activity or contexts of use they had in mind. We
built feedback options into the application to encourage partici­
pants to provide feedback. The types of feedback they provided are
discussed in section 5.4.


At the end of their 2 weeks, participants took part in a one-on-one
semi-structured interview with a member of the research team. This

helped us get an in-depth understanding of how the participants
used the application and in what contexts, what challenges they
faced, and what improvements they would like to see. At the end
of the interview, participants were asked to permanently delete the
application from their devices.


**5.3** **Procedures**


_5.3.1_ **Information** **Session:** In the information session, a mem­
ber of the research team frst explained what picture-based aug­
mented reality was and then played demo/screen capture videos
of the application to explain its layout and the features. Interested
participants were taken through an informed consent process in
the presence of a witness. The participants then downloaded the
application on their preferred devices. All our participants used
iOS devices. For iOS users, we distributed the application through
Apple’s Testfight [7].


_5.3.2_ **Diary** **Study** **and** **Follow-up** **Interview:** During the 2-week
diary study, we sent emails twice a week to remind and encourage
our participants to continue testing the application and provide
feedback. At the end of the 2 weeks, we conducted a one-on-one
interview with them via Zoom. These interviews typically lasted
an hour and were either audio or audio/video recorded based on
the participants’ preferences (indicated in the consent forms).


**5.4** **Data** **Collection** **&** **Analysis**


_5.4.1_ **Types** **of** **Data** **Collected:** We collected the following qualitative data:


  - Written feedback   - Participants provided written feedback
by flling out a short Qualtrics survey [ 4 ] that opened up
in a browser when they clicked the ‘Survey’ button in the
application. This short survey asked participants to indicate
which features they used, how they used them, and any other
comments they had.

  - Voice notes   - Participants provided verbal feedback through
the application by recording voice notes and pressing the
‘Send Voice Note’ button to upload them to an AWS simple
storage bucket [ 10 ]. Similar to the survey, participants had to
elaborate on which features they used, and in what contexts.

  - Interview recordings   - The audio/video recordings of interviews were manually transcribed. In the interviews, we
asked our participants to describe their overall experience
with the application, what AR experiences they created and
for which learning exercises, what features may be more
useful in autistic contexts etc.


_5.4.2_ **Analysis** **Methods:** We performed a thematic analysis on
the written feedback, and the transcripts of the voice notes and
interview recordings. Braun & Clarke’s [18] approach to thematic



analysis was used. A member of the research team frst transcribed
the data, generated initial codes, gathered data/quotes pertaining
to each code, collated them into themes, discussed the themes with
other members of the research team, and then reviewed and refned
them. A second coder (from outside the initial study team) validated
the themes and the data belonging to each particular theme.


**6** **RESULTS**


We asked our participants to explore the application while keeping
in mind the autistic population they work with, and the learning
exercises they conduct. As such, some participants only explored
features relevant to the context they were developing their AR
experiences for, while others explored as many features as possible.
In this section, we frst highlight the participants’ general experi­
ence/progress with the application and provide details about the
learning activities they had in mind. We then analyze their feedback
and interview responses to answer our research questions.


**6.1** **Participants’** **Progress** **With** **the** **Application**


All our participants encountered a learning curve when testing
the application, but some made more progress than others. These
participants either got better after repeatedly using the application,
were able to intuitively fgure out what to do, or took advantage of
the in-app tutorials.


_6.1.1_ **Geting** **Beter** **Afer** **Repeated** **Use:** Some participants
mentioned getting better at using the application over time. For
example, P1 said that she was able to ‘fgure things out’ after she
‘played around with it’ and that with repeated use, she would be
‘more comfortable’ with the application. Similarly, P2 got faster at
using the application over time. She stated, ‘I defnitely got faster at
it. And so once I was able to do it like a couple times, it was pretty
seamless.’


_6.1.2_ **Using** **One’s** **Intuition:** P5 mentioned that the initial tuto­
rial in the one-on-one information session was enough for her to
use the application ‘independently’, and she ‘didn’t really have to
go back to the tutorials that are built in’. She thought the buttons
‘were clear’, ‘made sense’ and if she was not sure what to do then
as an ‘intuitive user of apps like this’, she was able to ‘fgure it out’.


_6.1.3_ **Leveraging** **the** **In-app** **Video** **Tutorials:** P1 mentioned
that the in-app tutorials were ‘defnitely helpful’ and P7 said that
they were ‘great reminders’. P6 had trouble remembering what
the miscellaneous buttons on the screen did (e.g. the ‘load’ but­
ton) and sought help from the in-app tutorials. She stated that she
was not ‘good at remembering steps’ so she watched the tutorials
multiple times, which were ‘very clear and very easy to understand’.


Participants who made less progress either failed to notice the
in-app video tutorials, or were unclear on how to trigger the AR
experiences they had created.


_6.1.4_ **Lack** **of** **Prior** **Experience** **With** **AR** **&** **Failure** **to** **Notice**
**In-app** **Tutorials:** P4 enjoyed ‘exploring’ the application, but was
‘new to AR’ and so ‘had some difculty’ with creating full AR
experiences and viewing them. She did not notice the ‘tutorial’
button in the application and was therefore unable to get help.


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.



_6.1.5_ **Confusion** **About** **How** **to** **Trigger** **an** **AR** **Experience:**
P3 misunderstood how to trigger an AR experience and instead
of using the target images to trigger the experience, she tried to
use the actual objects she took images of. For example, instead of
holding her camera to the picture of her driveway, she held it up to
the actual driveway and had a hard time making sure the camera
was in the ‘right place’ to trigger the experience. This negatively
impacted her progress with the application. Similarly, P6’s AR experiences did not appear on the screen because her target images
were so big that the entire image was not in view of the device
camera. We identifed and corrected this issue during the interview,
and she was able to trigger her AR experiences right then. That
said, both participants provided feedback based on the features they
successfully explored, and brainstormed improvements. Despite
encountering issues, P6 ‘really liked’ using the application and, at
the end of the study, said that it was ‘too bad’ she could not have it
again.


In section 7.3 we discuss some improvements we can make to
help reduce the application’s learning curve.


**6.2** **Details** **of** **Learning** **Activities**


Our participants envisioned creating AR experiences for a range of
learning activities. Table 1 provides background information about
each participant, the features they explored, and what learning
contexts they had in mind.

P1 and P2 considered the same symbolic development use-case
that was described in section 4.2.1 – they wanted to help children
make intentional choices using pictures of objects (toys, food etc.)
by superimposing them with 3D models of the objects to strengthen
the link between 2D images and their 3D referents. P3 wanted to use
the application to give children situational cues – such as how to
behave when entering a classroom. P3 and P4 both wanted to teach
daily living skills, such as ‘hair-brushing’ or tooth-brushing’ by
using the application to superimpose pictures representing the steps
of an activity with videos of the activity being performed. Children
would trigger these videos when they forgot the steps in a task. P5
was confdent that her high-school students could independently
use the application during group-work to create an AR battle game
using picture cards. Students would collaborate to make the rules of
the game, would decide which pictures to use, and would associate
actions with each picture (using audio or 3D models). Players could
trigger these actions by holding their iPads over each picture. This
spurred the discussion on whether any changes need to be made to
the UI so that autistic children could create AR experiences on their
own (section 7.4). P6’s school used worksheets (called ‘News2You’)
that paired action words, such as kicking, with pictures depicting
the action. She wanted to superimpose these static pictures with
videos showing what the actions looked like. Lastly, P7 envisioned
using the application to give ‘reminders or second prompts or visual
cues’ to children during group activities or if a paraprofessional
was not nearby to repeat instructions. He also wanted to reinforce
the visual schedules in his classroom with audio prompts. Children
could then ‘independently go up and check the schedule’ by holding
their iPads over the images in the schedule.



**6.3** **Participants’** **Experiences** **With** **The** **Various**
**Customization** **Options**


As mentioned in 6.2, our participants envisioned using the appli­
cation for a plethora of learning activities, for autistic children
ranging from younger kids with severe autism, to those who were
independently navigating high-school. In this section, we discuss
our participants’ experiences with the application’s customization
options and answer **RQ** **1** .


_6.3.1_ **Recording** **Custom** **Audio:** Participants could record au­
dio prompts that would either play automatically when a target
image was recognized, or would play when the associated 3D model
was tapped. P1 added the sound of a train honking from a Youtube
clip to the 3D model of ‘Thomas the train’ for her choice-making ac­
tivity and said that she could see ‘a kid really enjoying it because it’s
so realistic’. P5 highlighted that children ‘may be stimulated by hav­
ing their voice recorded’ and wanted her students to record audio
prompts for actions associated with each card in their battle game.
For example, a card could say, ‘You lost fve points’. P6 and P7 used
videos for their primary use-cases (teaching language and creating
reminders), but used audio for secondary activities. They imagined
using audio to pair instructions for a math lesson, or sounds of
musical instruments with worksheets and pictures respectively.
Children could hold up their devices to the worksheets/pictures to
listen to the instructions or the musical notes.


_6.3.2_ **Adding** **A** **Custom** **Video:** Participants liked the option to
add videos into the AR experience because videos either grasp a
child’s ‘attention’ better than ‘static’ content (P1) or because autistic
individuals ‘imitate video models more’ than if a person performed
the same action in front of them (P2). The latter especially could
help with teaching daily living skills. P2 added a video of someone
brushing their teeth, over an image of a tooth brush, to teach this
daily living task and P6 imagined using videos to demonstrate
the meaning of action words and emotions. For example, when
conducting a lesson on frustration, she could superimpose an image
of a frustrated kid with a video showing what ‘frustration looks
like’. P7’s goal was to foster independence in the children he worked
with - If stuck, they could hold their iPads up to their worksheets
to trigger a video of P7 giving them instructions, such as ‘please
write three complete sentences’. While an audio prompt may have
achieved the same purpose, it seemed the participants valued the
visual nature of videos. Participants who had trouble using this
feature (P4) or who found it irrelevant to their use-case (P5) also
thought that it had ‘potential’.


_6.3.3_ **Adding** **3D** **Models:** Some participants used 3D models as
an integral part of their AR experience (e.g., P1 and P2 used the
train, bubble wand, Lego block etc. for choice making activities),
while others explored them out of curiosity (P3 to P7). P5 and P6
liked the ability to add multiple 3D models to an AR experience - P5
could then use diferent 3D models at the same time to demonstrate

a theme, for example adding a cofee cup and toast together to rep­
resent ‘breakfast’, and P6 could add multiple 3D models to an AR
experience for a math activity (e.g., 2 + 5). That said, participants
agreed that having ‘more options’ (P1) or a ‘broader range’ (P2) of
3D models would be helpful. P2 worked with kids‘ in play contexts’
and would have liked to see 3D models of other toys and P5 said


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece


**Table** **1:** **Participants’** **Backgrounds**


























































|ID|Participant Occupa­<br>tion|Population in Mind|Learning Activity|Features Tested|Intended Users of the Applica­<br>tion|
|---|---|---|---|---|---|
|P1 <br>|Speech Language <br>Pathologist <br>|Younger <br>kids <br>with <br>moderate-severe <br>autism <br>who are minimally verbal <br><br><br>|Choice making & sym­<br>bolic development <br><br><br>|Audio, Video, 3D <br>models (a few) & an­<br>imations, Freeze <br>|The therapist holds the device <br>and shows the screen to the <br>child, the child may interact <br>with the virtual content them­<br>selves or with the therapist’s <br>help <br>|
|P2 <br>|Speech Language <br>Pathologist <br>|Younger <br>kids <br>with <br>moderate-severe <br>autism <br>who are minimally verbal <br><br><br>|Choice <br>making <br>& <br>symbolic development, <br>teaching daily living <br>skills <br>|Audio, Video, 3D <br>models (a few) & an­<br>imations, Freeze <br>|Same as above <br>|
|P3 <br>|Speech Language <br>Pathologist <br>|7th/8th <br>graders <br>with <br>Autism who have artic­<br>ulation <br>or <br>signifcant <br>communication difculties <br><br><br>|Teaching daily living <br>skills <br>|Video, 3D models (a <br>few) <br>|The therapist creates the AR ex­<br>periences beforehand, and the <br>kids use the AR-View to view <br>and interact with the virtual <br>content independently <br>|
|P4 <br>|Special Education <br>Teacher <br>|High-school <br>kids <br>with <br>moderate-severe Autism <br>|Teaching daily living <br>skills <br>|3D models <br>|— <br>|
|P5 <br>|Speech Language <br>Pathologist <br>|High-school kids who are <br>independently navigating a <br>public school setting <br>|Group work / collabo­<br>rative learning, creating <br>AR games together <br>|Audio, Video, 3D <br>models (a few) & an­<br>imations, Freeze <br>|The therapists or the kids in­<br>dependently create their own <br>AR experiences and use the AR-<br>view to show others what they <br>have created <br>|
|P6 <br>|Occupational Ther­<br>apist <br>|14 y/o with Down’s syn­<br>drome & a child who suf­<br>fered stroke in utero - kids <br>who have difculty speak­<br>ing, low cognition and are <br>emerging readers <br>|Worksheets with action <br>sentences, connecting <br>words and language, <br>teaching <br>emotions, <br>teaching math concepts <br><br>|Audio, Video, 3D <br>models (a few) & an­<br>imations <br>|The therapist creates the AR <br>experiences, and the kids view <br>them independently <br>|
|P7|Special Education <br>Teacher|autistic children in 4th <br>grade|Giving <br>children <br>re­<br>minders or directions <br>about individual or <br>group-related <br>class <br>activities, <br>visual <br>schedules and pairing <br>musical <br>notes <br>with <br>images <br>of <br>musical <br>instruments|Audio, Video and <br>3D models (a few)|The therapist creates the AR <br>experiences, and the kids view <br>them independently|


that categories related to daily living, such as ‘transportation’ or
‘morning routine’, and for her use case, categories like ‘battle ships’
would be helpful. P7 typically puts clipart on his slides to show chil­
dren what they need for an activity and could have done the same
with AR if 3D models related to school supplies had been available
in the in-app library, such as rulers, pencils, and crayons. Therefore,
providing users with the ability to add 3D models themselves or
search from a larger database of 3D models would be helpful. We
discuss this more in section 6.5.1.


_6.3.4_ **Using** **Animations** _:_ Some 3D models had simple anima­
tions, such as an apple rotating, while others had functional anima­
tions, such as a pair of hands getting soap from a soap dispenser.
Participants found functional animations - animations that show



the function of a particular 3D model – to be more useful. For ex­
ample, if the toy train had an animation of the train gliding over,
P1 could use it to teach concepts like ‘pushing the train’. Similarly,
P2 stated that the animations would be great for teaching ‘choice­
making’, as they depict the function of the object. Although the
3D models of day-to-day objects, such as the toothpaste, had func­
tional animations, P2 thought that having a sequence of animations
that depict the item’s use (such as all the steps involved in putting
toothpaste onto a toothbrush) could be helpful in teaching daily
living skills. Thus, while simple animations attract children’s atten­
tion, functional animations are more useful from a teaching point
of view. While animations may not be useful for every child - P3
stated that they would not be necessary for the 7th/8th graders she
works with – they can be ‘really important to have’ when teaching


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.



children with severe autism, or to make the application useful for
‘a wide variety of clients’ (P3).


_6.3.5_ **Are** **The** **Given** **Customization** **Options** **Suficient?** Recall that **RQ1** considered whether the application’s customization
options were sufcient to create AR experiences for a range of autistic children and learning exercises. While participants suggested
improvements for existing customization features, they did not
fnd anything ‘missing’, and although participants were considering diferent learning activities, they were each able to fnd some
customization options that were useful for their context. P6, for
example, stated the following, ‘I could defnitely use the audio. I
could defnitely use video. I could defnitely use an image. I can use
all your features to teach a lesson on an emotion’. There is, however,
a question of _how_ _much_ _customization_ _is_ _enough_ ? P5 thought the
application provided a good balance of ‘fexibility’, without the
‘possibilities being endless’. P5 envisioned a scenario where her
students would create AR experiences themselves, instead of the
teacher/therapist. To that end she stated that some previous tools
she had used with her students (e.g., 3D printing software) had ‘too
many options’, and students got ‘bogged down in the details’, were
‘too frustrated’, or ‘working too independently without consulting
each other’, thus defeating the purpose of group exercises. Our
application was simple enough that she envisioned her students
‘running with it’ and even ‘coming up with something more creative’ than her game idea, but without getting too bogged down.
That said, a user may come up with a unique or niche use-case
which requires more customization than what is currently available
in the application. Future studies will need to investigate this. In
the next subsection, we attempt to answer **RQ** **2** .


**6.4** **Can** **the** **Freeze** **Features** **Facilitate** **the** **Use**

**of** **AR** **in** **an** **Autistic** **Context?**


Our second goal was to understand whether the freeze feature could
facilitate the use of AR with autistic individuals. Participants liked
the freeze feature because it removed the need to continuously
hold the iPad/device over a target image to keep an AR experience
interactive. P5 saw its utility in group settings - she could ‘capture’
the AR experience on the screen and then show it to children who
were sitting further away from her in a group. She also thought that
taking a screenshot of the frozen AR experience and putting it in
a visual schedule would help prepare children for future activities
involving the application. Moreover, it could be helpful in scenarios
where children were unable to focus or stay still. P1 mentioned that
‘attention is sometimes very impacted’ for children on the spectrum,
so they may ‘wander the room’ or ‘walk away’ when she tries to
show them something on the iPad. The freeze feature would be
‘useful’ in these situations as she could trigger the AR experience,
leave the target image on the desk, and go where the child is. P3
echoed this sentiment and said that having the AR experience not
‘disappear once you move to a diferent spot’ would be helpful.
Therefore, it seems that the freeze feature may be especially
important to have when using AR in an autistic context. In contrast
to the freeze feature, most participants skipped over the settings
options in the AR-View or only tried a few options. When asked
why they did so, some participants said that they either did not feel
the need to edit the default settings, or they were not needed for



the activity being considered. In the next subsection, we talk about
some of the practical challenges that users may face when using
picture-based AR in day-to-day settings ( **RQ** **3** ).


**6.5** **Practical** **Challenges** **of** **Using** **AR** **in**
**Therapy** **/** **Learning** **Settings**


When thinking of using AR in day-to-day settings, our participants
were concerned about being able to access a wide range of 3D
models, being able to create AR experiences on-the-fy or ‘just-intime’ and generalizing AR Experiences. We discuss these concerns
below.


_6.5.1_ **Access** **to** **a** **Wider** **Range** **of** **3D** **Models:** As mentioned in
section 6.3.3, most of our participants thought that having a larger
library of 3D models at their disposal would help them create AR
experiences for a wider audience. P3 thought that being able to add
one’s own 3D models would be helpful. For example, participants
could search for and download 3D models from the internet. How
ever, these models may not have sounds or animations built-in; we
had to build the animation and sound associated with each model

in the application’s library. Moreover, other participants, may feel
the same as P2 who stated that this study was her ‘frst time really exploring AR’, and she was unaware that one could search for
and download 3D models from the internet. Therefore, building a
library of models into the application, or hosting one online that
users can access from within the application, may be preferable. If
users are unable to fnd a relevant 3D model, they could potentially
make requests for 3D models and associated animations through
the application, which would then be fulflled by members of the
research team.


_6.5.2_ **Creating** **AR** **Experience** **On-the-fly** **or** **Just-in-time:**
Preparing resources or creating exercise material according to each
child’s interests can be a difcult and time-consuming process. Being able to ‘customize an AR experience on-the-fy’ during a therapy
session would make a ‘huge diference’ as it would reduce the ‘prep
time’ participants have to put in _beforehand_ (P1). P3 echoed this sentiment, stating that one must ‘make things quickly’ while working
with some children, and that it currently requires a ‘lot of planning’
to create relevant AR experiences. Therefore, some degree of intelligence / automation may be helpful. For example, P2 thought
that it would be helpful if the application could detect the contents
of a target image and quickly provide options for appropriate 3D
models and audio prompts that label the objects. This would allow therapists and educational professionals to quickly create AR
experiences _during_ a therapy session, based on what the child is
interested in at that moment. In section 9.1 we present a prototype
for ‘just-in-time’ content creation as a proof of concept.


_6.5.3_ **Generalizing** **AR** **Experiences:** P3 pointed out that ‘generalization is a big area of focus when working with people on the
spectrum’. It involves learning a skill or concept and using it in any
environment, not just the one in which it was taught. P3 thought
it would be great if an AR experience could be generalized. For
example, in the context of hand-washing, the application would
recognize that a sink was present and would pull up the AR content
(audio, hand-washing videos etc.) that she had previously associated with another sink. While she was focused more on recognizing


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



3D objects and using those as triggers for AR experiences instead
of pictures, her idea could be extrapolated to work for pictures as
well. Moreover, she thought that if a clinician could create an AR
experience and share it so that ‘parents can use it at home’, it would
help generalize the skills taught in school to a home setting. We
discuss this further in section 7.


**7** **DISCUSSION**


While users found the application’s features and customization
options to be useful, there is room for improvement. In this section,
we use insights from our study to propose design implications
for future applications (AR or otherwise) that target therapists and
autistic contexts. We also discuss ways of reducing the application’s
learning curve and position autistic children as content creators.


**7.1** **Sharing** **AR** **Experiences** **&** **Just-in-Time**
**Creation** **- Implications** **for** **Content**
**Creation** **Apps**


Sharing AR experiences was initially brought up in the context
of generalization (6.5.3), but could also facilitate just-in-time con­
tent creation and collaboration/group-work. For example, thera­
pists/teachers could share their AR experiences with parents, or
vice versa, by uploading them to an online portal. This would allow
children to be exposed to the same prompts/AR experiences in difer­
ent environments, which could help with generalizing ideas/skills.
Additionally, therapists could download and edit pre-made AR ex­
periences or templates to speed up the creation process and reduce
their own time and efort. Moreover, in class/group activities, teach­
ers could upload a half-fnished AR experience for their students to
download and edit. Students could also share AR experiences with
each other to collaborate or show what they have created so far.
Therefore, applications (AR or otherwise) that involve content cre­
ation and target therapists/teachers and learning settings, should
provide support for content-sharing and collaboration.


**7.2** **How** **Much** **Customization** **is** **Enough** **-**
**Implications** **for** **Autism-Focused**
**Customizable** **Applications**


Recall that in section 6.3.5, we discussed whether or not our cus­
tomization options were sufcient. Improvements to 3D models
notwithstanding, perhaps one reason our approach to customiza­
tion was successful was because we provided sufcient fexibility
without the application becoming too overwhelming. For example,
users only had the option of adding audio, video or 3D models but
could decide themselves which of the three they wanted to add to
an AR experience and what the _content_ of the audio and/or videos
should be. This allowed them to create AR experiences for a vari­
ety of learning contexts. Moreover, for future AR application that
position autistic children as content creators, it might be helpful
to provide a limited set of options but provide fexibility within
those options, so that children can be creative without getting too
‘bogged down’ in the details. Of course some learning contexts may
require support for a lot more customization, and by no means
do we claim that our approach fts every context. However, as a



starting point, future applications might consider providing fex­
ibility within a limited set of customization options, or gradually
introducing customization options to users. The latter is discussed
in section 7.3 and 7.4.


**7.3** **Reducing** **the** **Application’s** **Learning** **Curve**

**- Tutorials** **&** **Gradually** **Exposing**
**Functionality**


Recall that some participants made more progress in using the
application’s features than others. Although we added in-app video
tutorials, interactive tutorials where the application helps the user
create and trigger their frst AR experience and points out useful
features, may further reduce the learning curve. P7 also advocated
for gradually exposing the application’s functionality to users. He
stated that a lite version of the application, where users can only add
audio to a target image, may be helpful for users who are not very
technologically savvy. He stated that ‘a broader range of people
are more comfortable’ with taking a photo or recording something,
so limiting the customization options can help ease them into the
creation process. Users can later upgrade to a version with videos
and 3D models.


**7.4** **Autistic** **Children** **as** **Content** **Creators** **-**

**Will** **Our** **Current** **UI** **Sufce?**


We initially envisioned therapists and educational professionals as
the main creators of AR experiences, while the autistic children
they worked with would simply view the AR content. P5, however,
stated that her high-school students could easily navigate the fea­
tures of the application to create their own AR experiences. This
begs the question: is the application’s UI sufcient to allow autistic
children to create their own AR experiences, or are modifcations
necessary? For example, some children may wish to hide some
buttons on the screen to reduce visual input. Other children may
have difculty remembering the steps involved in creating an AR
experience and may beneft from an interface that sequentially
takes them through each step of the creation process. P7’s idea of
gradually exposing functionality to users, as mentioned in section
7.3, may be useful here as well; children can take their time and
become comfortable with using one customization option before
moving onto another. To make the application accessible to a wide
range of content creators, we need to conduct user studies with
autistic individuals, particularly those who can independently nav­
igate similar applications and are interested in AR. We leave this
for future work.


**8** **KEY** **TAKEAWAYS**


The following bullet points summarize this work’s key takeaways:


  - The customization options we provided (audio, video and 3D
models with animation) allowed therapists/educational pro­
fessionals to create AR experiences for a variety of learning
exercises. Participants appreciated our approach of provid­
ing fexibility within a limited set of customization options
as it prevented users from getting too bogged down. Future
researchers/designers creating applications in an AR and


ASSETS ’22, October 23–26, 2022, Athens, Greece Tooba, et al.



autistic domain may beneft from using this approach to
customization (as a starting point).

  - The freeze feature can be helpful when working with autistic
students with limited attention, or when working in group
settings. Future researchers/designers creating AR applications should consider providing a way to freeze AR experiences on the screen to make it easier to use with autistic

children.

  - Therapists and educational professionals may need to create
content just-in-time during therapy sessions or may need to
generalize the same content to diferent situations. Future
researchers/designers who are developing content-creation
applications for autistic contexts (AR or otherwise) should
provide avenues for creating content quickly, or sharing
content/AR experiences with others.


**9** **LIMITATIONS** **&** **FUTURE** **WORK**


Our study had some limitations: Firstly, participants had a limited
selection of 3D models. Future prototypes should allow users to
upload their own 3D models, or provide a larger library to choose
from. Secondly, we cannot make any claims about whether the
application’s current UI will be sufcient for autistic children to
create their own AR experiences. We posit that a lite version, or a
version that either gradually exposes functionality or systematically
takes the user through each step of the creation process, might be
helpful. That said, we have yet to conduct user studies with autistic
children to confrm this hypothesis. The next subsection discusses
a proof-of-concept prototype that could be used in future studies
to answer some of these questions.


**9.1** **Just-In-Time** **Creation** **and** **Sequential**
**Interface**


Based on the discussion in 6.5.2 and 7.4 about just-in-time con­
tent creation and the benefts of a sequential interface, we made
some modifcations to the application’s UI. The third version of the
application takes users through each step of the creation process
sequentially. Users can move between steps using the buttons at
the bottom of the screen (fgure 8).

The application uses the AWS Rekognition [ 48 ] service to iden­
tify labels for the object, scene or actions present in a target image
(fgure 8a). Based on the label that a user selects, the application
provides recommendations for 3D models (fgure 8b). Users can
still explore all the categories manually but we posit that providing
them with some recommendations might speed up the creation
process. Moreover, we use the AWS Simple Storage Service (S3) [ 10 ]
to host a larger library of 3D models. Users can download these
3D models through their application. This allows us to provide
a larger library of 3D models without encroaching on the user’s
device storage.

This third prototype is a small proof-of-concept. We hope to use
it in future design meetings/studies with therapists, educational
professionals, and autistic children to understand whether they
prefer UIs where the customization options are exposed gradu­
ally/sequentially or all at once, and whether the recommendations
given by the application are helpful when creating AR content.



**(a)** **Sequential** **Interface.** **A** **user** **has** **uploaded** **a** **target** **im-**
**age** **of** **fruits.** **The** **application** **used** **the** **AWS** **Rekognition**
**service** **to** **provide** **the** **following** **labels** **for** **the** **contents** **of**
**the** **image:** **‘Plant’,** **‘Fruit’,** **‘Food’** **etc.** **The** **labels** **appear** **in**
**the** **window** **at** **the** **bottom-right** **and** **the** **user** **can** **select** **the**
**most** **appropriate** **label.**


**(b)** **3D** **Model** **Recommendations.** **The** **application** **has** **rec-**
**ommended** **several** **3D** **models** **to** **the** **user** **based** **on** **the** **label**
**they** **chose** **in** **the** **previous** **step** **(‘Fruits’).** **The** **recommenda-**
**tions** **are** **shown** **in** **window** **on** **the** **left.** **The** **user** **can** **explore**
**all** **the** **other** **categories** **of** **3D** **models** **using** **the** **buttons** **at**
**the** **top-right** **of** **the** **screen.**


**Figure** **8**


Other features, such as sharing AR experiences through an online
portal, are more complex and require further thought.


**10** **CONCLUSIONS**


This paper describes the design and evaluation of CustomAR, a
mobile application that allows therapists to create picture-based
AR experiences from scratch for use in autism-based learning exer­
cises. A diary and interview study revealed that therapists found
the application’s customization options to be sufcient for creat­
ing AR experiences for a variety of learning exercises, ranging
from choice-making activities to reminders, visual schedules and
groupwork. We posit that our approach was successful because we
provided a fair amount of fexibility, without inundating users with
customization options. Participants also thought that the freeze
feature would be useful when working with children with limited
attention. Moreover, our study highlighted some challenges to us­
ing picture-based AR in practical therapy settings, such as fnding


Designing a Customizable Picture-Based AR Application For Therapists Working in Autistic Contexts ASSETS ’22, October 23–26, 2022, Athens, Greece



3D models that capture the children’s interests, generalizing con­
cepts, and creating AR experiences quickly during therapy sessions.
Moving forward, application developers looking to create customiz­
able applications for autistic contexts, should allow users to share
their AR experiences or create experiences quickly – the latter may
require incorporating some degree of automation or intelligence
into the application.


**ACKNOWLEDGMENTS**


We thank Hedi Skali, a high-school intern who worked with us
during the summer of 2019. We also thank the reviewers for their
eforts in reviewing this work and providing constructive feedback.


**REFERENCES**


[1] 2017. Daily living skills: Strategies to help sequence & achieve personal hy­

giene tasks. [https://www.toolstogrowot.com/blog/2017/08/09/daily-living­](https://www.toolstogrowot.com/blog/2017/08/09/daily-living-skills-strategies-to-help-sequence-achieve-personal-hygiene-tasks)
[skills-strategies-to-help-sequence-achieve-personal-hygiene-tasks](https://www.toolstogrowot.com/blog/2017/08/09/daily-living-skills-strategies-to-help-sequence-achieve-personal-hygiene-tasks)

[2] 2021. AugmentedClass! augmented reality for education - apps on Google Play.

[https://play.google.com/store/apps/details?id=com.AugmentedClass.AClass](https://play.google.com/store/apps/details?id=com.AugmentedClass.AClass)

[3] 2021. The benefts of visual supports for children with autism. [https://www.](https://www.autismparentingmagazine.com/benefits-of-autism-visual-supports/)

[autismparentingmagazine.com/benefts-of-autism-visual-supports/](https://www.autismparentingmagazine.com/benefits-of-autism-visual-supports/)

[4] 2021. Qualtrics XM - experience management software. [https://www.qualtrics.](https://www.qualtrics.com/)

[com/](https://www.qualtrics.com/)

[5] 2021. What is Visual Scheduling? [https://www.appliedbehavioranalysisprograms.](https://www.appliedbehavioranalysisprograms.com/faq/what-is-visual-scheduling/#:~:text=Visual scheduling is a systematic,and achieve success in life.)

[com/faq/what-is-visual-scheduling/#:~:text=Visualschedulingisasystematic,](https://www.appliedbehavioranalysisprograms.com/faq/what-is-visual-scheduling/#:~:text=Visual scheduling is a systematic,and achieve success in life.)
[andachievesuccessinlife.](https://www.appliedbehavioranalysisprograms.com/faq/what-is-visual-scheduling/#:~:text=Visual scheduling is a systematic,and achieve success in life.)

[6] 2022. About AR Foundation: AR FOUNDATION: 4.1.7. [https://docs.unity3d.](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@4.1/manual/index.html)

[com/Packages/com.unity.xr.arfoundation@4.1/manual/index.html](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@4.1/manual/index.html)

[7] 2022. Apple. [https://testfight.apple.com/](https://testflight.apple.com/)

[8] 2022. Build new augmented reality experiences that seamlessly blend the digital
and physical worlds. [https://developers.google.com/ar](https://developers.google.com/ar)

[9] 2022. Video conferencing, Cloud Phone, WEBINARS, Chat, Virtual EVENTS:
ZOOM. [https://zoom.us/](https://zoom.us/)

[10] 2022. What is Amazon S3? - amazon simple storage service. [https://docs.aws.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

[amazon.com/AmazonS3/latest/userguide/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

[11] Mohammed Alzyoudi, AbedAlziz Sartawi, and Osha Almuhiri. 2015. The impact
of video modelling on improving social skills in children with autism. _British_
_Journal_ _of_ _Special_ _Education_ 42, 1, 53–68.

[12] Zhen Bai, Alan F Blackwell, and George Coulouris. 2013. Through the looking
glass: Pretend play for children with autism. In _2013_ _IEEE_ _International_ _Symposium_
_on_ _Mixed_ _and_ _augmented_ _reality_ _(ISMAR)_ . IEEE, 49–58.

[13] Zhen Bai, Alan F Blackwell, and George Coulouris. 2015. Exploring expressive
augmented reality: The FingAR puppet system for social pretend play. In _Proceed­_
_ings_ _of_ _the_ _33rd_ _Annual_ _ACM_ _Conference_ _on_ _Human_ _Factors_ _in_ _Computing_ _Systems_ .
1035–1044.

[14] Andy Bondy and Lori Frost. 2011. _A_ _picture’s_ _worth:_ _PECS_ _and_ _other_ _visual_
_communication_ _strategies_ _in_ _autism_ . Woodbine House.

[15] Monique Botha, Jacqueline Hanlon, and Gemma Louise Williams. 2021. Does lan­

guage matter? Identity-frst versus person-frst language use in autism research:
A response to Vivanti. _Journal_ _of_ _Autism_ _and_ _Developmental_ _Disorders_, 1–9.

[16] Brian A Boyd, Maureen A Conroy, G Richmond Mancil, Taketo Nakao, and Peter J
Alter. 2007. Efects of circumscribed interests on the social behaviors of children
with autism spectrum disorders. _Journal_ _of_ _autism_ _and_ _developmental_ _disorders_
37, 8, 1550–1561.

[17] Jorge Brandão, Pedro Cunha, José Vasconcelos, Vítor Carvalho, and Filomena
Soares. 2015. An augmented reality gamebook for children with autism spectrum
disorders. In _The_ _International_ _Conference_ _on_ _E-Learning_ _in_ _the_ _Workplace_ . 1–6.

[18] Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology.
_Qualitative_ _research_ _in_ _psychology_ 3, 2, 77–101.

[19] Chien-Hsu Chen, I-Jui Lee, and Ling-Yi Lin. 2016. Augmented reality-based videomodeling storybook of nonverbal facial cues for children with autism spectrum
disorder to improve their perceptions and judgments of facial expressions and
emotions. _Computers_ _in_ _Human_ _Behavior_ 55, 477–485.

[20] Chi-Hsuan Chung and Chien-Hsu Chen. 2017. Augmented reality based social
stories training system for promoting the social skills of children with autism.
In _Advances_ _in_ _ergonomics_ _modeling,_ _usability_ _&_ _special_ _populations_ . Springer,
495–505.

[21] Seungwon Chung and Jung-Woo Son. 2020. Visual perception in autism spectrum
disorder: A review of neuroimaging studies. _Journal_ _of_ _the_ _Korean_ _Academy_ _of_
_Child_ _and_ _Adolescent_ _Psychiatry_ 31, 3, 105.

[22] David F Cihak, Eric J Moore, Rachel E Wright, Don D McMahon, Melinda M
Gibbons, and Cate Smith. 2016. Evaluating augmented reality to complete a



chain task for elementary students with autism. _Journal_ _of_ _Special_ _Education_
_Technology_ 31, 2, 99–108.

[23] Blythe A Corbett and Maryam Abdullah. 2005. Video modeling: Why does it work
for children with autism? _Journal_ _of_ _Early_ _and_ _Intensive_ _Behavior_ _Intervention_ 2,
1, 2.

[24] Camilla Almeida da Silva, António Ramires Fernandes, and Ana Paula Grohmann.
2014. STAR: speech therapy with augmented reality for children with autism
spectrum disorders. In _International_ _Conference_ _on_ _Enterprise_ _Information_ _Systems_ .
Springer, 379–396.

[25] Sarah Dettmer, Richard L Simpson, Brenda Smith Myles, and Jennifer B Ganz.
2000. The use of visual supports to facilitate transitions of students with autism.
_Focus_ _on_ _autism_ _and_ _other_ _developmental_ _disabilities_ 15, 3, 163–169.

[26] Mihaela Dragomir, Andrew Manches, Sue Fletcher-Watson, and Helen Pain.
2018. Facilitating pretend play in autistic children: results from an augmented
reality app evaluation. In _Proceedings_ _of_ _the_ _20th_ _International_ _ACM_ _SIGACCESS_
_Conference_ _on_ _Computers_ _and_ _Accessibility_ . 407–409.

[27] Yao Du, LouAnne Boyd, and Seray Ibrahim. 2018. From Behavioral and Commu­

nication Intervention to Interaction Design: User Perspectives from Clinicians. In
_Proceedings_ _of_ _the_ _20th_ _International_ _ACM_ _SIGACCESS_ _Conference_ _on_ _Computers_
_and_ _Accessibility_ . 198–202.

[28] Carl J Dunst, Carol M Trivette, and Tracy Masiello. 2011. Exploratory inves­

tigation of the efects of interest-based learning on the development of young
children with autism. _Autism_ 15, 3, 295–305.

[29] Lizbeth Escobedo, David H Nguyen, LouAnne Boyd, Sen Hirano, Alejandro
Rangel, Daniel Garcia-Rosas, Monica Tentori, and Gillian Hayes. 2012. MOSOCO:
a mobile assistive tool to support children with autism practicing social skills in
real-life situations. In _Proceedings_ _of_ _the_ _SIGCHI_ _Conference_ _on_ _Human_ _Factors_ _in_
_Computing_ _Systems_ . 2589–2598.

[30] Lizbeth Escobedo, Monica Tentori, Eduardo Quintana, Jesus Favela, and Daniel
Garcia-Rosas. 2014. Using augmented reality to help children with autism stay
focused. _IEEE_ _Pervasive_ _Computing_ 13, 1, 38–46.

[31] Lori Frost and Andy Bondy. 2002. _The_ _picture_ _exchange_ _communication_ _system_
_training_ _manual_ . Pyramid Educational Products.

[32] Jennifer B Ganz, Theresa L Earles-Vollrath, Amy K Heath, Richard I Parker,
Mandy J Rispoli, and Jaime B Duran. 2012. A meta-analysis of single case research
studies on aided augmentative and alternative communication systems with
individuals with autism spectrum disorders. _Journal_ _of_ _autism_ _and_ _developmental_
_disorders_ 42, 1, 60–74.

[33] Barbara C Gartin and Nikki L Murdick. 2005. Idea 2004: The IEP. _Remedial_ _and_
_Special_ _Education_ 26, 6, 327–331.

[34] Martin Guha. 2014. Diagnostic and statistical manual of mental disorders: DSM-5.
_Reference_ _Reviews_ .

[35] Individual Education Plan IEP. 1978. Special educational needs.

[36] Apple Inc. 2022. ARKit - augmented reality. [https://developer.apple.com/](https://developer.apple.com/augmented-reality/arkit)
[augmented-reality/arkit](https://developer.apple.com/augmented-reality/arkit)

[37] Chloe Jennifer Jordan and Catherine L Caldwell-Harris. 2012. Understanding
diferences in neurotypical and autism spectrum special interests through internet
forums. _Intellectual_ _and_ _developmental_ _disabilities_ 50, 5, 391–402.

[38] Kamran Khowaja, Dena Al-Thani, Bilikis Banire, Siti Salwah Salim, and Asadullah
Shah. 2019. Use of augmented reality for social communication skills in children
and adolescents with autism spectrum disorder (ASD): A systematic review. In
_2019_ _IEEE_ _6th_ _International_ _Conference_ _on_ _Engineering_ _Technologies_ _and_ _Applied_
_Sciences_ _(ICETAS)_ . IEEE, 1–7.

[39] Kamran Khowaja, Bilikis Banire, Dena Al-Thani, Mohammed Tahri Sqalli,
Aboubakr Aqle, Asadullah Shah, and Siti Salwah Salim. 2020. Augmented reality
for learning of children and adolescents with autism spectrum disorder (ASD): A
systematic review. _IEEE_ _Access_ 8, 78779–78807.

[40] I Kurniawan et al . 2018. The improvement of autism spectrum disorders on chil­

dren communication ability with PECS method Multimedia Augmented RealityBased. In _Journal_ _of_ _Physics:_ _Conference_ _Series_, Vol. 947. IOP Publishing, 012009.

[41] Aaron Lanou, Lauren Hough, and Elizabeth Powell. 2012. Case studies on using
strengths and interests to address the needs of students with autism spectrum
disorders. _Intervention_ _in_ _School_ _and_ _Clinic_ 47, 3, 175–182.

[42] Gun A Lee, Ungyeon Yang, Yongwan Kim, Dongsik Jo, Ki-Hong Kim, Jae Ha Kim,
and Jin Sung Choi. 2009. Freeze-Set-Go interaction method for handheld mobile
augmented reality environments. In _Proceedings_ _of_ _the_ _16th_ _ACM_ _Symposium_ _on_
_Virtual_ _Reality_ _Software_ _and_ _Technology_ . 143–146.

[43] I-Jui Lee, Chien-Hsu Chen, Chuan-Po Wang, and Chi-Hsuan Chung. 2018. Aug­

mented reality plus concept map technique to teach children with ASD to use
social cues when meeting and greeting. _The_ _Asia-Pacifc_ _Education_ _Researcher_ 27,
3, 227–243.

[44] Roberto E Lopez-Herrejon, Oishi Poddar, Gerardo Herrera, and Javier Sevilla.
2020. Customization support in computer-based technologies for autism: A
systematic mapping study. _International_ _Journal_ _of_ _Human–Computer_ _Interaction_
36, 13, 1273–1290.

[45] Anabela Marto, Henrique A Almeida, and Alexandrino Gonçalves. 2019. Using
augmented reality in patients with autism: A systematic review. In _ECCOMAS_ _The­_
_matic_ _Conference_ _on_ _Computational_ _Vision_ _and_ _Medical_ _Image_ _Processing_ . Springer,


ASSETS ’22, October 23–26, 2022, Athens, Greece


454–463.

[46] MegEvans. 2022. Identity-frst language. [https://autisticadvocacy.org/about­](https://autisticadvocacy.org/about-asan/identity-first-language/)

[asan/identity-frst-language/](https://autisticadvocacy.org/about-asan/identity-first-language/)

[47] Esteban Menéndez and MD Lopez De Luise. 2018. Augmented reality as visual
communication for people with ASD. In _Proc._ _9th_ _Int._ _Conf._ _Soc._ _Inf._ _Technol.(ICSIT)_ .
28–32.

[48] Abhishek Mishra. 2019. Machine learning in the AWS cloud: Add intelligence
to applications with Amazon Sagemaker and Amazon Rekognition. [https:](https://aws.amazon.com/rekognition/)
[//aws.amazon.com/rekognition/](https://aws.amazon.com/rekognition/)

[49] Debora Nunes and Mary Frances Hanline. 2007. Enhancing the alternative
and augmentative communication use of a child with autism through a parentimplemented naturalistic intervention. _International_ _Journal_ _of_ _Disability,_ _Devel­_
_opment_ _and_ _Education_ 54, 2, 177–197.

[50] Shaila M Rao and Brenda Gagie. 2006. Learning through seeing and doing: Visual
supports for children with autism. _Teaching_ _exceptional_ _children_ 38, 6, 26–33.

[51] Christopher Stephen Rayner. 2010. Video-modelling to improve task completion
in a child with autism. _Developmental_ _Neurorehabilitation_ 13, 3, 225–230.

[52] Mikle South, Sally Ozonof, and William M McMahon. 2005. Repetitive behavior
profles in Asperger syndrome and high-functioning autism. _Journal_ _of_ _autism_
_and_ _developmental_ _disorders_ 35, 2, 145–158.



Tooba, et al.


[53] Elizabeth A Steed and Nancy Leech. 2021. Shifting to Remote Learning Dur­

ing COVID-19: Diferences for Early Childhood and Early Childhood Special
Education Teachers. _Early_ _childhood_ _education_ _journal_, 1–10.

[54] Issey Takahashi, Mika Oki, Baptiste Bourreau, Itaru Kitahara, and Kenji Suzuki.
2018. FUTUREGYM: A gymnasium with interactive foor projection for children
with special needs. _International_ _Journal_ _of_ _Child-Computer_ _Interaction_ 15, 37–47.

[55] Unity Technologies. 2022. [https://unity.com/](https://unity.com/)

[56] Catherine Tissot and Roy Evans. 2003. Visual teaching strategies for children
with autism. _Early_ _Child_ _Development_ _and_ _Care_ 173, 4, 425–433.

[57] Laurie A Vismara and Gregory L Lyons. 2007. Using perseverative interests to
elicit joint attention behaviors in young children with autism: Theoretical and
clinical implications for understanding motivation. _Journal_ _of_ _Positive_ _Behavior_
_Interventions_ 9, 4, 214–228.

[58] Cheng Zheng, Caowei Zhang, Xuan Li, Xin Liu, Chuqi Tang, Guanyun Wang,
Cheng Yao, Fan Zhang, Wenjie Xu, and Fangtian Ying. 2017. Toon-chat: a cartoonmasked chat system for children with autism. In _ACM_ _SIGGRAPH_ _2017_ _Posters_ .
1–2.

[59] Cheng Zheng, Caowei Zhang, Xuan Li, Fan Zhang, Bing Li, Chuqi Tang, Cheng
Yao, Ting Zhang, and Fangtian Ying. 2017. KinToon: a kinect facial projector for
communication enhancement for ASD children. In _Adjunct_ _Publication_ _of_ _the_ _30th_
_Annual_ _ACM_ _Symposium_ _on_ _User_ _Interface_ _Software_ _and_ _Technology_ . 201–203.


