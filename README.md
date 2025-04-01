# Pokedex-AI
Deep Learning Model that aims to classify everyone of the 151 pokemons from the first generation.

## Goal
My goal is to **design**, **train** and **deploy** a **Deep Learning model** that can classify the 151 pokémon of the first generation, regardless of whether it is **art work**, **hand drawing**, **anime scenes** or **stuffed animals** and **figurines**.

Some of the use cases I want to give to the model are: A **mobile application** that, when capturing images with the camera, can determine which pokémon it is. The other is quite similar, but instead of a mobile application, **an Arduino / Raspberry Pi system**. That is, a **Real Pokedex**. But before I start with these two projects, I want to complete at least **80%** of the pokémon (_121/151_).

&nbsp;

## How am I doing it?
To achieve this, the first thing I do is, with an automated script, obtain online images of the pokémon in question, unfortunately several services like Google Images or Pinterest, make it quite difficult when doing **WebScraping** (at least for my current knowledge), therefore, for certain pokémon I must manually search for images, or check that the images extracted by the script are not dirty.

### Technologies
I am using Python, Tensorflow and Keras. In order to deploy the model and consume it as API, I am using FastAPI.

### Dataset
**Unfortunately**, most of the Datasets that I found online are images that do not serve the purpose of the model, since they are images without visual noise, without background, and generally of repeated sprites. Given this problem, I am creating the Dataset myself, for the moment, a small one with **350 images per class**.

&nbsp;

## Actuality
I am currently in the eighth architecture of the Deep Learning model. Previously I had to discard quite a few because they did not generalize or classify well or did not meet my **self-imposed 75% accuracy criterion**. Model number 8 has **84% accuracy** and currently classifies correctly the pokémon you can see below (at the `to-do` section), including hand drawings, art work or anime scenes.

&nbsp;

## TO-DO
### Icon Meaning
| ⬛ | 🟨 | 🟩 |
| :---: | :---: | :---: |
| Uninitiated | In process | Done |

&nbsp;

