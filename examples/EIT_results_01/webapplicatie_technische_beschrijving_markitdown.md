Immissietoets
webapplicatie

Technische beschrijving

F.M. Kleissen

Versie: 0.2
Revisie: ----

1 juli 2025

Immissietoets webapplicatie, Technische beschrijving

Gepubliceerd en gedrukt door:
Deltares
Boussinesqweg 1
2629 HV Delft
Postbus 177
2600 MH Delft
Nederland

telefoon: +31 88 335 82 73
e-mail:
www:

Informatie
Deltares

Verkoop:
telefoon: +31 88 335 81 88
e-mail: Verkoop
www:

Verkoop & Ondersteuning

Ondersteuning:
telefoon: +31 88 335 81 00
e-mail: Ondersteuning
www:

Verkoop & Ondersteuning

Copyright © 2025 Deltares
Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd in enige vorm
door middel van druk,
fotokopie, microfilm of op welke andere wijze dan ook, zonder
voorafgaande schriftelijke toestemming van de uitgever: Deltares.

Inhoudsopgave

Lijst van figuren

Woordenlijst

1 Inleiding

2 Definitie van de maximale toegestane mengzone

3 Near-field berekeningen met Jet3D en Fisher diffusie
.

3.1
.
.
3.2 Pluimverspreiding volgens de zoete toets (Fisher diffusie) .
.
.
3.3

Inleiding .

Jet3D .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

4 Algemene berekeningen
.
4.1 Begrip mengfactor
4.2 Eenvoudige menging .

.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.

.

.

.

.

.

.

.

5 Berekening van stofconcentraties in havens
.
.
5.1 Havens met een gegeven verblijftijd .
5.2 Havenuitwisseling zonder verblijftijd middels SILTHAR .
.
.

.
.
.
5.2.1 Uitwisseling door het getij .
.
5.2.2 Uitwisseling door neervorming .
.
5.2.3 Uitwisseling ten gevolge van dichtheidverschillen .
.
Totale uitwisseling op basis van SILTHAR .
5.2.4
.
.
5.2.5 Concentratieverdeling in de haven .
Schatting van factor γ .
.
.
5.2.6
.
Bepaling van D0 als functie van γ .
.
.
5.2.7
.
Afleiding van concentratieprofiel
5.2.8
.
.
.
Invloed van andere lozingen in de haven .
5.2.9

.
.
.
.
.
.

.
.
.
.
.
.

.
.
.
.
.
.

.
.
.
.

.
.
.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.

.

.

.

.

.

.

.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

6 Getij-uitwisseling

7 Kust en zee

8 Totale menging en eindconcentratie

9 Koudwaterlozingen
Inleiding .
.
.
Thermisch lengteprofiel .

.

.

.

.

.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.
9.1
.
.
9.2
.
.
.
9.3 Bepaling van de dimensies van de mengzone .
.
.
.
9.4 Koudelozingen in havens .
.
9.4.1 Warmtebalansen .
.
.
.
9.4.2 Opzetten van het warmteprofiel in havens .
.
.
.
9.4.3 Recirculatie in andere wateren .
andere wateren met
.
.
.

in
waterbeweging .

9.4.3.1 Recirculatie

.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

ii

iv

1

3

4

7
7
.
8
.
. 10

11
. 11
. 11

12
. 12
. 13
. 13
. 13
. 14
. 15
. 15
. 15
. 16
. 16
. 17

18

20

21

22
. 22
. 22
. 23
. 24
. 24
. 27
. 28

. 29

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.

.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.

.
.

.
.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
complexere
.
.
.
.

.

.

INHOUDSOPGAVE

9.4.3.2 Rivieren en ander lijnvormige wateren met 1 stromingsrichting 29

A Testinstructie

A.1
Inleiding .
.
.
A.2 Stoflozing .
A.3 Temperatuurlozing .
.
A.4

Informatie .

.
.

.
.

.
.

.
.

.

.

.

.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

.
.
.
.

32
. 32
. 32
. 37
. 39

Deltares

iii

Lijst van figuren

Lijst van figuren

2.1 Definitie van de maximaal toegestande mengzone, Mz

3.1 Uitwerking diffusie volgens Fisher .

.

.

.

.

.

.

.

.

5.1 Definitie van geometrie en debieten in een haven .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

5

9

. 15

.

.

.

.

9.2

9.1 Haven debieten en warmte transport bij recirculatie, ΦL is de toegevoegde
warmte .
.
.
.
.
Temperatuurverlaging met en zonder warmteuitwisseling (20 W/m2) en met en
zonder recirculatie. De ∆TL is -8 oC .
.
9.3 Overzicht van de methodiek voor het afleiden van het thermische profiel in
.
.

havens .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.

.
.
Informatieblad
.
.
Informatieblad
Invoerscherm voor de geavanceerde berekening .
.
.

.
A.1
.
A.2
.
A.3
.
A.4 Beslisbloom voor de geavanceerde berekening .
A.5 Drinkwater tabel
.
.
.
.
.
A.6 Concentratie als functie van de afstand tot het lozingspunt
.
A.7 Scherm van de temperatuur tab na selectie .
A.8 Temperatuur invoer en resultaat scherm .
.
.
A.9
A.10 Informatieblad

.
.
.
.
.
.
.
.
Indicatie van het gebied dat door de koudelozing wordt beïnvloed .
.
.

.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.

.
.
.
.
.

.
.
.
.
.

.
.
.
.
.

.
.

.
.

.
.

.
.

.
.

.
.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.
.

. 25

. 27

. 28

. 32
. 33
. 34
. 35
. 36
. 36
. 37
. 38
. 38
. 39

Deltares

iv

Woordenlijst

Cv : warmtecapaciteit water [J.kg−1.oC−1]. 22, 23, 25, 26, 28, 29

Qa : additioneel debiet [m3.s−1]. 24, 26

L : afstand tot de toegestande temperatuurverschil [m]. 24

Qra : benodigde rivierdebiet [m3.s−1]. 23

W : breedte van de rivier [m]. 22–24, 29

H : waterdiepte in de rivier [m]. 23, 24

: benodigd doorstromend oppervlak [m2]. 23

AMTt
Te : evenwichtstemperatuur met de atmosfeer [oC]. 22, 26

∆Tin : inname temperatuurverschil [oC]. 29

Lr : karakteristieke lengte [m]. 29

Tx het thermische lengte profiel, temperatuur [oC] als functie van de afstand x. 22, 23

QL : lozingsdebiet [m3.s−1]. 23–26, 28–30

MF : mengfactor [-]. 25, 26

AMopp : benodigd doorstromend oppervlak [m2]. 24

Q : rivierdebiet [m3.s−1]. 22, 23, 29

Aseg : segmentoppervlak [m2]. 26, 28

Vs : segmentvolume [m3]. 24, 25

T0 : temperatuur bij lozingspunt na volledige mening [oC]. 22

x : afstand stroomafwaarts [m]. 22, 29

MTt

: de benodigde menging om de het temperatuurverschil van het effluent met de
achtergrond terug te brengen tot het toegestane temperatuurverschil [-]. 23, 24

∆TL : temperatuurverschil van het effluent met de achtergrond/verschil tov inname [oC]. iv,

25–27, 29

∆Tn : temperatuurverschil in volume/segment n [oC]. 28

∆T : temperatuurverschil [oC]. 23, 25–28

∆Tt : toegestane temperatuurverschil [oC]. 23

∆TLe : uiteindelijke lozingstemperatuur (verschil met achtergrond) [oC]. 29, 30

Qx : uitwisselingsdebiet [m3.s−1]. 24–26, 28

τ : verblijftijd [s]. 24–26

Φatm : warmteflux met atmosfeer [W/m2]. 26

λ : Warmteuitwisselingscoefficient met de atmosfeer [W.m−2C−1]. 22, 23, 26, 28, 29

Deltares

1 van 39

Woordenlijst

ΦL : warmtevracht lozing [J/s]. iv, 25

ρ : dichtheid water [kg.m3]. 22, 23, 25, 26, 28, 29

T : Water temperatuur [oC]. 22, 26

Deltares

2 van 39

1 Inleiding

De webapplicatie van de immissietoets is een eerste stap in de beoordeling van individuele
lozingen. Lozingen van stoffen (in een effluent) worden beoordeeld volgens het Handboek
Koudelozingen worden beoordeeld volgens het STOWA stappenplan :
Immissietoets.
(https://www.stowa.nl/sites/default/files/assets/PUBLICATIES/Publicaties%202021/STOWA%202021-
30%20koudelozingen%20stappenplan.ppsx). De webapplicatie (www.immissietoets.nl) zal
bij standaard gebruik een consdervatieve aanpak hanteren, hetgeen betekent dat de
effecten door de applicatie worden overschat. Het gevolg is dat de applicatie geen conclusie
zal trekken dat een lozing niet is toegestaan.
Indien volgens de gebruikte berekening niet
aan de criteria kan worden voldaan, dan zal een vervolgonderzoek moeten uitwijzing of een
lozing al dan niet vergunbaar i

De applicatie heeft op dit moment twee werkgebieden, te weten:

⋄ Stoflozingen

⋄ Koudelozing

De stoffen die met een effluent worden geloosd worden als conservatief beschouwd, dus
zonder afbraakprocessen. Voor koudelozing is dat voor het eerste deel (de pluimverspreiding)
ook zo, maar voor dit werkgebied is ook toegevoegd een inschatting van de invloed van een
koudelozing en hierbij wordt een conservatieve schatting van de warmteuitwisseling met de
atmosfeer meegenomen.

Deltares

3 van 39

2 Definitie van de maximale toegestane mengzone

De definitie van het begrip mengzone is gebaseerd op de definitie zoals die de Kaderrichtlijn
water is geintroduceerd. Directive 2008/105/EC Article 4 introduceert mengzones als volgt:

Member States may designate mixing zones adjacent to points of discharge. Concentrations
of one or more substances listed in Part A of Annex I may exceed the relevant EQS within
such mixing zones if they do not affect the compliance of the rest of the body of surface water
with those standards

in dit document de maximale toegestane mengzone
Met het begrip “mengzone” wordt
(MTMZ) bedoeld en de grootte van MTZT is afhankelijk van het watertype en dimensies van
het ontvangende water. Ter verduidelijking is dit niet hetzelfde als de initiele mengzone die
hier is gedefinieerd als dat gebied van pluimverspreiding tot het punt waarbij de de pluim het
Hoe dit punt wordt bepaald hang af van welke
oppervlak (of bodem/kant)
rekentechniek wordt gebruikt (Jet3D versus Fisher). De pluim zelf kan dan worden
gerelateerd aan het gebied tot het punt waarop de menging niet meer toeneemt, dus een
maximale menging heeft bereikt.

