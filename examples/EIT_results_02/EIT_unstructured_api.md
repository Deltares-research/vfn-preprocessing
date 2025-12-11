

# Immissietoets webapplicatie

# Technische beschrijving

F.M. Kleissen

Versie: 0.2  Revisie: ----

1 juli 2025



# Immissietoets webapplicatie, Technische beschrijving

Gepubliceerd en gedrukt door: Deltares  Boussinesqweg 1  2629 HV Delft  Postbus 177  2600 MH Delft  Nederland telefoon: +31 88 335 82 73  e-mail: Informatie  www: Deltares Verkoop: telefoon: +31 88 335 81 88  e-mail: Verkoop  www: Verkoop & Ondersteuning Ondersteuning: telefoon: +31 88 335 81 00  e-mail: Ondersteuning  www: Verkoop & Ondersteuning Copyright © 2025 Deltares Alle rechten voorbehouden. Niets uit deze uitgave mag worden verveelvoudigd in enige vorm door middel van druk, fotokopie, microfilm of op welke andere wijze dan ook, zonder voorafgaande schriftelijke toestemming van de uitgever: Deltares.



# Inhoudsopgave

| L1 | L2 | Value |
| --- | --- | --- |
| Lijst van figuren |  | iv |
| Woordenlijst |  | 1 |
| 1 | Inleiding | 3 |
| 2 | Definitie van de maximale toegestane mengzone | 4 |
| 3 | Near-field berekeningen met Jet3D en Fisher diffusie | 7 |
|  | 3.1 | Inleiding | 7 |
|  | 3.2 | Pluimverspreiding volgens de zoete toets (Fisher diffusie) | 8 |
|  | 3.3 | Jet3D | 10 |
| 4 | Algemene berekeningen | 11 |
|  | 4.1 | Begrip mengfactor | 11 |
|  | 4.2 | Eenvoudige menging | 11 |
| 5 | Berekening van stofconcentraties in havens | 12 |
|  | 5.1 | Havens met een gegeven verblijftijd | 12 |
|  | 5.2 | Havenuitwisseling zonder verblijftijd middels SILTHAR | 13 |
|  | 5.2.1 | Uitwisseling door het getij | 13 |
|  | 5.2.2 | Uitwisseling door neervorming | 13 |
|  | 5.2.3 | Uitwisseling ten gevolge van dichtheidsverschillen | 14 |
|  | 5.2.4 | Totale uitwisseling op basis van SILTHAR | 15 |
|  | 5.2.5 | Concentratieverdeling in de haven | 15 |
|  | 5.2.6 | Schatting van factor γ | 15 |
|  | 5.2.7 | Bepaling van D0als functie van γ | 16 |
|  | 5.2.8 | Afleiding van concentratieprofiel | 16 |
|  | 5.2.9 | Invloed van andere lozingen in de haven | 17 |
| 6 | Getij-uitwisseling | 18 |
| 7 | Kust en zee | 20 |
| 8 | Totale menging en eindconcentratie | 21 |
| 9 | Koudwaterlozingen | 22 |
|  | 9.1 | Inleiding | 22 |
|  | 9.2 | Thermisch lengteprofiel | 22 |
|  | 9.3 | Bepaling van de dimensies van de mengzone | 23 |
|  | 9.4 | Koudelozingen in havens | 24 |
|  | 9.4.1 | Warmtebalansen | 24 |
|  | 9.4.2 | Opzetten van het warmteprofiel in havens | 27 |
|  | 9.4.3 | Recirculatie in andere wateren | 28 |
|  | 9.4.3.1 | Recirculatie in andere wateren met complexere waterbeweging | 29 |

ii



INHOUDSOPGAVE

<table class="TableOfContents"><tbody><tr><span>9.4.3.2</span><span>Rivieren en ander lijnvormige wateren met 1 stromingsrichting</span><span>29</span></tr><tr><span>A</span><span>Testinstructie</span><span>32</span></tr><tr><span>A.1</span><span>Inleiding</span><span>32</span></tr><tr><span>A.2</span><span>Stoflozing</span><span>32</span></tr><tr><span>A.3</span><span>Temperatuurlozing</span><span>37</span></tr><tr><span>A.4</span><span>Informatie</span><span>39</span></tr></tbody></table>

Deltares iii



# Lijst van figuren

<table class="TableOfContents"><tbody><tr><li>2.1</li><li><p>Definitie van de maximaal toegestande mengzone, M</p><sub>z</sub></li><li>5</li></tr><tr><li>3.1</li><li>Uitwerking diffusie volgens Fisher</li><li>9</li></tr><tr><li>5.1</li><li>Definitie van geometrie en debieten in een haven</li><li>15</li></tr><tr><li>9.1</li><li><p>Haven debieten en warmte transport bij recirculatie, Φ</p><sub>L</sub><p>is de toegevoegde warmte</p></li><li>25</li></tr><tr><li>9.2</li><li><p>Temperatuurverlaging met en zonder warmteuitwisseling (20 W/m</p><sub>2</sub><p>) en met en zonder recirculatie. De ΔT</p><sub>L</sub><p>is -8 °C</p></li><li>27</li></tr><tr><li>9.3</li><li>Overzicht van de methodiek voor het afleiden van het thermische profiel in havens</li><li>28</li></tr><tr><li>A.1</li><li>Informatieblad</li><li>32</li></tr><tr><li>A.2</li><li>Informatieblad</li><li>33</li></tr><tr><li>A.3</li><li>Invoerscherm voor de geavanceerde berekening</li><li>34</li></tr><tr><li>A.4</li><li>Beslisbloom voor de geavanceerde berekening</li><li>35</li></tr><tr><li>A.5</li><li>Drinkwater tabel</li><li>36</li></tr><tr><li>A.6</li><li>Concentratie als functie van de afstand tot het lozingspunt</li><li>36</li></tr><tr><li>A.7</li><li>Scherm van de temperatuur tab na selectie</li><li>37</li></tr><tr><li>A.8</li><li>Temperatuur invoer en resultaat scherm</li><li>38</li></tr><tr><li>A.9</li><li>Indicatie van het gebied dat door de koudelozing wordt beïnvloed</li><li>38</li></tr><tr><li>A.10</li><li>Informatieblad</li><li>39</li></tr></tbody></table>

Deltares iv



# Woordenlijst

C

    v warmtecapaciteit water [J.kg

    -1
   
.°C

    -1
   
].

    22
   
,

    23
   
,

    25
   
,

    26
   
,

    28
   
,

    29 Q

    a additioneel debiet [m

    3
   
.s

    -1
   
].

    24
   
,

    26 L afstand tot de toegestande temperatuurverschil [m].

    24 Q

    ra benodigde rivierdebiet [m

    3
   
.s

    -1
   
].

    23 W breedte van de rivier [m].

    22–24
   
,

    29 H waterdiepte in de rivier [m].

    23
   
,

    24 A

    Mrt benodigd doorstroomend oppervlak [m

    2
   
].

    23 T

    e evenwichtstemperatuur met de atmosfeer [°C].

    22
   
,

    26 ΔT

    in innametemperatuurverschil [°C].

    29 L

    r karakteristieke lengte [m].

    29 T

    x het thermische lengte profiel, temperatuur [°C] als functie van de afstand x.

    22
   
,

    23 Q

    L lozingsdebiet [m

    3
   
.s

    -1
   
].

    23–26
   
,

    28–30 M

    F mengfactor [-].

    25
   
,

    26 A

    Mopp benodigd doorstroomend oppervlak [m

    2
   
].

    24 Q rivierdebiet [m

    3
   
.s

    -1
   
].

    22
   
,

    23
   
,

    29 A

    seg segmentoppervlak [m

    2
   
].

    26
   
,

    28 V

    s segmentvolume [m

    3
   
].

    24
   
,

    25 T

    0 temperatuur bij lozingspunt na volledige menging [°C].

    22 x afstand stroomafwaarts [m].

    22
   
,

    29 M

    T1 de benodigde menging om de het temperatuurverschil van het effluent met de achtergrond terug te brengen tot het toegestane temperatuurverschil [-].

    23
   
,

    24 ΔT

    L temperatuurverschil van het effluent met de achtergrond/verschil tov inname [°C].

    iv
   
,

    25–27
   
,

    29 ΔT

    n temperatuurverschil in volume/segment n [°C].

    28 ΔT temperatuurverschil [°C].

    23
   
,

    25
   
–

    28 ΔT

    t toegestane temperatuurverschil [°C].

    23 ΔT

    Le uiteindelijke lozingstemperatuur (verschil met achtergrond) [°C].

    29
   
,

    30 Q

    x uitwisselingsdebiet [m

    3
   
.s

    -1
   
].

    24–26
   
,

    28 τ verblijftijd [s].

    24–26 Φ

    atm warmteflux met atmosfeer [W/m

    2
   
].

    26 λ Warmteuitwisselingscoefficient met de atmosfeer [W.m

    -2
   
°C

    -1
   
].

    22
   
,

    23
   
,

    26
   
,

    28
   
,

    29

Deltares 1 van 39



# Woordenlijst

Φ

    L warmtevracht lozing [J/s].

    iv, 25 ρ dichtheid water [kg.m

    3
   
].

    22, 23, 25, 26, 28, 29 T Water temperatuur [°C].

    22, 26

Deltares 2 van 39



# 1 Inleiding

