from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Data Cleaning Tips Bot 🤖</h1>
    <p>Write '/tip?topic=missing' or '/tip?topic=encoding'</p>
    '''

@app.route('/tip')
def tip():
    topic = request.args.get('topic')
    if topic == 'missing':
        return '''
        <h2>Handling Missing Values</h2>
        <ul>
            <li>Use mean/median for numerical columns</li>
            <li>Use mode or "Unknown" for categorical columns</li>
            <li>Use dropna() to remove rows</li>
        </ul>
        '''
    elif topic == 'encoding':
        return '''
        <h2>Encoding Tips</h2>
        <ul>
            <li>Use Label Encoding for ordinal categories</li>
            <li>Use One-Hot Encoding for nominal categories</li>
            <li>Use get_dummies() in Pandas</li>
        </ul>
        '''
    else:
        return '<p>Topic not found. Try "missing" or "encoding".</p>'