raakt.

De berekeningen van de webbapplicatie van de immissietoets bestaat uit een
pluimberekening
algemene
mengberekeningen. Wanneer in het kader van de webapplicatie de pluim de bodem, het
oppervlak of een van de oevers raakt is dit in beginsel de initiele menging.

eenvoudige modelberekeningen)

en meer

(middels

Voor het voorstel van de definitie van de mengzone zijn de oppervlaktewateren in
verschillende typen onderscheiden:

1 Zoet water (saliniteit minder dan 0,5 PSU):

(a) Rivier/kanaal;

(b) Meer;

2 Estuaria en getijrivieren met een restdebiet;

3 Doodlopende kanaalpanden en havens (zonder restdebiet);

4 Aan de oevers van brede estuaria, zeearmen en Waddenzee/ Eems-Dollard met

duidelijk aanwijsbare getijgeulen;

5 Aan de kust van de open zee;

6 Open zee.

In beginsel wordt uitgegaan van een mengzone die een cirkel beslaat met een maximum straal
van 500m. De ligging van het lozingspunt in de cirkel varieert, afhankelijk van de condities.
De algemene vorm, grootte en ligging ten opzichte van het lozingspunt is globaal aangegeven
in Figuur 2.1. Verder zijn er nog een aantal bijzonderheden en extra beperkingen.

Deltares

4 van 39

Definitie van de maximale toegestane mengzone

Figuur 2.1: Definitie van de maximaal toegestande mengzone, Mz

De mengzones zijn als volgt gedefinieerd:

Ad 1: De breedte van de mengzone wordt beperkt tot ¼ van de breedte van het ontvangende
water met een maximum van 1000m. De gehele mengzone bevindt zich stroomafwaarts van
het lozingspunt, omdat de stroming in dit type water slechts 1 richting kent.

Voor meren geldt de huidige definitie breedte mengzone (CIW, 2000):

Hierbij is A is oppervlak, L is lengte en B is breedte van het meer.

Het huidige maximum is 1000m, maar hier wordt voorgesteld om de maximale afstand vanaf
het
lozingspunt voor meren te beperken tot 500m, gelijk aan de eerder gedefinieerde
maximum straal, waardoor de definitie van de mengzone strenger is dan huidige definitie
maar wel consistent is met de definitie in andere watertypen.

Ad 2: Mengzone is hetzelfde gedefinieerd als voor zoet. Echter, de ligging van het
lozingspunt binnen de mengzone varieert, afhankelijk van de verhouding tussen het
vloedvolume en ebvolume. Zonder netto afvoer zijn deze twee gelijk (verhouding =1) en dan
ligt het lozingspunt precies in het centrum van de mengzone (met een maximum straal van
500m). Als het vloedvolume nul is dan is de mengzone precies hetzelfde gedefinieerd als
voor zoet water. De toetsing vindt dan plaats op de rand van de mengzone met de grootste
afstand tot het lozingspunt, hetgeen in praktijk betekent in de richting van de netto afvoer
(zeewaarts).

Ad 3: Aan het eind van een haven kunnen de criteria worden versoepeld, afhankelijk van
de doelstelling van dit waterlichaam. Voor een van te voren vastgesteld deel van de haven
wordt een minimale waterkwaliteit nagestreefd, zoals een minimale zuurstofconcentratie van
3 of 4 mg/l. Tevens mag 25 m van het lozingspunt de ER niet worden overschreden (inclusief
de verhoging van de achtergrond door ophoping van het effluent) om acute problemen te
voorkomen. Voor welk deel dit wordt toegestaan is een relatief arbitraire beslissing, maar
zou gebaseerd kunnen zijn op een maximum percentage van de haven, en/of een maximum
volume en/of maximum oppervlak, gebaseerd op een halve cirkel met een straal van 500m.
Dit deel van de haven geldt vanaf het verste punt in de haven. De mengzone voor een haven
zal nog in detail moeten worden ingevuld.

Ad 4: Een zelfde definitie als voor getijdewateren wordt gehanteerd, maar de dimensies van

Deltares

5 van 39

Definitie van de maximale toegestane mengzone

het ontvangende water waar de mengzone op wordt gebaseerd zijn de dimensies en andere
karakteristieken van de geul bij
Als de lozing tijdens laag water op een
drooggevallen plaat plaatsvindt, dan zullen andere criteria gehanteerd worden. Daar wordt in
de definitie van de mengzone geen uitspraak over gedaan.

laagwater.

Ad 5: Aan de kust geldt een zelfde mengzone als voor estuaria, dus een halve cirkel met een
straal van 500m.

Ad 6: Bij een diepte van 30 m of meer geldt dat de mengzone een straal heeft van 150 m
rondom het lozingspunt en een dikte (diepte) van 30m. Dit vertegenwoordigt een volume
van 2.106 m3. Voor dieptes minder dan 30 m, maar meer dan 5 m geldt dat de straal wordt
afgeleid van de diepte en het toegestane volume. Voor bijvoorbeeld 10 m diepte zou dit
een straal van 250 m betekenen. Bij minder dan 5 m wordt de maximale straal van 500 m
gehanteerd. Dit geldt overigens niet als het een lokale diepte betreft, zoals een (getij)geul.

De webapplicatie berekend op basis van de de definitie van het ontvangende water (het
watertype) de maximaal toeghestane mengzone waarop getoetst wordt. Hierbij wordt geen
rekening gehouden met het eventueel overlappen met een beschermd gebied.

Voor acute toxiciteit is een mengzone afgeleid die maximale 25 m gehanteerd is voor een
ontvangende water waarvoor een maximale mengzone geld van 1000m. De MAC afstand
wordt evenredig kleiner naarmate de mengzone kleiner is, dus 0.25 * Mz . De concentratie
wordt getoetst aan de toegestane concentratie, de MAC waarde (Maximum Aanvaardbare
Concentratie). Voor de bestaande zoete toets wordt voor het ER niveau (Ernstig Risico)
wordt een maximale afstand van 25 m gehanteerd (0.25 * Bwaterlichaam ≤ 25 m). Het ligt
dan voor de hand om voor zoute wateren in eerste instantie ook deze verhouding 0.25 * B
waterlichaam met een maximum van 25 m als mengzone te hanteren.

Deze keuze kan in praktijk betekenen dat voor kleinere mengzones dit nagenoeg gelijkwaardig
is aan het hanteren van de MAC als concentratielimiet in het effluent. Bijvoorbeeld, een
lozing op een smal watersysteem, bijvoorbeeld 10 m, resulteert in een lengte voor de MAC-
mengzone van 2,5 m. Over een dergelijke afstand treden in het algemeen slechts kleine
verdunningsfactoren op.

Deltares

6 van 39

3 Near-field berekeningen met Jet3D en Fisher diffusie

3.1

Inleiding

Er zijn in de applicatie twee soorten pluimberekeningen beschikbaar. De eerste is de
pluimberekening, die ook al wordt toegepast binnen het kader van de zoete toets (IJff
(2000)). Deze berekening houdt echter geen rekening met dichtheidverschillen tussen
effluent en ontvangende water of met verticale dichtheidsgradiënten in het ontvangende
water. Deze kunnen het verspreidingsgedrag van de pluim significant beïnvloeden. Vandaar
dat ook een pluimverspreidingsmodel, dat met dergelijke dichtheidverschillen rekening kan
houden, in het instrument is opgenomen. Dit is het model Jet3D dat door het toenmalige
Waterloopkundig Laboratorium is ontwikkeld (Delvigne (1979)) en wordt toegepast wanneer
het dichtheidsverschil tussen lozing en ontvangende water groter is dan 1 kg/m3.

Voor beide pluimberekeningen is de maximale menging begrensd door de hoeveelheid water
dat beschikbaar is voor menging. Dit is bepaald door de eenvoudige menging waarbij een
massabalans de maximale menging uitrekent op basis van het beschikbare debiet
(rivierafvoer) en lozingsdebiet (zie Hoofdstuk 4.2).

De lozing kan plaatsvinden op verschillende posities in het ontvangende water. Om het
gebruik van de applicatie zo eenvoudig mogelijk te houden is gekozen om die positie in het
oppervlaktewater te beperken tot:

• Positie van de lozing = horizontaal

1 = midden

2 = oever

• Positie van de lozing = vertikaal

1 = top (oppervlakte)

2 = midden (halverwege de diepte)

3 = bodem.

Jet3D kan met optie 3 (lozing bij de bodem) rekenen, CIW-Fisher gaat er van uit dat resultaat
van pluim aan top (1) gelijk is aan resultaat aan bodem (3)
is immers geen
dichtheidsverschil)