De webapplicatie van de immissietoets is een eerste stap in de beoordeling van individuele lozingen. Lozingen van stoffen (in een effluent) worden beoordeeld volgens het Handboek Immissietoets. Koudelozingen worden beoordeeld volgens het STOWA stappenplan : (https://www.stowa.nl/sites/default/files/assets/PUBLICATIES/Publicaties%202021/STOWA%202021-30%20koudelozingen%20stappenplan.paspx) . De webapplicatie (www.immissietoets.nl) zal bij standaard gebruik een conservatieve aanpak hanteren, hetgeen betekent dat de effecten door de applicatie worden overschat. Het gevolg is dat de applicatie geen conclusie zal trekken dat een lozing niet is toegestaan. Indien volgens de gebruikte berekening niet aan de criteria kan worden voldaan, dan zal een vervolgonderzoek moeten uitwijzen of een lozing al dan niet vergundbaar i

De applicatie heeft op dit moment twee werkgebieden, te weten:

Stoflozingen Koudelozing

De stoffen die met een effluent worden geloosd worden als conservatief beschouwd, dus zonder afbraakprocessen. Voor koudelozing is dat voor het eerste deel (de pluimverspreiding) ook zo, maar voor dit werkgebied is ook toegevoegd een inschatting van de invloed van een koudelozing en hierbij wordt een conservatieve schatting van de warmteuitwisseling met de atmosfeer meegenomen.

Deltares 3 van 39



# 2 Definitie van de maximale toegestane mengzone

De definitie van het begrip mengzone is gebaseerd op de definitie zoals die de Kaderrichtlijn water is geïntroduceerd. Directive 2008/105/EC Article 4 introduceert mengzones als volgt: Member States may designate mixing zones adjacent to points of discharge. Concentrations of one or more substances listed in Part A of Annex I may exceed the relevant EQS within such mixing zones if they do not affect the compliance of the rest of the body of surface water with those standards Met het begrip “mengzone” wordt in dit document de maximale toegestane mengzone (MTMZ) bedoeld en de grootte van MTZT is afhankelijk van het watertype en dimensies van het ontvangende water. Ter verduidelijking is dit niet hetzelfde als de initiële mengzone die hier is gedefinieerd als dat gebied van pluimverspreiding tot het punt waarbij de de pluim het oppervlak (of bodem/kant) raakt. Hoe dit punt wordt bepaald hang af van welke rekenmethode wordt gebruikt (Jet3D versus Fisher). De pluim zelf kan dan worden gerelateerd aan het gebied tot het punt waarop de menging niet meer toeneemt, dus een maximale menging heeft bereikt. De berekeningen van de webapplicatie van de immissietoets bestaat uit een pluimberekening (middels eenvoudige modelberekeningen) en meer algemene mengberekeningen. Wanneer in het kader van de webapplicatie de pluim de bodem, het oppervlak of een van de oevers raakt is dit in beginsel de initiële menging. Voor het voorstel van de definitie van de mengzone zijn de oppervlaktewateren in verschillende typen onderscheiden:

Zoet water (saliniteit minder dan 0,5 PSU): Rivier/kanaal; Meer; Estuaria en getijrivieren met een restdebiet; Doodlopende kanaalpanden en havens (zonder restdebiet); Aan de oevers van brede estuaria, zeearmen en Waddenzee/ Eems-Dollard met duidelijk aanwijsbare getijgeulen; Aan de kust van de open zee; Open zee.

In beginsel wordt uitgegaan van een mengzone die een cirkel beslaat met een maximum straal van 500m. De ligging van het lozingspunt in de cirkel varieert, afhankelijk van de condities. De algemene vorm, grootte en ligging ten opzichte van het lozingspunt is globaal aangegeven in Figuur 2.1. Verder zijn er nog een aantal bijzonderheden en extra beperkingen.

Deltares 4 van 39



# Definitie van de maximaal toegestane mengzone

Diagram of mixing zone Figuur 2.1: Definitie van de maximaal toegestande mengzone, M z

De mengzones zijn als volgt gedefinieerd: Ad 1: De breedte van de mengzone wordt beperkt tot ¼ van de breedte van het ontvangende water met een maximum van 1000m. De gehele mengzone bevindt zich stroomafwaarts van het lozingspunt, omdat de stroming in dit type water slechts 1 richting kent. Voor meren geldt de huidige definitie breedte mengzone (CIW, 2000): Hierbij is A is oppervlak, L is lengte en B is breedte van het meer. Het huidige maximum is 1000m, maar hier wordt voorgesteld om de maximale afstand vanaf het lozingspunt voor meren te beperken tot 500m, gelijk aan de eerder gedefinieerde maximum straal, waardoor de definitie van de mengzone strenger is dan huidige definitie maar wel consistent is met de definitie in andere watertypen. Ad 2: Mengzone is hetzelfde gedefinieerd als voor zoet. Echter, de ligging van het lozingspunt binnen de mengzone varieert, afhankelijk van de verhouding tussen het vloevolume en ebvolume. Zonder netto afvoer zijn deze twee gelijk (verhouding =1) en dan ligt het lozingspunt precies in het centrum van de mengzone (met een maximum straal van 500m). Als het vloevolume nul is dan is de mengzone precies hetzelfde gedefinieerd als voor zoet water. De toetsing vindt dan plaats op de rand van de mengzone met de grootste afstand tot het lozingspunt, hetgeen in praktijk betekent in de richting van de netto afvoer (zeewaarts). Ad 3: Aan het eind van een haven kunnen de criteria worden versoepeld, afhankelijk van de doelstelling van dit waterlichaam. Voor een van te voren vastgesteld deel van de haven wordt een minimale waterkwaliteit nagestreefd, zoals een minimale zuurstofconcentratie van 3 of 4 mg/l. Tevens mag 25 m van het lozingspunt de ER niet worden overschreden (inclusief de verhoging van de achtergrond door ophoping van het effluent) om acute problemen te voorkomen. Voor welk deel dit wordt toegestaan is een relatief arbitraire beslissing, maar zou gebaseerd kunnen zijn op een maximum percentage van de haven, en/of een maximum volume en/of maximum oppervlak, gebaseerd op een halve cirkel met een straal van 500m. Dit deel van de haven geldt vanaf het verste punt in de haven. De mengzone voor een haven zal nog in detail moeten worden ingevuld. Ad 4: Een zelfde definitie als voor getijdewateren wordt gehanteerd, maar de dimensies van

5 van 39



# Definitie van de maximale toegestane mengzone

het ontvangen de water waar de mengzone op wordt gebaseerd zijn de dimensies en andere
      karakteristieken van de geul bij laagwater. Als de lozing tijdens laag water op een
      drooggevallen plaat plaatsvindt, dan zullen andere criteria gehanteerd worden. Daar wordt in
      de definitie van de mengzone geen uitspraak over gedaan. Ad 5: Aan de kust geldt een zelfde mengzone als voor estuaria, dus een halve cirkel met een
      straal van 500m. Ad 6: Bij een diepte van 30 m of meer geldt dat de mengzone een straal heeft van 150 m
      rondom het lozingspunt en een dikte (diepte) van 30m. Dit vertegenwoordigt een volume
      van 2.106 m3. Voor dieptes minder dan 30 m, maar meer dan 5 m geldt dat de straal wordt
      afgeleid van de diepte en het toegestane volume. Voor bijvoorbeeld 10 m diepte zou dit
      een straal van 250 m betekenen. Bij minder dan 5 m wordt de maximale straal van 500 m
      gehanteerd. Dit geldt overigens niet als het een lokale diepte betreft, zoals een (getij)geul. De webapplicatie berekend op basis van de de definitie van het ontvangen de water (het
      watertype) de maximaal toegestane mengzone waarop getoetst wordt. Hierbij wordt geen
      rekening gehouden met het eventueel overlappen met een beschermd gebied.

Voor acute toxiciteit is een mengzone afgeleid de maximale 25 m gehanteerd is voor een
      ontvangen de water waarvoor een maximale mengzone geld van 1000m. De MAC afstand
      wordt evenredig kleiner naarmate de mengzone kleiner is, dus 0.25 * M t . De concentratie
      wordt getoetst aan de toegestane concentratie, de MAC waarde (Maximum Aanvaardbare
      Concentratie). Voor de bestaande zoete toets wordt voor het ER niveau (Ernstig Risico)
      wordt een maximale afstand van 25 m gehanteerd (0.25 * B waterlichaam ≤ 25 m). Het ligt
      dan voor de hand om voor zoute wateren in eerste instantie ook deze verhouding 0.25 * B
      waterlichaam met een maximum van 25 m als mengzone te hanteren.

Deze keuze kan in praktijk betekenen dat voor kleinere mengzones dit nagenoeg gelijkwaardig
      is aan het hanteren van de MAC als concentratielimiet in het effluent. Bijvoorbeeld, een
      lozing op een smal watersysteem, bijvoorbeeld 10 m, resulteert in een lengte voor de MAC-
      mengzone van 2,5 m. Over een dergelijke afstand treden in het algemeen slechts kleine
      verdunningsfactoren op.

Deltares 6 van 39



# 3 Near-field berekeningen met Jet3D en Fisher diffusie

# 3.1 Inleiding

Er zijn in de applicatie twee soorten pluimberekeningen beschikbaar. De eerste is de pluimberekening, die ook al wordt toegepast binnen het kader van de zoete toets (Iff (2000)). Deze berekening houdt echter geen rekening met dichtheidsverschillen tussen effluent en ontvangende water of met verticale dichtheidsgradiënten in het ontvangende water. Deze kunnen het verspreidingsgedrag van de pluim significant beïnvloeden. Vandaar dat ook een pluimverspreidingsmodel, dat met dergelijke dichtheidsverschillen rekening kan houden, in het instrument is opgenomen. Dit is het model Jet3D dat door het toenmalige Waterloopkundig Laboratorium is ontwikkeld (Delvigne (1979)) en wordt toegepast wanneer het dichtheidsverschil tussen lozing en ontvangende water groter is dan 1 kg/m 3 .

Voor beide pluimberekeningen is de maximale menging begrensd door de hoeveelheid water dat beschikbaar is voor menging. Dit is bepaald door de eenvoudige menging waarbij een massabalans de maximale menging uitrekent op basis van het beschikbare debiet (rivierafvoer) en lozingsdebiet (zie Hoofdstuk 4.2). De lozing kan plaatsvinden op verschillende posities in het ontvangende water. Om het gebruik van de applicatie zo eenvoudig mogelijk te houden is gekozen om die positie in het oppervlaktewater te beperken tot:

Positie van de lozing = horizontaal 1 = midden 2 = oever Positie van de lozing = vertikaal 1 = top (oppervlakte) 2 = midden (halverwege de diepte) 3 = bodem.

Jet3D kan met optie 3 (lozing bij de bodem) rekenen, CIW-Fisher gaat er van uit dat resultaat van pluim aan top (1) gelijk is aan resultaat aan bodem (3) (er is immers geen dichtheidsverschil) De pluimberekening (zowel Jet3D als Fisher en de combinatie van beide) loopt door tot de toetsafstand (de berekende m_mixingzone_ya_length, afhankelijk van het type en dimensies van het ontvangende water) is bereikt. Op die toetsafstand wordt de menging van de pluim gebruikt in combinatie met de achtergrondmenging. In havens is het zo dat een pluim berekening niet meer verder kan als de pluim de haven uitgaat en in een langstromend water terecht komt. De hydrodynamica gaat dan significant afwijken van het water waarin wordt geloosd en dan is de pluimberekening niet meer relevant. Vandaar ook dat in havens de m_mixingzone_ya_length wordt gelimiteerd tot de afstand van het lozingspunt tot de haven mond (w_distance_effluent_to_harbour_entrance). Deze laatste afstand is gekoppeld aan het haven segment (dus 1 waarde voor elk segment in de haven). Dit afkapmechanisme van de mixingzonelength vindt plaats voor zowel havens met als zonder tracer.

7 van 39 Deltares



Near-field berekeningen met Jet3D en Fisher diffusie

# 3.2 Pluimverspreiding volgens de zoete toets (Fisher diffusie)

De beschrijving van de berekeningen zijn in de documentatie van de zoete toets opgenomen 
    ( IJff (2000) ). Bij deze berekening wordt een onderscheid gemaakt in:

Een situatie waarbij in eerste instantie sprake is van een uitstroom in de vorm van een 
      jet die vervolgens overgaat in een tweedimensionale pluim; Een situatie waarbij de uitstroom direct plaatsvindt in de vorm van een 
      driedimensionale pluim die daarna overgaat in een tweedimensionale pluim.

Welke van deze twee condities gelden is afhankelijk van de verhouding tussen de 
    uitstroomsnelheid en de stroomsnelheid van het ontvangende water. De berekening is 
    uitgewerkt volgens onderstaande figuur 3.1 .

Deltares 8 van 39



Near-field berekeningen met Jet3D en Fisher diffusie

graph TD;
          A[Invoergegevens (uit werkblad "immissietoets") Waterysteem: type, debiet, breedte, lengte (meer) Lozing: debiet, pijpdiameter] --> B{is uitstroom in eerste instantie een jet of een pluim?};
          B -->|als: 4 * π * sqrt(D_y * D_z) / α * Q_lozing > 1| C[eerst 3D-pluim daarna 2D-pluim];
          B -->|als: 4 * π * sqrt(D_y * D_z) / α * Q_lozing < 1| D[eerst jet daarna 2D-pluim];
          C --> E[De overgang van de 3D-pluim naar de 2D-pluim vindt plaats op: x_max = 4 * π * D_z / u_opp * h^2];
          E --> F[De menging in de 3D-pluim als functie van x is: M = x * 3D-pluim / α * Q_lozing];
          F --> G[De menging in de 2D-pluim als functie van x is: M = x * 2D-pluim / α * Q_lozing];
          D --> H[Als de waterdiepte geen beperkende factor is geschiedt de overgang van de jet naar de pluim op een afstand benedenstrooms van het lozingspunt gelijk aan: x_jet / x_max = 7 * l_lozing / V_lozing];
          H --> I[Als de bodem of het wateroppervlak wel een beperkende factor is vindt de overgang plaats op een afstand: x_jet(b/o) / x_max = h * D_lozing / 0.107];
          I --> J[Voor verdere berekening wordt de laagste van deze waarden aangehouden: x_jet = min(x_jet / x_max, x_jet(b/o) / x_max)];
          G --> K[De menging in de jet als functie van x is: M = x / 5.6 * l_lozing];
          K --> L[De menging in de 2D-pluim als functie van x is: M = x * 2D-pluim / α * Q_lozing];
          L --> M[met: x_jet / x_max = x * l_lozing / 5.6];
          M --> N[x_schuil = 4 * π * u_opp * D_y];

Figuur 3.1: Uitwerking diffusie volgens Fisher

Dit figuur komt uit IJff (2000)

Deltares 9 van 39



# 3.3 Jet3D

Voor situaties waar dichtheidsverschillen een rol spelen in de verspreiding van de pluim is het pluimverspreidingsmodel Jet3D beschikbaar (Delvigne (1979)). Dit model is in de jaren 70 door het toenmalig Waterloopkundig Laboratorium ontwikkeld en beschrijft de drie-dimensionale verspreiding van een ronde pluim met een dichtheid die kan afwijken van het ontvangende water. Het ontvangende water kan een niet-uniform verticaal dichtheidprofiel en een niet-uniform snelheidsprofiel hebben. Dit model is nodig in situaties die niet door de ‘zoete’ pluimberekening kunnen worden gesimuleerd vanwege optredende dichtheidsverschillen. Zonder de significante initiele dichtheidsverschillen wordt de Fisher pluimverspreiding gebruikt zodat de resultaten voor dergelijke situaties (rivieren en kanalen met stroming) overeenkomen met de oorspronkelijk berekeningen met het spreadsheet dat oorspronkelijk ontwikkeld was ten behoeve van de immissietoets (IJff (2000)). Het model beschrijft de pluim vanaf het moment dat het effluent de pijp verlaat. De berekeningen stoppen wanneer de rand van de mengzone is bereikt of wanneer de pluim de bodem of wateroppervlak of een van beide oevers raakt. In de applicatie stopt de berekening ook wanneer de diameter van de pluim groter wordt dan de diepte of de breedte van het ontvangende water.

Als de Jet3D berekening stopt voordat de rand van de mengzone is bereikt worden de gegevens overgenomen door de 2D berekening die ook in de zoete pluimberekening is opgenomen. Hierbij wordt ervoor gezorgd dat er geen discontinuïteit optreedt in de verdunning van de pluim door de diepte die in de 2D berekening wordt gebruikt aan te passen en in de verdere berekening constant te houden.

Er is nog wel een opmerking te maken ten aanzien van een gestratificeerd ontvangend water. Wanneer het ontvangende water is gestratificeerd met een spronglaag (dus niet een lineair geinterpoleerde verticale dichtheidgradient) dan wordt de jet in een waterlaag geloosd met de dikte van de laag die qua dichtheid het laagste verschil geeft met de dichtheid van het geloosde effluent. Dan wordt dus kunstmatig de diepte aangepast. (Dit is een conservatieve aanname). Dit heeft overigens geen effect op de verhoging van de achtergrond concentratie (ter hoogte van het lozingspunt).

Deltares 10 van 39



# 4 Algemene berekeningen

# 4.1 Begrip mengfactor

In de rekentechnieken die in de applicatie zijn opgenomen worden mengfactoren berekend.
      De mengfactor die voor het effluent kan worden afgeleid is het resultaat van het samenvloeien
      van verschillende stromingen en is gedefinieerd vanuit een eenvoudige massabalans. De mengfactor is berekend door:

$M_f = \frac{Q_r + Q_a + Q_l}{Q_l}$

(4.1)

Waarbij Q_r is het rivierdebiet, Q_a ander debiet door het watersysteem en Q_l het lozingsdebiet
      (allen in m^3/s). Deze mengfactor kan ook worden afgeleid vanuit de de concentraties van het effluent en de
      achtergrond en het bereikte concentratieverschil:

$M_f = \frac{C_l - C_a}{\Delta C}$

(4.2)

Waarbij C_l en C_a de concentratieverandering na menging met een mengfactor M_f. Vanuit
      de in de berekende mengfactoren wordt vervolgens de concentratie na menging berekend.
      In de applicatie van de immissietoets wordt gebruik gemaakt van een algemene menging
      en een pluim verspreiding. De berekening van de algemene menging is afhankelijk van het
      watertype. Voor de pluimberekening worden twee modellen toegepast, te weten het Jet3D
      model, wanneer er een significant dichtheidsverschil is tussen effluent en ontvangende water,
      en het Fisher model wanneer dat niet zo is. De eindconcentratie op de toetsafstand is een
      combinatie van de algemene menging en de pluimmenging (zie hoofdstuk 8)

# 4.2 Eenvoudige menging

De berekening is beschikbaar voor watersystemen die goed gemengd zijn waardoor er een
      verhoging van de achtergrondconcentratie (\Delta C) ten gevolge van de lozing optreedt. Dit geld
      voor beken, kanalen, rivieren. Deze massabalans wordt ook toegepast op andere
      oppervlakte wateren, zoals getijdewateren en meren om de verhoging van de
      achtergrondconcentratie te berekenen, volgens vergelijking 4.1. Deze menging wordt dan
      gecombineerd met het resultaat van de pluimmenging.

Deltares 11 van 39



# 5 Berekening van stofconcentraties in havens

Voor de berekening van pluim concentraties in havens zijn twee methodes toegepast. De eerste is door gebruik te maken van verblijftijden die uit modelberekeningen zijn afgeleid (de zogenaamde tracer berekeningen). De tweede is om de uitwisseling tussen de haven en het voorbijstromende water te berekenen en daaruit de concentraties ten gevolge van een lozing in de haven af te leiden.

# 5.1 Havens met een gegeven verblijftijd

Deze methode om de achtergrondconcentratieverhoging ten gevolge van een lozing in een haven te bepalen maakt gebruik van de resultaten van modelsimulaties van tracers. Deze methode wordt ook voor andere wateren gebruikt en is gebaseerd op tracer berekening met het achterliggende hydrodynamische model (zoals Delft3D of SOBEK). Uitgangspunt is een haven met een tracerconcentratie van 1 en een concentratie van 0 in het hoofdwatersysteem, waarna het model de afname van de tracer concentratie ten gevolge van de uitwisseling tussen de haven en het hoofdwatersysteem berekent. De haven wordt vervolgens in een aantal deelgebieden opgedeeld. De afnemende concentratie als functie van de tijd in een deelgebied bepaalt de verversingstijd voor dat deelgebied. Deze verversingstijd wordt dan gebruikt om de verhoging van de achtergrondconcentratie in een deelgebied ten gevolge van een effluent lozing in dat gebied te berekenen. Om de berekening binnen de webapplicatie te vereenvoudigen en toepasbaar te maken wordt aangenomen:

de concentratie in de gedefinieerde deelgebieden neemt exponentieel af (deze aanname is equivalent met de aanname dat de deelgebieden volledig gemengd zijn); de te beoordelen lozing beïnvloedt de hydrodynamica in de haven niet significant.

Bij een exponentiële aanname geldt voor elk segment (deelgebied) dat de verversingstijd kan worden uitgedrukt als T = V/Q , met Q het ‘verversingsdebiet’ en V het volume van het deelgebied. Als een effluent, bestaand uit debiet Q_l en concentratie C_l , in een deelgebied loost, dan kan via een massabalans de evenwichtsconcentratie in dat deelgebied worden berekend.

Als een mogelijk andere debiet ( Q_a ) die niet in de hydrodynamische modelberekeningen is meegenomen, omdat het bijvoorbeeld andere industriële lozingen betreft die relatief klein zijn, dan kan deze lozing wel in de massabalans worden meegenomen.

Dan wordt aangenomen wordt dat deze andere lozing zich bovenstrooms van de lozingslocatie of in hetzelfde subgebied bevindt (benedenstrooms van de lozing heeft het geen direct effect op de verversingstijd ter hoogte van de effluentlozing). Dit wordt in de aanpak met de SILTHAR berekeningen (zoals op dit moment ook in de webapplicatie is opgenomen) ook aangenomen. Als vervolgens wordt aangenomen dat de concentratie van deze andere lozing 0 is en in het deelgebied volledig is gemengd dan volgt uit de massabalans:

$C_l/C = \left(\frac{V}{T} + Q_l + Q_a\right)/Q_l$

(5.1)

Deltares 12 van 39



Berekening van stofconcentraties in havens



Deze beschrijving geldt indien de achtergrondconcentratie nul is. Wanneer deze groter is dan 0, dan wordt in de berekeningen niet de effluentconcentratie gebruikt, maar het verschil in concentratie tussen het effluent en het ontvangende water. Deze verversingsberekeningen worden alleen gebruikt als in de onderliggende database de afgeleide gegevens (verversingstijden) voor de betreffende havensegmenten zijn opgeslagen. Als deze gegevens niet aanwezig zijn, dan wordt de SILTHAR methode toegepast. De verhoging van de achtergrondconcentratie in het deelgebied waar wordt geloosd wordt vervolgens gecombineerd met de pluim/jet berekening (paragraaf 4.1) waarna de concentratie op de toetsafstand wordt afgeleid.

# 5.2 Havenuitwisseling zonder verblijftijd middels SILTHAR

Havens en doodlopende kanaalpanden hebben geen zoetwaterafvoer die het water in de haven kan verversen. Effluent dat in havens wordt geloosd kan alleen maar verdunnen als er een transport is vanuit de haven naar de uitgang van de haven. Dit transport kan bestaan uit diffusie/dispersion in combinatie met uitwisseling van water in de haven met het water daarbuiten. De uitwisseling zorgt voor de verversing in de haven (en een verlaging van de verblijftijd) terwijl de diffusie/dispersion processen de concentratiegradiënten in de haven bepalen. In de webapplicatie zijn twee berekeningen opgenomen om menging in havens en de uitwisseling met het hoofdwatersysteem te beschrijven. De in dit hoofdstuk 5.2 gepresenteerde methode is gebaseerd op de uitwisselingsprocessen die zijn afgeleid uit het SILTHAR model (Eysink (2004)). Ook in MAMPEC worden dezelfde formuleringen gebruikt (Van Hattum et al. (2002)). Een tweede methode die in paragraaf 5 is uitgewerkt is afgeleid uit modelresultaten waarbij een tracer is gebruikt om de verversingssnelheid in vooraf gedefinieerde (haven)segmenten te bepalen. Voor uitwisseling tussen het water in de haven en het voor de ingang van de haven langsstromende (getijde)rivierwater zijn drie processen bepaald:

Uitwisseling door het getij; Uitwisseling door neervorming; Uitwisseling ten gevolge van dichtheidsverschillen tussen het water in en buiten de haven.

# 5.2.1 Uitwisseling door het getij

Het uitwisselingsvolume ten gevolge van het getij is het zogenaamde getijvolume en is bepaald door de verticale getijslag ( H_g ) en het oppervlak van de haven ( B_h \times L_h ):

$V_t = H_g \times B_h \times L_h$

(5.2)

# 5.2.2 Uitwisseling door neervorming

Door stroming langs de ingang van de haven of doodlopend kanaal ontstaat neervorming die wateruitwisseling tussen de haven en het langsstromende water genereert. Dit proces is beschreven door (Van de Graaf en Reinalda (1977)):

$$
Q_h = f_1 \times h \times b \times u_0 - f_2 \times Q_t
$$

(5.3)

13 van 39



Berekening van stofconcentraties in havens



met h en b de hoogte en breedte van de haveningang, u 0 de stroomsnelheid voor de ingang en Q t het debiet van het binnenstromende water bij het vullen van de haven tijdens de vloed. De twee coëfficiënten f 1 en f 2 zijn in de orde van respectievelijk 0,01-0,03 en 0,1-0,25. Dit proces kan worden geïntegreerd over een getij en dat levert (Eysink 2004):

$v$

h = f 1 × h 0 × b ×

u

    0,max

/ π - f 2 × V t

waarbij h 0 de diepte van de haveningang ten opzichte van gemiddelde zeeniveau, T de getijperiode en u 0,max de maximale snelheid van de getijrivijer voor de haveningang (w_flow_velocity_maximum). Voor de coëfficiënten f 1 en f 2 zijn in de applicatie waarden aangenomen van respectievelijk 0,02 en 0,2.

# 5.2.3 Uitwisseling ten gevolge van dichtheidsverschillen

Wanneer het water in de haven een lagere dichtheid heeft dan buiten de haven zal het water buiten de haven over de bodem de haven binnendringen en zo een wateruitwisseling genereren. Als het water buiten de haven een constante dichtheid heeft, dan zal dit een relatief kortstondig proces zijn totdat de haven en het langstromende water dezelfde dichtheid hebben. Dit proces treedt dus alleen maar permanent op wanneer in de haven een zoetwaterafvoer plaatsvindt of als het langstromende water varieert in dichtheid en dit kan voor getijdwateren het geval zijn. De uitwisseling wordt dan gedreven door de variatie in de dichtheid van het langstromende water tijdens een getij. Dit kan komen door zout en temperatuurverschillen. Het proces is in de SILTHAR documentatie uitvoerig beschreven (Eysink, 2004). Het uitwisselende volume per getij is:

$V$

d = V 0 ×

f

    4

/

f 4,max

- f 5 × V t waarbij:

$V$

0 = f 4,max × h 0 × b × (

Δρ

    max

/ ρ × g × h 0 )

1/2

× T

Δρ max is het karakteristieke dichtheidsverschil dat om praktische redenen de helft is van de dichtheidvariatie binnen een getij van het langstromende water. De gemiddelde dichtheid van het water is ρ. In deze beschrijving zijn 3 coëfficiënten opgenomen, f 4 , f 4,max en f 5 . De coëfficiënt f 5 is afhankelijk van de verhouding V

     d / V 0 en het faseverschil tussen de dichtheidsstroming en de getijstroom. Naarmate het faseverschil kleiner is neemt de invloed van de getijstroom toe en is f 5 groter. Ook neemt f 5 toe bij een grotere V

     d / V 0 . Volgens Eysink (2004) ligt f 5 tussen 0,1 en 1. Voor een conservatieve benadering is in de immissietoets een waarde 1 aangenomen. Dit heeft tot gevolg dat het uitwisselend volume eerder onderschat wordt dan overschat, waardoor de concentratieverhoging eerder overschat wordt dan onderschat.

Voor f 4,max is door Eysink (2004) een waarde van 0,125 als gemiddelde schatting gegeven en ook blijkt uit de diverse case studies die zijn uitgevoerd dat de ratio f 4 /f 4,max altijd tussen 1,0 en 0,985 ligt. Een conservatieve aanname is dat f 4 = 0,985f 4,max .

14 van 39 Deltares



# 5.2.4 Totale uitwisseling op basis van SILTHAR

Nadat de verschillende uitwisselingsvolumes zijn berekent kan het totale uitwisselingsdebiet worden berekend:

$V_e = V_i + V_h + V_d + V_eff$

(5.7) V_eff vertegenwoordigt extra uitwisseling door doorstromende debieten in de haven die de verblijftijd nog verder reduceren.

# 5.2.5 Concentratieverdeling in de haven

Het uitwisselende debiet dat van het volume is afgeleid resulteert in een verlaging van de verblijftijd. Als de haven gezien wordt als een 1-dimensionaal bassin, dan volgt uit de verblijftijd en het effluentdebiet meteen een gemiddelde concentratie. Echter kan worden aangetoond dat dit een onderschatting kan opleveren van de concentratie omdat het effect van de uitwisseling in de haven niet overal gelijk is, maar bij de havenmond groter dan aan het eind van de haven. Dit kan worden beschreven door gebruik te maken van een plaatsafhankelijke effectieve dispersiecoëfficiënt en hier een analytische oplossing voor het concentratieprofiel van af te leiden. De hier gepresenteerde beschouwing is die voor een haven die een uitwisselingsdebiet Q met de omgeving heeft, waarin achter in de haven een continue lozing W (kg/s) van een conservatieve stof plaatsvindt (Figuur 5.1), terwijl de achtergrondconcentratie buiten de haven 0 is. Als we deze situatie zouden weergeven als een eenvoudig boxmodel, met een doorstroming Q dan is de resulterende concentratie . In werkelijkheid is te verwachten dat de verversing in de haven minder efficiënt is waardoor de gemiddelde concentratie C hoger uitvalt dan W/Q. De effectiviteit is uit te drukken door een factor γ . Voor een goed gemengde haven (boxmodel) is γ gelijk aan 1, terwijl de verwachting is dat deze in werkelijkheid minder dan 1 is.

Diagram of geometry and flow rates in a harbor Figuur 5.1: Definitie van geometrie en debieten in een haven

# 5.2.6 Schatting van factor γ

De factor γ is slechts in een enkel geval bekend uit numerieke experimenten. Het is de bedoeling dat in de toekomst aanvullende numerieke experimenten zullen plaatsvinden. Op dit moment is de waarde van γ niet meer dan een ruwe schatting.

Deltares 15 van 39



Berekening van stofconcentraties in havens



De hypothese is dat de factor γ afhangt van de lengte-breedteverhouding van de haven; hoe langer een haven, hoe minder efficiënt het uitwisselingsdebiet en hoe lager de waarde van γ. Daarnaast speelt overduidelijk de aanwezigheid van dichtheidsstromen een rol. Uit de beschikbare numerieke experimenten is af te leiden dat een toename van het uitwisselingsdebiet door dichtheidsstroming met een factor van ruim 2 leidt tot een toename van γ met ongeveer een factor 2. Voor de volgende analyse is aangenomen dat:

γ hangt lineair af van L h /B h ; γ hangt lineair af van V e /(V e − V d ) (verder aangeduid als η);

De lineaire afhankelijkheden zijn te beschouwen als een eerste schatting. Naarmate meer informatie beschikbaar komt kunnen deze, indien nodig, worden aangepast. Uit de beperkte data volgt een eerste kwantificering van de afhankelijkheden:

$γ = 1 + (−0.237 + 0.0287 × η) L$

h /B h (0, 01 ≤ γ ≤ 1) (5.8)

De ondergrens van γ is bepaald door een willekeurige waarde om te voorkomen dat de dispersiecoëfficiënt nul kan worden. Een alternatief zou kunnen zijn om gebruik te maken van een functie die asymptotisch naar nul gaat als L h /B h ook naar oneindig gaat. Dit vereist echter meerdere parameters waarvoor de onderbouwing op dit moment ontbreekt. Ook de relatie tussen de lengte/breedte verhouding en γ is speculatief te noemen.

# 5.2.7 Bepaling van D 0 als functie van γ

Het boven geschetste diffusieprobleem kan op basis van de vergelijking van Fick als volgt analytisch worden uitgedrukt:

$W = −D(x) · A$

h · dC/dx (5.9)

waarbij A h de (constant veronderstelde) dwarsdoorsnede voorstelt. Na substitutie van ξ = x/L en D(ξ) = ξD 0 dain volgt de oplossing:

$C(ξ) = −C$

0 · ln(ξ) = −W · L h /D 0 · A h ln(ξ) (5.10)

De over de haven gemiddelde concentratie is C 0 . Door substitutie van γ = W/Q/C 0 , volgt dan een schatting van D 0 als functie van γ:

$D$

0 = γ Q e · L h /A h (5.11)

# 5.2.8 Afleiding van concentratieprofiel

Uit de vergelijking van Fick, gebruik makend van de lineaire afhankelijkheid van de dispersiecoëfficiënt in de haven volgt voor een lozing op positie x in de haven (x is de afstand vanaf het eind van de haven, zie Figuur 5.1, de concentratie als functie van de afstand x

16 van 39



Berekening van stofconcentraties in havens

tussen het lozingspunt en de haveningang (x > x l waarbij x l de locatie van het lozingspunt is):

$dC(x - x$

l )/dx = +Q l (C(x - x l ) - C l )/(A h x - x l L h D 0 )

(5.12)

C l is de concentratie van de stof in het effluent. Verder is aangenomen dat het debiet van de lozing klein is ten opzichte van het uitwisselingsdebiet zodat het advectieve transport dat door de lozing wordt gegenereerd ook verwaarloosbaar is. De dwarsdoorsnede van de haven A is constant verondersteld.

De oplossing van deze vergelijking is vervolgens:

$C(x) = C$

l - K 1 (x - x l )

K

   2

(5.13)

met:

$K$

1 = (C l - C a )/L

K

   2

en

$K$

2 = Q l (A/L)D 0

C a is de achtergrondconcentratie. Deze vergelijking geldt voor x > x l (x l is de positie van het lozingspunt). Voor x < x l is de concentratie niet meer afhankelijk van x.

# 5.2.9 Invloed van andere lozingen in de haven

Het komt regelmatig voor dat in een haven ook andere effluenten aanwezig zijn die de verblijftijd in de haven beïnvloeden. Gezien de mogelijke lange verblijftijden in havens kunnen de extra debieten een significante invloed hebben op de verhoging van de concentratie ten gevolge van de lozing. Om dit in te schatten is de mogelijkheid aanwezig om die extra debieten in de haven mee te nemen, aannemende dat de concentratie van de stof gelijk is aan de achtergrond. Dit extra debiet geeft dus het effect van een extra doorspoeling aan en leidt niet tot concentratieverhogingen. Het is bij de implementatie ook aangenomen dat dit extra debiet aan de kop van de haven geloosd wordt. De berekening van de menging maakt gebruik van de dezelfde afleiding als voor de lozing zelf. Beide mengfactoren worden vervolgens gecombineerd hetgeen leidt tot een longitudinaal concentratieprofiel in de haven. Deze combinatie is afgeleid door een massabalans:

$C(x) = (Q$

l + Q a )/M l (x) (C l (x) - C a ) + (Q a /M a (x) + Q l /M l (x)) + C a

(5.14)

De verhoging van de achtergrondconcentratie ter hoogte van het lozingspunt wordt vervolgens gecombineerd met de pluim/jet berekening (paragraaf 3.3) waarna de concentratie op de toetsafstand wordt afgeleid.

17 van 39



# 6 Getij-uitwisseling

Bij een lozing op een getijdewater zal accumulatie plaatsvinden ten gevolge van de eb- en 
      vloedbeweging omdat geloosd effluent (Q l ) na verloop van tijd weer langs het lozingspunt 
      stroomt. De mate van accumulatie hangt af van het getij en de netto rivier afvoer (Q an ). Hoe 
      groter de netto afvoer ten opzichte van de eb (Q ae ) en vloed (Q av ) beweging, des te kleiner 
      de accumulatie. Benodigde gegevens zijn:

Lozingsdebiet, Q l [m 3 /s]; Netto afvoer, Q an [m 3 /s]; Gemiddeld eb- en vloeddebiet, Q ae en Q av - Q an [m 3 /s]; Breedte van het ontvangende water, B w [m]; 6 Diepte van het ontvangende water, D w [m]; Benedenstroomse limitatie eb afstand, M axLends [m].

The duration of the flood T v [s]:

$T$

v = T L · (Q ae - Q an ) / (Q av + Q ae ) (6.1)

where T L (44712 seconden) is de lengte van een dubbeldags getij (12:25u).

Afgelegde afstand tijdens de vloed fase (in m):

$L$

v = (Q av / (B w × D w )) T v (6.2) Afgelegde afstand tijdens de eb fase (in m):

$L$

e = (Q ae / (B w × D w )) (T deSec - T v ) (6.3)

Het aantal getijdes voor het bereiken van steady state accumulatie N g is berekend door:

$N$

g = ⌈L v / (L e - L v )⌉ (6.4) Dit wordt naar boven afgerond op een geheel getal. Wanneer de eb en vloed afstand even 
      groot zijn kan er geen menging worden uitgerekend.

Wanneer er een limiterende afstand L max is (bijvoorbeeld door een dwarsstroming waardoor 
      het water volledig wordt afgevoerd en niet terug kan komen) wordt het aantal getijdes 
      aangepast door:

$N$

Rg = ⌈L max / (L e - L v )⌉ (6.5)

N Rg wordt op een geheel getal afgerond met een minimum van 1.

Deltares 18 van 39



Per getijslag wordt iteratief een cumulatieve menging berekend, uitgaande van de menging tijdens 1 getij. De menging tijdens de vloed (M v ) en eb (M e ) zijn resp:

$M_v = \frac{Q_{av}}{4} + \frac{Q_l}{Q_l}$

(6.6)

en

$M_e = \frac{Q_{ae}}{4} + \frac{Q_l}{Q_l}$

(6.7)

De factor 4 is een veiligheidsfactor die is ingevoerd omdat er niet vanuit gegaan kan worden dat het effluent over de gehele breedte is gemengd. Er is hier dus aangenomen dat een kwart van het water beschikbaar is voor de menging. Deze factor 4 is ook consistent met de maximale breedte van de mengzone.

Voor het eerste volledige getij geeft dit een totale menging (M 1e ):

$$
\frac{1}{M_1} = \frac{1}{M_v} + \frac{1}{M_e} - \frac{1}{(M_e \times M_v)}
$$

(6.8)

Loop over alle getijslagen (n = 2 tot N g ) voor uiteindelijke menging:

Vloedmenging:

$$
\frac{1}{M_{nv}} = \frac{1}{M_{(n-1)}} + \frac{1}{M_v} - \frac{1}{(M_{(n-1)e} \times M_v)}
$$

(6.9)

Ebmenging:

$$
\frac{1}{M_n} = \frac{1}{M_{nv}} + \frac{1}{M_e} - \frac{1}{(M_{nv} \times M_e)}
$$

(6.10)

Als de noemer 0 is dan wordt de ebmenging gebruikt omdat de berekening niet kan worden uitgevoerd. Als de vloedmengfactor 1 is dan betekent dat er geen vloeddebiet is een ook dan wordt de ebmenging gebruikt om te voorkomen dat er geen menging meer is. Zodra de vloedmenging groter is dan 1 is er alleen een vloed debiet en kunnen de berekeningen worden uitgevoerd.

Deltares 19 van 39



# 7 Kust en zee

Kustwateren en open zee verschillen van de in de vorige hoofdstukken genoemde wateren in die zin dat een berekening van de verhoging van de concentratie alleen goed kan worden geschat door gebruik te maken van geavanceerde modellen. Er kan echter wel een bovengrens worden aangegeven voor de concentratie in de mengzone. Deze is gebaseerd op een menging van het effluent met het volume van de mengzone met een verblijftijd die is afgeleid van het door de mengzone stromende debiet. Voor dit debiet wordt de reststroom gebruikt omdat die de netto verversing van het mengvolume vertegenwoordigt. De concentratie die hieruit is af te leiden vertegenwoordigt de maximale verhoging van de achtergrond. De verdunning van het effluent in de mengzone is op basis van een eenvoudige massabalans:

$$
M_k = \frac{u_r \times 2 \times R_{mengzone} \times H_{mengzone}}{Q_l}
$$

(7.1)

Waarbij u_r de reststroomsnelheid is, R_{mengzone} de straal van de mengzone en H_{mengzone} de dikte/diepte van de mengzone (zie Hoofdstuk 3). Dit geldt voor een lozing op open zee. Voor een lozing aan de kust is de maximale toegestane mengzone begrensd door de kustlijn waardoor de massabalans niet 2 × R maar alleen R bevat. De menging M_k bepaalt de verhoging van de achtergrond in de mengzone. Hierna volgt nog een berekening van de concentratie in een pluim (of jet) waaruit de gecombineerde concentratie van achtergrondverhoging en pluim (of jet) volgt.

Deltares 20 van 39



# 8 Totale menging en eindconcentratie

Voor elk type water vormt de eindconcentratie het resultaat van een pluimberekening of een berekening van de algemene menging van het effluent met achtergrond die al of niet gevolgd wordt door een pluimberekening. De algemene mengfactor M

    a is gedefinieerd als:

$M$

a = 1 + Q a / Q l = Q l + Q a / Q l (8.1) met:

Lozingsdebiet, Q l [m 3 /s]; Afvoer, Q a [m 3 /s];

Wanneer dit reeds gemengde water nog een keer gemengd wordt met het effluent met mengfactor M

    p (bijvoorbeeld door een pluimberekening), dan volgt uit een massabalans dat de totale mengfactor M

    tot gedefinieerd wordt door:

$1 / M$

tot = 1 / M a + 1 / M p - 1 / M a × M p (8.2)

De laatste term is onbelangrijk bij vrij grote mengfactoren (groter dan ....) maar is wel significant bij lage mengfactoren. Wanneer eenmaal totale menging op deze wijze is afgeleid, volgt de verhoging van de concentratie ΔC t ten opzichte van de achtergrondconcentratie (C w ):

$ΔC$

t = C l - C w / M tot (8.3) met:

Concentratie effluent C l [g/l]; Achtergrond concentratie C w [g/l]; Verhoging concentratie (tov C w ) na twee mengvormen, ΔC t [g/l];

achtergrondconcentratie (C w ):

$ΔC$

t = C l - C w / M tot (8.4)

Deltares 21 van 39



# 9 Koudwaterlozingen

# 9.1 Inleiding

Voor Koudelozingen is een apart tabblad opgezet. De basis vergelijkingen voor menging zijn dezelfde als voor stoflozingen. Dit betekent dat de pluimmening met het oppervlaktewater hetzelfde is. Het kader voor de beoordeling is echter wel anders. Dit blijkt voornamelijk uit de beslisboom die wordt gehanteerd en de gegevens die nodig zijn om tot een beoordeling te komen. Veel velden zullen door de gebruiker moeten worden ingevuld omdat hier geen informatie aanwezig is in de database van de immissietoets. Het thermische lengteprofiel wordt vervolgens ook getoond als tweede deel van de verdunningsgrafiek. Voor de verdere verspreiding van koudelozingen (verder dan de pluim berekeningen toelaat) wordt de warmte-uitwisseling met de atmosfeer belangrijk. Vandaar dat er een warmtebalans is toegevoegd om daar een inschatting van te geven. Hieruit volgt dan een thermisch lenteprofiel. Hiervoor wordt gebruik gemaakt van het Nationaal Water Model (NWM), waarin een tracer is meegenomen (vergelijkbaar met de stoflozingen) waarin uitwisseling met de atmosfeer ook in is meegenomen. Voor de pluimberekeningen wordt op dit moment gebruik gemaakt van de 10% lage afvoer.

# 9.2 Thermisch lengteprofiel

Het thermische lengteprofiel wordt uitgerekende aan de hand van een warmtebalans. De warmtebalans is:

$$
ρ × C_v × Q × \frac{dT}{dx} = λ × W × (T - T_e) \quad (9.1)
$$

ρ: dichtheid water [kg.m

    3
   
] C_v: warmtecapaciteit water [J.kg

    -1
   
.°C

    -1
   
] Q: rivierdebiet [m

    3
   
.s

    -1
   
] T: Water temperatuur [°C] x: afstand stroomafwaards [m] λ: Warmteuitwisselingscoefficient met de atmosfeer [W.m

    -2
   
°C

    -1
   
] W: Breedte van rivier [m] T_e: evenwichtstemperatuur met de atmosfeer [°C]

Dit leidt tot een beschrijving van de temperatuur als functie van de afstand:

$$
T_x = (T_0 - T_e) × e^{-\frac{x}{L}} + T_e \quad (9.2)
$$

waarbij:

$L = \frac{ρ × C_v × Q}{λ × W} \quad (9.3)$

22 van 39



Als er de inname vanuit een ander waterlichaam is kan er geen recirculatie optreden en wordt het lozingsdebiet toegevoegd aan het ontvangende water waardoor het debiet waarmee het lengteprofiel wordt berekend verhoogt en wordt vergelijking 9.3:

$$
L = \frac{\rho \times C_v \times (Q + Q_L)}{\lambda \times W}
$$

(9.4)

Wanneer ddit lozingsdebiet Q_L klein is ten opzichte van de afvoer Q zullen beide nagenoeg hetzelfde resultaat geven. De T_x levert dan het thermische lengte profiel.

# 9.3 Bepaling van de dimensies van de mengzone

Voor de beoordeling van de impact is een mengzone gedefinieerd door een lengte, dwarsdoorsnede en een oppervlakte. De grens van de mengzone is bepaald door het toegestane temperatuurverschil. De pluim berekening in de immissietoets levert alleen de menging als functie van de lengte. Het oppervlak en dwarsdoorsnede zullen nog moeten worden afgeleid. Voor de dwarsdoorsnede (met een contour van het toegestane temperatuurverschil) kan worden afgeleid van een massabalans. Dit levert de maximale doorsnede op die je dan kunt vergelijken met de doorsnede van het ontvangende water. Hiervoor maken we gebruik van de benodigde menging om de het temperatuurverschil van het effluent met de achtergrond (ΔT) terug te brengen tot het toegestane temperatuurverschil (ΔT_i).

$M_{T_i} = \frac{\Delta T}{\Delta T_i}$

(9.5)

Om het effluent met een debiet van Q_L te verdunnen is een rivierdebiet nodig van Q_ra. De dwarsdoorsnede die hiervoor nodig is hangt af van de doorsnede van de rivier (ontvangende water), H × W en het totale rivierdebiet Q en dit vertaalt zich in :

$$
\frac{Q_{ra} + Q_L}{Q_L} = M_{T_i} \Rightarrow Q_{ra} = (M_{T_i} - 1) \times Q_L
$$

(9.6)

De ratio van het benodigde debiet van de rivier en het actuele debiet van de rivier vertegenwoordigd het relatieve dwarsdoorsnede van de mengzone tov de dwarsdoorsnede van de rivier. Dit leidt tot een benodigde doorstroomd oppervlakte van:

$$
A_{M_{T_i}} = \frac{Q_{ra}}{Q} \times (H \times W)
$$

(9.7)

Met Q het debiet van de rivier (m³/s). In het huidige kader wordt verwezen naar 50% van de natte doorsnede hetgeen bijvoorbeeld betekent: Een rivier met 250 m² doorsnede (W=25, H = 10 m) en een debiet (Q) van 15 m³/s een lozingsdebiet (Q_L) van 1 m³/s en een temperatuurverschil tussen effluent en rivier van -14 graden (toegestane temperatuurverschil van 4) leidt tot een relatieve maximale doorsnede van (A_{M_{T_i}}=abs(-14)/4=3.5, dus Q_{ra}=(3.5-1) × 1 = 2.5) : \frac{Q_{ra}}{Q} = \frac{2.5}{15} = 16.7% en dit is minder dan de maximale 50%. Op deze wijze kan de dwarsdoorsnede van de mengzone worden afgeleid.

Deltares 23 van 39



Het oppervlak van de pluim kan dan vervolgens worden afgeleid uit een breedte (\sqrt{AM_T}) en de menglengte die door de pluim 
    berekening wordt uitgerekend ( L , de afstand tot de 
    toegestane temperatuurverschil). Aannemende dat dit een gelijkbenige driehoek 
    vormt wordt daarvan de oppervlak :

$A_{Mopp} = \frac{W \times L}{2}$

(9.8)

Deze vergelijking gaat echter van uit dat de dimensies van de pluim niet wordt 
    beperkt door de geometrie (dwarsdoorsnede) van het ontvangende water en de diepte 
    groter is dan deze dimensie. Omdat in de handreiking wordt verwezen naar het 
    epilimnion (oppervlaktelaag) ligt het voor de hand om dit ook mee te nemen bij 
    de bepaling van de maximale dikte van de pluim. In de immissietoets is de waarde 
    van spronglaag (indien>0) beschikbaar en vormt dan de limiet van de dikte van de 
    pluim. Als er geen dikte gegeven is dan kan de waterdiepte als limiterend optreden. 
    De dimensies van de pluim zijn altijd begrensd door de dimensies van het ontvangende 
    water. Dit betekent dat indien de diepte (of spronglaag) kleiner is dan (\sqrt{AM_T}) de dikte van de pluim wordt begrensd 
    door die diepte (ligging van de spronglaag) H . De 
    breedte van de pluim wordt dan W = \frac{A_{Mopp}}{H} . Deze kan dan worden gebruikt 
    om het oppervlak te bepalen van de driehoek va de menglengte en deze breedte. Het 
    kan in theorie voorkomen dat dit uitkomt op groter dan de breedte van het 
    ontvangende water, maar in dat geval is de doorsnede van de pluim altijd meer dan 
    50% en zal het niet door de desbetreffende beslisboom worden goedgekeurd.

# 9.4 Koude lozingen in havens

# 9.4.1 Warmtebalansen

Ook in havens (dus zonder restdebiet) kunnen koudelozingen voorkomen. In deze 
    gebieden is het debiet (wflow 0) waardoor op dit moment voor het NWM deel geen 
    resultaat mogelijk is, maar ook het berekenen van het thermische lengteprofiel is 
    dan ook niet mogelijk. Binnen de pluim berekening kan dezelfde techniek wel worden 
    gehanteerd als voor de stoffen, ook de verhoging van de achtergrond wordt dan in 
    beginsel zonder uitwisseling met de atmosfeer berekend hetgeen wel een worst-case 
    aanpak is. In de warmtebalans van het ontvangende segment kan daar wel voor worden 
    gecorrigeerd door een warmte-uitwisselingscoëfficiënt, oppervlak en diepte. De 
    koppeling met het NWM is er dan nog niet, zodat er geen temperatuurkaart kan worden 
    gegenereerd. Voor een haven is de verblijftijd als volgt af te leiden:

$\tau = \frac{V_s}{Q_L + Q_x + Q_a}$

(9.9)

Met Q_L het lozingsdebiet, Q_x het uitwisselings debiet met het langstromende 
    water en Q_a het additioneel debiet (allen in m³/s).

In de immissietoets zijn er havens waarvan de ververstijd in de database al bekend 
    is (uit tracer berekeningen die in de modelsimulaties zijn meegenomen) en waar dit 
    niet zo is en de uitwisseling met het langstromende water is afgeleid met een 
    zgn. Silthar berekening (Eysink (2004)). De berekeningen van Silthar leidt het 
    totale uitwisselende debiet af, maar niet wat dit voor het lokale ontvangende 
    segment betekent waardoor de door Silthar afgeleide debieten niet direct kunnen 
    worden gebruikt voor de thermische balans van het ontvangende segment.

Voor elk segment wordt wel een verdunning of mengfactor M_F voor de berekening van de verhoging van de 
    achtergrond afgeleid. Deze mengfactor berekening wordt gebruikt voor de

24 van 39



Koudwaterlozingen

stoflozing. Hieruit kan het uitwisselingsdebiet worden afgeleid dat voor dit segment nodig is: Q_x = Q_L \times (M_f - 1) . Hieruit volgt meteen dat de verblijftijd (verversingstijd) in dat segment 
    kan worden uitgerekend door:

$\tau = \frac{V_s}{Q_L \times (1 + M_f)}$

(9.10)

In havens zonder verversingstijd (met name de havens in Rotterdam) kan deze uit bestaande 
    gegevens in de immissietoets worden afgeleid. Wanneer deze wel bekend is kan die bekende 
    verversingstijd worden gehanteerd.

Voor het bepalen van de verblijftijd is het volume van het ontvangende segment wel van 
    belang. Het oppervlak van dat segment is bekend voor de polygoon waar de lozing in 
    plaatsvindt, de diepte ook dus daaruit volgt het volume. Als de inname wel uit de haven zelf 
    komt dan verandert niets aan de vergelijking, behalve dat er geen volume wordt toegevoegd 
    door de lozing, dus Q_L = 0 .

Wanneer water dat wordt geloosd ook in dezelfde haven wordt ingenomen dan treedt 
    recirculatie op. Dit kan schematisch worden weergegeven (figuur 9.1):

Diagram of water flow and heat transport in a harbor with recirculation Figuur 9.1: Haven debieten en warmte transport bij recirculatie, Φ_L is de toegevoegde 
      warmte

In eerste instantie gaan we er van uit dat de recirculatie komt door een lokale verhoging van 
    de achtergrond, zoals bij de stoflozing uitgerekend wordt, wat warmtebalans betreft ziet deze 
    er iets anders uit namelijk:

$$
Q_x \cdot \rho \cdot C_v \cdot \Delta T + Q_L \cdot \rho \cdot C_v \cdot \Delta T - Q_L \cdot \rho \cdot C_v \times (\Delta T + \Delta T_L) = 0
$$

(9.11)

De warmtevracht van de lozing is Φ_L (J/s), en is gedefinieerd als Φ_L = ρ · C_v · ΔT_L · Q_L, met 
    ΔT_L de temperatuurverhoging tov de inname temperatuur. Als het water ingenomen wordt 
    van een andere locatie dan wordt de recirculatiegraad 0 en de vergelijking:

$$
Q_x \cdot \rho \cdot C_v \cdot \Delta T + Q_L \cdot \rho \cdot C_v \cdot \Delta T - Q_L \cdot \rho \cdot C_v \times \Delta T_L = 0
$$

(9.12)

Deltares 25 van 39





Tot nu toe geldt dezelfde afleiding ook voor stoffen omdat er geen warmte-uitwisseling aanwezig is. De warmte/massabalans en de debieten die hiervan zijn afgeleid gaan er van uit dat het binnenkomende water van de uitwisseling (Q x ) dezelfde temperatuur heeft als de achtergrond. Dit zou wellicht kunnen leiden tot een onderschatting van de temperatuurverandering in het segment omdat in de haven ook het binnenstromende water in dat segment al door de lozing zelf is beïnvloed. Echter, in de massabalans die is uitgewerkt (dat geld voor zowel stoffen als temperatuur) wordt uitgegaan van het theoretische concentratie profiel (stationaire oplossing) waarbij de concentraties als functie van de afstand tot de haveningang inclusief dit effect is (voor deze afleiding zie hoofdstuk 5.2.8) en dus correct. Het resultaat is dat de mengfactor, M f , die is uitgerekend en waar de debieten van worden afgeleid gecorrigeerd zijn voor het terugstromen bij het uitwisselingsproces. Hierdoor kan de aanname worden gehanteerd dat dit terugstromende water inderdaad de achtergrondtemperatuur heeft.

De voorafgaande afleidingen is nog exclusief het effect van een warmte-uitwisseling met de atmosfeer. Om de warmte-uitwisseling te kunnen berekenen is de verblijftijd of verversingstijd nodig. Bij afwezigheid van de verversingstijd τ, zoals in Rotterdam, kan deze τ worden uitgerekend op basis van de stofverspreiding via de mengfactor M f die bekend is. Daar kan dan de Q x van afgeleid worden zodat alle info bekend is om de uiteindelijke ΔT uit te rekenen. Om die warmte-uitwisseling uit te rekenen is wel het oppervlakte van het segment A seq nodig omdat de verdwijnende warmteflux bepaald wordt door:

$Φ$

atm = λ × (T − T c ) × A seq (9.13)

λ is de warmte-uitwisselingscoëfficiënt en bedraagt 20 W/m 2 (conservatieve schatting die consistent is met die van het NWM).

Deze flux kan worden opgenomen in de warmtebalans en dit leidt dan tot:

$Q$

x ·ρ·C v ·ΔT+Q L ·ρ·C v ·ΔT−Q L ·ρ·C v ·(ΔT+ΔT L )+λ×(T−T c )×A seq = 0 (9.14) Dit wordt vereenvoudigd tot:

$Q$

x ·ΔT + Q L · ΔT − Q L × (ΔT + ΔT L ) + λ × (ΔT) × A seq / ρ · C v = 0 (9.15) Hierin is aangenomen dat ΔT is gebaseerd op een achtergrond temperatuur van het water dat in evenwicht is met de lucht, dus een temperatuurverandering (zowel stijging als daling). Hieruit kan dan de temperatuur in het segment worden bepaald door:

$ΔT = Q$

L · ΔT L / Q x + Q a + λ·A seq / ρ·C v (9.16) Zonder recirculatie wordt dit:

$ΔT = Q$

L · ΔT L / Q x + Q a + Q L + λ·A seq / ρ·C v (9.17) Hierbij is het eventuele additionele debiet ook meegenomen in de massabalans. Het resultaat van een dergelijke berekening is in een grafiek uitgewerkt Figuur (9.2) waarbij hier de onafhankelijke variabele de verblijftijd in dagen is.

Deltares 26 van 39



graph TD;
        A[Delta T without exchange, no recirculation(deg.C)] --> B[Delta T with exchange, no recirculation(deg.C)];
        A --> C[Delta T with exchange, with recirculation(deg.C)];
        A --> D[Delta T without exchange, with recirculation(deg.C)]; Figuur 9.2: Temperatuurverlaging met en zonder warmteuitwisseling (20 W/m²) en met en zonder recirculatie. De ΔT L is -8°C

# 9.4.2 Opzetten van het warmteprofiel in havens

De berekeningen in het vorige hoofdstuk hebben betrekking op de verhoging van de achtergrond temperatuur zonder de directe pluimverspreiding, die komt daar nog bij zoals dat ook voor zoetwatersystemen is geïmplementeerd (dat dus door de applicatie als pluimmening wordt bestempeld). De tweede stap is de omgevingsmenging die wordt berekend aan de hand van een thermische lengte profiel zoals dat al in hoofdstuk 9.2 is uiteengezet. Daarbij is een debiet en breedte nodig en wanneer de inname ook in de haven is dan is in beginsel is het netto debiet in een haven 0 en kan deze oplossing niet direct worden gebruikt.

Een methodiek kan wel worden opgezet wanneer de beschikbare karakteristieken en rekenresultaten voor het lozingssegment worden gebruikt. Binnen de huidige opzet van de applicatie zijn alle locatiesegmenten onafhankelijk van elkaar en is niet bekend welke segmenten bijvoorbeeld buursegmenten zijn. Een havenlengteprofiel kan op dit moment dus alleen worden afgeleid door gebruik te maken van de gegevens die bij het lozingssegment horen. Bij de gebruikte methode wordt geen rekening gehouden met de mogelijke complexiteit van de haven of uitstroom vanuit de haven naar het hoofdsysteem. Wanneer gebruik gemaakt wordt van een conservatieve aanpak dan geeft het resultaat dus een indruk van de maximale afstand waarover een lozing in de gegeven omstandigheden effect heeft. Wanneer de karakteristieken van het lozingssegment worden toegepast op de segmenten, dan is een beste benadering om de karakteristieken van dat segment ook voor het thermische profiel te gebruiken. Dit kan dan worden ingezet door het profiel op te bouwen voor lengtes van het ontvangende segment en vergelijking 9.17 te gebruiken waarbij ΔT L vervangen wordt door ΔT 1 , de berekende temperatuur van het segment waarin geloosd wordt. Hierbij moet ook een onderscheid gemaakt worden tussen met en zonder

27 van 39



Koudwaterlozingen



recirculatie. Schematisch is het thermische profiel gebaseerd op figuur

graph TD;
        A[ΔT₀] -->|Qₖ| B[ΔT₁];
        B -->|Qₖ| C[ΔT₂];
        A -->|Qₖ| D[Qₑ,stem];
        B -->|Qₖ| E[Qₑ,stem];
        C -->|Qₖ| F[Qₑ,stem];
        G[Q₁ ΔT₀] --> A;
        H[Q₁ ΔT₀+ΔT₁] --> A;
        I[Q₁ ΔT₀+ΔT₁] --> G;

Figuur 9.3: Overzicht van de methodiek voor het afleiden van het thermische profiel in havens

Het is dus een iteratieve berekenwijze. Voor segment n kan uit figuur 9.3 een thermische balans worden afgeleid door:

$$
Qₓ · ρ · Cᵥ · ΔTₙ₋₁ = Qₓ · ρ · Cᵥ · ΔTₙ + λ · ΔTₙ · Aₛₑg
$$

(9.18)

en hieruit volgt dan inclusief recirculatie:

$ΔTₙ = Qₓ · ΔTₙ₋₁ / (Qₓ + λ · Aₛₑg / ρ · Cᵥ)$

(9.19)

In het uitwisselingsdebiet, zoals dat vanuit de verblijftijd is afgeleid, is het lozingsdebiet voor de segmenten n>0 niet meegenomen. Zonder recirculatie zal dus het lozingsdebiet moeten worden opgeteld om de massa en warmtebalans volledig te maken. Dan wordt de vorige vergelijking 9.19:

$$
ΔTₙ = (Qₓ + Qₗ) · ΔTₙ₋₁ / (Qₓ + Qₗ + λ · Aₛₑg / ρ · Cᵥ)
$$

(9.20)

Deze aanpak is consistent met hoe de de concentraties voor de stoflozingen in de havensegmenten worden afgeleid. Een beperking is wel dat dit alleen waardes oplevert voor een integer vermenigvuldiging van de lengte van het havensegment (oftewel het oppervlakte gedeeld door de breedte dat door de gebruiker is ingevoerd), waardoor een vrij groffe discretisatie in de afstand optreedt. Er wordt ook geen rekening gehouden met een mogelijke complexere geometrie van de haven.

# 9.4.3 Recirculatie in andere wateren

Deltares 28 van 39



# 9.4.3.1 Recirculatie in andere wateren met complexere waterbeweging

De methodiek zoals die voor havens is afgeleid is ook toepasbaar voor wateren waar voor de
      segmenten een verversingstijd beschikbaar is (dus die met een tracer zijn berekend). De
      (worst-case) aanname is dat wel dat het inname punt ook in het lozingssegment zit (dat hoeft
      niet perse zo te zijn). Als dat niet zo is dan is er geen recirculatie (daar zou dan een vinkje in
      opgenomen kunnen worden?). Voor dit type water (exclusief de havens) kan voor de verdere
      verspreiding van het koude water (inclusief de recirculatie ) op dezelfde wijze gekoppeld
      worden aan de NWM segmenten. Dus de temperatuurverlaging aan het eind van de
      mengzone wordt gebruikt als input voor het NWM. Voor lijnvormige wateren met 1
      stromingsrichting gaat dit niet omdat er geen verversingstijd beschikbaar is voor het
      lozingssegment en de recirculatie graad op een andere manier berekend moet worden.

# 9.4.3.2 Rivieren en ander lijnvormige wateren met 1 stromingsrichting

Wanneer in een oppervlakte water ingenomen wordt en met een lagere temperatuur geloosd
      wordt kan er ook recirculatie optreden. Voor wateren waarin een achtergrond menging wordt
      berekend kan dezelfde methodologie worden gebruikt als in haven. En hierbij kan dan ook
      worden verwezen naar vergelijking 9.16. Dit geldt in beginsel wanneer aangenomen wordt
      dat de inname in het zelfde segment plaats vindt als de lozing zelf. Wanneer dit niet het
      geval is en er alleen een lozing plaatsvindt, dan kan vergelijking 9.17 worden toegepast. Dus
      zolang de verblijftijd bekend is kan dit worden bepaald voor elk watersysteem. De verblijftijd
      in een segment wordt niet door de lokale recirculatie beïnvloed. Immers, de verblijftijd wordt
      bepaald door het uitstroomende debiet en het volume van het segment, en dat verandert niet
      bij recirculatie. Dit betekent dat voor alle segmenten waar een achtergrondconcentratie
      verhoging voor stoffen wordt berekend, dezelfde aanpak kan worden gehanteerd, omdat
      voor die wateren voor het segment waarin de warmte lozing plaatsvindt, de verversingstijd
      bekend is en dit bepaald de recirculatie zoals ook in havens is berekend. Voor wateren waar
      geen verblijftijd wordt berekend is dit echter niet het geval. Er kan immers recirculatie
      optreden wanneer het debiet van de inname (bovenstrooms van het lozingspunt) groter
      wordt dan de rivierafvoer. Er vindt dan tussen het lozingspunt en innamepunt een
      terugstroom plaats die het tekort vanuit de rivier aanvult. Met andere woorden, de
      recirculatiestroom wordt dan Q_L - Q , waarbij Q_L groter is dan Q . Wanneer de afstand
      tussen inname en lozing bekend is in combinatie met de breedte van het ontvangende water
      verminderd de recirculatie door de warmteuitwisseling met de atmosfeer en kan de
      uiteindelijke lozingstemperatuur (verschil met de achtergrond) worden afgeleid:

$ΔT_{Le} = ΔT_{in} + ΔT_{Lr} \tag{9.21}$

met de inname temperatuur ΔT_{in} inclusief de recirculatie en rekening houden met het
      thermische profiel tussen lozingspunt en innamepunt (zie vergelijking 9.2). Hierbij kan dan wel
      worden opgemerkt dat Q_L in vergelijking 9.3 wordt vervangen door Q - Q_L :

$$
L_r = \frac{ρ × C_v × (Q_L - Q)}{λ × W} \tag{9.22}
$$

De temperatuur van het terugstromende water bij de inlaat na menging met de rivierafvoer
      wordt dan (het inlaatdebiet Q_L is groter dan de rivierafvoer Q ):

$$
ΔT_{in} = \frac{Q_L - Q}{Q_L} × ΔT_{Le} × e^{-\frac{t}{L_r}} \tag{9.23}
$$

De combinatie van vergelijkingen 9.21 met vergelijking 9.23 levert dit uiteindelijk:

$$
ΔT_{Le} = \frac{ΔT_L}{1 - \frac{Q_L - Q}{Q_L} × e^{-\frac{t}{L_r}}} \tag{9.24}
$$

Deltares 29 van 39



Koudwaterlozingen

De ΔT_{Le} is de effluent temperatuur (de Q_{L} verandert niet) die uiteindelijk wordt geloosd en als startpunt dient voor de rest van de koudelozing berekeningen. In beginsel zijn alle gegevens bekend. Mocht er geen info zijn over de afstand tussen het inname en lozingspunt, dan kan deze ook op 0 gezet worden waardoor de vergelijking vereenvoudigd wordt omdat de temperatuur bij de inlaat enkel het resultaat is van de menging van de rivier afvoer en het terugstromende debiet.

Deltares 30 van 39



# Bibliography

Delvigne, G., 1979. “Round buoyant jet with three-dimensional trajectory in ambient flow.” 18th Congress of the IAHR, Cagliari, Italy . Eysink, W., 2004. “SILTHAR Version 4.2 - A mathematical program for the computation of siltation in harbour basins.” Report 8.6520, Delft Hydraulics, Delft . Graaf, J. van de en R. Reinalda, 1977. “Horizontale uitwisseling in samengekrompen modellen.” Report S0061, Waterloopkundig Laboratorium, Delft . Hattum, B. van, A. Baart en J. Boon, 2002. “Computer model to generate predicted environmental concentrations (PECs) for antifouling products in the marine environment - 2nd edition accompanying the release of Mam-Pec Version 1.4.” Report number E-02-04/Z3117, IVM, Vrije Universiteit, Amsterdam . IJff, J., 2000. “Emissie-immissie: prioritering van bronnen en de immissietoets (juni 2000).” CIW werkgroep Emissies en diffuse bronnen (werkgroep VI) .

Deltares 31 van 39



# A Testinstructie

# A.1 Inleiding

Bij elke aanpassing van de applicatie wordt deze getest, maar voor het interface zijn geen automatische testen beschikbaar, vandaar deze testinstructie. De applicatie heeft 3 tabbladen:

Stoflozing Temperatuurlozing Informatie

Het is aan te raden om bij het testen de cache eerst te legen zodat nog aanwezige restanten van een vorige versie het gedrag van de applicatie kunnen beïnvloeden. Wanneer de applicatie wordt opgestart zal het versienummer in de bovenste balk zichtbaar zijn. IN dit document wordt gebruik gemaakt van een specifiek voorbeeld, maar het verdient aanbevelingen om verschillende watertypes te selecteren en te testen.

# A.2 Stoflozing

Open de website van de immissietoets (de publieke site is: www.immissietoets.nl )

Informatieblad Figuur A.1: Informatieblad

Het startscherm wordt zichtbaar (figuur A.1) en de eerste stap is het selecteren en invullen van de gegevens voor de basisberekening. De eerste stap voor het uitvoeren van de berekeningen is het selecteren van een locatie en dat gebeurt door in te zoomen en met de muis te klikken op een locatie (zoals hieronder al is gedaan). Selecteren kan alleen wanneer de segmenten zichtbaar worden, dus er moet voldoende worden ingezoomed, zie figuur A.2.

Deltares 32 van 39



Testinstructie

Map and interface screenshot Figuur A.2: Informatieblad

In de figuur is in de info box aangegeven (geen onderdeel van het interface) dat een aantal kaartlagen kunnen worden geselecteerd (indien beschikbaar), dit heeft voor de applicatie verder geen consequenties. In dit voorbeeld is een locatie gekozen in de Nieuwe Waterweg. Het nummer van de locatie is hier 3836. Na het selecteren verschijnen aan de rechterkant van het scherm het menu voor het in- en aanvullen van resterende gegevens. Voor atrazine zijn ook metingen beschikbaar die zijn aangegeven en in dit voorbeeld is locatie 200102 geselecteerd (en dit geeft een concentratie van 0.0033μg/l. Het invoerveld voor de stof kijkt ook naar of de tekst in de naam voorkomt (als een filter). Wanneer bijvoorbeeld allen 'atra' is ingevuld verschijnen er 4 stoffen (dd: 2-2-24) waaruit kan worden geselecteerd.

atraton atrazine desethylatrazine desisopropylatrazine

Als er voor een stof meetpunten beschikbaar zijn kan dat op een vergelijkbare manier worden gekozen via de drop-down lijst, of door het klikken op de locatie van het meetpunt.

kies een stof. Er is een lijst en door een stofnaam in te toetsen verschijnen de mogelijke stoffen (er wordt op sub-strings gezocht), kies atrazine De JG-MKN wordt opgehaald uit de database, de gebruiker kan de waarde aanpassing indien noodzakelijk, er verschijnt dan aan de rechterkant een icoon die kan worden aangeklikt om de database waarde te herstellen Debiet en concentratie van het effluent invullen kies een beschikbaar meetpunt voor de achtergrond concentratie door een punt te selecteren (zichtbaar op de kaart). Meetpunt 17914 levert een achtergrondconcentratie van 0.0057μg/ klik op de knop “resultaten”. Een basisberekening wordt uitgevoerd en de beslisboom wordt zichtbaar onder de invoerdata.

Deltares 33 van 39



Testinstructie



De naam van het waterlichaam verschijnt als KRW Waterlichaam. Er kan gekozen worden voor een ander waterlichaam als daar specifieke redenen voor zijn. Na de eerste berekening verschijnt de beslisboom onder Resultaten met daarin de effluent en triviaaltoets. Ook zichtbaar onder de kaart worden de invoervelden voor de geavanceerde berekening (figuur A.3):

Geavanceerde berekening - immissietoets Figuur A.3: Invoerscherm voor de geavanceerde berekening

De meeste informatie wordt opgehaald uit de achterliggende database. Wel moet nog worden ingevuld:

dichtheid van de lozing (hier 1000 kg/m3) de diameter van de lozingspijp (hier 0.5 m) de ligging van de pijp in de horizontaal als de verticaal (hier aan de oever en aan het oppervlak). Hier is een beperkte keuze voor beschikbaar via een drop-down lijst met de default ‘Oever’ en ‘Oppervlak’.

Deltares 34 van 39



Testinstructie

Wanneer geen gebruiker gedefinieerde afstand wordt opgegeven wordt de toetsafstand
    afgeleid van de dimensies van het ontvangende water (hier niet ingevuld). Voor een ingevuld
    scherm zie figuur A.4

# Resultaten

graph TD;
      A[Lozing] --> B[effluenten];
      B --> C[significatie];
      C --> D[normen];
      D --> E[normen MAC];

Figuur A.4: Beslisboom voor de geavanceerde berekening

Indien beschikbaar is de MAC MKN voor de gekozen stof ingevuld en een veld dat weergeeft
    welke norm dit is (bijvoorbeeld 'Andere oppervlaktewateren wettelijke MAC-MKN (totaal) (zout
    water)')

Druk op de knop “geavanceerde berekening” en een geavanceerde berekening wordt
    uitgevoerd en genereert een beslisboom zoals hierboven in figuur A.4 aangegeven. In de
    uitvoer zijn nog een aantal knoppen zichtbaar: Drinkwater inname: Wanneer op deze knop
    wordt gedrukt dan verschijnt de volgende tabel met de uitkomsten van de drinkwatertoets
    (figuur A.5 ):

Deltares 35 van 39



Testinstructie

# Resultaten

| Locatie | Concentratie verhoging [µg/l] | Achtergrondconcentratie [µg/l] | Totale concentratie [µg/l] | Voldoet aan norm |
| --- | --- | --- | --- | --- |
| Ridderkerk, Reijerwaard, Nwe Maas | 0.243 | 0.006 | 0.248 | Ja |
| Noordkant Kralingen | 0.252 | 0.003 | 0.255 | Ja |
| Noordkant Benedenplaat | 0 | 0.005 | 0.005 | Ja |
| Middelharnis | 0 | 0.005 | 0.005 | Ja |
| Bestebosch | 0 | 0.005 | 0.005 | Ja |
| Hendrik-Ido-Ambacht, Noord | 0 | 0.007 | 0.007 | Ja |
| Schenkelhoek | 0 | 0.009 | 0.009 | Ja |
| Heel | 0 | 0.005 | 0.005 | Ja |
| Brakel | 0 | 0.005 | 0.005 | Ja |
| Andijk | 0 | 0.003 | 0.003 | Ja |
| Roosteren, Maas | 0 | 0.005 | 0.005 | Ja |
| Lopikerk, De Steeg, Lek | 0 | 0.008 | 0.008 | Ja |
| Bergambacht, C. Roodehuis, Lek | 0 | 0.005 | 0.005 | Ja |
| Noordkant Bergambacht | 0 | 0.005 | 0.005 | Ja |
| Lekkerkerk, Schuwacht & Tiendweg, Lek | 0 | 0.006 | 0.006 | Ja |
| Nieuwegein | 0 | 0 | 0 | Ja |
| Noordkant Baanhoek | 0 | 0 | 0 | Ja |
| Zwolle, Engelen Veld, IJssel | 0 | 0 | 0 | Ja |
| Nieuwe-Lekkerland, De Pla, Lek | 0 | 0 | 0 | Ja |

Figuur A.5: Drinkwater tabel

Ook wordt een grafiek gegenereerd met het verloop van de concentratie als functie van de afstand tot het lozingspunt.

# Resultaten

# Grafische weergave pluim

graph TD;
      A[lozingsconcentratie + achtergrondconcentratie] --> B[achtergrondconcentratie];
      A --> C[JG-AKTK standaard];
      A --> D[MAC afstand];
      A --> E[JG-MKN];
      A --> F[MAC];

Figuur A.6: Concentratie als functie van de afstand tot het lozingspunt

Er is ook een log uitvoer waarin in detail kan worden gekeken naar details van berekeningsresultaten. Deze is met name bedoeld om in detail te onderzoeken welke

Deltares 36 van 39



Testinstructie



getallen zijn gebruikt en voor expert analyse als dat nodig is. Met de knop kan een pdf
      uitvoer worden gegenereerd waarin alle in en uitvoer van de berekeningen zijn opgenomen.
      Deze kan lokaal op een computer worden opgeslagen. Er zal goed gekeken moeten worden of alle gewenste velden aanwezig zijn en de uitvoer
      correct. Tevens wordt er ook een log gegenereerd en is het mogelijk om een pdf van het
      volledige resultaat (in- en uitvoer) van de immissietoets te genereren.

# A.3 Temperatuurlozing

Bij het selecteren van de tab temperatuurlozing verschijnt een scherm dat vergelijkbaar is met
      de stoflozing tab. Als vanuit een geselecteerd gebied in stoflozing wordt overgestapt naar de
      temperatuur tab, dan blijf de locatie selectie in stand.

Scherm van de temperatuur tab na selectie Figuur A.7: Scherm van de temperatuur tab na selectie

Specifieke data zal nog moeten worden ingevuld. In dit voorbeeld is de diameter van 0.5m
      gekozen en onder het kopje Temperatuur is een lozing van -8 graden (ten opzichte van het
      ontvangende water) gekozen. Let op dat ook naar de zoutconcentratie moet worden gekeken
      omdat deze bij default op 0 staat. In beginsel is de zoutconcentratie gelijk aan die van het
      ontvangende water maar moet die wel worden ingevuld, tenzij het proces de zoutconcentratie
      verandert of de inname uit een ander watersysteem wordt gehaald (dus de zoutconcentratie
      afwijkt).

In het voorbeeld van figuur A.7 is dezelfde locatie gekozen (3836).

Na het uitvoeren van de berekening wordt het volgende scherm zichtbaar. Zaak is om te
      controleren dat alle velden inderdaad aanwezig zijn.

Deltares 37 van 39



Testinstructie

Temperature input and result screen Figuur A.8: Temperatuur invoer en resultaat scherm

In versie 1.13.1 is de beslisboom niet meer zichtbaar omdat die niet meer actueel is en in de loop van 2024 zal worden vervangen. In plaats daarvan wordt de 'Resultaten' tab met daarin een grafiek getoond. Wanneer de aangegeven locatie is gekozen wordt een watertype O geselecteerd. Om echter een resultaat te krijgen zal een selectie gemaakt moeten worden en in dit geval is gekozen voor "Grote rivieren(R8)". In de grafiek is het toegestane verschil (in dit geval 4 graden) grijs aangegeven. Er wordt ook een kaart gegenereerd met daarin aangegeven hoe groot het gebied is dat door de koudelozing wordt beïnvloed.

# Resultaten

Map showing the area affected by cold discharge Figuur A.9: Indicatie van het gebied dat door de koudelozing wordt beïnvloed

Deltares 38 van 39



# A.4 Informatie

Dit tabblad geeft algemene inhoudelijke informatie over de applicatie.

Informatieblad Figuur A.10: Informatieblad

Aan het eind van de pagina is een link opgenomen die verwijst naar de IPLO site om vragen in te kunnen dienen. Contact: Vraag het onze experts | Informatiepunt Leefomgeving (iplo.nl)

Deze link verwijst naar: https://iplo.nl/contact/vragenformulier/ en deze link kan dan ook worden getest of inderdaad naar een bestaand adres wordt verwezen.

Deltares 39 van 39