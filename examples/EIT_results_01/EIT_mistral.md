# Immissietoets webapplicatie 

## Technische beschrijving

F.M. Kleissen

Versie: 0.2
Revisie: ----
1 juli 2025# Gepubliceerd en gedrukt door: 

Deltares
Boussinesqweg 1
2629 HV Delft
Postbus 177
2600 MH Delft
Nederland

## Verkoop:

telefoon: +31883358188
e-mail: Verkoop
www: Verkoop \& Ondersteuning
telefoon: +31883358100
e-mail: Ondersteuning
www: Verkoop \& Ondersteuning

Copyright © 2025 Deltares
Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd in enige vorm door middel van druk, fotokopie, microfilm of op welke andere wijze dan ook, zonder voorafgaande schriftelijke toestemming van de uitgever: Deltares.# Inhoudsopgave 

Lijst van figuren ..... iv
Woordenlijst ..... 1
1 Inleiding ..... 3
2 Definitie van de maximale toegestane mengzone ..... 4
3 Near-field berekeningen met Jet3D en Fisher diffusie ..... 7
3.1 Inleiding ..... 7
3.2 Pluimverspreiding volgens de zoete toets (Fisher diffusie) ..... 8
3.3 Jet3D ..... 10
4 Algemene berekeningen ..... 11
4.1 Begrip mengfactor ..... 11
4.2 Eenvoudige menging ..... 11
5 Berekening van stofconcentraties in havens ..... 12
5.1 Havens met een gegeven verblijftijd ..... 12
5.2 Havenuitwisseling zonder verblijftijd middels SILTHAR ..... 13
5.2.1 Uitwisseling door het getij ..... 13
5.2.2 Uitwisseling door neervorming ..... 13
5.2.3 Uitwisseling ten gevolge van dichtheidverschillen ..... 14
5.2.4 Totale uitwisseling op basis van SILTHAR ..... 15
5.2.5 Concentratieverdeling in de haven ..... 15
5.2.6 Schatting van factor $\gamma$ ..... 15
5.2.7 Bepaling van $D_{0}$ als functie van $\gamma$ ..... 16
5.2.8 Afleiding van concentratieprofiel ..... 16
5.2.9 Invloed van andere lozingen in de haven ..... 17
6 Getij-uitwisseling ..... 18
7 Kust en zee ..... 20
8 Totale menging en eindconcentratie ..... 21
9 Koudwaterlozingen ..... 22
9.1 Inleiding ..... 22
9.2 Thermisch lengteprofiel ..... 22
9.3 Bepaling van de dimensies van de mengzone ..... 23
9.4 Koudelozingen in havens ..... 24
9.4.1 Warmtebalansen ..... 24
9.4.2 Opzetten van het warmteprofiel in havens ..... 27
9.4.3 Recirculatie in andere wateren ..... 28
9.4.3.1 Recirculatie in andere wateren met complexere waterbeweging ..... 299.4.3.2 Rivieren en ander lijnvormige wateren met 1 stromingsrichting ..... 29
A Testinstructie ..... 32
A. 1 Inleiding ..... 32
A. 2 Stoflozing ..... 32
A. 3 Temperatuurlozing ..... 37
A. 4 Informatie ..... 39# Lijst van figuren 

2.1 Definitie van de maximaal toegestande mengzone, $\mathrm{M}_{x}$ ..... 5
3.1 Uitwerking diffusie volgens Fisher ..... 9
5.1 Definitie van geometrie en debieten in een haven ..... 15
9.1 Haven debieten en warmte transport bij recirculatie, $\Phi_{L}$ is de toegevoegde warmte ..... 25
9.2 Temperatuurverlaging met en zonder warmteuitwisseling ( $20 \mathrm{~W} / \mathrm{m}^{2}$ ) en met en zonder recirculatie. De $\Delta T_{L}$ is $-8^{\circ} \mathrm{C}$ ..... 27
9.3 Overzicht van de methodiek voor het afleiden van het thermische profiel in havens ..... 28
A. 1 Informatieblad ..... 32
A. 2 Informatieblad ..... 33
A. 3 Invoerscherm voor de geavanceerde berekening ..... 34
A. 4 Beslisbloom voor de geavanceerde berekening ..... 35
A. 5 Drinkwater tabel ..... 36
A. 6 Concentratie als functie van de afstand tot het lozingspunt ..... 36
A. 7 Scherm van de temperatuur tab na selectie ..... 37
A. 8 Temperatuur invoer en resultaat scherm ..... 38
A. 9 Indicatie van het gebied dat door de koudelozing wordt beïnvloed ..... 38
A. 10 Informatieblad ..... 39# Woordenlijst 

$C_{v}:$ warmtecapaciteit water $\left[\mathrm{J} . \mathrm{kg}^{-1} .{ }^{\circ} \mathrm{C}^{-1}\right] .22,23,25,26,28,29$
$Q_{a}:$ additioneel debiet $\left[\mathrm{m}^{3} . \mathrm{s}^{-1}\right] .24,26$
$L$ : afstand tot de toegestande temperatuurverschil $[m] .24$
$Q_{r a}:$ benodigde rivierdebiet $\left[\mathrm{m}^{3} . \mathrm{s}^{-1}\right] .23$
$W$ : breedte van de rivier [m]. 22-24, 29
$H$ : waterdiepte in de rivier [m]. 23, 24
$A_{M_{T_{t}}}$ : benodigd doorstromend oppervlak $\left[m^{2}\right] .23$
$T_{e}$ : evenwichtstemperatuur met de atmosfeer $\left[{ }^{\circ} \mathrm{C}\right] .22,26$
$\Delta T_{i n}$ : inname temperatuurverschil $\left[{ }^{\circ} \mathrm{C}\right] .29$
$L_{r}$ : karakteristieke lengte $[m] .29$
$T_{x}$ het thermische lengte profiel, temperatuur $\left[{ }^{\circ} \mathrm{C}\right]$ als functie van de afstand x. 22, 23
$Q_{L}$ : lozingsdebiet $\left[\mathrm{m}^{3} . \mathrm{s}^{-1}\right] .23-26,28-30$
$M_{F}$ : mengfactor [-]. 25, 26
$A_{M_{\text {opp }}}$ : benodigd doorstromend oppervlak $\left[m^{2}\right] .24$
$Q$ : rivierdebiet $\left[\mathrm{m}^{3} . \mathrm{s}^{-1}\right] .22,23,29$
$A_{\text {seg }}:$ segmentoppervlak $\left[m^{2}\right] .26,28$
$V_{s}:$ segmentvolume $\left[m^{3}\right] .24,25$
$T_{0}$ : temperatuur bij lozingspunt na volledige mening $\left[{ }^{\circ} \mathrm{C}\right] .22$
$x$ : afstand stroomafwaarts [m]. 22, 29
$M_{T_{t}}:$ de benodigde menging om de het temperatuurverschil van het effluent met de achtergrond terug te brengen tot het toegestane temperatuurverschil [-]. 23, 24
$\Delta T_{L}$ : temperatuurverschil van het effluent met de achtergrond/verschil tov inname $\left[{ }^{\circ} \mathrm{C}\right]$. iv, 25-27, 29
$\Delta T_{n}$ : temperatuurverschil in volume/segment $\mathrm{n}\left[{ }^{\circ} \mathrm{C}\right] .28$
$\Delta T:$ temperatuurverschil $\left[{ }^{\circ} \mathrm{C}\right] .23,25-28$
$\Delta T_{t}:$ toegestane temperatuurverschil $\left[{ }^{\circ} \mathrm{C}\right] .23$
$\Delta T_{L e}$ : uiteindelijke lozingstemperatuur (verschil met achtergrond) $\left[{ }^{\circ} \mathrm{C}\right] .29,30$
$Q_{x}$ : uitwisselingsdebiet $\left[\mathrm{m}^{3} . \mathrm{s}^{-1}\right] .24-26,28$
$\tau$ : verblijftijd [s]. 24-26
$\Phi_{\text {atm }}$ : warmteflux met atmosfeer $\left[W / m^{2}\right] .26$
$\lambda$ : Warmteuitwisselingscoefficient met de atmosfeer $\left[\mathrm{W} . \mathrm{m}^{-2} \mathrm{C}^{-1}\right] .22,23,26,28,29$$\Phi_{L}:$ warmtevracht lozing $[J / \pi]$. iv, 25
$\rho:$ dichtheid water $\left[\mathrm{kg} \cdot \mathrm{m}^{3}\right] .22,23,25,26,28,29$
$T$ : Water temperatuur $\left[{ }^{\circ} \mathrm{C}\right] .22,26$# 1 Inleiding 

