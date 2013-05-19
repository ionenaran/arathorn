text = raw_input("Zu encryptender Text: ")
print ''.join(map(lambda char: chr((ord(char)+13)%ord('z')+ord('a')-1), text))
