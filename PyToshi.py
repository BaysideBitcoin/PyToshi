#By: Justin Chase (Onename.io/juju)
#Description: Simple and Small API for interacting with a given toshi node
import json
import urllib2

#Global declaration for api version to use
VERSION='v0'

#Pre: Given a URL to query returns an Object
#Post: Returns the entire json object
def getData(URL):
	try:
		data=json.load(urllib2.urlopen(URL))
	except urllib2.HTTPError:
		return str("HTTPException")
	else:
		return data
 
#Pre: Given a TOSHINODE, returns the latest block
#Post: Returns the latest block
def getLatestBlock(TOSHINODE):
	URL=TOSHINODE+'/api/'+VERSION+'/blocks/latest'
	print URL
	return getData(URL)

#Pre: Given a TOSHINODE and the block height or the hash of a block
#Post: Returns the block data
def getBlockBy(URL,HEIGHTORHASH):
	URL=TOSHINODE+'/api/'+VERSION+'/blocks/'+ str(HEIGHTORHASH)
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No block found with given height or Hash'
	else:
		return temp

#Pre: Given a TOSHINODE and the block height or the hash of a block
#Post: Returns all the transaction data for a given block
def getBlockTransactions(URL,HEIGHTORHASH):
	URL=TOSHINODE+'/api/'+VERSION+'/blocks/'+ str(HEIGHTORHASH) + '/transactions'
#	print URL
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No transactions found at given Height or Hash'
	else:
		return temp

#Pre: Given a TOSHINODE url
#Post: Returns all the current unconfirmed transaction data for the next block (Transactions Picked up by the Toshi node)
def getTransactionsUnconfirmed(URL):
	URL=TOSHINODE+'/api/'+VERSION+'/transactions/'+ 'unconfirmed'
#	print URL
	return getData(URL)

#Pre: Given a TOSHINODE and the block height or the hash of a block
#Post: Returns all the transaction data for a given block
def getTransactionByHash(URL,HASH):
	URL=TOSHINODE+'/api/'+VERSION+'/transactions/'+ str(HASH)
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No transaction found with given Hash'
	else:
		return temp

#Pre: Given a TOSHINODE and a Bitcoin address
#Post: Returns all the balance of the Bitcoin Adddress
def getAddressBalance(URL,ADDRESS):
	URL=TOSHINODE+'/api/'+VERSION+'/addresses/'+ str(ADDRESS)
#	print URL
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No Balance or Address is not valid'
	else:
		return temp

#Pre: Given a TOSHINODE and address returns all transactions
#Post: Returns all the transaction data for a given address
def getAddressTransactions(URL,ADDRESS):
	URL=TOSHINODE+'/api/'+VERSION+'/addresses/'+ str(ADDRESS) + '/transactions'
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No transactions for associated address or invalid address'
	else:
		return temp

#Pre: Given a TOSHINODE and address returns all unspent coins
#Post: Returns all the Unspent coins for a given address
def getAddressUnspent(URL,ADDRESS):
	URL=TOSHINODE+'/api/'+VERSION+'/addresses/'+ str(ADDRESS) + '/unspent_outputs'
	temp=getData(URL)
	if (str(temp)=="HTTPException"):
		return 'No Unspent associated address or invalid address'
	else:
		return temp
		
#For Testing Purposes
TOSHINODE='https://bitcoin.toshi.io'

#latest_block=getLatestBlock(TOSHINODE)
#print latest_block

#genesisblock=getBlockBy(TOSHINODE, 1)
#print genesisblock

#transactions=getBlockTransactions(TOSHINODE, 9999999)
#print transactions

#txhash='0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098'
#transaction_data=getTransactionByHash(TOSHINODE,txhash)
#print transaction_data

#unconfirmed_transaction_data=getTransactionsUnconfirmed(TOSHINODE)
#print unconfirmed_transaction_data

#ADDRESS=''
#address_balance=getAddressBalance(TOSHINODE,ADDRESS)
#print address_balance

#address_transactions=getAddressTransactions(TOSHINODE,ADDRESS)
#print address_transactions

#address_unspent=getAddressUnspent(TOSHINODE,ADDRESS)
#print address_unspent
