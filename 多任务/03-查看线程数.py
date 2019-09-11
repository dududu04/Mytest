import threading

def test1():
	for i in range(5):
		print("---test1----%d" % i)

def test2():
	for i in range(5):
		print("---test2----%d" % i)

def main():
	t1 = threading.Thread(target=test1)
	t2 = threading.Thread(target=test2)

	t1.start()
	t2.start()

	print(threading.enumerate())

if __name__ == "__main__":
	main()
