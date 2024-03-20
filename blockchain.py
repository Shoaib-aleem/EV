from web3 import Web3
import json

# Connect to the Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set the default account for transactions
web3.eth.defaultAccount = web3.eth.accounts[0]

def connect_to_blockchain():
    # Check if connected to the Ethereum blockchain
    if web3.isConnected():
        print("Connected to Ethereum blockchain")
    else:
        print("Failed to connect to Ethereum blockchain")

def deploy_contract(contract_file, candidate_names):
    # Read the contract code
    with open(contract_file, 'r') as file:
        contract_code = file.read()

    # Compile the contract
    compiled_contract = compile_contract(contract_code)

    # Deploy the contract
    contract = web3.eth.contract(
        abi=compiled_contract['abi'],
        bytecode=compiled_contract['bin']
    )
    tx_hash = contract.constructor(candidate_names).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    contract_instance = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=compiled_contract['abi'],
    )
    return contract_instance

def compile_contract(contract_source_code):
    # Compile the contract code
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:Voting']
    return contract_interface

def register_voter(contract, voter_address):
    # Register a new voter
    tx_hash = contract.functions.registerVoter(voter_address).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

def cast_vote(contract, voter_address, candidate_index):
    # Cast a vote
    tx_hash = contract.functions.vote(candidate_index).transact({'from': voter_address})
    web3.eth.waitForTransactionReceipt(tx_hash)