# Alexza Jean R. Catanoy
# BSCPE 1-4
# Lab Exercise No. 1.3

#Title
print("\033[0;36m*" * 70)
print("\033[1;97mThe Vigenère Cipher".center(77)) 
print("\033[0;36m*" * 70)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4.")
print("-" * 70)

# Request for users message and key input
message = input("\033[0;33m\nKindly type in the message(all uppercase letters, no spaces): ")
key = input("\033[0;33m\nKindly type in the keyword(all uppercase letters): ")

# Apply ASCII code to the key to convert it into the appropriate letter values of 0 to 25.
key_map = [ord(i) - 65 for i in key]