De webapplicatie van de immissietoets is een eerste stap in de beoordeling van individuele lozingen. Lozingen van stoffen (in een effluent) worden beoordeeld volgens het Handboek Immissietoets. Koudelozingen worden beoordeeld volgens het STOWA stappenplan : (https://www.stowa.nl/sites/default/files/assets/PUBLICATIES/Publicaties\ 2021/STOWA\ 202130\%20koudelozingen\%20stappenplan.ppsx). De webapplicatie (www.immissietoets.nl) zal bij standaard gebruik een consdervatieve aanpak hanteren, hetgeen betekent dat de effecten door de applicatie worden overschat. Het gevolg is dat de applicatie geen conclusie zal trekken dat een lozing niet is toegestaan. Indien volgens de gebruikte berekening niet aan de criteria kan worden voldaan, dan zal een vervolgonderzoek moeten uitwijzing of een lozing al dan niet vergunbaar i

De applicatie heeft op dit moment twee werkgebieden, te weten:
$\diamond$ Stoflozingen
$\diamond$ Koudelozing

De stoffen die met een effluent worden geloosd worden als conservatief beschouwd, dus zonder afbraakprocessen. Voor koudelozing is dat voor het eerste deel (de pluimverspreiding) ook zo, maar voor dit werkgebied is ook toegevoegd een inschatting van de invloed van een koudelozing en hierbij wordt een conservatieve schatting van de warmteuitwisseling met de atmosfeer meegenomen.# 2 Definitie van de maximale toegestane mengzone 

De definitie van het begrip mengzone is gebaseerd op de definitie zoals die de Kaderrichtlijn water is geintroduceerd. Directive 2008/105/EC Article 4 introduceert mengzones als volgt:

Member States may designate mixing zones adjacent to points of discharge. Concentrations of one or more substances listed in Part A of Annex I may exceed the relevant EQS within such mixing zones if they do not affect the compliance of the rest of the body of surface water with those standards

Met het begrip "mengzone" wordt in dit document de maximale toegestane mengzone (MTMZ) bedoeld en de grootte van MTZT is afhankelijk van het watertype en dimensies van het ontvangende water. Ter verduidelijking is dit niet hetzelfde als de initiele mengzone die hier is gedefinieerd als dat gebied van pluimverspreiding tot het punt waarbij de de pluim het oppervlak (of bodem/kant) raakt. Hoe dit punt wordt bepaald hang af van welke rekentechniek wordt gebruikt (Jet3D versus Fisher). De pluim zelf kan dan worden gerelateerd aan het gebied tot het punt waarop de menging niet meer toeneemt, dus een maximale menging heeft bereikt.

De berekeningen van de webbapplicatie van de immissietoets bestaat uit een pluimberekening (middels eenvoudige modelberekeningen) en meer algemene mengberekeningen. Wanneer in het kader van de webapplicatie de pluim de bodem, het oppervlak of een van de oevers raakt is dit in beginsel de initiele menging.

Voor het voorstel van de definitie van de mengzone zijn de oppervlaktewateren in verschillende typen onderscheiden:

1 Zoet water (saliniteit minder dan 0,5 PSU):
(a) Rivier/kanaal;
(b) Meer;

2 Estuaria en getijrivieren met een restdebiet;
3 Doodlopende kanaalpanden en havens (zonder restdebiet);
4 Aan de oevers van brede estuaria, zeearmen en Waddenzee/ Eems-Dollard met duidelijk aanwijsbare getijgeulen;

5 Aan de kust van de open zee;
6 Open zee.

In beginsel wordt uitgegaan van een mengzone die een cirkel beslaat met een maximum straal van 500 m . De ligging van het lozingspunt in de cirkel varieert, afhankelijk van de condities. De algemene vorm, grootte en ligging ten opzichte van het lozingspunt is globaal aangegeven in Figuur 2.1. Verder zijn er nog een aantal bijzonderheden en extra beperkingen.![img-0.jpeg](img-0.jpeg)

Figuur 2.1: Definitie van de maximaal toegestande mengzone, $M_{x}$

De mengzones zijn als volgt gedefinieerd:
Ad 1: De breedte van de mengzone wordt beperkt tot $1 / 4$ van de breedte van het ontvangende water met een maximum van 1000 m . De gehele mengzone bevindt zich stroomafwaarts van het lozingspunt, omdat de stroming in dit type water slechts 1 richting kent.

Voor meren geldt de huidige definitie breedte mengzone (CIW, 2000):
Hierbij is $A$ is oppervlak, $L$ is lengte en $B$ is breedte van het meer.
Het huidige maximum is 1000 m , maar hier wordt voorgesteld om de maximale afstand vanaf het lozingspunt voor meren te beperken tot 500 m , gelijk aan de eerder gedefinieerde maximum straal, waardoor de definitie van de mengzone strenger is dan huidige definitie maar wel consistent is met de definitie in andere watertypen.

Ad 2: Mengzone is hetzelfde gedefinieerd als voor zoet. Echter, de ligging van het lozingspunt binnen de mengzone varieert, afhankelijk van de verhouding tussen het vloedvolume en ebvolume. Zonder netto afvoer zijn deze twee gelijk (verhouding $=1$ ) en dan ligt het lozingspunt precies in het centrum van de mengzone (met een maximum straal van 500 m ). Als het vloedvolume nul is dan is de mengzone precies hetzelfde gedefinieerd als voor zoet water. De toetsing vindt dan plaats op de rand van de mengzone met de grootste afstand tot het lozingspunt, hetgeen in praktijk betekent in de richting van de netto afvoer (zeewaarts).

Ad 3: Aan het eind van een haven kunnen de criteria worden versoepeld, afhankelijk van de doelstelling van dit waterlichaam. Voor een van te voren vastgesteld deel van de haven wordt een minimale waterkwaliteit nagestreefd, zoals een minimale zuurstofconcentratie van 3 of $4 \mathrm{mg} / \mathrm{l}$. Tevens mag 25 m van het lozingspunt de ER niet worden overschreden (inclusief de verhoging van de achtergrond door ophoping van het effluent) om acute problemen te voorkomen. Voor welk deel dit wordt toegestaan is een relatief arbitraire beslissing, maar zou gebaseerd kunnen zijn op een maximum percentage van de haven, en/of een maximum volume en/of maximum oppervlak, gebaseerd op een halve cirkel met een straal van 500m. Dit deel van de haven geldt vanaf het verste punt in de haven. De mengzone voor een haven zal nog in detail moeten worden ingevuld.

Ad 4: Een zelfde definitie als voor getijdewateren wordt gehanteerd, maar de dimensies vanhet ontvangende water waar de mengzone op wordt gebaseerd zijn de dimensies en andere karakteristieken van de geul bij laagwater. Als de lozing tijdens laag water op een drooggevallen plaat plaatsvindt, dan zullen andere criteria gehanteerd worden. Daar wordt in de definitie van de mengzone geen uitspraak over gedaan.

Ad 5: Aan de kust geldt een zelfde mengzone als voor estuaria, dus een halve cirkel met een straal van 500 m .

Ad 6: Bij een diepte van 30 m of meer geldt dat de mengzone een straal heeft van 150 m rondom het lozingspunt en een dikte (diepte) van 30m. Dit vertegenwoordigt een volume van 2.106 m 3 . Voor dieptes minder dan 30 m , maar meer dan 5 m geldt dat de straal wordt afgeleid van de diepte en het toegestane volume. Voor bijvoorbeeld 10 m diepte zou dit een straal van 250 m betekenen. Bij minder dan 5 m wordt de maximale straal van 500 m gehanteerd. Dit geldt overigens niet als het een lokale diepte betreft, zoals een (getij)geul.

De webapplicatie berekend op basis van de de definitie van het ontvangende water (het watertype) de maximaal toeghestane mengzone waarop getoetst wordt. Hierbij wordt geen rekening gehouden met het eventueel overlappen met een beschermd gebied.

Voor acute toxiciteit is een mengzone afgeleid die maximale 25 m gehanteerd is voor een ontvangende water waarvoor een maximale mengzone geld van 1000m. De MAC afstand wordt evenredig kleiner naarmate de mengzone kleiner is, dus $0.25^{*} \mathrm{M}_{2}$. De concentratie wordt getoetst aan de toegestane concentratie, de MAC waarde (Maximum Aanvaardbare Concentratie). Voor de bestaande zoete toets wordt voor het ER niveau (Ernstig Risico) wordt een maximale afstand van 25 m gehanteerd $\left(0.25^{*} \mathrm{~B}_{10}\right.$ aterlichaam $\left.\leq 25 \mathrm{~m}\right)$. Het ligt dan voor de hand om voor zoute wateren in eerste instantie ook deze verhouding $0.25^{*} \mathrm{~B}$ waterlichaam met een maximum van 25 m als mengzone te hanteren.

Deze keuze kan in praktijk betekenen dat voor kleinere mengzones dit nagenoeg gelijkwaardig is aan het hanteren van de MAC als concentratielimiet in het effluent. Bijvoorbeeld, een lozing op een smal watersysteem, bijvoorbeeld 10 m , resulteert in een lengte voor de MACmengzone van $2,5 \mathrm{~m}$. Over een dergelijke afstand treden in het algemeen slechts kleine verdunningsfactoren op.# 3 Near-field berekeningen met Jet3D en Fisher diffusie 

### 3.1 Inleiding

Er zijn in de applicatie twee soorten pluimberekeningen beschikbaar. De eerste is de pluimberekening, die ook al wordt toegepast binnen het kader van de zoete toets (IJff (2000)). Deze berekening houdt echter geen rekening met dichtheidverschillen tussen effluent en ontvangende water of met verticale dichtheidsgradiënten in het ontvangende water. Deze kunnen het verspreidingsgedrag van de pluim significant beïnvloeden. Vandaar dat ook een pluimverspreidingsmodel, dat met dergelijke dichtheidverschillen rekening kan houden, in het instrument is opgenomen. Dit is het model Jet3D dat door het toenmalige Waterloopkundig Laboratorium is ontwikkeld (Delvigne (1979)) en wordt toegepast wanneer het dichtheidsverschil tussen lozing en ontvangende water groter is dan $1 \mathrm{~kg} / \mathrm{m}^{3}$.

Voor beide pluimberekeningen is de maximale menging begrensd door de hoeveelheid water dat beschikbaar is voor menging. Dit is bepaald door de eenvoudige menging waarbij een massabalans de maximale menging uitrekent op basis van het beschikbare debiet (rivierafvoer) en lozingsdebiet (zie Hoofdstuk 4.2).

De lozing kan plaatsvinden op verschillende posities in het ontvangende water. Om het gebruik van de applicatie zo eenvoudig mogelijk te houden is gekozen om die positie in het oppervlaktewater te beperken tot:

- Positie van de lozing = horizontaal
$1=$ midden
$2=$ oever
- Positie van de lozing = vertikaal
$1=$ top (oppervlakte)
$2=$ midden (halverwege de diepte)
$3=$ bodem.

Jet3D kan met optie 3 (lozing bij de bodem) rekenen, CIW-Fisher gaat er van uit dat resultaat van pluim aan top (1) gelijk is aan resultaat aan bodem (3) (er is immers geen dichtheidsverschil)

De pluimberekening (zowel Jet3D als Fisher en de combinatie van beide) loopt door tot de toetsafstand (de berekende m_mixingzone_ya_length, afhankelijk van het type en dimensies van het ontvangende water) is bereikt. Op die toetsafstand wordt de menging van de pluim gebruikt in combinatie met de achtergrondmenging.

In havens is het zo dat een pluim berekening niet meer verder kan als de pluim de haven uitgaat en in een langsstromend water terecht komt. De hydrodynamica gaat dan significant afwijken van het water waarin wordt geloosd en dan is de pluimberekening niet meer relevant.

Vandaar ook dat in havens de m_mixingzone_ya_length word gelimiteerd tot de afstand van het lozingspunt tot de haven mond (w_distance_effluent_to_harbour_entrance). Deze laatste afstand is gekoppeld aan het haven segment (dus 1 waarde voor elk segment in de haven). Dit afkapmechanisme van de mixingzonelength vindt plaats voor zowel havens met als zonder tracer.# 3.2 Pluimverspreiding volgens de zoete toets (Fisher diffusie) 

De beschrijving van de berekeningen zijn in de documentatie van de zoete toets opgenomen (IJff (2000)). Bij deze berekening wordt een onderscheid gemaakt in:
$\diamond$ Een situatie waarbij in eerste instantie sprake is van een uitstroming in de vorm van een jet die vervolgens overgaat in een tweedimensionale pluim;
$\diamond$ Een situatie waarbij de uitstroming direct plaatsvindt in de vorm van een driedimensionale pluim die daarna overgaat in een tweedimensionale pluim.

Welke van deze twee condities gelden is afhankelijk van de verhouding tussen de uitstroomsnelheid en de stroomsnelheid van het ontvangende water. De berekening is uitgewerkt volgens onderstaande figuur 3.1.![img-1.jpeg](img-1.jpeg)

Figuur 3.1: Uitwerking diffusie volgens Fisher

Dit figuur komt uit IJff (2000)# 3.3 Jet3D 

Voor situaties waar dichtheidsverschillen een rol spelen in de verspreiding van de pluim is het pluimverspreidingsmodel Jet3D beschikbaar (Delvigne (1979)). Dit model is in de jaren 70 door het toenmalig Waterloopkundig Laboratorium ontwikkeld en beschrijft de driedimensionale verspreiding van een ronde pluim met een dichtheid die kan afwijken van het ontvangende water. Het ontvangende water kan een niet-uniform verticaal dichtheidprofiel en een niet-uniform snelheidsprofiel hebben.

Dit model is nodig in situaties die niet door de 'zoete' pluimberekening kunnen worden gesimuleerd vanwege optredende dichtheidsverschillen. Zonder de significante initiele dichtheidsverschillen wordt de Fisher pluimverspreiding gebruikt zodat de resultaten voor dergelijke situaties (rivieren en kanalen met stroming) overeenkomen met de oorspronkelijk berekeningen met het spreadsheet dat oorspronkelijk ontwikkeld was ten behoeve van de immissietoets (IJff (2000)).

Het model beschrijft de pluim vanaf het moment dat het effluent de pijp verlaat. De berekeningen stoppen wanneer de rand van de mengzone is bereikt of wanneer de pluim de bodem of wateroppervlak of een van beide oevers raakt. In de applicatie stopt de berekening ook wanneer de diameter van de pluim groter wordt dan de diepte of de breedte van het ontvangende water.

Als de Jet3D berekening stopt voordat de rand van de mengzone is bereikt worden de gegevens overgenomen door de 2D berekening die ook in de zoete pluimberekening is opgenomen. Hierbij wordt ervoor gezorgd dat er geen discontinuïteit optreedt in de verdunning van de pluim door de diepte die in de 2D berekening wordt gebruikt aan te passen en in de verdere berekening constant te houden.

Er is nog wel een opmerking te maken ten aanzien van een gestratificeerd ontvangend water. Wanneer het ontvangende water is gestratificeerd met een spronglaag (dus niet een linear geinterpoleerde verticale dichtheidgradient) dan wordt de jet in een waterlaag geloosd met de dikte van de laag die qua dichtheid het laagste verschil geeft met de dichtheid van het geloosde effluent. Dan wordt dus kunstmatig de diepte aangepast.(Dit is een conservatieve aanname). Dit heeft overigens geen effect op de verhoging van de achtergrond concentratie (ter hoogte van het lozingspunt).# 4 Algemene berekeningen 

### 4.1 Begrip mengfactor

In de rekentechnieken die in de applicatie zijn opgenomen worden mengfactoren berekend. De mengfactor die voor het effluent kan worden afgeleid is het resultaat van het samenvloeien van verschillende stromingen en is gedefinieerd vanuit een eenvoudige massabalans.

De mengfactor is berekend door:

$$
M_{f}=\frac{Q_{r}+Q_{a}+Q_{l}}{Q_{l}}
$$

Waarbij $Q_{r}$ is het rivierdebiet, $Q_{a}$ ander debiet door het watersysteem en $Q_{l}$ het lozingsdebiet (allen in $\mathrm{m}^{3} / \mathrm{s}$ ).

Deze mengfactor kan ook worden afgeleid vanuit de de concentraties van het effluent en de achtergrond en het bereikte concentratieverschil:

$$
M_{f}=\frac{C_{l}-C_{a}}{\Delta C}
$$

Waarbij $C_{l}$ en $C_{a}$ de concentratieverandering na menging met een mengfactor $M_{f}$. Vanuit de in de berekende mengfactoren wordt vervolgens de concentratie na menging berekend. In de applicatie van de immissietoets wordt gebruik gemaakt van een algemene menging en een pluim verspreiding. De berekening van de algemene menging is afhankelijk van het watertype. Voor de pluimberekening worden twee modellen toegepast, te weten het Jet3D model, wanneer er een significant dichtheidsverschil is tussen effluent en ontvangende water, en het Fisher model wanneer dat niet zo is. De eindconcentratie op de toetsafstand is een combinatie van de algemene menging en de pluimmenging (zie hoofdstuk 8)

### 4.2 Eenvoudige menging

De berekening is beschikbaar voor watersystemen die goed gemengd zijn waardoor er een verhoging van de achtergrondconcentratie $(\Delta C)$ ten gevolge van de lozing optreedt. Dit geld voor beken, kanalen, rivieren. Deze massabalans wordt ook toegepast op andere oppervlaktge wateren, zoals getijdewateren en meren om de verhoging van de achtergrondconcentratie te berekenen, volgens vergelijking 4.1. Deze menging wordt dan gecombineerd met het resultaat van de pluimmenging.# 5 Berekening van stofconcentraties in havens 

Voor de berekening van pluim concentraties in havens zijn twee methodes toegepast. De eerste is door gebruikt te maken van verblijftijden die uit modelberekeningen zijn afgeleid (de zogenaamde tracer berekeningen). De tweede is om de uitwisseling tussen de haven en het voorbijstromende water te berekenen en daaruit de concentraties ten gevolge van een lozing in de haven af te leiden.

### 5.1 Havens met een gegeven verblijftijd

Deze methode om de achtergrondconcentratieverhoging ten gevolge van een lozing in een haven te bepalen maakt gebruik van de resultaten van modelsimulaties van tracers. Deze methode wordt ook voor andere wateren gebruikt en is gebaseerd op tracer berekenening met het achterliggende hydrodynamische model (zoals Delft3D of SOBEK).

Uitgangspunt is een haven met een tracerconcentratie van 1 en een concentratie van 0 in het hoofdwatersysteem, waarna het model de afname van de tracer concentratie ten gevolge van de uitwisseling tussen de haven en het hoofdwatersysteem berekent. De haven wordt vervolgens in een aantal deelgebieden opgedeeld. De afnemende concentratie als functie van de tijd in een deelgebied bepaalt de verversingstijd voor dat deelgebied. Deze verversingstijd wordt dan gebruikt om de verhoging van de achtergrondconcentratie in een deelgebied ten gevolge van een effluent lozing in dat gebied te berekenen.

Om de berekening binnen de webapplicatie te vereenvoudigen en toepasbaar te maken wordt aangenomen:
$\diamond$ de concentratie in de gedefinieerde deelgebieden neemt exponentieel af (deze aanname is equivalent met de aanname dat de deelgebieden volledig gemengd zijn);
$\diamond$ de te beoordelen lozing beïnvloedt de hydrodynamica in de haven niet significant.

Bij een exponentiële aanname geldt voor elk segment (deelgebied) dat de verversingstijd kan worden uitgedrukt als $T=V / Q$, met $Q$ het 'verversingsdebiet' en $V$ het volume van het deelgebied. Als een effluent, bestaand uit debiet $Q_{l}$ en concentratie $C_{l}$, in een deelgebied loost, dan kan via een massabalans de evenwichtsconcentratie in dat deelgebied worden berekend.

Als een mogelijk andere debiet $\left(Q_{a}\right)$ die niet in de hydrodynamische modelberekeningen is meegenomen, omdat het bijvoorbeeld andere industriële lozingen betreft die relatief klein zijn, dan kan deze lozing wel in de massabalans worden meegenomen.

Dan wordt aangenomen wordt dat deze andere lozing zich bovenstrooms van de lozingslocatie of in hetzelfde subgebied bevindt (benedenstrooms van de lozing heeft het geen direct effect op de verversingstijd ter hoogte van de effluentlozing). Dit wordt in de aanpak met de SILTHAR berekeningen (zoals op dit moment ook in de webapplicatie is opgenomen) ook aangenomen. Als vervolgens wordt aangenomen dat de concentratie van deze andere lozing 0 is en in het deelgebied volledig is gemengd dan volgt uit de massabalans:

$$
\frac{C_{l}}{C}=\frac{\left(\frac{V}{T}+Q_{l}+Q_{a}\right)}{Q_{l}}
$$Deze beschrijving geldt indien de achtergrondconcentratie nul is. Wanneer deze groter is dan 0 , dan wordt in de berekeningen niet de effluentconcentratie gebruikt, maar het verschil in concentratie tussen het effluent en het ontvangende water.

Deze verversingsberekeningen worden alleen gebruikt als in de onderliggende database de afgeleide gegevens (verversingstijden) voor de betreffende havensegmenten zijn opgeslagen. Als deze gegevens niet aanwezig zijn, dan wordt de SILTHAR methode toegepast.

De verhoging van de achtergrondconcentratie in het deelgebied waar wordt geloosd wordt vervolgens gecombineerd met de pluim/jet berekening (paragraaf 4.1) waarna de concentratie op de toetsafstand wordt afgeleid.

# 5.2 Havenuitwisseling zonder verblijftijd middels SILTHAR 

Havens en doodlopende kanaalpanden hebben geen zoetwaterafvoer die het water in de haven kan verversen. Effluent dat in havens wordt geloosd kan alleen maar verdunnen als er een transport is vanuit de haven naar de uitgang van de haven. Dit transport kan bestaan uit diffusie/dispersie in combinatie met uitwisseling van water in de haven met het water daarbuiten. De uitwisseling zorgt voor de verversing in de haven (en een verlaging van de verblijftijd) terwijl de diffusie/dispersie processen de concentratiegradiënten in de haven bepalen. In de webapplicatie zijn twee berekeningen opgenomen om menging in havens en de uitwisseling met het hoofdwatersysteem te beschrijven.

De in dit hoofdstuk 5.2 gepresenteerde methode is gebaseerd op de uitwisselingsprocessen die zijn afgeleid uit het SILTHAR model (Eysink (2004)). Ook in MAMPEC worden dezelfde formuleringen gebruikt (Van Hattum et al. (2002)). Een tweede methode die in paragraaf 5 is uitgewerkt is afgeleid uit modelresultaten waarbij een tracer is gebruikt om de verversingssnelheid in vooraf gedefinieerde (haven)segmenten te bepalen.

Voor uitwisseling tussen het water in de haven en het voor de ingang van de haven langsstromende (getijde)rivierwater zijn drie processen bepalend:
$\diamond$ Uitwisseling door het getij;
$\diamond$ Uitwisseling door neervorming;
$\diamond$ Uitwisseling ten gevolge van dichtheidsverschillen tussen het water in en buiten de haven.

### 5.2.1 Uitwisseling door het getij

Het uitwisselingsvolume ten gevolge van het getij is het zogenaamde getijvolume en is bepaald door de verticale getijslag $\left(H_{g}\right)$ en het oppervlak van de haven $\left(B_{h} \times L_{h}\right)$ :

$$
V_{t}=H_{g} \times B_{h} \times L_{h}
$$

### 5.2.2 Uitwisseling door neervorming

Door stroming langs de ingang van de haven of doodlopend kanaal ontstaat neervorming die wateruitwisseling tussen de haven en het langsstromende water genereert. Dit proces is beschreven door (Van de Graaf en Reinalda (1977)):

$$
Q_{h}=f_{1} \times h \times b \times u_{0}-f_{2} \times Q_{t}
$$met $h$ en $b$ de hoogte en breedte van de haveningang, $u_{0}$ de stroomsnelheid voor de ingang en $Q_{t}$ het debiet van het binnenstromende water bij het vullen van de haven tijdens de vloed. De twee coëfficiënten $f_{1}$ en $f_{2}$ zijn in de orde van respectievelijk 0,01-0,03 en 0,1-0,25. Dit proces kan worden geïntegreerd over een getij en dat levert (Eysink (2004):

$$
v_{h}=f_{1} \times h_{0} \times b \times \frac{u_{0, \max }}{\pi}-f_{2} \times V_{t}
$$

waarbij $h_{0}$ de diepte van de haveningang ten opzichte van gemiddelde zeeniveau, $T$ de getijperiode en $u_{0, \max }$ de maximale snelheid van de getijrivier voor de haveningang (w_flow_velocity_maximum). Voor de coëfficiënten $f_{1}$ en $f_{2}$ zijn in de applicatie waarden aangenomen van respectievelijk 0,02 en 0,2 .

# 5.2.3 Uitwisseling ten gevolge van dichtheidverschillen 

Wanneer het water in de haven een lagere dichtheid heeft dan buiten de haven zal het water buiten de haven over de bodem de haven binnendringen en zo een wateruitwisseling genereren. Als het water buiten de haven een constante dichtheid heeft, dan zal dit een relatief kortstondig proces zijn totdat de haven en het langsstromende water dezelfde dichtheid hebben. Dit proces treedt dus alleen maar permanent op wanneer in de haven een zoetwaterafvoer plaatsvindt of als het langsstromende water varieert in dichtheid en dit kan voor getijdewateren het geval zijn. De uitwisseling wordt dan gedreven door de variatie in de dichtheid van het langsstromende water tijdens een getij. Dit kan komen door zout en temperatuurverschillen. Het proces is in de SILTHAR documentatie uitvoerig beschreven (Eysink, 2004). Het uitwisselende volume per getij is:

$$
V_{d}=V_{d 0} \times \frac{f_{4}}{f_{4, \max }}-f_{5} \times V_{t}
$$

waarbij:

$$
V_{d 0}=f_{4, \max } \times h_{0} \times b \times\left(\frac{\Delta \rho_{\max }}{\rho} \times g \times h_{0}\right)^{\frac{1}{2}} \times T
$$

$\Delta \rho_{\max }$ is het karakteristieke dichtheidsverschil dat om praktische redenen de helft is van de dichtheidvariatie binnen een getij van het langsstromende water. De gemiddelde dichtheid van het water is $\rho$. In deze beschrijving zijn 3 coëfficiënten opgenomen, $f_{4}, f_{4, \max }$ en $f_{5}$. De coefficient $f_{5}$ is afhankelijk van de verhouding $\frac{V_{d 0}}{V_{t}}$ en het faseverschil tussen de dichtheidsstroming en de getijstroom. Naarmate het faseverschil kleiner is neemt de invloed van de getijstroom toe en is $f_{5}$ groter. Ook neemt $f_{5}$ toe bij een grotere $\frac{V_{d 0}}{V_{t}}$. Volgens Eysink (2004) ligt $f_{5}$ tussen 0,1 en 1 . Voor een conservatieve benadering is in de immissietoets een waarde 1 aangenomen. Dit heeft tot gevolg dat het uitwisselend volume eerder onderschat wordt dan overschat, waardoor de concentratieverhoging eerder overschat wordt dan onderschat.

Voor $f_{4, \max }$ is door Eysink (2004) een waarde van 0,125 als gemiddelde schatting gegeven en ook blijkt uit de diverse case studies die zijn uitgevoerd dat de ratio $f 4 / f 4$, max altijd tussen 1,0 en 0,985 ligt. Een conservatieve aanname is dat $f_{4}=0,985 f_{4, \max }$.# 5.2.4 Totale uitwisseling op basis van SILTHAR 

Nadat de verschillende uitwisselingsvolumes zijn berekent kan het totale uitwisselingsdebiet worden berekend:

$$
V_{e}=V_{t}+V_{h}+V_{d}+V_{e f f}
$$

$V_{\text {eff }}$ vertegenwoordigt extra uitwisseling door doorstromende debieten in de haven die de verblijftijd nog verder reduceren.

### 5.2.5 Concentratieverdeling in de haven

Het uitwisselende debiet dat van het volume is afgeleid resulteert in een verlaging van de verblijftijd. Als de haven gezien wordt als een 1-dimensionaal bassin, dan volgt uit de verblijftijd en het effluentdebiet meteen een gemiddelde concentratie. Echter kan worden aangetoond dat dit een onderschatting kan opleveren van de concentratie omdat het effect van de uitwisseling in de haven niet overal gelijk is, maar bij de havenmond groter dan aan het eind van de haven. Dit kan worden beschreven door gebruik te maken van een plaatsafhankelijke effectieve dispersiecoëfficiënt en hier een analytische oplossing voor het concentratieprofiel van af te leiden.

De hier gepresenteerde beschouwing is die voor een haven die een uitwisselingsdebiet $Q$ met de omgeving heeft, waarin achter in de haven een continue lozing $W(\mathrm{~kg} / \mathrm{s})$ van een conservatieve stof plaatsvindt (Figuur 5.1), terwijl de achtergrondconcentratie buiten de haven 0 is. Als we deze situatie zouden weergeven als een eenvoudig boxmodel, met een doorstroming $Q$ dan is de resulterende concentratie. In werkelijkheid is te verwachten dat de verversing in de haven minder efficiënt is waardoor de gemiddelde concentratie $C$ hoger uitvalt dan $W / Q$. De effectiviteit is uit te drukken door een factor $\gamma$. Voor een goed gemengde haven (boxmodel) is $\gamma$ gelijk aan 1, terwijl de verwachting is dat deze in werkelijkheid minder dan 1 is.
![img-2.jpeg](img-2.jpeg)

Figuur 5.1: Definitie van geometrie en debieten in een haven

### 5.2.6 Schatting van factor $\gamma$

De factor $\gamma$ is slechts in een enkel geval bekend uit numerieke experimenten. Het is de bedoeling dat in de toekomst aanvullende numerieke experimenten zullen plaatsvinden. Op dit moment is de waarde van $\gamma$ niet meer dan een ruwe schatting.De hypothese is dat de factor $\gamma$ afhangt van de lengte-breedteverhouding van de haven; hoe langer een haven, hoe minder efficiënt het uitwisselingsdebiet en hoe lager de waarde van $\gamma$. Daarnaast speelt overduidelijk de aanwezigheid van dichtheidsstromen een rol. Uit de beschikbare numerieke experimenten is af te leiden dat een toename van het uitwisselingsdebiet door dichtheidsstroming met een factor van ruim 2 leidt tot een toename van $\gamma$ met ongeveer een factor 2 .

Voor de volgende analyse is aangenomen dat:
$\diamond \gamma$ hangt lineair af van $L_{h} / B_{h}$
$\diamond \gamma$ hangt lineair af $V_{e} /\left(V_{e}-V_{d}\right)$ (verder aangeduid als $\eta$ );

De lineaire afhankelijkheden zijn te beschouwen als een eerste schatting. Naarmate meer informatie beschikbaar komt kunnen deze, indien nodig, worden aangepast.

Uit de beperkte data volgt een eerste kwantificering van de afhankelijkheden:

$$
\gamma=1+(-0.237+0.0287 \times \eta) \frac{L_{h}}{B_{h}} \quad(0,01 \leq \gamma \leq 1)
$$

De ondergrens van $\gamma$ is bepaald door een willekeurige waarde om te voorkomen dat de dispersiecoëfficiënt nul kan worden. Een alternatief zou kunnen zijn om gebruik te maken van een functie die asymptotisch naar nul gaat als $L_{h} / B_{h}$ ook naar oneindig gaat. Dit vereist echter meerdere parameters waarvoor de onderbouwing op dit moment ontbreekt. Ook de relatie tussen de lengte/breedte verhouding en $\gamma$ is speculatief te noemen.

# 5.2.7 Bepaling van $D_{0}$ als functie van $\gamma$ 

Het boven geschetste diffusieprobleem kan op basis van de vergelijking van Fick als volgt analytisch worden uitgedrukt:

$$
W=-D(x) \cdot A_{h} \cdot \frac{d C}{d x}
$$

waarbij $A_{h}$ de (constant veronderstelde) dwarsdoorsnede voorstelt. Na substitutie van $\xi=$ $x / L$ en $D(\xi)=\xi D_{0}$ dajn volgt de oplossing:

$$
C(\xi)=-C_{0} \cdot \ln (\xi)=-\frac{W \cdot L_{h}}{D_{0} \cdot A_{h}} \ln (\xi)
$$

De over de haven gemiddelde concentratie is $C_{0}$. Door substitutie van $\gamma=W / Q / C_{0}$, volgt dan een schatting van $D_{0}$ als functie van $\gamma$ :

$$
D_{0}=\gamma \frac{Q_{e} \cdot L_{h}}{A_{h}}
$$

### 5.2.8 Afleiding van concentratieprofiel

Uit de vergelijking van Fick, gebruik makend van de lineaire afhankelijkheid van de dispersiecoëfficiënt in de haven volgt voor een lozing op positie $x$ in de haven ( $x$ is de afstand vanaf het eind van de haven, zie Figuur 5.1, de concentratie als functie van de afstand xtussen het lozingspunt en de haveningang ( $x>x_{l}$ waarbij $x_{l}$ de locatie van het lozingspunt is):

$$
\frac{d C\left(x-x_{l}\right)}{d x}=\frac{+Q_{l}\left(C\left(x-x_{l}\right)-C_{l}\right)}{A_{h} \frac{x-x_{l}}{L_{h}} D_{0}}
$$

$C_{l}$ is de concentratie van de stof in het effluent. Verder is aangenomen dat het debiet van de lozing klein is ten opzichte van het uitwisselingsdebiet zodat het advectieve transport dat door de lozing wordt gegenereerd ook verwaarloosbaar is. De dwarsdoorsnede van de haven A is constant verondersteld.

De oplossing van deze vergelijking is vervolgens:

$$
C(x)=C_{l}-K_{l}\left(x-x_{l}\right)^{K_{2}}
$$

met:

$$
K_{l}=\frac{\left(C_{l}-C_{a}\right)}{L^{K_{2}}}
$$

en

$$
K_{2}=\frac{Q_{l}}{\left(\frac{A}{L}\right) D_{0}}
$$

$C_{a}$ is de achtergrondconcentratie. Deze vergelijking geldt voor $x \geq x_{l}$ ( $x_{l}$ is de positie van het lozingspunt). Voor $x<x_{l}$ is de concentratie niet meer afhankelijk van $x$.

# 5.2.9 Invloed van andere lozingen in de haven 

Het komt regelmatig voor dat in een haven ook andere effluenten aanwezig zijn die de verblijftijd in de haven beïnvloeden. Gezien de mogelijke lange verblijftijden in havens kunnen de extra debieten een significante invloed hebben op de verhoging van de concentratie ten gevolge van de lozing. Om dit in te schatting is de mogelijkheid aanwezig om die extra debieten in de haven mee te nemen, aannemende dat de concentratie van de stof gelijk is aan de achtergrond. Dit extra debiet geeft dus het effect van een extra doorspoeling aan en leidt niet tot concentratieverhogingen. Het is bij de implementatie ook aangenomen dat dit extra debiet aan de kop van de haven geloosd wordt. De berekening van de menging maakt gebruik van de dezelfde afleiding als voor de lozing zelf. Beide mengfactoren worden vervolgens gecombineerd hetgeen leidt tot een longitudinaal concentratieprofiel in de haven. Deze combinatie is afgeleid door een massabalans :

$$
C(x)=\frac{\left(\frac{Q_{l}+Q_{a}}{M_{l}(x)}\right)\left(C_{l}(x)-C_{a}\right)}{\left(\frac{Q_{a}}{M_{a}(x)}+\frac{Q_{l}}{M_{l}(x)}\right)}+C_{a}
$$

De verhoging van de achtergrondconcentratie ter hoogte van het lozingspunt wordt vervolgens gecombineerd met de pluim/jet berekening (paragraaf 3.3) waarna de concentratie op de toetsafstand wordt afgeleid.# 6 Getij-uitwisseling 

Bij een lozing op een getijdewater zal accumulatie plaatsvinden ten gevolge van de eb- en vloedbeweging omdat geloosd effluent $\left(Q_{l}\right)$ na verloop van tijd weer langs het lozingspunt stroomt. De mate van accumulatie hangt af van het getij en de netto rivier afvoer $\left(Q_{a n}\right)$. Hoe groter de netto afvoer ten opzichte van de $\mathrm{eb}\left(Q_{a e}\right)$ en vloed $\left(Q_{a v}\right)$ beweging, des te kleiner de accumulatie. Benodigde gegevens zijn:
$\diamond$ Lozingsdebiet, $Q_{l}\left[\mathrm{~m}^{3} / \mathrm{s}\right]$;
$\diamond$ Netto afvoer, $Q_{a n}\left[\mathrm{~m}^{3} / \mathrm{s}\right]$;
$\diamond$ Gemiddeld eb- en vloeddebiet, $Q_{a e}$ en $Q_{a v}-Q_{a n}\left[\mathrm{~m}^{3} / \mathrm{s}\right]$;
$\diamond$ Breedte van het ontvangende water, $B_{w}[\mathrm{~m}] ; 6$
$\diamond$ Diepte van het ontvangende water, $D_{w}[\mathrm{~m}]$;
$\diamond$ Benedenstroomse limitatie eb afstand, $\operatorname{MaxLen}_{d s}[\mathrm{~m}]$.

The duration of the flood $T_{v}[s]$ :

$$
T_{v}=T_{L} \cdot \frac{\left(Q_{a e}-Q_{a n}\right)}{\left(Q_{a v}+Q_{a e}\right)}
$$

where $\mathrm{T}_{L}$ (44712 seconden) is de lengte van een dubbeldaags getij (12:25u).
Afgelegde afstand tijdens de vloed fase (in $m$ ):

$$
L_{v}=\frac{Q_{a v}}{\left(B_{w} \times D_{w}\right)} T_{v}
$$

Afgelegde afstand tijdens de eb fase (in $m$ ):

$$
L_{e}=\frac{Q_{a e}}{\left(B_{w} \times D_{w}\right)}\left(T d e S e c-T_{v}\right)
$$

Het aantal getijdes voor het bereiken van steady state accumulatie $N_{g}$ is berekend door:

$$
N_{g}=\frac{L_{v}}{\left(L_{e}-L_{v}\right)}
$$

Dit wordt naar boven afgerond op een geheel getal. Wanneer de eb en vloed afstand even groot zijn kan er geen menging worden uitgerekend.

Wanneer er een limiterende afstand $\mathrm{L}_{\max }$ is (bijvoorbeeld door een dwarstroming waardoor het water volledig wordt afgevoerd en niet terug kan komen) wordt het aantal getijdes aangepast door:

$$
N R_{g}=\left[\frac{L_{\max }}{\left(L_{e}-L_{v}\right)}\right]
$$

$\mathrm{NR}_{g}$ wordt op een geheel getal afgerond met een minimum van 1.Per getijslag wordt iteratief een cumulatieve menging berekend, uitgaande van de menging tijdens 1 getij. De menging tijdens de vloed $\left(M_{v}\right)$ en eb $\left(M_{e}\right)$ zijn resp:

$$
M_{v}=\frac{\frac{Q_{a c}}{4}+Q_{l}}{Q_{l}}
$$

en

$$
M_{e}=\frac{\frac{Q_{a c}}{4}+Q_{l}}{Q_{l}}
$$

De factor 4 is een veiligheidsfactor die is ingevoerd omdat er niet vanuit gegaan kan worden dat het effluent over de gehele breedte is gemengd. Er is hier dus aangenomen dat een kwart van het water beschikbaar is voor de menging. Deze factor 4 is ook consistent met de maximale breedte van de mengzone.

Voor het eerste volledige getij geeft dit een totale menging $\left(M_{1 e}\right)$ :

$$
\frac{1}{M_{1}}=\frac{1}{M_{v}}+\frac{1}{M_{e}}-\frac{1}{\left(M_{e} \times M_{v}\right)}
$$

Loop over alle getijslagen ( $\mathrm{n}=2$ tot $N_{g}$ ) voor uiteindelijke menging:

$$
\begin{aligned}
& \text { Vloedmenging: } \frac{1}{M_{n v}}=\frac{1}{M_{(n-1)}}+\frac{1}{M_{v}}-\frac{1}{\left(M_{(n-1) e} \times M_{v}\right)} \\
& \text { Ebmenging: } \frac{1}{M_{n}}=\frac{1}{M_{n v}}+\frac{1}{M_{e}}-\frac{1}{\left(M_{n v} \times M_{e}\right)}
\end{aligned}
$$

Als de noemer 0 is dan wordt de ebmenging gebruikt omdat de berekening niet kan worden uitgevoerd. Als de vloedmengfactor 1 is dan betekent dat er geen vloeddebiet is een ook dan wordt de ebmenging gebruikt om te voorkomen dat er geen menging meer is. Zodra de vloedmenging groter is dan 1 is er alleen een vloed debiet en kunnen de berekeningen worden uitgevoerd.# 7 Kust en zee 

Kustwateren en open zee verschillen van de in de vorige hoofdstukken genoemde wateren in die zin dat een berekening van de verhoging van de concentratie alleen goed kan worden geschat door gebruik te maken van geavanceerde modellen. Er kan echter wel een bovengrens worden aangegeven voor de concentratie in de mengzone. Deze is gebaseerd op een menging van het effluent met het volume van de mengzone met een verblijftijd die is afgeleid van het door de mengzone stromende debiet. Voor dit debiet wordt de restsnelheid gebruikt omdat die de netto verversing van het mengvolume vertegenwoordigt. De concentratie die hieruit is af te leiden vertegenwoordigt de maximale verhoging van de achtergrond.

De verdunning van het effluent in de mengzone is op basis van een eenvoudige massabalans:

$$
M_{k}=\frac{u_{r} \times 2 \times R_{\text {mengzone }} \times H_{\text {mengzone }}}{Q_{l}}
$$

Waarbij $u_{r}$ de reststroomsnelheid is, $R_{\text {mengzone }}$ de straal van de mengzone en $H_{\text {mengzone }}$ de dikte/diepte van de mengzone (zie Hoofdstuk 3). Dit geldt voor een lozing op open zee. Voor een lozing aan de kust is de maximale toegestane mengzone begrenst door de kustlijn waardoor de massabalans niet $2 \times R$ maar alleen $R$ bevat. De menging $M_{k}$ bepaalt de verhoging van de achtergrond in de mengzone. Hierna volgt nog een berekening van de concentratie in een pluim (of jet) waaruit de gecombineerde concentratie van achtergrondverhoging en pluim (of jet) volgt.# 8 Totale menging en eindconcentratie 

Voor elk type water vormt de eindconcentratie het resultaat van een pluimberekening of een berekening van de algemene menging van het effluent met achtergrond die al of niet gevolgd wordt door een pluimberekening. De algemene mengfactor $M_{a}$ is gedefinieerd als:

$$
M_{a}=1+\frac{Q_{a}}{Q_{l}}=\frac{Q_{l}+Q_{a}}{Q_{l}}
$$

met:
$\diamond$ Lozingsdebiet, $Q_{l}[\mathrm{~m} 3 / \mathrm{s}]$;
$\diamond$ Afvoer, $Q_{a}[\mathrm{~m} 3 / \mathrm{s}]$

Wanneer dit reeds gemengde water nog een keer gemengd wordt met het effluent met mengfactor $M_{p}$ (bijvoorbeeld door een pluimberekening), dan volgt uit een massabalans dat de totale mengfactor $M_{\text {tot }}$ gedefinieerd wordt door:

$$
\frac{1}{M_{t o t}}=\frac{1}{M_{a}}+\frac{1}{M_{p}}-\frac{1}{M_{a} \times M_{p}}
$$

De laatste term is onbelangrijk bij vrij grote mengfactoren (groter dan ....) maar is wel significant bij lage mengfactoren. Wanneer eenmaal totale menging op deze wijze is afgeleid, volgt de verhoging van de concentratie $\Delta C_{t}$ ten opzichte van de achtergrondconcentratie $\left(C_{w}\right)$ :

$$
\Delta C_{t}=\frac{C_{l}-C_{w}}{M_{t o t}}
$$

met:
$\diamond$ Concentratie effluent $C_{l}[\mathrm{~g} / \mathrm{l}]$;
$\diamond$ Achtergrond concentratie $C_{w}[\mathrm{~g} / \mathrm{l}]$;
$\diamond$ Verhoging concentratie (tov $C_{w}$ )na twee mengvormen, $\Delta C_{t}[\mathrm{~g} / \mathrm{l}]$;
achtergrondconcentratie $\left(C_{w}\right)$ :

$$
\Delta C_{t}=\frac{C_{l}-C_{w}}{M_{t o t}}
$$# 9 Koudwaterlozingen 

### 9.1 Inleiding

Voor Koudelozingen is een apart tabblad opgezet. De basis vergelijkingen voor menging zijn dezelfde als voor stoflozingen.

Dit betekent dat de pluimmenging met het oppervlaktewater hetzelfde is. Het kader voor de beoordeling is echter wel anders. Dit blijkt voornamelijk uit de beslisboom die wordt gehanteerd en de gegevens die nodig zijn om tot een beoordeling te komen. Veel velden zullen door de gebruiker moeten worden ingevuld omdat hier geen informatie aanwezig is in de database van de immissietoets. Het thermische lengteprofiel wordt vervolgens ook getoond als tweede deel van de verdunningsgrafiek.

Voor de verdere verspreiding van koudelozingen (verder dan de pluim berekeningen toelaat) wordt de warmte-uitwisseling met de atmosfeer belangrijk. Vandaar dat er een warmtebalans is toegevoegd om daar een inschatting van te geven. Hieruit volgt dan een thermisch lenteprofiel. Hiervoor wordt gebruikt gemaakt van het Nationaal Water Model (NWM), waarin een tracer is meegenomen (vergelijkbaar met de stoflozingen) waarin uitwisseling met de atmosfeer ook in is meegenomen. Voor de pluimberekeningen wordt op dit moment gebruik gemaakt van de 10\% lage afvoer.

### 9.2 Thermisch lengteprofiel

Het thermische lengteprofiel wordt uitgerekende aan de hand van een warmtebalans. De warmtebalans is:

$$
\rho \times C_{v} \times Q \times \frac{d T}{d x}=\lambda \times W \times\left(T-T_{e}\right)
$$

$\rho$ : dichtheid water $\left[\mathrm{kg} \cdot \mathrm{m}^{3}\right]$
$C_{v}$ : warmtecapaciteit water $\left[\mathrm{J} . \mathrm{kg}^{-1} .{ }^{\circ} \mathrm{C}^{-1}\right]$
$Q$ : rivierdebiet $\left[\mathrm{m}^{3} \cdot \mathrm{~s}^{-1}\right]$
$T$ : Water temperatuur $\left[{ }^{\circ} \mathrm{C}\right]$
$x$ : afstand stroomafwaards $[\mathrm{m}]$
$\lambda$ : Warmteuitwisselingscoefficient met de atmosfeer $\left[\mathrm{W} \cdot \mathrm{m}^{-2} \mathrm{C}^{-1}\right]$
$W$ : Breedte van rivier $[\mathrm{m}]$
$T_{e}$ : evenwichtstemperatuur met de atmosfeer $\left[{ }^{\circ} \mathrm{C}\right]$

Dit leidt tot een beschrijving van de temperatuur als functie van de afstand:

$$
T_{x}=\left(T_{0}-T_{e}\right) \times e^{\frac{-x}{L}}+T_{e}
$$

waarbij:

$$
L=\frac{\rho \times C_{v} \times Q}{\lambda \times W}
$$Als er de inname vanuit een ander waterlichaam is kan er geen recirculatie optreden en wordt het lozingsdebiet toegevoegd aan het ontvangende water waardoor het debiet waarmee het lengteprofiel wordt berekend verhoogt en wordt vergelijking 9.3:

$$
L=\frac{\rho \times C_{v} \times\left(Q+Q_{L}\right)}{\lambda \times W}
$$

Wanneer ddit lozingsdebiet $Q_{L}$ klein is ten opzichte van de afvoer $Q$ zullen beide nagenoeg hetzelfde resultaat geven.

De $T_{x}$ levert dan het thermische lengte profiel.

# 9.3 Bepaling van de dimensies van de mengzone 

Voor de beoordeling van de impact is een mengzone gedefinieerd door een lengte, dwarsdoorsnede en een oppervlakte. De grens van de mengzone is bepaald door het toegestane temperatuurverschil. De pluim berekening in de immissietoets levert alleen de menging als functie van de lengte. Het oppervlak en dwarsdoorsnede zullen nog moeten worden afgeleid.

Voor de dwarsdoorsnede (met een contour van het toegestane temperatuurverschil) kan worden afgeleid van een massabalans. Dit levert de maximale doorsnede op die je dan kunt vergelijken met de doorsnede van het ontvangende water. Hiervoor maken we gebruik van de benodigde menging om de het temperatuurverschil van het effluent met de achtergrond $(\Delta T)$ terug te brengen tot het toegestane temperatuurverschil $\left(\Delta T_{t}\right)$.

$$
M_{T_{t}}=\frac{\Delta T}{\Delta T_{t}}
$$

Om het effluent met een debiet van $Q_{L}$ te verdunnen is een rivierdebiet nodig van $Q_{r a}$. De dwarsdoorsnede die hiervoor nodig is hangt af van de doorsnede van de rivier (ontvangende water), $H \times W$ en het totale rivierdebiet $Q$ en dit vertaalt zich in :

$$
\frac{Q_{r a}+Q_{L}}{Q_{L}}=M_{T_{t}} \Rightarrow Q_{r a}=\left(M_{T_{t}}-1\right) \times Q_{L}
$$

De ratio van het benodigde debiet van de rivier en het actuele debiet van de rivier vertegenwoordigd het relatieve dwarsdoorsnede van de mengzone tov de dwarsdoorsnede van de rivier. Dit leidt tot een benodigde doorstromend oppervlak van:

$$
A_{M_{T_{t}}}=\frac{Q_{r a}}{Q} \times(H \times W)
$$

Met $Q$ het debiet van de rivier $\left(\mathrm{m}^{3} / \mathrm{s}\right)$. In het huidige kader wordt verwezen naar $50 \%$ van de natte doorsnede hetgeen bijvoorbeeld betekent:

Een rivier met $250 \mathrm{~m}^{2}$ doorsnede $(\mathrm{W}=25, \mathrm{H}=10 \mathrm{~m})$ en een debiet $(Q)$ van $15 \mathrm{~m}^{3} / \mathrm{s}$ een lozingsdebiet $\left(Q_{L}\right)$ van $1 \mathrm{~m}^{3} / \mathrm{s}$ en een temperatuurverschil tussen effluent en rivier van -14 graden (toegestane temperatuurverschil van 4) leidt tot een relatieve maximale doorsnede van $\left(A_{M_{T_{t}}}=a b s(-14) / 4=3.5\right.$, dus $Q_{r a}=(3.5-1) \times 1=2.5): \frac{Q_{r a}}{Q}=\frac{2.5}{15} \times$ $100 \%=16.7 \%$ en dit is minder dan de maximale $50 \%$.

Op deze wijze kan de dwarsdoorsnede van de mengzone worden afgeleid.Het oppervlak van de pluim kan dan vervolgens worden afgeleid uit een breedte $\left(\sqrt{A_{M_{T_{1}}}}\right)$ en de menglengte die door de pluim berekening wordt uitgerekend (L, de afstand tot de toegestane temperatuurverschil). Aannemende dat dit een gelijkbenige driehoek vormt wordt daarvan de oppervlak :

$$
A_{M_{o p p}}=\frac{W \times L}{2}
$$

Deze vergelijking gaat echter van uit dat de dimensies van de pluim niet wordt beperkt door de geometrie (dwarsdoorsnede) van het ontvangende water en de diepte groter is dan deze dimensie. Omdat in de handreiking wordt verwezen naar het epilimnion (oppervlaktelaag) ligt het voor de hand om dit ook mee te nemen bij de bepaling van de maximale dikte van de pluim. In de immissietoets is de waarde van spronglaag (indien $>0$ ) beschikbaar en vormt dan de limiet van de dikte van de pluim. Als er geen dikte gegeven is dan kan de waterdiepte als limiterend optreden. De dimensies van de pluim zijn altijd begrenst door de dimensies van het ontvangende water. Dit betekent dat indien de diepte (of spronglaag) kleiner is dan $\sqrt{A_{M_{T_{1}}}}$ de dikte van de pluim wordt begrenst door die diepte (ligging van de spronglaag) $H$. De breedte van de pluim wordt dan $W=A_{M_{\text {opp }}} / H$. Deze kan dan worden gebruikt om het oppervlak te bepalen van de driehoek va de menglengte en deze breedte. Het kan in theorie voorkomen dat dit uitkomt op groter dan de breedte van het ontvangende water, maar in dat geval is de doorsnede van de pluim altijd meer dan $50 \%$ en zal het niet door de desbetreffende beslisboom worden goedgekeurd.

# 9.4 Koudelozingen in havens 

### 9.4.1 Warmtebalansen

Ook in havens (dus zonder restdebiet) kunnen koudelozingen voorkomen. In deze gebieden is het debiet (wflow) 0 waardoor op dit moment voor het NWM deel geen resultaat mogelijk is, maar ook het berekenen van het thermische lengteprofiel is dan ook niet mogelijk. Binnen de pluim berekening kan dezelfde techniek wel worden gehanteerd als voor de stoffen, ook de verhoging van de achtergrond wordt dan in beginsel zonder uitwisseling met de atmosfeer berekend hetgeen wel een worst-case aanpak is. In de warmtebalans van het ontvangende segment kan daar wel voor worden gecorrigeerd door een warmte-uitwisselingscoëfficiënt, oppervlakte en diepte. De koppeling met het NWM is er dan nog niet, zodat er geen temperatuurkaart kan worden gegenereerd.

Voor een haven is de verblijftijd als volgt af te leiden:

$$
\tau=\frac{V_{s}}{Q_{L}+Q_{x}+Q_{a}}
$$

Met $Q_{L}$ het lozingsdebiet, $Q_{x}$ het uitwisselings debiet met het langsstromende water en $Q_{a}$ het additioneel debiet (allen in $\mathrm{m}^{3} / \mathrm{s}$ ).

In de immissietoets zijn er havens waarvan de verversingstijd in de database al bekend is (uit tracer berekeningen die in de modelsimulaties zijn meegenomen) en waar dit niet zo is en de uitwisseling met het langsstromende water is afgeleid met een zgn. Silthar berekening (Eysink (2004)). De berekeningen van Silthar leidt het totale uitwisselende debiet af, maar niet wat dit voor het lokale ontvangende segment betekent waardoor de door Silthar afgeleide debieten niet direct kunnen worden gebruikt voor de thermische balans van het ontvangende segment.

Voor elk segment wordt wel een verdunning of mengfactor $\mathrm{M}_{F}$ voor de berekening van de verhoging van de achtergrond afgeleid. Deze mengfactor berekening wordt gebuikt voor destoflozing. Hieruit kan het uitwisselingsdebiet worden afgeleid dat voor dit segment nodig is: $Q_{x}=Q_{L} \times\left(M_{f}-1\right)$. Hieruit volgt meteen dat de verblijftijd (verversingstijd) in dat segment kan worden uitgerekend door:

$$
\tau=\frac{V_{s}}{Q_{L} \times\left(1+M_{f}\right)}
$$

In havens zonder verversingstijd (met name de havens in Rotterdam) kan deze uit bestaande gegevens in de immissietoets worden afgeleid. Wanneer deze wel bekend is kan die bekende verversingstijd worden gehanteerd.

Voor het bepalen van de verblijftijd is het volume van het ontvangende segment wel van belang. Het oppervlak van dat segment is bekend voor de polygoon waar de lozing in plaatsvindt, de diepte ook dus daaruit volgt het volume. Als de inname wel uit de haven zelf komt dan veranderd niets aan de vergelijking, behalve dat er geen volume wordt toegevoegd door de lozing, dus $Q_{L}=0$.

Wanneer water dat wordt geloosd ook in dezelfde haven wordt ingenomen dan treedt recirculatie op. Dit kan schematisch worden weergegeven (figuur 9.1):
![img-3.jpeg](img-3.jpeg)

Figuur 9.1: Haven debieten en warmte transport bij recirculatie, $\Phi_{L}$ is de toegevoegde warmte

In eerste instantie gaan we er van uit dat de recirculatie komt door een lokale verhoging van de achtergrond, zoals bij de stoflozing uitgerekend wordt, wat warmtebalans betreft ziet deze er iets anders uit namelijk:

$$
Q_{x} \cdot \rho \cdot C_{v} \cdot \Delta T+Q_{L} \cdot \rho \cdot C_{v} \cdot \Delta T-Q_{L} \cdot \rho \cdot C_{v} \times\left(\Delta T+\Delta T_{L}\right)=0
$$

De warmtevracht van de lozing is $\Phi_{L}(\mathrm{~J} / \mathrm{s})$, en is gedefinieerd als $\Phi_{L}=\rho \cdot C_{v} \cdot \Delta T_{L} \cdot Q_{L}$, met $\Delta T_{L}$ de temperatuurverhoging tov de inname temperatuur. Als het water ingenomen wordt van een andere locatie dan wordt de recirculatiegraad 0 en de vergelijking:

$$
Q_{x} \cdot \rho \cdot C_{v} \cdot \Delta T+Q_{L} \cdot \rho \cdot C_{v} \cdot \Delta T-Q_{L} \cdot \rho \cdot C_{v} \times \Delta T_{L}=0
$$

Tot nu toe geldt dezelfde afleiding ook voor stoffen omdat er geen warmte-uitwisseling aanwezig is. De warmte/massabalans en de debieten die hiervan zijn afgeleid gaan er van uit dat het binnenkomende water van de uitwisseling $\left(Q_{x}\right)$ dezelfde temperatuur heeft als de achtergrond. Dit zou wellicht kunnen leiden tot een onderschatting van de temperatuurverandering in het segment omdat in de haven ook het binnenstromende water in dat segment al door de lozing zelf is beïnvloed. Echter, in de massabalans die is uitgewerkt (dat geld voor zowel stoffen als temperatuur) wordt uitgegaan van het theoretische concentratie profiel (stationaire oplossing) waarbij de concentraties als functie van de afstand tot de haveningang inclusief dit effect is (voor deze afleiding zie hoofdstuk 5.2.8) en dus correct. Het resultaat is dat de mengfactor, $M_{f}$, die is uitgerekend en waar de debieten van worden afgeleid gecorrigeerd zijn voor het terugstromen bij het uitwisselingsproces. Hierdoor kan de aanname worden gehanteerd dat dit terugstromende water inderdaad de achtergrondtemperatuur heeft.

De voorafgaande afleidingen is nog exclusief het effect van een warmte-uitwisseling met de atmosfeer. Om de warmte-uitwisseling te kunnen berekenen is de verblijftijd of verversingstijd nodig. Bij afwezigheid van de verversingstijd $\tau$, zoals in Rotterdam, kan deze $\tau$ worden uitgerekend op basis van de stofverspreiding via de mengfactor $M_{f}$ die bekend is. Daar kan dan de $Q_{x}$ van afgeleid worden zodat alle info bekend is om de uiteindelijke $\Delta T$ uit te rekenen. Om die warmte-uitwissing uit te rekenen is wel het oppervlakte van het segment $A_{\text {seg }}$ nodig omdat de verdwijnende warmteflux bepaald wordt door:

$$
\Phi_{a t m}=\lambda \times\left(T-T_{e}\right) \times A_{s e g}
$$

$\lambda$ is de warmte-uitwisselingscoëfficiënt en bedraagt $20 \mathrm{~W} / \mathrm{m}^{2}$ (conservatieve schatting die consistent is met die van het NWM).

Deze flux kan worden opgenomen in de warmtebalans en dit leidt dan tot:

$$
Q_{x} \cdot \rho \cdot C_{v} \cdot \Delta T+Q_{L} \cdot \rho \cdot C_{v} \cdot \Delta T-Q_{L} \cdot \rho \cdot C_{v} \times\left(\Delta T+\Delta T_{L}\right)+\lambda \times\left(T-T_{e}\right) \times A_{s e g}=0
$$

Dit wordt vereenvoudigd tot:

$$
Q_{x} \cdot \Delta T+Q_{L} \cdot \Delta T-Q_{L} \times\left(\Delta T+\Delta T_{L}\right)+\frac{\lambda \times(\Delta T) \times A_{s e g}}{\rho \cdot C_{v}}=0
$$

Hierin is aangenomen dat $\Delta T$ is gebaseerd op een achtergrond temperatuur van het water dat in evenwicht is met de lucht, dus een temperatuurverandering (zowel stijging als daling). Hieruit kan dan de temperatuur in het segment worden bepaald door:

$$
\Delta T=\frac{Q_{L} \cdot \Delta T_{L}}{Q_{x}+Q_{a}+\frac{\lambda \cdot A_{s e g}}{\rho \cdot C_{v}}}
$$

Zonder recirculatie wordt dit:

$$
\Delta T=\frac{Q_{L} \cdot \Delta T_{L}}{Q_{x}+Q_{a}+Q_{L}+\frac{\lambda \cdot A_{s e g}}{\rho \cdot C_{v}}}
$$

Hierbij is het eventuele additionele debiet ook meegenomen in de massabalans. Het resultaat van een dergelijke berekening is in een grafiek uitgewerkt Figuur (9.2) waarbij hier de onafhankelijke variabele de verblijftijd in dagen is.![img-0.jpeg](img-0.jpeg)

Figuur 9.2: Temperatuurverlaging met en zonder warmteuitwisseling ( $20 \mathrm{~W} / \mathrm{m}^{2}$ ) en met en zonder recirculatie. De $\Delta T_{L}$ is $-8^{\circ} \mathrm{C}$

# 9.4.2 Opzetten van het warmteprofiel in havens 

De berekeningen in het vorige hoofdstuk hebben betrekking op de verhoging van de achtergrond temperatuur zonder de directe pluimverspreiding, die komt daar nog bij zoals dat ook voor zoetwatersystemen is geïmplementeerd (dat dus door de applicatie als pluimmenging wordt bestempeld). De tweede stap is de omgevingsmenging die wordt berekend aan de hand van een thermische lengte profiel zoals dat al in hoofdstuk 9.2 is uiteengezet. Daarbij is een debiet en breedte nodig en wanneer de inname ook in de haven is dan is in beginsel is het netto debiet in een haven 0 en kan deze oplossing niet direct worden gebruikt.

Een methodiek kan wel worden opgezet wanneer de beschikbare karakteristieken en rekenresultaten voor het lozingssegment worden gebruikt. Binnen de huidige opzet van de applicatie zijn alle locatiesegmenten onafhankelijk van elkaar en is niet bekend welke segmenten bijvoorbeeld buursegmenten zijn. Een havenlengteprofiel kan op dit moment dus alleen worden afgeleid door gebruik te maken van de gegevens die bij het lozingssegment horen. Bij de gebruikte methode wordt geen rekening gehouden met de mogelijke complexiteit van de haven of uitstroom vanuit de haven naar het hoofdwatersysteem. Wanneer gebruik gemaakt wordt van een conservatieve aanpak dan geeft het resultaat dus een indruk van de maximale afstand waarover een lozing in de gegeven omstandigheden effect heeft. Wanneer de karakteristieken van het lozingssegment wordt toegepast op de segmenten, dan is een beste benadering om de karakteristieken van dat segment ook voor het thermische profiel te gebruiken. Dit kan dan worden ingezet door het profiel op te bouwen voor lengtes van het ontvangende segment en vergelijking 9.17 te gebruiken waarbij $\Delta T_{L}$ vervangen wordt door $\Delta T_{1}$, de berekende temperatuur van het segment waarin geloosd wordt. Hierbij moet ook een onderscheid gemaakt worden tussen met en zonderrecirculatie. Schematisch is het thermische profiel gebaseerd op figuur
![img-1.jpeg](img-1.jpeg)

Figuur 9.3: Overzicht van de methodiek voor het afleiden van het thermische profiel in havens

Het is dus een iteratieve berekenwijze. Voor segment $n$ kan uit figuur 9.3 een thermische balans worden afgeleid door:

$$
Q_{x} \cdot \rho \cdot C_{v} \cdot \Delta T_{n-1}=Q_{x} \cdot \rho \cdot C_{v} \cdot \Delta T_{n}+\lambda \cdot \Delta T_{n} \cdot A_{\text {seg }}
$$

en hieruit volgt dan inclusief recirculatie:

$$
\Delta T_{n}=\frac{Q_{x} \cdot \Delta T_{n-1}}{Q_{x}+\frac{\lambda \cdot A_{\text {seg }}}{\rho \cdot C_{v}}}
$$

In het uitwisselingsdebiet, zoals dat vanuit de verblijftijd is afgeleid, is het lozingsdebiet voor de segmenten $n>0$ niet meegenomen. Zonder recirculatie zal dus het lozingsdebiet moeten worden opgeteld om de massa en warmtebalans volledig te maken. Dan wordt de vorige vergelijking 9.19:

$$
\Delta T_{n}=\frac{\left(Q_{x}+Q_{L}\right) \cdot \Delta T_{n-1}}{Q_{x}+Q_{L}+\frac{\lambda \cdot A_{\text {seg }}}{\rho \cdot C_{v}}}
$$

Deze aanpak is consistent met hoe de de concentraties voor de stoflozingen in de havensegmenten worden afgeleid. Een beperking is wel dat dit alleen waardes oplevert voor een integer vermenigvuldiging van de lengte van het havensegment (oftewel het oppervlakte gedeeld door de breedte dat door de gebruiker is ingevoerd), waardoor een vrij groffe discretisatie in de afstand optreedt. Er wordt ook geen rekening gehouden met een mogelijke complexere geometrie van de haven.

# 9.4.3 Recirculatie in andere wateren# 9.4.3.1 Recirculatie in andere wateren met complexere waterbeweging 

De methodiek zoals die voor havens is afgeleid is ook toepasbaar voor wateren waar voor de segementen een verversingstijd beschikbaar is (dus die met een tracer zijn berekend). De (worst-case) aanname is dat wel dat het inname punt ook in het lozingssegment zit (dat hoeft niet perse zo te zijn). Als dat niet zo is dan is er geen recirculatie (daar zou dan een vinkje in opgenomen kunnen worden?). Voor dit type water (exclusief de havens) kan voor de verdere verspreiding van het koude water (inclusief de recirculatie ) op dezelfde wijze gekoppekd worden aan de NWM segmenten. Dus de temperatuurverlaging aan het eind van de mengzone wordt gebruikt als input voor het NWM. Voor lijnvormige wateren met 1 stromingsrichting gaat dit niet omdat er geen verversingstijd beschikbaar is voor het lozingssegment en de recirculatie graad op een andere manier berekend moet worden.

### 9.4.3.2 Rivieren en ander lijnvormige wateren met 1 stromingsrichting

Wanneer in een oppervlakte water ingenomen wordt en met een lagere temperatuur geloosd wordt kan er ook recirculatie optreden. Voor wateren waarin een achtergrond menging wordt berekend kan dezelfde methodologie worden gebruikt als in haven. En hierbij kan dan ook worden verwezen naar vergelijking 9.16. Dit geldt in beginsel wanneer aangenomen wordt dat de inname in het zelfde segment plaats vindt als de lozing zelf. Wanneer dit niet het geval is en er alleen een lozing plaatsvindt, dan kan vergelijking 9.17 worden toegepast. Dus zolang de verblijftijd bekend is kan dit worden bepaald voor elk watersysteem. De verblijftijd in een segment wordt niet door de lokale recirculatie beinvloed. Immers, de verblijttijd wordt bepaald door het uitstromende debiet en het volume van het segment, en dat verandert niet bij recirculatie. Dit betekent dat voor alle segmenten waar een achtergrondconcdentratie verhoging voor stoffen wordt berekend, dezelfde aanpak kan worden gehanteerd, omdat voor die wateren voor het segment waarin de warmtelozing plaatsvindt, de verversingstijd bekend is en dit bepaald de recirculatie zoals ook in havens is berekend. Voor wateren waar geen verblijttijd wordt berekend is dit echter niet het geval. Er kan immers recirculatie optreden wanneer het debiet van de inname (bovenstrooms van het lozingspunt) groter wordt dan de rivierafvoer. Er vindt dan tussen het lozingspunt en innamepunt een terugstroom plaats die het tekort vanuit de rivier aanvult. Met andere woorden, de recirculatiestroom wordt dan $Q_{L}-Q$, waarbij $Q_{L}$ groter is dan $Q$. Wanneer de afstand tussen inname en lozing bekend is in combinatie met de breedte van het ontvangende water verminderd de recirculatie door de warmetuitwisseling met de atmosfeer en kan de uiteindelijke lozingstempertuur (verschil met de achtergrond) worden afgeleid:

$$
\Delta T_{L e}=\Delta T_{i n}+\Delta T_{L}
$$

met de innametemperatuur $\Delta T_{i n}$ inclusief de recirculatie en rekening houden met het termische profiel tussen lozingspunt en innamepunt (zie vergelijking 9.2). Hierbij kan dan wel worden opgemerkt dat $Q_{L}$ in vergelijking 9.3 wordt vervangen door $Q-Q_{L}$ :

$$
L_{r}=\frac{\rho \times C_{v} \times\left(Q_{L}-Q\right)}{\lambda \times W}
$$

De temperatuur van het terugstromende water bij de inlaat na menging met de rivierafvoer wordt dan (het inlaatdebiet $Q_{L}$ is groter dan de rivierafvoer $Q$ ):

$$
\Delta T_{i n}=\frac{Q_{L}-Q}{Q_{L}} \cdot \Delta T_{L e} \cdot e^{-\frac{v}{L_{r}}}
$$

De combinatie van vergelijkingen 9.21 met vergelijking 9.23 levert dit uiteindelijk:

$$
\Delta T_{L e}=\frac{\Delta T_{L}}{1-\frac{Q_{L}-Q}{Q_{L}} \cdot e^{-\frac{v}{L_{r}}}}
$$De $\Delta T_{L e}$ is de effluent temperatuur (de $Q_{L}$ verandert niet) die uiteindelijk wordt geloosd en als startpunt dient voor de rest van de koudelozing berekeningen. In beginsel zijn alle gegevens bekend. Mocht er geen info zijn over de afstand tussen het inname en lozingspunt, dan kan deze ook op 0 gezet worden waardoor de vergelijking vereenvoudigd wordt omdat de temperatuur bij de inlaat enkel het resultaat is van de menging van de rivier afvoer en het terugstromende debiet.# Bibliography 

Delvigne, G., 1979. "Round buoyant jet with three-dimensional trajectory in ambient flow." 18th Congress of the IAHR, Cagliari, Italy .

Eysink, W., 2004. "SILTHAR Version 4.2 - A mathematical program for the computation of siltation in harbour basins." Report 8.6520, Delft Hydraulics, Delft .

Graaf, J. van de en R. Reinalda, 1977. "Horizontale uitwisseling in samengetrokken modellen." Report S0061, Waterloopkundig Laboratorium, Delft .

Hattum, B. van, A. Baart en J. Boon, 2002. " Computer model to generate predicted environmental concentrations (PECs) for antifouling products in the marine environment - 2nd edition accompanying the release of Mam-Pec Version 1.4." Report number E-0204/Z3117, IVM, Vrije Universiteit, Amsterdam .

IJff, J., 2000. "Emissie-immissie: prioritering van bronnen en de immissietoets (juni 2000)." CIW werkgroep Emissies en diffuse bronnen (werkgroep VI) .# A Testinstructie 

## A. 1 Inleiding

Bij eke aanpassing van de applicatie wordt deze getest, maar voor het interface zijn geen automatische testen beschikbaar, vandaar deze testinstructie. De applicatie heeft 3 tabbladen:

1 Stoflozing
2 Temperatuurlozing
3 Informatie

Het is aan te raden om bij het testen de cache eerst te legen zodat nog aanwezige restanten van een vorige versie het gedrag van de applicatie kunnen beïnvloeden. Wanneer de applicatie wordt opgestart zal het versienummer in de bovenste balk zichtbaar zijn. IN dit document wordt gebruik gemaakt van een specifiek voorbeeld, maar het verdient aanbevelingen om verschillende watertypes te selecteren en te testen.

## A. 2 Stoflozing

Open de website van de immissietoets (de publieke site is: www.immissietoets.nl)
![img-2.jpeg](img-2.jpeg)

Figuur A.1: Informatieblad

Het startscherm wordt zichtbaar (figuur A.1) en de eerste stap is het selecteren en invullen van de gegevens voor de basisberekening.

De eerste stap voor het uitvoeren van de berekeningen is het selecteren van een locatie en dat gebeurt door in te zoomen en met de muis te klikken op een locatie (zoals hieronder al is gedaan). Selecteren kan alleen wanneer de segmenten zichtbaar worden, dus er moet voldoende worden ingezoomed, zie figuur A.2.![img-3.jpeg](img-3.jpeg)

Figuur A.2: Informatieblad

In de figuur is in de info box aangegeven (geen onderdeel van het interface) dat een aantal kaartlagen kunnen worden geselecteerd (indien beschikbaar), dit heeft voor de applicatie verder geen consequenties. In dit voorbeeld is een locatie gekozen in de Nieuwe Waterweg. Het nummer van de locatie is hier 3836. Na het selecteren verschijn aan de rechterkant van het scherm het menu voor het in- en aanvullen van resterende gegevens. Voor atrazine zijn ook metingen beschikbaar die zijn aangegeven en in dit voorbeeld is locatie 200102 geselecteerd (en dit geeft een concentratie van $0.0033 \mu \mathrm{~g} / \mathrm{l}$. Het invoerveld voor de stof kijkt ook naar of de tekst in de naam voorkomt (als een filter). Wanneer bijvoorbeeld allen 'atra' is ingevuld verschijnen er 4 stoffen (dd: 2-2-24) waaruit kan worden geselecteerd.
$\diamond$ atraton
$\diamond$ atrazine
$\diamond$ desethylatrazine
$\diamond$ desisopropylatrazine

Als er voor een stof meetpunten beschikbaar zijn kan dat op een vergelijkbare manier worden gekozen via de drop-down lijst, of door het klikken op de locatie van het meetpunt.

1 kies een stof. Er is een lijst en door een stofnaam in te toetsen verschijnen de mogelijke stoffen (er wordt op sub-strings gezocht), kies atrazine

2 De JG-MKN wordt opgehaald uit de database, de gebruiker kan de waarde aanpassing indien noodzakelijk, er verschijnt dan aan de rechterkant een icoon die kan worden aangeklikt om de database waarde te herstellen

3 Debiet en concentratie van het effluent invullen
4 kies een beschikbaar meetpunt voor de achtergrond concentratie door een punt te selecteren (zichtbaar op de kaart). Meetpunt 17914 levert een achtergrondconcentratie van $0.0057 \mu \mathrm{~g} /$

5 klik op de knop "resultaten". Een basisberekening wordt uitgevoerd en de beslisboom wordt zichtbaar onder de invoerdata.De naam van het waterlichaam verschijnt als KRW Waterlichaam. Er kan gekozen worden voor een ander waterlichaam als daar specifieke redenen voor zijn.

Na de eerste berekening verschijnt de beslisboom onder Resultaten met daarin de effluent en triviaaltoets. Ook zichtbaar onder de kaart worden de invoervelden voor de geavanceerde berekening (figuur A.3):
![img-4.jpeg](img-4.jpeg)

Figuur A.3: Invoerscherm voor de geavanceerde berekening

De meeste informatie wordt opgehaald uit de achterliggende database. Wel moet nog worden ingevuld:

1 dichtheid van de lozing (hier $1000 \mathrm{~kg} / \mathrm{m} 3$ )
2 de diameter van de lozingspijp (hier 0.5 m )
3 de ligging van de pijp in de horizontaal als de verticaal (hier aan de oever en aan het oppervlak). Hier is een beperkte keuze voor beschikbaar via een drop-down lijst met de default 'Oever' en 'Oppervlak'.Wanneer geen gebruiker gedefinieerde afstand wordt opgegeven wordt de toetsafstand afgeleid van de dimensies van het ontvangende water (hier niet ingevuld). Voor een ingevuld scherm zie figuur A. 4
![img-5.jpeg](img-5.jpeg)

Figuur A.4: Beslisbloom voor de geavanceerde berekening

Indien beschikbaar is de MAC MKN voor de gekozen stof ingevuld en een veld dat weergeeft welke norm dit is (bijvoorbeeld 'Andere oppervlaktewateren wettelijke MAC-MKN (totaal) (zout water)')

Druk op de knop "geavanceerde berekening" en een geavanceerde berekening wordt uitgevoerd en genereert een beslisboom zoals hierboven in figuur A. 4 aangegeven. In de uitvoer zijn nog een aantal knoppen zichtbaar: Drinkwater inname: Wanneer op deze knop wordt gedrukt dan verschijnt de volgende tabel met de uitkomsten van de drinkwatertoets (figuur A.5):Resultaten

| BESL1SBOOM | DRINKWATER INNAME | GRAFIEKEN | LOOS | PSP |
| :-- | :-- | :-- | :-- | :-- |

# Drinkwater concentraties bij innamepunten 

| Locatie | Concentratie verhooging [ug/l] | Achtergrondconcentratie [ug/l] | Totale concentratie [ug/l] | Volstart aan norm |
| :-- | :-- | :-- | :-- | :-- |
| Rotterdam, Reijervraard, Nive Maas | 0.263 | 0.006 | 0.268 | Ja |
| Noodınlaat Kralingen | 0.252 | 0.003 | 0.255 | Ja |
| Noodınlaat Berenplaat | 0 | 0.005 | 0.005 | Ja |
| Middelharnis | 0 | 0.005 | 0.005 | Ja |
| Biesbosch | 0 | 0.005 | 0.005 | Ja |
| Hendrik-lido-Ambacht, Noord | 0 | 0.007 | 0.007 | Ja |
| Scheethoek | 0 | 0.009 | 0.009 | Ja |
| Heel | 0 | 0.005 | 0.005 | Ja |
| Brakel | 0 | 0.005 | 0.005 | Ja |
| Andijk | 0 | 0.003 | 0.003 | Ja |
| Roosteren, Maas | 0 | 0.005 | 0.005 | Ja |
| Langenik, De Steeg, Lek | 0 | 0.008 | 0.008 | Ja |
| Bergambacht, C.Rodeirhuis, Lek | 0 | 0.005 | 0.005 | Ja |
| Noodinnemepunt Bergambacht | 0 | 0.005 | 0.005 | Ja |
| Lekkerkerk, Schuwacht \& Tiendweg, Lek | 0 | 0.006 | 0.006 | Ja |
| Nieuwersluis | 0 | 0.002 | 0.002 | Ja |
| Nieuwegein | 0 | 0 | 0 | Ja |
| Noodınlaat Baarnioek | 0 | 0 | 0 | Ja |
| Zwolle, Engelse Werk, IJssel | 0 | 0 | 0 | Ja |
| Nieuw-Lekkerland, De Put, Lek | 0 | 0 | 0 | Ja |

Laatste correcte berekening om: 11:28:34 18-01-2024
Figuur A.5: Drinkwater tabel

Ook wordt een grafiek gegenereerd met het verloop van de concentratie als functie van de afstand tot het lozingspunt.

## Resultaten

BESL1SBOOM
DRINKWATER INNAME
GRAFIEKEN

## Grafische weergave pluim

![img-6.jpeg](img-6.jpeg)

Laatste correcte berekening om: 11:28:34 18-01-2024

Figuur A.6: Concentratie als functie van de afstand tot het lozingspunt

Er is ook een log uitvoer waarin in detail kan worden gekeken naar details van berekeningsresultaten. Deze is met name bedoeld om in detail te onderzoeken welkegetallen zijn gebruikt en voor expert analyse als dat nodig is. Met de knop kan een pdf uitvoer worden gegenereerd waarin alle in en uitvoer van de berekeningen zijn opgenomen. Deze kan lokaal op een computer worden opgeslagen.

Er zal goed gekeken moeten worden of alle gewenste velden aanwezig zijn en de uitvoer correct. Tevens wordt er ook een log gegenereerd en is het mogelijk om een pdf van het volledige resultaat (in- en uitvoer) van de immissietoets te genereren.

# A. 3 Temperatuurlozing 

Bij het selecteren van de tab temperatuurlozing verschijnt een scherm dat vergelijkbaar is met de stoflozing tab. Als vanuit een geselecteerd gebied in stoflozing wordt overgestapt naar de temperatuur tab, dan blijf de locatie selectie in stand.
![img-7.jpeg](img-7.jpeg)

Figuur A.7: Scherm van de temperatuur tab na selectie

Specifieke data zal nog moeten worden ingevuld. In dit voorbeeld is de diameter van 0.5 m gekozen en onder het kopje Temperatuur is een lozing van -8 graden (ten opzichte van het ontvangende water) gekozen. Let op dat ook naar de zoutconcentratie moet worden gekeken omdat deze bij default op 0 staat. In beginsel is de zoutconcentratie gelijk aan die van het ontvangende water maar moet die wel worden ingevuld, tenzij het proces de zoutconcentratie verandert of de inname uit een ander watersysteem wordt gehaald (dus de zoutconcentratie afwijkt).

In het voorbeeld van figuur A. 7 is dezelfde locatie gekozen (3836).
Na het uitvoeren van de berekening wordt het volgende scherm zichtbaar. Zaak is om te controleren dat alle velden inderdaad aanwezig zijn.![img-8.jpeg](img-8.jpeg)

Figuur A.8: Temperatuur invoer en resultaat scherm

In versie 1.13 .1 is de beslisboom niet meer zichtbaar omdat die niet meer actueel is en in de loop van 2024 zal worden vervangen. In plaats daarvan wordt de 'Resultaten' tab met daarin een grafiek getoond. Wanneer de aangegeven locatie is gekozen wordt een watertype O geselecteerd. Om echter een resultaat te krijgen zal een selectie gemaakt moeten worden en in dit geval is gekozen voor "Grote rivieren(R8)".

In de grafiek is het toegestane verschil (in dit geval 4 graden) grijs aangegeven.
Er wordt ook een kaar gegenereerd met daarin aangegeven hoe groot het gebied is dat door de koudelozing wordt beïnvloed.
![img-9.jpeg](img-9.jpeg)

Figuur A.9: Indicatie van het gebied dat door de koudelozing wordt beïnvloed# A. 4 Informatie 

Dit tabblad geeft algemene inhoudelijke informatie over de applicatie.
![img-10.jpeg](img-10.jpeg)

Figuur A.10: Informatieblad

Aan het eind van de pagina is een link opgenomen die verwijst naar de IPLO site om vragen in te kunnen dienen.

Contact: Vraag het onze experts | Informatiepunt Leefomgeving (iplo.nl)

Deze link verwijst naar: https://iplo.nl/contact/vragenformulier/ en deze link kan dan ook worden getest of inderdaad naar een bestaand adres wordt verwezen.