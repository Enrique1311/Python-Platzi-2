matches = [
  {
    "home_team": "Argentina",
    "away_team": "Brasil",
    "home_team_score": 1,
    "away_team_score": 0,
    "home_team_result": "Win",
  },
    {
    "home_team": "Colombia",
    "away_team": "Ecuador",
    "home_team_score": 2,
    "away_team_score": 2,
    "home_team_result": "Draw",
  },
    {
    "home_team": "Uruguay",
    "away_team": "Paraguay",
    "home_team_score": 3,
    "away_team_score": 1,
    "home_team_result": "Win",
  }
]
print(matches)
print(len(matches))

new_list = list(filter(lambda item: item["home_team_result"] == "Win", matches))
print(new_list)
print(len(new_list))

print(matches)
print(len(matches))
