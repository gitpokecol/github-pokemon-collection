<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/docs/logo-white.png">
    <source media="(prefers-color-scheme: light)" srcset="/docs/logo.png">
    <img alt="logo" src="/docs/logo.png"/>
  </picture>
    <p align="center">GitHub 기여를 통해 모든 포켓몬을 모아보세요!</p>
</div>
<div align="center">
    <a href="/README.md">english</a> · <a href="/docs/README_kr.md">한국어</a>
</div>

## 포켓몬 컬렉션

[프리뷰](https://gitpokecol.org/static/preview.html)에서 쉽게 만들 수 있어요!

또는 아래의 원하는 컬렉션을 마크다운 혹은 html에 복사하여 붙여넣으세요.  
`{username}`칸은 여러분의 GitHub 유저명으로 바꿔주세요.

```
<a href="https://github.com/2jun0/github-pokemon-collection">
  <img src="https://gitpokecol.org/pokemons/{username}?face=left" alt="{username}'s GitHub Pokemon Collection"/>
</a>
```

## 커스터마이징

개성있는 컬렉션을 만들어 보세요!

### 왼쪽 혹은 오른쪽으로 움직이기

기본 값은 `left` 입니다.

```
https://gitpokecol.org/pokemons/{username}?face={left | right}
```

| 왼쪽 방향                                                                   | 오른쪽 방향                                                                   |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![Left Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?face=left) | ![Right Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?face=right) |

<details>
  <summary>html 태그 보기</summary>
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

### 배경

기본 배경 값은 `none` 입니다.

```
https://gitpokecol.org/pokemons/{username}?background={ abyss | badlands | beach | cave | desert | normal | plain | none }
```

| abyss                                                                                 | badlands                                                                                  | beach                                                                               | cave                                                                              |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ![Abyss Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=abyss)   | ![Badlands Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=badlands) | ![Beach Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=beach) | ![Cave Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=cave) |
| desert                                                                                | normal                                                                                    | plain                                                                               | none                                                                              |
| ![Desert Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=desert) | ![Normal Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=normal)     | ![Plain Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=plain) | ![None Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?background=none) |

<details>
  <summary>html 태그 보기</summary>
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

### 너비와 높이

기본 너비는 `300` 이고 너비는 `250` 보다 크거나 같아야 합니다.  
기본 높이는 `250` 이고 높이는 `200` 보다 크거나 같아야 합니다.

```
https://gitpokecol.org/pokemons/{username}?width={width}&height={height}
```

![Big Pokemon Collection](https://gitpokecol.org/pokemons/2jun0?width=500&height=300)

<details>
  <summary>html 태그 보기</summary>
  <div>

    <a href="https://github.com/2jun0/github-pokemon-collection">
      <img src="https://gitpokecol.org/pokemons/{username}?width=500&height=300" alt="{username}'s GitHub Pokemon Collection"/>
    </a>

  </div>
</details>

## 커밋 포인트 (CP)

커밋 포인트는 "cp"로 표시되며 여러분의 총 GitHub 기여 수를 나타냅니다.  
100번 커밋할 때마다 랜덤하게 포켓몬 한 마리를 받게 됩니다.  
포켓몬은 근-본 1세대 중 하나이며 총 151마리입니다.

## 이미지 출처

스프라이트 이미지는 [www.pokencyclopedia.info](www.pokencyclopedia.info)에서 가져옵니다.  
[라이선스](/LICENSE.md)에 따라, 모든 포켓몬 이미지의 저작권은 닌텐도에게 있습니다.
