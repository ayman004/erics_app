import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('final.csv')
df = df.fillna('n/a')


major_must = ['g3/af111c', 'g3/af112c', 'af12/af121c', 'af12/af122c', 'g4/af21c', 'g4/af22c', 'g4/af23c', 'g5/af34c', 'af42/af422c', 'af44/af441c', 'af44/af442c', 'af45/af451c', 'af45/af453c', 'af45/af454c','g7/af51c', 'af62/af622c',
 'g10/af81c', 'g11/af91c', 'g12/af101c', 'g13/afa111c', 'g14/afa121c',
 'g15/afa131c', 'g15/afa132c', 'g15/afa133c', 'g15/afa134c', 'g16/afa141c', 'g16/afa142c', 'g16/afa143c', 'g17/afa151c',
 'cb/cb11c', 'cb23/cb231c', 'cb23/cb233c', 'cb23/cb235c', 'cb43/cb436c', 'cb44/cb441c', 'cb53/cb531c',
 'cb54/cb542c', 'g23/cb62c', 'g23/cb63c', 'g23/cb64c', 'g24/cb712c', 'g24/cb713c', 'cb72/cb721c', 'cb73/cb731c',
 'cb74/cb741c', 'cb76/cb761c', 'cb76/cb762c', 'cb76/cb763c', 'cb76/cb764c', 'cb76/cb767c', 'cb77/cb771c',
 'cb78/cb782c', 'cb79/cb791c', 'cb79/cb796c', 'fv/fv111c', 'fv/fv112c', 'fv3/fv32c', 'fv4/fv411c',
 'fv4/fv413c', 'fv4/fv421c', 'g25/fv511c', 'g25/fv512c', 'g25/fv513c', 'g25/fv514c', 'g25/fv515c', 'g25/fv516c',
 'fv52/fv521c', 'fv52/fv523c', 'fv52/fv524c', 'fv52/fv526c', 'fv53/fv531c',
 'fv54/fv541c', 'fv54/fv542c', 'fv54/fv543c', 'fv54/fv548c', 'fv54/fv549c', 'fv56/f561c', 'fv56/f562c', 'fv57/f571c', 'fv57/f572c',
 'fv58/fv581c', 'fv58/fv582c', 'fv58/fv584c', 'fv58/fv585c', 'fv58/fv586c', 'fv58/fv587c', 'fv58/fv58910c']


minor_must = ['g5/af31c','g5/af32c', 'g5/af33c', 'g6/af411c', 'g6/af412c', 'g6/af413c', 'af42/af421c','af43/af431c','af43/af432c',
 'af43/af433c','af43/af434c', 'af43/af435c','af45/af452c', 'af45/af455c' 'g8/af611c', 'af62/af621c','af62/af623c','g9/af711c', 'af73/af731c', 'g20/cb211c', 'g20/cb212c', 'g20/cb213c', 'cb22/cb221c', 'cb22/cb222c', 'cb23/cb232c', 'cb23/cb234c', 'cb3b/cb31c', 'cb3b/cb33c', 'cb3b/cb34c', 'cb3b/cb35c', 'cb3b/cb36c', 'cb3b/cb37c', 'g21/cb411c', 'cb42/cb421c', 'cb42/cb422c', 'cb42/cb423c', 'cb42/cb424c', 'cb42/cb425c','cb42/cb426c',
 'cb43/cb431c', 'cb43/cb432c', 'cb43/cb433c', 'cb43/cb434c', 'cb43/cb435c', 'cb43/cb437c', 'cb44/cb442c','cb44/cb443c',
 'cb45/cb451c','g22/cb511c', 'cb52/cb521c', 'cb52/cb522c', 'cb52/cb523c', 'cb53/cb532c', 'cb53/cb533c', 'cb53/cb534c',
 'cb53/cb535c', 'cb54/cb541c', 'g23/cb61c', 'g23/cb65c', 'g24/cb711c', 'g24/cb714c', 'cb73/cb732c', 'cb73/cb733c', 'cb73/cb734c', 'cb73/cb735c', 'cb73/cb736c',
 'cb73/cb737c', 'cb73/cb738c', 'cb75/cb751c', 'cb76/cb765c', 'cb76/cb766c', 'cb77/cb772c', 'cb77/cb773c', 'cb77/cb774c',
 'cb77/cb775c', 'cb77/cb776c', 'cb77/cb777c', 'cb77/cb778c', 'cb77/cb779c', 'cb77/cb7710c', 'cb77/cb7711c', 'cb77/cb7712c',
 'cb77/cb7713c', 'cb77/cb7714c', 'cb77/cb7715c', 'cb78/cb781c', 'cb78/cb783c', 'cb78/cb784c', 'cb79/cb792c', 'cb79/cb793c',
 'cb79/cb794c', 'cb79/cb795c', 'cb710/cb7101c', 'cb710/cb7112c', 'cb8/cb81c', 'cb8/cb82c', 'cb8/cb84c', 'fv2/fv211c', 'fv2/fv212c', 'fv3/fv33c', 'fv4/fv412c',
 'fv4/fv414c', 'fv43/fv431c', 'fv52/fv522c', 'fv54/fv544c', 'fv54/fv545c', 'fv54/fv546c',
 'fv54/fv5410c', 'fv55/fv551c', 'fv56/fv563c', 'fv58/fv583c', 'fv58/fv588c', 'fv58/fv589c']


df['major_no'] = (df.loc[:,major_must]=='no').sum(axis=1)
df['major_yes'] = (df.loc[:,major_must]=='yes').sum(axis=1)

df['minor_no'] = (df.loc[:,minor_must] == 'no').sum(axis=1)
df['minor_yes'] = (df.loc[:,minor_must] == 'yes').sum(axis=1)
df['minor_n/a'] = (df.loc[:,minor_must] == 'n/a').sum(axis=1)

y = 113 - df['minor_n/a']
df['Minor_Score'] = ((y - round(y * 0.05) ) / y ) * 100 

major_no = sum((df.loc[:,major_must]=='no').sum(axis=0))
major_yes = sum((df.loc[:,major_must]=='yes').sum(axis=0))
minor_no = sum((df.loc[:,minor_must] == 'no').sum(axis=0))
minor_yes = sum((df.loc[:,minor_must] == 'yes').sum(axis=0))
minor_na = sum((df.loc[:,minor_must] == 'n/a').sum(axis=0))

col = df.columns.tolist()
s_col = col[-6:] + col[:-6]
df = df[s_col]
app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
trace1 = go.Bar(
x=['Major Must', 'Minor Must'],
y=[major_yes, minor_yes],
name='Yes'
)
trace2 = go.Bar(
	x=['Major Must', 'Minor Must'],
	y=[major_no, minor_no],
	name='No'
)
trace3 = go.Bar(
	x=[ 'Minor Must'],
	y=[minor_na],
	name='n/a'
)
data = [trace1, trace2,trace3]
 
app.layout = html.Div(children=[
	 
    
    html.H4(children='Table data'),
	html.Div([
        dt.DataTable(
            rows=df.to_dict('records'),
            columns=df.columns,
            row_selectable=True,
            filterable=True,
            sortable=True,
            selected_row_indices=list(df.index),  # all rows selected by default
            id='product-datatable'
        )]
		),
		dcc.Graph(
		figure=go.Figure(
		data = data,
		layout=go.Layout(title='Score Summary',barmode='group')),
		style={'height': 600},
		id='my-graph')
		
	
	
])




if __name__ == '__main__':
	#address = '192.168.0.129'
	app.run_server()