(er

De pluimberekening (zowel Jet3D als Fisher en de combinatie van beide) loopt door tot de
toetsafstand (de berekende m_mixingzone_ya_length, afhankelijk van het type en dimensies
van het ontvangende water) is bereikt. Op die toetsafstand wordt de menging van de pluim
gebruikt in combinatie met de achtergrondmenging.

In havens is het zo dat een pluim berekening niet meer verder kan als de pluim de haven
uitgaat en in een langsstromend water terecht komt. De hydrodynamica gaat dan significant
afwijken van het water waarin wordt geloosd en dan is de pluimberekening niet meer relevant.

Vandaar ook dat in havens de m_mixingzone_ya_length word gelimiteerd tot de afstand van
het lozingspunt tot de haven mond (w_distance_effluent_to_harbour_entrance). Deze laatste
afstand is gekoppeld aan het haven segment (dus 1 waarde voor elk segment in de haven).
Dit afkapmechanisme van de mixingzonelength vindt plaats voor zowel havens met als zonder
tracer.

Deltares

7 van 39

Near-field berekeningen met Jet3D en Fisher diffusie

3.2 Pluimverspreiding volgens de zoete toets (Fisher diffusie)

De beschrijving van de berekeningen zijn in de documentatie van de zoete toets opgenomen
(IJff (2000)). Bij deze berekening wordt een onderscheid gemaakt in:

⋄ Een situatie waarbij in eerste instantie sprake is van een uitstroming in de vorm van een

jet die vervolgens overgaat in een tweedimensionale pluim;

⋄ Een situatie waarbij de uitstroming direct plaatsvindt

in de vorm van een

driedimensionale pluim die daarna overgaat in een tweedimensionale pluim.

Welke van deze twee condities gelden is afhankelijk van de verhouding tussen de
uitstroomsnelheid en de stroomsnelheid van het ontvangende water. De berekening is
uitgewerkt volgens onderstaande figuur 3.1.

Deltares

8 van 39

Near-field berekeningen met Jet3D en Fisher diffusie

Figuur 3.1: Uitwerking diffusie volgens Fisher

Dit figuur komt uit IJff (2000)

Deltares

9 van 39

Near-field berekeningen met Jet3D en Fisher diffusie

3.3

Jet3D

Voor situaties waar dichtheidsverschillen een rol spelen in de verspreiding van de pluim is
het pluimverspreidingsmodel Jet3D beschikbaar (Delvigne (1979)). Dit model is in de jaren
toenmalig Waterloopkundig Laboratorium ontwikkeld en beschrijft de drie-
70 door het
dimensionale verspreiding van een ronde pluim met een dichtheid die kan afwijken van het
ontvangende water. Het ontvangende water kan een niet-uniform verticaal dichtheidprofiel
en een niet-uniform snelheidsprofiel hebben.

is nodig in situaties die niet door de ‘zoete’ pluimberekening kunnen worden
Dit model
gesimuleerd vanwege optredende dichtheidsverschillen.
Zonder de significante initiele
dichtheidsverschillen wordt de Fisher pluimverspreiding gebruikt zodat de resultaten voor
dergelijke situaties (rivieren en kanalen met stroming) overeenkomen met de oorspronkelijk
berekeningen met het spreadsheet dat oorspronkelijk ontwikkeld was ten behoeve van de
immissietoets (IJff (2000)).

Het model beschrijft de pluim vanaf het moment dat het effluent de pijp verlaat. De
berekeningen stoppen wanneer de rand van de mengzone is bereikt of wanneer de pluim de
bodem of wateroppervlak of een van beide oevers raakt. In de applicatie stopt de berekening
ook wanneer de diameter van de pluim groter wordt dan de diepte of de breedte van het
ontvangende water.

Als de Jet3D berekening stopt voordat de rand van de mengzone is bereikt worden de
gegevens overgenomen door de 2D berekening die ook in de zoete pluimberekening is
opgenomen. Hierbij wordt ervoor gezorgd dat er geen discontinuïteit optreedt in de
verdunning van de pluim door de diepte die in de 2D berekening wordt gebruikt aan te
passen en in de verdere berekening constant te houden.

Er is nog wel een opmerking te maken ten aanzien van een gestratificeerd ontvangend water.
Wanneer het ontvangende water is gestratificeerd met een spronglaag (dus niet een
linear geinterpoleerde verticale dichtheidgradient) dan wordt de jet in een waterlaag
geloosd met de dikte van de laag die qua dichtheid het laagste verschil geeft met de
dichtheid van het geloosde effluent. Dan wordt dus kunstmatig de diepte aangepast.(Dit
is een conservatieve aanname). Dit heeft overigens geen effect op de verhoging van de
achtergrond concentratie (ter hoogte van het lozingspunt).

Deltares

10 van 39

4 Algemene berekeningen

4.1 Begrip mengfactor

In de rekentechnieken die in de applicatie zijn opgenomen worden mengfactoren berekend.
De mengfactor die voor het effluent kan worden afgeleid is het resultaat van het samenvloeien
van verschillende stromingen en is gedefinieerd vanuit een eenvoudige massabalans.

De mengfactor is berekend door:

Mf =

Qr + Qa + Ql
Ql

(4.1)

Waarbij Qr is het rivierdebiet, Qa ander debiet door het watersysteem en Ql het lozingsdebiet
(allen in m3/s).

Deze mengfactor kan ook worden afgeleid vanuit de de concentraties van het effluent en de
achtergrond en het bereikte concentratieverschil:

Mf =

Cl − Ca
∆C

(4.2)

Waarbij Cl en Ca de concentratieverandering na menging met een mengfactor Mf . Vanuit
de in de berekende mengfactoren wordt vervolgens de concentratie na menging berekend.
In de applicatie van de immissietoets wordt gebruik gemaakt van een algemene menging
en een pluim verspreiding. De berekening van de algemene menging is afhankelijk van het
watertype. Voor de pluimberekening worden twee modellen toegepast, te weten het Jet3D
model, wanneer er een significant dichtheidsverschil is tussen effluent en ontvangende water,
en het Fisher model wanneer dat niet zo is. De eindconcentratie op de toetsafstand is een
combinatie van de algemene menging en de pluimmenging (zie hoofdstuk 8)

4.2 Eenvoudige menging

De berekening is beschikbaar voor watersystemen die goed gemengd zijn waardoor er een
verhoging van de achtergrondconcentratie (∆C) ten gevolge van de lozing optreedt. Dit geld
voor beken, kanalen,
Deze massabalans wordt ook toegepast op andere
zoals getijdewateren en meren om de verhoging van de
oppervlaktge wateren,
achtergrondconcentratie te berekenen, volgens vergelijking 4.1. Deze menging wordt dan
gecombineerd met het resultaat van de pluimmenging.

rivieren.

Deltares

11 van 39

5 Berekening van stofconcentraties in havens

Voor de berekening van pluim concentraties in havens zijn twee methodes toegepast. De
eerste is door gebruikt te maken van verblijftijden die uit modelberekeningen zijn afgeleid (de
zogenaamde tracer berekeningen). De tweede is om de uitwisseling tussen de haven en het
voorbijstromende water te berekenen en daaruit de concentraties ten gevolge van een lozing
in de haven af te leiden.

5.1 Havens met een gegeven verblijftijd

Deze methode om de achtergrondconcentratieverhoging ten gevolge van een lozing in een
haven te bepalen maakt gebruik van de resultaten van modelsimulaties van tracers. Deze
methode wordt ook voor andere wateren gebruikt en is gebaseerd op tracer berekenening
met het achterliggende hydrodynamische model (zoals Delft3D of SOBEK).

Uitgangspunt is een haven met een tracerconcentratie van 1 en een concentratie van 0 in
het hoofdwatersysteem, waarna het model de afname van de tracer concentratie ten gevolge
van de uitwisseling tussen de haven en het hoofdwatersysteem berekent. De haven wordt
vervolgens in een aantal deelgebieden opgedeeld. De afnemende concentratie als functie van
de tijd in een deelgebied bepaalt de verversingstijd voor dat deelgebied. Deze verversingstijd
wordt dan gebruikt om de verhoging van de achtergrondconcentratie in een deelgebied ten
gevolge van een effluent lozing in dat gebied te berekenen.

Om de berekening binnen de webapplicatie te vereenvoudigen en toepasbaar te maken wordt
aangenomen:

⋄ de concentratie in de gedefinieerde deelgebieden neemt exponentieel af (deze
aanname is equivalent met de aanname dat de deelgebieden volledig gemengd zijn);

⋄ de te beoordelen lozing beïnvloedt de hydrodynamica in de haven niet significant.

Bij een exponentiële aanname geldt voor elk segment (deelgebied) dat de verversingstijd kan
worden uitgedrukt als T = V /Q, met Q het ‘verversingsdebiet’ en V het volume van het
deelgebied. Als een effluent, bestaand uit debiet Ql en concentratie Cl, in een deelgebied
loost, dan kan via een massabalans de evenwichtsconcentratie in dat deelgebied worden
berekend.

Als een mogelijk andere debiet (Qa) die niet in de hydrodynamische modelberekeningen is
meegenomen, omdat het bijvoorbeeld andere industriële lozingen betreft die relatief klein zijn,
dan kan deze lozing wel in de massabalans worden meegenomen.

Dan wordt aangenomen wordt dat deze andere lozing zich bovenstrooms van de
lozingslocatie of in hetzelfde subgebied bevindt (benedenstrooms van de lozing heeft het
geen direct effect op de verversingstijd ter hoogte van de effluentlozing). Dit wordt in de
aanpak met de SILTHAR berekeningen (zoals op dit moment ook in de webapplicatie is
opgenomen) ook aangenomen. Als vervolgens wordt aangenomen dat de concentratie van
deze andere lozing 0 is en in het deelgebied volledig is gemengd dan volgt uit de
massabalans:

(cid:18) V
T

(cid:19)

+ Ql + Qa

Ql

Cl
C

=

Deltares

(5.1)

12 van 39

Berekening van stofconcentraties in havens

Deze beschrijving geldt indien de achtergrondconcentratie nul is. Wanneer deze groter is dan
0, dan wordt in de berekeningen niet de effluentconcentratie gebruikt, maar het verschil in
concentratie tussen het effluent en het ontvangende water.

Deze verversingsberekeningen worden alleen gebruikt als in de onderliggende database de
afgeleide gegevens (verversingstijden) voor de betreffende havensegmenten zijn opgeslagen.
Als deze gegevens niet aanwezig zijn, dan wordt de SILTHAR methode toegepast.

De verhoging van de achtergrondconcentratie in het deelgebied waar wordt geloosd wordt
vervolgens gecombineerd met de pluim/jet berekening (paragraaf 4.1) waarna de concentratie
op de toetsafstand wordt afgeleid.

5.2 Havenuitwisseling zonder verblijftijd middels SILTHAR

Havens en doodlopende kanaalpanden hebben geen zoetwaterafvoer die het water in de
haven kan verversen. Effluent dat in havens wordt geloosd kan alleen maar verdunnen als er
een transport is vanuit de haven naar de uitgang van de haven. Dit transport kan bestaan uit
diffusie/dispersie in combinatie met uitwisseling van water in de haven met het water
daarbuiten. De uitwisseling zorgt voor de verversing in de haven (en een verlaging van de
verblijftijd) terwijl de diffusie/dispersie processen de concentratiegradiënten in de haven
bepalen. In de webapplicatie zijn twee berekeningen opgenomen om menging in havens en
de uitwisseling met het hoofdwatersysteem te beschrijven.

De in dit hoofdstuk 5.2 gepresenteerde methode is gebaseerd op de uitwisselingsprocessen
die zijn afgeleid uit het SILTHAR model (Eysink (2004)). Ook in MAMPEC worden dezelfde
formuleringen gebruikt (Van Hattum et al. (2002)). Een tweede methode die in paragraaf 5 is
uitgewerkt
is gebruikt om de
verversingssnelheid in vooraf gedefinieerde (haven)segmenten te bepalen.

is afgeleid uit modelresultaten waarbij een tracer

Voor uitwisseling tussen het water in de haven en het voor de ingang van de haven
langsstromende (getijde)rivierwater zijn drie processen bepalend:

⋄ Uitwisseling door het getij;

⋄ Uitwisseling door neervorming;

⋄ Uitwisseling ten gevolge van dichtheidsverschillen tussen het water in en buiten de

haven.

5.2.1 Uitwisseling door het getij

Het uitwisselingsvolume ten gevolge van het getij
bepaald door de verticale getijslag (Hg) en het oppervlak van de haven (Bh × Lh):

is het zogenaamde getijvolume en is

Vt = Hg × Bh × Lh

(5.2)

5.2.2 Uitwisseling door neervorming

Door stroming langs de ingang van de haven of doodlopend kanaal ontstaat neervorming
die wateruitwisseling tussen de haven en het langsstromende water genereert. Dit proces is
beschreven door (Van de Graaf en Reinalda (1977)):

Qh = f1 × h × b × u0 − f2 × Qt

Deltares

(5.3)

13 van 39

Berekening van stofconcentraties in havens

met h en b de hoogte en breedte van de haveningang, u0 de stroomsnelheid voor de ingang
en Qt het debiet van het binnenstromende water bij het vullen van de haven tijdens de vloed.
De twee coëfficiënten f1 en f2 zijn in de orde van respectievelijk 0,01-0,03 en 0,1-0,25. Dit
proces kan worden geïntegreerd over een getij en dat levert (Eysink (2004):

vh = f1 × h0 × b ×

u0,max
π

− f2 × Vt

(5.4)

waarbij h0 de diepte van de haveningang ten opzichte van gemiddelde zeeniveau, T de
getijperiode en u0,max de maximale snelheid van de getijrivier voor de haveningang
(w_flow_velocity_maximum). Voor de coëfficiënten f1 en f2 zijn in de applicatie waarden
aangenomen van respectievelijk 0,02 en 0,2.

5.2.3 Uitwisseling ten gevolge van dichtheidverschillen

Wanneer het water in de haven een lagere dichtheid heeft dan buiten de haven zal het water
buiten de haven over de bodem de haven binnendringen en zo een wateruitwisseling
genereren. Als het water buiten de haven een constante dichtheid heeft, dan zal dit een
relatief kortstondig proces zijn totdat de haven en het
langsstromende water dezelfde
dichtheid hebben. Dit proces treedt dus alleen maar permanent op wanneer in de haven een
zoetwaterafvoer plaatsvindt of als het langsstromende water varieert in dichtheid en dit kan
voor getijdewateren het geval zijn. De uitwisseling wordt dan gedreven door de variatie in de
dichtheid van het langsstromende water tijdens een getij. Dit kan komen door zout en
temperatuurverschillen. Het proces is in de SILTHAR documentatie uitvoerig beschreven
(Eysink, 2004). Het uitwisselende volume per getij is:

Vd = Vd0 ×

f4
f4,max

− f5 × Vt

waarbij:

Vd0 = f4,max × h0 × b ×

(cid:18)∆ρmax
ρ

(cid:19) 1

2

× g × h0

× T

(5.5)

(5.6)

∆ρmax is het karakteristieke dichtheidsverschil dat om praktische redenen de helft is van de
dichtheidvariatie binnen een getij van het langsstromende water. De gemiddelde dichtheid
van het water is ρ. In deze beschrijving zijn 3 coëfficiënten opgenomen, f4, f4,max en f5. De
coefficient f5 is afhankelijk van de verhouding V d0
tussen de
Vt
dichtheidsstroming en de getijstroom. Naarmate het faseverschil kleiner is neemt de invloed
van de getijstroom toe en is f5 groter. Ook neemt f5 toe bij een grotere V d0
. Volgens Eysink
Vt
(2004) ligt f5 tussen 0,1 en 1. Voor een conservatieve benadering is in de immissietoets een
waarde 1 aangenomen. Dit heeft tot gevolg dat het uitwisselend volume eerder onderschat
wordt dan overschat, waardoor de concentratieverhoging eerder overschat wordt dan
onderschat.

faseverschil

en het

Voor f4,max is door Eysink (2004) een waarde van 0,125 als gemiddelde schatting gegeven
en ook blijkt uit de diverse case studies die zijn uitgevoerd dat de ratio f 4/f 4, max altijd
tussen 1,0 en 0,985 ligt. Een conservatieve aanname is dat f4 = 0, 985f4,max.

Deltares

14 van 39

Berekening van stofconcentraties in havens

5.2.4

Totale uitwisseling op basis van SILTHAR

Nadat de verschillende uitwisselingsvolumes zijn berekent kan het totale uitwisselingsdebiet
worden berekend:

Ve = Vt + Vh + Vd + Vef f

(5.7)

Vef f vertegenwoordigt extra uitwisseling door doorstromende debieten in de haven die de
verblijftijd nog verder reduceren.

5.2.5 Concentratieverdeling in de haven

Het uitwisselende debiet dat van het volume is afgeleid resulteert in een verlaging van de
verblijftijd. Als de haven gezien wordt als een 1-dimensionaal bassin, dan volgt uit de
verblijftijd en het effluentdebiet meteen een gemiddelde concentratie. Echter kan worden
aangetoond dat dit een onderschatting kan opleveren van de concentratie omdat het effect
van de uitwisseling in de haven niet overal gelijk is, maar bij de havenmond groter dan aan
het eind van de haven. Dit kan worden beschreven door gebruik te maken van een
plaatsafhankelijke effectieve dispersiecoëfficiënt en hier een analytische oplossing voor het
concentratieprofiel van af te leiden.

De hier gepresenteerde beschouwing is die voor een haven die een uitwisselingsdebiet Q
met de omgeving heeft, waarin achter in de haven een continue lozing W (kg/s) van een
terwijl de achtergrondconcentratie buiten de
conservatieve stof plaatsvindt (Figuur 5.1),
haven 0 is. Als we deze situatie zouden weergeven als een eenvoudig boxmodel, met een
doorstroming Q dan is de resulterende concentratie .
In werkelijkheid is te verwachten dat
de verversing in de haven minder efficiënt is waardoor de gemiddelde concentratie C hoger
uitvalt dan W/Q. De effectiviteit is uit te drukken door een factor γ . Voor een goed
gemengde haven (boxmodel) is γ gelijk aan 1,
terwijl de verwachting is dat deze in
werkelijkheid minder dan 1 is.

Figuur 5.1: Definitie van geometrie en debieten in een haven

5.2.6 Schatting van factor γ

De factor γ is slechts in een enkel geval bekend uit numerieke experimenten. Het is de
bedoeling dat in de toekomst aanvullende numerieke experimenten zullen plaatsvinden. Op
dit moment is de waarde van γ niet meer dan een ruwe schatting.

Deltares

15 van 39

Berekening van stofconcentraties in havens

De hypothese is dat de factor γ afhangt van de lengte-breedteverhouding van de haven; hoe
langer een haven, hoe minder efficiënt het uitwisselingsdebiet en hoe lager de waarde van γ.
Daarnaast speelt overduidelijk de aanwezigheid van dichtheidsstromen een rol. Uit de
beschikbare numerieke experimenten is af
te leiden dat een toename van het
uitwisselingsdebiet door dichtheidsstroming met een factor van ruim 2 leidt tot een toename
van γ met ongeveer een factor 2.

Voor de volgende analyse is aangenomen dat:

⋄ γ hangt lineair af van Lh/Bh;

⋄ γ hangt lineair af Ve/(Ve − Vd) (verder aangeduid als η);

De lineaire afhankelijkheden zijn te beschouwen als een eerste schatting. Naarmate meer
informatie beschikbaar komt kunnen deze, indien nodig, worden aangepast.

Uit de beperkte data volgt een eerste kwantificering van de afhankelijkheden:

γ = 1 + (−0.237 + 0.0287 × η)

Lh
Bh

(0, 01 ≤ γ ≤ 1)

(5.8)

De ondergrens van γ is bepaald door een willekeurige waarde om te voorkomen dat de
dispersiecoëfficiënt nul kan worden. Een alternatief zou kunnen zijn om gebruik te maken
van een functie die asymptotisch naar nul gaat als Lh/Bh ook naar oneindig gaat. Dit
vereist echter meerdere parameters waarvoor de onderbouwing op dit moment ontbreekt.
Ook de relatie tussen de lengte/breedte verhouding en γ is speculatief te noemen.

5.2.7 Bepaling van D0 als functie van γ

Het boven geschetste diffusieprobleem kan op basis van de vergelijking van Fick als volgt
analytisch worden uitgedrukt:

W = −D(x) · Ah ·

dC
dx

(5.9)

waarbij Ah de (constant veronderstelde) dwarsdoorsnede voorstelt. Na substitutie van ξ =
x/L en D(ξ) = ξD0 dajn volgt de oplossing:

C(ξ) = −C0 · ln(ξ) = −

W · Lh
D0 · Ah

ln(ξ)

(5.10)

De over de haven gemiddelde concentratie is C0. Door substitutie van γ = W/Q/C0, volgt
dan een schatting van D0 als functie van γ:

D0 = γ

Qe · Lh
Ah

5.2.8 Afleiding van concentratieprofiel

(5.11)

Uit de vergelijking van Fick, gebruik makend van de lineaire afhankelijkheid van de
dispersiecoëfficiënt in de haven volgt voor een lozing op positie x in de haven (x is de afstand
vanaf het eind van de haven, zie Figuur 5.1, de concentratie als functie van de afstand x

Deltares

16 van 39

Berekening van stofconcentraties in havens

tussen het lozingspunt en de haveningang (x > xl waarbij xl de locatie van het lozingspunt
is):

dC(x − xl)
dx

=

+Ql(C(x − xl) − Cl)
x − xl
Lh

D0

Ah

(5.12)

Cl is de concentratie van de stof in het effluent. Verder is aangenomen dat het debiet van de
lozing klein is ten opzichte van het uitwisselingsdebiet zodat het advectieve transport dat door
de lozing wordt gegenereerd ook verwaarloosbaar is. De dwarsdoorsnede van de haven A is
constant verondersteld.

De oplossing van deze vergelijking is vervolgens:

C(x) = Cl − Kl(x − xl)K2

(5.13)

met:

en

Kl =

(Cl − Ca)
LK2

K2 =

Ql
(cid:19)

(cid:18) A
L

D0

Ca is de achtergrondconcentratie. Deze vergelijking geldt voor x ≥ xl (xl is de positie van
het lozingspunt). Voor x < xl is de concentratie niet meer afhankelijk van x.

5.2.9

Invloed van andere lozingen in de haven

Het komt regelmatig voor dat in een haven ook andere effluenten aanwezig zijn die de
verblijftijd in de haven beïnvloeden. Gezien de mogelijke lange verblijftijden in havens
kunnen de extra debieten een significante invloed hebben op de verhoging van de
concentratie ten gevolge van de lozing. Om dit in te schatting is de mogelijkheid aanwezig
om die extra debieten in de haven mee te nemen, aannemende dat de concentratie van de
stof gelijk is aan de achtergrond. Dit extra debiet geeft dus het effect van een extra
doorspoeling aan en leidt niet tot concentratieverhogingen. Het is bij de implementatie ook
aangenomen dat dit extra debiet aan de kop van de haven geloosd wordt. De berekening
van de menging maakt gebruik van de dezelfde afleiding als voor de lozing zelf. Beide
mengfactoren worden vervolgens gecombineerd hetgeen leidt
tot een longitudinaal
concentratieprofiel in de haven. Deze combinatie is afgeleid door een massabalans :

(cid:18) Ql + Qa
Ml(x)
(cid:18) Qa

C(x) =

(cid:19)

(Cl(x) − Ca)

(cid:19) + Ca

+

Ql
Ml(x)

(5.14)

Ma(x)

De verhoging van de achtergrondconcentratie ter hoogte van het lozingspunt wordt vervolgens
gecombineerd met de pluim/jet berekening (paragraaf 3.3) waarna de concentratie op de
toetsafstand wordt afgeleid.

Deltares

17 van 39

6 Getij-uitwisseling

Bij een lozing op een getijdewater zal accumulatie plaatsvinden ten gevolge van de eb- en
vloedbeweging omdat geloosd effluent (Ql) na verloop van tijd weer langs het lozingspunt
stroomt. De mate van accumulatie hangt af van het getij en de netto rivier afvoer (Qan). Hoe
groter de netto afvoer ten opzichte van de eb (Qae) en vloed (Qav) beweging, des te kleiner
de accumulatie. Benodigde gegevens zijn:

⋄ Lozingsdebiet, Ql [m3/s];

⋄ Netto afvoer, Qan [m3/s];

⋄ Gemiddeld eb- en vloeddebiet, Qae en Qav - Qan [m3/s];

⋄ Breedte van het ontvangende water, Bw [m]; 6

⋄ Diepte van het ontvangende water, Dw [m];

⋄ Benedenstroomse limitatie eb afstand, M axLends [m].

The duration of the flood Tv[s]:

Tv = TL ·

(Qae − Qan)
(Qav + Qae)

where TL (44712 seconden) is de lengte van een dubbeldaags getij (12:25u).

Afgelegde afstand tijdens de vloed fase (in m):

Lv =

Qav
(Bw × Dw)

Tv

Afgelegde afstand tijdens de eb fase (in m):

Le =

Qae
(Bw × Dw)

(T deSec − Tv)

(6.1)

(6.2)

(6.3)

Het aantal getijdes voor het bereiken van steady state accumulatie Ng is berekend door:

Ng =

Lv
(Le − Lv)

]

(6.4)

Dit wordt naar boven afgerond op een geheel getal. Wanneer de eb en vloed afstand even
groot zijn kan er geen menging worden uitgerekend.

Wanneer er een limiterende afstand Lmax is (bijvoorbeeld door een dwarstroming waardoor
het water volledig wordt afgevoerd en niet terug kan komen) wordt het aantal getijdes
aangepast door:

N Rg = [

Lmax
(Le − Lv)

]

NRg wordt op een geheel getal afgerond met een minimum van 1.

Deltares

(6.5)

18 van 39

Per getijslag wordt iteratief een cumulatieve menging berekend, uitgaande van de menging
tijdens 1 getij. De menging tijdens de vloed (Mv) en eb (Me) zijn resp:

Getij-uitwisseling

en

Mv =

Qav
4 + Ql
Ql

Me =

Qae
4 + Ql
Ql

(6.6)

(6.7)

De factor 4 is een veiligheidsfactor die is ingevoerd omdat er niet vanuit gegaan kan worden
dat het effluent over de gehele breedte is gemengd. Er is hier dus aangenomen dat een
kwart van het water beschikbaar is voor de menging. Deze factor 4 is ook consistent met de
maximale breedte van de mengzone.

Voor het eerste volledige getij geeft dit een totale menging (M1e):

1
M1

=

1
Mv

+

1
Me

−

1
(Me × Mv)

Loop over alle getijslagen (n = 2 tot Ng) voor uiteindelijke menging:

Vloedmenging:

1
Mnv

=

1
M(n−1)

+

1
Mv

−

1
(M(n−1)e × Mv)

Ebmenging:

1
Mn

=

1
Mnv

+

1
Me

−

1
(Mnv × Me)

(6.8)

(6.9)

(6.10)

Als de noemer 0 is dan wordt de ebmenging gebruikt omdat de berekening niet kan worden
uitgevoerd. Als de vloedmengfactor 1 is dan betekent dat er geen vloeddebiet is een ook
dan wordt de ebmenging gebruikt om te voorkomen dat er geen menging meer is. Zodra
de vloedmenging groter is dan 1 is er alleen een vloed debiet en kunnen de berekeningen
worden uitgevoerd.

Deltares

19 van 39

7 Kust en zee

Kustwateren en open zee verschillen van de in de vorige hoofdstukken genoemde wateren in
die zin dat een berekening van de verhoging van de concentratie alleen goed kan worden
geschat door gebruik te maken van geavanceerde modellen. Er kan echter wel een
bovengrens worden aangegeven voor de concentratie in de mengzone. Deze is gebaseerd
op een menging van het effluent met het volume van de mengzone met een verblijftijd die is
afgeleid van het door de mengzone stromende debiet. Voor dit debiet wordt de restsnelheid
De
gebruikt omdat die de netto verversing van het mengvolume vertegenwoordigt.
concentratie die hieruit is af te leiden vertegenwoordigt de maximale verhoging van de
achtergrond.

De verdunning van het effluent in de mengzone is op basis van een eenvoudige massabalans:

Mk =

ur × 2 × Rmengzone × Hmengzone
Ql

(7.1)

Waarbij ur de reststroomsnelheid is, Rmengzone de straal van de mengzone en Hmengzone
de dikte/diepte van de mengzone (zie Hoofdstuk 3). Dit geldt voor een lozing op open zee.
Voor een lozing aan de kust is de maximale toegestane mengzone begrenst door de kustlijn
waardoor de massabalans niet 2 × R maar alleen R bevat. De menging Mk bepaalt de
verhoging van de achtergrond in de mengzone. Hierna volgt nog een berekening van de
concentratie in een pluim (of
jet) waaruit de gecombineerde concentratie van
achtergrondverhoging en pluim (of jet) volgt.

Deltares

20 van 39

8 Totale menging en eindconcentratie

Voor elk type water vormt de eindconcentratie het resultaat van een pluimberekening of een
berekening van de algemene menging van het effluent met achtergrond die al of niet gevolgd
wordt door een pluimberekening. De algemene mengfactor Ma is gedefinieerd als:

Ma = 1 +

Qa
Ql

=

Ql + Qa
Ql

met:

⋄ Lozingsdebiet, Ql [m3/s];

⋄ Afvoer, Qa [m3/s];

(8.1)

Wanneer dit reeds gemengde water nog een keer gemengd wordt met het effluent met
mengfactor Mp (bijvoorbeeld door een pluimberekening), dan volgt uit een massabalans dat
de totale mengfactor Mtot gedefinieerd wordt door:

1
Mtot

=

1
Ma

+

1
Mp

−

1
Ma × Mp

(8.2)

De laatste term is onbelangrijk bij vrij grote mengfactoren (groter dan ....) maar is wel
totale menging op deze wijze is
significant bij
afgeleid,
ten opzichte van de
achtergrondconcentratie (Cw):

volgt de verhoging van de concentratie ∆Ct

lage mengfactoren. Wanneer eenmaal

∆Ct =

Cl − Cw
Mtot

met:

⋄ Concentratie effluent Cl [g/l];

⋄ Achtergrond concentratie Cw [g/l];

⋄ Verhoging concentratie (tov Cw)na twee mengvormen, ∆Ct [g/l];

achtergrondconcentratie (Cw):

∆Ct =

Cl − Cw
Mtot

(8.3)

(8.4)

Deltares

21 van 39

9 Koudwaterlozingen

9.1

Inleiding

Voor Koudelozingen is een apart tabblad opgezet. De basis vergelijkingen voor menging zijn
dezelfde als voor stoflozingen.

Dit betekent dat de pluimmenging met het oppervlaktewater hetzelfde is. Het kader voor de
beoordeling is echter wel anders. Dit blijkt voornamelijk uit de beslisboom die wordt
gehanteerd en de gegevens die nodig zijn om tot een beoordeling te komen. Veel velden
zullen door de gebruiker moeten worden ingevuld omdat hier geen informatie aanwezig is in
de database van de immissietoets. Het thermische lengteprofiel wordt vervolgens ook
getoond als tweede deel van de verdunningsgrafiek.

Voor de verdere verspreiding van koudelozingen (verder dan de pluim berekeningen toelaat)
wordt de warmte-uitwisseling met de atmosfeer belangrijk. Vandaar dat er een warmtebalans
is toegevoegd om daar een inschatting van te geven. Hieruit volgt dan een thermisch
lenteprofiel. Hiervoor wordt gebruikt gemaakt van het Nationaal Water Model (NWM), waarin
een tracer is meegenomen (vergelijkbaar met de stoflozingen) waarin uitwisseling met de
atmosfeer ook in is meegenomen. Voor de pluimberekeningen wordt op dit moment gebruik
gemaakt van de 10% lage afvoer.

9.2

Thermisch lengteprofiel

Het thermische lengteprofiel wordt uitgerekende aan de hand van een warmtebalans. De
warmtebalans is:

ρ × Cv × Q ×

dT
dx

= λ × W × (T − Te)

ρ: dichtheid water [kg.m3]

Cv: warmtecapaciteit water [J.kg−1.oC−1]

Q: rivierdebiet [m3.s−1]

T : Water temperatuur [oC]

x: afstand stroomafwaards [m]

λ: Warmteuitwisselingscoefficient met de atmosfeer [W.m−2C−1]

W : Breedte van rivier [m]

Te: evenwichtstemperatuur met de atmosfeer [oC]

Dit leidt tot een beschrijving van de temperatuur als functie van de afstand:

Tx = (T0 − Te) × e

−x

L + Te

waarbij:

L =

ρ × Cv × Q
λ × W

(9.1)

(9.2)

(9.3)

Deltares

22 van 39

Koudwaterlozingen

Als er de inname vanuit een ander waterlichaam is kan er geen recirculatie optreden en wordt
het lozingsdebiet toegevoegd aan het ontvangende water waardoor het debiet waarmee het
lengteprofiel wordt berekend verhoogt en wordt vergelijking 9.3:

L =

ρ × Cv × (Q + QL)
λ × W

(9.4)

Wanneer ddit lozingsdebiet QL klein is ten opzichte van de afvoer Q zullen beide nagenoeg
hetzelfde resultaat geven.

De Tx levert dan het thermische lengte profiel.

9.3 Bepaling van de dimensies van de mengzone

Voor de beoordeling van de impact
is een mengzone gedefinieerd door een lengte,
dwarsdoorsnede en een oppervlakte. De grens van de mengzone is bepaald door het
toegestane temperatuurverschil. De pluim berekening in de immissietoets levert alleen de
menging als functie van de lengte. Het oppervlak en dwarsdoorsnede zullen nog moeten
worden afgeleid.

Voor de dwarsdoorsnede (met een contour van het toegestane temperatuurverschil) kan
worden afgeleid van een massabalans. Dit levert de maximale doorsnede op die je dan kunt
vergelijken met de doorsnede van het ontvangende water. Hiervoor maken we gebruik van
de benodigde menging om de het temperatuurverschil van het effluent met de achtergrond
(∆T ) terug te brengen tot het toegestane temperatuurverschil (∆Tt).

MTt =

∆T
∆Tt

(9.5)

Om het effluent met een debiet van QL te verdunnen is een rivierdebiet nodig van Qra. De
dwarsdoorsnede die hiervoor nodig is hangt af van de doorsnede van de rivier (ontvangende
water), H × W en het totale rivierdebiet Q en dit vertaalt zich in :

Qra + QL
QL

= MTt ⇒ Qra = (MTt − 1) × QL

(9.6)

De ratio van het benodigde debiet van de rivier en het actuele debiet van de rivier
vertegenwoordigd het relatieve dwarsdoorsnede van de mengzone tov de dwarsdoorsnede
van de rivier. Dit leidt tot een benodigde doorstromend oppervlak van:

AMTt

=

Qra
Q

× (H × W )

(9.7)

Met Q het debiet van de rivier (m3/s). In het huidige kader wordt verwezen naar 50% van de
natte doorsnede hetgeen bijvoorbeeld betekent:

Een rivier met 250 m2 doorsnede (W=25, H = 10 m) en een debiet (Q) van 15 m3/s
een lozingsdebiet (QL) van 1 m3/s en een temperatuurverschil tussen effluent en rivier
van -14 graden (toegestane temperatuurverschil van 4) leidt tot een relatieve maximale
15 ×
doorsnede van (AMTt
100% = 16.7% en dit is minder dan de maximale 50%.

=abs(-14)/4=3.5, dus Qra= (3.5-1) × 1 = 2.5) : Qra

Q = 2.5

Op deze wijze kan de dwarsdoorsnede van de mengzone worden afgeleid.

Deltares

23 van 39

Koudwaterlozingen

Het oppervlak van de pluim kan dan vervolgens worden afgeleid uit een breedte ((cid:112)AMTt
)
en de menglengte die door de pluim berekening wordt uitgerekend (L, de afstand tot de
toegestane temperatuurverschil). Aannemende dat dit een gelijkbenige driehoek vormt wordt
daarvan de oppervlak :

AMopp =

W × L
2

(9.8)

Deze vergelijking gaat echter van uit dat de dimensies van de pluim niet wordt beperkt door
de geometrie (dwarsdoorsnede) van het ontvangende water en de diepte groter is dan deze
dimensie. Omdat in de handreiking wordt verwezen naar het epilimnion (oppervlaktelaag) ligt
het voor de hand om dit ook mee te nemen bij de bepaling van de maximale dikte van de
pluim. In de immissietoets is de waarde van spronglaag (indien>0) beschikbaar en vormt dan
de limiet van de dikte van de pluim. Als er geen dikte gegeven is dan kan de waterdiepte
als limiterend optreden. De dimensies van de pluim zijn altijd begrenst door de dimensies
van het ontvangende water. Dit betekent dat indien de diepte (of spronglaag) kleiner is dan
(cid:112)AMTt
de dikte van de pluim wordt begrenst door die diepte (ligging van de spronglaag)
H. De breedte van de pluim wordt dan W = AMopp/H. Deze kan dan worden gebruikt
om het oppervlak te bepalen van de driehoek va de menglengte en deze breedte. Het kan
in theorie voorkomen dat dit uitkomt op groter dan de breedte van het ontvangende water,
maar in dat geval is de doorsnede van de pluim altijd meer dan 50% en zal het niet door de
desbetreffende beslisboom worden goedgekeurd.

9.4 Koudelozingen in havens

9.4.1 Warmtebalansen

Ook in havens (dus zonder restdebiet) kunnen koudelozingen voorkomen. In deze gebieden
is het debiet (wflow) 0 waardoor op dit moment voor het NWM deel geen resultaat mogelijk
is, maar ook het berekenen van het thermische lengteprofiel is dan ook niet mogelijk. Binnen
de pluim berekening kan dezelfde techniek wel worden gehanteerd als voor de stoffen, ook
de verhoging van de achtergrond wordt dan in beginsel zonder uitwisseling met de atmosfeer
berekend hetgeen wel een worst-case aanpak is. In de warmtebalans van het ontvangende
segment kan daar wel voor worden gecorrigeerd door een warmte-uitwisselingscoëfficiënt,
oppervlakte en diepte. De koppeling met het NWM is er dan nog niet, zodat er geen
temperatuurkaart kan worden gegenereerd.

Voor een haven is de verblijftijd als volgt af te leiden:

τ =

Vs
QL + Qx + Qa

(9.9)

Met QL het lozingsdebiet, Qx het uitwisselings debiet met het langsstromende water en Qa
het additioneel debiet (allen in m3/s).

In de immissietoets zijn er havens waarvan de verversingstijd in de database al bekend is
(uit tracer berekeningen die in de modelsimulaties zijn meegenomen) en waar dit niet zo is
en de uitwisseling met het langsstromende water is afgeleid met een zgn. Silthar berekening
(Eysink (2004)). De berekeningen van Silthar leidt het totale uitwisselende debiet af, maar
niet wat dit voor het lokale ontvangende segment betekent waardoor de door Silthar afgeleide
debieten niet direct kunnen worden gebruikt voor de thermische balans van het ontvangende
segment.

Voor elk segment wordt wel een verdunning of mengfactor MF voor de berekening van de
verhoging van de achtergrond afgeleid. Deze mengfactor berekening wordt gebuikt voor de

Deltares

24 van 39

Koudwaterlozingen

stoflozing. Hieruit kan het uitwisselingsdebiet worden afgeleid dat voor dit segment nodig is:
Qx = QL × (Mf − 1). Hieruit volgt meteen dat de verblijftijd (verversingstijd) in dat segment
kan worden uitgerekend door:

τ =

Vs
QL × (1 + Mf )

(9.10)

In havens zonder verversingstijd (met name de havens in Rotterdam) kan deze uit bestaande
gegevens in de immissietoets worden afgeleid. Wanneer deze wel bekend is kan die bekende
verversingstijd worden gehanteerd.

Voor het bepalen van de verblijftijd is het volume van het ontvangende segment wel van
belang. Het oppervlak van dat segment is bekend voor de polygoon waar de lozing in
plaatsvindt, de diepte ook dus daaruit volgt het volume. Als de inname wel uit de haven zelf
komt dan veranderd niets aan de vergelijking, behalve dat er geen volume wordt toegevoegd
door de lozing, dus QL = 0.

Wanneer water dat wordt geloosd ook in dezelfde haven wordt
recirculatie op. Dit kan schematisch worden weergegeven (figuur 9.1):

ingenomen dan treedt

Figuur 9.1: Haven debieten en warmte transport bij recirculatie, ΦL is de toegevoegde

warmte

In eerste instantie gaan we er van uit dat de recirculatie komt door een lokale verhoging van
de achtergrond, zoals bij de stoflozing uitgerekend wordt, wat warmtebalans betreft ziet deze
er iets anders uit namelijk:

Qx · ρ · Cv · ∆T + QL · ρ · Cv · ∆T − QL · ρ · Cv × (∆T + ∆TL) = 0

(9.11)

De warmtevracht van de lozing is ΦL (J/s), en is gedefinieerd als ΦL = ρ · Cv · ∆TL · QL, met
∆TL de temperatuurverhoging tov de inname temperatuur. Als het water ingenomen wordt
van een andere locatie dan wordt de recirculatiegraad 0 en de vergelijking:

Qx · ρ · Cv · ∆T + QL · ρ · Cv · ∆T − QL · ρ · Cv × ∆TL = 0

(9.12)

Deltares

25 van 39

Koudwaterlozingen

Tot nu toe geldt dezelfde afleiding ook voor stoffen omdat er geen warmte-uitwisseling
aanwezig is. De warmte/massabalans en de debieten die hiervan zijn afgeleid gaan er van
uit dat het binnenkomende water van de uitwisseling (Qx) dezelfde temperatuur heeft als de
achtergrond.
Dit zou wellicht kunnen leiden tot een onderschatting van de
temperatuurverandering in het segment omdat in de haven ook het binnenstromende water
in dat segment al door de lozing zelf is beïnvloed. Echter,
in de massabalans die is
uitgewerkt
(dat geld voor zowel stoffen als temperatuur) wordt uitgegaan van het
theoretische concentratie profiel (stationaire oplossing) waarbij de concentraties als functie
van de afstand tot de haveningang inclusief dit effect is (voor deze afleiding zie hoofdstuk
5.2.8) en dus correct. Het resultaat is dat de mengfactor, Mf , die is uitgerekend en waar de
debieten van worden afgeleid gecorrigeerd zijn voor het
terugstromen bij het
uitwisselingsproces. Hierdoor kan de aanname worden gehanteerd dat dit terugstromende
water inderdaad de achtergrondtemperatuur heeft.

De voorafgaande afleidingen is nog exclusief het effect van een warmte-uitwisseling met de
atmosfeer. Om de warmte-uitwisseling te kunnen berekenen is de verblijftijd of verversingstijd
nodig. Bij afwezigheid van de verversingstijd τ , zoals in Rotterdam, kan deze τ worden
uitgerekend op basis van de stofverspreiding via de mengfactor Mf die bekend is. Daar
kan dan de Qx van afgeleid worden zodat alle info bekend is om de uiteindelijke ∆T uit te
rekenen. Om die warmte-uitwissing uit te rekenen is wel het oppervlakte van het segment
Aseg nodig omdat de verdwijnende warmteflux bepaald wordt door:

Φatm = λ × (T − Te) × Aseg

(9.13)

λ is de warmte-uitwisselingscoëfficiënt en bedraagt 20 W/m2 (conservatieve schatting die
consistent is met die van het NWM).

Deze flux kan worden opgenomen in de warmtebalans en dit leidt dan tot:

Qx·ρ·Cv·∆T +QL·ρ·Cv·∆T −QL·ρ·Cv×(∆T +∆TL)+λ×(T −Te)×Aseg = 0 (9.14)

Dit wordt vereenvoudigd tot:

Qx · ∆T + QL · ∆T − QL × (∆T + ∆TL) +

λ × (∆T ) × Aseg
ρ · Cv

= 0

(9.15)

Hierin is aangenomen dat ∆T is gebaseerd op een achtergrond temperatuur van het water
dat in evenwicht is met de lucht, dus een temperatuurverandering (zowel stijging als daling).
Hieruit kan dan de temperatuur in het segment worden bepaald door:

∆T =

QL · ∆TL
Qx + Qa + λ·Aseg
ρ·Cv

Zonder recirculatie wordt dit:

∆T =

QL · ∆TL
Qx + Qa + QL + λ·Aseg
ρ·Cv

(9.16)

(9.17)

Hierbij
is het eventuele additionele debiet ook meegenomen in de massabalans. Het
resultaat van een dergelijke berekening is in een grafiek uitgewerkt Figuur (9.2) waarbij hier
de onafhankelijke variabele de verblijftijd in dagen is.

Deltares

26 van 39

Koudwaterlozingen

Figuur 9.2: Temperatuurverlaging met en zonder warmteuitwisseling (20 W/m2) en met

en zonder recirculatie. De ∆TL is -8 oC

9.4.2 Opzetten van het warmteprofiel in havens

De berekeningen in het vorige hoofdstuk hebben betrekking op de verhoging van de
achtergrond temperatuur zonder de directe pluimverspreiding, die komt daar nog bij zoals
dat ook voor zoetwatersystemen is geïmplementeerd (dat dus door de applicatie als
pluimmenging wordt bestempeld). De tweede stap is de omgevingsmenging die wordt
berekend aan de hand van een thermische lengte profiel zoals dat al in hoofdstuk 9.2 is
uiteengezet. Daarbij is een debiet en breedte nodig en wanneer de inname ook in de haven
is dan is in beginsel is het netto debiet in een haven 0 en kan deze oplossing niet direct
worden gebruikt.

Een methodiek kan wel worden opgezet wanneer de beschikbare karakteristieken en
rekenresultaten voor het lozingssegment worden gebruikt. Binnen de huidige opzet van de
applicatie zijn alle locatiesegmenten onafhankelijk van elkaar en is niet bekend welke
segmenten bijvoorbeeld buursegmenten zijn. Een havenlengteprofiel kan op dit moment dus
alleen worden afgeleid door gebruik te maken van de gegevens die bij het lozingssegment
horen.
Bij de gebruikte methode wordt geen rekening gehouden met de mogelijke
complexiteit van de haven of uitstroom vanuit de haven naar het hoofdwatersysteem.
Wanneer gebruik gemaakt wordt van een conservatieve aanpak dan geeft het resultaat dus
een indruk van de maximale afstand waarover een lozing in de gegeven omstandigheden
effect heeft. Wanneer de karakteristieken van het lozingssegment wordt toegepast op de
segmenten, dan is een beste benadering om de karakteristieken van dat segment ook voor
het thermische profiel te gebruiken. Dit kan dan worden ingezet door het profiel op te
bouwen voor lengtes van het ontvangende segment en vergelijking 9.17 te gebruiken waarbij
∆TL vervangen wordt door ∆T 1, de berekende temperatuur van het segment waarin
geloosd wordt. Hierbij moet ook een onderscheid gemaakt worden tussen met en zonder

Deltares

27 van 39

recirculatie. Schematisch is het thermische profiel gebaseerd op figuur

Koudwaterlozingen

Figuur 9.3: Overzicht van de methodiek voor het afleiden van het thermische profiel in

havens

Het is dus een iteratieve berekenwijze. Voor segment n kan uit figuur 9.3 een thermische
balans worden afgeleid door:

Qx · ρ · Cv · ∆T n−1 = Qx · ρ · Cv · ∆T n + λ · ∆T n · Aseg

(9.18)

en hieruit volgt dan inclusief recirculatie:

∆Tn =

Qx · ∆T n−1
Qx + λ·Aseg
ρ·Cv

(9.19)

In het uitwisselingsdebiet, zoals dat vanuit de verblijftijd is afgeleid, is het lozingsdebiet voor
de segmenten n>0 niet meegenomen. Zonder recirculatie zal dus het lozingsdebiet moeten
worden opgeteld om de massa en warmtebalans volledig te maken. Dan wordt de vorige
vergelijking 9.19:

∆Tn =

(Qx + QL) · ∆T n−1
Qx + QL + λ·Aseg
ρ·Cv

(9.20)

Deze aanpak is consistent met hoe de de concentraties voor de stoflozingen in de
havensegmenten worden afgeleid. Een beperking is wel dat dit alleen waardes oplevert voor
een integer vermenigvuldiging van de lengte van het havensegment (oftewel het oppervlakte
gedeeld door de breedte dat door de gebruiker is ingevoerd), waardoor een vrij groffe
discretisatie in de afstand optreedt. Er wordt ook geen rekening gehouden met een
mogelijke complexere geometrie van de haven.

9.4.3 Recirculatie in andere wateren

Deltares

28 van 39

Koudwaterlozingen

9.4.3.1 Recirculatie in andere wateren met complexere waterbeweging

De methodiek zoals die voor havens is afgeleid is ook toepasbaar voor wateren waar voor de
segementen een verversingstijd beschikbaar is (dus die met een tracer zijn berekend). De
(worst-case) aanname is dat wel dat het inname punt ook in het lozingssegment zit (dat hoeft
niet perse zo te zijn). Als dat niet zo is dan is er geen recirculatie (daar zou dan een vinkje in
opgenomen kunnen worden?). Voor dit type water (exclusief de havens) kan voor de verdere
verspreiding van het koude water (inclusief de recirculatie ) op dezelfde wijze gekoppekd
worden aan de NWM segmenten. Dus de temperatuurverlaging aan het eind van de
mengzone wordt gebruikt als input voor het NWM. Voor
lijnvormige wateren met 1
stromingsrichting gaat dit niet omdat er geen verversingstijd beschikbaar is voor het
lozingssegment en de recirculatie graad op een andere manier berekend moet worden.

9.4.3.2 Rivieren en ander lijnvormige wateren met 1 stromingsrichting

Wanneer in een oppervlakte water ingenomen wordt en met een lagere temperatuur geloosd
wordt kan er ook recirculatie optreden. Voor wateren waarin een achtergrond menging wordt
berekend kan dezelfde methodologie worden gebruikt als in haven. En hierbij kan dan ook
worden verwezen naar vergelijking 9.16. Dit geldt in beginsel wanneer aangenomen wordt
dat de inname in het zelfde segment plaats vindt als de lozing zelf. Wanneer dit niet het
geval is en er alleen een lozing plaatsvindt, dan kan vergelijking 9.17 worden toegepast. Dus
zolang de verblijftijd bekend is kan dit worden bepaald voor elk watersysteem. De verblijftijd
in een segment wordt niet door de lokale recirculatie beinvloed. Immers, de verblijftijd wordt
bepaald door het uitstromende debiet en het volume van het segment, en dat verandert niet
bij recirculatie. Dit betekent dat voor alle segmenten waar een achtergrondconcdentratie
verhoging voor stoffen wordt berekend, dezelfde aanpak kan worden gehanteerd, omdat
voor die wateren voor het segment waarin de warmtelozing plaatsvindt, de verversingstijd
bekend is en dit bepaald de recirculatie zoals ook in havens is berekend. Voor wateren waar
geen verblijftijd wordt berekend is dit echter niet het geval. Er kan immers recirculatie
optreden wanneer het debiet van de inname (bovenstrooms van het lozingspunt) groter
Er vindt dan tussen het
wordt dan de rivierafvoer.
lozingspunt en innamepunt een
tekort vanuit de rivier aanvult. Met andere woorden, de
terugstroom plaats die het
recirculatiestroom wordt dan QL − Q, waarbij QL groter is dan Q. Wanneer de afstand
tussen inname en lozing bekend is in combinatie met de breedte van het ontvangende water
verminderd de recirculatie door de warmetuitwisseling met de atmosfeer en kan de
uiteindelijke lozingstempertuur (verschil met de achtergrond) worden afgeleid:

∆TLe = ∆Tin + ∆TL

(9.21)

met de innametemperatuur ∆Tin inclusief de recirculatie en rekening houden met het
termische profiel tussen lozingspunt en innamepunt (zie vergelijking 9.2). Hierbij kan dan wel
worden opgemerkt dat QL in vergelijking 9.3 wordt vervangen door Q − QL:

Lr =

ρ × Cv × (QL − Q)
λ × W

(9.22)

De temperatuur van het terugstromende water bij de inlaat na menging met de rvierafvoer
wordt dan (het inlaatdebiet QL is groter dan de rivierafvoer Q):

∆Tin =

QL − Q
QL

· ∆TLe · e− x

Lr

De combinatie van vergelijkingen 9.21 met vergelijking 9.23 levert dit uiteindelijk:

∆TL
1 − QL−Q

QL

· e− x

Lr

∆TLe =

Deltares

(9.23)

(9.24)

29 van 39

Koudwaterlozingen

De ∆TLe is de effluent temperatuur (de QL verandert niet) die uiteindelijk wordt geloosd
en als startpunt dient voor de rest van de koudelozing berekeningen.
In beginsel zijn alle
gegevens bekend. Mocht er geen info zijn over de afstand tussen het inname en lozingspunt,
dan kan deze ook op 0 gezet worden waardoor de vergelijking vereenvoudigd wordt omdat
de temperatuur bij de inlaat enkel het resultaat is van de menging van de rivier afvoer en het
terugstromende debiet.

Deltares

30 van 39

Bibliography

Delvigne, G., 1979.

“Round buoyant jet with three-dimensional trajectory in ambient flow.”

18th Congress of the IAHR, Cagliari, Italy .

Eysink, W., 2004.

“SILTHAR Version 4.2 - A mathematical program for the computation of

siltation in harbour basins.” Report 8.6520, Delft Hydraulics, Delft .

Graaf, J. van de en R. Reinalda, 1977. “Horizontale uitwisseling in samengetrokken modellen.”

Report S0061, Waterloopkundig Laboratorium, Delft .

Hattum, B. van, A. Baart en J. Boon, 2002.

“ Computer model to generate predicted
environmental concentrations (PECs) for antifouling products in the marine environment
- 2nd edition accompanying the release of Mam-Pec Version 1.4.” Report number E-02-
04/Z3117, IVM, Vrije Universiteit, Amsterdam .

IJff, J., 2000. “Emissie-immissie: prioritering van bronnen en de immissietoets (juni 2000).”

CIW werkgroep Emissies en diffuse bronnen (werkgroep VI) .

Deltares

31 van 39

A Testinstructie

A.1

Inleiding

Bij eke aanpassing van de applicatie wordt deze getest, maar voor het interface zijn geen
automatische testen beschikbaar, vandaar deze testinstructie.
De applicatie heeft 3
tabbladen:

1 Stoflozing

2 Temperatuurlozing

3 Informatie

Het is aan te raden om bij het testen de cache eerst te legen zodat nog aanwezige restanten
van een vorige versie het gedrag van de applicatie kunnen beïnvloeden. Wanneer de
applicatie wordt opgestart zal het versienummer in de bovenste balk zichtbaar zijn.
IN dit
document wordt gebruik gemaakt van een specifiek voorbeeld, maar het verdient
aanbevelingen om verschillende watertypes te selecteren en te testen.

A.2 Stoflozing

Open de website van de immissietoets (de publieke site is: www.immissietoets.nl)

Figuur A.1: Informatieblad

Het startscherm wordt zichtbaar (figuur A.1) en de eerste stap is het selecteren en invullen
van de gegevens voor de basisberekening.

De eerste stap voor het uitvoeren van de berekeningen is het selecteren van een locatie en
dat gebeurt door in te zoomen en met de muis te klikken op een locatie (zoals hieronder al
is gedaan). Selecteren kan alleen wanneer de segmenten zichtbaar worden, dus er moet
voldoende worden ingezoomed, zie figuur A.2.

Deltares

32 van 39

Testinstructie

Figuur A.2: Informatieblad

In de figuur is in de info box aangegeven (geen onderdeel van het interface) dat een aantal
kaartlagen kunnen worden geselecteerd (indien beschikbaar), dit heeft voor de applicatie
verder geen consequenties. In dit voorbeeld is een locatie gekozen in de Nieuwe Waterweg.
Het nummer van de locatie is hier 3836. Na het selecteren verschijn aan de rechterkant van
het scherm het menu voor het in- en aanvullen van resterende gegevens. Voor atrazine zijn
ook metingen beschikbaar die zijn aangegeven en in dit voorbeeld is locatie 200102
geselecteerd (en dit geeft een concentratie van 0.0033µg/l. Het invoerveld voor de stof kijkt
ook naar of de tekst in de naam voorkomt (als een filter). Wanneer bijvoorbeeld allen ’atra’ is
ingevuld verschijnen er 4 stoffen (dd: 2-2-24) waaruit kan worden geselecteerd.

⋄ atraton

⋄ atrazine

⋄ desethylatrazine

⋄ desisopropylatrazine

Als er voor een stof meetpunten beschikbaar zijn kan dat op een vergelijkbare manier worden
gekozen via de drop-down lijst, of door het klikken op de locatie van het meetpunt.

1 kies een stof. Er is een lijst en door een stofnaam in te toetsen verschijnen de mogelijke

stoffen (er wordt op sub-strings gezocht), kies atrazine

2 De JG-MKN wordt opgehaald uit de database, de gebruiker kan de waarde aanpassing
indien noodzakelijk, er verschijnt dan aan de rechterkant een icoon die kan worden
aangeklikt om de database waarde te herstellen

3 Debiet en concentratie van het effluent invullen

4 kies een beschikbaar meetpunt voor de achtergrond concentratie door een punt te
een
kaart).

Meetpunt

17914

levert

op

de

selecteren
(zichtbaar
achtergrondconcentratie van 0.0057µg/

5 klik op de knop “resultaten”. Een basisberekening wordt uitgevoerd en de beslisboom

wordt zichtbaar onder de invoerdata.

Deltares

33 van 39

Testinstructie

De naam van het waterlichaam verschijnt als KRW Waterlichaam. Er kan gekozen worden
voor een ander waterlichaam als daar specifieke redenen voor zijn.

Na de eerste berekening verschijnt de beslisboom onder Resultaten met daarin de effluent
en triviaaltoets. Ook zichtbaar onder de kaart worden de invoervelden voor de geavanceerde
berekening (figuur A.3):

Figuur A.3: Invoerscherm voor de geavanceerde berekening

De meeste informatie wordt opgehaald uit de achterliggende database. Wel moet nog worden
ingevuld:

1 dichtheid van de lozing (hier 1000 kg/m3)

2 de diameter van de lozingspijp (hier 0.5 m)

3 de ligging van de pijp in de horizontaal als de verticaal (hier aan de oever en aan het
oppervlak). Hier is een beperkte keuze voor beschikbaar via een drop-down lijst met
de default ’Oever’ en ’Oppervlak’.

Deltares

34 van 39

Wanneer geen gebruiker gedefinieerde afstand wordt opgegeven wordt de toetsafstand
afgeleid van de dimensies van het ontvangende water (hier niet ingevuld). Voor een ingevuld
scherm zie figuur A.4

Testinstructie

Figuur A.4: Beslisbloom voor de geavanceerde berekening

Indien beschikbaar is de MAC MKN voor de gekozen stof ingevuld en een veld dat weergeeft
welke norm dit is (bijvoorbeeld ’Andere oppervlaktewateren wettelijke MAC-MKN (totaal) (zout
water)’)

Druk op de knop “geavanceerde berekening” en een geavanceerde berekening wordt
uitgevoerd en genereert een beslisboom zoals hierboven in figuur A.4 aangegeven.
In de
uitvoer zijn nog een aantal knoppen zichtbaar: Drinkwater inname: Wanneer op deze knop
wordt gedrukt dan verschijnt de volgende tabel met de uitkomsten van de drinkwatertoets
(figuur A.5):

Deltares

35 van 39

Testinstructie

Figuur A.5: Drinkwater tabel

Ook wordt een grafiek gegenereerd met het verloop van de concentratie als functie van de
afstand tot het lozingspunt.

Figuur A.6: Concentratie als functie van de afstand tot het lozingspunt

Er
is ook een log uitvoer waarin in detail kan worden gekeken naar details van
berekeningsresultaten. Deze is met name bedoeld om in detail te onderzoeken welke

Deltares

36 van 39

Testinstructie

getallen zijn gebruikt en voor expert analyse als dat nodig is. Met de knop kan een pdf
uitvoer worden gegenereerd waarin alle in en uitvoer van de berekeningen zijn opgenomen.
Deze kan lokaal op een computer worden opgeslagen.

Er zal goed gekeken moeten worden of alle gewenste velden aanwezig zijn en de uitvoer
correct. Tevens wordt er ook een log gegenereerd en is het mogelijk om een pdf van het
volledige resultaat (in- en uitvoer) van de immissietoets te genereren.

A.3

Temperatuurlozing

Bij het selecteren van de tab temperatuurlozing verschijnt een scherm dat vergelijkbaar is met
de stoflozing tab. Als vanuit een geselecteerd gebied in stoflozing wordt overgestapt naar de
temperatuur tab, dan blijf de locatie selectie in stand.

Figuur A.7: Scherm van de temperatuur tab na selectie

Specifieke data zal nog moeten worden ingevuld.
In dit voorbeeld is de diameter van 0.5m
gekozen en onder het kopje Temperatuur is een lozing van -8 graden (ten opzichte van het
ontvangende water) gekozen. Let op dat ook naar de zoutconcentratie moet worden gekeken
In beginsel is de zoutconcentratie gelijk aan die van het
omdat deze bij default op 0 staat.
ontvangende water maar moet die wel worden ingevuld, tenzij het proces de zoutconcentratie
verandert of de inname uit een ander watersysteem wordt gehaald (dus de zoutconcentratie
afwijkt).

In het voorbeeld van figuur A.7 is dezelfde locatie gekozen (3836).

Na het uitvoeren van de berekening wordt het volgende scherm zichtbaar. Zaak is om te
controleren dat alle velden inderdaad aanwezig zijn.

Deltares

37 van 39

Testinstructie

Figuur A.8: Temperatuur invoer en resultaat scherm

In versie 1.13.1 is de beslisboom niet meer zichtbaar omdat die niet meer actueel is en in
de loop van 2024 zal worden vervangen.
In plaats daarvan wordt de ’Resultaten’ tab met
daarin een grafiek getoond. Wanneer de aangegeven locatie is gekozen wordt een watertype
O geselecteerd. Om echter een resultaat te krijgen zal een selectie gemaakt moeten worden
en in dit geval is gekozen voor "Grote rivieren(R8)".

In de grafiek is het toegestane verschil (in dit geval 4 graden) grijs aangegeven.

Er wordt ook een kaar gegenereerd met daarin aangegeven hoe groot het gebied is dat door
de koudelozing wordt beïnvloed.

Figuur A.9: Indicatie van het gebied dat door de koudelozing wordt beïnvloed

Deltares

38 van 39

A.4

Informatie

Dit tabblad geeft algemene inhoudelijke informatie over de applicatie.

Testinstructie

Figuur A.10: Informatieblad

Aan het eind van de pagina is een link opgenomen die verwijst naar de IPLO site om vragen
in te kunnen dienen.

Contact: Vraag het onze experts | Informatiepunt Leefomgeving (iplo.nl)

Deze link verwijst naar: https://iplo.nl/contact/vragenformulier/ en deze link kan dan ook
worden getest of inderdaad naar een bestaand adres wordt verwezen.

Deltares

39 van 39

