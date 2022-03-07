#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>

#include <openssl/md5.h>

int main(int argc, char *argv[]) {
	if (argc == 1) {
		std::cout << "Error: No input!" << std::endl;
		return 1;
	}
	
	std::string input = argv[1];

	//std::string input = "5f4dcc3b5aa765d61d8327deb882cf99";
	std::cout << "Cracking: " << input << std::endl;
	std::cout << std::endl;
	
	std::ifstream reader("./words_out.txt");
	if (!reader.is_open()) {
		std::cerr << "Error: Unable to find hash file." << std::endl;
		return 1;
	}
	
	std::string line = "";
	while (std::getline(reader, line)) {
		unsigned char buf[MD5_DIGEST_LENGTH];
		MD5((unsigned char*)line.c_str(), line.length(), buf);
		
		std::string result = "";
		unsigned char buf2[32];
		for (int i = 0; i<16; i++) {
			sprintf((char *)buf2, "%02x", buf[i]);
			result.append((char *)buf2);
		}
		/*if (line == "password") {
			std::cout << "Found1" << std::endl;
			std::cout << "Input:   " << input << std::endl;
			std::cout << "Current: " << result << std::endl;
		}*/
		//std::cout << "Current: " << result << std::endl;
		
		// These test a few corner values to eliminate hashes more quickly
		if (result[0] != input[0]) continue;
		if (result[1] != input[1]) continue;
		if (result[MD5_DIGEST_LENGTH/2] != input[MD5_DIGEST_LENGTH/2]) continue;
		if (result[MD5_DIGEST_LENGTH-1] != input[MD5_DIGEST_LENGTH-1]) continue;
		
		if (result == input) {
			std::cout << "ANSWER FOUND! -> " << line << std::endl;
			break;
		}
	}
	
	reader.close();
	
	return 0;
}
