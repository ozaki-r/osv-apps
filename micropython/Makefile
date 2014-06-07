.PHONY: module
module: micropython.so sock-server.py

micropython.so: micropython
	$(MAKE) -C micropython/osv
	cp -f micropython/osv/build/micropython.so .

sock-server.py: micropython
	cp -f micropython/examples/unix/sock-server.py .
	sed -i 's/"127.0.0.1", 8080/"0.0.0.0", 80/g' sock-server.py
	sed -i 's/\(print("Listening\)/#\1/g' sock-server.py

micropython:
	./GET

clean:
	rm -rf micropython micropython.so sock-server.py
