def fetch_words():
	appendwords=[]
	words = ['cat', 'window', 'defenestrate']
	
	for listitems in words:
		
		
			appendwords.append(listitems)
	
	return appendwords
def print_words(appendwords):
	for word in appendwords:
		print(word)
		
def main():
	words=fetch_words()
	print_words(words)

if __name__ == '__main__':
	main()
