import sys
if len(sys.argv) < 2:
    print("Usage: caesar_cracker.py <encrypted_message_file>")
    sys.exit(1)
filename = sys.argv[1]
try:
    with open(filename, "r") as f:
        encrypted_message = f.read()
except IOError:
    print("Cannot open '{}'. Sorry about that.".format(filename))
    sys.exit(1)
for shift in range(26):
    decrypted_message = ""
    for ch in encrypted_message:
        if ch.isalpha():
            if ch.isupper():
                decrypted_message += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
            else:
                decrypted_message += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        else:
            decrypted_message += ch
    print("Shift {}: {}".format(shift, decrypted_message))