### Pokédex List
| **Dex number** | **Pokémon** | **Img Amount** | **Status** |
| :--- | :---: | :---: | ---: |
| 1 | Bulbasaur | 350 | 🟩 |
| 2 | Ivysaur | 350 | 🟩 |
| 3 | Venusaur | 350 | 🟩 |
| 4 | Charmander | 350 | 🟩 |
| 5 | Charmeleon | 350 | 🟩 |
| 6 | Charizard | 350 | 🟩 |
| 7 | Squirtle | 350 | 🟩 |
| 8 | Wartortle | 350 | 🟩 |
| 9 | Blastoise | 350 | 🟩 |
| 10 | Caterpie | 350 | 🟩 |
| 11 | Metapod | 350 | 🟩 |
| 12 | Butterfree | 350 | 🟩 |
| 13 | Weedle | 350 | 🟩 |
| 14 | Kakuna | 350 | 🟩 |
| 15 | Beedrill | 350 | 🟩 |
| 16 | Pidgey | 350 | 🟩 |
| 17 | Pidgeotto | 350 | 🟩 |
| 18 | Pidgeot | 350 | 🟩 |
| 19 | Rattata | 350 | 🟩 |
| 20 | Raticate | 0 | 🟨 |
| 21 | Spearow | 0 | ⬛ |
| 22 | Fearow | 0 | ⬛ |
| 23 | Ekans | 0 | ⬛ |
| 24 | Arbok | 0 | ⬛ |
| 25 | Pikachu | 0 | ⬛ |
| 26 | Raichu | 0 | ⬛ |
| 27 | Sandshrew | 0 | ⬛ |
| 28 | Sandslash | 0 | ⬛ |
| 29 | Nidoran♀ | 0 | ⬛ |
| 30 | Nidorina | 0 | ⬛ |
| 31 | Nidoqueen | 0 | ⬛ |
| 32 | Nidoran♂ | 0 | ⬛ |
| 33 | Nidorino | 0 | ⬛ |
| 34 | Nidoking | 0 | ⬛ |
| 35 | Clefairy | 0 | ⬛ |
| 36 | Clefable | 0 | ⬛ |
| 37 | Vulpix | 0 | ⬛ |
| 38 | Ninetales | 0 | ⬛ |
| 39 | Jigglypuff | 0 | ⬛ |
| 40 | Wigglytuff | 0 | ⬛ |
| 41 | Zubat | 0 | ⬛ |
| 42 | Golbat | 0 | ⬛ |
| 43 | Oddish | 0 | ⬛ |
| 44 | Gloom | 0 | ⬛ |
| 45 | Vileplume | 0 | ⬛ |
| 46 | Paras | 0 | ⬛ |
| 47 | Parasect | 0 | ⬛ |
| 48 | Venonat | 0 | ⬛ |
| 49 | Venomoth | 0 | ⬛ |
| 50 | Diglett | 0 | ⬛ |
| 51 | Dugtrio | 0 | ⬛ |
| 52 | Meowth | 0 | ⬛ |
| 53 | Persian | 0 | ⬛ |
| 54 | Psyduck | 0 | ⬛ |
| 55 | Golduck | 0 | ⬛ |
| 56 | Mankey | 0 | ⬛ |
| 57 | Primeape | 0 | ⬛ |
| 58 | Growlithe | 0 | ⬛ |
| 59 | Arcanine | 0 | ⬛ |
| 60 | Poliwag | 0 | ⬛ |
| 61 | Poliwhirl | 0 | ⬛ |
| 62 | Poliwrath | 0 | ⬛ |
| 63 | Abra | 0 | ⬛ |
| 64 | Kadabra | 0 | ⬛ |
| 65 | Alakazam | 0 | ⬛ |
| 66 | Machop | 0 | ⬛ |
| 67 | Machoke | 0 | ⬛ |
| 68 | Machamp | 0 | ⬛ |
| 69 | Bellsprout | 0 | ⬛ |
| 70 | Weepinbell | 0 | ⬛ |
| 71 | Victreebel | 0 | ⬛ |
| 72 | Tentacool | 0 | ⬛ |
| 73 | Tentacruel | 0 | ⬛ |
| 74 | Geodude | 0 | ⬛ |
| 75 | Graveler | 0 | ⬛ |
| 76 | Golem | 0 | ⬛ |
| 77 | Ponyta | 0 | ⬛ |
| 78 | Rapidash | 0 | ⬛ |
| 79 | Slowpoke | 0 | ⬛ |
| 80 | Slowbro | 0 | ⬛ |
| 81 | Magnemite | 0 | ⬛ |
| 82 | Magneton | 0 | ⬛ |
| 83 | Farfetch’d | 0 | ⬛ |
| 84 | Doduo | 0 | ⬛ |
| 85 | Dodrio | 0 | ⬛ |
| 86 | Seel | 0 | ⬛ |
| 87 | Dewgong | 0 | ⬛ |
| 88 | Grimer | 0 | ⬛ |
| 89 | Muk | 0 | ⬛ |
| 90 | Shellder | 0 | ⬛ |
| 91 | Cloyster | 0 | ⬛ |
| 92 | Gastly | 0 | ⬛ |
| 93 | Haunter | 0 | ⬛ |
| 94 | Gengar | 0 | ⬛ |
| 95 | Onix | 0 | ⬛ |
| 96 | Drowzee | 0 | ⬛ |
| 97 | Hypno | 0 | ⬛ |
| 98 | Krabby | 0 | ⬛ |
| 99 | Kingler | 0 | ⬛ |
| 100 | Voltorb | 0 | ⬛ |
| 101 | Electrode | 0 | ⬛ |
| 102 | Exeggcute | 0 | ⬛ |
| 103 | Exeggutor | 0 | ⬛ |
| 104 | Cubone | 0 | ⬛ |
| 105 | Marowak | 0 | ⬛ |
| 106 | Hitmonlee | 0 | ⬛ |
| 107 | Hitmonchan | 0 | ⬛ |
| 108 | Lickitung | 0 | ⬛ |
| 109 | Koffing | 0 | ⬛ |
| 110 | Weezing | 0 | ⬛ |
| 111 | Rhyhorn | 0 | ⬛ |
| 112 | Rhydon | 0 | ⬛ |
| 113 | Chansey | 0 | ⬛ |
| 114 | Tangela | 0 | ⬛ |
| 115 | Kangaskhan | 0 | ⬛ |
| 116 | Horsea | 0 | ⬛ |
| 117 | Seadra | 0 | ⬛ |
| 118 | Goldeen | 0 | ⬛ |
| 119 | Seaking | 0 | ⬛ |
| 120 | Staryu | 0 | ⬛ |
| 121 | Starmie | 0 | ⬛ |
| 122 | Mr. Mime | 0 | ⬛ |
| 123 | Scyther | 0 | ⬛ |
| 124 | Jynx | 0 | ⬛ |
| 125 | Electabuzz | 0 | ⬛ |
| 126 | Magmar | 0 | ⬛ |
| 127 | Pinsir | 0 | ⬛ |
| 128 | Tauros | 0 | ⬛ |
| 129 | Magikarp | 0 | ⬛ |
| 130 | Gyarados | 0 | ⬛ |
| 131 | Lapras | 0 | ⬛ |
| 132 | Ditto | 0 | ⬛ |
| 133 | Eevee | 0 | ⬛ |
| 134 | Vaporeon | 0 | ⬛ |
| 135 | Jolteon | 0 | ⬛ |
| 136 | Flareon | 0 | ⬛ |
| 137 | Porygon | 0 | ⬛ |
| 138 | Omanyte | 0 | ⬛ |
| 139 | Omastar | 0 | ⬛ |
| 140 | Kabuto | 0 | ⬛ |
| 141 | Kabutops | 0 | ⬛ |
| 142 | Aerodactyl | 0 | ⬛ |
| 143 | Snorlax | 0 | ⬛ |
| 144 | Articuno | 0 | ⬛ |
| 145 | Zapdos | 0 | ⬛ |
| 146 | Moltres | 0 | ⬛ |
| 147 | Dratini | 0 | ⬛ |
| 148 | Dragonair | 0 | ⬛ |
| 149 | Dragonite | 0 | ⬛ |
| 150 | Mewtwo | 350 | 🟩 |
| 151 | Mew | 350 | 🟩 |

