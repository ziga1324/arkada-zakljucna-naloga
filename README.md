# Pametna omrežna arkada z centralnim strežnikom in mobilnim dostopom

Navodila:

 

Kandidat načrtuje in izdela pametni arkadni sistem, ki poleg lokalnega igranja omogoča povezovanje z osrednjim strežnikom, spremljanje stanja naprav, beleženje rezultatov ter večigralsko igranje preko interneta.

Sistem bo sestavljen iz arkadne naprave, osrednjega strežnika in spletne aplikacije za uporabnike ter administratorje. Vsaka arkadna naprava bo imela lasten enolični identifikator (ID), preko katerega bo registrirana v sistemu in povezana s strežnikom.

Kandidat izdela strežniški del sistema, ki omogoča:

    registracijo in upravljanje arkadnih naprav,
    spremljanje stanja posameznih arkad v realnem času,
    prikaz informacij o aktivnih igrah,
    spremljanje različic programske opreme posameznih arkad,
    evidenco prijavljenih uporabnikov,
    shranjevanje rezultatov in statistike igranja,
    vodenje lestvic najboljših igralcev,
    beleženje zgodovine odigranih iger,
    administracijo sistema preko spletnega vmesnika.

Za shranjevanje podatkov kandidat vzpostavi podatkovno bazo, v kateri hrani:

    podatke o uporabnikih,
    podatke o arkadah,
    rezultate iger,
    lestvice igralcev,
    statistične podatke o uporabi sistema,
    dnevnike dogodkov in aktivnosti.

Kandidat izdela spletno aplikacijo, ki omogoča:

    registracijo uporabnikov,
    prijavo in avtentikacijo uporabnikov,
    urejanje uporabniških profilov,
    pregled lastnih rezultatov,
    spremljanje lestvic,
    pregled zgodovine igranja,
    upravljanje sistema za administratorje.

Sistem mora podpirati igranje preko več omrežno povezanih arkad. Kandidat vzpostavi mehanizem, ki omogoča:

    komunikacijo med arkadami preko osrednjega strežnika,
    večigralsko igranje na različnih lokacijah,
    sinhronizacijo podatkov med igralci,
    prenos dogodkov v realnem času,
    evidentiranje rezultatov večigralskih tekem.

Poleg arkadnega igranja kandidat izdela tudi mobilni dostop do sistema. Na arkadni napravi se uporabnik poveže preko:

    NFC oznake,
    QR kode.

Po povezavi se uporabniku odpre spletna aplikacija PWA (Progressive Web Application), ki deluje na operacijskih sistemih Android in iOS.

Mobilna aplikacija omogoča:

    prijavo uporabnika,
    pridružitev igri,
    sodelovanje v večigralskih igrah,
    pregled rezultatov,
    komunikacijo z igralnim sistemom.

Kandidat zagotovi delovanje sistema tudi ob izpadu internetne povezave. Arkada mora omogočati:

    lokalno igranje brez internetne povezave,
    začasno lokalno shranjevanje podatkov,
    samodejno sinhronizacijo podatkov ob ponovni vzpostavitvi povezave,
    preprečevanje izgube rezultatov in uporabniških podatkov.

Kot dodatno funkcionalnost kandidat izdela navideznega AI igralnega pomočnika, ki se prikaže na arkadi v času neaktivnosti sistema. AI pomočnik lahko:

    pozdravi uporabnika,
    predstavi delovanje sistema,
    poda osnovna navodila za uporabo,
    komunicira preko besedila ali govora,
    pomaga pri zagonu igre.

Kandidat poskrbi za ustrezne varnostne mehanizme sistema:

    varno prijavo uporabnikov,
    zaščito komunikacije med arkado in strežnikom,
    zaščito podatkovne baze,
    beleženje napak in dogodkov sistema,
    izdelavo varnostnih kopij podatkov.

Ob zaključku projekta kandidat izvede testiranje:

    delovanja arkade v lokalnem načinu,
    delovanja strežniškega sistema,
    povezovanja več arkad med seboj,
    pravilnega delovanja mobilne aplikacije,
    delovanja brez internetne povezave,
    sinhronizacije podatkov po ponovni vzpostavitvi povezave,
    obremenitvenega in funkcionalnega testiranja.

 

Kandidat izdela projektno dokumentacijo, ki vključuje načrtovanje sistema, arhitekturo rešitve, opis uporabljene strojne in programske opreme, razvoj aplikacije, testiranje in evalvacijo rešitve ter kritično presojo opravljenega dela, pri čemer oceni uspešnost izvedbe, omejitve sistema in možnosti nadaljnjega razvoja.