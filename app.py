from flask import Flask, render_template, request, redirect, url_for
import blockchain

app = Flask(__name__)

# Connect to the Ethereum blockchain
blockchain.connect_to_blockchain()

# Deploy the Voting contract
voting_contract = blockchain.deploy_contract('Voting.sol', ['Candidate1', 'Candidate2'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Register the voter
        voter_address = request.form['address']
        blockchain.register_voter(voting_contract, voter_address)
        return redirect(url_for('vote'))
    return render_template('register.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        # Cast the vote
        voter_address = request.form['address']
        candidate_index = int(request.form['candidate'])
        blockchain.cast_vote(voting_contract, voter_address, candidate_index)
        return redirect(url_for('results'))
    return render_template('vote.html', candidates=voting_contract.functions.getCandidates().call())

@app.route('/results')
def results():
    # Get the voting results
    winner = voting_contract.functions.getWinner().call()
    return render_template('result.html', winner=winner)

if __name__ == '__main__':
    app.run(debug=True)