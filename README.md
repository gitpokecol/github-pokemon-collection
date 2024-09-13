<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/docs/logo-white.png">
    <source media="(prefers-color-scheme: light)" srcset="/docs/logo.png">
    <img alt="logo" src="/docs/logo.png"/>
  </picture>
  <p align="center">Collect all Pokémon through GitHub contributions!<br/><a href="app.gitpokecol.org">app.gitpokecol.org</a> </p>
</div>
<div align="center">
    <a href="/README.md">english</a> · <a href="/docs/README_kr.md">한국어</a>
</div>

## Your Pokémon Collection

Go [web site](https://app.gitpokecol.org) to make your collection!

Or copy and paste this into your markdown or html.  
Replace `{username}` with your GitHub username.

```
<a href="https://app.gitpokecol.org">
  <img src="https://gitpokecol.org/pokemons/{username}" alt="{username}'s GitHub Pokemon Collection"/>
</a>
```

## Customization

You can customize your collection.

### Moving left or right

The default value is `left`.

```
https://gitpokecol.org/pokemons/{username}?face={left | right}
```

| Moving left                                                                 | Moving right                                                                  |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![Left Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?face=left) | ![Right Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?face=right) |

<details>
  <summary>Show html tags</summary>
  <div>

    # Moving left
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?face=left" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Moving right
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?face=right" alt="{username}'s GitHub Pokemon Collection"/>
    </a>

  </div>
</details>

### Backgrounds

The default background is `none`.

```
https://gitpokecol.org/pokemons/{username}?background={ abyss | badlands | beach | cave | desert | normal | plain | none }
```

| abyss                                                                                                            | badlands                                                                                                             | beach                                                                                                          | cave                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| <img alt="Abyss Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=abyss" width="100"/>   | <img alt="Badlands Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=badlands" width="100"/> | <img alt="Beach Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=beach" width="100"/> | <img alt="Cave Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=cave" width="100"/> |
| desert                                                                                                           | normal                                                                                                               | plain                                                                                                          | none                                                                                                         |
| <img alt="Desert Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=desert" width="100"/> | <img alt="Normal Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=normal" width="100"/>     | <img alt="Plain Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=plain" width="100"/> | <img alt="None Pokemon Collection" src="https://gitpokecol.org/pokemons/2jun0?background=none" width="100"/> |

<details>
  <summary>Show html tags</summary>
  <div>

    # Background abyss
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=abyss" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background badlands
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=badlands" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background beach
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=beach" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background cave
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=cave" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background desert
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=desert" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background normal
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=normal" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background plain
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=plain" alt="{username}'s GitHub Pokemon Collection"/>
    </a>
    # Background none
    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?background=none" alt="{username}'s GitHub Pokemon Collection"/>
    </a>

  </div>
</details>

### Width & Height

The default width is `300` and must be at least `250`.  
and the default height is `250` and must be at least `200`.

```
https://gitpokecol.org/pokemons/{username}?width={width}&height={height}
```

![Big Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?width=500&height=300)

<details>
  <summary>Show html tag</summary>
  <div>

    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?width=500&height=300" alt="{username}'s GitHub Pokemon Collection"/>
    </a>

  </div>
</details>

## Commit Points (CP)

Commit Points that display as "cp" represent your total GitHub contributions.
As you commit 100 times, you will receive one Pokémon randomly.
Pokémon are from Gen 1, with a total count of 151.

## Image Source

The sprites are from [www.pokencyclopedia.info](www.pokencyclopedia.info).
As [The License](/LICENSE.md) states, all Pokémon images are the property of Nintendo.
