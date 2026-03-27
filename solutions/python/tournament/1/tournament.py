def extract_match_score(match_score):
    d = {'win': 'loss',
        'draw': 'draw',
        'loss': 'win'}

    x = match_score.split(';')
    team_1 = x[0]
    team_2 = x[1]
    result = x[2]

    return (team_1,result), (team_2,d[result])

def parse_results(results):
    di = {}

    for i in results:
        teams = extract_match_score(i)

        team_1 = teams[0][0]
        team_1_result= teams[0][-1]

        team_2 = teams[1][0]
        team_2_result = teams[1][-1]

        if team_1 in di:
            di[team_1].append(team_1_result)
        else:
            di[team_1] = [team_1_result]

        if team_2 in di:
            di[team_2].append(team_2_result)
        else:
            di[team_2] = [team_2_result]

    return di

def sort_teams(clean_results):
    teams=[]
    for i in parse_results(clean_results).items():
        team = i[0]
        match_result = i[1]

        MatchesPlayed = len(match_result)
        MatchesWon = match_result.count('win')
        MatchesDrawn = match_result.count('draw')
        MatchesLost = match_result.count('loss')

        Points = 3*MatchesWon + MatchesDrawn

        teams.append((-Points, team, MatchesPlayed, MatchesWon, MatchesDrawn, MatchesLost))

    return sorted(teams)

def tally(rows):
    final_table = ['Team                           | MP |  W |  D |  L |  P',]
    for i in sort_teams(rows):
        Points, team, *match_results = i
        spaces1 = ' ' * (55-(len(team)+24))
        spaces2 = ' ' * (3 - len(str(-Points)))
        final_table.append(f'{team}{spaces1}|  {match_results[0]} |  {match_results[1]} |  {match_results[2]} |  {match_results[3]} |{spaces2}{-Points}')
    return final_table
