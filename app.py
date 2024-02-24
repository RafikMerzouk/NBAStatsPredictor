from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from nba_api.stats.static import players
from Tables.player import Player
from Tables import Base, connection_string
from nba_api.stats.endpoints import commonplayerinfo
import time
import requests


def get_team_id(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_info_df = player_info.get_data_frames()[0]
    team_id = player_info_df.loc[0, 'TEAM_ID']
    return team_id

def get_team_id_with_retry(player_id, retries=3, delay=5):
    for i in range(retries):
        try:
            return get_team_id(player_id)
        except requests.exceptions.ReadTimeout:
            print(f"Read timeout occurred for player_id {player_id}, retrying in {delay}s...")
            time.sleep(delay)

engine = create_engine(connection_string)

# Création de la table
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Récupération des données des joueurs
current_players = players.get_active_players()
i = 0
for player in current_players:
    player_id = int(player['id'])
    full_name = player['full_name']
    print(f'player {i + 1} / {len(current_players)} players')
    # Récupération de l'ID de l'équipe
    team_id = int(get_team_id_with_retry(player_id))
    
    new_player = Player(id=player_id, full_name=full_name, team_id=team_id)
    session.add(new_player)
    i += 1
    try :
        session.commit()
    except :
        continue
