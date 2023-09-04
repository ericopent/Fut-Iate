import pandas as pd
import streamlit as st
import datetime

client_json = {
  "type": "service_account",
  "project_id": "futicrj",
  "private_key_id": "7dc67f095b6bb76eae099a9981a44af552aae703",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPJuIo+yg/0Ocr\n7vCtJT2sefNzR54AGTFFP6JSS0OigE52/Dlrlf8xewqzxICMxge9IKPOgbEeLnI7\nnZiU+G9UoLUlXiuFOL02J1UC7KikYdIzegHtinuzLcDJuCiLPM0dRSqFVLD43YHB\nPdjW2yGeU0NUpZCP+yXNSq2UK82MstLE07UkNIt4smXi9xWc+qHlAf/3PrPosUhW\nGogI1NehoOr/JFSNGBoYC3OJljlb4nKp4+7eY2pbxyA/Qti46iYuin/gQfJnL1j6\nmCcmuno3GWcnIflA9JY0iYbAuYv7OTlAIn8Ph2FPCxznFVQrSLzFENiTTPvtIiHR\nnz1WaG7BAgMBAAECggEAQ6poYsmTvrC+6ods36oUCMR3JRdmQZL5GK0uGSKTr7+o\noc5G9WE0UFXoS4trEFDZk0pXp6uOjxTN5LJYdoTmXOb39QJbRfOgPtG/P6rNdZCs\niHsYqR68xG00FdBNkhnkyGRg/NeKzWgRq+1HaPuAckaxbjN80sNPeE0mAQoD5Sqn\nfESh3dyhtT/eCfbQX1w+nLzfnNr2alURJMm5Ga6X+6PCE558z9vNVrsBUsylbRMZ\nAEGKPluSVviYaiGqqkqQ3x5ayOFV/DNK3We2XjxV7uuo3ChflzTBBxSOzKXoPU42\ndLnUEOdXXPVIuePiXZ4YZE36feyui1DscCG5RbsRPwKBgQD8wUIWQDMDJ4Qri5H8\nmDTtzumdOj0Hj0dZ/OWsvnF3VdXBI0IXqy9Dlcn4T9+TiDw3nlfNhT5wJNOFOdZO\nvWO/3f1pxekxlNvW65tbQGEofn92ZZvYuhtdkOPsy9XsPPrsXOaUJKbibBidCQxW\nSWi/f8xlG3Fu870sfvKMaKMsLwKBgQDRz71WzKIdiSg1mI1aC+Xp73CXw+TI0BJM\nzD+E1RFW4cqOmSGL6uORYHOAt3mAawx34qYp7HNWrsOKPy0dKtXzfl37tr5XdiEg\nXKBrnHYZ498tJ3d7IoHZpkPG5Namg9nXKFzAgpg3OmEpGdNwV6XiG7OSOG8cr0Is\nlpEM5UaoDwKBgQCT4ltRe4SdXtyVQddLzJ6DWaIUTUPyDWH5A+A5/z+STBWCKKf+\nAznnOFfwwoMU5gwdmrbS2BgdM17TP3Dlpyga1b70yUhUqz0pdbbzYCq4r7LSSkcy\nOknSp/jDzsu+qjtCWmTK3tsJ9ac9ElM2lUMFcLfdnH31JgVUaH5vqrV2HwKBgDNd\nFBEnz5hDd6CHVDNzLjny8DF3N48hwRkj93jhYHlQlXILcvb57fQtFJmyUQBrNIY0\n6lDhHetepWg2xyiYz//oM8HnnvlyZfGyO2OczhzQeFZpjwqKDBfoaDdM1m+1X6MY\nsnw+fF0o4ZhaRjT+gBG2jmOBhVIUZbLcuW3aw01pAoGBAOSyuQtrVYczK4WXIMeq\n6Q6lTST41ilQcY/rK35y+8Ml9lk4/lsFbT3JHJvQyOfgEll9hgYijFE5D/LXPE+v\npmqAARXxSllM0Sj39j8OvHK8y4nHAuMEZkorfm5ypUo8zjCzUrVWjm3d+geraX0/\n2n4OxPSJkOFrWL2tm5juPQM6\n-----END PRIVATE KEY-----\n",
  "client_email": "futicrj@futicrj.iam.gserviceaccount.com",
  "client_id": "115944344368992571371",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/futicrj%40futicrj.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

import gspread
from gspread_dataframe import set_with_dataframe
st.set_page_config(
    layout="wide",
    page_title = 'Fut Iate',
    page_icon='https://www.icrj.com.br/iate/images/logo/logo60.png')
    
st.markdown("""
    <style>
    p {
        font-size:20px;
        place-items: center;

    }
    
    .st-af {
        font-size: 19px;
    }
    
    .css-10trblm.eqr7zpz0 {
        
        font-size:25px;
    }
    
    code {
        color: rgb(9, 171, 59);
        overflow-wrap: break-word;
        font-size: 20px;
    }   
    
    .stMarkdown {
    display: grid;
    place-items: center;
    }
    
    button{
        display: grid;
        place-items: center;
        
    }
    
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] {
        font-size:24px;
        text-align: center;
        place-items: center;

    }
    
    .css-q8sbsg.eqr7zpz4 {
        
        font-size:24px;
        text-align: center;
        place-items: center;
        
    }
    
    .css-10trblm.eqr7zpz0 {
        
        font-size:40px;
        text-align: center;
        place-items: center;
        
    }
    
    .css-3mmywe.e15ugz7a0 {
        
        place-items: center;
        align-content: center;
        
    }
    
    h2 {text-align: center;}
    </style>
    """, unsafe_allow_html=True)

def read_data(sheet = "FutIate", tab = "Ranking"):
    
    gc = gspread.service_account(filename=r"I:\Análise de Dados\Erico\service-account-key.json")

    sh = gc.open(sheet)    
    
    worksheet = sh.worksheet(tab)

    df = pd.DataFrame(worksheet.get_all_records())

    return(df)

def write_data (dados, data, nome, gols, assists, presença, sheet = "FutIate", tab = "Ranking"):
    
    df = [{
        
        'DATA': data,
        'NOME': nome,
        'GOLS': gols,
        'ASSISTÊNCIAS': assists,
        'PRESENÇA': presença
    }]
    
    gc = gspread.service_account(filename=r"I:\Análise de Dados\Erico\service-account-key.json")

    sh = gc.open(sheet)    
    
    worksheet = sh.worksheet(tab)
    
    df = pd.DataFrame(df)    
    
    db = pd.concat([dados, df])
    db['DATA'] = pd.to_datetime(db['DATA'])
    
    db['DATA'] = db['DATA'].apply(lambda x: x.strftime("%d/%m/%Y"))
    
    set_with_dataframe(worksheet, db)
    # pd.concat([dados, df])
    return()

dados = read_data(sheet = "FutIate", tab = "Ranking").drop_duplicates(subset=['DATA', 'NOME'], keep = 'last')

dados['DATA'] = pd.to_datetime(dados['DATA'])

st.markdown(
    "# Fut Iate :crown: :trophy:"
)




def stable_matching(ranking):
    team_size = 5
    players = ranking['Nome'].tolist()
    scores = ranking['Score'].tolist()
    
    n = len(players)
    proposals = [-1] * n
    engaged = [-1] * n
    preferences = {players[i]: [(scores[i], i) for i in range(n)] for i in range(n)}
    
    while -1 in engaged:
        free_player = engaged.index(-1)
        for _, preferred_player_idx in preferences[players[free_player]]:
            if proposals[preferred_player_idx] == -1:
                engaged[free_player] = preferred_player_idx
                proposals[preferred_player_idx] = free_player
                break
            else:
                current_partner_idx = proposals[preferred_player_idx]
                if preferences[players[preferred_player_idx]].index((scores[free_player], free_player)) < preferences[players[preferred_player_idx]].index((scores[current_partner_idx], current_partner_idx)):
                    engaged[free_player] = preferred_player_idx
                    proposals[preferred_player_idx] = free_player
                    engaged[current_partner_idx] = -1
                    break
            
    teams = []
    substitutes = []
    
    for i in range(0, n, team_size):
        
        team_players = players[i:i+team_size]
        
        if len(team_players) < team_size:
            substitutes.extend(team_players)
        else:
            teams.append(team_players)
    
    st.markdown(f"**Time 1: {' | '.join(teams[0])}**")
    st.markdown(f"**Time 2: {' | '.join(teams[1])}**")
    st.markdown(f"**Substitutos: {' | '.join(substitutes)}**")
    return teams, substitutes
    
import random

def form_random_teams_with_substitutes(ranking):
    
    team_size = 5
    players = ranking['Nome'].tolist()
    
    random.shuffle(players)  # Shuffle the list of players randomly
    num_teams = len(players) // team_size
    teams = [players[i:i+team_size] for i in range(0, len(players), team_size)]
    substitutes = players[num_teams * team_size:]  # Any remaining players are substitutes

    st.markdown(f"**Time 1: {' | '.join(teams[0])}**")
    st.markdown(f"**Time 2: {' | '.join(teams[1])}**")
    st.markdown(f"**Substitutos: {' | '.join(substitutes)}**")

    return teams, substitutes

def head2head(dados, person1, person2, metrica):
    
    person1_db = dados[dados['NOME'] == person1]
    person2_db = dados[dados['NOME'] == person2]
    
    person2_ratio = person2_db[metrica].sum()/person2_db.PRESENÇA.sum()
    person1_ratio = person1_db[metrica].sum()/person2_db.PRESENÇA.sum()

    if (person2_ratio < person1_ratio):
        st.markdown(f"**{metrica.title()}:\n {person1.title()} | {person1_db[metrica].sum()} {metrica} em {person1_db['PRESENÇA'].sum()} dia(s) :crown:**")

    elif (person2_ratio > person1_ratio):
        st.markdown(f"**{metrica.title()}:\n {person2.title()} | {person2_db[metrica].sum()} {metrica} em {person2_db['PRESENÇA'].sum()} dia(s) :crown:**")

    elif (person2_ratio == person1_ratio):
        st.markdown(f"**{metrica.title()}:\n EMPATE**")

def RankingTotal (dados, pesoGols, pesoAssists, pesoPresença):
    
    
    if(pesoGols + pesoAssists + pesoPresença != 1):
        st.error('Pesos não somam 1')
    else:
        
        result = dados.groupby('NOME').apply(lambda x: x.GOLS.sum()*pesoGols + x.PRESENÇA.sum()*pesoPresença + x.ASSISTÊNCIAS.sum()*pesoAssists).sort_values(ascending=False)
        
        result = result.to_frame().reset_index()
        
        result.columns = ['NOME', 'Score']
        
        result = pd.merge(dados.groupby('NOME').sum(['GOLS', 'ASSISTÊNCIAS', 'PRESENÇA']), result, on='NOME')

        def format_score(score):
            return f"{score:.2f}"

        result.sort_values('Score', inplace=True, ascending=False)
        result.reset_index(inplace = True, drop=True)
        result['Posição'] = result.index + 1
        result = result[['NOME', 'GOLS', 'ASSISTÊNCIAS', 'PRESENÇA', 'Score', 'Posição']]
        
        result.columns = ['Nome', 'Gols', 'Assistências', 'Presença','Score', 'Posição']
        result['Score'] = result['Score'].apply(lambda x: round(x, 2))  
        view = result.style.hide(axis="index")
        
        view.set_table_styles([
        {'selector': "th", 'props': [("font-weight", "bold"), ("text-transform", "capitalize")]},])
        
        view.format(lambda x: f"<i title='tooltip'>{x}</i>", 'Posição')
            
        st.markdown(view.to_html(), unsafe_allow_html=True)
        return(result)

with st.sidebar:
    
    data = st.date_input('Data', value=datetime.datetime.today())
    nome = st.selectbox('Nome', options=dados['NOME'].unique())
    gols = st.number_input('Gols', min_value=0., max_value=100., value = 0., step = 1.)
    assists = st.number_input('Assistências', min_value=0., max_value=100., value = 0.,step = 1.)
    presença = st.number_input('Presença', min_value=0., max_value=100.,value = 0.,step = 1.)
    bt = st.button('ADD dados')
    if bt:
        write_data(dados.drop_duplicates(subset=['DATA', 'NOME'], keep = 'last'), data=data,nome = nome, gols=gols, assists=assists, presença=presença, sheet = "FutIate", tab = "Ranking")
        dados = read_data(sheet='FutIate', tab='Ranking').drop_duplicates(subset=['DATA', 'NOME'], keep = 'last')
    
tab1, tab2 = st.tabs(['# Ranking All-Time', "# Ranking Mensal"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        pesoGols = st.number_input('Peso de Gols', min_value=0.,max_value=1., value = 0.2)
    with col2:
        pesoAssistências = st.number_input('Peso de Assistências', min_value=0.,max_value=1.,value = 0.2)
    with col3:
        pesoPresença = st.number_input('Peso de Presença', min_value=0.,max_value=1.,value = 0.6)
        
    ranking = RankingTotal(dados,pesoGols,pesoAssistências,pesoPresença)

with tab2:

    dateRef = st.date_input('Data de Referência', pd.to_datetime(dados['DATA']).unique()[-1])
    
    dt = dados[dados['DATA'].apply(lambda x: pd.to_datetime(x).month) == dateRef.month]
    
    st.write('Mês de Referência: ', dateRef.strftime('%m-%Y').title())
    
    col1, col2, col3 = st.columns(3)
    with col1:
        pesoGols1 = st.number_input('Peso de Gols - mensal', min_value=0.,max_value=1., value = 0.4)
    with col2:
        pesoAssistências2 = st.number_input('Peso de Assistências - mensal', min_value=0.,max_value=1.,value = 0.3)
    with col3:
        pesoPresença3 = st.number_input('Peso de Presença - mensal', min_value=0.,max_value=1.,value = 0.3)
    
    if (dt.empty):
        st.error('Ainda não tiveram partidas esse Mês')
    else:
        ranking = RankingTotal(dt,pesoGols1,pesoAssistências2,pesoPresença3)
    
with st.sidebar:
    with st.expander("# Head-To-Head"):
        st.markdown("## Head-to-head :rage:")
        with st.form(key="head2head"):
            person1 = st.selectbox("Player 1: ", dados['NOME'].unique())
            person2 = st.selectbox("Player 2: ", [el for el in dados['NOME'].unique() if el != person1])
            submit_head2head = st.form_submit_button(label="Submit")
            
            if(submit_head2head):
                head2head(dados, person1, person2, 'GOLS')
                head2head(dados, person1, person2, 'PRESENÇA')
                head2head(dados, person1, person2, 'ASSISTÊNCIAS')
                
    with st.expander('# Seletor de Times'):
        st.markdown("## Usando Stable Matching de Gale-Shapley :computer:")
        with st.form(key="Gale-Shapley"):
            submit_stable = st.form_submit_button(label="Bater Time")
            if(submit_stable):
                stable_matching(ranking)
            
        st.markdown("## Random Selector :1234:")
        with st.form(key="Random"):

            submit_random = st.form_submit_button(label="Time Random")
            if(submit_random):
                
                form_random_teams_with_substitutes(ranking)
